#!/usr/bin/env python3
"""One-time normalization of the LayoutGAN++ paper alias to its canonical paper title."""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
CANONICAL = "Constrained Graphic Layout Generation via Latent Optimization"
ALIAS = "LayoutGAN++"


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader.fieldnames or []), list(reader)


def write_csv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def rename(path: Path) -> None:
    fields, rows = read_csv(path)
    for row in rows:
        if row.get("name") == ALIAS:
            row["name"] = CANONICAL
            if path.name == "resources.csv":
                row["description"] = "Introduces LayoutGAN++ and constrained latent optimization for generating realistic layouts that satisfy alignment, overlap, and other explicit design constraints (ACM MM 2021)."
                row["venue"] = "ACM MM"
                row["venue_year"] = "2021"
                row["arxiv_date"] = "2021-08-02"
                row["date_note"] = "arXiv v1; LayoutGAN++ is a model contribution within this paper"
    write_csv(path, fields, rows)


if __name__ == "__main__":
    rename(DATA / "resources.csv")
    rename(DATA / "paper_methods.csv")
    rename(DATA / "paper_metadata.csv")
