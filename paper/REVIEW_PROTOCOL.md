# Review protocol (prospective draft; not executed)

This is a plan for making the research synthesis reproducible, **not** a claim that the searches and screening below have been run. Working checkpoint: 2026-11-03.

## Review questions

1. Which output representations (pixels, geometry, SVG, layers, DOM/code or native documents) are delivered?
2. Which editing, reconstruction and generation-time control operations are possible, demonstrated, and quantitatively scored?
3. What are the evaluation targets, input/output contracts, native-format checks and human-judgment protocols?
4. What are the availability and provenance of code, weights, training data and evaluation data?

## Planned discovery sources and search concepts

Proposed sources: ACM Digital Library, IEEE/CVF proceedings, ACL Anthology, OpenReview, arXiv and a broad bibliographic index (such as OpenAlex). Record **source, exact query, search fields, filters, timestamp, result count and exported identifiers** for every execution; do not claim a source was searched until its log exists.

Candidate Boolean concepts (adapt each to the database syntax):

- `("graphic design" OR advertising poster OR infographic OR "slide generation" OR "scientific figure") AND (generat* OR edit* OR reconstruct* OR benchmark)`
- `(SVG OR vector OR layered OR PSD OR HTML OR "layout generation") AND (design OR poster OR illustration) AND (generat* OR edit* OR reconstruct*)`
- `(typography OR graphic OR layout OR vector) AND (benchmark OR metric OR evaluation OR "user study")`

Also perform backward and forward citation searches from core surveys and benchmark papers. The proposed cut-off is **2026-11-03**; record each paper's earliest public date and its venue publication date separately.

## Planned screening and deduplication

Initial title/abstract inclusion: research substantially concerned with composed visual design, typography in graphics, structured design representations, graphic-design editing or design-specific evaluation. Exclusion codes: `E1 off-topic`, `E2 generic natural-image generation without design-specific contribution`, `E3 duplicate/preprint version`, `E4 original paper unavailable`, `E5 nonresearch resource`, `E6 task or artifact mismatch`.

For retained full texts, extract representation, inputs, outputs, demonstrated versus measured edit operations, experiment table/figure locators, dataset and evaluation protocol, and source depth. Use independent reviewers on a pilot screening set and adjudicate disagreements before final inclusion. Do not report inter-rater agreement without computing it.

## Minimum evidence fields

`study_id, canonical_title, authors, first_public_date, venue_year, primary_url, doi, arxiv_id, task, input_contract, output_representation, editable_object, generation_time_control, demonstrated_edit, scored_edit, target_metric, non_target_metric, reflow_scope, native_format_validity, human_study, datasets, source_section, evidence_tier, code_availability, weight_availability, uncertainty, adjudication_status`.

Distinguish `not_reported`, `not_verified`, and `not_applicable`. Verify numeric claims against original methods/results, tables, and supplements. Cross-check bibliographic author, title and DOI metadata against the publisher record.

## Direct 225-study spreadsheet-to-bibliography crosswalk (2026-11-04)

We directly read the native Google Sheet Evidence Matrix 225 and related prior-survey and citation tracking tabs. The frozen snapshot contains 225 stable records; conservative DOI/arXiv/URL/title matching maps 157 to the 186-item bibliography, leaving 68 pending review. The two CSV files evidence_register_225_snapshot.csv and evidence_register_225_crosswalk.csv are now mandatory inputs to scripts/check_evidence_register.py in pre-commit and CI, and their IDs are transferred to literature_citation_audit.csv without transferring unverifiable evidence tiers. This is an identity crosswalk, not an inclusion/exclusion decision. See EVIDENCE_REGISTER_RECONCILIATION.md for the exact workbook tab, snapshot date, source metadata and mandatory manual refresh after changes in the private Sheet.

## Citation-level audit register (initialized, not fully adjudicated)

The file `literature_citation_audit.csv` enumerates the 186 BibTeX references with keys, bibliography titles, citation-year metadata, and URLs. For the first 144 keys, `not_verified` indicates that a per-key verification record has **not yet been transferred and documented**; they do not negate earlier method-level reading in the separate 225-entry working register. `working_register_id` must be populated only after identity/version reconciliation, with `duplicate_group` for preprint/published aliases and `source_section_locator` for original methods/results evidence. A provisional identity ratio of 157/225 is now available from the frozen spreadsheet crosswalk; do not interpret the unmatched 68 as excluded studies or the match as verified experimental evidence. The original 36 added references and six new primary-source-checked studies have `source_depth=abstract_index` with an original arXiv author/title/abstract locator, not an unperformed methods/results verification. `catalog_citation_crosswalk.csv` independently matches the 207 public-catalogue paper records to the 186 citations (143 linked; 64 unresolved automatically), without assigning inclusion or exclusion. The validator `scripts/check_literature_audit.py` checks CSV/BibTeX sync and requires a source locator before any evidence is marked verified.

## Counts and diagrams

The public awesome catalog and the **225-entry provisional working evidence register** are different snapshots. The 88/28/109 evidence-tier checkpoint measures verification depth and is not a screening flow or a count of studies independently read in full. Reconcile version/duplicate IDs before computing year distributions, acceptance fractions or any PRISMA-style figure. A proper flow requires logged **identified → deduplicated → title-screened → full-text assessed → included** counts with exclusions.

## Evaluation rubric

Separate: (a) output-format affordance, (b) qualitative editing demonstration, (c) controlled human editing efficiency, (d) quantitative edit instruction success, (e) necessary dependent reflow and protected-content preservation, and (f) native-format validity. Do not interpret FID/CLIP, SVG export, raster compositing or VLM aesthetic scores as interchangeable editing outcomes.

## Private workbook freshness gate

Before bibliography or survey coverage changes, read the original private Google Sheet again. The committed snapshot manifest requires a new authenticated review within 30 days; CI fails if the source review date expires or the worksheet identity changes. The CI has no real-time private Google Sheets access. Never renew the manifest without actually checking the live source. Negative-case tests guard against losing a study ID or a published/preprint alias.

## Ten-source P1 expansion and review boundaries (2026-11-04)

I re-opened the native Evidence Matrix 225, prior-survey and source-tier tabs and read original author/publisher abstracts for ten previously unresolved P1 papers.
The bibliography now contains **196** cited works, and the frozen 225-study identity crosswalk links **167**, leaving **58** under review.
The separate 207-paper public-catalogue crosswalk links **150**, leaving 57 requiring reconciliation.
The new ten citation-audit entries are conservatively tagged `abstract_index`; original quantitative experiment tables and editability claims have **not** been re-audited merely because the source's title or abstract was checked.
