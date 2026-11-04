"""Negative cases for the mandatory 225-study evidence crosswalk gate."""
from __future__ import annotations

import csv
import importlib.util
import shutil
import tempfile
import unittest
from pathlib import Path

PAPER = Path(__file__).resolve().parents[2]
VALIDATOR = PAPER / "scripts" / "check_evidence_register.py"
spec = importlib.util.spec_from_file_location("evidence_gate", VALIDATOR)
assert spec is not None and spec.loader is not None
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)
ASSETS = [
    "evidence_register_225_snapshot.csv",
    "evidence_register_225_crosswalk.csv",
    "literature_citation_audit.csv",
    "references.bib",
    "evidence_register_snapshot_manifest.json",
    "evidence_review_queue.csv",
]


class EvidenceRegisterTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.paper = Path(self.tmp.name)
        for name in ASSETS:
            shutil.copy2(PAPER / name, self.paper / name)

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def rewrite(self, filename: str, operation) -> None:
        path = self.paper / filename
        with path.open(encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle)
            header, rows = reader.fieldnames, list(reader)
        operation(rows)
        with path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=header)
            writer.writeheader()
            writer.writerows(rows)

    def test_unchanged_baseline(self) -> None:
        errors, counts = validator.validate(self.paper)
        self.assertEqual(errors, [])
        self.assertEqual(counts["sheet_studies"], 225)
        self.assertEqual(counts["linked"], 169)
        self.assertEqual(counts["needs_review"], 56)

    def test_old_spreadsheet_review_is_rejected(self) -> None:
        manifest = self.paper / "evidence_register_snapshot_manifest.json"
        content = manifest.read_text(encoding="utf-8")
        manifest.write_text(
            content.replace('"snapshot_reviewed_utc": "2026-11-04"',
                            '"snapshot_reviewed_utc": "2020-01-01"'),
            encoding="utf-8",
        )
        errors, _ = validator.validate(self.paper)
        self.assertTrue(any("snapshot review expired" in e for e in errors))

    def test_publication_preprint_alias_regression_is_rejected(self) -> None:
        bib = self.paper / "references.bib"
        content = bib.read_text(encoding="utf-8")
        self.assertIn("eprint = {2602.17690}", content)
        bib.write_text(content.replace("eprint = {2602.17690}", ""), encoding="utf-8")
        errors, _ = validator.validate(self.paper)
        self.assertTrue(any("Stale/missing BibTeX link" in e for e in errors))

    def test_missing_unresolved_queue_row_is_rejected(self) -> None:
        self.rewrite("evidence_review_queue.csv", lambda rows: rows.pop())
        errors, _ = validator.validate(self.paper)
        self.assertTrue(any("Review queue must contain exactly" in e for e in errors))

    def test_changed_priority_is_rejected(self) -> None:
        def corrupt(rows):
            rows[0]["review_priority"] = "P3-catalogue"
        self.rewrite("evidence_review_queue.csv", corrupt)
        errors, _ = validator.validate(self.paper)
        self.assertTrue(any("Stale source-tier review priority" in e for e in errors))

    def test_tkgdm_preprint_alias_regression_is_rejected(self) -> None:
        bib = self.paper / "references.bib"
        content = bib.read_text(encoding="utf-8")
        self.assertIn("eprint = {2411.15580}", content)
        broken = content.replace("eprint = {2411.15580}", "eprint = {2411.15581}")
        broken = broken.replace("url = {https://arxiv.org/abs/2411.15580}",
                                "url = {https://arxiv.org/abs/2411.15581}")
        bib.write_text(broken, encoding="utf-8")
        errors, _ = validator.validate(self.paper)
        self.assertTrue(any("Stale/missing BibTeX link: CGD-092" in e for e in errors))

    def test_missing_sheet_study_is_rejected(self) -> None:
        self.rewrite(ASSETS[0], lambda rows: rows.pop())
        errors, _ = validator.validate(self.paper)
        self.assertTrue(any("snapshot changed size" in e for e in errors))

    def test_invalid_bibtex_match_is_rejected(self) -> None:
        def corrupt(rows):
            row = next(r for r in rows if r["citation_status"] == "linked")
            row["bibtex_key"] = "fabricated-key"
        self.rewrite(ASSETS[1], corrupt)
        errors, _ = validator.validate(self.paper)
        self.assertTrue(any("Stale/missing BibTeX link" in e for e in errors))

    def test_unreconciled_citation_audit_is_rejected(self) -> None:
        def corrupt(rows):
            row = next(r for r in rows if r["working_register_id"])
            row["working_register_id"] = ""
        self.rewrite(ASSETS[2], corrupt)
        errors, _ = validator.validate(self.paper)
        self.assertTrue(any("Missing or outdated 225-study ID" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
