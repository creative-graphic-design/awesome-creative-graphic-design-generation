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
W, H = 1320, 1315
X0, STEP = 264, 260
Y0, LANE_STEP = 411, 174
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

    # Research-map layout: a dated interpretive technology map, not a paper table.
    # Major transitions are conceptual comparison labels, never causal arrows.
    add(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
    rect(0, 0, W, H, "#F8FAFC")
    rect(0, 0, W, 120, "#18364F")
    label(35, 51, "GRAPHIC DESIGN GENERATION: A RESEARCH MAP", 30, "#FFFFFF", 700)
    label(37, 87, "Representative systems  ·  2019–2026  ·  research questions, models, and editable outputs", 17, "#C9DBE8")

    # Four illustrated developments sit above the dated evidence. Each is a
    # research *theme*, not a claim of direct influence from one study to another.
    label(35, 152, "WHAT CHANGED?", 16, "#385773", 700)
    label(208, 152, "Illustrative themes — not a model genealogy", 13, "#73899B")
    themes = (
        ("GEOMETRY", "Where do elements go?", "#DDECF6", "#2C86B6"),
        ("CONDITIONING", "What guides composition?", "#FBEBE2", "#CB7A47"),
        ("STRUCTURE", "What remains editable?", "#E3F1ED", "#368B7B"),
        ("WORKFLOWS", "How are documents revised?", "#ECE8F8", "#8067BA"),
    )
    def paper_sample(px, py, kind, color):
        rect(px, py, 84, 84, "#FFFFFF", "#C9D6DF", radius=5)
        if kind == 0:
            for xx, yy, ww, hh in ((9,9,64,13),(9,29,22,38),(37,29,36,18),(37,53,36,14)):
                rect(px+xx,py+yy,ww,hh,"#E5F0F7",color,radius=2,sw=1.5)
        elif kind == 1:
            rect(px+9,py+9,66,66,"#F2DFD2",radius=2)
            rect(px+15,py+16,54,30,"#B6C8D0",radius=2)
            label(px+18,py+63,"DESIGN",11,"#8B6247",700)
        elif kind == 2:
            for xx,yy in ((9,18),(15,13),(21,8)):
                rect(px+xx,py+yy,49,51,"none",color,radius=3)
            for dx,dy in ((16,21),(53,21),(16,54),(53,54)):
                rect(px+dx,py+dy,5,5,"#FFFFFF",color)
        else:
            rect(px+14,py+11,54,63,"#F5F1FC","#9F91C4",radius=2)
            rect(px+22,py+20,38,11,"#D7CDEA",radius=2)
            for yy in (40,50,60):
                rect(px+22,py+yy,38,4,"#B5AACF",radius=2)
    for i, (head, question, fill, accent) in enumerate(themes):
        px=25+i*324
        rect(px, 174, 306, 131, "#FFFFFF", "#DCE6ED", radius=10)
        rect(px, 174, 306, 7, accent, radius=3)
        paper_sample(px+13,py if False else 191,i,accent)
        label(px+111,217,head,18,"#27445B",700)
        label(px+111,245,question,14,"#5B7487")
        label(px+111,276,("layout prediction","visual/text constraints","vectors and layers","slide and figure objects")[i],12,"#7C90A0")

    # Each row is a stream of research questions; the horizontal axis supplies
    # dates, and border colors convey the *model family*. The faint directional
    # spine is a reading guide and does not assert citation or model ancestry.
    label(36, 351, "PRIMARY RESEARCH TASK", 13, "#587389", 700)
    for period, (first, last) in enumerate(ERAS):
        x=X0+period*STEP
        yr=str(first) if first==last else f"{first}–{last}"
        label(x+12,350,yr,19,"#26455E",700)
    for lane, (track, name, description, accent) in enumerate(LANES):
        y=Y0+lane*LANE_STEP
        rect(21,y-42,W-42,164,"#FFFFFF",radius=11,stroke="#E3EAF0")
        rect(21,y-42,7,164,accent,radius=3)
        label(40,y-9,name,16,"#29465B",700)
        label(40,y+16,description,12,"#6D8498")
        # horizontal track backbone under all representative system cards
        line(251,y+56,W-34,y+56,"#D2DFE7",2.8)
        add(f'<path d="M{W-41} {y+50} L{W-31} {y+56} L{W-41} {y+62}" fill="none" stroke="#C5D5E0" stroke-width="2"/>')
        for period in range(len(ERAS)):
            x=X0+period*STEP
            cards=buckets[(track,period)]
            assert len(cards)<=2,(track,period,cards)
            # Companion nodes are staggered around the trajectory, with a
            # compact lower tier when there are two studies in a period.
            for index,(label_name,family,detail,year) in enumerate(cards):
                cy=y+3+index*65
                color,_=STYLES[family]
                card_w,card_h=242,61
                rect(x,cy,card_w,card_h,"#FFFFFF",color,radius=7,sw=1.7)
                rect(x,cy,5,card_h,color,radius=2)
                marks=logos.get(label_name,())
                title_x=x+(48 if marks else 15)
                title_size=16 if len(label_name)<=14 else 14
                label(title_x,cy+23,label_name,title_size,"#213A4E",700)
                label(x+15,cy+46,detail,13 if len(detail)<=24 else 12,"#6B8194")
                if len(marks)==1:
                    assert logo_at(marks[0],x+12,cy+6,29),(label_name,marks)
                elif len(marks)==2:
                    assert logo_at(marks[0],x+9,cy+5,20),(label_name,marks)
                    assert logo_at(marks[1],x+24,cy+21,20),(label_name,marks)

    # Lower panel puts the representation question into graphic-document terms.
    foot_y=Y0+len(LANES)*LANE_STEP-36
    rect(21,foot_y,W-42,130,"#E9F0F6",radius=11)
    label(40,foot_y+27,"A CROSS-CUTTING QUESTION",16,"#27445B",700)
    label(40,foot_y+53,"From visual quality alone to controllable and revisable design artifacts",15,"#4D687E")
    # This schematic explicitly shows an editable document's object structure.
    x=755
    rect(x,foot_y+16,150,88,"#FFFFFF","#BFCEDA",radius=7)
    for xx,yy,ww,hh in ((13,12,124,16),(13,35,49,38),(70,35,67,16),(70,57,67,16)):
        rect(x+xx,foot_y+16+yy,ww,hh,"#DCE8EF","#6B92B2",radius=2)
    add(f'<path d="M{x+162} {foot_y+60} L{x+208} {foot_y+60}" stroke="#657F9A" stroke-width="3" fill="none"/>')
    add(f'<path d="M{x+200} {foot_y+53} L{x+209} {foot_y+60} L{x+200} {foot_y+67}" stroke="#657F9A" stroke-width="3" fill="none"/>')
    rect(x+223,foot_y+16,155,88,"#FFFFFF","#B9ADDA",radius=7)
    for j in range(3):
        rect(x+233+j*8,foot_y+30+j*9,95,42,"none","#8D78B8",radius=4)
    label(40,foot_y+89,"Illustrations are author-made abstractions; no implied paper-to-paper lineage.",12,"#758B9D")

    # Consistent legend separated from study labels, with enough font size
    # to remain readable when scaled to a two-column paper figure.
    legend_y=foot_y+155
    label(39,legend_y,"MODEL FAMILIES",13,"#4F6B81",700)
    for i,(color,name) in enumerate(STYLES.values()):
        xx=238+(i%3)*335
        yy=legend_y-13+(i//3)*28
        rect(xx,yy,16,16,"#FFFFFF",color,radius=3,sw=2)
        label(xx+23,yy+14,name,14,"#3E5A70",600)
    label(40,H-25,"Positions encode task and cited-reference period. Adjacent methods are not necessarily related.",13,"#70879A")
    add("</svg>")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text("\n".join(out)+"\n", encoding="utf-8")
    print(f"Generated {len(entries)} audited narrative nodes: {OUTPUT}")

if __name__ == "__main__":
    main()
