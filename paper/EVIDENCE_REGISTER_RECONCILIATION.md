# Mandatory evidence-register crosswalk

I directly read the 2026-11-04 snapshot of [Graphic Design Generation -- 185 Paper Evidence Matrix](https://docs.google.com/spreadsheets/d/1PJtvX34FYoOnF8LS4-0WHpiR3B_KQ6n5fqRBtTeF3Zc/edit), despite the legacy workbook name.

**Source-of-truth tab:** Evidence Matrix 225 (Google Sheet gid 8402), A1:AG226. I also inspected the actual contents of 225 Citation and R-E-V Coverage, Prior Survey and Screening, 225 Source Tier Reconciliation, Search Screen Decisions, and 225 Manuscript Citations. This is a frozen source copy, not a live link.

**Historical baseline (2026-11-04, at the earlier source-adjudication step):** 225 stable study IDs; **186** bibliography entries; **157** matched identities; **68** needing review. The separate public catalogue has 207 papers, with **143 matched** and **64 needing review**. The old 180/148/77 and 207/138/69 results were initial checkpoints. Neither unmatched group should be labelled excluded. No source-tier was promoted merely because its citation key matched.

## Mandatory review flow

1. Before each bibliography, survey-coverage or literature claim change, open the **live private Google Sheet**, verify its modification time, and read Evidence Matrix 225, 225 Citation and R-E-V Coverage, Prior Survey and Screening, and the source-tier reconciliation tab.
2. If any row or metadata changed, refresh evidence_register_225_snapshot.csv from the live workbook, preserving stable IDs, year, task, primary source URL, original evidence-tier and source-verification details. Do not silently infer new tiers.
3. Recompute evidence_register_225_crosswalk.csv from DOI, arXiv ID, exact URL and normalized title, reconcile working_register_id in literature_citation_audit.csv, and manually adjudicate version aliases. No auto-exclusion is permitted. All 68 unresolved items have explicit needs_review statuses.
4. Run python3 paper/scripts/check_evidence_register.py and python3 -m unittest discover -s paper/scripts/tests -p 'test_*.py'. They reject missing or repeated IDs, wrong BibTeX links, dropped audit IDs, and regression above 68 unresolved sources. CI and pre-commit run the same gate.
5. Resolve missing citations by task and paper importance, original-paper methods/results evidence and verified identities, not to hit an arbitrary citation count.
6. Compare original prior surveys on what they actually count. Zou et al. (2025) describes **500 finally selected** papers in its methodology; its comparison table separately reports 267, which should be identified as an unresolved internal denominator discrepancy, not a 500-to-300 screening count.
7. Build the manuscript, visually inspect the actual PDF and research maps, and provide links with the PR outcome.

## CI authentication limitation

This workbook is private. **GitHub Actions cannot read the live Sheet without an authorized connection.** Our GitHub gate validates the checked-in, dated 225-row snapshot and the manuscript BibTeX against one another; it cannot detect an external Google Sheet edit that has not been synchronized. The source snapshot must be explicitly refreshed when the workbook changes. A stale external snapshot is a remaining operational risk, not evidence of a live automated sync.

## Current review queue

68 unresolved study identities remain; check their title, original source link, preprint-to-proceedings aliases, specific contribution, scope, and source tier. The unmatched pool contains catalog-only work and primary-source-checked studies; do not treat all 77 as equally studied, equally important, or eligible for automatic insertion.

## Updated source and mandatory renewal gate

I verified three publication/arXiv aliases: DesignAsCode (2602.17690), GlyphDraw2 (2407.02252), and BizGen (2503.20672). I also checked original abstracts/proceedings for NeuralSVG, IGD, OmniSVG, LayerFusion, Revision Matters, and Draw with Thought, and added these six sources to the manuscript. Each new audit entry remains `abstract_index` rather than claiming a methods/results re-audit.

The new `evidence_register_snapshot_manifest.json` declares the private source workbook, worksheet, and date last reviewed. CI fails after 30 days without a newly recorded live-source review. **GitHub cannot read or detect private Sheet edits directly**: an authorized editor must actually re-open the workbook, compare the tabs, and refresh the snapshot before renewing the manifest date. Negative-case tests cover an expired date and a dropped arXiv/publication identity.

## Per-study triage queue (2026-11-04)

The file `evidence_review_queue.csv` enumerates all **68** unresolved stable IDs with their source URL, original catalogue task, spreadsheet evidence tier, pending manual decision and required next action. The working queue sorts **18 `P1-primary-source`**, **13 `P2-abstract-source`**, and **37 `P3-catalogue`** records. Those labels are based on the recorded verification metadata and are only *review priorities*; they do not assert an independent full-text read or eligibility. The same `check_evidence_register.py` CI gate now verifies the queue is a bijection with unresolved IDs, retains source metadata and includes no silently finalized decisions. Negative tests remove a row and corrupt a priority to ensure the gate fails.

## P1 source-identification batch (2026-11-04)

I consulted the live 225-study spreadsheet and its prior-survey, citation and source-tier tabs before adding ten previously unmatched papers from author/publisher original records.
The current snapshot remains 225 working studies; the manuscript bibliography is **196** papers, with **167 linked identities and 58 unmatched**.
The remaining priority tiers are **8 P1, 13 P2 and 37 P3**; these are review priorities, not exclusions or full-text reading totals.
I reduced the `check_evidence_register.py` unresolved ceiling to **58** and updated its negative-case tests to assert the new baseline.
The original-source metadata and boundary interpretations are recorded in `P1_SOURCE_TRIAGE_20261104.md`.

## T01: CGD-091 / TAUE (2026-11-04)

I re-opened row 92 in the live Google Sheet's Evidence Matrix 225, citation coverage and source-tier tabs, and read its prior-survey comparison tab. I independently inspected [the TAUE original HTML](https://arxiv.org/html/2511.02580), Sections 3–6, Table 2 and Figure 6, and matched the 2026 CVPR Findings publication to arXiv:2511.02580 (first public 2025-11-04). The 225-study frozen snapshot is unchanged; the manuscript now has **197 references / 188 acro entries / 168 linked / 57 unresolved (7 P1, 13 P2, 37 P3)**. The primary-source evidence, scope and editing-claim limitation are in T01_TAUE_SOURCE_AUDIT.md; T02 remains pending author approval. The unmatched 57 are not screened exclusions.

## T02: CGD-092 / TKG-DM (2026-11-05)

I checked the live Evidence Matrix row 93, citation/source-tier tabs and prior-survey comparison, then read the original [TKG-DM](https://arxiv.org/html/2411.15580) §§3–7, Table 1 and Figure 10. The CVPR 2025 paper and first arXiv publication (2024-11-23) are the same research contribution. The **225-row spreadsheet snapshot is unchanged**; this source-level update gives **198 references / 189 acro / 169 linked / 56 pending (6 P1, 13 P2, 37 P3)**. Chroma-key raster images are not native semantic layers; SDXL Table 1 does not show TKG-DM superiority over LayerDiffuse. Detailed evidence is in [T02_TKGDM_SOURCE_AUDIT.md](T02_TKGDM_SOURCE_AUDIT.md). The CI gate now requires <=56 unresolved and rejects broken TKG-DM source-identity aliases.

## T03: CGD-159 / Alfie (2026-11-05)

I re-read the live Evidence Matrix 225 row 160, Citation and R-E-V Coverage, Source Tier Reconciliation and Prior Survey and Screening. The Drive modification time **2026-11-03T06:03:55Z** predates the committed 2026-11-04 snapshot-review date; the 225-source snapshot remains unchanged. `alfie2025` links the ECCV 2024 arXiv/workshop study to Springer LNCS publication in 2025 using the original arXiv eprint and publisher DOI, without duplicating the contribution. The single RGBA foreground is a compositing affordance, not demonstrated native semantic design editing. Source evidence and numeric limitations: [T03 audit](T03_ALFIE_SOURCE_AUDIT.md).

Current manuscript identity accounting: **225 study IDs / 199 cited BibTeX works / 190 acro entries / 170 linked / 55 unresolved (5 P1 / 13 P2 / 37 P3)**. The public 207-paper catalogue independently matches **153** and leaves **54** unmatched; neither unmatched set is an exclusion count.

The strengthened source-identity regression tests and source-level validators passed [Paper PDF #41871516836](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/runs/41871516836), alongside Catalog Check and Awesome Lint. I also downloaded its genuine 29-page PDF and inspected the Alfie discussion, index, bibliography and both maps. Scientific author sign-off is still pending.

## T04: CGD-174 / LayeringDiff (2026-11-05)

I re-read live Evidence Matrix 225 row 175, 225 Citation and R-E-V Coverage, 225 Source Tier Reconciliation and Prior Survey and Screening before adding the citation.
The Sheet's last-modified timestamp (**2026-11-03T06:03:55Z**) predates the committed 2026-11-04 snapshot-review date; I did not silently re-date or change its 225-row snapshot.
The arXiv `layeringdiff2025` identity is now linked to CGD-174 with original §§3–5/Tables 1–4 source evidence, without treating compositable image layers as demonstrated semantic editing.
**Current tally:** 225 stable IDs / **200** BibTeX / **193** acro / **171** linked / **54** pending (4 P1, 13 P2, 37 P3); the distinct 207-paper public catalog has **154** linked / **53** pending, none automatically excluded.
The identity gate's expected maximum is 54; its negative arXiv test expects detection of a *stale match method* if a damaged ID falls back to a title match.
After the regression-test correction, [Paper PDF #41944766288](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/runs/41944766288), Catalog Check and Awesome Lint passed on `1750e184`; I downloaded its 30-page PDF and inspected both maps.
Live private spreadsheet edits are not automatically synchronized to GitHub CI; author scientific approval is still pending before T05.

## T05: CGD-184 / UniWorld-Design (2026-11-05)

I re-read the live Evidence Matrix 225 row 185, Citation and R-E-V Coverage, Source Tier Reconciliation and Prior Survey and Screening.
The Drive workbook last changed **2026-11-03T06:03:55.045Z**, before the existing 2026-11-04 checked-in snapshot review; I therefore kept the frozen 225-row snapshot and date intact.
Original [arXiv:2608.03971v1](https://arxiv.org/html/2608.03971), §§3–5, Tables 1–4 and Appendix B support instruction-controlled **raster** layer recovery and generation but not exported native PSD or quantitative post-export editing success.
I linked CGD-184 to uniworlddesign2026 in both crosswalks, recording **225 IDs / 201 references / 194 acro / 172 linked / 53 unresolved** (3 P1/13 P2/37 P3), public **155/207 linked / 52 pending**.
The source-tier history was not transferred automatically, and no unmatched study was excluded. See [T05 original-source audit](T05_UNIWORLD_DESIGN_SOURCE_AUDIT.md).
