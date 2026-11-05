# acro coverage audit — initiated 2026-11-04

**Latest PDF-verified checkpoint T05 (2026-11-05):** **194** entries (26 abbreviations, 150 systems, 18 evaluation). I inspected UniWorld-Design's actual source-linked index record on **p. 22** of the 30-page manuscript from [Paper PDF #41989947985](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/runs/41989947985), including usage pp. 7, 11 and 13.

**Latest PDF-verified checkpoint (T04, 2026-11-05):** **193** registry entries (26 abbreviations, 149 systems, 18 evaluation resources). The older tables and dated sections below document *historical* checkpoints rather than today's totals. The T03 original source commit passed [Paper PDF #41871516836](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/runs/41871516836); I checked the real 29-page output's Alfie entry on p. 17, including its first-use pages, source citation, year, venue, paper link and DOI.

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

Added TAUE as a source-linked system: its original 2026 CVPR Findings citation, year, original paper link, task (layer-wise image generation), and output representation (foreground, background and composite image layers) appear in the exhaustive acro index. This makes **188 registered terms**; no generic metric was recast as a model name.

## Two standard metrics after CI detection

The manuscript check identified missing acro keys for SSIM and LPIPS when citing the TAUE evaluation. Both have now been added as general technical abbreviations, not new research methods or new bibliography entries. Full index: **188** records = 25 general abbreviations, 146 systems, 17 evaluation resources. The PDF display remains subject to the new source-commit build.

## T02 TKG-DM source-linked metadata (2026-11-05)

Added `tkgdm` with CVPR 2025 citation, DOI, paper link, source-grounded task and **keyed RGB** (not native layer hierarchy) representation. The full index now comprises **189 entries: 25 abbreviations, 147 systems, 17 evaluation resources**. Its original experimental distinctions are audited in `T02_TKGDM_SOURCE_AUDIT.md`.

## T03 Alfie source-linked index entry (2026-11-05)

I added `alfie` to the **systems** tag with original `alfie2025` bibliography source, an arXiv 2024 eprint, Springer LNCS 2025 venue, DOI, explicit task and single-RGBA-foreground representation.
The full index comprises **190 entries: 25 abbreviations, 148 named systems, 17 evaluation resources**.
I inspected its actual printed entry on manuscript **p. 17**, including rendered citation `[128]`, `2025` venue, paper/DOI links and the occurrence-page references.
The same source commit passed Paper PDF / Catalog Check / Awesome Lint; no acro warning was reported in the final TeX log.

## T04 KID / LayeringDiff / FG-mIoU index verification (2026-11-05)

I added KID as a general abbreviation, LayeringDiff as a source-cited named system, and its original FG-mIoU as a source-cited evaluation resource.
The current index contains **193** entries (26 abbreviations, 149 systems, 18 evaluation resources).
I inspected the actual 30-page PDF from [Paper PDF #41944766288](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/runs/41944766288): KID on **p. 17**, LayeringDiff on **p. 19**, FG-mIoU on **p. 22**, bibliography on **p. 25**, with source links and appearance pages.
No acro warning was present in its compiled log; the older historical 190-entry checkpoint above refers to T03.

## T05 source-linked system

I added **UniWorld-Design** with the original arXiv 2026 BibTeX key, source citation, year, task and the correct ordered RGBA-raster-stack output instead of an unsupported PSD-export claim.
The resulting 194-entry list was compiled and I inspected UniWorld-Design on p. 22, including the original source and appearance-page references, in artifact **13398466465**. No acro warnings were found in the final log.
