#!/usr/bin/env python3
"""One-time migration: add missing layout work, workshops, and method index."""

from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
RESOURCES = DATA / "resources.csv"
METADATA = DATA / "paper_metadata.csv"
METHODS = DATA / "paper_methods.csv"
VENUES = DATA / "venues.csv"

RESOURCE_FIELDS = [
    "section", "category", "name", "url", "description", "venue",
    "venue_year", "arxiv_date", "venue_date", "date_note",
]

RESOURCE_ADDITIONS = [
    {
        "section": "Papers",
        "category": "Content-Aware Layout Generation",
        "name": "UniLayDiff",
        "url": "https://arxiv.org/abs/2512.08897",
        "description": "Unifies diverse content-aware layout constraints in a single multimodal diffusion transformer with relation-aware LoRA adaptation.",
        "venue": "arXiv", "venue_year": "2025", "arxiv_date": "2025-12-09",
        "venue_date": "", "date_note": "arXiv v1",
    },
    {
        "section": "Papers",
        "category": "Content-Aware Layout Generation",
        "name": "LLMs as Layout Designers (LaySPA)",
        "url": "https://arxiv.org/abs/2509.16891",
        "description": "Augments language-model layout agents with reinforcement-learned spatial reasoning over geometric validity, structural fidelity, and visual quality.",
        "venue": "arXiv", "venue_year": "2025", "arxiv_date": "2025-09-21",
        "venue_date": "", "date_note": "arXiv v1",
    },
    {
        "section": "Papers",
        "category": "Layout Generation",
        "name": "LayoutRectifier",
        "url": "https://arxiv.org/abs/2508.11177",
        "description": "Rectifies generated graphic layouts with two-stage optimization over grid alignment, overlap, and containment while limiting deviation from the input layout (Pacific Graphics 2025).",
        "venue": "Pacific Graphics", "venue_year": "2025", "arxiv_date": "2025-08-15",
        "venue_date": "", "date_note": "arXiv v1",
    },
    {
        "section": "Papers",
        "category": "Content-Aware Layout Generation",
        "name": "ReLayout: Relation Reasoning for Content-Aware Layout Generation",
        "url": "https://arxiv.org/abs/2507.05568",
        "description": "Uses relation chain-of-thought and layout-prototype rebalancing to improve structure, diversity, and explainability in multimodal-LLM content-aware layouts.",
        "venue": "arXiv", "venue_year": "2025", "arxiv_date": "2025-07-08",
        "venue_date": "", "date_note": "arXiv v1",
    },
    {
        "section": "Papers",
        "category": "Content-Aware Layout Generation",
        "name": "CAL-RAG",
        "url": "https://arxiv.org/abs/2506.21934",
        "description": "Combines multimodal retrieval, an LLM layout recommender, a vision-language grader, and feedback agents for iterative content-aware layout generation.",
        "venue": "arXiv", "venue_year": "2025", "arxiv_date": "2025-06-27",
        "venue_date": "", "date_note": "arXiv v1",
    },
    {
        "section": "Papers",
        "category": "Layout Generation",
        "name": "StructLayoutFormer",
        "url": "https://doi.org/10.1109/TVCG.2025.3574311",
        "description": "Generates explicitly structured layouts with a Transformer using structure serialization and disentanglement for conditional structure control (TVCG 2025).",
        "venue": "TVCG", "venue_year": "2025", "arxiv_date": "2025-10-30",
        "venue_date": "2025-05-27", "date_note": "IEEE early-access publication predates arXiv v1",
    },
    {
        "section": "Papers",
        "category": "Content-Aware Layout Generation",
        "name": "AesthetiQ",
        "url": "https://arxiv.org/abs/2503.00591",
        "description": "Aligns multimodal language models to aesthetic preferences for content-aware graphic layout prediction using preference optimization (CVPR 2025).",
        "venue": "CVPR", "venue_year": "2025", "arxiv_date": "2025-03-01",
        "venue_date": "", "date_note": "arXiv v1",
    },
    {
        "section": "Papers",
        "category": "Content-Aware Layout Generation",
        "name": "VASCAR",
        "url": "https://arxiv.org/abs/2412.04237",
        "description": "Uses a large vision-language model to iteratively inspect rendered layouts and self-correct content-aware element placement without additional training.",
        "venue": "arXiv", "venue_year": "2024", "arxiv_date": "2024-12-05",
        "venue_date": "", "date_note": "arXiv v1",
    },
    {
        "section": "Papers",
        "category": "Layout Generation",
        "name": "Sketch-to-Layout",
        "url": "https://arxiv.org/abs/2510.27632",
        "description": "Generates layouts from intuitive user sketches and content assets with a multimodal Transformer and releases large-scale synthetic sketch supervision (ICCV 2025 HiGen Workshop).",
        "venue": "ICCV Workshop (HiGen)", "venue_year": "2025", "arxiv_date": "2025-10-31",
        "venue_date": "2025-10-19", "date_note": "HiGen workshop presentation predates arXiv v1",
    },
    {
        "section": "Papers",
        "category": "Graphic Design Editing and Reconstruction",
        "name": "ReLayout: Structure-Preserving Design Layout Editing",
        "url": "https://arxiv.org/abs/2602.01046",
        "description": "Edits design layouts from natural-language intents while preserving unedited structure through relation graphs and self-supervised relation-aware design reconstruction.",
        "venue": "arXiv", "venue_year": "2026", "arxiv_date": "2026-02-01",
        "venue_date": "", "date_note": "arXiv v1",
    },
    {
        "section": "Evaluation Methods and Metrics",
        "category": "",
        "name": "Design-o-Meter",
        "url": "https://arxiv.org/abs/2411.14959",
        "description": "Scores graphic-design quality and proposes refinements within a unified learned evaluation-and-improvement framework (WACV 2025).",
        "venue": "WACV", "venue_year": "2025", "arxiv_date": "2024-11-22",
        "venue_date": "", "date_note": "arXiv v1",
    },
]

