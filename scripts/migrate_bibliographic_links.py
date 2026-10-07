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
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESOURCE_PATH = ROOT / "data" / "resources.csv"
ARXIV_ONLY_VENUES = {"", "arXiv", "Technical Report"}
USER_AGENT = "awesome-creative-graphic-design-generation/1.0 bibliographic migration"

# Only verified exceptions belong here. Automated matching remains fail-closed.
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


def request_json(url: str) -> dict:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    last_error: Exception | None = None
    for attempt in range(2):
        try:
            with urllib.request.urlopen(request, timeout=8) as response:
                return json.loads(response.read().decode("utf-8"))
        except Exception as exc:
            last_error = exc
            time.sleep(0.5 * (attempt + 1))
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
    result: list[str] = []
    for url in info_ee(info):
        if not url.startswith("https://") or is_arxiv_url(url):
            continue
        result.append(url)
    return result


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


def canonical_title(name: str, venue_year: str, identifier: str = "") -> str:
    queries = [identifier, name] if identifier else [name]
    candidates: list[tuple[int, str]] = []
    for query in queries:
        if not query:
            continue
        for info in dblp_hits(query):
            title = info_title(info)
            score = score_title(name, title)
            if identifier and identifier in json.dumps(info, ensure_ascii=False):
                score += 120
            if venue_year and str(info.get("year", "")) == venue_year:
                score += 25
            if score >= 80:
                candidates.append((score, title))
    if not candidates:
        return name
    candidates.sort(reverse=True)
    return candidates[0][1]


def publication_url(title: str, venue_year: str) -> str | None:
    matches: list[tuple[int, int, str]] = []
    for info in dblp_hits(title):
        title_score = score_title(title, info_title(info))
        year_score = 25 if venue_year and str(info.get("year", "")) == venue_year else 0
        if title_score + year_score < 90:
            continue
        for url in publication_from_info(info):
            host_rank = next(
                (len(PREFERRED_PUBLICATION_HOSTS) - index for index, host in enumerate(PREFERRED_PUBLICATION_HOSTS) if host in url),
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


def arxiv_url_for_title(title: str, venue_year: str) -> str | None:
    matches: list[tuple[int, str]] = []
    for info in dblp_hits(title):
        candidate = arxiv_from_info(info)
        if not candidate:
            continue
        score = score_title(title, info_title(info))
        # CoRR record year is commonly the preprint year, so venue-year mismatch
        # must not reject an otherwise exact title.
        if score >= 100:
            matches.append((score, candidate))
    if not matches:
        return None
    urls = {url for score, url in matches if score == max(item[0] for item in matches)}
    return next(iter(urls)) if len(urls) == 1 else None


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

    unresolved: list[dict[str, str]] = []

    for row in rows:
        row["arxiv_url"] = (row.get("arxiv_url") or "").strip()
        if row.get("section") != "Papers":
            row["arxiv_url"] = ""
            continue

        primary = row["url"].strip()
        published = row.get("venue", "") not in ARXIV_ONLY_VENUES

        if is_arxiv_url(primary):
            identifier = arxiv_id(primary)
            canonical_arxiv = f"https://arxiv.org/abs/{identifier}"
            if not published:
                row["url"] = canonical_arxiv
                row["arxiv_url"] = ""
                continue

            row["arxiv_url"] = canonical_arxiv
            if row["name"] in PUBLICATION_OVERRIDES:
                row["url"] = PUBLICATION_OVERRIDES[row["name"]]
                continue

            try:
                title = canonical_title(row["name"], row.get("venue_year", ""), identifier)
                resolved = publication_url(title, row.get("venue_year", ""))
            except Exception as exc:
                unresolved.append({"name": row["name"], "kind": "publication", "error": repr(exc)})
                continue
            if resolved:
                row["url"] = resolved
            else:
                unresolved.append({"name": row["name"], "kind": "publication", "title": title})
            continue

        if row.get("arxiv_date") and not row["arxiv_url"]:
            if row["name"] in ARXIV_OVERRIDES:
                row["arxiv_url"] = ARXIV_OVERRIDES[row["name"]]
                continue
            try:
                title = canonical_title(row["name"], row.get("venue_year", ""))
                resolved = arxiv_url_for_title(title, row.get("venue_year", ""))
            except Exception as exc:
                unresolved.append({"name": row["name"], "kind": "arxiv", "error": repr(exc)})
                continue
            if resolved:
                row["arxiv_url"] = resolved
            else:
                unresolved.append({"name": row["name"], "kind": "arxiv", "title": title})

    if unresolved:
        print(json.dumps(unresolved, indent=2, ensure_ascii=False), file=sys.stderr)
        print("Refusing to write resources.csv until every bibliographic link is resolved.", file=sys.stderr)
        return 1

    with RESOURCE_PATH.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
