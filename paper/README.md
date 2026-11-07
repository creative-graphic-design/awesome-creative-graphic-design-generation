# Graphic-design generation survey (working draft)

This directory contains an initial **research-survey manuscript**, not a submitted CVPR paper. The taxonomy, references, screening criteria, and claims must be reviewed before publication.

## Latest acro typography correction — compiled and inspected (2026-11-05)

I corrected the printed two-column `acro` index after comparing the actual previous full-paper PDFs and finding that ragged-right text alone still left verbose Task/Representation annotations wrapped across narrow columns.
The print template now displays name/description, reference year, venue, original citation, paper/DOI links and manuscript occurrence pages; **Task** and **Representation** remain stored in all 198 source-linked registry entries, not printed in the compact index.
The source change `0dbe879` passed [Paper PDF #42033969385](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/runs/42033969385), Catalog Check and Awesome Lint; I retrieved artifact **13417988514**, inspected the real **31-page** PDF at index pp. **18, 22, 24** and the bibliography transition, and verified zero out-of-page text boxes or unresolved citation/acro/TeX box warnings.
This is typesetting QA, **not** author scientific approval of T04–T06 or a primary-source verification of PosterText v3.

## Latest source-stage checkpoint — T06 / PosterText (2026-11-05)

I reviewed [PosterText original arXiv v2 §§3–4/Tables 1–2](https://arxiv.org/html/2608.16289v2), inspected current arXiv v3 version metadata and re-read the private live 225-study workbook.
PosterText quantitatively measures text-patch addition, deletion and modification **on raster poster images** with OCR fidelity, protected-region masked LPIPS and VLM scores; the HTML patch structure is in the **dataset construction pipeline** rather than the exported model result.
The [T06 evidence audit](T06_POSTERTEXT_SOURCE_AUDIT.md) preserves lower text accuracy on modification and lower visual quality on some tasks compared with closed-source baselines.
**Source-stage tally: 225 IDs / 202 references / 198 acro / 173 linked / 52 unresolved (2 P1, 13 P2, 37 P3), public 156/207 linked / 51 pending.**
I downloaded and visually reviewed the **31-page anonymous T06 manuscript** and both standalone maps from successful [Paper PDF #41997058915](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/runs/41997058915), artifact **13401199657**; see [T06 audit](T06_POSTERTEXT_SOURCE_AUDIT.md) for checked pages, the source-linked index and QA limitations. Catalog Check and Awesome Lint also passed. **T04/T05/T06 scientific sign-off and v3 primary-source numerical reconciliation remain pending.**


## Historical single-study source checkpoint — T05 / UniWorld-Design (2026-11-05)

I re-read the [original source](https://arxiv.org/html/2608.03971) and live evidence workbook before adding CGD-184; see [T05 source audit](T05_UNIWORLD_DESIGN_SOURCE_AUDIT.md).
UniWorld-Design trains on PSD-authored semantic layers but **outputs complete compositable RGBA raster assets and stacks, not an exported native PSD document**.
I distinguish I2L layer recovery on 512 Crello designs from T2RGBA generation on 512 prompts and record worse alpha cleanliness and FID counterexamples.
**Source stage:** 225 register IDs / 201 cited references / 194 acro / 172 linked / 53 unresolved (3 P1/13 P2/37 P3); public 155/207 linked / 52 pending.
I downloaded and inspected the actual **30-page** anonymous manuscript and both standalone maps from [Paper PDF #41989947985](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/runs/41989947985), artifact **13398466465**. All three CI checks passed for source `fb1f41e`; see the [T05 audit](T05_UNIWORLD_DESIGN_SOURCE_AUDIT.md) for inspected pages and limits. **Scientific author review of T04/T05 remains pending.**


## Historical single-study checkpoint — T04 / LayeringDiff (2026-11-05)

I inspected [LayeringDiff's original methods/results](https://arxiv.org/html/2501.01197), §§3–5 and Tables 1–4 after re-reading the native 225-study evidence workbook.
The first composite uses a fixed pretrained generator, but FBDD/HFA are trained on **20,000 synthetic composites**; the entire method is not training-free.
Its foreground and background raster layers support compositing and sequential decomposition; FID/KID/CLIP, detector-derived FG-mIoU, a 24-person preference study and reconstruction metrics do not evaluate held-out semantic edit instructions.
**Historical T04 checkpoint: 225 working IDs / 200 BibTeX / 193 acro entries / 171 linked / 54 unresolved (4 P1 / 13 P2 / 37 P3)**.
See [T04 source audit](T04_LAYERINGDIFF_SOURCE_AUDIT.md). I verified the actual **30-page** anonymous PDF, source-linked `acro` entries, bibliography and both maps from [Paper PDF #41944766288](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/runs/41944766288), with all three CI checks successful. Author scientific review of T04 remains pending; the next T05 audit is not automatic scientific approval.

## Historical single-study checkpoint — T03 / Alfie (2026-11-05)

I compared the live 225-study workbook with Alfie's original Sections 4–5.1, Table 1 and Figures 3/5–7 and the Springer publication record.
Alfie delivers a compositable single RGBA foreground image; cropping proxies and matting preference do not measure post-export design edits.
The 2024 workshop/arXiv and the published 2025 LNCS chapter refer to one study.
The historical T03 audited coverage was **225 working IDs, 199 references, 190 acro entries, 170 linked and 55 unresolved (5 P1 / 13 P2 / 37 P3)**.
See [T03 source audit](T03_ALFIE_SOURCE_AUDIT.md) for evidence and limitations. **Paper PDF #41871516836, Catalog Check and Awesome Lint succeeded for the T03 source commit;** I downloaded the actual **29-page anonymous PDF** and inspected the Alfie body, citation/acro index, bibliography and two standalone map PDFs. **Author scientific review remains open** before T04.
Earlier totals below are historical checkpoints.

## Historical T02 checkpoint and task-by-task work queue

The earlier T02 single-study primary-source audit covered **CGD-092 / TKG-DM** ([original experiment review](T02_TKGDM_SOURCE_AUDIT.md)): **198 references, 189 acro terms, 169 linked and 56 unresolved studies**. The original §3–7 and Table 1 show chroma-key RGB generation is not native document editing, while SDXL comparisons do not support unconditional superiority over LayerDiffuse. Author review remains pending before T03.

See **[TODO.md](TODO.md)** for the next single research-study review, required evidence, acceptance gates and actual PDF checks. Initial verified baseline (2026-11-04, before T01–T06): **225** study IDs, **196** references, **185** acro entries, **167** matched and **58** unresolved (**8 P1, 13 P2, 37 P3**). Historical counts in sections below are earlier checkpoints, not current totals. Do not process all unresolved studies as one bulk citation operation.

## Historical citation coverage and source gates — 2026-11-04

I reconciled three previously cited paper identities across publication/arXiv versions (DesignAsCode, GlyphDraw2, BizGen) and added six independently source-checked references (NeuralSVG, IGD, OmniSVG, LayerFusion, Revision Matters, Draw with Thought). At this historical 2026-11-04 checkpoint, the paper contained **186 bibliography entries**, **175 registered acro terms**, and the 225-study workbook crosswalk matched **157 studies**, with **68 pending** identity/coverage review. Those 68 are not excluded studies; the six new references have original abstract/proceedings checks but no newly completed quantitative methods/results audit. The dated source manifest in `evidence_register_snapshot_manifest.json` and `check_evidence_register.py` reject a snapshot older than 30 days; they do not supply live access to the private Google Sheet.

## Compile and read

From this directory, with TeX Live, latexmk, and BibTeX installed:

    make pdf

The local output is `paper/main.pdf`. The CI workflow `.github/workflows/paper-pdf.yml` builds the manuscript when a PR or push changes `paper/**` (or when manually dispatched). In the GitHub **Actions → Paper PDF** run, download the **survey-paper-<commit>** artifact from the Artifacts section. It includes the PDF, first-page PNG, extracted text, and diagnostic log. The manuscript and figure PDFs are generated and uploaded in CI artifacts, not committed to Git.

## Official template

- CVPR/ICCV/3DV author kit: https://github.com/cvpr-org/author-kit
- CVPR2027-v1 pinned upstream commit: `a2369342011145be8c85e5ad21a9b61f9fa53473`
- Vendored, unmodified: `cvpr.sty` and `ieeenat_fullname.bst`. The original headers and license notices remain attached to those files.
- `main.tex` uses the official review mode, which hides the sample author block and renders **Anonymous CVPR submission**. Update dummy fields only for the final version.

## Historical initial evidence spreadsheet reconciliation (2026-11-04)

Before updating the literature, consult the actual [Google Sheet evidence register](https://docs.google.com/spreadsheets/d/1PJtvX34FYoOnF8LS4-0WHpiR3B_KQ6n5fqRBtTeF3Zc/edit), particularly Evidence Matrix 225, 225 Citation and R-E-V Coverage, Prior Survey and Screening, and 225 Source Tier Reconciliation. At this initial 2026-11-04 reconciliation checkpoint, we compared the 225 stable study IDs to **180 then-cited BibTeX works**: 148 uniquely matched and 77 unresolved. Frozen source metadata and decisions are in evidence_register_225_snapshot.csv and evidence_register_225_crosswalk.csv. The 148 linked citation-audit rows now contain their exact CGD IDs. Run scripts/check_evidence_register.py before any manuscript citation change; the pre-commit hook and Paper PDF CI enforce it. See EVIDENCE_REGISTER_RECONCILIATION.md for source refresh and limitations. CI is NOT connected to the private live spreadsheet: this gate detects drift from the committed snapshot, not unseen changes in Google Drive.

## Research evidence status (2026-11-03)

The public repository catalog and the broader research evidence register are *different snapshots*. At the **historical 2026-11-03 workbook checkpoint**, the working register held 225 provisional entries, with 88 labelled as methods/results-reviewed, 28 abstract/publication-record reviewed, and 109 catalogue-only. Those source-depth tags belong to the workbook snapshot and must not be automatically propagated to citation-level audit rows. The existing public README currently counts fewer papers. Do not describe all 225 as full-text assessed or as PRISMA-complete. The present paper emphasizes a representation–editability–evaluation crosswalk rather than a benchmark leaderboard.

Citation keys in `references.bib` are traceable to source URLs. I expanded `literature_citation_audit.csv` to 180 citation-level records: 144 still `not_verified` by individual source key and 36 newly added references whose original author/title/abstract records were checked (`abstract_index`), without claiming methods/results verification. The aggregate historical 88/28/109 source-depth figures cannot be assigned to those citations without identity matching. The audit is checked by `scripts/check_literature_audit.py` in pre-commit and CI. Bibliographic authors missing from provisional entries must be verified from publisher/proceedings sources instead of being guessed. Survey completion also requires a reproducible retrieval log, screening flow, deduplication, adjudicated scope boundaries, and full-text checks for eight remaining narrative papers.

## Writing and audit invariants

- Distinguish representation affordance, qualitative edit demonstration, human editing efficiency, and measured edit-instruction execution.
- Do not equate raster creation-time conditioning with post-export editing, or SVG/PSD/DOM export with quantitative editing success.
- FID, CLIP similarity, Chamfer reconstruction, and layout IoU are not editing performance metrics by themselves.
- Keep catalog changes in canonical data CSVs; do not manually modify the root README, which is generated.

## Related-survey and figure design notes

Seven prior surveys were compared in `sections/related_surveys.tex`: Huang (2023), Shi (2023), Liu (2024), Tian and G\u00fcnther (2024), Li et al. (2024), Zou et al. (2025), and Malashenko et al. (2025). Common figure roles are (1) overview/taxonomy, (2) survey discovery/counts, (3) specific research-line methods, and (4) synthesis/research challenges. This working draft adds two original **editable TikZ** figures: `figs/tex/overview.tex` (R–E–V crosswalk) and `figs/tex/edit_protocol.tex` (measured editing dimensions). We deliberately do not fabricate PRISMA exclusion counts or a publication-time histogram; those require a frozen and reconciled corpus. See the survey comparison table in the paper.

## Citation health checks

Run `python3 paper/scripts/check_bibliography.py` from the repository root (or `python3 scripts/check_bibliography.py` inside `paper/`) to validate citation resolution, required BibTeX fields, duplicate identifiers, placeholder authors and unused bibliography entries. CI executes the same script before TeX compilation. These checks test **structural consistency**, not the truth of author names, venues, empirical results or source selection. Source-level bibliographic verification remains an editorial responsibility.

### Review provenance and sample count
The Zou et al. (2025) paper describes a 500-item dataset in its methodology narrative and lists 267 reviewed papers in its earlier-survey comparison table. We document both numbers rather than silently choosing one. Tang et al. (2024) is a seven-designer interview study, included as practitioner context and explicitly distinguished from technical surveys.

## New evidence and benchmark comparison

I added a comparison section covering SVGEditBench, VectorGym, MiLDEdit, InfoEdit, MPTc-Bench, GraphicDesignBench, BizGenEval and AesEval-Bench. The paper now distinguishes protected objects from necessary dependent layout reflow rather than requiring every non-target pixel to remain fixed.

`REVIEW_PROTOCOL.md` is a **prospective protocol, not an executed search log**. It specifies database/query templates, screening and exclusion codes, source-depth labels, and requirements for eventual inclusion-flow figures. Do not present its planned searches as completed.

The bibliography contains newly verified benchmark primary-source records; older entries still require final title/author/DOI checks before publication.

## Source layout and writing-review gates

- `figs/tex/`: standalone TikZ figure sources and float wrappers with captions and labels.
- `figs/pdf/`: generated vector PDFs, created by `make figures` and included in CI artifacts.
- `tabs/tex/`: five independent TeX tables, included by their original narrative sections.
- Before every paper commit, read `WRITING_CHECKLIST.md`, run `python3 paper/scripts/check_manuscript.py` and `python3 paper/scripts/check_bibliography.py`, then run `cd paper && make pdf` and check the rendered PDF. Agent instructions are in `paper/AGENTS.md`. Local hooks can be installed by `uvx pre-commit install` at repository root; CI checks paper changes even when hooks are absent.

## Numbered sections, sentence diffs and historical research map

Manuscript sections follow `01_abstract.tex`, `02_introduction.tex`, through `10_conclusion.tex`. TeX prose uses **one sentence per physical source line** (blank lines separate paragraphs), making version-control diffs and PR reviews sentence-granular without changing rendered paragraph breaks. Use `\\citet{key}` when an author is part of a sentence; use `\\citep{key}` for a parenthetical citation, without manually repeating author names.

`figs/tex/research_map.tex` contains an original chronological, task-colored research map motivated by the SSII2024 overview shared for visual reference; `figs/tex/research_map_figure.tex` holds its caption and label. The map groups selected 2019–2026 studies and **does not assert direct causal or citation relationships**. The source is independently compilable; `make figures` generates `figs/pdf/research_map.pdf`.

The paper CI runs the same source-line checker as the pre-commit hook, plus its negative-fixture unit tests. The checker is an intentionally conservative static lint, not a guarantee of grammatical correctness or source verification.

## Historical exhaustive, source-linked acro index checkpoint (2026-11-04)

The earlier review PDF displayed **all 175 registered entries** in three lists, with an extended list template in `acro_list_template.tex`. Along with each name and description, the historical template showed every then-available original-work citation, BibTeX publication/reference year, conference or journal, paper hyperlink, DOI hyperlink, and the `acro` appearance pages. All **152** named systems/benchmarks have source citations, reference years, and paper links; the bibliography has venue information for **81** such entries and DOI fields for **19**. The other **22** entries are generic abbreviations, so paper-level citations are not invented. Optional task/representation fields are supported, but they are not populated until primary-source evidence justifies them. The historical index was deliberately exhaustive for review; the latest compact layout is documented at the top of this README, preserving all **198** declared terms and their citation/URL metadata while suppressing long Task/Representation annotations in the two-column print display. The original `cite` property still adds the first prose-use citation; a separate `source` property prints the citation in the list. The manuscript CI now checks these fields against `references.bib`.

## Illustrated narrative figure added to the manuscript (2026-11-04)

The manuscript contains an **original, editable 26-milestone research map** (`figs/tex/research_map_narrative.tex`) with research-task lanes, independent method-family border colors, annotated time periods, and four original output-format schematics. Its nodes, citation keys and reference years are tracked in `figs/tex/research_map_narrative_sources.csv` and checked in CI; the broader **67-paper atlas remains a separate second figure**. **T16 (2026-11-07, updated):** following the original-figure review, I removed the footer-style `Affiliation provenance` logo strip and moved the authentic marks **inside the individual study cards**, in identical square 0.46 cm slots. OpenCOLE uses CyberAgent's **CA symbol only**, retained as original vector paths clipped from its SHA-1-pinned source SVG (not the horizontal wordmark); COLE uses Peking University's original square seal. Both are **draft-only attributed identifiers**, not publication permissions or endorsements. The remaining BIT, Adobe and Microsoft Research Asia marks are not enabled. The workflow verifies upstream bytes, builds vector PDFs and rejects marks in an unrelated footer or unmatched study node; it does not claim trademark clearance. See `figs/assets/logos/README.md`, `figs/tex/logo_asset_candidates.csv` and `figs/tex/affiliation_logo_provenance.csv` for source/rights review and figure QA.

## Survey figure design review (2026-11-04)

`FIGURE_DESIGN_SURVEY.md` compares figures visually inspected in the Huang (2023), Zou (2025), Luo (2025) and Zhang (2026) surveys, with separately labelled publisher/author-summary observations for Shi (2023) and Tian & Günther (2024). It defines a richer diagram architecture inspired by the SSII2024 map without copying it. `figs/tex/affiliation_logo_provenance.csv` records paper-date institutional evidence; official visual logos have not yet been retrieved or cleared for publication. A standalone original TikZ **concept** was compiled locally for review, but the vetted 67-milestone map remains the current manuscript figure.

## Historical citation coverage checkpoint (2026-11-03)

At this earlier checkpoint, the manuscript bibliography contained **180 distinct references**, including 36 added from original abstract records across six graphic-design research lines. `catalog_citation_crosswalk.csv` reconciles these against 207 public catalogue papers, conservatively matching 138 and flagging 69 unmatched for further work. Those 69 are not screened exclusions; the separate provisional 225-study register is not yet joined to citation keys. See `LITERATURE_COVERAGE_AUDIT.md` and the `check_catalog_crosswalk.py` validator.

## Acronyms and named systems (CTAN acro)

The central registry is `paper/acronyms.tex`, using CTAN `acro` v3 instead of `glossaries`.
Genuine abbreviations expand on first use through `\ac{key}`; subsequent mentions display the short form.
Named model and system entries use `first-style=short` to preserve published names without fabricating expansions.
Three `\printacronyms` lists separate general abbreviations, named generation/editing systems, and benchmark/dataset/evaluation resources. **Current T06 count: 198 entries (27 abbreviations, 151 systems, 20 evaluation resources).** The initial 2026-11-03 registry had **22 abbreviations, 130 systems, and 16 evaluation resources**; these older figures are retained as a dated historical baseline, not presented as the current index. All named resources keep their original BibTeX `cite` keys. Plain-text model/benchmark names and technical abbreviations in manuscript prose were migrated to `\ac{...}` so their usage pages are actually recorded by `pages/display=all`; resource titles remain descriptions rather than invented long-form expansions.
The manuscript checker rejects missing or duplicate definitions and obsolete package commands; the PDF CI verifies LaTeX compilation.

The research map is a curated **six-track by four-era** matrix with **67 representative milestones**, not a citation graph or complete publication census.
Its year labels use the cited bibliography year (venue year when available, otherwise preprint year); they do not always equal the first public version date.
Its editable source is `figs/tex/research_map.tex` and its compiled vector output is `figs/pdf/research_map.pdf`.
The 67 figure labels are cross-referenced to actual BibTeX entries in `figs/tex/research_map_sources.csv`, checked in CI; see `RESEARCH_MAP_AUDIT.md` for date and selection caveats.

**All three** `\printacronyms` lists use `display=all`, so every declared abbreviation, named system, benchmark and dataset is included even if it has not yet appeared in the paper. PDF CI verifies representative entries and rejects an empty acronym-list warning.

## Historical P1 source triage and bibliography update (2026-11-04)

Ten previously unresolved P1 studies were source-identified from original author/publisher records and added with task-specific R--E--V analysis to the manuscript.
Reference total: **196**; acro total: **185** (the earlier documentation count of 174 was incorrect; the actual original file held 175).
The private 225-study register maps **167** identities to BibTeX and keeps **58** pending; the public 207-paper catalogue currently matches **150** and leaves **57** unmatched.
The new bibliography audits remain at abstract/index tier, not comprehensive methods/results.
See `P1_SOURCE_TRIAGE_20261104.md` and `evidence_review_queue.csv`.

## Latest decision — stock acro list rather than hand-built typography (2026-11-06)

Per the author's direct request, `main.tex` now prints the 3 `acro` groups using the **built-in default list template**. We removed the experimental `survey-rich` list and custom page-index typography. All **198 acronym definitions** and the original-source metadata fields remain intact in `acronyms.tex` and checked against `references.bib`; those custom metadata fields are **not rendered** in the stock printed list. Standard source citation behavior on first mention stays enabled. This change does **not** alter research content or the 225-study register.
I then verified the exact full-paper source build in successful [Paper PDF #42062616167](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/runs/42062616167), downloading artifact **13433601126** and inspecting the real **28-page** anonymous manuscript (index pp. 17–21 and references transition p. 21) and the two research-map PDF artifacts. No undefined citation, acro or TeX box warnings or out-of-page text words were found. The old custom template, print-only PDF URI checker and associated tests are removed. **The stock list provides short/long descriptions, not the custom year/venue/citation/URL/DOI/usage-page annotations**; those data remain registered and bibliography-backed. Scientific review still requires independent author approval.

## Default acro occurrence-page index (2026-11-06)

The manuscript now uses the **standard `acro` v3.8 page-index options**, not a custom list template: `pages/display=all` prints **all observed usage pages**, `pages/name=true` prefixes `p.` or `pp.`, and `pages/seq/use=false` prints explicit page numbers instead of `f.`/`ff.`. All three ordinary `\\printacronyms` groups and all **198** registered terms are unchanged. An `acro`-only three-page example was compiled and visually inspected; the full anonymous-paper source build must still be checked. Original custom paper/DOI URLs, year, venue and source-citation metadata remain in the registry and bibliography, not the stock print list.

## Native acro page-index build convergence (2026-11-06)

The built-in `pages/display=all` appearance index increases the initial LaTeX/BibTeX passes needed for the anonymous two-column manuscript. The first full source run [Paper PDF #42150444462](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/runs/42150444462) hit latexmk's default **five-pass limit** (the emitted fifth-pass PDF already contained correct-looking occurrence labels). I added `paper/.latexmkrc` with an **eight-pass finite cap** to permit proper convergence. This is a build-system setting, **not a custom `acro` list renderer**. Full source-run success and PDF QA must still be confirmed.

## Verified default acro appearance index (2026-11-06)

I completed the full-source build at `117f247`: [Paper PDF #42153100997](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/runs/42153100997) succeeded together with Awesome Lint and Catalog Check. I retrieved artifact **13473718306** and inspected the real **29-page anonymous PDF**, including index **pp. 17–22** and both unchanged vector maps. The **stock** `acro` list now displays usage pages, e.g. PosterText **pp. 7, 10, 14**, UniWorld-Design **pp. 7, 11, 13**, PosterText-Bench **pp. 14, 15**, without a custom list renderer. No clipping or unresolved-citation/`acro` warnings were detected in the inspected output. **No original-paper evidence or 198-term metadata changed.**

## Native acro source-link pilot (2026-11-06)

I tested **four representative** built-in `acro` `extra` fields (`\\citealp{bibkey}; \\href{paperurl}{paper}`) rather than restoring an exhaustive custom bibliographic renderer. The actual **29-page** anonymous manuscript from source `dd1ee78`, [Paper PDF #42159374944](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/runs/42159374944) (artifact **13476423122**), passed PDF compilation and visual index review on pp. 19–22. All four `paper` PDF URI annotations match the source-registered arXiv URLs; the original `p.`/`pp.` appearance-page index remains visible, and all three default lists plus 198 terms are preserved. No external metadata was changed. The pilot introduces a small amount of ordinary column wrapping, so adding such annotations across all systems is a separate **readability and page-budget decision**; it is **not** approved automatically.
