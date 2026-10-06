#!/usr/bin/env python3
"""One-time follow-up migration for historical layout coverage and method labels."""

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
        "section": "Papers", "category": "Layout Generation", "name": "CLASS",
        "url": "https://openaccess.thecvf.com/content/WACV2025/html/Manandhar_CLASS_Conditional_Latent_Architecture_for_Search_and_Synthesis_of_Design_WACV_2025_paper.html",
        "description": "Unifies layout synthesis and retrieval with a variational latent representation, an autoregressive Transformer layout decoder, and a raster decoder (WACV 2025).",
        "venue": "WACV", "venue_year": "2025", "arxiv_date": "", "venue_date": "2025-02-26",
        "date_note": "WACV 2025 conference start",
    },
    {
        "section": "Papers", "category": "Layout Generation", "name": "Learn and Sample Together",
        "url": "https://www.ijcai.org/proceedings/2023/649",
        "description": "Jointly trains a spatial-graph generator and graph-conditioned layout decoder with collaborative knowledge transfer for constrained graphic-layout generation (IJCAI 2023).",
        "venue": "IJCAI", "venue_year": "2023", "arxiv_date": "", "venue_date": "2023-08-19",
        "date_note": "IJCAI 2023 conference start",
    },
    {
        "section": "Papers", "category": "Graphic Design Generation", "name": "CreaGAN",
        "url": "https://doi.org/10.1145/3503161.3548763",
        "description": "Automates display-ad creative adaptation with aesthetics-aware product placement and context-aware inpainting while reusing existing design elements (ACM MM 2022).",
        "venue": "ACM MM", "venue_year": "2022", "arxiv_date": "", "venue_date": "2022-10-10",
        "date_note": "ACM Multimedia 2022 conference start",
    },
    {
        "section": "Papers", "category": "Layout Generation", "name": "LayoutMCL",
        "url": "https://arxiv.org/abs/2301.06629",
        "description": "Uses an autoregressive multi-choice predictor with winner-takes-all learning to generate diverse multimedia layouts from the same input (ACM MM 2021).",
        "venue": "ACM MM", "venue_year": "2021", "arxiv_date": "2023-01-16", "venue_date": "2021-10-20",
        "date_note": "ACM Multimedia 2021 presentation predates arXiv v1",
    },
    {
        "section": "Papers", "category": "Layout Generation", "name": "VTN",
        "url": "https://arxiv.org/abs/2104.02416",
        "description": "Combines self-attention with a variational autoencoder to learn global design rules and synthesize diverse layouts (CVPR 2021).",
        "venue": "CVPR", "venue_year": "2021", "arxiv_date": "2021-04-06", "venue_date": "",
        "date_note": "arXiv v1",
    },
    {
        "section": "Papers", "category": "Layout Generation", "name": "AC-LayoutGAN",
        "url": "https://doi.org/10.1109/TVCG.2020.2999335",
        "description": "Generates graphic layouts conditioned on element attributes such as area, aspect ratio, and reading order with an attribute-conditioned GAN (TVCG).",
        "venue": "TVCG", "venue_year": "2021", "arxiv_date": "2020-09-11", "venue_date": "2020-06-02",
        "date_note": "IEEE early-access publication predates arXiv v1 and 2021 issue",
    },
    {
        "section": "Papers", "category": "Layout Generation", "name": "DesignScape",
        "url": "https://doi.org/10.1145/2702123.2702149",
        "description": "Provides interactive refinement and brainstorming layout suggestions that improve position, scale, and alignment during graphic-design authoring (CHI 2015).",
        "venue": "CHI", "venue_year": "2015", "arxiv_date": "", "venue_date": "2015-04-18",
        "date_note": "ACM publication / CHI 2015 conference start",
    },
    {
        "section": "Evaluation Methods and Metrics", "category": "", "name": "LayoutGCN",
        "url": "https://research.adobe.com/publication/learning-structural-similarity-of-user-interface-layouts-using-graph-networks/",
        "description": "Learns structural layout-similarity embeddings with a graph-convolutional encoder and convolutional decoder for retrieval over interface layouts (ECCV 2020).",
        "venue": "ECCV", "venue_year": "2020", "arxiv_date": "", "venue_date": "2020-03-01",
        "date_note": "Adobe Research publication date",
    },
]

METHOD_ADDITIONS = [
    ("CLASS", "VAE", "Variational latent layout representation"),
    ("CLASS", "Autoregressive / Transformer", "Autoregressive Transformer layout decoder"),
    ("Learn and Sample Together", "Encoder-only Neural Model", "BERT-like graph modeling in a collaborative two-stage generator"),
    ("CreaGAN", "GAN", "Aesthetics-aware placement plus creative inpainting framework"),
    ("CreaGAN", "Agentic / Multi-stage System", "Two-stage placement and inpainting framework"),
    ("LayoutMCL", "Autoregressive / Transformer", "Autoregressive multi-choice layout predictor"),
    ("VTN", "VAE", "Variational autoencoder formulation"),
    ("VTN", "Autoregressive / Transformer", "Self-attention / Transformer backbone"),
    ("AC-LayoutGAN", "GAN", "Attribute-conditioned generative adversarial network"),
    ("DesignScape", "Classical / Optimization", "Interactive layout suggestion and refinement system"),
]

FALSE_POSITIVE_METHODS = {
    ("MRT", "LLM / VLM"),
    ("PosterOmni", "LLM / VLM"),
    ("Qwen-Image-Layered", "LLM / VLM"),
}


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
    names = {row["name"] for row in resources}
    for row in ADDITIONS:
        if row["name"] not in names:
            resources.append(row)
            names.add(row["name"])
    write_csv(RESOURCES, RESOURCE_FIELDS, resources)

    methods = read_csv(METHODS)
    methods = [
        row for row in methods
        if (row["name"], row["method_family"]) not in FALSE_POSITIVE_METHODS
    ]
    seen = {(row["name"], row["method_family"]) for row in methods}
    for name, family, note in METHOD_ADDITIONS:
        if (name, family) not in seen:
            methods.append({"name": name, "method_family": family, "note": note})
            seen.add((name, family))
    methods.sort(key=lambda row: (row["method_family"], row["name"].casefold()))
    write_csv(METHODS, ["name", "method_family", "note"], methods)


if __name__ == "__main__":
    main()
