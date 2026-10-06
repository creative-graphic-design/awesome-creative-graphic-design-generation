#!/usr/bin/env python3
"""One-time audit migration for method coverage and missing graphic-design papers."""

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

RESOURCE_ADDITIONS = [
    {
        "section": "Papers", "category": "Graphic Design Generation",
        "name": "Vinci",
        "url": "https://doi.org/10.1145/3411764.3445117",
        "description": "Introduces an intelligent graphic-design system that composes advertising posters from user-provided product assets and design intent (CHI 2021).",
        "venue": "CHI", "venue_year": "2021", "arxiv_date": "", "venue_date": "2021-05-08",
        "date_note": "CHI 2021 conference start",
    },
    {
        "section": "Papers", "category": "Layout Generation",
        "name": "Constrained Graphic Layout Generation via Latent Optimization",
        "url": "https://arxiv.org/abs/2108.00871",
        "description": "Optimizes the latent space of a Transformer-based layout generator to satisfy alignment, overlap, and other explicit design constraints (ACM MM 2021).",
        "venue": "ACM MM", "venue_year": "2021", "arxiv_date": "2021-08-02", "venue_date": "",
        "date_note": "arXiv v1",
    },
    {
        "section": "Papers", "category": "Graphic Design Editing and Reconstruction",
        "name": "De-Rendering Stylized Texts",
        "url": "https://arxiv.org/abs/2110.01890",
        "description": "Vectorizes rasterized display text into editable content, geometry, font, styling, effects, and hidden-background parameters through differentiable rendering (ICCV 2021).",
        "venue": "ICCV", "venue_year": "2021", "arxiv_date": "2021-10-05", "venue_date": "",
        "date_note": "arXiv v1",
    },
    {
        "section": "Papers", "category": "Layout Generation",
        "name": "LayoutDM: Transformer-Based Diffusion Model for Layout Generation",
        "url": "https://arxiv.org/abs/2305.02567",
        "description": "Instantiates conditional DDPM layout generation with a purely Transformer-based denoiser for diverse, high-quality conditional layouts (CVPR 2023).",
        "venue": "CVPR", "venue_year": "2023", "arxiv_date": "2023-05-04", "venue_date": "",
        "date_note": "arXiv v1; distinct from the discrete-diffusion LayoutDM by Inoue et al.",
    },
    {
        "section": "Papers", "category": "Content-Aware Layout Generation",
        "name": "PDA-GAN",
        "url": "https://arxiv.org/abs/2303.14377",
        "description": "Uses GAN-based unsupervised domain adaptation with a pixel-level discriminator to generate image-aware advertising-poster layouts (CVPR 2023).",
        "venue": "CVPR", "venue_year": "2023", "arxiv_date": "2023-03-25", "venue_date": "",
        "date_note": "arXiv v1",
    },
    {
        "section": "Papers", "category": "Graphic Design Generation",
        "name": "CG4CTR",
        "url": "https://arxiv.org/abs/2401.10934",
        "description": "Builds a Stable-Diffusion-based advertising-creative generation pipeline that incorporates user preferences and downstream click-through-rate ranking (WWW 2024 Companion).",
        "venue": "WWW Companion", "venue_year": "2024", "arxiv_date": "2024-01-17", "venue_date": "",
        "date_note": "arXiv v1",
    },
    {
        "section": "Papers", "category": "Layout Generation",
        "name": "Spot the Error",
        "url": "https://arxiv.org/abs/2401.16375",
        "description": "Improves non-autoregressive graphic-layout generation with a learned wireframe locator that identifies erroneous layout tokens for iterative refinement (AAAI 2024).",
        "venue": "AAAI", "venue_year": "2024", "arxiv_date": "2024-01-29", "venue_date": "",
        "date_note": "arXiv v1",
    },
    {
        "section": "Papers", "category": "Layout Generation",
        "name": "CoLay",
        "url": "https://arxiv.org/abs/2405.13045",
        "description": "Uses multi-conditional latent diffusion to generate layouts with style properties from flexible combinations of text, guidelines, element types, and partial designs.",
        "venue": "arXiv", "venue_year": "2024", "arxiv_date": "2024-05-18", "venue_date": "",
        "date_note": "arXiv v1",
    },
    {
        "section": "Papers", "category": "Graphic Design Editing and Reconstruction",
        "name": "Revision Matters",
        "url": "https://arxiv.org/abs/2406.18559",
        "description": "Fine-tunes a Gemini multimodal backbone on human revision traces to iteratively refine generated layouts toward expert design edits.",
        "venue": "arXiv", "venue_year": "2024", "arxiv_date": "2024-05-27", "venue_date": "",
        "date_note": "arXiv v1 metadata reports first submission 2024-05-27",
    },
    {
        "section": "Papers", "category": "Scientific Poster and Slide Generation",
        "name": "PostDoc",
        "url": "https://arxiv.org/abs/2405.20213",
        "description": "Generates posters from long multimodal documents using learned submodular content selection, LLM paraphrasing, and content-conditioned template generation.",
        "venue": "AAAI", "venue_year": "2025", "arxiv_date": "2024-05-30", "venue_date": "",
        "date_note": "arXiv v1",
    },
    {
        "section": "Papers", "category": "Graphic Design Editing and Reconstruction",
        "name": "Neural Contrast",
        "url": "https://arxiv.org/abs/2410.07211",
        "description": "Uses diffusion-based generative editing to create low-saliency, high-contrast regions beneath design assets for improved graphic-design readability (PRICAI 2024).",
        "venue": "PRICAI", "venue_year": "2024", "arxiv_date": "2024-09-26", "venue_date": "",
        "date_note": "arXiv v1 metadata",
    },
    {
        "section": "Papers", "category": "Composable and Layered Asset Generation",
        "name": "Alfie",
        "url": "https://arxiv.org/abs/2408.14826",
        "description": "Modifies the inference behavior of a pretrained Diffusion Transformer to generate easily isolated RGBA-style illustration assets without additional training (ECCV 2024 AI4VA Workshop).",
        "venue": "ECCV Workshop", "venue_year": "2024", "arxiv_date": "2024-08-27", "venue_date": "",
        "date_note": "arXiv v1",
    },
    {
        "section": "Papers", "category": "Layout Generation",
        "name": "LGGPT",
        "url": "https://arxiv.org/abs/2502.14005",
        "description": "Unifies multiple layout-generation tasks and domains with compact instruction and response encodings for a 1.5B-parameter large language model.",
        "venue": "arXiv", "venue_year": "2025", "arxiv_date": "2025-02-19", "venue_date": "",
        "date_note": "arXiv v1",
    },
    {
        "section": "Papers", "category": "Graphic Design Generation",
        "name": "BizGen",
        "url": "https://arxiv.org/abs/2503.20672",
        "description": "Generates infographic and slide imagery from article-length prompts and ultra-dense layouts using layout-guided cross-attention and region-wise latent refinement (CVPR 2025).",
        "venue": "CVPR", "venue_year": "2025", "arxiv_date": "2025-03-26", "venue_date": "",
        "date_note": "arXiv v1",
    },
]

