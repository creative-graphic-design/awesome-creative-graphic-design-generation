#!/usr/bin/env python3
"""Verify that the proportional 50/50 title/subtitle rows retain consistent separation.

Requires Poppler's pdftotext, already installed for figure preview CI.
Use the actual vector PDF rather than checking only a TeX macro setting.\nThe two equal-height rows form a compact, vertically centered stack.
"""

from pathlib import Path
import re
import subprocess
import sys
import xml.etree.ElementTree as ET


SOURCE = Path(__file__).resolve().parents[1] / "figs" / "tex" / "research_map_narrative.tex"
STUDY = re.compile(
    r"^\\MapPaper(?:Brand|BrandPair)?\{[A-D]\}\{([^{}]+)\}\{\d{2}\}\{[a-z0-9]+\}"
    r"\{[^{}]+\}\{[^{}]+\}\{[a-z]+\}\{([^{}]+)\}(?:\{[a-z-]+\})?$",
    re.MULTILINE,
)


def source_pairs() -> list[tuple[str, str]]:
    studies = STUDY.findall(SOURCE.read_text(encoding="utf-8"))
    if len(studies) != 26 or len({label for label, _ in studies}) != 26:
        raise SystemExit("Expected 26 uniquely named source study cards")
    return [(label, subtitle.split()[0]) for label, subtitle in studies]
MAX_GAP_PT = 3.0
MIN_GAP_PT = 0.0


def verify(pdf_path: Path) -> None:
    result = subprocess.run(
        ["pdftotext", "-bbox", str(pdf_path), "-"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )
    root = ET.fromstring(result.stdout)
    words = [
        (node.text or "", float(node.attrib["xMin"]),
         float(node.attrib["yMin"]), float(node.attrib["yMax"]))
        for node in root.iter()
        if node.tag.endswith("word")
    ]

    for title, subtitle_first_word in source_pairs():
        titles = [word for word in words if word[0] == title]
        if len(titles) != 1:
            raise SystemExit(f"Expected one study title {title!r}, got {len(titles)}")
        word = titles[0]
        subtitles = [
            candidate for candidate in words
            if candidate[0] == subtitle_first_word
            and abs(candidate[1] - word[1]) < 0.6
            and 0 <= candidate[2] - word[3] < 20
        ]
        if len(subtitles) != 1:
            raise SystemExit(
                f"{title}: subtitle {subtitle_first_word!r} missing or misaligned"
            )
        gap = subtitles[0][2] - word[3]
        if not MIN_GAP_PT <= gap <= MAX_GAP_PT:
            raise SystemExit(
                f"{title}: title/subtitle gap is {gap:.2f}pt "
                f"(allowed {MIN_GAP_PT}..{MAX_GAP_PT}pt)"
            )
        print(f"PASS {title}: title/subtitle gap {gap:.2f}pt")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: check_research_map_card_spacing.py figure.pdf")
    verify(Path(sys.argv[1]))
