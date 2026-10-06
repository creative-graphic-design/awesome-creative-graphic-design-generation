#!/usr/bin/env python3
"""One-time migration for SSII technology-map coverage follow-up."""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
RESOURCES = DATA / "resources.csv"
METHODS = DATA / "paper_methods.csv"

RESOURCE_FIELDS = [
    "section", "category", "name", "url", "description", "venue",
    "venue_year", "arxiv_date", "venue_date", "date_note",
]

ADDITIONS = [
    {
        "section": "Papers",
        "category": "Layout Generation",
        "name": "READ: Recursive Autoencoders for Document Layout Generation",
        "url": "https://arxiv.org/abs/1909.00302",
        "description": "Generates hierarchical document layouts with a recursive variational autoencoder and introduces a structural similarity metric for dense document compositions (CVPRW 2020).",
        "venue": "CVPR Workshop",
        "venue_year": "2020",
        "arxiv_date": "2019-09-01",
        "venue_date": "2020-06-15",
        "date_note": "arXiv v1 predates CVPRW 2020 presentation",
    },
    {
        "section": "Papers",
        "category": "Layout Generation",
        "name": "Machine Learning Model to Evaluate the Appropriateness of Layout for Automatic Generation of Graphic Design Works",
        "url": "https://doi.org/10.1109/IMCOM56909.2023.10035646",
        "description": "Uses adversarial layout generation and a trained discriminator to generate and score graphic-design layouts conditioned on specified materials (IMCOM 2023).",
        "venue": "IMCOM",
        "venue_year": "2023",
        "arxiv_date": "",
        "venue_date": "2023-01-03",
        "date_note": "IEEE proceedings publication date",
    },
    {
        "section": "Papers",
        "category": "Layout Generation",
        "name": "Layout Generation for Various Scenarios in Mobile Shopping Apps",
        "url": "https://doi.org/10.1145/3544548.3581446",
        "description": "Introduces LayoutVQ-VAE, a discrete latent model for generating layouts under internal and scenario-level constraints in mobile shopping applications (CHI 2023).",
        "venue": "CHI",
        "venue_year": "2023",
        "arxiv_date": "",
        "venue_date": "2023-04-26",
        "date_note": "CHI 2023 Creativity Support session",
    },
    {
        "section": "Papers",
        "category": "Content-Aware Layout Generation",
        "name": "Automatic Layout Planning for Visually-Rich Documents with Instruction-Following Models",
        "url": "https://arxiv.org/abs/2404.15271",
        "description": "Uses a multimodal instruction-following model to arrange user-provided visual elements for posters, brochures, book covers, advertisements, and related visually rich documents (ALVR 2024).",
        "venue": "ALVR Workshop",
        "venue_year": "2024",
        "arxiv_date": "2024-04-23",
        "venue_date": "2024-08-16",
        "date_note": "arXiv v1 predates ALVR 2024 workshop publication",
    },
    {
        "section": "Papers",
        "category": "Content-Aware Layout Generation",
        "name": "Iris: a multi-constraint graphic layout generation system",
        "url": "https://doi.org/10.1631/FITEE.2300312",
        "description": "Combines an interactive graphic-layout design system with multi-constraint LayoutVQ-VAE for background-aware generation, editing, and rendering (FITEE 2024).",
        "venue": "FITEE",
        "venue_year": "2024",
        "arxiv_date": "",
        "venue_date": "2024-07-27",
        "date_note": "publisher first-online date",
    },
    {
        "section": "Papers",
        "category": "Layout Generation",
        "name": "LayoutKAG: Enhancing Layout Generation in Large Language Models Through Knowledge-Augmented Generation",
        "url": "https://doi.org/10.1109/AIHCIR65563.2024.00056",
        "description": "Uses knowledge-augmented generation to improve large-language-model layout generation and control (AIHCIR 2024).",
        "venue": "AIHCIR",
        "venue_year": "2024",
        "arxiv_date": "",
        "venue_date": "2024-11-15",
        "date_note": "AIHCIR 2024 conference start",
    },
]

METHOD_ADDITIONS = [
    {
        "name": "READ: Recursive Autoencoders for Document Layout Generation",
        "method_family": "VAE",
        "note": "Recursive variational autoencoder (RvNN-VAE) over hierarchical document layouts",
    },
    {
        "name": "Machine Learning Model to Evaluate the Appropriateness of Layout for Automatic Generation of Graphic Design Works",
        "method_family": "GAN",
        "note": "Adversarial layout generator and discriminator; discriminator also scores layout appropriateness",
    },
    {
        "name": "Layout Generation for Various Scenarios in Mobile Shopping Apps",
        "method_family": "VAE",
        "note": "LayoutVQ-VAE with discrete latent layout representation and multi-constraint conditioning",
    },
    {
        "name": "Automatic Layout Planning for Visually-Rich Documents with Instruction-Following Models",
        "method_family": "LLM / VLM",
        "note": "mPLUG-Owl-based multimodal instruction-following layout planner (DocLap)",
    },
    {
        "name": "Iris: a multi-constraint graphic layout generation system",
        "method_family": "VAE",
        "note": "Multi-constraint LayoutVQ-VAE conditioned on background and design-element constraints",
    },
    {
        "name": "Iris: a multi-constraint graphic layout generation system",
        "method_family": "Agentic / Multi-stage System",
        "note": "Interactive specification, layout generation, custom editing, and rendering system",
    },
    {
        "name": "LayoutKAG: Enhancing Layout Generation in Large Language Models Through Knowledge-Augmented Generation",
        "method_family": "LLM / VLM",
        "note": "Knowledge-augmented large-language-model layout generation",
    },
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    resources = read_csv(RESOURCES)
    existing_names = {row["name"] for row in resources}
    for row in ADDITIONS:
        if row["name"] not in existing_names:
            resources.append(row)
            existing_names.add(row["name"])
    write_csv(RESOURCES, RESOURCE_FIELDS, resources)

    methods = read_csv(METHODS)
    existing_methods = {(row["name"], row["method_family"]) for row in methods}
    for row in METHOD_ADDITIONS:
        key = (row["name"], row["method_family"])
        if key not in existing_methods:
            methods.append(row)
            existing_methods.add(key)
    methods.sort(key=lambda row: (row["method_family"].casefold(), row["name"].casefold()))
    write_csv(METHODS, ["name", "method_family", "note"], methods)


if __name__ == "__main__":
    main()
