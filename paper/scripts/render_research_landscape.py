#!/usr/bin/env python3
"""Render the audited 67-study research atlas from the single source CSV.

Design tokens, data and geometry are deliberately separate. No per-study
coordinates. The SVG stays vector and is converted to PDF by rsvg-convert.
"""
from __future__ import annotations

import csv
import html
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "figs/tex/research_map_sources.csv"
OUTPUT = ROOT / "figs/pdf/research_landscape.svg"

# Shared design tokens; these are the ONLY spatial values to change in a redesign.
WIDTH, HEIGHT = 1830, 1330
LEFT, TOP = 320, 168
CELL_W, ROW_H = 355, 167
COL_GAP, ROW_GAP = 15, 15
CARD_H, CARD_GAP = 27, 5
PADDING = 18
FAMILIES = (
    ("A", "LAYOUT GENERATION", "Geometry, conditions and constraints", "#287BA8"),
    ("B", "POSTERS & ADVERTISING", "Composition of images and typography", "#C16D4B"),
    ("C", "VECTOR & TYPOGRAPHY", "Structured marks, paths and lettering", "#288F83"),
    ("D", "EDITABLE DESIGN", "Layers, objects and iterative operations", "#845FB0"),
    ("F", "DOCUMENT WORKFLOWS", "Slides, figures and native documents", "#4C78A3"),
    ("E", "SURVEYS & EVALUATION", "Taxonomies, benchmarks and validity", "#A36879"),
)
ERAS = ((2019, 2021), (2022, 2023), (2024, 2025), (2026, 2026))


def xml(value: object) -> str:
    return html.escape(str(value), quote=True)


def draw() -> str:
    with SOURCE.open(encoding="utf-8", newline="") as handle:
        records = list(csv.DictReader(handle))
    assert len(records) == 67, f"Expected 67 audited studies, got {len(records)}"
    keys = [r["bibtex_key"] for r in records]
    assert len(keys) == len(set(keys)), "Repeated bibliography keys"

    groups = defaultdict(list)
    for row in records:
        year = int(row["reference_year"])
        assert row["track"] in {item[0] for item in FAMILIES}
        assert 2019 <= year <= 2026
        period = next(i for i, (start, end) in enumerate(ERAS) if start <= year <= end)
        groups[(row["track"], period)].append(row)

    pieces: list[str] = []
    def add(value: str) -> None:
        pieces.append(value)

    def rect(x, y, w, h, fill, radius=0, stroke="none", stroke_width=1):
        add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}"/>')

    def text(x, y, value, size=15, color="#243A50", weight=400, anchor="start"):
        add(f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" '
            f'font-family="DejaVu Sans,Arial,sans-serif" font-weight="{weight}" '
            f'fill="{color}">{xml(value)}</text>')

    add(f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" '
        f'height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">')
    rect(0, 0, WIDTH, HEIGHT, "#F7F9FC")
    rect(0, 0, WIDTH, 116, "#153552")
    text(36, 54, "RESEARCH LANDSCAPE OF GENERATIVE GRAPHIC DESIGN", 26, "#FFFFFF", 700)
    text(38, 88, "67 audited milestones  •  six research domains  •  cited-reference years", 16, "#C4D6E5")
    for ci, (start, end) in enumerate(ERAS):
        x = LEFT + ci * (CELL_W + COL_GAP)
        rect(x, 129, CELL_W, 50, "#E3ECF4", radius=9)
        text(x + 18, 160, f"{start}–{end}" if start != end else str(start),
             21, "#213D56", 700)
    text(38, 155, "RESEARCH TASK / YEAR", 13, "#60778C", 700)
    for ri, (code, name, explanation, color) in enumerate(FAMILIES):
        y = TOP + 25 + ri * (ROW_H + ROW_GAP)
        rect(23, y, WIDTH - 46, ROW_H, "#FFFFFF", radius=12)
        rect(23, y, 7, ROW_H, color, radius=3)
        text(47, y + 38, f"0{ri + 1}", 27, color, 700)
        text(46, y + 71, name, 15, "#1E354C", 700)
        text(46, y + 95, explanation, 11, "#71859B")
        for ci in range(4):
            x = LEFT + ci * (CELL_W + COL_GAP)
            bucket = groups[(code, ci)]
            rect(x, y + 9, CELL_W, ROW_H - 18, "#F7F9FC",
                 radius=8, stroke="#E1E8F0")
            # Token-based row layout. All cards are identical, except their text.
            max_cards = (ROW_H - 18 - 2 * PADDING + CARD_GAP) // (CARD_H + CARD_GAP)
            assert len(bucket) <= max_cards, (code, ci, len(bucket))
            for index, row in enumerate(bucket):
                cy = y + 9 + PADDING + index * (CARD_H + CARD_GAP)
                rect(x + PADDING, cy, CELL_W - 2 * PADDING, CARD_H,
                     "#FFFFFF", radius=5, stroke="#DBE4EC")
                rect(x + PADDING, cy, 4, CARD_H, color, radius=2)
                label = row["label"]
                assert len(label) <= 26, f"Long research label: {label}"
                text(x + PADDING + 14, cy + 19, label, 13, "#263D53", 600)
                text(x + CELL_W - PADDING - 11, cy + 19,
                     f"’{str(row['reference_year'])[-2:]}", 12, "#657B90",
                     anchor="end")

    footer_y = TOP + 25 + len(FAMILIES) * (ROW_H + ROW_GAP) + 4
    text(34, footer_y, "Placement encodes research task × citation period; neighboring studies do not imply citation, lineage, or causal dependence.",
         13, "#687F94")
    text(34, footer_y + 27, "Selection is illustrative, not an exhaustive census. Years follow the bibliography; preprint dates can differ.",
         12, "#8293A4")
    add("</svg>")
    return "\n".join(pieces) + "\n"


if __name__ == "__main__":
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    content = draw()
    OUTPUT.write_text(content, encoding="utf-8")
    print(f"Rendered {SOURCE} -> {OUTPUT}")
