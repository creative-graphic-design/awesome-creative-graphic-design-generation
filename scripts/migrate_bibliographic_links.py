#!/usr/bin/env python3
"""One-off deterministic migration for publication/arXiv links in resources.csv.

The final schema stays in data/resources.csv. This helper is temporary and will be
removed after the migration lands. It performs no network requests: authoritative
publication URLs that have been verified are pinned below, while unresolved
preprint-primary entries remain direct arXiv links rather than arXiv DOI surrogates.
"""

from __future__ import annotations

import csv
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
RESOURCE_PATH = ROOT / "data" / "resources.csv"

PUBLICATION_OVERRIDES: dict[str, str] = {
    "AutoPP": "https://ojs.aaai.org/index.php/AAAI/article/view/37377",
    "CGL-GAN": "https://www.ijcai.org/proceedings/2022/692",
    "CreatiDesign": "https://proceedings.iclr.cc/paper_files/paper/2026/hash/b46b78c353f672d83997d4cce5f1b0fb-Abstract-Conference.html",
    "Design Your Ad": "https://openaccess.thecvf.com/content/CVPR2026/html/Xu_Design_Your_Ad_Personalized_Advertising_Image_and_Text_Generation_with_CVPR_2026_paper.html",
    "Dolfin": "https://doi.org/10.1007/978-3-031-72983-6_19",
    "GlyphDraw2": "https://ojs.aaai.org/index.php/AAAI/article/view/32636",
    "InnoAds-Composer": "https://openaccess.thecvf.com/content/CVPR2026/html/Qin_InnoAds-Composer_Efficient_Condition_Composition_for_E-Commerce_Poster_Generation_CVPR_2026_paper.html",
    "LACE": "https://proceedings.iclr.cc/paper_files/paper/2024/hash/25d61d11fcbbfb28d1fbcc217141e776-Abstract-Conference.html",
    "Layout-Corrector": "https://doi.org/10.1007/978-3-031-72754-2_6",
    "LayoutDETR": "https://link.springer.com/chapter/10.1007/978-3-031-72661-3_10",
    "LayoutFlow": "https://link.springer.com/chapter/10.1007/978-3-031-72764-1_4",
    "LayoutGPT": "https://proceedings.neurips.cc/paper_files/paper/2023/hash/3a7f9e485845dac27423375c934cb4db-Abstract.html",
    "LayoutNUWA": "https://proceedings.iclr.cc/paper_files/paper/2024/hash/a6a1e4c756d700d9aedcc1896a7e6fb0-Abstract-Conference.html",
    "LayoutPrompter": "https://proceedings.neurips.cc/paper_files/paper/2023/hash/88a129e44f25a571ae8b838057c46855-Abstract-Conference.html",
    "MRT": "https://openaccess.thecvf.com/content/CVPR2026/html/Tang_Masked_Region_Transformer_for_Layered_Image_Generation_and_Editing_at_CVPR_2026_paper.html",
    "Mise-en-Scène": "https://human-ai-co-creation.github.io/workshop/",
    "P2P": "https://proceedings.iclr.cc/paper_files/paper/2026/hash/1fe6f635fe265292aba3987b5123ae3d-Abstract-Conference.html",
    "PLay": "https://proceedings.mlr.press/v202/cheng23b.html",
    "Paper2Poster": "https://proceedings.neurips.cc/paper_files/paper/2025/hash/17337b1d5eeac8b59c80e025a552fa7a-Abstract-Datasets_and_Benchmarks_Track.html",
    "PosterForest": "https://aclanthology.org/2026.acl-long.15/",
    "PosterGen": "https://openaccess.thecvf.com/content/CVPR2026F/papers/Zhang_PosterGen_Aesthetic-Aware_Multi-Modal_Paper-to-Poster_Generation_Via_Multi-Agent_LLMs_CVPRF_2026_paper.pdf",
    "PosterLLaMA": "https://doi.org/10.1007/978-3-031-73007-8_26",
    "PosterVerse": "https://ojs.aaai.org/index.php/AAAI/article/view/37656",
    "Qwen-Image-Layered": "https://openaccess.thecvf.com/content/CVPR2026/html/Yin_Qwen-Image-Layered_Towards_Inherent_Editability_via_Layer_Decomposition_CVPR_2026_paper.html",
    "RefAdGen": "https://ojs.aaai.org/index.php/AAAI/article/view/37307",
    "SIMPLEPOSTER": "https://openaccess.thecvf.com/content/CVPR2026/html/Cui_SIMPLEPOSTER_A_SIMPLE_BASELINE_FOR_PRODUCT_POSTER_GENERATION_CVPR_2026_paper.html",
    "SciPostLayout": "https://bmvc2024.org/proceedings/28/",
    "SlideTailor": "https://ojs.aaai.org/index.php/AAAI/article/view/40758",
    "TAUE": "https://openaccess.thecvf.com/content/CVPR2026F/html/Nagai_TAUE_Training-free_Noise_Transplant_and_Cultivation_Diffusion_Model_CVPRF_2026_paper.html",
    "TextDiffuser": "https://proceedings.neurips.cc/paper_files/paper/2023/hash/1df4afb0b4ebf492a41218ce16b6d8df-Abstract-Conference.html",
    "TextDiffuser-2": "https://doi.org/10.1007/978-3-031-72652-1_23",
    "TextLap": "https://aclanthology.org/2024.findings-emnlp.833/",
    "Towards Reliable Advertising Image Generation Using Human Feedback": "https://doi.org/10.1007/978-3-031-72661-3_23",
}

