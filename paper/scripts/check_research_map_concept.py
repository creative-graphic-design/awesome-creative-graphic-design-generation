#!/usr/bin/env python3
"""Validate the actual generated narrative research-map SVG, including nested logos."""
from __future__ import annotations

import csv
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

PAPER = Path(__file__).resolve().parents[1]
SVG = Path(sys.argv[1]) if len(sys.argv) > 1 else PAPER / "figs/pdf/research_map_concept.svg"
AUDIT = PAPER / "figs/tex/research_map_narrative_sources.csv"
NS = "{http://www.w3.org/2000/svg}"

root = ET.parse(SVG).getroot()
assert root.tag == NS + "svg", "Expected valid root SVG"
assert root.attrib["viewBox"] == "0 0 1680 1330", "Unexpected canvas bounds"
with AUDIT.open(encoding="utf-8", newline="") as handle:
    entries = list(csv.DictReader(handle))
assert len(entries) == 26 and len({row["bibtex_key"] for row in entries}) == 26

texts = ["".join(element.itertext()) for element in root.iter(NS + "text")]
for record in entries:
    assert record["label"] in texts, f"Missing map card: {record['label']}"
ids = [element.get("id") for element in root.iter() if element.get("id") is not None]
assert len(ids) == len(set(ids)), "PDF-to-SVG logo definitions collide across cards"
defined = set(ids)
for element in root.iter():
    for value in element.attrib.values():
        for target in re.findall(r"url\(#([^)]+)\)", value):
            assert target in defined, f"Missing SVG reference: {target}"
        if value.startswith("#") and value[1:] not in defined:
            # Colors such as #FFFFFF are legal attributes, unlike href references.
            continue
assert len(root.findall(f".//{NS}rect")) >= 26, "No paper-card geometry"
print(f"PASS: {len(entries)} cited paper labels, {len(ids)} unique SVG defs, valid references")
