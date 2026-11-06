# acro coverage audit — initiated 2026-11-04

**Latest compact-index visual acceptance (2026-11-05):** `0dbe879` passed [Paper PDF #42033969385](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/runs/42033969385), Catalog Check and Awesome Lint. I downloaded exact artifact **13417988514** and visually compared real index pp. **18, 22, 24** side by side with the previously ragged-right-only PDF. The redundant Task/Representation paragraphs no longer cause multi-line wraps; all **198** registered entries and source-linked bibliography metadata are kept. The compiled review PDF remains **31 pages**, with **0** off-page text-word boxes and no unresolved citation/acro or TeX box warnings.

**Latest PDF-verified T06 checkpoint (2026-11-05): 198 entries** (27 abbreviations, 151 systems, 20 evaluation resources). I visually inspected SGSD on **p. 18**, the PosterText system entry on **p. 22**, and PosterText-320K / PosterText-Bench on **p. 24** of the actual **31-page** anonymous manuscript from successful [Paper PDF #41997058915](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/runs/41997058915), artifact **13401199657**.

**Latest PDF-verified checkpoint T05 (2026-11-05):** **194** entries (26 abbreviations, 150 systems, 18 evaluation). I inspected UniWorld-Design's actual source-linked index record on **p. 22** of the 30-page manuscript from [Paper PDF #41989947985](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/runs/41989947985), including usage pp. 7, 11 and 13.

**Latest PDF-verified checkpoint (T04, 2026-11-05):** **193** registry entries (26 abbreviations, 149 systems, 18 evaluation resources). The older tables and dated sections below document *historical* checkpoints rather than today's totals. The T03 original source commit passed [Paper PDF #41871516836](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/runs/41871516836); I checked the real 29-page output's Alfie entry on p. 17, including its first-use pages, source citation, year, venue, paper link and DOI.

This revision expands the central CTAN **acro v3.8** registry and links plain-text mentions in the survey manuscript to their real usage pages.

## Historical 2026-11-04 registry baseline (not the current 198-entry total)

The table below captures the original expansion to **185 entries**. The **current** total is **198** (27 abbreviations / 151 systems / 20 evaluation resources), as validated and PDF-inspected in the latest checkpoint above. Keep the dated early snapshot for traceability.

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

At the historical 175-key checkpoint, the manuscript source referenced **all 175 registered keys** at least once with an `acro` command, including the general `GAN` abbreviation. This is a **syntactic occurrence audit**, not evidence that all 168 named resources received a full experiment review. The generated PDF's page-number list remains the visual authority for the appearance index.

## All-metadata preview before pruning (2026-11-04)

Following author feedback, the PDF displays **all 175 `acro` records** rather than selecting a subset. The original `cite` field retains first-use provenance; an additional `source = {\\citep{...}}` field renders the same source directly in the list. We added a `survey-rich` list template to display every currently available name, explanation, reference year, venue, original citation, clickable paper URL, DOI link and occurrence page. Generic abbreviations do not inherit fabricated source citations.

Of the 146 named-system/evaluation entries, the bibliography provides **146** paper URLs, **146** reference years, **81** venues, and **19** DOI strings. Missing venue/DOI means the current BibTeX does not contain that value, **not** that no venue/DOI exists. The template defines optional `task` and `representation` properties but leaves them unset until individual evidence is audited; they will be displayed when available. A new `check_manuscript.py` gate verifies each displayed metadata field against its exact BibTeX record.

The extensive PDF list is a **working review artifact**, and it should be shortened or moved to supplementary materials only after inspecting the complete rendered output.

## Current checkpoint after source reconciliation (2026-11-04)

At the earlier 2026-11-04 checkpoint, the PDF index covered **175** entries: **23 abbreviations, 136 named systems, 16 evaluation resources**. The 6 new systems are NeuralSVG, IGD, OmniSVG, LayerFusion, Revision Matters, and Draw with Thought. Each received original paper metadata and a manuscript use. The total manuscript bibliography is **186**, not the previous 180. All six are recorded as abstract/proceedings-verified rather than methods/results-verified. The preceding 168-entry counts are the earlier glossary checkpoint, not the current source-of-truth.

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

## T06 PosterText source-linked index additions (2026-11-05)

I added **PosterText** to `systems`, **PosterText-Bench** and **PosterText-320K** to `evaluation`, and **SGSD** to `abbreviations`, with original `postertext2026` attribution and evidence-bounded artifact descriptions.
The complete source-linked 198-entry index (27/151/20) has now been **visually inspected in the actual 31-page PDF**: PosterText pp. 7, 10, 14 listed on p. 22; PosterText-320K pp. 10, 15 and PosterText-Bench pp. 14 f. listed on p. 24; SGSD occurrence p. 10 listed on p. 18. I found no citation/acro or TeX box warnings and no obvious index overflow in the inspected pages.

## Acro index line-wrapping fix (2026-11-05)

I inspected the prior actual T06 rendered index (including pp. **18, 22, 24**) and identified the source of odd breaks: `survey-rich` used full-justified `description` items with paragraph hyphenation, followed by densely concatenated optional metadata on two-column lines.
I updated **only the index template and its mechanical validator**, keeping all 198 entries, `paperurl`/DOI/source metadata, displayed task/representation and page references.
The template now uses `\\raggedright`, `\\hyphenpenalty=10000`, `\\exhyphenpenalty=10000` and `\\itemsep=.45\\baselineskip`; a standalone `acro` LaTeX specimen compiled and rendered successfully.
**The full-paper PDF after this change still requires actual source-commit CI and visual inspection**; standalone proof is not publication-quality acceptance.

## Acro wrapping follow-up: rich metadata versus readable print index (2026-11-05)

My direct comparison of the compiled full T06 PDF and ragged-right-only [Paper PDF #42025690265](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/runs/42025690265) **pp. 22 and 24** showed that the initial fix improved justification but left long *Task* and *Representation* annotations unnaturally wrapped.
I therefore redesigned the **printed** `survey-rich` index as a compact bibliographic listing: `short`, `list`, optional `extra`, `refyear`, `venue`, `source`, `paperurl`, `doi`, and `acropages`.
I preserved the custom `task`/`representation` property declarations and all 198 source-linked records in `acronyms.tex`; these fields are not discarded and can be described more readably in technical prose/tables.
A standalone full-width/two-column `acro` proof with four representative long entries compiled and rendered successfully. **I subsequently verified the actual full manuscript PDF** in [Paper PDF #42033969385](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/runs/42033969385), artifact **13417988514**: 31 pages; visual side-by-side index comparison pp. 18/22/24; PosterText/PosterText-320K/PosterText-Bench source citations, links and usage pages retained; list-to-References transition readable; no out-of-page text words or undefined citation/acro/TeX box warnings. Scientific author approval remains separate.

## Eight-page index visual review and section-heading correction (2026-11-05)

I separately rendered and inspected the entire **pp. 17–24** of the actual compact T06 PDF (artifact **13417988514**), not only PosterText examples.
In addition to verifying the compact references on pp. 22/24, I found the **evaluation-group heading** on p. **23** hyphenated as `Re-` / `sources`.
I shortened the LaTeX heading from `Benchmarks, Datasets, and Evaluation Resources` to **`Evaluation Resources`** and added an exact heading invariant to `paper/scripts/check_manuscript.py`.
This is a **pure heading/layout correction**; no acronym identity, tag, source or citation metadata changed. **Pending** source-commit PDF CI and visual check of the new p. 23 heading.

## Critical PDF hyperlink target audit (2026-11-05)

After checking all printed index pages, I inspected **actual PDF link action dictionaries**, not only colored `paper` and `DOI` labels.
In the previous successful **31-page** PDF, named-resource `paper` links were malformed `GoToR` file actions targeting an escaped `\\acroprintfield` expression; DOI URI actions literally contained `https://doi.org/\\acrowrite {doi}`.
These links were **broken** despite the earlier visual pass and successful CI; I retract the prior statement that their targets were verified.
The cause is passing nonexpandable `\\acrowrite` to `\\href`.
I replaced it with `\\ExpandArgs{e}\\acrofield{\\AcronymID}{paperurl}` and equivalent DOI target expansion; a **compiled local `acro` specimen** generated working arXiv/DOI PDF link URIs.
I added `paper/scripts/check_acro_pdf_links.py`, five local negative/positive unit tests, and a source-build CI step that checks **all 171 indexed paper links + 25 DOI links** (count and repeated-target multiplicity) using `pdfinfo -url`, storing `pdf-links.txt` in the workflow artifact.
**Full manuscript PDF link and layout acceptance remains pending** until the updated Actions artifact is retrieved and its actual PDF URI annotations inspected.

## Inconsistent name/description spacing: root cause and structural remedy (2026-11-06)

I rendered the actual current **31-page** PR PDF and inspected full-resolution screenshots of the `acro` index, especially **p. 19**. Contrary to earlier “fixed” reports, the old `\\begin{description}` + `\\item[\\acrowrite{short}]` still rendered different-sized name labels whose following descriptions started after the label, while wrapped description lines started at a **fixed** paragraph indentation. This was the visible misalignment the earlier `\\raggedright` and shortened-annotation changes did not correct.
I reproduced and contrasted the behavior in a standalone **two-column** `acro` PDF with eight representative entries and the exact metadata and expandable paper/DOI hyperlink mechanisms. I replaced `description` with `list` using zero list/label/item margins; **short names print inline as nonbreaking bold text** and a consistent `\\enspace` separates description text. A 1 em hanging offset applies only to the small-font source-metadata line. I added a source validator regression guard and preserved all 198 registered terms, source/year/venue/URL/DOI and occurrence pages. **Actual revised full-manuscript PDF acceptance is still pending** until this exact source-commit CI artifact has been inspected.

## Default template reset requested by author (2026-11-06)

The author explicitly requested **simple stock `acro` functionality**, not an ever-more-intricate custom glossary renderer. I had over-engineered `survey-rich`, causing a sequence of alignment/spacing and broken hyperlink defects. I verified the **stock** `\\printacronyms[include=systems,heading=none,display=all]` in a real two-column LaTeX/PDF example before changing the manuscript.
I now removed `survey-rich` as a print template and use the built-in `acro` formatter for all three lists. The 198 source-linked definitions and all custom paper/DOI/year/venue/task/representation **data values remain stored**, with their nonstandard property declarations relocated to `acronyms.tex`. The original BibTeX and first-use citation logic remain unchanged.
Because the default list does not include our hand-added `paper`/DOI hyperlink labels, I removed the associated count-specific PDF CI assertion. Prior full index hyperlink claims apply to the superseded renderer, not this stock list. **The latest full manuscript was subsequently source-build verified:** [Paper PDF #42062616167](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/runs/42062616167), downloaded artifact **13433601126**, **28-page** anonymous PDF. I rendered and examined pp. 17–22 (all three default-print lists and their transition into the bibliography), including the formerly misaligned pp. 19–20; the variable-width `description` labels are gone. The log has no undefined citation, `acro` or TeX box warnings; no out-of-page text words; **0 PDF URI annotations**, which is the expected non-hyperlinked behavior of the stock list. Full scientific author review is still open. The obsolete custom template, link-validator script and print-only tests were deleted after this verification.
