#!/usr/bin/env python3
"""Audit the frozen 225-study Google Sheet snapshot against the manuscript.

Github CI does not have live credentials for the private sheet. These checks
protect against manuscript/bibliography drift relative to the COMMITTED snapshot.
They cannot establish inclusion/exclusion or full-text review status.
"""
from __future__ import annotations

import csv
import json
from datetime import date
import re
import sys
from pathlib import Path

PAPER = Path(__file__).resolve().parents[1]
SNAPSHOT_FIELDS = [
    "working_register_id", "paper_title", "venue_year", "venue", "primary_task",
    "primary_url", "evidence_tier_sheet", "evidence_scope_sheet",
    "source_recheck_level_sheet", "verified_source_url_sheet",
]
CROSSWALK_FIELDS = [
    "working_register_id", "bibtex_key", "match_method", "citation_status",
    "editorial_decision", "editorial_note",
]
QUEUE_FIELDS = [
    "working_register_id", "paper_title", "primary_task", "primary_url",
    "evidence_tier", "source_recheck_level", "review_priority", "next_action",
    "editorial_status",
]
AUDIT_FIELDS = [
    "bibtex_key", "canonical_title_bib", "reference_year", "bib_url",
    "doi_bib", "working_register_id", "duplicate_group", "source_depth",
    "source_section_locator", "empirical_claim_audit", "representation_audit",
    "editability_audit", "evaluation_audit", "adjudication_status", "notes",
]
EXPECTED_ROWS = 225
UNRESOLVED_CEILING = 55


def csv_rows(path: Path, columns: list[str], errors: list[str]) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != columns:
            errors.append(f"{path.name}: unexpected header {reader.fieldnames}")
        return list(reader)


def normalized_title(text: str) -> str:
    text = re.sub(r"\\[A-Za-z]+\{([^{}]+)\}", r"\1", text)
    return re.sub(r"[^a-z0-9]", "", text.lower())


def normalized_url(text: str) -> str:
    text = re.sub(r"^https?://", "", text.strip().lower())
    return re.sub(r"/$", "", re.sub(r"^www\.", "", text))


def arxiv_id(text: str) -> str:
    result = re.search(
        r"(?:arxiv\.org/(?:abs|pdf|html)/|arxiv:)(\d{4}\.\d{4,5})", text, re.I
    )
    return result.group(1) if result else ""


def normalized_doi(text: str) -> str:
    return re.sub(r"^https?://(?:dx\.)?doi\.org/", "", text.strip().lower())


def bib_entries(path: Path) -> dict[str, dict[str, str]]:
    source = path.read_text(encoding="utf-8")
    starts = list(re.finditer(r"(?m)^@\w+\{([^,]+),", source))
    results: dict[str, dict[str, str]] = {}
    for i, match in enumerate(starts):
        end = starts[i + 1].start() if i + 1 < len(starts) else len(source)
        block = source[match.start():end]
        values = {}
        for field in ("title", "url", "doi", "eprint"):
            m = re.search(rf"(?m)^\s*{field}\s*=\s*\{{(.*)\}},?\s*$", block)
            values[field] = m.group(1) if m else ""
        results[match.group(1)] = values
    return results


def identify(row: dict[str, str], bib: dict[str, dict[str, str]]) -> dict[str, str]:
    found = {}
    source = row["primary_url"]
    source_arxiv = arxiv_id(source)
    for key, b in bib.items():
        match = ""
        if source_arxiv and source_arxiv == (arxiv_id(b["url"]) or b["eprint"]):
            match = "arxiv_id"
        elif (re.match(r"^https?://(?:dx\.)?doi\.org/", source, re.I)
              and normalized_doi(source) == normalized_doi(b["doi"])):
            match = "doi"
        elif normalized_url(source) and normalized_url(source) == normalized_url(b["url"]):
            match = "url"
        elif (normalized_title(row["paper_title"])
              and normalized_title(row["paper_title"]) == normalized_title(b["title"])):
            match = "title"
        if match:
            found[key] = match
    return found


