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
        self.assertEqual(counts["linked"], 225)
        self.assertEqual(counts["needs_review"], 0)

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

    def inject_queue_row(self, priority: str) -> None:
        """Model a stale unresolved queue row after all 225 identities are linked."""
        with (self.paper / "evidence_register_225_snapshot.csv").open(
            encoding="utf-8", newline=""
        ) as handle:
            source = next(csv.DictReader(handle))
        row = {
            "working_register_id": source["working_register_id"],
            "paper_title": source["paper_title"],
            "primary_task": source["primary_task"],
            "primary_url": source["primary_url"],
            "evidence_tier": source["evidence_tier_sheet"],
            "source_recheck_level": source["source_recheck_level_sheet"],
            "review_priority": priority,
            "next_action": "Investigate stale row",
            "editorial_status": "pending",
        }
        path = self.paper / "evidence_review_queue.csv"
        with path.open(encoding="utf-8", newline="") as handle:
            fields = csv.DictReader(handle).fieldnames
        assert fields is not None
        with path.open("a", encoding="utf-8", newline="") as handle:
            csv.DictWriter(handle, fieldnames=fields).writerow(row)

    def test_spurious_unresolved_queue_row_is_rejected(self) -> None:
        self.inject_queue_row("P1-primary-source")
        errors, _ = validator.validate(self.paper)
        self.assertTrue(any("Review queue must contain exactly" in e for e in errors))

    def test_changed_priority_is_rejected(self) -> None:
        with (self.paper / "evidence_register_225_snapshot.csv").open(
            encoding="utf-8", newline=""
        ) as handle:
            source = next(csv.DictReader(handle))
        tier = (source["evidence_tier_sheet"] + " " +
                source["source_recheck_level_sheet"]).lower()
        import re
        if re.search(r"primary.methods|methods.results|full.sections|selected.method|original.section|checked.main|paper.text.verified", tier):
            expected = "P1-primary-source"
        elif re.search(r"abstract|publisher|author|mirror", tier):
            expected = "P2-abstract-source"
        else:
            expected = "P3-catalogue"
        wrong = "P3-catalogue" if expected != "P3-catalogue" else "P1-primary-source"
        self.inject_queue_row(wrong)
        errors, _ = validator.validate(self.paper)
        self.assertTrue(any("Stale source-tier review priority" in e for e in errors))

    def test_stale_link_status_is_rejected_with_empty_queue(self) -> None:
        def corrupt(rows):
            rows[0]["citation_status"] = "needs_review"
        self.rewrite("evidence_register_225_crosswalk.csv", corrupt)
        errors, _ = validator.validate(self.paper)
        self.assertTrue(any("Stale citation status" in e for e in errors))

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

    def test_alfie_publication_preprint_alias_regression_is_rejected(self) -> None:
        bib = self.paper / "references.bib"
        content = bib.read_text(encoding="utf-8")
        self.assertIn("eprint = {2408.14826}", content)
        broken = content.replace("eprint = {2408.14826}", "eprint = {2408.14827}")
        broken = broken.replace("url = {https://arxiv.org/abs/2408.14826}",
                                "url = {https://arxiv.org/abs/2408.14827}")
        bib.write_text(broken, encoding="utf-8")
        errors, _ = validator.validate(self.paper)
        self.assertTrue(any("Stale/missing BibTeX link: CGD-159" in e for e in errors))

    def test_layeringdiff_arxiv_identity_regression_is_rejected(self) -> None:
        bib = self.paper / "references.bib"
        content = bib.read_text(encoding="utf-8")
        self.assertIn("eprint = {2501.01197}", content)
        broken = content.replace("eprint = {2501.01197}", "eprint = {2501.01198}")
        broken = broken.replace("url = {https://arxiv.org/abs/2501.01197}",
                                "url = {https://arxiv.org/abs/2501.01198}")
        bib.write_text(broken, encoding="utf-8")
        errors, _ = validator.validate(self.paper)
        self.assertTrue(any("Stale/incorrect identity match method: CGD-174" in e for e in errors))

    def test_uniworld_design_arxiv_identity_regression_is_rejected(self) -> None:
        bib = self.paper / "references.bib"
        content = bib.read_text(encoding="utf-8")
        self.assertIn("eprint = {2608.03971}", content)
        broken = content.replace("eprint = {2608.03971}", "eprint = {2608.03972}")
        broken = broken.replace("url = {https://arxiv.org/abs/2608.03971}",
                                "url = {https://arxiv.org/abs/2608.03972}")
        bib.write_text(broken, encoding="utf-8")
        errors, _ = validator.validate(self.paper)
        self.assertTrue(any("Stale/incorrect identity match method: CGD-184" in e for e in errors))

    def test_postertext_arxiv_identity_regression_is_rejected(self) -> None:
        bib = self.paper / "references.bib"
        content = bib.read_text(encoding="utf-8")
        self.assertIn("eprint = {2608.16289}", content)
        broken = content.replace("eprint = {2608.16289}", "eprint = {2608.16290}")
        broken = broken.replace("url = {https://arxiv.org/abs/2608.16289}",
                                "url = {https://arxiv.org/abs/2608.16290}")
        bib.write_text(broken, encoding="utf-8")
        errors, _ = validator.validate(self.paper)
        self.assertTrue(any("Stale/incorrect identity match method: CGD-103" in e for e in errors))

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
