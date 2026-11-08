# Scientific readiness — 2026-11-08

**PR:** https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/pull/135

**Scope:** The paper, scientific source records, bibliography, source-related CI and methods. Research maps and institutional logos are managed in another concurrent session and were not changed here.

## Source accounting

| Denominator | Number | Valid interpretation |
| --- | ---: | --- |
| Frozen working study IDs | 225 | Curated inventory, not a systematically screened inclusion count |
| Bibliographically linked study IDs | 225 | Study identities with citation keys; not 225 experimental checks |
| Public catalogue paper rows | 207 | Separate snapshot, now all matched to a bibliography key |
| Citation keys and audit rows | 259 | Includes methods, related surveys, datasets and benchmarks |
| Citation-level original methods/results audits | 102 | Bounded original sections/tables or prior documented source audits, not replication |
| Citation-level original author/publisher abstracts | 153 | Task/scope verified; no results audit |
| Publisher metadata only | 3 | Research identity known; full methods/experiments unverified |
| Unverified primary abstract | 1 | `liu2024graphiclayoutsurvey`, IEEE CSCWD 2024 |
| Historical methods/results transfers | 58 | Frozen live-workbook provenance in `PRIMARY_SOURCE_EVIDENCE_TRANSFERS_20261108.csv` |
| Original abstract checks transferred in T22 | 75 | Frozen first-party abstract provenance in `T22_ABSTRACT_SOURCE_RECONCILIATION_20261108.csv` |
| Original abstract checks transferred in T23 | 4 | Rico, DocLayNet, Visual Feedback Layout Model, Mackinlay 1986 |

Original author/publisher source checks have distinct levels: `methods_results` certifies a limited source-locator record, not independent scientific replication; `abstract_index` certifies original source abstract identity and task, not detailed methods or numeric table results. Numerical outcome/edited-file interpretation must match each particular table, input and output contract. All working-study scientific inclusion decisions remain separate.

## Research synthesis checked

The manuscript analyzes representation × editing operation × evaluation target. LayoutDM and LayoutFlow FIDs depend on split/feature network; COLE's SVG editor illustration is not measured edit-command reliability; layered raster outputs are not semantic editable text; PosterMELD's print-ready rate is not its conditional aesthetic quality score; LayoutGAN, PosterLayout, CGL-GAN and SVGEditBench have adverse metric comparisons and conditional task denominators. Advertising CTR, subject preservation, OCR legibility, format validity, human aesthetics and executed native edit operations are not interchangeable outcomes.

`paper/scripts/report_citation_evidence.py` inventories bibliography evidence tiers, `paper/scripts/report_claim_evidence.py` enumerates citation-bearing source lines and lexical numerical/table claims, and `paper/scripts/check_literature_audit.py` checks provenance-manifest consistency and prevents abstract-level verified empirical results. These are mechanical gates **not** a demonstration of semantic factual accuracy in every sentence.

## Screening and methodological limitations

The live Google Sheets **Evidence Matrix 225** and audit/screening tabs were read. `Search Query Log` and `Search Wave2 Query Log` record targeted exploration in October 2026, including approximate query phrases, candidate decisions and source class. They **explicitly do not record raw per-database retrieval counts**. The project has not demonstrated reproducible platform search exports, deduplication with record IDs, complete title/abstract and full-text exclusion records, reviewer agreement or final systematic included-study count. The manuscript appropriately labels itself an initial narrative survey with structured evidence coding; do not create a PRISMA flow or a systematic coverage claim.

## Substantive work still required

1. Source-review depth: **157 citation keys** have not yet been traced to original methods/results, including three catalogue-only and one unavailable original abstract. Of these, some may only need abstract-level attribution because they are used as background; numerical/editing claims need original tables and exact source locators.
2. Original accessible abstract/fulltext for `liu2024graphiclayoutsurvey` (CSCWD 2024, DOI 10.1109/CSCWD61410.2024.10580676) remains unavailable through retrieved first-party endpoints; published authors and pages 2632–2637 are corroborated by the original conference TOC.
3. Independently evaluated reopen–modify–save, protected-object preservation, instruction edit success, and semantic text retention cannot be inferred from SVG/PPTX/HTML/PSD output formats. Distinguish proposed evaluation protocol from an experiment actually run.
4. A systematic search and screening with real database retrieval exports, exclusion reasons, deduplication and scientific author decisions is unfinished. Author signoff is unperformed.
5. A latest-source GitHub Paper PDF CI success **plus actual rendered PDF visual inspection** remains necessary. Concurrent map/logo pushes can auto-cancel the paper workflow; a green older commit is not sufficient.

## Operational checks

- `python3 paper/scripts/check_literature_audit.py`
- `python3 paper/scripts/check_evidence_register.py`
- `python3 paper/scripts/check_bibliography.py`
- `python3 paper/scripts/report_claim_evidence.py --summary`
- `python3 paper/scripts/report_citation_evidence.py --json`

Do not promote a citation-level source tier, conclude scientific acceptance or report an editing operation as quantitatively validated merely because a check command passes.
