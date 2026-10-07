#!/usr/bin/env python3
"""One-off migration for publication/arXiv link separation in resources.csv.

This script updates only data/resources.csv. It adds an arxiv_url column, moves
existing arXiv primary URLs into arxiv_url for published papers, and resolves an
authoritative publication URL from bibliographic services. It refuses to write
when a row cannot be resolved confidently.
"""

from __future__ import annotations

import csv
import html
import json
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
RESOURCE_PATH = ROOT / "data" / "resources.csv"
ARXIV_ONLY_VENUES = {"", "arXiv", "Technical Report"}
USER_AGENT = "awesome-creative-graphic-design-generation bibliographic migration"

# Explicit overrides are intentionally small. Add one only after verifying the
# authoritative target manually when automated bibliographic matching is not
# exact enough.
PUBLICATION_OVERRIDES: dict[str, str] = {}
ARXIV_OVERRIDES: dict[str, str] = {
    # Preprint title differs from the eventual publication title.
    "T-Stars-Poster": "https://arxiv.org/abs/2501.12756",
}


def request_text(url: str) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return response.read().decode("utf-8")
        except Exception:
            if attempt == 3:
                raise
            time.sleep(1.5 * (attempt + 1))
    raise AssertionError("unreachable")


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


def arxiv_title_from_id(identifier: str) -> str | None:
    url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode({"id_list": identifier})
    root = ET.fromstring(request_text(url))
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    entry = root.find("atom:entry", ns)
    if entry is None:
        return None
    title = entry.findtext("atom:title", default="", namespaces=ns)
    return " ".join(title.split()) or None


def arxiv_url_for_title(title: str, expected_date: str) -> str | None:
    query = f'ti:"{title.replace(chr(34), "")}"'
    url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(
        {"search_query": query, "start": 0, "max_results": 8}
    )
    root = ET.fromstring(request_text(url))
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    target = normalize_title(title)
    candidates: list[tuple[int, str]] = []
    for entry in root.findall("atom:entry", ns):
        candidate_title = " ".join(
            entry.findtext("atom:title", default="", namespaces=ns).split()
        )
        norm = normalize_title(candidate_title)
        if not norm:
            continue
        score = 0
        if norm == target:
            score += 100
        elif target in norm or norm in target:
            score += 50
        published = entry.findtext("atom:published", default="", namespaces=ns)[:10]
        if expected_date and published == expected_date:
            score += 30
        entry_id = entry.findtext("atom:id", default="", namespaces=ns)
        match = re.search(r"arxiv\.org/abs/([^/?#]+)", entry_id)
        if match and score >= 80:
            candidates.append((score, f"https://arxiv.org/abs/{match.group(1).split('v', 1)[0]}"))
    if not candidates:
        return None
    candidates.sort(reverse=True)
    if len(candidates) > 1 and candidates[0][0] == candidates[1][0]:
        return None
    return candidates[0][1]


