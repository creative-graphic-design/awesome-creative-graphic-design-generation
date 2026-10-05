#!/usr/bin/env python3
"""Generate README.md from structured CSV data."""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from datetime import date
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "resources.csv"
VENUES_PATH = ROOT / "data" / "venues.csv"
README_PATH = ROOT / "README.md"

SECTION_ORDER = [
    "Surveys and Overviews",
    "Papers",
    "Datasets",
    "Benchmarks and Evaluation",
    "Models and Implementations",
    "Related Resources",
]

PAPER_CATEGORY_ORDER = [
    "Layout Generation",
    "Content-Aware Layout Generation",
    "Graphic Design Generation",
    "Typography and Text Rendering",
    "Graphic Design Editing and Reconstruction",
    "Scientific Poster and Slide Generation",
]

VENUE_TYPE_ORDER = ["Conference", "Journal"]

HEADER = """# Awesome Creative Graphic Design Generation [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<!-- This file is generated from data/resources.csv and data/venues.csv by scripts/generate_readme.py. Do not edit it directly. -->

Curated resources for generating, editing, representing, and evaluating composed graphic-design artifacts such as posters, advertisements, social-media graphics, magazine layouts, scientific posters, slides, banners, and related visual compositions.

This list focuses on work where layout, typography, visual elements, editable structure, or design-specific evaluation is a first-class part of the problem. Generic text-to-image generation and generic image editing are out of scope unless they make a direct contribution to graphic-design generation.

Research resources are ordered by **first public appearance** within each category, from newest to oldest. The sort key is the earlier of the arXiv v1 date and the venue/presentation date when both are known; journal-only work uses its first public publication date.

## Contents

- [Surveys and Overviews](#surveys-and-overviews)
- [Papers](#papers)
  - [Layout Generation](#layout-generation)
  - [Content-Aware Layout Generation](#content-aware-layout-generation)
  - [Graphic Design Generation](#graphic-design-generation)
  - [Typography and Text Rendering](#typography-and-text-rendering)
  - [Graphic Design Editing and Reconstruction](#graphic-design-editing-and-reconstruction)
  - [Scientific Poster and Slide Generation](#scientific-poster-and-slide-generation)
- [Datasets](#datasets)
- [Benchmarks and Evaluation](#benchmarks-and-evaluation)
- [Models and Implementations](#models-and-implementations)
- [Relevant Venues and Journals](#relevant-venues-and-journals)
  - [Conferences](#conferences)
  - [Journals](#journals)
- [Related Resources](#related-resources)
"""

FOOTER = """## Contributing

Contributions are welcome. Please read the [contribution guidelines](CONTRIBUTING.md) before opening a pull request.
"""


def parse_date(value: str) -> date | None:
    value = value.strip()
    return date.fromisoformat(value) if value else None


def first_public_date(row: dict[str, str]) -> date | None:
    candidates = [parse_date(row["arxiv_date"]), parse_date(row["venue_date"])]
    candidates = [candidate for candidate in candidates if candidate is not None]
    return min(candidates) if candidates else None


