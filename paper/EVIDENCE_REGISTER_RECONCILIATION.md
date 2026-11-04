# Mandatory evidence-register crosswalk

I directly read the 2026-11-04 snapshot of [Graphic Design Generation -- 185 Paper Evidence Matrix](https://docs.google.com/spreadsheets/d/1PJtvX34FYoOnF8LS4-0WHpiR3B_KQ6n5fqRBtTeF3Zc/edit), despite the legacy workbook name.

**Source-of-truth tab:** Evidence Matrix 225 (Google Sheet gid 8402), A1:AG226. I also inspected the actual contents of 225 Citation and R-E-V Coverage, Prior Survey and Screening, 225 Source Tier Reconciliation, Search Screen Decisions, and 225 Manuscript Citations. This is a frozen source copy, not a live link.

**Current baseline (2026-11-04, after source adjudication):** 225 stable study IDs; **186** bibliography entries; **157** matched identities; **68** needing review. The separate public catalogue has 207 papers, with **143 matched** and **64 needing review**. The old 180/148/77 and 207/138/69 results were initial checkpoints. Neither unmatched group should be labelled excluded. No source-tier was promoted merely because its citation key matched.

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
