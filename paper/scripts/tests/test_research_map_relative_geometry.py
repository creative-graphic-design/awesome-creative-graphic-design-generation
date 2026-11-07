"""Guard the research-map card's proportional spacing and alignment contract."""

from pathlib import Path
import unittest

SOURCE = Path(__file__).resolve().parents[2] / "figs/tex/research_map_narrative.tex"


class ResearchMapRelativeGeometryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = SOURCE.read_text(encoding="utf-8")

    def test_padding_is_derived_from_shared_width(self):
        self.assertIn(r"\setlength{\MapCardPaddingX}{.025\MapCardWidth}", self.source)
        self.assertIn(r"\setlength{\MapCardPaddingY}{.0125\MapCardWidth}", self.source)
        self.assertIn(r"\dimexpr\MapCardWidth-2\MapCardPaddingX\relax", self.source)
        self.assertIn(r"inner xsep=\MapCardPaddingX", self.source)
        self.assertIn(r"inner ysep=\MapCardPaddingY", self.source)

    def test_content_uses_relative_quarter_and_equal_halves(self):
        self.assertIn(r"\setlength{\MapCardLogoWidth}{.25\linewidth}", self.source)
        self.assertIn(r"\setlength{\MapCardTextWidth}{.75\linewidth}", self.source)
        self.assertIn(r"\setlength{\MapCardLogoHeight}{2\MapCardRowHeight}", self.source)
        self.assertEqual(self.source.count(r"\vbox to \MapCardRowHeight"), 2)
        self.assertIn(r"\parbox[c][\MapCardLogoHeight][c]{\MapCardLogoWidth}{\centering #4}", self.source)

    def test_logo_is_bounded_by_relative_width_and_height(self):
        self.assertIn(
            r"\includegraphics[width=.8\MapCardLogoWidth,height=.8\MapCardLogoHeight,keepaspectratio]",
            self.source,
        )


if __name__ == "__main__":
    unittest.main()
