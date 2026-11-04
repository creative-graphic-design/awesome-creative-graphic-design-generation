# acro coverage audit — 2026-11-04

This revision expands the central CTAN **acro v3.8** registry and links plain-text mentions in the survey manuscript to their real usage pages.

## Registry counts

| Tag | Entries | First-use behavior | Source attribution |
|---|---:|---|---|
| abbreviations | 23 | Full term on first use, short form later | General standard terms |
| systems | 145 | Published short name only | Each entry has an original BibTeX `cite` key |
| evaluation | 17 | Published resource short name only | Each entry has an original BibTeX `cite` key |
| **Total** | **185** | | |

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

## Appearance-page completion

The current manuscript source references **all 175 registered keys** at least once with an `acro` command, including the general `GAN` abbreviation. This is a **syntactic occurrence audit**, not evidence that all 168 named resources received a full experiment review. The generated PDF's page-number list remains the visual authority for the appearance index.

## All-metadata preview before pruning (2026-11-04)

Following author feedback, the PDF displays **all 175 `acro` records** rather than selecting a subset. The original `cite` field retains first-use provenance; an additional `source = {\\citep{...}}` field renders the same source directly in the list. We added a `survey-rich` list template to display every currently available name, explanation, reference year, venue, original citation, clickable paper URL, DOI link and occurrence page. Generic abbreviations do not inherit fabricated source citations.

Of the 146 named-system/evaluation entries, the bibliography provides **146** paper URLs, **146** reference years, **81** venues, and **19** DOI strings. Missing venue/DOI means the current BibTeX does not contain that value, **not** that no venue/DOI exists. The template defines optional `task` and `representation` properties but leaves them unset until individual evidence is audited; they will be displayed when available. A new `check_manuscript.py` gate verifies each displayed metadata field against its exact BibTeX record.

The extensive PDF list is a **working review artifact**, and it should be shortened or moved to supplementary materials only after inspecting the complete rendered output.

## Current checkpoint after source reconciliation (2026-11-04)

The complete PDF index now covers **175** entries: **23 abbreviations, 136 named systems, 16 evaluation resources**. The 6 new systems are NeuralSVG, IGD, OmniSVG, LayerFusion, Revision Matters, and Draw with Thought. Each received original paper metadata and a manuscript use. The total manuscript bibliography is **186**, not the previous 180. All six are recorded as abstract/proceedings-verified rather than methods/results-verified. The preceding 168-entry counts are the earlier glossary checkpoint, not the current source-of-truth.

## New source-grounded model/index entries (2026-11-04)

The prior registry contained 175 TeX definitions, including 23 abbreviations.
I added nine named systems and one diagram benchmark for a total of **185 entries**: 23 abbreviations, 145 systems and 17 evaluation resources.
Every new named entry includes its source citation, BibTeX year and paper URL, plus venue/DOI only where identified by the publisher.
A personalized e-commerce banner study without a stable named-system short form is cited directly rather than adding a fabricated acronym.

## Source-grounded T01 entry (2026-11-04)

Added TAUE as a source-linked system: its original 2026 CVPR Findings citation, year, original paper link, task (layer-wise image generation), and output representation (foreground, background and composite image layers) appear in the exhaustive acro index. This makes **186 registered terms**; no generic metric was recast as a model name.
