#!/usr/bin/env python3
"""One-off migration for publication/arXiv links in canonical resources.csv.

The final schema stays in data/resources.csv. This helper is temporary and must
be removed after the migration lands. It never writes partial/ambiguous results.
"""

from __future__ import annotations

import csv
import functools
import html
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESOURCE_PATH = ROOT / "data" / "resources.csv"
ARXIV_ONLY_VENUES = {"", "arXiv", "Technical Report"}
USER_AGENT = "awesome-creative-graphic-design-generation/1.0 bibliographic migration"
MAX_WORKERS = 6

PUBLICATION_OVERRIDES: dict[str, str] = {}
ARXIV_OVERRIDES: dict[str, str] = {
    "T-Stars-Poster": "https://arxiv.org/abs/2501.14316",
}

PREFERRED_PUBLICATION_HOSTS = (
    "doi.org",
    "openaccess.thecvf.com",
    "proceedings.mlr.press",
    "aclanthology.org",
    "openreview.net",
    "ojs.aaai.org",
    "ijcai.org",
    "dl.acm.org",
    "ieeexplore.ieee.org",
    "link.springer.com",
)


def normalize_title(value: str) -> str:
    value = html.unescape(re.sub(r"<[^>]+>", " ", value))
    value = value.casefold().replace("–", "-").replace("—", "-")
    return re.sub(r"[^a-z0-9]+", " ", value).strip()


def is_arxiv_url(url: str) -> bool:
    parsed = urllib.parse.urlparse(url)
    return (
        parsed.scheme == "https"
        and (parsed.hostname or "").casefold() == "arxiv.org"
        and parsed.path.startswith("/abs/")
    )


def arxiv_id(url: str) -> str:
    return urllib.parse.urlparse(url).path.removeprefix("/abs/").split("v", 1)[0]


def semantic_scholar_id(url: str) -> str | None:
    if is_arxiv_url(url):
        return f"ARXIV:{arxiv_id(url)}"
    parsed = urllib.parse.urlparse(url)
    if (parsed.hostname or "").casefold() == "doi.org":
        doi = parsed.path.lstrip("/")
        return f"DOI:{doi}" if doi else None
    if (parsed.hostname or "").casefold() == "aclanthology.org":
        acl_id = parsed.path.strip("/")
        return f"ACL:{acl_id}" if acl_id else None
    return None


def request_json(url: str) -> dict:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    last_error: Exception | None = None
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=8) as response:
                return json.loads(response.read().decode("utf-8"))
        except Exception as exc:
            last_error = exc
            time.sleep(0.75 * (attempt + 1))
    assert last_error is not None
    raise last_error


def semantic_scholar_batch(ids: list[str]) -> dict[str, dict]:
    if not ids:
        return {}
    url = (
        "https://api.semanticscholar.org/graph/v1/paper/batch?"
        + urllib.parse.urlencode({"fields": "title,externalIds"})
    )
    body = json.dumps({"ids": ids}).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=body,
        headers={
            "User-Agent": USER_AGENT,
            "Content-Type": "application/json",
        },
        method="POST",
    )
    last_error: Exception | None = None
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                records = json.loads(response.read().decode("utf-8"))
            return {
                requested_id: record
                for requested_id, record in zip(ids, records, strict=True)
                if record is not None
            }
        except Exception as exc:
            last_error = exc
            time.sleep(1.0 * (attempt + 1))
    assert last_error is not None
    raise last_error


@functools.lru_cache(maxsize=None)
def dblp_hits(query: str) -> tuple[dict, ...]:
    url = "https://dblp.org/search/publ/api?" + urllib.parse.urlencode(
        {"q": query, "format": "json", "h": 30}
    )
    payload = request_json(url)
    hits = payload.get("result", {}).get("hits", {}).get("hit", [])
    if isinstance(hits, dict):
        hits = [hits]
    return tuple(hit.get("info", {}) for hit in hits)


def info_title(info: dict) -> str:
    return " ".join(str(info.get("title", "")).split())


def info_ee(info: dict) -> list[str]:
    ee = info.get("ee", [])
    if isinstance(ee, str):
        ee = [ee]
    return [str(url) for url in ee]


def arxiv_from_info(info: dict) -> str | None:
    for url in info_ee(info):
        match = re.search(r"https?://arxiv\.org/abs/([^/?#]+)", url)
        if match:
            return f"https://arxiv.org/abs/{match.group(1).split('v', 1)[0]}"
    key = str(info.get("key", ""))
    match = re.fullmatch(r"journals/corr/abs-(.+)", key)
    if match:
        return f"https://arxiv.org/abs/{match.group(1)}"
    return None


def publication_from_info(info: dict) -> list[str]:
    return [
        url
        for url in info_ee(info)
        if url.startswith("https://") and not is_arxiv_url(url)
    ]


def score_title(target: str, candidate: str) -> int:
    target_norm = normalize_title(target)
    candidate_norm = normalize_title(candidate)
    if not target_norm or not candidate_norm:
        return 0
    if target_norm == candidate_norm:
        return 100
    if target_norm in candidate_norm or candidate_norm in target_norm:
        return 55
    return 0


def publication_from_external_ids(external_ids: dict) -> str | None:
    doi = external_ids.get("DOI")
    if doi:
        return f"https://doi.org/{doi}"
    acl = external_ids.get("ACL")
    if acl:
        return f"https://aclanthology.org/{acl}/"
    return None


