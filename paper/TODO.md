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
- [ ] **T06 · CGD-103 · PosterText** — inspect typography/editing evidence separately from raster text quality.
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
- [ ] **T17 · acro index:** evaluate the **185-entry complete display** (source citation, year, venue, task/representation where known, appearance pages); postpone pruning until after author review.
- [ ] **T18 · Fix stale overview prose:** reconcile historical 180/186 or 148/157/68 counts in documentation with the latest labelled checkpoint, without rewriting history.
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
