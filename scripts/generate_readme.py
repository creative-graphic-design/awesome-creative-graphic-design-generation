#!/usr/bin/env python3
"""Generate README.md from structured CSV data and a Jinja template."""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path
from typing import Any

from jinja2 import Environment, FileSystemLoader, StrictUndefined

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
RESOURCE_PATHS = sorted(DATA_DIR.glob("resources*.csv"))
METADATA_PATHS = sorted(DATA_DIR.glob("paper_metadata*.csv"))
VENUES_PATH = DATA_DIR / "venues.csv"
TEMPLATE_DIR = ROOT / "templates"
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
    "Composable and Layered Asset Generation",
    "Typography and Text Rendering",
    "Graphic Design Editing and Reconstruction",
    "Scientific Poster and Slide Generation",
]

DATED_SECTION_ORDER = ["Datasets", "Benchmarks and Evaluation"]
VENUE_TYPE_ORDER = ["Conference", "Journal"]
CODE_STATUSES = {
    "train+inference",
    "inference-only",
    "evaluation-only",
    "pipeline",
    "announced",
    "withdrawn",
    "none",
    "unknown",
}
WEIGHT_STATUSES = {
    "released",
    "partial",
    "announced",
    "withdrawn",
    "not-applicable",
    "unknown",
}
CODE_STATUS_LABELS = {
    "train+inference": "training + inference",
    "inference-only": "inference only",
    "evaluation-only": "evaluation only",
    "pipeline": "pipeline",
    "announced": "announced",
    "withdrawn": "withdrawn",
    "none": "no release",
    "unknown": "unknown",
}
WEIGHT_STATUS_LABELS = {
    "released": "released",
    "partial": "partial",
    "announced": "announced",
    "withdrawn": "withdrawn",
    "not-applicable": "n/a",
    "unknown": "unknown",
}


def parse_date(value: str) -> date | None:
    value = value.strip()
    return date.fromisoformat(value) if value else None


def first_public_date(row: dict[str, str]) -> date | None:
    candidates = [parse_date(row["arxiv_date"]), parse_date(row["venue_date"])]
    candidates = [candidate for candidate in candidates if candidate is not None]
    return min(candidates) if candidates else None


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def load_rows() -> list[dict[str, str]]:
    if not RESOURCE_PATHS:
        raise ValueError("No data/resources*.csv files found")

    rows: list[dict[str, str]] = []
    for path in RESOURCE_PATHS:
        rows.extend(load_csv(path))

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


def load_metadata(paper_names: set[str]) -> dict[str, dict[str, str]]:
    metadata: dict[str, dict[str, str]] = {}
    for path in METADATA_PATHS:
        for row in load_csv(path):
            name = row["name"]
            if not name:
                raise ValueError(f"{path.name} contains an empty name")
            if name in metadata:
                raise ValueError(f"Duplicate paper metadata: {name}")
            if name not in paper_names:
                raise ValueError(f"Metadata does not match a paper entry: {name}")
            if row["code_status"] not in CODE_STATUSES:
                raise ValueError(f"Unknown code_status for {name}: {row['code_status']}")
            if row["weights_status"] not in WEIGHT_STATUSES:
                raise ValueError(
                    f"Unknown weights_status for {name}: {row['weights_status']}"
                )
            for field in ("project_url", "code_url", "weights_url"):
                if row[field] and not row[field].startswith("https://"):
                    raise ValueError(f"{field} must use HTTPS for {name}: {row[field]}")
            if row.get("checked_at"):
                parse_date(row["checked_at"])
            metadata[name] = row
    return metadata


def load_venues() -> list[dict[str, str]]:
    rows = load_csv(VENUES_PATH)
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


