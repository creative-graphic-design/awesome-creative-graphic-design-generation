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
for stem in ("overview", "edit_protocol", "research_map", "research_map_narrative"):
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
n_evaluation = 0
acro_bib_source = (PAPER / "references.bib").read_text(encoding="utf-8")
acro_bib_keys = set(re.findall(r"(?m)^@\w+\{([^,]+),", acro_bib_source))
for key, options in definitions:
    tags = re.search(r"\btag\s*=\s*\{([^}]+)\}", options)
    tag = tags.group(1) if tags else ""
    if tag == "abbreviations":
        n_abbr += 1
    elif tag in ("systems", "evaluation"):
        if tag == "systems":
            n_systems += 1
        else:
            n_evaluation += 1
        require(bool(re.search(r"first-style\s*=\s*short", options)),
                f"Named resource {key} must display its name without invented expansion")
        citation = re.search(r"(?m)^\s*cite\s*=\s*\{([^}]+)\}", options)
        require(citation is not None, f"Named resource {key} is missing an original-source cite key")
        if citation:
            for bib_key in citation.group(1).split(","):
                require(bib_key.strip() in acro_bib_keys,
                        f"Named resource {key} cites missing BibTeX entry {bib_key}")
    else:
        errors.append(f"acro entry missing recognized tag: {key}")
    require("short" in options and "long" in options,
            f"acro entry missing short/long metadata: {key}")
require(n_abbr >= 22 and n_systems >= 120 and n_evaluation >= 15,
        "Preserve expanded abbreviation, named-system, and benchmark/dataset groups")
require(r"\printacronyms[include=evaluation,heading=none,display=all]" in main,
        "Print benchmark/dataset resources in their own acro list")
require(r"pages/display = all" in main,
        "Use the stock acro option to list every page an acronym appears on")
require(r"pages/name = true" in main,
        "Label first and subsequent occurrence pages as p. / pp.")
require(r"pages/seq/use = false" in main,
        "Show explicit occurrence page numbers instead of f./ff. shorthand")
require(r"\section*{Evaluation Resources}" in main,
        "Use a single-line heading for the compact two-column evaluation index")
require(r"\section*{Benchmarks, Datasets, and Evaluation Resources}" not in main,
        "Avoid the hyphenated multi-line evaluation index heading")

# Use the stock acro list formatter; the custom registry metadata remains stored
# but is not a reason to replace acro's built-in typesetting with our own.
require(r"\NewAcroTemplate" not in main and "template=survey-rich" not in main,
        "Use acro's built-in default print template, not survey-rich")
require(r"\input{acro_list_template}" not in main,
        "Do not load the obsolete custom list template")
for property_name in ("source", "refyear", "venue", "paperurl", "doi",
                      "task", "representation"):
    require(r"\DeclareAcroProperty{" + property_name + "}" in acro_source,
            f"Preserve registered source metadata field: {property_name}")

acro_bib_records: dict[str, dict[str, str]] = {}
acro_bib_starts = list(re.finditer(r"(?m)^@\w+\{([^,]+),\s*$", acro_bib_source))
for i, item in enumerate(acro_bib_starts):
    end = acro_bib_starts[i + 1].start() if i + 1 < len(acro_bib_starts) else len(acro_bib_source)
    chunk = acro_bib_source[item.end():end]
    fields: dict[str, str] = {}
    for field in ("year", "booktitle", "journal", "url", "doi"):
        found = re.search(rf"(?m)^\s*{field}\s*=\s*\{{(.*)\}},?\s*$", chunk)
        fields[field] = found.group(1) if found else ""
    acro_bib_records[item.group(1)] = fields

