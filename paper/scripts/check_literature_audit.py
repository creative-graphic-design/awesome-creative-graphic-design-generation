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
    # Empirical claims must be grounded in inspected original methods/results.
    if row.get("source_depth") != "methods_results" and row.get("empirical_claim_audit") == "verified":
        errors.append(f"Empirical result marked verified without methods/results audit: {key}")
    if row.get("source_depth") == "catalogue_only" and any(
        row.get(column) == "verified"
        for column in ("representation_audit", "editability_audit", "evaluation_audit")
    ):
        errors.append(f"Catalogue-only record cannot verify representation/edit/evaluation: {key}")
    if row.get("source_depth") == "methods_results" and not row.get("source_section_locator"):
        errors.append(f"Methods/results audit needs a source locator: {key}")
    if any(row.get(column) == "verified" for column in (
        "empirical_claim_audit", "representation_audit", "editability_audit", "evaluation_audit",
    )) and not row.get("source_section_locator"):
        errors.append(f"Verified claim needs source locator: {key}")

# A frozen transfer manifest protects citations from drifting after evidence
# originally checked in a private workbook is copied into this registry.
TRANSFER_PATH = PAPER / "PRIMARY_SOURCE_EVIDENCE_TRANSFERS_20261108.csv"
if TRANSFER_PATH.is_file():
    with TRANSFER_PATH.open(encoding="utf-8", newline="") as handle:
        transfers = list(csv.DictReader(handle))
    by_key = {row["bibtex_key"]: row for row in rows}
    seen_transfers: set[str] = set()
    for transfer in transfers:
        key = transfer["bibtex_key"]
        if key in seen_transfers:
            errors.append(f"Duplicate prior-source transfer: {key}")
        seen_transfers.add(key)
        linked = by_key.get(key)
        if not linked or linked["working_register_id"] != transfer["working_register_id"]:
            errors.append(f"Stale prior-source transfer key or study: {key}")
            continue
        if linked["source_depth"] != "methods_results":
            errors.append(f"Prior-source transfer lost methods/results depth: {key}")
        for column in ("primary_source_url", "original_section_or_table_locator"):
            if not transfer.get(column) or transfer[column] not in linked["source_section_locator"]:
                errors.append(f"Prior-source transfer locator mismatch: {key}: {column}")
        if not transfer.get("original_audit_workbook_tab"):
            errors.append(f"Prior-source transfer missing workbook provenance: {key}")

# Frozen audit log of original abstract-only source checks, distinct from
# original methods/results inspection. Never infer experimental verification.
RESULTS_AUDIT = PAPER / "T24_SELECTED_PRIMARY_RESULTS_20261108.csv"
fulltext_by_key: dict[str, dict[str, str]] = {}
if RESULTS_AUDIT.is_file():
    with RESULTS_AUDIT.open(encoding="utf-8", newline="") as handle:
        fulltext_rows = list(csv.DictReader(handle))
    audit_by_key = {row["bibtex_key"]: row for row in rows}
    for item in fulltext_rows:
        key = item["bibtex_key"]
        if key in fulltext_by_key:
            errors.append(f"Duplicated original methods review: {key}")
        fulltext_by_key[key] = item
        actual = audit_by_key.get(key)
        if not actual or actual["source_depth"] != "methods_results":
            errors.append(f"Original methods review missing methods/results tier: {key}")
        elif not item["original_methods_locator"] or item["original_methods_url"] not in actual["source_section_locator"]:
            errors.append(f"Original methods review source locator mismatch: {key}")

ABSTRACT_PATH = PAPER / "T22_ABSTRACT_SOURCE_RECONCILIATION_20261108.csv"
if ABSTRACT_PATH.is_file():
    with ABSTRACT_PATH.open(encoding="utf-8", newline="") as handle:
        abstract_records = list(csv.DictReader(handle))
    ledger = {r["bibtex_key"]: r for r in rows}
    seen_abstracts: set[str] = set()
    for record in abstract_records:
        key = record["bibtex_key"]
        if key in seen_abstracts:
            errors.append(f"Duplicate abstract-source check: {key}")
        seen_abstracts.add(key)
        row = ledger.get(key)
        if row is None or row["working_register_id"] != record["working_register_id"]:
            errors.append(f"Abstract-source citation identity mismatch: {key}")
            continue
        verified_fulltext = fulltext_by_key.get(key)
        # T22 is a historical snapshot of abstract-stage checking, not a
        # permanent cap on evidence depth. Later original-source reviews
        # are preserved in the audit ledger and must be explicitly traced.
        is_later_original_review = (
            row["source_depth"] == "methods_results"
            and "NEW ORIGINAL-SOURCE AUDIT:" in row["notes"]
            and bool(re.search(
                r"(?i)original (?:full|complete|author|publisher|CHI)|"
                r"original Sections? |original full text|original paper",
                row["source_section_locator"],
            ))
            and bool(re.search(r"https?://", row["source_section_locator"]))
        )
        if verified_fulltext and row["source_depth"] == "methods_results":
            if verified_fulltext["original_methods_url"] not in row["source_section_locator"]:
                errors.append(f"Original methods/results locator drift: {key}")
        elif is_later_original_review:
            # A newer independently recorded source review supersedes the
            # T22 abstract-only status; do not rewrite its historical row.
            pass
        elif row["source_depth"] != "abstract_index":
            errors.append(f"Abstract claim promoted without documented original-source review: {key}")
        if not verified_fulltext and not is_later_original_review:
            if record["primary_abstract_url"] not in row["source_section_locator"]:
                errors.append(f"Abstract source URL drift: {key}")
            if row["empirical_claim_audit"] == "verified":
                errors.append(f"Abstract-only empirical claim incorrectly promoted: {key}")

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
