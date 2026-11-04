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
- [ ] **T02 · CGD-092 · TKG-DM** — same review, independently; do not borrow TAUE's evidence tier.
- [ ] **T03 · CGD-159 · Alfie** — same review, including what is actually editable after export.
- [ ] **T04 · CGD-174 · LayeringDiff** — distinguish generated layers from demonstrated edit success.
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
- [ ] Confirm CI and visually inspect current manuscript PDF including all acro lists and maps; check only after inspecting the actual generated artifact.
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