VENUE_ADDITIONS = [
    {
        "type": "Conference", "name": "WACV", "url": "https://wacv.thecvf.com/",
        "note": "Computer vision; includes graphic-design evaluation and multimodal visual-generation work.",
    },
    {
        "type": "Conference", "name": "Pacific Graphics", "url": "https://pg2025.nccu.edu.tw/",
        "note": "Computer graphics; includes optimization, authoring, and graphic-layout research.",
    },
    {
        "type": "Workshop", "name": "Graphic Design Understanding and Generation (GDUG)",
        "url": "https://sites.google.com/view/gdug-workshop",
        "note": "Dedicated graphic-design workshop series; held at CVPR 2024 and ICCV 2025 with topics spanning layout, typography, datasets, evaluation, and AI-assisted authoring.",
    },
    {
        "type": "Workshop", "name": "Human-Interactive Generation and Editing (HiGen)",
        "url": "https://higen-2025.github.io/",
        "note": "Human-interactive visual generation and editing workshop; first held at ICCV 2025 and second at CVPR 2026, including multimodal control and sketch-guided design generation.",
    },
    {
        "type": "Workshop", "name": "AI for Content Creation (AI4CC)",
        "url": "https://ai-for-content-creation.github.io/",
        "note": "Recurring CVPR workshop on AI-assisted content creation across art, design, documents, advertising, photography, video, and related media.",
    },
    {
        "type": "Workshop", "name": "AI for Creative Visual Content Generation, Editing and Understanding (CVEU)",
        "url": "https://openaccess.thecvf.com/CVPR2025_workshops/CVEU",
        "note": "Workshop series on generative and editing technologies for creative visual content, with editions across CVPR, ICCV, ECCV, and SIGGRAPH-related venues.",
    },
]

