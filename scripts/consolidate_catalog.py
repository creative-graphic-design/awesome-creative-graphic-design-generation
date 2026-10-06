#!/usr/bin/env python3
"""One-time migration: consolidate bootstrap CSV shards into canonical catalogs."""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

RESOURCE_FIELDS = [
    "section", "category", "name", "url", "description", "venue",
    "venue_year", "arxiv_date", "venue_date", "date_note",
]
METADATA_FIELDS = [
    "name", "project_url", "code_url", "weights_url", "code_status",
    "weights_status", "model_family", "backbone", "train_datasets",
    "eval_datasets", "output_format", "notes", "checked_at",
]
SECTION_ORDER = [
    "Surveys and Overviews", "Papers", "Datasets and Benchmarks",
    "Evaluation Methods and Metrics", "Models and Implementations",
    "Related Resources",
]
PAPER_CATEGORY_ORDER = [
    "Layout Generation", "Content-Aware Layout Generation",
    "Graphic Design Generation", "Composable and Layered Asset Generation",
    "Typography and Text Rendering", "Graphic Design Editing and Reconstruction",
    "Scientific Figure and Graphical Abstract Generation",
    "Scientific Poster and Slide Generation",
]
LEGACY_EVALUATION_METHOD_NAMES = {
    "Graphic Design Evaluation", "Layout FID", "LTSim",
}


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def canonical_section(row: dict[str, str]) -> str:
    section = row["section"]
    if section == "Datasets":
        return "Datasets and Benchmarks"
    if section == "Benchmarks and Evaluation":
        return (
            "Evaluation Methods and Metrics"
            if row["name"] in LEGACY_EVALUATION_METHOD_NAMES
            else "Datasets and Benchmarks"
        )
    return section


def write_rows(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    resource_paths = sorted(DATA.glob("resources*.csv"))
    resources: list[dict[str, str]] = []
    seen_resource_names: set[tuple[str, str, str]] = set()
    seen_urls: set[str] = set()

    for path in resource_paths:
        for row in read_rows(path):
            row["section"] = canonical_section(row)
            key = (row["section"], row["category"], row["name"])
            if key in seen_resource_names:
                raise ValueError(f"Duplicate resource during migration: {key}")
            if row["url"] in seen_urls:
                raise ValueError(f"Duplicate resource URL during migration: {row['url']}")
            seen_resource_names.add(key)
            seen_urls.add(row["url"])
            resources.append({field: row.get(field, "") for field in RESOURCE_FIELDS})

    section_rank = {name: index for index, name in enumerate(SECTION_ORDER)}
    category_rank = {name: index for index, name in enumerate(PAPER_CATEGORY_ORDER)}
    resources.sort(
        key=lambda row: (
            section_rank[row["section"]],
            category_rank.get(row["category"], 999),
            row["name"].casefold(),
        )
    )
    write_rows(DATA / "resources.csv", RESOURCE_FIELDS, resources)

    metadata_paths = sorted(DATA.glob("paper_metadata*.csv"))
    metadata: list[dict[str, str]] = []
    seen_metadata: set[str] = set()
    for path in metadata_paths:
        for row in read_rows(path):
            name = row["name"]
            if name in seen_metadata:
                raise ValueError(f"Duplicate paper metadata during migration: {name}")
            seen_metadata.add(name)
            metadata.append({field: row.get(field, "") for field in METADATA_FIELDS})
    metadata.sort(key=lambda row: row["name"].casefold())
    write_rows(DATA / "paper_metadata.csv", METADATA_FIELDS, metadata)

    for path in resource_paths:
        if path.name != "resources.csv":
            path.unlink()
    for path in metadata_paths:
        if path.name != "paper_metadata.csv":
            path.unlink()

    print(f"Consolidated {len(resources)} resources and {len(metadata)} audited papers.")


if __name__ == "__main__":
    main()
