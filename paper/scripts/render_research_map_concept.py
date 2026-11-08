#!/usr/bin/env python3
"""Source-audited, print-legible graphic-design research map.

Reads the 26 audited node declarations rather than maintaining hand-tuned
coordinates for individual papers. The same output is used by the manuscript and CI.
"""
from __future__ import annotations

import csv
import html
import re
import subprocess
import tempfile
from xml.etree import ElementTree as ET
from collections import defaultdict
from pathlib import Path

PAPER = Path(__file__).resolve().parents[1]
TEX = PAPER / "figs/tex/research_map_narrative.tex"
AUDIT = PAPER / "figs/tex/research_map_narrative_sources.csv"
OUTPUT = PAPER / "figs/pdf/research_map_concept.svg"
W, H = 1050, 1080
X0, STEP = 260, 190
Y0, LANE_STEP = 248, 180
ERAS = ((2019, 2021), (2022, 2023), (2024, 2025), (2026, 2026))
LANES = (
    ("A", "LAYOUT GENERATION", "Geometry and constraints", "#2C86B6"),
    ("B", "POSTERS & ADS", "Text and imagery", "#CB7A47"),
    ("C", "STRUCTURED ARTIFACTS", "Paths, layers and objects", "#368B7B"),
    ("D", "DOCUMENT WORKFLOWS", "Slides, figures and reflow", "#8067BA"),
)
STYLES = {
    "gan": ("#C07553", "GAN"),
    "latent": ("#6583A7", "VAE / TRANSFORMER"),
    "diff": ("#3289C1", "DIFFUSION / FLOW"),
    "agent": ("#8A69B6", "LM / AGENT"),
    "struct": ("#329783", "VECTOR / CODE"),
    "edit": ("#B85C81", "EDITING"),
}
# Matches either single-logo, dual-logo, or logo-free source declarations.
NODE = re.compile(
    r"^\\MapPaper(?:Brand|BrandPair)?\{([A-D])\}\{([^{}]+)\}\{(\d{2})\}"
    r"\{([a-z0-9]+)\}\{\\MapCol[^{}]+\}\{\\MapRow[^{}]+\}"
    r"\{([a-z]+)\}\{([^{}]+)\}", re.M
)

def source_logo_mapping(source: str) -> dict[str, tuple[str, ...]]:
    """Read affiliations from the same audited TeX declarations as the map.

    Never maintain a second, drifting hand-written institution list.
    """
    logos: dict[str, tuple[str, ...]] = {}
    for match in NODE.finditer(source):
        name = match.group(2)
        tail = source[match.end():].split("\n", 1)[0]
        pair = re.match(r"\{\\MapLogoPair\{([a-z-]+)\}\{([a-z-]+)\}\}", tail)
        single = re.match(r"\{([a-z-]+)\}", tail)
        if pair:
            logos[name] = pair.groups()
        elif single:
            logos[name] = (single.group(1),)
    return logos


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)