EXPLICIT_METHODS = {
    "UniLayDiff": [("Diffusion", "Multimodal diffusion transformer"), ("Autoregressive / Transformer", "Diffusion Transformer backbone")],
    "LLMs as Layout Designers (LaySPA)": [("LLM / VLM", "LLM spatial reasoning with reinforcement learning")],
    "LayoutRectifier": [("Classical / Optimization", "Two-stage discrete and continuous layout optimization")],
    "ReLayout: Relation Reasoning for Content-Aware Layout Generation": [("LLM / VLM", "Relation-CoT with a multimodal large language model")],
    "CAL-RAG": [("LLM / VLM", "LLM/VLM retrieval-and-grading loop"), ("Agentic / Multi-stage System", "Retrieval-augmented collaborative agents")],
    "StructLayoutFormer": [("Autoregressive / Transformer", "Transformer with structure serialization and disentanglement")],
    "AesthetiQ": [("LLM / VLM", "Multimodal LLM preference alignment")],
    "VASCAR": [("LLM / VLM", "LVLM visual-aware self-correction")],
    "Sketch-to-Layout": [("Autoregressive / Transformer", "Multimodal Transformer")],
    "ReLayout: Structure-Preserving Design Layout Editing": [("LLM / VLM", "MLLM-based relation-aware design reconstruction")],
    "LayoutGAN": [("GAN", "Generative adversarial layout model")],
    "LayoutGAN++": [("GAN", "GAN with differentiable rendering")],
    "ContentGAN": [("GAN", "Content-aware generative adversarial model")],
    "CGL-GAN": [("GAN", "Content-aware generative adversarial model")],
    "LayoutVAE": [("VAE", "Variational autoencoder")],
    "CanvasVAE": [("VAE", "Variational autoencoder")],
    "ICVT": [("VAE", "Geometry-aligned variational Transformer"), ("Autoregressive / Transformer", "Transformer backbone")],
    "LayoutFlow": [("Flow Matching", "Continuous flow-matching layout model")],
    "LayoutGPT": [("LLM / VLM", "In-context language-model layout generation")],
    "LayoutNUWA": [("LLM / VLM", "Code-oriented language model")],
    "LayoutPrompter": [("LLM / VLM", "In-context LLM prompting")],
    "PosterLLaMA": [("LLM / VLM", "Multimodal language model")],
    "PosterLLaVA": [("LLM / VLM", "Multimodal instruction-tuned language model")],
    "BannerAgency": [("Agentic / Multi-stage System", "Collaborating multimodal agents"), ("LLM / VLM", "Multimodal LLM agents")],
    "PSDesigner": [("Agentic / Multi-stage System", "Tool-using graphic-design agent"), ("LLM / VLM", "Multimodal planner")],
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def migrate_resources() -> list[dict[str, str]]:
    rows = read_csv(RESOURCES)
    names = {row["name"] for row in rows}
    for addition in RESOURCE_ADDITIONS:
        if addition["name"] not in names:
            rows.append(addition)
            names.add(addition["name"])

    # PosterO is explicitly content-aware in the paper title and formulation.
    for row in rows:
        if row["name"] == "PosterO":
            row["category"] = "Content-Aware Layout Generation"
    write_csv(RESOURCES, RESOURCE_FIELDS, rows)
    return rows


def migrate_venues() -> None:
    rows = read_csv(VENUES)
    names = {row["name"] for row in rows}
    for addition in VENUE_ADDITIONS:
        if addition["name"] not in names:
            rows.append(addition)
            names.add(addition["name"])
    write_csv(VENUES, ["type", "name", "url", "note"], rows)


def infer_methods(resource: dict[str, str], meta: dict[str, str] | None) -> list[tuple[str, str]]:
    if resource["name"] in EXPLICIT_METHODS:
        return EXPLICIT_METHODS[resource["name"]]

    metadata_text = ""
    note = ""
    if meta:
        metadata_text = " ".join(
            [meta.get("model_family", ""), meta.get("backbone", ""), meta.get("notes", "")]
        )
        note = meta.get("model_family", "").strip()
    text = f'{resource["name"]} {resource["description"]} {metadata_text}'.casefold()
    families: list[str] = []

    def add(family: str) -> None:
        if family not in families:
            families.append(family)

    if "diffusion" in text or "denois" in text:
        add("Diffusion")
    if "flow matching" in text or "flow-matching" in text or "flow-based" in text:
        add("Flow Matching")
    if re.search(r"\bgan\b", text) or "generative adversarial" in text:
        add("GAN")
    if "variational autoencoder" in text or re.search(r"\bvae\b", text):
        add("VAE")
    if any(term in text for term in [
        "autoregressive", "transformer", "sequence-to-sequence", "bidirectional layout",
        "serialized layout", "serialization", "masked transformer",
    ]):
        add("Autoregressive / Transformer")
    if any(term in text for term in [
        "large language", "language model", "llm", "vlm", "vision-language",
        "multimodal language", "multi-modal language", "qwen", "llama", "gemini", "gpt-",
    ]):
        add("LLM / VLM")
    if any(term in text for term in ["agentic", "multi-agent", "multi agent", "collaborating agents", "tool-using", "agent pipeline"]):
        add("Agentic / Multi-stage System")
    if "graph convolution" in text or re.search(r"\bgcn\b", text):
        add("Graph Neural Network")
    if re.search(r"\bbert\b", text):
        add("Encoder-only Neural Model")
    if any(term in text for term in ["optimization-based", "grid-based", "constraint solver", "combinatorial optimization"]):
        add("Classical / Optimization")

    return [(family, note) for family in families]


def migrate_methods(resources: list[dict[str, str]]) -> None:
    metadata = {row["name"]: row for row in read_csv(METADATA)}
    paper_rows = [row for row in resources if row["section"] == "Papers"]
    output: list[dict[str, str]] = []
    seen: set[tuple[str, str]] = set()
    for resource in paper_rows:
        for family, note in infer_methods(resource, metadata.get(resource["name"])):
            key = (resource["name"], family)
            if key in seen:
                continue
            seen.add(key)
            output.append({"name": resource["name"], "method_family": family, "note": note})
    output.sort(key=lambda row: (row["method_family"], row["name"].casefold()))
    write_csv(METHODS, ["name", "method_family", "note"], output)


def main() -> None:
    resources = migrate_resources()
    migrate_venues()
    migrate_methods(resources)


if __name__ == "__main__":
    main()
