#!/usr/bin/env python3
"""Check citation-audit coverage without pretending that a paper has been screened.

This validator checks registry consistency, not the correctness of primary sources.
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

PAPER = Path(__file__).resolve().parents[1]
BIB_PATH = PAPER / "references.bib"
AUDIT_PATH = PAPER / "literature_citation_audit.csv"
REQUIRED = [
    "bibtex_key", "canonical_title_bib", "reference_year", "bib_url", "doi_bib",
    "working_register_id", "duplicate_group", "source_depth",
    "source_section_locator", "empirical_claim_audit", "representation_audit",
    "editability_audit", "evaluation_audit", "adjudication_status", "notes",
]
CHECK_STATES = {"not_verified", "verified", "not_applicable"}
DEPTH_STATES = {"not_verified", "catalogue_only", "abstract_index", "methods_results"}
ADJUDICATION_STATES = {"pending", "included", "excluded", "needs_review"}
errors: list[str] = []

bib = BIB_PATH.read_text(encoding="utf-8")
start_re = re.compile(r"(?m)^@(article|inproceedings|misc)\{([^,{}\s]+),\s*$")
starts = list(start_re.finditer(bib))
bib_records: dict[str, dict[str, str]] = {}

for index, match in enumerate(starts):
    key = match.group(2)
    chunk = bib[match.end():starts[index + 1].start() if index + 1 < len(starts) else len(bib)]
    fields: dict[str, str] = {}
    for field in ("title", "year", "url", "doi"):
        value = re.search(rf"(?m)^\s*{field}\s*=\s*\{{(.*)\}},?\s*$", chunk)
        fields[field] = value.group(1) if value else ""
    fields["title"] = fields["title"].removeprefix("{").removesuffix("}")
    bib_records[key] = fields

with AUDIT_PATH.open(encoding="utf-8", newline="") as handle:
    reader = csv.DictReader(handle)
    if reader.fieldnames != REQUIRED:
        errors.append("Audit CSV header does not match expected schema")
    rows = list(reader)

seen: set[str] = set()
for row in rows:
    key = row.get("bibtex_key", "")
    if key in seen:
        errors.append(f"Duplicate audit key: {key}")
    seen.add(key)
    if key not in bib_records:
        errors.append(f"Audit key absent from BibTeX: {key}")
        continue
    record = bib_records[key]
    for column, bib_field in (
        ("canonical_title_bib", "title"),
        ("reference_year", "year"),
        ("bib_url", "url"),
        ("doi_bib", "doi"),
    ):
        if row.get(column, "") != record[bib_field]:
            errors.append(f"Stale audit metadata for {key}: {column}")
    if row.get("source_depth") not in DEPTH_STATES:
        errors.append(f"Invalid evidence depth for {key}")
    if row.get("adjudication_status") not in ADJUDICATION_STATES:
        errors.append(f"Invalid adjudication state for {key}")
    for column in ("empirical_claim_audit", "representation_audit", "editability_audit", "evaluation_audit"):
        if row.get(column) not in CHECK_STATES:
            errors.append(f"Invalid {column} for {key}")
    if row.get("source_depth") == "methods_results" and not row.get("source_section_locator"):
        errors.append(f"Methods/results audit needs a source locator: {key}")
    if any(row.get(column) == "verified" for column in (
        "empirical_claim_audit", "representation_audit", "editability_audit", "evaluation_audit",
    )) and not row.get("source_section_locator"):
        errors.append(f"Verified claim needs source locator: {key}")

missing = set(bib_records) - seen
if missing:
    errors.append("BibTeX entries missing from audit: " + ", ".join(sorted(missing)))

print(f"Citation-audit rows: {len(rows)}, BibTeX keys: {len(bib_records)}")
print("Evidence-depth counts: " + ", ".join(
    f"{state}={sum(row.get('source_depth') == state for row in rows)}"
    for state in sorted(DEPTH_STATES)
))
if errors:
    for err in errors:
        print("ERROR:", err, file=sys.stderr)
    sys.exit(1)
print("Citation-audit coverage and metadata consistency passed")