def main() -> None:
    source = TEX.read_text(encoding="utf-8")
    entries = NODE.findall(source)
    logos = source_logo_mapping(source)
    with AUDIT.open(encoding="utf-8", newline="") as handle:
        audited = {(r["track"], r["label"], r["bibtex_key"], r["reference_year"], r["method_family"]) for r in csv.DictReader(handle)}
    actual = {(track, name, key, "20"+year, family) for track, name, year, key, family, _ in entries}
    assert len(entries) == 26 and actual == audited, "Narrative nodes differ from audited CSV"
    assert len(logos) == 21, f"Expected affiliation marks for 21 audited cards, got {len(logos)}"
    buckets = defaultdict(list)
    for track, name, year, key, family, detail in entries:
        reference_year = 2000 + int(year)
        period = next(i for i, (lo, hi) in enumerate(ERAS) if lo <= reference_year <= hi)
        buckets[(track, period)].append((name, family, detail, year))
    out: list[str] = []
    def add(x: str) -> None: out.append(x)
    def rect(x, y, w, h, fill, stroke="none", radius=0, sw=1):
        add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')
    def line(x1, y1, x2, y2, color="#DDE6EE", width=1):
        add(f'<path d="M{x1} {y1} L{x2} {y2}" fill="none" stroke="{color}" stroke-width="{width}"/>')
    def label(x, y, value, size=14, color="#253D56", weight=400):
        add(f'<text x="{x}" y="{y}" font-family="DejaVu Sans,Arial,sans-serif" font-size="{size}" font-weight="{weight}" fill="{color}">{esc(value)}</text>')
    def logo_at(stem: str, x: float, y: float, size: float) -> bool:
        source = PAPER / "figs/assets/logos" / (stem + ".pdf")
        if not source.is_file():
            return False
        with tempfile.TemporaryDirectory(prefix="research-map-mark-") as directory:
            target = Path(directory) / "logo.svg"
            subprocess.run(["pdftocairo", "-svg", str(source), str(target)],
                           check=True, stdout=subprocess.DEVNULL)
            symbol = ET.parse(target).getroot()
        # Cairo reuses IDs such as "clip-0" and "source-5" for each PDF.
        # Scope every SVG definition and every reference to this placement;
        # otherwise embedded logos may share the wrong clipping paths.
        prefix = f"mark-{stem.replace('-', '_')}-{int(x)}-{int(y)}-"
        remap = {}
        for element in symbol.iter():
            original = element.get("id")
            if original:
                remap[original] = prefix + original
        for element in symbol.iter():
            for key, value in list(element.attrib.items()):
                if key == "id" and value in remap:
                    element.set(key, remap[value])
                else:
                    for old_id, new_id in remap.items():
                        value = value.replace(f"url(#{old_id})", f"url(#{new_id})")
                        if value == f"#{old_id}":
                            value = f"#{new_id}"
                    element.set(key, value)
        symbol.set("x", str(x))
        symbol.set("y", str(y))
        symbol.set("width", str(size))
        symbol.set("height", str(size))
        add(ET.tostring(symbol, encoding="unicode"))
        return True

    # Layout geometry derives from a four-period grid, never study-specific x/y.
    add(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
    rect(0, 0, W, H, "#F8FAFD")
    rect(0, 0, W, 122, "#173552")
    label(31, 48, "RESEARCH LANDSCAPE OF GENERATIVE GRAPHIC DESIGN", 20, "#FFFFFF", 700)
    label(32, 82, "From learned layouts to editable documents and native artifacts", 15, "#C4D6E5")
    rect(20, 146, W-40, 70, "#E8EEF5", radius=10)
    label(38, 184, "CITED YEAR", 13, "#647D92", 700)
    for period, (first, last) in enumerate(ERAS):
        x = X0 + STEP*period
        year_text = str(first) if first == last else f"{first}–{last}"
        label(x+10, 187, year_text, 17, "#29455E", 700)

    for lane, (track, title, description, accent) in enumerate(LANES):
        y = Y0 + lane*LANE_STEP
        rect(20, y-17, W-40, LANE_STEP-7, "#FFFFFF", radius=10)
        rect(20, y-17, 6, LANE_STEP-7, accent, radius=3)
        label(39, y+23, f"0{lane+1}", 23, accent, 700)
        label(39, y+57, title, 15, "#234059", 700)
        label(39, y+80, description, 11, "#73889D")
        for period in range(len(ERAS)):
            x = X0 + period*STEP + 3
            cards = buckets[(track, period)]
            assert len(cards) <= 2, (track, period, cards)
            for index, (name, family, detail, year) in enumerate(cards):
                cy = y + 8 + index*78
                color, _family_name = STYLES[family]
                card_w, card_h = 179, 69
                rect(x, cy, card_w, card_h, "#FFFFFF", color, radius=7, sw=1.5)
                rect(x, cy, 5, card_h, color, radius=2)
                marks = logos.get(name, ())
                title_x = x + (41 if marks else 12)
                # Keep titles within the card even when a source logo is present.
                title_size = 13 if marks and len(name)>=11 else 12 if len(name)>15 else 14
                label(title_x, cy+26, name, title_size, "#213B53", 700)
                label(x+12, cy+53, detail, 11 if len(detail)<=23 else 10, "#698097")
                label(x+card_w-27, cy+15, f"'{year}", 9, "#8B9BAC")
                if len(marks) == 1:
                    assert logo_at(marks[0], x+12, cy+7, 24), (name, marks)
                elif len(marks) == 2:
                    assert logo_at(marks[0], x+10, cy+5, 17), (name, marks)
                    assert logo_at(marks[1], x+23, cy+18, 17), (name, marks)

    footer_y = Y0 + (len(LANES)-1)*LANE_STEP + LANE_STEP - 3
    rect(20, footer_y+14, W-40, 95, "#E8EEF5", radius=10)
    label(38, footer_y+43, "METHOD FAMILY", 12, "#60798F", 700)
    # Two rows of three legend items, using a fixed column grid.
    # Long family labels cannot consume the neighboring legend's padding.
    for i, (color, family_name) in enumerate(STYLES.values()):
        legend_x = 190 + 270*(i % 3)
        legend_y = footer_y + 23 + 19*(i // 3)
        rect(legend_x, legend_y, 13, 13, "#FFFFFF", color, radius=2)
        label(legend_x+19, legend_y+11, family_name, 10, "#36536B", 600)
    label(38, footer_y+76, "X = cited-reference period; row = primary task; border = method family; logos = audited affiliations.", 11, "#60798F")
    label(38, footer_y+94, "Representative milestones, not a census. Proximity does not imply citation or causal influence.", 11, "#60798F")
    add("</svg>")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text("\n".join(out)+"\n", encoding="utf-8")
    print(f"Generated {len(entries)} audited narrative nodes: {OUTPUT}")

if __name__ == "__main__":
    main()
