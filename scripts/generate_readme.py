#!/usr/bin/env python3
"""Generate README.md from data/resources.csv."""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from datetime import date
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "resources.csv"
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
    "Content-Aware Graphic Design",
    "Typography and Text Rendering",
    "Language and Multimodal Design Agents",
    "End-to-End Graphic Design Generation",
]

HEADER = """# Awesome Creative Graphic Design Generation [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<!-- This file is generated from data/resources.csv by scripts/generate_readme.py. Do not edit it directly. -->

Curated resources for generating, editing, representing, and evaluating composed graphic-design artifacts such as posters, advertisements, social-media graphics, magazine layouts, banners, and related visual compositions.

This list focuses on work where layout, typography, visual elements, editable structure, or design-specific evaluation is a first-class part of the problem. Generic text-to-image generation and generic image editing are out of scope unless they make a direct contribution to graphic-design generation.

Research resources are ordered by **first public appearance** within each category, from oldest to newest. The sort key is the earlier of the arXiv v1 date and the venue/presentation date when both are known; journal-only work uses its first public publication date.

## Contents

- [Surveys and Overviews](#surveys-and-overviews)
- [Papers](#papers)
  - [Layout Generation](#layout-generation)
  - [Content-Aware Graphic Design](#content-aware-graphic-design)
  - [Typography and Text Rendering](#typography-and-text-rendering)
  - [Language and Multimodal Design Agents](#language-and-multimodal-design-agents)
  - [End-to-End Graphic Design Generation](#end-to-end-graphic-design-generation)
- [Datasets](#datasets)
- [Benchmarks and Evaluation](#benchmarks-and-evaluation)
- [Models and Implementations](#models-and-implementations)
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
    for year in sorted(dated):
        lines.extend([f"{marker} {year}", ""])
        for sort_date, row in sorted(
            dated[year], key=lambda pair: (pair[0], pair[1]["name"].casefold())
        ):
            lines.append(entry_line(row))
        lines.append("")

    if undated:
        lines.extend([f"{marker} Other", ""])
        for row in sorted(undated, key=lambda item: item["name"].casefold()):
            lines.append(entry_line(row))
        lines.append("")

    return lines


def generate() -> str:
    rows = load_rows()
    by_section: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        by_section[row["section"]].append(row)

    lines = [HEADER.rstrip(), ""]

    lines.extend(["## Surveys and Overviews", ""])
    lines.extend(render_dated(by_section["Surveys and Overviews"], 3))

    lines.extend(["## Papers", ""])
    paper_rows = by_section["Papers"]
    for category in PAPER_CATEGORY_ORDER:
        lines.extend([f"### {category}", ""])
        category_rows = [row for row in paper_rows if row["category"] == category]
        lines.extend(render_dated(category_rows, 4))

    for section in ("Datasets", "Benchmarks and Evaluation"):
        lines.extend([f"## {section}", ""])
        lines.extend(render_dated(by_section[section], 3))

    for section in ("Models and Implementations", "Related Resources"):
        lines.extend([f"## {section}", ""])
        for row in sorted(by_section[section], key=lambda item: item["name"].casefold()):
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
