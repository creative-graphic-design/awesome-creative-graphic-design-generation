# Citation coverage and unfinished literature audit

## Updated citation-coverage checkpoint — 2026-11-04

I read the live private 225-study Evidence Matrix and the preceding survey/comparison tabs, joined its stable IDs to the BibTeX bibliography and recorded all unresolved sources. After confirming three arXiv-to-publication aliases and adding six studies supported by original publisher/author abstracts, the bibliography now contains **186** entries, with **157 / 225** working-study IDs linked and **68 / 225** pending manual identity/coverage review. The independent public 207-paper catalogue matches **143** and leaves **64** unresolved. These are two distinct source populations, and unmatched records are **not** excluded. The new `evidence_register_snapshot_manifest.json` creates a 30-day live-source review expiration in CI, while the GitHub CI checks only the frozen authorized snapshot (it cannot query a private Google Sheet). The subsequent 2026-11-03 numbers are historical, not the current status.

Checkpoint: **2026-11-03**. This is an executable bibliography/catalog crosswalk, **not** a PRISMA flow, independently screened sample, or full-text evidence synthesis.

## Distinct denominators

- Public `data/resources.csv` catalogue: **207 rows classified as Papers**, plus separate survey and benchmark/resource rows.
- Manuscript `references.bib`: **180 unique citation entries** after adding 36 primary-page-verified papers.
- Conservative public-catalogue to citation matching: **138 / 207 matched**, **69 / 207 unresolved** by canonical arXiv identifier, exact URL, or normalized exact title. The 42 bibliography entries not matched to a catalogue paper are **not necessarily missing from the catalogue**: they include related surveys, foundational datasets, and metrics, and may include version/title aliases.
- Separate provisional evidence register: **225 items** at a previous checkpoint (88 methods/results selections examined, 28 abstract/index only, 109 catalogue only). Those IDs have **not** been joined to the 180 bibliography keys. Counts from these distinct populations must not be divided to compute screening or reading rates.

The new `catalog_citation_crosswalk.csv` contains the exact public-catalogue records, matched BibTeX keys where found, and provisional unresolved rows. `scripts/check_catalog_crosswalk.py` checks against both files. Its unresolved rows are **not exclusions** and do not prove an article was never read.

## Remaining unmatched catalog papers, by primary category

| Primary category | Total | Unresolved |
|---|---:|---:|
| Content-agnostic layout generation | 50 | 17 |
| Content-aware layout generation | 39 | 16 |
| Graphic design generation | 40 | 13 |
| Composable and layered asset generation | 22 | 8 |
| Typography and text rendering | 14 | 2 |
| Graphic design editing and reconstruction | 18 | 7 |
| Scientific figure and graphical abstract generation | 8 | 0 |
| Scientific poster and slide generation | 16 | 6 |
| **Total** | **207** | **69** |

The 36 additions were identified from the public catalogue and then their **author names, original titles and task descriptions** checked against author-supplied arXiv abstract pages; the metadata snapshot is in `literature_expansion_20261103.csv`. They are marked `abstract_index` in `literature_citation_audit.csv`. Their original experimental tables, appendices, claims and paper-to-paper comparison assumptions have **not yet been comprehensively audited**. The remaining previously cited 144 records conservatively retain `not_verified` until individually linked to evidence locators.

## Next actions before claiming completeness

1. Adjudicate the 69 unresolved public-catalogue matches, prioritizing content-aware layout generation and graphics output/reconstruction.
2. Reconcile the separate 225-entry provisional register to citation keys, merging preprint and publication versions only with identity evidence.
3. Inspect original methods, experiment tables, benchmarks, native output contracts and editing claims; record exact source locators for each promoted row.
4. Run source-dated database searches, deduplicate discoveries and log exclusion reasons as defined in `REVIEW_PROTOCOL.md`, then consider a systematic-screening flow.

The bibliography targets **coverage of technical and empirical research lines**, not a cosmetic citation quota. The added material explicitly distinguishes layout generation-time conditioning, rendering quality, layered-format affordances, native editing operations, and multi-turn evaluation.
