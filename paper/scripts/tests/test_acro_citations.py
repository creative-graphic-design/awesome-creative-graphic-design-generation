"""Regression tests for the source-level acro citation convention."""
import re
import unittest

CITE_KEY = re.compile(r"(?m)^\s*cite\s*=\s*\{([^}]+)\}")
DUPLICATE = re.compile(r"\\ac\{([^}]+)\}[ \t]*~?[ \t]*\\citep\{([^}]+)\}")


class TestAcroFirstUseCitation(unittest.TestCase):
    def test_registered_source_is_parsed(self):
        self.assertEqual(CITE_KEY.search("  cite = {cole2023},").group(1), "cole2023")

    def test_redundant_same_source_is_detected(self):
        self.assertEqual(DUPLICATE.findall(r"\ac{cole} \citep{cole2023}"),
                         [("cole", "cole2023")])

    def test_independent_evidence_remains_distinct(self):
        sources = {"cole": "cole2023"}
        matches = DUPLICATE.findall(r"\ac{cole} \citep{other2025}")
        self.assertTrue(all(sources.get(k) != cite for k, cite in matches))

    def test_plain_acro_is_valid(self):
        self.assertEqual(DUPLICATE.findall(r"\ac{cole}"), [])

    def test_optional_tilde_spacing(self):
        self.assertEqual(DUPLICATE.findall(r"\ac{cole}~\citep{cole2023}"),
                         [("cole", "cole2023")])


if __name__ == "__main__":
    unittest.main()
