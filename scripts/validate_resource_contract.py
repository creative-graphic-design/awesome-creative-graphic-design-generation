#!/usr/bin/env python3
"""Validate the canonical data/resources.csv contract."""

from __future__ import annotations

import csv
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
RESOURCE_PATH = ROOT / "data" / "resources.csv"

RESOURCE_COLUMNS = [
    "section",
    "category",
    "name",
    "url",
    "arxiv_url",
    "description",
    "architecture",
    "venue",
    "venue_year",
    "arxiv_date",
    "venue_date",
    "date_note",
]

ARXIV_ONLY_VENUES = {"", "arXiv", "Technical Report"}


def is_arxiv_url(value: str) -> bool:
    if not value:
        return False
    parsed = urlparse(value)
    return (
        parsed.scheme == "https"
        and (parsed.hostname or "").casefold() == "arxiv.org"
        and parsed.path.startswith("/abs/")
        and len(parsed.path.removeprefix("/abs/")) > 0
        and not parsed.params
        and not parsed.query
        and not parsed.fragment
    )


def is_arxiv_doi(value: str) -> bool:
    if not value:
        return False
    parsed = urlparse(value)
    return (
        parsed.scheme == "https"
        and (parsed.hostname or "").casefold() == "doi.org"
        and parsed.path.lstrip("/").casefold().startswith("10.48550/arxiv.")
    )


def fail(message: str) -> None:
    print(f"resources.csv contract violation: {message}", file=sys.stderr)


def main() -> int:
    errors = 0
    with RESOURCE_PATH.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != RESOURCE_COLUMNS:
            fail(
                "header must be exactly "
                + ",".join(RESOURCE_COLUMNS)
                + f"; got {reader.fieldnames}"
            )
            return 1
        rows = list(reader)

    seen_primary_urls: set[str] = set()
    seen_arxiv_urls: set[str] = set()

    for line_number, row in enumerate(rows, start=2):
        name = row["name"] or f"line {line_number}"
        primary = row["url"].strip()
        arxiv = row["arxiv_url"].strip()
        primary_is_arxiv = is_arxiv_url(primary)
        primary_is_arxiv_doi = is_arxiv_doi(primary)

        if primary in seen_primary_urls:
            fail(f"{name}: duplicate primary url {primary}")
            errors += 1
        seen_primary_urls.add(primary)

        if arxiv:
            if not is_arxiv_url(arxiv):
                fail(f"{name}: arxiv_url must be canonical https://arxiv.org/abs/...: {arxiv}")
                errors += 1
            if arxiv in seen_arxiv_urls:
                fail(f"{name}: duplicate arxiv_url {arxiv}")
                errors += 1
            seen_arxiv_urls.add(arxiv)
            if not row["arxiv_date"]:
                fail(f"{name}: arxiv_url requires arxiv_date")
                errors += 1

        if primary_is_arxiv and arxiv:
            fail(f"{name}: do not duplicate the primary arXiv URL in arxiv_url")
            errors += 1

        if row["section"] != "Papers":
            if arxiv:
                fail(f"{name}: arxiv_url is currently defined only for Papers entries")
                errors += 1
            continue

        published = row["venue"] not in ARXIV_ONLY_VENUES

        if published and (primary_is_arxiv or primary_is_arxiv_doi):
            fail(
                f"{name}: published paper must use an authoritative publication/proceedings/venue "
                "URL as url; arXiv URLs and arXiv DOIs are preprint surrogates"
            )
            errors += 1

        if published and row["arxiv_date"] and not arxiv:
            fail(f"{name}: published paper with arxiv_date must also set arxiv_url")
            errors += 1

        if not published and primary_is_arxiv and arxiv:
            fail(f"{name}: arXiv-only paper must not duplicate its primary link")
            errors += 1

        if row["venue"] == "arXiv" and not primary_is_arxiv:
            fail(f"{name}: venue=arXiv requires the primary url to be arXiv")
            errors += 1

        if row["arxiv_date"] and not (primary_is_arxiv or arxiv):
            fail(f"{name}: arxiv_date requires either an arXiv primary url or arxiv_url")
            errors += 1

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
