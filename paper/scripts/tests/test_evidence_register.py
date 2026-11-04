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
        self.assertEqual(counts["linked"], 148)
        self.assertEqual(counts["needs_review"], 77)

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
