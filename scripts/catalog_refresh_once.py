#!/usr/bin/env python3
"""One-off catalog refresh for newly audited poster research.

This script is intentionally idempotent and will be removed after the branch is refreshed.
"""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESOURCES = ROOT / "data" / "resources.csv"
METADATA = ROOT / "data" / "paper_metadata.csv"

RESOURCE_FIELDS = [
    "section",
    "category",
    "name",
    "url",
    "description",
    "venue",
    "venue_year",
    "arxiv_date",
    "venue_date",
    "date_note",
]

METADATA_FIELDS = [
    "name",
    "project_url",
    "code_url",
    "weights_url",
    "code_status",
    "weights_status",
    "model_family",
    "backbone",
    "train_datasets",
    "eval_datasets",
    "output_format",
    "notes",
    "checked_at",
]

RESOURCE_UPSERTS = [
    {
        "section": "Papers",
        "category": "Graphic Design Generation",
        "name": "PosterCraft",
        "url": "https://arxiv.org/abs/2506.10741",
        "description": "Generates high-aesthetic posters in a unified diffusion framework with staged text-rendering optimization, region-aware fine-tuning, preference optimization, and vision-language feedback (ICLR 2026).",
        "venue": "ICLR",
        "venue_year": "2026",
        "arxiv_date": "2025-06-12",
        "venue_date": "",
        "date_note": "arXiv v1",
    },
    {
        "section": "Papers",
        "category": "Graphic Design Generation",
        "name": "DreamPoster",
        "url": "https://arxiv.org/abs/2507.04218",
        "description": "Generates image-conditioned posters while preserving source content and supporting flexible resolution, layout, and typographic hierarchy with progressive multi-task training.",
        "venue": "Technical Report",
        "venue_year": "2025",
        "arxiv_date": "2025-07-06",
        "venue_date": "",
        "date_note": "arXiv v1",
    },
    {
        "section": "Papers",
        "category": "Graphic Design Generation",
        "name": "PosterOmni",
        "url": "https://arxiv.org/abs/2602.12127",
        "description": "Unifies local poster editing and global image-to-poster creation through task distillation and poster-specific reward feedback across six creation tasks (CVPR 2026).",
        "venue": "CVPR",
        "venue_year": "2026",
        "arxiv_date": "2026-02-12",
        "venue_date": "",
        "date_note": "arXiv v1",
    },
    {
        "section": "Papers",
        "category": "Graphic Design Generation",
        "name": "Chaining Text-to-Image and Large Language Model for Personalized E-commerce Banners",
        "url": "https://arxiv.org/abs/2403.05578",
        "description": "Chains an LLM with text-to-image generation to turn shopper interaction and product metadata into personalized e-commerce banner imagery at scale (KDD 2024).",
        "venue": "KDD",
        "venue_year": "2024",
        "arxiv_date": "2024-02-28",
        "venue_date": "2024-08-27",
        "date_note": "arXiv v1 precedes KDD 2024 presentation",
    },
    {
        "section": "Evaluation Methods and Metrics",
        "category": "",
        "name": "PosterReward",
        "url": "https://arxiv.org/abs/2603.29855",
        "description": "Provides poster-specific reward models that score graphic designs across visual quality, artifacts, textual accuracy, prompt fidelity, and aesthetics (CVPR 2026).",
        "venue": "CVPR",
        "venue_year": "2026",
        "arxiv_date": "2026-02-23",
        "venue_date": "",
        "date_note": "public preprint first posted 2026-02-23; later arXiv identifier 2603.29855",
    },
    {
        "section": "Datasets and Benchmarks",
        "category": "",
        "name": "PosterOmni-Bench",
        "url": "https://github.com/MeiGen-AI/PosterOmni",
        "description": "Benchmarks unified image-to-poster creation across local editing and global design tasks with reference adherence, composition, and aesthetic evaluation.",
        "venue": "CVPR",
        "venue_year": "2026",
        "arxiv_date": "2026-02-12",
        "venue_date": "",
        "date_note": "released with PosterOmni arXiv v1",
    },
    {
        "section": "Datasets and Benchmarks",
        "category": "",
        "name": "PosterRewardBench",
        "url": "https://github.com/MeiGen-AI/PosterReward/tree/main/poster_reward_bench",
        "description": "Benchmarks poster-reward models on professionally reviewed preference pairs spanning basic and advanced generation quality regimes.",
        "venue": "CVPR",
        "venue_year": "2026",
        "arxiv_date": "2026-02-23",
        "venue_date": "",
        "date_note": "released with PosterReward",
    },
    {
        "section": "Datasets and Benchmarks",
        "category": "",
        "name": "PosterBench",
        "url": "https://github.com/MeiGen-AI/PosterReward/tree/main/poster_bench",
        "description": "Benchmarks text-to-image poster generation over 250 prompts with repeated sampling and poster-specific multi-stage scoring.",
        "venue": "CVPR",
        "venue_year": "2026",
        "arxiv_date": "2026-02-23",
        "venue_date": "",
        "date_note": "released with PosterReward",
    },
]

METADATA_UPSERTS = [
    {
        "name": "PosterCraft",
        "project_url": "https://ephemeral182.github.io/PosterCraft/",
        "code_url": "https://github.com/MeiGen-AI/PosterCraft",
        "weights_url": "https://huggingface.co/PosterCraft/PosterCraft-v1_RL",
        "code_status": "inference-only",
        "weights_status": "released",
        "model_family": "Unified diffusion poster generation with staged text and aesthetic optimization",
        "backbone": "FLUX.1-dev",
        "train_datasets": "Text-Render-2M; HQ-Poster100K",
        "eval_datasets": "PosterCraft evaluation set",
        "output_format": "Raster poster image",
        "notes": "Official repository provides inference and demo code plus released model weights; no public end-to-end training entry point was located. Authors report partial dataset release.",
        "checked_at": "2026-10-06",
    },
    {
        "name": "PosterOmni",
        "project_url": "https://ephemeral182.github.io/PosterOmni/",
        "code_url": "https://github.com/MeiGen-AI/PosterOmni",
        "weights_url": "https://huggingface.co/MeiGen-AI/PosterOmni_v1",
        "code_status": "inference-only",
        "weights_status": "released",
        "model_family": "Unified multi-task image-to-poster generation and editing via task distillation and reward feedback",
        "backbone": "Qwen-Image-Edit / QwenImageEditPlusPipeline",
        "train_datasets": "PosterOmni-200K",
        "eval_datasets": "PosterOmni-Bench",
        "output_format": "Raster poster image",
        "notes": "Official repository provides inference for six poster tasks and released transformer weights; public training code was not located.",
        "checked_at": "2026-10-06",
    },
]


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_rows(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def upsert(rows: list[dict[str, str]], updates: list[dict[str, str]], key: str) -> None:
    index = {row[key]: i for i, row in enumerate(rows)}
    for update in updates:
        if update[key] in index:
            rows[index[update[key]]].update(update)
        else:
            rows.append(update)
            index[update[key]] = len(rows) - 1


def main() -> None:
    resources = read_rows(RESOURCES)
    metadata = read_rows(METADATA)
    upsert(resources, RESOURCE_UPSERTS, "name")
    upsert(metadata, METADATA_UPSERTS, "name")
    write_rows(RESOURCES, RESOURCE_FIELDS, resources)
    write_rows(METADATA, METADATA_FIELDS, metadata)


if __name__ == "__main__":
    main()
