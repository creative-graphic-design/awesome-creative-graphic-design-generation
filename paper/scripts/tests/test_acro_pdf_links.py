"""Negative regression fixtures for generated acro PDF hyperlink targets."""

import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from check_acro_pdf_links import validate


class AcroPdfLinkTests(unittest.TestCase):
    SOURCE = r"""
\DeclareAcronym{a}{
  paperurl = {https://arxiv.org/abs/2608.16289},
  doi = {10.1000/test}
}
\DeclareAcronym{b}{
  paperurl = {https://arxiv.org/abs/2608.16289}
}
"""
    GOOD = """Page  Type          URL
   1  Annotation    https://arxiv.org/abs/2608.16289
   1  Annotation    https://arxiv.org/abs/2608.16289
   1  Annotation    https://doi.org/10.1000/test
"""

    def test_valid_duplicate_paper_links(self):
        self.assertEqual(validate(self.GOOD, self.SOURCE), (2, 1, []))

    def test_missing_second_occurrence_is_rejected(self):
        data = self.GOOD.replace("   1  Annotation    https://arxiv.org/abs/2608.16289\n", "", 1)
        _, _, issues = validate(data, self.SOURCE)
        self.assertTrue(any("Missing 1 of 2" in e for e in issues))

    def test_macro_literal_doi_is_rejected(self):
        data = self.GOOD.replace("https://doi.org/10.1000/test", r"https://doi.org/\acrowrite {doi}")
        _, _, issues = validate(data, self.SOURCE)
        self.assertTrue(any("Unexpanded TeX macro" in e for e in issues))
        self.assertTrue(any("Missing 1" in e for e in issues))

    def test_broken_gotor_paper_links_not_treated_as_uri(self):
        data = "Page  Type          URL\n   1  Annotation    https://doi.org/10.1000/test\n"
        _, _, issues = validate(data, self.SOURCE)
        self.assertTrue(any("Missing 2 of 2" in e for e in issues))

    def test_empty_registry_fails_closed(self):
        _, _, issues = validate(self.GOOD, "")
        self.assertTrue(any("No acro paperurl" in e for e in issues))


if __name__ == "__main__":
    unittest.main()
