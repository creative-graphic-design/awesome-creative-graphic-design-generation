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
        self.assertIn(r"\setlength{\MapCardContentWidth}{\MapCardWidth}", self.source)
        self.assertIn(r"inner xsep=\MapCardPaddingX", self.source)
        self.assertIn(r"inner ysep=\MapCardPaddingY", self.source)

    def test_content_uses_relative_quarter_and_equal_halves(self):
        self.assertIn(r"\setlength{\MapCardLogoWidth}{.25\linewidth}", self.source)
        self.assertIn(r"\setlength{\MapCardTextWidth}{.75\linewidth}", self.source)
        self.assertIn(r"\setlength{\MapCardLogoHeight}{2\MapCardRowHeight}", self.source)
        self.assertIn(r"\setlength{\MapCardRowHeight}{.055\linewidth}", self.source)
        self.assertEqual(self.source.count(r"\vbox to \MapCardRowHeight"), 2)
        self.assertIn(r"\parbox[c][\MapCardLogoHeight][c]{\MapCardLogoWidth}{\centering #4}", self.source)

    def test_all_card_positions_use_relative_grid(self):
        self.assertIn(r"\setlength{\MapCardMarginX}{.172619\MapCardWidth}", self.source)
        self.assertIn(r"\setlength{\MapCardRowPitch}{.244048\MapCardWidth}", self.source)
        self.assertIn(r"\dimexpr\MapColOne+\MapCardWidth+\MapCardMarginX\relax", self.source)
        self.assertIn(r"\dimexpr\MapRowATop-\MapCardRowPitch\relax", self.source)
        import re

        cards = re.findall(
            r"^\\MapPaper(?:Brand)?\{[A-D]\}\{[^{}]+\}\{\d+\}\{[^{}]+\}"
            r"\{\\MapCol(?:One|Two|Three|Four)\}"
            r"\{\\MapRow(?:A|B|C|D)(?:Top|Bottom)\}",
            self.source,
            re.MULTILINE,
        )
        self.assertEqual(len(cards), 26)

    def test_logo_is_bounded_by_relative_width_and_height(self):
        self.assertIn(
            r"\includegraphics[width=.64\MapCardLogoWidth,height=.72\MapCardLogoHeight,keepaspectratio,clip]",
            self.source,
        )


if __name__ == "__main__":
    unittest.main()