def arxiv_from_external_ids(external_ids: dict) -> str | None:
    identifier = external_ids.get("ArXiv")
    return f"https://arxiv.org/abs/{identifier}" if identifier else None


def publication_url(title: str, venue_year: str) -> str | None:
    matches: list[tuple[int, int, str]] = []
    for info in dblp_hits(title):
        title_score = score_title(title, info_title(info))
        year_score = 25 if venue_year and str(info.get("year", "")) == venue_year else 0
        if title_score + year_score < 90:
            continue
        for url in publication_from_info(info):
            host_rank = next(
                (
                    len(PREFERRED_PUBLICATION_HOSTS) - index
                    for index, host in enumerate(PREFERRED_PUBLICATION_HOSTS)
                    if host in url
                ),
                0,
            )
            matches.append((title_score + year_score, host_rank, url))
    if not matches:
        return None
    matches.sort(reverse=True)
    top = matches[0]
    tied = [item for item in matches if item[:2] == top[:2]]
    if len({item[2] for item in tied}) > 1:
        return None
    return top[2]


def arxiv_url_for_title(title: str) -> str | None:
    matches: list[tuple[int, str]] = []
    for info in dblp_hits(title):
        candidate = arxiv_from_info(info)
        if candidate and score_title(title, info_title(info)) >= 100:
            matches.append((100, candidate))
    urls = {url for _, url in matches}
    return next(iter(urls)) if len(urls) == 1 else None


def resolve_row(
    row: dict[str, str], s2_records: dict[str, dict]
) -> tuple[dict[str, str], dict[str, str] | None]:
    row = dict(row)
    row["arxiv_url"] = (row.get("arxiv_url") or "").strip()
    if row.get("section") != "Papers":
        row["arxiv_url"] = ""
        return row, None

    primary = row["url"].strip()
    published = row.get("venue", "") not in ARXIV_ONLY_VENUES

    if is_arxiv_url(primary):
        identifier = arxiv_id(primary)
        canonical_arxiv = f"https://arxiv.org/abs/{identifier}"
        if not published:
            row["url"] = canonical_arxiv
            row["arxiv_url"] = ""
            return row, None

        row["arxiv_url"] = canonical_arxiv
        if row["name"] in PUBLICATION_OVERRIDES:
            row["url"] = PUBLICATION_OVERRIDES[row["name"]]
            return row, None

        record = s2_records.get(f"ARXIV:{identifier}", {})
        external_ids = record.get("externalIds") or {}
        resolved = publication_from_external_ids(external_ids)
        title = str(record.get("title") or row["name"])
        if not resolved:
            try:
                resolved = publication_url(title, row.get("venue_year", ""))
            except Exception as exc:
                return row, {"name": row["name"], "kind": "publication", "error": repr(exc)}
        if not resolved:
            return row, {"name": row["name"], "kind": "publication", "title": title}
        row["url"] = resolved
        return row, None

    if row.get("arxiv_date") and not row["arxiv_url"]:
        if row["name"] in ARXIV_OVERRIDES:
            row["arxiv_url"] = ARXIV_OVERRIDES[row["name"]]
            return row, None

        lookup_id = semantic_scholar_id(primary)
        record = s2_records.get(lookup_id or "", {})
        external_ids = record.get("externalIds") or {}
        resolved = arxiv_from_external_ids(external_ids)
        title = str(record.get("title") or row["name"])
        if not resolved:
            try:
                resolved = arxiv_url_for_title(title)
            except Exception as exc:
                return row, {"name": row["name"], "kind": "arxiv", "error": repr(exc)}
        if not resolved:
            return row, {"name": row["name"], "kind": "arxiv", "title": title}
        row["arxiv_url"] = resolved

    return row, None


def main() -> int:
    with RESOURCE_PATH.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise SystemExit("resources.csv has no header")
        fieldnames = list(reader.fieldnames)
        rows = list(reader)

    if "arxiv_url" not in fieldnames:
        fieldnames.insert(fieldnames.index("url") + 1, "arxiv_url")
        for row in rows:
            row["arxiv_url"] = ""

    lookup_ids: list[str] = []
    for row in rows:
        if row.get("section") != "Papers":
            continue
        primary = row["url"].strip()
        published = row.get("venue", "") not in ARXIV_ONLY_VENUES
        if is_arxiv_url(primary) and published:
            lookup_ids.append(f"ARXIV:{arxiv_id(primary)}")
        elif row.get("arxiv_date"):
            lookup_id = semantic_scholar_id(primary)
            if lookup_id:
                lookup_ids.append(lookup_id)

    lookup_ids = list(dict.fromkeys(lookup_ids))
    try:
        s2_records = semantic_scholar_batch(lookup_ids)
    except Exception as exc:
        print(f"Semantic Scholar batch lookup failed: {exc!r}; using DBLP fallback", file=sys.stderr)
        s2_records = {}

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        results = list(executor.map(lambda row: resolve_row(row, s2_records), rows))

    resolved_rows = [row for row, _ in results]
    unresolved = [error for _, error in results if error is not None]
    if unresolved:
        print(json.dumps(unresolved, indent=2, ensure_ascii=False), file=sys.stderr)
        print("Refusing to write resources.csv until every bibliographic link is resolved.", file=sys.stderr)
        return 1

    with RESOURCE_PATH.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(resolved_rows)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
