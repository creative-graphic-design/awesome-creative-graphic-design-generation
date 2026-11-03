#!/usr/bin/env python3
"""Mechanical, CI-enforced checks derived from the author feedback checklist.

Scientific correctness and whether a human actually read the checklist cannot
be proven by this linter; the local commit checklist still must be reviewed.
"""
from __future__ import annotations

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
require(not any(re.search(r"\b[A-Z][A-Za-z-]* et al\.~\\citep\{", path.read_text(encoding="utf-8"))
                for path in (PAPER / "sections").glob("*.tex")),
        "Use \\citet{key} for textual author citations; do not write Author et al.~\\citep{key}")

require("CVPR-style" not in (PAPER / "README.md").read_text(encoding="utf-8"),
        "Use plain survey naming rather than a template-style label")

print("Reviewed guidance: paper/WRITING_CHECKLIST.md (read before drafting and each commit)")
print(f"Checked anonymous mode, 3 editable figures, 5 tables, ordered sections and natbib citations, manuscript inputs, labels and introductory evidence ({len(labels)} labels)")
if errors:
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    raise SystemExit(1)
print("Manuscript structure and review gates passed")