def dated_groups(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    dated: dict[int, list[tuple[date, dict[str, Any]]]] = defaultdict(list)
    undated: list[dict[str, Any]] = []

    for row in rows:
        sort_date = first_public_date(row)
        if sort_date is None:
            undated.append(row)
        else:
            dated[sort_date.year].append((sort_date, row))

    groups: list[dict[str, Any]] = []
    for year in sorted(dated, reverse=True):
        entries = [
            row
            for _, row in sorted(
                dated[year],
                key=lambda pair: (-pair[0].toordinal(), pair[1]["name"].casefold()),
            )
        ]
        groups.append({"year": str(year), "entries": entries})

    if undated:
        groups.append(
            {
                "year": "Other",
                "entries": sorted(undated, key=lambda row: row["name"].casefold()),
            }
        )
    return groups


def anchor(value: str) -> str:
    value = value.casefold().replace("&", "and")
    value = re.sub(r"[^a-z0-9\s-]", "", value)
    return re.sub(r"[\s-]+", "-", value).strip("-")


def entry(row: dict[str, Any]) -> str:
    line = f'- [{row["name"]}]({row["url"]}) - {row["description"].strip()}'
    metadata = row.get("metadata")
    if not metadata:
        return line

    release_bits: list[str] = []
    release_bits.append(
        f'[Project]({metadata["project_url"]})' if metadata["project_url"] else "Project: —"
    )

    code_label = CODE_STATUS_LABELS[metadata["code_status"]]
    release_bits.append(
        f'[Code]({metadata["code_url"]}) (`{code_label}`)'
        if metadata["code_url"]
        else f'Code: `{code_label}`'
    )

    weights_label = WEIGHT_STATUS_LABELS[metadata["weights_status"]]
    release_bits.append(
        f'[Weights]({metadata["weights_url"]}) (`{weights_label}`)'
        if metadata["weights_url"]
        else f'Weights: `{weights_label}`'
    )

    line = line.rstrip(".") + ". " + " · ".join(release_bits) + "."

    details: list[str] = []
    for label, field in (
        ("Method", "model_family"),
        ("Base", "backbone"),
        ("Train", "train_datasets"),
        ("Eval", "eval_datasets"),
        ("Output", "output_format"),
        ("Checked", "checked_at"),
    ):
        if metadata.get(field):
            details.append(f'**{label}:** {metadata[field]}')

    if details:
        line += "<br>  " + " · ".join(details) + "."
    return line


def generate() -> str:
    rows = load_rows()
    venues = load_venues()
    paper_names = {row["name"] for row in rows if row["section"] == "Papers"}
    metadata = load_metadata(paper_names)

    for row in rows:
        row["metadata"] = metadata.get(row["name"])

    by_section: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        by_section[row["section"]].append(row)

    paper_rows = by_section["Papers"]
    context = {
        "paper_category_order": PAPER_CATEGORY_ORDER,
        "dated_section_order": DATED_SECTION_ORDER,
        "survey_groups": dated_groups(by_section["Surveys and Overviews"]),
        "paper_groups": {
            category: dated_groups(
                [row for row in paper_rows if row["category"] == category]
            )
            for category in PAPER_CATEGORY_ORDER
        },
        "dated_sections": {
            section: dated_groups(by_section[section]) for section in DATED_SECTION_ORDER
        },
        "models": sorted(
            by_section["Models and Implementations"],
            key=lambda row: row["name"].casefold(),
        ),
        "related": sorted(
            by_section["Related Resources"], key=lambda row: row["name"].casefold()
        ),
        "conference_venues": sorted(
            [row for row in venues if row["type"] == "Conference"],
            key=lambda row: row["name"].casefold(),
        ),
        "journal_venues": sorted(
            [row for row in venues if row["type"] == "Journal"],
            key=lambda row: row["name"].casefold(),
        ),
    }

    environment = Environment(
        loader=FileSystemLoader(TEMPLATE_DIR),
        undefined=StrictUndefined,
        autoescape=False,
        keep_trailing_newline=True,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    environment.filters["anchor"] = anchor
    environment.filters["entry"] = entry
    template = environment.get_template("README.md.j2")
    return template.render(**context).rstrip() + "\n"


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
                "README.md is out of date. Run: uv run python scripts/generate_readme.py",
                file=sys.stderr,
            )
            return 1
        return 0

    README_PATH.write_text(generated, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