def load_rows() -> list[dict[str, str]]:
    with DATA_PATH.open(newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    seen_names: set[tuple[str, str, str]] = set()
    seen_urls: set[str] = set()

    for row in rows:
        section = row["section"]
        category = row["category"]
        name = row["name"]
        url = row["url"]

        if section not in SECTION_ORDER:
            raise ValueError(f"Unknown section for {name}: {section}")
        if section == "Papers" and category not in PAPER_CATEGORY_ORDER:
            raise ValueError(f"Unknown paper category for {name}: {category}")
        if section != "Papers" and category:
            raise ValueError(f"Only Papers entries may set category: {name}")
        if not name or not url or not row["description"]:
            raise ValueError(f"Missing required field: {row}")
        if not url.startswith("https://"):
            raise ValueError(f"URL must use HTTPS: {name}: {url}")

        for field in ("arxiv_date", "venue_date"):
            if row[field]:
                parse_date(row[field])

        key = (section, category, name)
        if key in seen_names:
            raise ValueError(f"Duplicate entry: {key}")
        seen_names.add(key)

        if url in seen_urls:
            raise ValueError(f"Duplicate canonical URL: {url}")
        seen_urls.add(url)

    return rows


def load_venues() -> list[dict[str, str]]:
    with VENUES_PATH.open(newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    seen_names: set[str] = set()
    for row in rows:
        if row["type"] not in VENUE_TYPE_ORDER:
            raise ValueError(f"Unknown venue type: {row['type']}")
        if not row["name"] or not row["url"] or not row["note"]:
            raise ValueError(f"Missing venue field: {row}")
        if not row["url"].startswith("https://"):
            raise ValueError(f"Venue URL must use HTTPS: {row['name']}")
        if row["name"] in seen_names:
            raise ValueError(f"Duplicate venue: {row['name']}")
        seen_names.add(row["name"])
    return rows


def entry_line(row: dict[str, str]) -> str:
    return f'- [{row["name"]}]({row["url"]}) - {row["description"]}'


def render_dated(rows: list[dict[str, str]], year_heading_level: int) -> list[str]:
    dated: dict[int, list[tuple[date, dict[str, str]]]] = defaultdict(list)
    undated: list[dict[str, str]] = []

    for row in rows:
        sort_date = first_public_date(row)
        if sort_date is None:
            undated.append(row)
        else:
            dated[sort_date.year].append((sort_date, row))

    lines: list[str] = []
    marker = "#" * year_heading_level
    for year in sorted(dated, reverse=True):
        lines.extend([f"{marker} {year}", ""])
        # Publication date is primary. Name is only a deterministic tie-breaker
        # when two resources have exactly the same first-public date.
        for sort_date, row in sorted(
            dated[year],
            key=lambda pair: (-pair[0].toordinal(), pair[1]["name"].casefold()),
        ):
            lines.append(entry_line(row))
        lines.append("")

    if undated:
        lines.extend([f"{marker} Other", ""])
        for row in sorted(undated, key=lambda item: item["name"].casefold()):
            lines.append(entry_line(row))
        lines.append("")

    return lines


def render_venues(venues: list[dict[str, str]]) -> list[str]:
    lines: list[str] = []
    heading = {"Conference": "Conferences", "Journal": "Journals"}
    for venue_type in VENUE_TYPE_ORDER:
        lines.extend([f"### {heading[venue_type]}", ""])
        for row in sorted(
            (row for row in venues if row["type"] == venue_type),
            key=lambda item: item["name"].casefold(),
        ):
            lines.append(f'- [{row["name"]}]({row["url"]}) - {row["note"]}')
        lines.append("")
    return lines


def generate() -> str:
    rows = load_rows()
    venues = load_venues()
    by_section: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        by_section[row["section"]].append(row)

    lines = [HEADER.rstrip(), ""]

    lines.extend(["## Surveys and Overviews", ""])
    lines.extend(render_dated(by_section["Surveys and Overviews"], 3))

    lines.extend(["## Papers", ""])
    lines.extend([
        "Papers are classified by their **primary output and task**, rather than by model family. LLM-, VLM-, diffusion-, and agent-based approaches can therefore appear in any category.",
        "",
        "- **Layout Generation** outputs structured element geometry or arrangement without relying on the visual content of a target canvas.",
        "- **Content-Aware Layout Generation** still outputs layout or placement, but conditions that geometry on a background image, product/brand assets, saliency, element content, or another visual canvas.",
        "- **Graphic Design Generation** goes beyond geometry to create a composed design artifact, such as backgrounds, imagery, typography, styles, layers, or editable HTML/CSS/PSD/PPTX structures.",
        "- **Typography and Text Rendering** focuses primarily on legible, faithful, or stylized text generation and placement within designed imagery.",
        "- **Graphic Design Editing and Reconstruction** focuses on iterative editing, layer recovery, or conversion of rendered designs back into editable structures.",
        "- **Scientific Poster and Slide Generation** covers research communication workflows that combine source-document understanding, content selection, layout, typography, rendering, and often editable output.",
        "",
    ])
    paper_rows = by_section["Papers"]
    for category in PAPER_CATEGORY_ORDER:
        lines.extend([f"### {category}", ""])
        category_rows = [row for row in paper_rows if row["category"] == category]
        lines.extend(render_dated(category_rows, 4))

    for section in ("Datasets", "Benchmarks and Evaluation"):
        lines.extend([f"## {section}", ""])
        lines.extend(render_dated(by_section[section], 3))

    lines.extend(["## Models and Implementations", ""])
    for row in sorted(
        by_section["Models and Implementations"],
        key=lambda item: item["name"].casefold(),
    ):
        lines.append(entry_line(row))
    lines.append("")

    lines.extend(["## Relevant Venues and Journals", ""])
    lines.append("Recurring publication venues worth monitoring for work in this area.")
    lines.append("")
    lines.extend(render_venues(venues))

    lines.extend(["## Related Resources", ""])
    for row in sorted(
        by_section["Related Resources"], key=lambda item: item["name"].casefold()
    ):
        lines.append(entry_line(row))
    lines.append("")

    lines.append(FOOTER.rstrip())
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check", action="store_true", help="Fail if README.md is not up to date."
    )
    args = parser.parse_args()

    generated = generate()
    if args.check:
        current = README_PATH.read_text(encoding="utf-8")
        if current != generated:
            print(
                "README.md is out of date. Run: python3 scripts/generate_readme.py",
                file=sys.stderr,
            )
            return 1
        return 0

    README_PATH.write_text(generated, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