ARXIV_OVERRIDES: dict[str, str] = {
    "AutoFigure-Edit": "https://arxiv.org/abs/2603.06674",
    "CAL-RAG": "https://arxiv.org/abs/2506.21934",
    "Design First Code Later": "https://arxiv.org/abs/2605.26451",
    "FreeText": "https://arxiv.org/abs/2601.00535",
    "Graphist": "https://arxiv.org/abs/2404.14368",
    "LaDe: Unified Multi-Layered Graphic Media Generation and Decomposition": "https://arxiv.org/abs/2603.17965",
    "LayoutGAN": "https://arxiv.org/abs/1901.06767",
    "Mirror in the Model: Ad Banner Image Generation via Reflective Multi-LLM and Multi-modal Agents": "https://arxiv.org/abs/2507.03326",
    "PaperBanana": "https://arxiv.org/abs/2601.23265",
    "ReContraster": "https://arxiv.org/abs/2604.10442",
    "T-Stars-Poster": "https://arxiv.org/abs/2501.14316",
}


def is_arxiv_url(value: str) -> bool:
    parsed = urlparse(value)
    return (
        parsed.scheme == "https"
        and (parsed.hostname or "").casefold() == "arxiv.org"
        and parsed.path.startswith("/abs/")
    )


def is_arxiv_doi(value: str) -> bool:
    parsed = urlparse(value)
    return (
        parsed.scheme == "https"
        and (parsed.hostname or "").casefold() == "doi.org"
        and parsed.path.lstrip("/").casefold().startswith("10.48550/arxiv.")
    )


def arxiv_id(value: str) -> str:
    if is_arxiv_url(value):
        return urlparse(value).path.removeprefix("/abs/").split("v", 1)[0]
    if is_arxiv_doi(value):
        doi = urlparse(value).path.lstrip("/")
        return doi.casefold().split("10.48550/arxiv.", 1)[1]
    raise ValueError(value)


def canonical_arxiv(value: str) -> str:
    return f"https://arxiv.org/abs/{arxiv_id(value)}"


def main() -> int:
    with RESOURCE_PATH.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise SystemExit("resources.csv has no header")
        fieldnames = list(reader.fieldnames)
        rows = list(reader)

    if "arxiv_url" not in fieldnames:
        fieldnames.insert(fieldnames.index("url") + 1, "arxiv_url")
        for row in rows:
            row["arxiv_url"] = ""

    for row in rows:
        row["arxiv_url"] = (row.get("arxiv_url") or "").strip()
        if row.get("section") != "Papers":
            row["arxiv_url"] = ""
            continue

        name = row["name"]
        primary = row["url"].strip()
        primary_is_preprint = is_arxiv_url(primary) or is_arxiv_doi(primary)

        if primary_is_preprint:
            arxiv = row["arxiv_url"] or canonical_arxiv(primary)
            if name in PUBLICATION_OVERRIDES:
                row["url"] = PUBLICATION_OVERRIDES[name]
                row["arxiv_url"] = arxiv
            else:
                # A venue label may precede proceedings publication. Until an
                # authoritative publication page is verified, use direct arXiv
                # as the primary link rather than the arXiv DOI surrogate.
                row["url"] = arxiv
                row["arxiv_url"] = ""
            continue

        if row.get("arxiv_date") and not row["arxiv_url"] and name in ARXIV_OVERRIDES:
            row["arxiv_url"] = ARXIV_OVERRIDES[name]

    with RESOURCE_PATH.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