METHOD_ADDITIONS = {
    # Existing unclassified papers.
    "Coarse-to-Fine": [("VAE", "Hierarchical variational layout generation")],
    "i-Design": [("LLM / VLM", "InternVL-based multimodal aesthetic policy"), ("Autoregressive / Transformer", "Progressive autoregressive element placement")],
    "Learning Layouts for Single-Page Graphic Designs": [("Classical / Optimization", "Pre-deep-learning structured layout model")],
    "Neural Design Network": [("VAE", "Variational structured design model")],
    "Parse-Then-Place": [("Autoregressive / Transformer", "Parsed constraints followed by sequential placement")],
    "TextLap": [("LLM / VLM", "Customized language model for text-to-layout planning")],
    "CreatiPoster": [("LLM / VLM", "RGBA large multimodal model for layered poster planning"), ("Agentic / Multi-stage System", "Layer planning plus conditional background generation")],
    "Design Element Aware Poster Layout Generation": [("Autoregressive / Transformer", "Design-element-aware structured layout modeling")],
    "Graphist": [("LLM / VLM", "Multimodal structural context model")],
    "iPoster": [("Diffusion", "Graph-enhanced content-aware diffusion"), ("Graph Neural Network", "Graph-conditioned cross-content reasoning")],
    "RADM": [("Diffusion", "Content-aware advertising layout diffusion")],
    "SEGA": [("LLM / VLM", "LLaVA-based coarse and fine layout reasoning"), ("Agentic / Multi-stage System", "Coarse-to-fine stepwise evolution pipeline")],
    "SmartText": [("Agentic / Multi-stage System", "Saliency and aesthetic-compatibility text-placement system")],
    "Uni-Layout": [("LLM / VLM", "Natural-language-conditioned unified layout generation and evaluation"), ("Agentic / Multi-stage System", "Generator/evaluator preference-alignment framework")],
    "AutoPoster": [("Agentic / Multi-stage System", "Content analysis plus layout and rendering pipeline")],
    "AutoPP": [("Agentic / Multi-stage System", "Unified poster generation plus CTR-oriented preference optimization")],
    "Brief2Design": [("Agentic / Multi-stage System", "Requirement extraction, element exploration, and compositional recombination")],
    "COLE": [("LLM / VLM", "Language-model-guided hierarchical design planning"), ("Agentic / Multi-stage System", "Hierarchical planning and layered rendering framework")],
    "Desigen": [("Autoregressive / Transformer", "Autoregressive joint design generation")],
    "Human-aware Design Generation": [("Autoregressive / Transformer", "Causal and bidirectional Transformer modules"), ("VAE", "VQ-VAE human-pose representation")],
    "InnoAds-Composer": [("Diffusion", "Single-stage subject/glyph/style-conditioned diffusion")],
    "InterIL": [("Diffusion", "Coupled image and layout diffusion backbones")],
    "LaDeCo": [("LLM / VLM", "Large multimodal model for layer planning and attributes")],
    "Multi-Object Advertisement Creative Generation": [("Agentic / Multi-stage System", "Product pairing, layout, and background-generation modules")],
    "OpenCOLE": [("LLM / VLM", "Multimodal planning for graphic-design generation"), ("Agentic / Multi-stage System", "Open layered design-generation pipeline")],
    "Planning and Rendering": [("Agentic / Multi-stage System", "Separated semantic planning and visual rendering")],
    "PosterVerse": [("LLM / VLM", "LLM blueprint planning and multimodal HTML generation"), ("Diffusion", "Diffusion background generation"), ("Agentic / Multi-stage System", "Blueprint/background/typography pipeline")],
    "SIMPLEPOSTER": [("Diffusion", "FLUX-Fill diffusion-transformer poster generation"), ("Autoregressive / Transformer", "Diffusion Transformer backbone")],
    "PAID": [("LLM / VLM", "VLM prompt and layout expert models"), ("Diffusion", "SDXL-based layout-controlled background generation"), ("Agentic / Multi-stage System", "Four-stage prompt/layout/background/rendering framework")],
    "PrismLayers": [("Diffusion", "LayerFLUX and MultiLayerFLUX diffusion models"), ("Autoregressive / Transformer", "ART+ multi-layer Transformer component")],
    "SAWNA": [("Diffusion", "Training-free diffusion with negative-space-preserving noise control")],
    "Text2Poster": [("VAE", "Variational visual-textual poster composition model")],
    "TextPainter": [("Agentic / Multi-stage System", "Text understanding and image-space stylized rendering framework")],
    "Draw with Thought": [("LLM / VLM", "MLLM chain-of-thought for diagram reconstruction"), ("Agentic / Multi-stage System", "Coarse-to-fine code reconstruction pipeline")],
    "LayerD": [("Agentic / Multi-stage System", "Iterative matting and inpainting decomposition pipeline")],
    "PosterText": [("Flow Matching", "Text-patch generation/editing trained with a flow-matching objective")],
    "ReDesign": [("Agentic / Multi-stage System", "Agentic raster-to-editable design decomposition")],
    "AutoFigure-Edit": [("LLM / VLM", "LLM/VLM-guided scientific-figure parsing and refinement"), ("Agentic / Multi-stage System", "Multi-stage SVG reconstruction and refinement")],
    "Figures as Programs": [("LLM / VLM", "Program-generating multimodal agents"), ("Agentic / Multi-stage System", "Recursive SVG generation with render-critic refinement")],
    "GenGA": [("Agentic / Multi-stage System", "Source-grounded hierarchical vector generation framework")],
    "Any2Poster": [("LLM / VLM", "LLM analyzers/planner with VLM feedback"), ("Agentic / Multi-stage System", "Any-source poster generation agent")],
    "PosterGen": [("LLM / VLM", "LLM/VLM-driven scientific poster generation"), ("Agentic / Multi-stage System", "Parser/curator/layout/stylist/renderer agents")],
    "PosterVisor": [("Agentic / Multi-stage System", "Orchestrated semantic-geometric contracts with validation and repair")],
    "Scientific Poster Generation A New Dataset and Approach": [("Autoregressive / Transformer", "Template-free sequence-to-sequence poster-layout generator")],
    "SciPostGen": [("Agentic / Multi-stage System", "Retrieval-augmented scientific-poster layout generation pipeline")],
    "DreamPoster": [("Diffusion", "Seedream-based image-conditioned poster generation")],
    # Newly added coverage papers.
    "Vinci": [("Agentic / Multi-stage System", "End-to-end intelligent poster design system")],
    "Constrained Graphic Layout Generation via Latent Optimization": [("Classical / Optimization", "Constraint satisfaction through latent optimization"), ("Autoregressive / Transformer", "Transformer-based generative layout backbone")],
    "De-Rendering Stylized Texts": [("Agentic / Multi-stage System", "Neural vectorization plus differentiable rendering and reconstruction")],
    "LayoutDM: Transformer-Based Diffusion Model for Layout Generation": [("Diffusion", "Conditional DDPM for layouts"), ("Autoregressive / Transformer", "Pure Transformer denoiser")],
    "PDA-GAN": [("GAN", "Image-aware GAN with pixel-level discriminator and domain adaptation")],
    "CG4CTR": [("Diffusion", "Stable-Diffusion-based advertising creative generation"), ("Agentic / Multi-stage System", "Generation plus CTR-ranking pipeline")],
    "Spot the Error": [("Encoder-only Neural Model", "Non-autoregressive token refinement with wireframe error locator")],
    "CoLay": [("Diffusion", "Multi-conditional latent diffusion for controllable layouts")],
    "Revision Matters": [("LLM / VLM", "Gemini multimodal backbone fine-tuned on designer revisions")],
    "PostDoc": [("Classical / Optimization", "Deep submodular multimodal content selection"), ("LLM / VLM", "LLM paraphrasing for poster content"), ("Agentic / Multi-stage System", "Content selection, template generation, and harmonization pipeline")],
    "Neural Contrast": [("Diffusion", "Generative diffusion editing beneath design assets")],
    "Alfie": [("Diffusion", "Inference-time RGBA generation with a pretrained Diffusion Transformer"), ("Autoregressive / Transformer", "Diffusion Transformer backbone")],
    "LGGPT": [("LLM / VLM", "1.5B instruction-tuned LLM for unified layout generation")],
    "BizGen": [("Diffusion", "Layout-guided latent image generation with region-wise refinement")],
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def migrate_resources() -> None:
    rows = read_csv(RESOURCES)

    # Correct an early alias: arXiv:2501.14316 is formally titled PAID.
    for row in rows:
        if row["name"] == "T-Stars-Poster" and row["url"] == "https://arxiv.org/abs/2501.14316":
            row["name"] = "PAID"
            row["description"] = "Generates product-centric advertising images through VLM prompt and layout experts, SDXL-based background generation, and final graphics rendering (2025)."
            row["venue"] = "arXiv"
            row["venue_year"] = "2025"
            row["date_note"] = "arXiv v1; canonical title corrected from an earlier alias"

    names = {row["name"] for row in rows}
    urls = {row["url"] for row in rows}
    for addition in RESOURCE_ADDITIONS:
        if addition["name"] in names or addition["url"] in urls:
            continue
        rows.append(addition)
        names.add(addition["name"])
        urls.add(addition["url"])

    write_csv(RESOURCES, RESOURCE_FIELDS, rows)


def migrate_methods() -> None:
    rows = read_csv(METHODS)
    # Handle the same canonical rename if a prior method row ever existed.
    for row in rows:
        if row["name"] == "T-Stars-Poster":
            row["name"] = "PAID"

    seen = {(row["name"], row["method_family"]) for row in rows}
    for name, labels in METHOD_ADDITIONS.items():
        for family, note in labels:
            key = (name, family)
            if key not in seen:
                rows.append({"name": name, "method_family": family, "note": note})
                seen.add(key)

    rows.sort(key=lambda row: (row["method_family"].casefold(), row["name"].casefold()))
    write_csv(METHODS, ["name", "method_family", "note"], rows)


if __name__ == "__main__":
    migrate_resources()
    migrate_methods()
