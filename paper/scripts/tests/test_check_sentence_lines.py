"""Positive and negative controls for the manuscript sentence-line guard."""
from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from check_sentence_lines import bad_sentence_line, check_files, strip_comment


class SentenceLineCheckerTests(unittest.TestCase):
    def test_rejects_multiple_ordinary_sentences(self) -> None:
        self.assertTrue(bad_sentence_line("First claim ends. Another claim starts."))

    def test_rejects_multiple_caption_sentences(self) -> None:
        self.assertTrue(bad_sentence_line(r"\caption{First claim ends. The next claim starts.}"))

    def test_accepts_single_sentence(self) -> None:
        self.assertFalse(bad_sentence_line(r"Prior work is relevant \citep{huang2023survey}."))

    def test_handles_abbreviations_and_initials(self) -> None:
        self.assertFalse(bad_sentence_line("Refer to Fig. 2 and Dr. Smith's text."))
        self.assertFalse(bad_sentence_line("The work of J. Smith is useful."))
        self.assertFalse(bad_sentence_line("The method of Huang et al. remains influential."))

    def test_ignores_comment_and_preserves_escaped_percent(self) -> None:
        self.assertFalse(bad_sentence_line("Good sentence. % Ignored. Another ignored."))
        self.assertEqual(strip_comment(r"Accuracy was 95\%. % trailing note"), r"Accuracy was 95\%. ")

    def test_reports_violation_location(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "02_introduction.tex"
            path.write_text("A sentence.\nTwo sentences. An extra sentence.\n", encoding="utf-8")
            issues = check_files([path])
            self.assertEqual(len(issues), 1)
            self.assertEqual(issues[0][1], 2)


if __name__ == "__main__":
    unittest.main()