def dblp_publication_url(title: str, venue_year: str) -> str | None:
    url = "https://dblp.org/search/publ/api?" + urllib.parse.urlencode(
        {"q": title, "format": "json", "h": 20}
    )
    payload = json.loads(request_text(url))
    hits = payload.get("result", {}).get("hits", {}).get("hit", [])
    if isinstance(hits, dict):
        hits = [hits]
    target = normalize_title(title)
    matches: list[tuple[int, str]] = []
    for hit in hits:
        info = hit.get("info", {})
        candidate = normalize_title(str(info.get("title", "")))
        if not candidate:
            continue
        score = 0
        if candidate == target:
            score += 100
        elif target in candidate or candidate in target:
            score += 45
        if venue_year and str(info.get("year", "")) == venue_year:
            score += 25
        if score < 90:
            continue
        ee = info.get("ee", [])
        if isinstance(ee, str):
            ee = [ee]
        for candidate_url in ee:
            if not candidate_url.startswith("https://"):
                continue
            if is_arxiv_url(candidate_url):
                continue
            matches.append((score, candidate_url))
    if not matches:
        return None
    preferred_hosts = (
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
    matches.sort(
        key=lambda item: (
            item[0],
            max(
                (len(preferred_hosts) - index for index, host in enumerate(preferred_hosts) if host in item[1]),
                default=0,
            ),
        ),
        reverse=True,
    )
    if len(matches) > 1 and matches[0][0] == matches[1][0] and matches[0][1] != matches[1][1]:
        # Prefer the explicit host ranking above; ties after that are ambiguous.
        top = matches[0]
        second = matches[1]
        rank = lambda u: next((i for i, h in enumerate(preferred_hosts) if h in u), 999)
        if rank(top[1]) == rank(second[1]):
            return None
    return matches[0][1]


def crossref_publication_url(title: str, venue_year: str) -> str | None:
    url = "https://api.crossref.org/works?" + urllib.parse.urlencode(
        {"query.title": title, "rows": 5, "select": "DOI,title,published-online,published-print"}
    )
    payload = json.loads(request_text(url))
    target = normalize_title(title)
    matches: list[tuple[int, str]] = []
    for item in payload.get("message", {}).get("items", []):
        titles = item.get("title", [])
        candidate = normalize_title(titles[0] if titles else "")
        if not candidate:
            continue
        score = 100 if candidate == target else 45 if target in candidate or candidate in target else 0
        if venue_year:
            years: set[str] = set()
            for key in ("published-online", "published-print"):
                parts = item.get(key, {}).get("date-parts", [])
                if parts and parts[0]:
                    years.add(str(parts[0][0]))
            if venue_year in years:
                score += 25
        doi = item.get("DOI")
        if doi and score >= 90:
            matches.append((score, f"https://doi.org/{doi}"))
    if not matches:
        return None
    matches.sort(reverse=True)
    if len(matches) > 1 and matches[0][0] == matches[1][0]:
        return None
    return matches[0][1]


def publication_url(title: str, venue_year: str) -> str | None:
    return dblp_publication_url(title, venue_year) or crossref_publication_url(title, venue_year)


def canonical_title_for_publication_row(row: dict[str, str]) -> str:
    # DBLP often expands acronym-style catalog names into the paper's full title.
    url = "https://dblp.org/search/publ/api?" + urllib.parse.urlencode(
        {"q": row["name"], "format": "json", "h": 10}
    )
    payload = json.loads(request_text(url))
    hits = payload.get("result", {}).get("hits", {}).get("hit", [])
    if isinstance(hits, dict):
        hits = [hits]
    year = row.get("venue_year", "")
    normalized_name = normalize_title(row["name"])
    candidates: list[tuple[int, str]] = []
    for hit in hits:
        info = hit.get("info", {})
        title = " ".join(str(info.get("title", "")).split())
        norm = normalize_title(title)
        if not norm:
            continue
        score = 0
        if norm == normalized_name:
            score += 100
        elif normalized_name in norm:
            score += 55
        if year and str(info.get("year", "")) == year:
            score += 25
        if score >= 70:
            candidates.append((score, title))
    if not candidates:
        return row["name"]
    candidates.sort(reverse=True)
    return candidates[0][1]


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
        if row.get("section") != "Papers":
            row["arxiv_url"] = row.get("arxiv_url", "") or ""
            continue

        primary = row["url"].strip()
        row["arxiv_url"] = (row.get("arxiv_url") or "").strip()
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
                title = arxiv_title_from_id(identifier) or row["name"]
                resolved = publication_url(title, row.get("venue_year", ""))
            except Exception as exc:
                unresolved.append({"name": row["name"], "kind": "publication", "error": repr(exc)})
                continue
            if resolved:
                row["url"] = resolved
            else:
                unresolved.append({"name": row["name"], "kind": "publication", "title": title})
            continue

        # The primary URL is already a publication/proceedings link. If an
        # arXiv v1 date is recorded, preserve the verified preprint separately.
        if row.get("arxiv_date") and not row["arxiv_url"]:
            if row["name"] in ARXIV_OVERRIDES:
                row["arxiv_url"] = ARXIV_OVERRIDES[row["name"]]
                continue
            try:
                title = canonical_title_for_publication_row(row)
                resolved = arxiv_url_for_title(title, row["arxiv_date"])
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