def validate(paper: Path = PAPER) -> tuple[list[str], dict[str, int]]:
    errors: list[str] = []
    manifest_path = paper / "evidence_register_snapshot_manifest.json"
    if not manifest_path.is_file():
        errors.append("Missing dated live-spreadsheet snapshot manifest")
    else:
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            reviewed = date.fromisoformat(manifest["snapshot_reviewed_utc"])
            age = (date.today() - reviewed).days
            if manifest.get("spreadsheet_id") != "1PJtvX34FYoOnF8LS4-0WHpiR3B_KQ6n5fqRBtTeF3Zc":
                errors.append("Unexpected source workbook identity")
            if manifest.get("source_tab") != "Evidence Matrix 225":
                errors.append("Unexpected source worksheet")
            if manifest.get("expected_study_rows") != EXPECTED_ROWS:
                errors.append("Snapshot manifest row count does not match validator baseline")
            if not isinstance(manifest.get("expires_after_days"), int) or not 1 <= manifest["expires_after_days"] <= 30:
                errors.append("Snapshot review expiration interval must be 1-30 days")
            elif age < 0 or age > manifest["expires_after_days"]:
                errors.append(f"Live spreadsheet snapshot review expired or future-dated (age {age} days)")
        except (ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
            errors.append(f"Invalid spreadsheet snapshot provenance manifest: {exc}")
    sources = csv_rows(paper / "evidence_register_225_snapshot.csv", SNAPSHOT_FIELDS, errors)
    links = csv_rows(paper / "evidence_register_225_crosswalk.csv", CROSSWALK_FIELDS, errors)
    audits = csv_rows(paper / "literature_citation_audit.csv", AUDIT_FIELDS, errors)
    review_queue = csv_rows(paper / "evidence_review_queue.csv", QUEUE_FIELDS, errors)
    bib = bib_entries(paper / "references.bib")
    source_ids = [row["working_register_id"] for row in sources]
    linked = unresolved = 0
    if len(sources) != EXPECTED_ROWS:
        errors.append(f"225-study source snapshot changed size: {len(sources)}")
    if len(set(source_ids)) != len(source_ids):
        errors.append("Duplicate stable IDs in source snapshot")
    for row in sources:
        sid = row["working_register_id"]
        if not re.fullmatch(r"CGD-\d{3}", sid):
            errors.append(f"Malformed source ID: {sid}")
        if not row["paper_title"] or not row["primary_url"] or not row["evidence_tier_sheet"]:
            errors.append(f"Missing study identity/evidence tier: {sid}")
    link_ids = [row["working_register_id"] for row in links]
    if len(links) != len(sources) or set(link_ids) != set(source_ids):
        errors.append("Crosswalk must include all and only the 225 frozen study IDs")
    if len(set(link_ids)) != len(link_ids):
        errors.append("Duplicate crosswalk study ID")
    by_id = {row["working_register_id"]: row for row in links}
    bib_to_sheet: dict[str, str] = {}
    for row in sources:
        sid = row["working_register_id"]
        record = by_id.get(sid)
        if record is None:
            continue
        candidates = identify(row, bib)
        if len(candidates) > 1:
            errors.append(f"Ambiguous bibliographic identity: {sid}: {sorted(candidates)}")
            continue
        matched = bool(candidates)
        expected_key = next(iter(candidates)) if matched else ""
        expected_method = next(iter(candidates.values())) if matched else ""
        if record["bibtex_key"] != expected_key:
            errors.append(f"Stale/missing BibTeX link: {sid}")
        if record["match_method"] != expected_method:
            errors.append(f"Stale/incorrect identity match method: {sid}")
        if record["citation_status"] != ("linked" if matched else "needs_review"):
            errors.append(f"Stale citation status: {sid}")
        if record["editorial_decision"] not in {"pending", "needs_review", "included", "excluded"}:
            errors.append(f"Invalid editorial decision: {sid}")
        if record["editorial_decision"] == "excluded" and "source:" not in record["editorial_note"].lower():
            errors.append(f"Exclusion requires a documented primary-source locator: {sid}")
        if not record["editorial_note"]:
            errors.append(f"Every study needs a traceable pending decision: {sid}")
        if matched:
            linked += 1
            if expected_key in bib_to_sheet:
                errors.append(f"Duplicate source mapping for {expected_key}")
            bib_to_sheet[expected_key] = sid
        else:
            unresolved += 1
    if unresolved > UNRESOLVED_CEILING:
        errors.append(f"Unresolved working studies rose: {unresolved} > {UNRESOLVED_CEILING}")
    if linked + unresolved != len(sources):
        errors.append("A study is missing from the identity accounting")
    audit_keys = [row["bibtex_key"] for row in audits]
    if len(set(audit_keys)) != len(audit_keys) or set(audit_keys) != set(bib):
        errors.append("Citation-level audit and bibliography keys do not match")
    for row in audits:
        key = row["bibtex_key"]
        expected_id = bib_to_sheet.get(key, "")
        if row["working_register_id"] != expected_id:
            errors.append(f"Missing or outdated 225-study ID in citation audit: {key}")
    # Every unresolved paper must have one actionable row, not merely a
    # coarse aggregate count. Priorities reflect source-tier *claims* in the
    # frozen Sheet, not independently re-verified full-text findings.
    pending_ids = {r["working_register_id"] for r in links
                   if r["citation_status"] == "needs_review"}
    queue_ids = [r["working_register_id"] for r in review_queue]
    if set(queue_ids) != pending_ids or len(queue_ids) != len(pending_ids):
        errors.append("Review queue must contain exactly every unresolved study ID")
    if len(queue_ids) != len(set(queue_ids)):
        errors.append("Duplicate study ID in unresolved review queue")
    sources_by_id = {r["working_register_id"]: r for r in sources}
    for queued in review_queue:
        key = queued["working_register_id"]
        original = sources_by_id.get(key)
        if original is None:
            errors.append(f"Review queue ID absent from evidence snapshot: {key}")
            continue
        for queue_field, source_field in (
            ("paper_title", "paper_title"),
            ("primary_task", "primary_task"),
            ("primary_url", "primary_url"),
            ("evidence_tier", "evidence_tier_sheet"),
            ("source_recheck_level", "source_recheck_level_sheet"),
        ):
            if queued[queue_field] != original[source_field]:
                errors.append(f"Stale review queue source field {key}:{queue_field}")
        tier = (original["evidence_tier_sheet"] + " " +
                original["source_recheck_level_sheet"]).lower()
        if re.search(r"primary.methods|methods.results|full.sections|selected.method|original.section|checked.main|paper.text.verified", tier):
            expected_priority = "P1-primary-source"
        elif re.search(r"abstract|publisher|author|mirror", tier):
            expected_priority = "P2-abstract-source"
        else:
            expected_priority = "P3-catalogue"
        if queued["review_priority"] != expected_priority:
            errors.append(f"Stale source-tier review priority: {key}")
        if queued["editorial_status"] not in {"pending", "needs_review"}:
            errors.append(f"Invalid or prematurely finalized review status: {key}")
        if not queued["next_action"]:
            errors.append(f"Unresolved study lacks manual review action: {key}")

    return errors, {
        "sheet_studies": len(sources), "bibtex_entries": len(bib),
        "linked": linked, "needs_review": unresolved,
    }


def main() -> int:
    issues, counts = validate()
    print("225-study spreadsheet snapshot citation audit:", counts)
    for issue in issues:
        print("ERROR:", issue, file=sys.stderr)
    if issues:
        return 1
    print("PASS: all 225 IDs reconciled against BibTeX; unresolved != excluded")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
