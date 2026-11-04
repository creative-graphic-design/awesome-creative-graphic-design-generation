# Mandatory evidence-register crosswalk

I directly read the 2026-11-04 snapshot of [Graphic Design Generation -- 185 Paper Evidence Matrix](https://docs.google.com/spreadsheets/d/1PJtvX34FYoOnF8LS4-0WHpiR3B_KQ6n5fqRBtTeF3Zc/edit), despite the legacy workbook name.

**Source-of-truth tab:** Evidence Matrix 225 (Google Sheet gid 8402), A1:AG226. I also inspected the actual contents of 225 Citation and R-E-V Coverage, Prior Survey and Screening, 225 Source Tier Reconciliation, Search Screen Decisions, and 225 Manuscript Citations. This is a frozen source copy, not a live link.

**Current baseline (2026-11-04):** 225 stable CGD IDs; 180 manuscript bibliography records; 148 unique automatic identity matches (arXiv/DOI/exact URL/normalized title); 77 unresolved IDs. The 207-paper public catalog is a separate snapshot (138 linked, 69 unresolved by its existing method). Neither unmatched group should be labelled excluded. No source-tier was promoted merely because its citation key matched.

## Mandatory review flow

1. Before each bibliography, survey-coverage or literature claim change, open the **live private Google Sheet**, verify its modification time, and read Evidence Matrix 225, 225 Citation and R-E-V Coverage, Prior Survey and Screening, and the source-tier reconciliation tab.
2. If any row or metadata changed, refresh evidence_register_225_snapshot.csv from the live workbook, preserving stable IDs, year, task, primary source URL, original evidence-tier and source-verification details. Do not silently infer new tiers.
3. Recompute evidence_register_225_crosswalk.csv from DOI, arXiv ID, exact URL and normalized title, reconcile working_register_id in literature_citation_audit.csv, and manually adjudicate version aliases. No auto-exclusion is permitted. All 77 unresolved items have explicit needs_review statuses.
4. Run python3 paper/scripts/check_evidence_register.py and python3 -m unittest discover -s paper/scripts/tests -p 'test_*.py'. They reject missing or repeated IDs, wrong BibTeX links, dropped audit IDs, and regression above 77 unresolved sources. CI and pre-commit run the same gate.
5. Resolve missing citations by task and paper importance, original-paper methods/results evidence and verified identities, not to hit an arbitrary citation count.
6. Compare original prior surveys on what they actually count. Zou et al. (2025) describes **500 finally selected** papers in its methodology; its comparison table separately reports 267, which should be identified as an unresolved internal denominator discrepancy, not a 500-to-300 screening count.
7. Build the manuscript, visually inspect the actual PDF and research maps, and provide links with the PR outcome.

## CI authentication limitation

This workbook is private. **GitHub Actions cannot read the live Sheet without an authorized connection.** Our GitHub gate validates the checked-in, dated 225-row snapshot and the manuscript BibTeX against one another; it cannot detect an external Google Sheet edit that has not been synchronized. The source snapshot must be explicitly refreshed when the workbook changes. A stale external snapshot is a remaining operational risk, not evidence of a live automated sync.

## Current review queue

77 unresolved study identities remain; check their title, original source link, preprint-to-proceedings aliases, specific contribution, scope, and source tier. The unmatched pool contains catalog-only work and primary-source-checked studies; do not treat all 77 as equally studied, equally important, or eligible for automatic insertion.
