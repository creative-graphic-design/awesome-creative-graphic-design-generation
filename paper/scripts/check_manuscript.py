#!/usr/bin/env python3
"""Mechanical, CI-enforced checks derived from the author feedback checklist.

Scientific correctness and whether a human actually read the checklist cannot
be proven by this linter; the local commit checklist still must be reviewed.
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

PAPER = Path(__file__).resolve().parents[1]
REPO = PAPER.parent
errors: list[str] = []


def require(test: bool, description: str) -> None:
    if not test:
        errors.append(description)


def tex(path: str) -> str:
    p = PAPER / path
    require(p.is_file(), f"Missing TeX file: {path}")
    return p.read_text(encoding="utf-8") if p.is_file() else ""


for required in (
    "WRITING_CHECKLIST.md",
    "AGENTS.md",
    "figs/tex/README.md",
    "figs/pdf/README.md",
    "tabs/tex/README.md",
    "scripts/build_figures.sh",
):
    require((PAPER / required).is_file(), f"Missing paper review/source-layout file: {required}")
require((REPO / ".pre-commit-config.yaml").is_file(), "Missing local pre-commit rules")

main = tex("main.tex")
intro = tex("sections/02_introduction.tex")
require(r"\usepackage[review]{cvpr}" in main, "Use official anonymous [review] mode")
require(r"\usepackage[pagenumbers]{cvpr}" not in main, "Do not use named-author draft mode")
require("First Author" in main and "Second Author" in main, "Keep the official non-identifying author template block")
require("Authors to be confirmed" not in main, "Remove the old author placeholder")
require(r"\paragraph{" not in intro, "Introduction must read as continuous prose, without artificial paragraph headings")
require(r"\begin{enumerate}" not in intro, "Introduction should not be a numbered list of research questions")
require(r"\cite" in intro, "Introduction needs citations for graphic design and application tasks")
intro_paragraphs = [p for p in re.split(r"\n\s*\n", intro) if p.strip()]
require(len(intro_paragraphs) >= 5, "Introduction must develop a connected academic argument")
require("huang2023survey" in intro and "zou2025fragment" in intro, "Ground the field definition in core surveys")
for citation in ("posterlayout2023", "cglgan2022", "autopresent2025", "bizgen2025", "autofigure2026"):
    require(citation in intro, f"Introduction needs task-specific original evidence: {citation}")
require("figures/" not in main, "Remove legacy figure paths from main.tex")
for stem in ("overview", "edit_protocol", "research_map"):
    root = tex(f"figs/tex/{stem}.tex")
    wrapper = tex(f"figs/tex/{stem}_figure.tex")
    require(r"\documentclass" in root and r"\begin{tikzpicture}" in root, f"{stem} must be standalone TikZ")
    require(f"figs/pdf/{stem}.pdf" in wrapper, f"{stem} wrapper must include generated vector PDF")
    require(r"\caption{" in wrapper and r"\label{" in wrapper, f"{stem} wrapper needs caption and label")
    require(f"figs/tex/{stem}_figure" in main, f"main.tex must input {stem} wrapper")
    require(not (PAPER / "figures" / f"{stem}.tex").exists(), f"Remove legacy figures/{stem}.tex")

table_files = (
    ("03_related_surveys", "prior_surveys"),
    ("04_methodology", "task_grounding"),
    ("05_representations", "representation_crosswalk"),
    ("07_evaluation", "evaluation_metrics"),
    ("08_benchmarks", "benchmark_coverage"),
)
for section, table in table_files:
    body = tex(f"sections/{section}.tex")
    source = tex(f"tabs/tex/{table}.tex")
    require(r"\begin{table" not in body, f"{section}: move table float into tabs/tex")
    require(f"tabs/tex/{table}" in body, f"{section}: missing table source input")
    require(r"\begin{table*}" in source and r"\end{table*}" in source, f"{table}: incomplete table*")
    require(r"\caption{" in source and r"\label{" in source, f"{table}: missing caption or label")

source_files = [PAPER / "main.tex"] + sorted((PAPER / "sections").glob("*.tex"))
source_files += sorted((PAPER / "tabs" / "tex").glob("*.tex"))
source_files += sorted((PAPER / "figs" / "tex").glob("*_figure.tex"))
labels: dict[str, str] = {}
for source in source_files:
    data = source.read_text(encoding="utf-8")
    for name in re.findall(r"\\input\{([^}]+)\}", data):
        require((PAPER / (name + ".tex")).is_file(), f"{source.relative_to(PAPER)}: unresolved input {name}")
    for label in re.findall(r"\\label\{([^}]+)\}", data):
        if label in labels:
            errors.append(f"Duplicate TeX label {label}: {labels[label]} and {source.relative_to(PAPER)}")
        labels[label] = str(source.relative_to(PAPER))
for required_section in (
    "01_abstract", "02_introduction", "03_related_surveys", "04_methodology",
    "05_representations", "06_methods", "07_evaluation", "08_benchmarks",
    "09_discussion", "10_conclusion",
):
    require((PAPER / "sections" / f"{required_section}.tex").is_file(),
            f"Missing ordered manuscript section: {required_section}.tex")
    require(r"\input{sections/" + required_section + "}" in main,
            f"Main TeX must include ordered section {required_section}")
for section_file in (PAPER / "sections").glob("*.tex"):
    require(bool(re.fullmatch(r"\d{2}_[a-z_]+\.tex", section_file.name)),
            f"Non-numbered section file: {section_file.name}")
require(not any(re.search(r"\b[A-Z][A-Za-z-]* et al\.(?:~|\s+)(?:20\d{2}\s+)?\\citep\{", path.read_text(encoding="utf-8"))
                for path in [*(PAPER / "sections").glob("*.tex"), *(PAPER / "tabs" / "tex").glob("*.tex")]),
        "Use \\citet{key} for textual author citations; do not write Author et al.~\\citep{key}")



acro_source = tex("acronyms.tex")
require(r"\usepackage{acro}" in main, "Use the CTAN acro package")
require(r"\input{acronyms}" in main, "Load acro definitions in the preamble")
require(r"\printacronyms[include=abbreviations" in main,
        "Print the abbreviation list using acro")
require(r"\printacronyms[include=systems" in main,
        "Print named systems separately using acro")
require(r"\printacronyms[include=abbreviations,heading=none,display=all]" in main,
        "Print all registered abbreviations, not only already-used ones")
require(r"\printacronyms[include=systems,heading=none,display=all]" in main,
        "Print all registered named systems, not only already-used ones")
require("glossaries" not in main and "printnoidxglossary" not in main,
        "Remove obsolete glossaries declarations")
definitions = re.findall(r"\\DeclareAcronym\{([^}]+)\}\{(.*?)\n\}", acro_source, re.S)
keys = [key for key, _ in definitions]
require(len(keys) == len(set(keys)), "Duplicate acro key")
require(len(keys) >= 49, "Preserve the shared acronym/model registry")
n_abbr = 0
n_systems = 0
for key, options in definitions:
    if re.search(r"\btag\s*=\s*\{abbreviations\}", options):
        n_abbr += 1
    elif re.search(r"\btag\s*=\s*\{systems\}", options):
        n_systems += 1
        require(bool(re.search(r"first-style\s*=\s*short", options)),
                f"Named system {key} must display its name without invented expansion")
    else:
        errors.append(f"acro entry missing recognized tag: {key}")
    require("short" in options and "long" in options,
            f"acro entry missing short/long metadata: {key}")
require(n_abbr >= 12 and n_systems >= 25,
        "Maintain separate general-abbreviation and named-system groups")
acro_sources = sorted((PAPER / "sections").glob("*.tex"))
acro_sources += sorted((PAPER / "tabs" / "tex").glob("*.tex"))
acro_sources += sorted((PAPER / "figs" / "tex").glob("*_figure.tex"))
for source_file in acro_sources:
    data = source_file.read_text(encoding="utf-8")
    for ref in re.findall(r"\\ac(?:p|f|s|l)?\{([^}]+)\}", data):
        require(ref in keys, f"{source_file.relative_to(PAPER)}: undefined acro key {ref}")
    require(not re.search(r"\\gls(?:pl|first|firstplural)?\{", data),
            f"{source_file.relative_to(PAPER)}: migrate glossaries commands to acro")


# Research-map provenance: each visible milestone must resolve to exactly one
# bibliography key and use its cited reference year. This is not a primary-paper
# full-text audit and does not assert a complete literature census.
map_registry = PAPER / "figs" / "tex" / "research_map_sources.csv"
require(map_registry.is_file(), "Missing research-map bibliography crosswalk")
if map_registry.is_file():
    with map_registry.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        require(reader.fieldnames == ["track", "label", "bibtex_key", "reference_year"],
                "Research-map registry has unexpected CSV columns")
        entries = list(reader)
    require(len(entries) >= 67, "Preserve at least 67 documented research milestones")
    map_tex = tex("figs/tex/research_map.tex")
    displayed = re.findall(
        r"\\fill\[track([A-F])\] \([^)]+\) circle \(\.034cm\);\s*"
        r"\\node\[anchor=west,[^\n]+\] at \([^)]+\) \{([^{}]+) '(\d{2})\};",
        map_tex,
    )
    displayed_items = {(track, label, 2000 + int(yy)) for track, label, yy in displayed}
    registered_items = set()
    seen_names = set()
    bib = (PAPER / "references.bib").read_text(encoding="utf-8")
    bib_years = {}
    for match in re.finditer(r"@\w+\{([^,]+),([\s\S]*?)(?=\n@\w+\{|$)", bib):
        year = re.search(r"^\s*year\s*=\s*\{(\d{4})\}", match.group(2), re.M)
        if year:
            bib_years[match.group(1)] = int(year.group(1))
    for entry in entries:
        track, label, key = entry["track"], entry["label"], entry["bibtex_key"]
        require(track in "ABCDEF", f"Unknown research-map track {track}: {label}")
        require(label not in seen_names, f"Duplicate research-map label: {label}")
        seen_names.add(label)
        try:
            year = int(entry["reference_year"])
        except (TypeError, ValueError):
            errors.append(f"Invalid research-map reference year: {label}")
            continue
        registered_items.add((track, label, year))
        require(key in bib_years, f"Research-map reference not found in BibTeX: {label} -> {key}")
        require(bib_years.get(key) == year,
                f"Research-map year mismatch: {label} ({year}) vs {key} ({bib_years.get(key)})")
    require(len(displayed) == len(displayed_items), "Research map has duplicate visible milestones")
    require(len(displayed_items) == len(entries), "Research-map figure/registry entry counts differ")
    require(displayed_items == registered_items,
            f"Research-map figure/registry mismatch: figure-only={sorted(displayed_items-registered_items)}, "
            f"registry-only={sorted(registered_items-displayed_items)}")

require("CVPR-style" not in (PAPER / "README.md").read_text(encoding="utf-8"),
        "Use plain survey naming rather than a template-style label")

print("Reviewed guidance: paper/WRITING_CHECKLIST.md (read before drafting and each commit)")
print(f"Checked anonymous mode, 3 editable figures, 5 tables, acro, ordered sections and natbib citations, manuscript inputs, labels and introductory evidence ({len(labels)} labels)")
if errors:
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    raise SystemExit(1)
print("Manuscript structure and review gates passed")
