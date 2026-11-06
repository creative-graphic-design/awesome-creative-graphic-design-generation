# Survey manuscript TODO — review one small item at a time

This is the **operational work queue** for [PR #135](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/pull/135).
Use [WRITING_CHECKLIST.md](WRITING_CHECKLIST.md) for permanent author instructions, [evidence_review_queue.csv](evidence_review_queue.csv) for the **complete** unresolved-paper list, and [REVIEW_PROTOCOL.md](REVIEW_PROTOCOL.md) for screening rules.
**Do not start another study while the current study is awaiting author review.**
Update this TODO in the same commit as the work it tracks; do not check an item merely because code was written.

## 0. Verified baseline — 2026-11-04

- [x] Read the live 225-study evidence workbook and check in its snapshot/identity crosswalk.
- [x] Record **225** working IDs / **196** BibTeX entries / **185** acro entries.
- [x] Reconcile **167** working IDs to references; keep **58** unresolved and explicitly **not excluded**.
- [x] Keep the remaining queue complete: **8 P1 / 13 P2 / 37 P3**.
- [x] Confirm Paper PDF, Catalog Check and Awesome Lint passed for source commit `bf56534a653e5143dad7a9b065ba3bf4d94a47f1`, [Paper PDF run #41840326573](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/runs/41840326573).
- [x] Retrieve the **28-page** PDF and visually inspect the manuscript's research-map page 3.
- [ ] **Author review:** approve this incremental work order before moving beyond the first study.

These numbers are a dated checkpoint, **not** a systematic-search flow, a complete primary-paper audit, or a fixed citation target.
Before a new citation batch, re-open the actual Google Sheet and confirm whether its content changed; GitHub CI only sees the frozen snapshot.

## 1. NEXT — review one P1 study at a time

- [ ] **T01 · CGD-091 · TAUE** — confirm same-work/preprint identity, original task and output, editing claim, evaluation evidence/section locator, and inclusion decision.
  - Source audit prepared for author review (2026-11-04): original Sections 3–6, Table 2 and Figure 6, plus CVPR 2026 Findings metadata; details in [T01 source audit](T01_TAUE_SOURCE_AUDIT.md). Keep unchecked until sign-off.
- [x] **T02 · CGD-092 · TKG-DM** — original Sections 3–7, Table 1 and Figures 2/10 independently audited in [T02_TKGDM_SOURCE_AUDIT.md](T02_TKGDM_SOURCE_AUDIT.md); author scientific approval remains pending.
- [x] **T03 · CGD-159 · Alfie** — original §§4–5.1, Table 1 and Figs. 3/5–7 checked in [T03 source audit](T03_ALFIE_SOURCE_AUDIT.md). A compositable RGBA bitmap is not native design-object editing; PDF and author-approval gates remain open.
- [x] **T04 · CGD-174 · LayeringDiff** — original §§3–5, Tables 1–4 and Figs 1/7/8 audited in [T04 source audit](T04_LAYERINGDIFF_SOURCE_AUDIT.md); pending PDF validation and author scientific review are tracked below.
- [ ] **T05 · CGD-184 · UniWorld-Design** — check the concrete output contract and any claimed native format.
- [x] **T06 · CGD-103 · PosterText** — inspected raster text-patch editing evidence separately from native document editability; main-paper v2/v3 tables and method are now source-verified. **Scientific author approval and a separate supplement audit remain pending**.
- [ ] **T07 · CGD-072 · Mise-en-Scène** — resolve paper identity and actual generation/editing task.
- [ ] **T08 · CGD-073 · Multi-Object Advertisement Creative Generation** — check compositional constraints and evaluation.

**Per-study definition of done (all required):**

1. Record original publisher/arXiv link, canonical title, authors, relevant year, version aliases, and exact methods/results/table/figure locations in the evidence notes.
2. Record **scope and editorial decision with a reason**; allow `pending`, and never turn an unlinked source into an automatic exclusion.
3. Distinguish **format affordance / demonstrated editing / quantitatively scored editing / evaluation target**. Mark unverified claims `not_verified`.
4. If justified by evidence, update `references.bib`, manuscript discussion, `acronyms.tex`, `literature_citation_audit.csv`, both identity crosswalks and `evidence_review_queue.csv` together. If no citation is warranted, explicitly document why.
5. Run the evidence-register validator, literature-audit/bibliography checks and negative tests; **build and visually inspect the resulting PDF and maps**; provide links and ask for confirmation before the next ticket.

## T01 source-audit checkpoint — 2026-11-04

- [x] Source review and synchronized records: 225 working IDs / **197 references / 188 acro / 168 linked / 57 unresolved (7 P1, 13 P2, 37 P3)**.
- [x] Confirmed all three CI checks passed at source commit `9545d800babd0235e6b512efe836bb19480a470a` ([Paper PDF run #41850864927](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/runs/41850864927)); retrieved the **29-page** PDF, inspected research map p. 3, TAUE evidence pp. 11–12, acro p. 21 and reference p. 26, and verified no unresolved citations or TeX box warnings in the log.
- [ ] Author sign-off on T01 before processing T02.

## 2. Remaining paper queue (do not bulk-add citations)

- [ ] **T09 · P2 abstract/index evidence — 13 records:** verify one by one in `evidence_review_queue.csv`, promoting a record only with its original source locator.
- [ ] **T10 · P3 catalogue evidence — 37 records:** start with identity/deduplication and scope; schedule full reading only when justified.
- [ ] **T11 · Resolve title/arXiv/proceedings aliases:** prevent two citations for the same contribution.
- [ ] **T12 · Validate source depth of linked studies:** an automatic match among the 167 is **not** a verified scientific claim.
- [ ] **T13 · Compare prior surveys:** log exact coverage, selection method and original figure references; preserve Zou (2025)'s unresolved 500-vs-267 discrepancy.
- [ ] **T14 · Check empirical comparisons:** validate original tables, datasets, measured outputs, experimental settings and limitations.

## 3. Presentation and publication-readiness

- [ ] **T15 · Research figures:** verify every research-map node, publication year and method-family encoding against original sources; compare at actual PDF size.
- [ ] **T16 · Images and university/company marks:** select attributed original examples and verify affiliation and logo redistribution/trademark conditions before adding assets.
- [x] **T17 · acro print index:** the **198-entry registry** (27/151/20) and its compact source-linked output are preserved, PDF CI succeeded at source `0dbe879` ([Paper PDF #42033969385](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/runs/42033969385)), and I compared actual index pp. 18/22/24, including year/source/URL/usage pages. Long Task/Representation descriptions remain stored as metadata, not printed in the two-column index. Final publication-page-budget curation and author scientific approval remain open.
- [x] **T18 · Label historical overview counts:** I revised README / acro audit headings and tense so old **2026-11-03/04 snapshots** (180/186 BibTeX, 175/185 acro, 148/157 matches and initial 22/130/16 acro distribution) are explicitly historical, not current coverage. I also corrected the README's stale reference to **two** acro lists: the current paper has **three**. Current validated source stage remains **225 / 202 BibTeX / 198 acro (27/151/20) / 173 linked / 52 pending**. Historical numbers are preserved for provenance.
- [ ] **T19 · Search reproducibility:** execute and log actual multi-database searches, deduplication, inclusion/exclusion decisions and a screening flow before claiming systematic completeness.
- [ ] **T20 · Final PDF review:** build anonymous manuscript, inspect all figures and acro lists, validate citation resolution and provide latest manuscript + both map PDFs.

**Operating rule:** Report only (a) the ticket just checked, (b) evidence and decision, (c) changed files/CI/PDF, and (d) the *single next ticket*. Do not expand all 58 unresolved studies in one turn.

## T02 primary-source checkpoint — 2026-11-05

- [x] Directly re-opened live Evidence Matrix 225 row 93, citation/source-tier tabs and prior-survey methodology.
- [x] Checked CVPR 2025 proceedings metadata, 2024 arXiv version, original Sections 3–7 and Table 1; no unsupported SDXL superiority claim.
- [x] Synchronized **225 records / 198 references / 189 acro / 169 linked / 56 unresolved (6 P1, 13 P2, 37 P3)**, including the pending queue and regression test.
- [x] At source commit `aa9579f80a71700eeff58817a361775909f033c3`, [Paper PDF #41857746475](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/runs/41857746475), Catalog Check and Awesome Lint **all succeeded**. Retrieved artifact **13339058432** (`survey-paper-ca1cabe08bf759c8e93715968f83620722dec331`): **29-page** anonymous manuscript; rendered and inspected manuscript pp. **3, 11–12, 21 and 26** and both standalone **26- and 67-study** research-map PDFs, with no apparent overlap or clipping in these inspected pages. The TeX log has no unresolved-citation/reference or overfull/underfull box messages.
- [ ] Author scientific review of T02 before T03 / CGD-159 / Alfie.

## T03 primary-source checkpoint — 2026-11-05

- [x] Re-read live Evidence Matrix 225 row 160, 225 Citation and R-E-V Coverage, 225 Source Tier Reconciliation, and Prior Survey and Screening; no newer sheet modification than the dated committed snapshot review.
- [x] Compared [original arXiv §§4–5.1](https://arxiv.org/html/2408.14826) with [Springer LNCS 15627](https://doi.org/10.1007/978-3-031-92808-6_3); 2024 preprint/workshop and 2025 publication describe the same contribution.
- [x] Synchronized **225 working IDs / 199 references / 190 acro / 170 linked / 55 unresolved (5 P1 / 13 P2 / 37 P3)**, including a negative arXiv-alias regression test.
- [x] **T03 source PDF accepted:** for source `0e308af`, [Paper PDF #41871516836](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/runs/41871516836), Catalog Check and Awesome Lint all passed. Downloaded artifact **13345402864**: **29-page anonymous PDF**; rendered and inspected pp. **3, 7, 11–12, 17, 27**, plus the standalone **26-study narrative** and **67-study atlas** PDFs; no visible clipping/overlap in these inspected locations and no unresolved citation/reference, acro, overfull or underfull box warnings in the final log. Details in [T03 source audit](T03_ALFIE_SOURCE_AUDIT.md).
- [ ] Author scientific review of T03 before **T04 / CGD-174 / LayeringDiff**. The user's instruction to continue permitted starting T03, but was not treated as unconditional scientific sign-off.

## T04 primary-source checkpoint — 2026-11-05

- [x] Re-read live Evidence Matrix 225 row 175, Citation and R-E-V Coverage, Source Tier Reconciliation, and Prior Survey and Screening; original sheet timestamp 2026-11-03T06:03:55Z predates the frozen 2026-11-04 snapshot review.
- [x] Rechecked [LayeringDiff original arXiv](https://arxiv.org/html/2501.01197) §§3–5, Tables 1–4 and Figures 1/4/6–8. Only the initial composite generator is fixed; FBDD/HFA require 20,000 training composites.
- [x] Synchronized **225 IDs / 200 references / 193 acro / 171 linked / 54 unresolved (4 P1 / 13 P2 / 37 P3)**, with an arXiv identity negative regression test.
- [x] **T04 original-source PDF QA passed:** for source `1750e184`, [Paper PDF #41944766288](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/runs/41944766288), Catalog Check and Awesome Lint passed. I retrieved artifact **13379065431** (**30-page** anonymous PDF), inspected pp. 3, 7, 11, 12, 17, 19, 22, 25, 30 and both 26-/67-study standalone maps; no visible overlap/clipping on inspected output or unresolved citation/acro/box warnings. Details: [T04 audit](T04_LAYERINGDIFF_SOURCE_AUDIT.md).
- [ ] Author scientific review of T04 before **T05 / CGD-184 / UniWorld-Design**. This request to continue authorizes work on T04, not automatic approval of T03 or T04 scientific claims.

## T05 primary-source checkpoint — 2026-11-05

- [x] Re-read live Evidence Matrix 225 row 185, Citation and R-E-V Coverage, Source Tier Reconciliation and Prior Survey and Screening; Drive modified 2026-11-03T06:03:55Z before the source snapshot review.
- [x] Check [UniWorld-Design §§3–5, Tables 1–4 and Appendix B](https://arxiv.org/html/2608.03971); PSD training material is not native PSD output, and VLM structural proxies are not observed edit-instruction success.
- [x] Source-stage synchrony: **225 IDs / 201 BibTeX / 194 acro / 172 linked / 53 unresolved (3 P1/13 P2/37 P3)**; public catalogue **155/207 linked**, new arXiv negative regression test, unresolved ceiling **53**.
- [x] Verified scholarly-source commit `fb1f41e`: [Paper PDF #41989947985](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/runs/41989947985), Catalog Check and Awesome Lint all passed. Downloaded artifact **13398466465**, 30-page anonymous PDF; visually inspected pp. **3, 7, 11, 13, 22, 26** and both 26-/67-study vector maps; no visible clipping/overlap in inspected regions or unresolved citation/acro/box warnings. Details: [T05 source audit](T05_UNIWORLD_DESIGN_SOURCE_AUDIT.md).
- [ ] Keep scientific sign-off open for T04 and T05; do not begin T06 / CGD-103 / PosterText before this gate.

## T06 primary-source checkpoint — 2026-11-05

- [x] With the user's latest instruction to continue, re-read the live Evidence Matrix 225 row **104**, Citation and R-E-V Coverage, Source Tier Reconciliation, and Prior Survey and Screening; its Drive modified time **2026-11-03T06:03:55Z** predates the committed source snapshot.
- [x] Audit [PosterText original arXiv v2](https://arxiv.org/html/2608.16289v2) Sections 3–4, Figure 3 and Tables 1–2; verify that arXiv v3 is later and retain the final numerical-version check.
- [x] Distinguish **quantitatively evaluated raster text-patch editing** from the HTML **dataset annotation**, as well as task-specific OCR fidelity, non-target Masked-LPIPS, VLM judging and worse modification text accuracy compared with Nano Banana 2; see [T06 original-source audit](T06_POSTERTEXT_SOURCE_AUDIT.md).
- [x] Synchronize **225 studies / 202 BibTeX / 198 acro (27/151/20) / 173 linked / 52 unresolved (2 P1 / 13 P2 / 37 P3)** and public catalogue **156/207 linked / 51 pending**, with new negative arXiv identity test and a CI ceiling of **52**.
- [x] **T06 PDF/map artifact gate:** scientific source `729c2343` passed [Paper PDF #41997058915](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/runs/41997058915), Catalog Check, and Awesome Lint. I downloaded exact artifact **13401199657**: the **31-page** anonymous PDF and both standalone **26-/67-study** maps; rendered the full manuscript at overview resolution, inspected original map (p. 3), representation (p. 7), method (p. 10), editing results (p. 14), benchmark (pp. 15–16), SGSD (p. 18), PosterText (p. 22), PosterText-320K/Bench (p. 24) and reference [99] (p. 27), plus both maps at 200 DPI. No evident clipping in inspected regions, log citation/acro/box warnings, or text-word boxes outside page boundaries. See [T06 audit](T06_POSTERTEXT_SOURCE_AUDIT.md).
- [ ] **T04/T05/T06 author scientific approval** remains pending. The **v3 main-paper** Tables 1–2, Figure 3, methods and metric definitions were directly compared with v2 on 2026-11-06; **supplementary implementation details are not independently verified**. **T07 / CGD-072 / Mise-en-Scène has not started.**

## T06 acro wrapping / typesetting correction — 2026-11-05

- [x] Diagnose the full-justified `description`-based `survey-rich` index and awkward intra-word line breaks on the actual T06 PDF.
- [x] Preserve every source-backed display field and all **198** entries, but use ragged-right copy and disable automatic word-hyphenation in the index, with a mechanical CI regression guard.
- [x] Compile/render an independent four-system `acro` specimen before changing the paper template.
- [x] The first ragged-right-only PDF built successfully at [#42025690265](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/runs/42025690265) and was inspected, but the odd metadata breaks remained; its typography was superseded by the **compact index** in `0dbe879`, verified in [Paper PDF #42033969385](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/runs/42033969385) and recorded in the later acro second-pass checkpoint below.
- [ ] Author scientific approval remains open; the former v3 main-paper numerical/source-claim check was resolved in the 2026-11-06 primary-PDF comparison, but a separate supplement remains unverified. No T07 work has started.

## acro second-pass: remaining awkward line wraps (2026-11-05)

- [x] Recheck the **actual** success-status [Paper PDF #42025690265](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/runs/42025690265), artifact and 31-page output at pp. **22 and 24**. The ragged-right-only change did **not** eliminate excessive wraps in long Task/Representation paragraphs.
- [x] Keep the full 198-entry registry and custom Task/Representation **data**, but make the **printed** index compact: short label, description, year/venue, original source, paper/DOI link and use pages. Do not silently remove provenance or source-linked entries.
- [x] Strengthen `check_manuscript.py` to forbid verbose Task/Representation data in the narrow two-column printed template while preserving underlying `\\DeclareAcroProperty` declarations.
- [x] Prototype the compact layout with a two-column `acro` LaTeX fixture and visually inspect it.
- [x] Scientific-layout source `0dbe879` passed [Paper PDF #42033969385](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/runs/42033969385), Awesome Lint and Catalog Check. I downloaded exact artifact **13417988514**, visually compared the **31-page** revised anonymous PDF at acro **pp. 18, 22, 24** against the earlier full PDF, verified PosterText/BENCH citations and usage pages and the transition to References (p. 24), scanned page-text bounding boxes (0 outside), and checked the final log (no unresolved citation, acro or TeX box warnings).

## Compact acro index: final heading wrap (2026-11-05)

- [x] Visually inspect the complete printed `acro` index pages **17–24**, including system/bibliography transitions, not just individual PosterText entries.
- [x] Identify the residual `Re-`/`sources` split in the long evaluation-group heading on p. **23**, shorten it to `Evaluation Resources`, and protect that title with the manuscript source CI.
- [ ] Verify a fresh full-paper PDF after this heading-only change, download its artifact and inspect actual p. 23 and overall page count before marking this final layout issue closed.

## acro PDF link-target fix (2026-11-05)

- [x] Diagnose actual old PDF link dictionaries: `paper` hyperlinks target escaped LaTeX text as external files and DOI hyperlinks contain literal `\\acrowrite`, despite visible blue labels. Prior 'working link' confidence was unjustified.
- [x] Fix the `survey-rich` template with expansion-safe `\\acrofield` targets; compile a local proof and verify its native PDF `LINK_URI` annotations, including repeated paper links and DOI.
- [x] Add structural and compiled-PDF CI regression checks for **all 171 paper URLs and 25 DOI URLs**, including repeated paper targets, with five positive/negative unit tests.
- [ ] Confirm updated **source-commit Paper PDF** CI succeeds, download full PDF and inspect real link actions/acro page headings and index; do not claim publication or author scientific approval based on PDF build alone.

## acro index: variable-width label spacing root cause — 2026-11-06

- [x] Screenshot the actual previous **p. 19** at high resolution; identify that `description` with `\\item[short]` uses mismatched start positions for first and continuation lines. The earlier ragged-right/metadata/heading/link fixes did **not** fix this structural alignment issue.
- [x] Compare locally compiled, real two-column eight-entry `acro` specimens of old `description` and new zero-indentation `list`, including long names, a paper link and a DOI link.
- [x] Apply the structural `list` index template without changing `acronyms.tex`, `references.bib`, scholarly prose, research maps or paper DOI/URL fields; guard against the original markup in CI.
- [ ] Confirm the complete newly built anonymous PDF, screenshot **pp. 18–24** (particularly p. 19), check output link URIs and original index entries, and update PR only after visual acceptance. Author scientific approval remains separate.

## Reset printed acro to the built-in template — 2026-11-06

- [x] Confirm in a locally compiled two-column `acro` specimen that the stock list works with full `short`/`long` descriptions and `display=all`; use that before any custom format design.
- [x] Remove the project-specific `survey-rich` printing template, keep all three stock `\\printacronyms` groups and 198 registered entries. Keep original metadata values stored but not printed as custom bibliography paragraphs.
- [x] Adapt CI from testing custom print layout and custom 196 PDF index hyperlinks to testing the **standard acro interface** plus original-source metadata consistency.
- [x] Verified [Paper PDF #42062616167](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/runs/42062616167) and artifact **13433601126**, actual **28-page** anonymous manuscript: rendered pp. 17–22, confirmed all three acro groups on pp. 17–21, including the previously problematic middle systems list (pp. 19–20), and inspected references transition on p. 21. Checked 0 off-page text words across the 28 pages and no undefined citation, acro or TeX box warnings. Standard template does not print custom source/year/URL/DOI/page-use metadata; registry source provenance remains intact. The 26-/67-study standalone vector maps are in the same artifact. Author scientific approval and PosterText v3 primary-source verification still remain pending.

## Default acro occurrence-page index — 2026-11-06

- [x] Confirm the stock `acro` v3.8 option `pages/display=all` records and prints occurrences in the ordinary `\\printacronyms` default template; test it after multiple LaTeX runs with usage pages 1 and 2.
- [x] Set `pages/display=all,pages/name=true,pages/seq/use=false` in the main paper's existing `\\acsetup` and add a CI source invariant. Preserve the stock three-list layout and complete 198-item acronym registry; no `survey-rich` custom template.
- [x] The successful [Paper PDF #42153100997](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/runs/42153100997) PDF (artifact **13473718306**) was inspected at all three index groups on pp. **17–22**. PosterText, UniWorld-Design and PosterText-Bench show explicit `pp.` usage pages without the old custom-renderer alignment defect; research maps and bibliography were retained. This is layout acceptance, not scientific author approval.

## Real-paper default acro pages: latexmk convergence (2026-11-06)

- [x] Retrieved failed [Paper PDF #42150444462](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/runs/42150444462) output and actual **29-page** last-pass PDF. Confirmed valid-looking stock page index: PosterText **pp. 7, 10, 14**, UniWorld-Design **pp. 7, 11, 13**, PosterText-Bench **pp. 14, 15**. The failure was **latexmk default 5-pass maximum**, not a TeX parse error.
- [x] Added `paper/.latexmkrc` with `$max_repeat=8;` to allow a finite number of BibTeX/acro crossreference convergence passes while preserving the stock list.
- [x] Verified `117f247` source-run [Paper PDF #42153100997](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/runs/42153100997) **success**; downloaded artifact **13473718306**, 29-page anonymous PDF, inspected pp. **17–22** and both research-map PDFs. Appearance-page text matches original manuscript uses, including PosterText `pp. 7, 10, 14`, UniWorld-Design `pp. 7, 11, 13`, PosterText-Bench `pp. 14, 15`; zero off-page text words and no undefined-citation, `acro` or box warnings. No custom list template was reintroduced.

## Native acro bibliography-link pilot (2026-11-06)

- [x] Reproduce `extra` + `\\citealp` + native clickable `\\href` in a two-column LaTeX/PDF sample while preserving page-occurrence lists.
- [x] Add only four representative pilot entries: LayoutGAN, PosterText, UniWorld-Design and PosterText-Bench. Validate each added cite/URL against the existing BibTeX-aligned acro metadata using the existing manuscript checker.
- [x] Verified all three source-commit checks for `dd1ee78`, [Paper PDF #42159374944](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/runs/42159374944), downloaded artifact **13476423122** (29-page manuscript and two standalone maps), and inspected actual index pp. **19–22** side-by-side with the previous stock version. Exactly **four** valid PDF URI annotations link to the source-registered arXiv URLs; `p.`/`pp.` occurrence pages are retained; no out-of-page text or citation/acro/box warnings. Keep this a **four-entry pilot** pending author design feedback before any bulk additional source fields.

## PosterText v3 supplementary availability audit (2026-11-06)

- [x] Recheck the [arXiv v3 record](https://arxiv.org/abs/2608.16289), [official v3 HTML](https://arxiv.org/html/2608.16289v3) and nine-page PDF for appendix/supplement links; search exact-title/author/arXiv-ID and PosterText-320K/Bench code/dataset release leads. Document inspected surfaces and limitations in [the T06 audit](T06_POSTERTEXT_SOURCE_AUDIT.md).
- [x] Record **not obtained / not independently verified**, **not** `no supplement exists`: the main paper references supplementary implementation details, but no independent supplement or official code/data release was identified from these searches. The arXiv source archive could not be inspected in this environment.
- [ ] If a verified original supplementary artifact or author-designated release becomes accessible, audit implementation details (LoRA and schedules, RL reward weights, SGSD teacher/student settings), data provenance/validation and benchmark VLM judging before promoting supplemental reproducibility claims.
- [ ] Keep T04–T06 author scientific review and documented systematic screening separate; do not start T07 on the strength of the main-paper v3 check.

## PosterText v3 main-paper reconciliation (2026-11-06)

- [x] Visually compare the version-identified **v2** and **v3** nine-page original arXiv PDFs, especially Table 1/Table 2 (PDF p. 7), Figure 3 and evaluation definitions (PDF p. 5), and four-stage method descriptions; record numeric and representation outcomes in [T06 source audit](T06_POSTERTEXT_SOURCE_AUDIT.md).
- [x] Confirm that all audited v2 Table 1–2 values still match v3 and that the model's deliverable is a **raster image**, not a native editable HTML/PSD/SVG/text-layer document. No numerical changes to the TeX manuscript or 225/202/198/173 source-stage snapshot were justified.
- [ ] Retrieve and review the independently available **supplementary implementation** details referenced by the nine-page main paper; the main PDF ends in references, without an appendix.
- [ ] Preserve separate T04–T06 **author scientific approval** and systematic literature-search gates; do not begin T07 on the strength of this main-paper comparison.
