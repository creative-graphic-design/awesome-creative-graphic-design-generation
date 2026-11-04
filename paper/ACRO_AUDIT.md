# acro coverage audit — 2026-11-04

This revision expands the central CTAN **acro v3.8** registry and links plain-text mentions in the survey manuscript to their real usage pages.

## Registry counts

| Tag | Entries | First-use behavior | Source attribution |
|---|---:|---|---|
| abbreviations | 22 | Full term on first use, short form later | General standard terms |
| systems | 130 | Published short name only | Each entry has an original BibTeX `cite` key |
| evaluation | 16 | Published resource short name only | Each entry has an original BibTeX `cite` key |
| **Total** | **168** | | |

The 61 newly registered generation/editing systems span layout, posters, typography, SVG, layers, slides and scientific figures. The 15 added evaluation entries encompass SVGEditBench, VectorGym, GraphicDesignBench, BizGenEval, AesEval-Bench, MPTc-Bench, DesignProbe, SridBench, SciFlow-Bench, LTSim, Design-o-meter, DesignSense, Rico, PubLayNet and DocLayNet. Existing PPTArena is moved into the evaluation group; it is **not a new bibliography item**.

## Conversion and guarding against misleading provenance

The original 70 named-system entries were retained (except PPTArena's category) and all new resources resolve to **existing entries** in the 180-item manuscript bibliography; no papers were fabricated or inserted merely to fill an acronym list. Entries are categorized by output role, not by authors' preferred marketing terminology. Named system descriptive long fields are **explanations**, not purported official expansions, so `first-style=short` is essential.

The revision uses `\\ac{key}` in manuscript prose and relies on `cite/cmd=\\citep`, `cite/display=first` and `pages/display=all` for source citation and appearance pages. Some entries have no occurrence page when they exist in the registry but are not referred to in running prose (including entries that occur only in a standalone figure). `list/display=all` is intentional and must **not** be misread as proof every item is fully analyzed.

A dedicated CI gate in `check_manuscript.py` now validates all three lists, resource categories, source keys and abbreviation definitions. The source checks guarantee resolution and formatting, not exact scientific findings, publishers' first-public dates, or the actual outcome of a system's empirical evaluation.

## Ambiguous names and output-mode caveats

Do **not** introduce a single conflated acro entry for both `LayoutDiffusion` references: the graphic-layout diffusion work and the layout-to-image diffusion work are unrelated research records. Likewise, `ReLayout` appears in both content-aware layout generation and structure-preserving editing. The paper retains descriptive bibliographic mentions for these boundaries rather than allowing one short model name to auto-cite the wrong study.

This is a language and provenance overhaul, **not** an increase in unique cited research: the 180-paper bibliography and the two existing research-map population counts remain unchanged.

## Distinct original models with similar names

The source audit found that `LayoutGAN` (2019) is **not** the same work as `Attribute-conditioned Layout GAN` (2020), which conditions element geometry on attributes ([IEEE TVCG source](https://ieeexplore.ieee.org/abstract/document/9106863)). We therefore use distinct `layoutgan` and `aclayoutgan` entries and BibTeX keys. Likewise, `PDA-GAN` is a named pixel-discriminator layout-domain-adaptation model ([CVPR 2023](https://openaccess.thecvf.com/content/CVPR2023/html/Xu_Unsupervised_Domain_Adaption_With_Pixel-Level_Discriminator_for_Image-Aware_Layout_Generation_CVPR_2023_paper.html)), not an arbitrary combination of a `PDA-` prefix and the general `GAN` abbreviation. Both are source-linked, and neither has been counted as a new paper.
