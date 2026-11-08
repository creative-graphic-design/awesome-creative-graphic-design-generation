"""Structural contract for independently positioned, proportional map cards."""

from pathlib import Path
import re
import unittest

SOURCE = Path(__file__).resolve().parents[2] / "figs/tex/research_map_narrative.tex"


class ResearchMapRelativeGeometryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = SOURCE.read_text(encoding="utf-8")

    def test_frame_and_content_geometry(self):
        source = self.source
        for token in (
            r"\setlength{\MapCardHeight}{.20\MapCardWidth}",
            r"\setlength{\MapCardPaddingX}{.04\MapCardWidth}",
            r"\setlength{\MapCardPaddingY}{.016\MapCardWidth}",
            r"\dimexpr\MapCardWidth-2\MapCardPaddingX\relax",
            r"\dimexpr\MapCardHeight-2\MapCardPaddingY\relax",
            r"\setlength{\MapCardLogoWidth}{.25\MapCardContentWidth}",
            r"\setlength{\MapCardTextWidth}{.75\MapCardContentWidth}",
            r"\setlength{\MapCardTextStackHeight}{.84\MapCardContentHeight}",
            r"\setlength{\MapCardRowHeight}{.5\MapCardTextStackHeight}",
            r"\MapCardTitleOffset}{\dimexpr.5\MapCardHeight-.5\MapCardRowHeight\relax}",
            r"\MapCardDetailOffset}{\dimexpr.5\MapCardHeight+.5\MapCardRowHeight\relax}",
            r"minimum width=\MapCardWidth,minimum height=\MapCardHeight",
        ):
            self.assertIn(token, source)
        self.assertNotIn(r"\begin{tabular}", source)

    def test_logo_title_and_detail_use_separate_anchors(self):
        source = self.source
        for token in (
            r"\MapCardLogoCenterX,-.5\MapCardHeight",
            r"\MapCardTextOffset,-\MapCardTitleOffset",
            r"\MapCardTextOffset,-\MapCardDetailOffset",
            r"\includegraphics[width=.72\MapCardLogoWidth,height=.77\MapCardContentHeight,keepaspectratio]",
        ):
            self.assertIn(token, source)

    def test_layoutflow_pair_stays_inside_logo_quarter(self):
        self.assertIn(r"\MapPaperBrandPair{A}{LayoutFlow}{24}{layoutflow2024}", self.source)
        self.assertIn(r"\MapLogoPair{utokyo}{cyberagent-symbol}", self.source)
        self.assertIn(r"at (.30\MapCardLogoWidth,.69\MapCardContentHeight)", self.source)
        self.assertIn(r"at (.70\MapCardLogoWidth,.31\MapCardContentHeight)", self.source)
        self.assertIn(r"\path[use as bounding box] (0pt,0pt) rectangle (\MapCardLogoWidth,\MapCardContentHeight)", self.source)
        self.assertIn(r"width=\MapPairLogoSize,height=\MapPairLogoSize,keepaspectratio", self.source)
        self.assertIn(r"\setlength{\MapPairLogoSize}{.38\MapCardLogoWidth}", self.source)
        self.assertEqual(self.source.count(r"minimum width=\MapPairLogoSize,minimum height=\MapPairLogoSize"), 2)

    def test_card_margins_are_relative(self):
        source = self.source
        self.assertIn(r"\setlength{\MapCardMarginX}{.172619\MapCardWidth}", source)
        self.assertIn(r"\setlength{\MapCardRowPitch}{.232\MapCardWidth}", source)
        self.assertIn(r"\dimexpr\MapColOne+\MapCardWidth+\MapCardMarginX\relax", source)
        self.assertIn(r"\dimexpr\MapRowATop-\MapCardRowPitch\relax", source)
        cards = re.findall(
            r"^\\MapPaper(?:Brand|BrandPair)?\{[A-D]\}\{[^{}]+\}\{\d+\}\{[^{}]+\}"
            r"\{\\MapCol(?:One|Two|Three|Four)\}"
            r"\{\\MapRow(?:A|B|C|D)(?:Top|Bottom)\}",
            source,
            re.MULTILINE,
        )
        self.assertEqual(len(cards), 26)


if __name__ == "__main__":
    unittest.main()