acro_list_sources = 0
for name, properties in definitions:
    item_tag = re.search(r"(?m)^\s*tag\s*=\s*\{([^}]+)\}", properties)
    if not item_tag or item_tag.group(1) == "abbreviations":
        continue
    original = re.search(r"(?m)^\s*cite\s*=\s*\{([^}]+)\}", properties)
    index_citation = re.search(r"(?m)^\s*source\s*=\s*\{\\citep\{([^}]+)\}\}", properties)
    year = re.search(r"(?m)^\s*refyear\s*=\s*\{(\d{4})\}", properties)
    url = re.search(r"(?m)^\s*paperurl\s*=\s*\{([^}]+)\}", properties)
    venue = re.search(r"(?m)^\s*venue\s*=\s*\{([^}]+)\}", properties)
    doi = re.search(r"(?m)^\s*doi\s*=\s*\{([^}]+)\}", properties)
    require(index_citation is not None, f"Missing list-source citation: {name}")
    require(year is not None, f"Missing list-reference year: {name}")
    require(url is not None, f"Missing paper hyperlink: {name}")
    if original is None:
        continue
    bib_key = original.group(1)
    bib_metadata = acro_bib_records.get(bib_key, {})
    require(index_citation is not None and index_citation.group(1) == bib_key,
            f"List citation and first-use source differ: {name}")
    require(year is not None and year.group(1) == bib_metadata.get("year"),
            f"Reference year differs from BibTeX: {name}")
    require(url is not None and url.group(1) == bib_metadata.get("url"),
            f"Paper link differs from BibTeX: {name}")
    venue_text = venue.group(1) if venue else ""
    require(venue_text == (bib_metadata.get("booktitle") or bib_metadata.get("journal")),
            f"Venue differs from BibTeX: {name}")
    doi_text = doi.group(1) if doi else ""
    require(doi_text == bib_metadata.get("doi"), f"DOI differs from BibTeX: {name}")
    # Stock acro prints its 'extra' property in the built-in list.
    # Every named source must carry a textual author citation and a native
    # clickable paper link. Validate both against the canonical registry/BibTeX.
    extra = re.search(r"(?m)^\s*extra\s*=\s*\{(.*)\},?\s*$", properties)
    require(extra is not None, f"Missing native acro citation/paper link: {name}")
    if extra and url:
        expected = rf"\citet{{{bib_key}}}; \href{{{url.group(1)}}}{{\mbox{{paper}}}}"
        require(extra.group(1) == expected,
                f"Extra list citation or paper link differs from the original source: {name}")

    acro_list_sources += 1
require(acro_list_sources == n_systems + n_evaluation,
        "Full list must cite every named model, system and evaluation resource")

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

# The compact, illustrated research map has its own curated bibliography crosswalk.
# This is a representative narrative selection, not a systematic study-flow count.
narrative_path = PAPER / "figs" / "tex" / "research_map_narrative_sources.csv"
require(narrative_path.is_file(), "Missing narrative research-map source crosswalk")
if narrative_path.is_file():
    with narrative_path.open(encoding="utf-8", newline="") as handle:
        narrative_reader = csv.DictReader(handle)
        require(narrative_reader.fieldnames == [
            "track", "label", "bibtex_key", "reference_year", "method_family"],
            "Narrative research-map registry has unexpected columns")
        narrative_entries = list(narrative_reader)
    narrative = tex("figs/tex/research_map_narrative.tex")
    macro = re.compile(
        r"\\MapPaper(?:Brand)?\{([A-D])\}\{([^{}]+)\}\{(\d{2})\}"
        r"\{([^{}]+)\}\{[^{}]+\}\{[^{}]+\}\{([^{}]+)\}\{([^{}]+)\}"
    )
    visible = {(track, title, key, 2000 + int(year), family)
               for track, title, year, key, family, _ in macro.findall(narrative)}
    source_items = set()
    for rec in narrative_entries:
        try:
            year = int(rec["reference_year"])
        except (TypeError, ValueError):
            errors.append(f"Narrative research-map has an invalid year: {rec['label']}")
            continue
        key = rec["bibtex_key"]
        source_items.add((rec["track"], rec["label"], key, year, rec["method_family"]))
        require(key in bib_years, f"Narrative research-map unknown BibTeX key: {key}")
        require(bib_years.get(key) == year,
                f"Narrative research-map bibliography year mismatch: {rec['label']}")
    require(len(narrative_entries) == 26, "Preserve the 26 audited narrative milestones")
    require(len(visible) == len(narrative_entries), "Narrative research-map visible count mismatch")
    require(visible == source_items,
            f"Narrative research-map source/figure mismatch: figure-only={visible-source_items}, "
            f"registry-only={source_items-visible}")

# T16: logos identify *their own* study nodes. A detached affiliation
# footer, a horizontal wordmark forced into a square, or an unreviewed
# institution must fail this audit. The CSV lists all 26 research nodes,
# including those still text-only because an original square mark is missing.
affiliations_path = PAPER / "figs" / "tex" / "research_map_affiliations.csv"
logo_registry_path = PAPER / "figs" / "tex" / "logo_asset_candidates.csv"
require(affiliations_path.is_file(), "Missing complete 26-paper affiliation register")
require(logo_registry_path.is_file(), "Missing institution-logo rights register")
if affiliations_path.is_file() and logo_registry_path.is_file():
    with affiliations_path.open(encoding="utf-8", newline="") as handle:
        affiliation_records = list(csv.DictReader(handle))
    with logo_registry_path.open(encoding="utf-8", newline="") as handle:
        logo_rows = {row["institution"]: row for row in csv.DictReader(handle)}
    with narrative_path.open(encoding="utf-8", newline="") as handle:
        narrative_records = list(csv.DictReader(handle))
    require(len(affiliation_records) == 26, "Every one of 26 study nodes needs an affiliation audit")
    audit_keys = {(r["track"], r["label"], r["bibtex_key"], r["reference_year"])
                  for r in affiliation_records}
    map_keys = {(r["track"], r["label"], r["bibtex_key"], r["reference_year"])
                for r in narrative_records}
    require(len(audit_keys) == 26 and audit_keys == map_keys,
            "Affiliation audit has missing/extra or duplicated research-map nodes")
    # Primary affiliation names and a corporate group mark are not always
    # spelled exactly alike in source papers: keep every alias explicit.
    institution_aliases = {
        "Google Research": "Google",
        "The University of Tokyo": "University of Tokyo",
        "Microsoft": "Microsoft Research Asia",
        "Microsoft Research": "Microsoft Research Asia",
        "Adobe Research": "Adobe Inc.",
        "University of California Berkeley": "University of California, Berkeley",
    }
    for row in affiliation_records:
        require(bool(row["selected_institution"]) and bool(row["evidence_url"]) and
                bool(row["selection_role"]) and bool(row["verification_level"]),
                f"Study lacks attribution source and selection rationale: {row['label']}")
        canonical = institution_aliases.get(row["selected_institution"], row["selected_institution"])
        require(canonical in logo_rows,
                f"Missing compact-logo source/rights candidate for study {row['label']}: {canonical}")
    require(len(logo_rows) >= 18, "Complete T16 source register should cover 18 distinct main institutions")
    # Audit states select an *unchanged compact original* for each verified
    # candidate, not a dynamically generated imitation of another institution.
    status_to_stem = {
        "verified_square_ca": "cyberagent-symbol",
        "verified_square_pku": "pku",
        "verified_square_ms": "microsoft",
        "verified_square_google": "google",
        "verified_square_bit": "bit-symbol",
        "verified_square_salesforce": "salesforce",
        "verified_square_meituan": "meituan-symbol",
        "verified_square_utokyo": "utokyo",
        "verified_square_berkeley": "berkeley",
        "verified_square_ucsd": "ucsd",
        "verified_square_adobe": "adobe",
        "verified_identity_epfl": "epfl",
        "verified_identity_alibaba": "alibaba",
    }
    figure_source = tex("figs/tex/research_map_narrative.tex")
    brand_uses = re.findall(
        r"\\MapPaperBrand\{([A-D])\}\{([^{}]+)\}\{(\d{2})\}\{([a-z0-9]+)\}\{[^{}]+\}\{[^{}]+\}\{[a-z]+\}\{[^{}]+\}\{([a-z-]+)\}",
        figure_source,
    )
    dual_brand_uses = re.findall(
        r"\\MapPaperBrandPair\{([A-D])\}\{([^{}]+)\}\{(\d{2})\}\{([a-z0-9]+)\}\{[^{}]+\}\{[^{}]+\}\{[a-z]+\}\{[^{}]+\}\{\\MapLogoPair\{([a-z-]+)\}\{([a-z-]+)\}\}",
        figure_source,
    )
    require(dual_brand_uses == [("A", "LayoutFlow", "24", "layoutflow2024", "utokyo", "cyberagent-symbol")],
            "LayoutFlow must show both verified University of Tokyo and CyberAgent icons")
    require(r"\newcommand{\MapLogoPair}[2]" in figure_source and
            r"width=.44\MapCardLogoWidth,height=.66\MapCardContentHeight,keepaspectratio" in figure_source,
            "Multiple affiliation symbols must be proportionally bounded within the logo column")
    seen = {(lane, label, "20"+year, key): stem
            for lane, label, year, key, stem in brand_uses}
    seen.update({(lane, label, "20"+year, key): primary for lane, label, year, key, primary, secondary in dual_brand_uses})
    require(len(seen) == len(brand_uses) + len(dual_brand_uses), "Duplicate identity logos for a study")
    expected = {}
    for rec in affiliation_records:
        stem = status_to_stem.get(rec["logo_review_state"])
        if stem is not None:
            expected[(rec["track"], rec["label"], rec["reference_year"], rec["bibtex_key"])] = stem
        else:
            require(rec["logo_review_state"] in {
                "pending_original_square_mark", "blocked_permission_review"},
                f"Unregistered logo decision: {rec['label']}")
    require(seen == expected, f"Research nodes' compact logo mapping mismatch: {seen} != {expected}")
    require("Affiliation provenance:" not in figure_source and "\\AffilBrand" not in figure_source,
            "Institution logos must not be placed in a separate affiliation footer")
    require(r"\newcommand{\MapPaperFrame}[4]" in figure_source and
            r"\newcommand{\MapPaperContent}[4]" in figure_source and
            r"\setlength{\MapCardHeight}{.20\MapCardWidth}" in figure_source and
            r"\setlength{\MapCardLogoWidth}{.25\MapCardContentWidth}" in figure_source and
            r"\setlength{\MapCardTextWidth}{.75\MapCardContentWidth}" in figure_source and
            r"\setlength{\MapCardTextStackHeight}{.84\MapCardContentHeight}" in figure_source and
            r"\setlength{\MapCardRowHeight}{.5\MapCardTextStackHeight}" in figure_source and
            r"\MapCardTitleOffset}{\dimexpr.5\MapCardHeight-.5\MapCardRowHeight\relax}" in figure_source and
            r"\MapCardDetailOffset}{\dimexpr.5\MapCardHeight+.5\MapCardRowHeight\relax}" in figure_source and
            r"minimum width=\MapCardWidth,minimum height=\MapCardHeight" in figure_source and
            r"\setlength{\MapCardPaddingX}{.025\MapCardWidth}" in figure_source and
            r"\setlength{\MapCardPaddingY}{.016\MapCardWidth}" in figure_source and
            r"\setlength{\MapCardMarginX}{.172619\MapCardWidth}" in figure_source and
            r"\MapCardLogoCenterX,-.5\MapCardHeight" in figure_source and
            r"\MapCardTextOffset,-\MapCardTitleOffset" in figure_source and
            r"\MapCardTextOffset,-\MapCardDetailOffset" in figure_source and
            r"\includegraphics[width=.72\MapCardLogoWidth,height=.77\MapCardContentHeight,keepaspectratio]" in figure_source,
            "Every study card must use independent anchored contents within fixed proportional frames")
    require(figure_source.count(r"\MapPaperFrame{#5}{#6}{#7}{") == 3 and
            figure_source.count(r"\MapPaperContent{#2}{#3}{#8}{") == 2,
            "Branded and unbranded study cards must share the proportional layout component")
    require(r"\hspace*{.53cm}" not in figure_source and
            r"m{.46cm}" not in figure_source and
            r"\begin{tabular}" not in figure_source,
            "Fixed-width typography columns and table baseline layout are forbidden")
    prep = tex("scripts/prepare_affiliation_logos.sh")
    require("cyberagent-symbol.tex" in prep and "pdflatex" in prep,
            "CA icon must use unchanged original logo in a square vector tile")
    require("prepare_affiliation_logos.sh" in tex("scripts/build_figures.sh"),
            "Figure build must verify the exact original logo SHA pins")
    source_icon = tex("figs/assets/logos/cyberagent-symbol.tex")
    require("trim=0bp 0bp 201bp 0bp,clip" in source_icon and
            "minipage}[c][57bp][c]{57bp}" in source_icon,
            "CA square symbol crop must preserve original paths and dimensions")
    to_registry = {
        "cyberagent-symbol": ("CyberAgent", "cyberagent", "6e364a261c7cfc57a6f434fee0aeff3fb1184a88"),
        "pku": ("Peking University", "pku", "14ffd592f63fb7231f71639e37b586467be667ea"),
        "google": ("Google", "google", "2cc789a02534557380d92124e2f8b9483d198fb3"),
        "microsoft": ("Microsoft Research Asia", "microsoft", "5b170117926ae5a5e451aa24676b5a124c2fa122"),
        "bit-symbol": ("Beijing Institute of Technology", "bit-original", "6fcb6505b213d2f858e82ff51aab605a1771dc7c"),
        "salesforce": ("Salesforce Research", "salesforce", "a05d80d66796327adad13e0574c4fa78b526545c"),
        "meituan-symbol": ("Meituan", "meituan-original", "0df68fc2b3b25ddbeaa7f4046c0f74b3aae2fb05"),
        "utokyo": ("University of Tokyo", "utokyo", "3d2c55ba43c606c9c7563677aca709b49a797d9e"),
        "berkeley": ("University of California, Berkeley", "berkeley", "dfb5fb42fc8533a6a6b0d07cf350770a3cb88d6a"),
        "ucsd": ("University of California San Diego", "ucsd", "c4d91d3aa318092f553439fa8e3820f62efb996e"),
        "adobe": ("Adobe Inc.", "adobe", "471dcc4a658857f96ea2b85f40dadfa15a455319"),
        "epfl": ("EPFL", "epfl", "5aae170a1e6c06178309e87d19cca7e2770dd9ec"),
        "alibaba": ("Alibaba Group", "alibaba", "42e5896c316a2394d5744812174641cb5710cbcd"),
    }
    for stem in set(expected.values()):
        institution, source_stem, digest = to_registry[stem]
        record = logo_rows.get(institution)
        require(record is not None, f"Missing original-logo register for {institution}")
        if record is None:
            continue
        require(record["status"] == "draft_nominative_review",
                f"Enabled logo has no explicit draft rights review: {institution}")
        require(bool(record["logo_source_page"]) and bool(record["rights_classification"]),
                f"Original mark source or rights description missing: {institution}")
        require(record["render_asset"] == stem + ".pdf",
                f"Wrong square logo asset linked for {institution}")
        require(record["asset_sha1"] == digest,
                f"Source digest does not match original logo register: {institution}")
        if stem == "bit-symbol":
            require(f"bit_sha={digest}" in prep and "bit-original.ai" in prep and
                    "bit-symbol.tex" in prep and "bit-original.pdf" in prep,
                    "BIT source must be the exact original PDF-compatible Illustrator master")
            bit_icon = tex("figs/assets/logos/bit-symbol.tex")
            require("trim=360bp 145bp 175bp 145bp,clip" in bit_icon and
                    "minipage}[c][307bp][c]{307bp}" in bit_icon,
                    "BIT square mark viewport must preserve original vector paths")
        elif stem == "meituan-symbol":
            require("meituan_zip_sha=6817f88d95f95bb6e6b8238aa0c0e7d36dd93008" in prep and
                    f"meituan_ai_sha={digest}" in prep and
                    "meituan-symbol.tex" in prep and
                    "meituan-original.pdf" in prep and
                    "unzip -p" in prep,
                    "Meituan icon must be extracted from original official media AI with pinned ZIP and master hashes")
            meituan_icon = tex("figs/assets/logos/meituan-symbol.tex")
            require("clip" in meituan_icon and "meituan-original.pdf" in meituan_icon,
                    "Meituan square mark must crop the original vector, not redraw it")
        elif stem == "salesforce":
            require("sf_sha=b8cca7fa6290153156dc0d260095079d0cb0708c" in prep and
                    f"expected = '{digest}'" in prep and
                    "Salesforce-Corporate-Logo-Cloud-RBG.svg" in prep and
                    "cls-3" in prep and "quoteattr" in prep and
                    "salesforce-symbol.svg" in prep,
                    "Salesforce compact mark must isolate original blue cloud path from pinned official brand ZIP")
        else:
            require(f"prepare_svg {source_stem} {digest}" in prep,
                    f"Enabled logo must have a pinned SVG source: {institution}")
        names = {r["label"] for r in affiliation_records
                 if status_to_stem.get(r["logo_review_state"]) == stem}
        require(names == set(record["placed_on_node"].split("|")),
                f"Rights register paper-to-logo mapping differs for {institution}")
    require(len(seen) == 21, "Exactly twenty-one sourced draft institutional marks currently expected")

require("CVPR-style" not in (PAPER / "README.md").read_text(encoding="utf-8"),
        "Use plain survey naming rather than a template-style label")

print("Reviewed guidance: paper/WRITING_CHECKLIST.md (read before drafting and each commit)")
print(f"Checked anonymous mode, 4 editable figures, 5 tables, {len(keys)} acro entries (abbr={n_abbr}, systems={n_systems}, evaluation={n_evaluation}), ordered sections and citation provenance ({len(labels)} labels)")
if errors:
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    raise SystemExit(1)
print("Manuscript structure and review gates passed")
