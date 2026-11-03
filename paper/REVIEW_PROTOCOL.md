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

## Counts and diagrams

The public awesome catalog and the **225-entry provisional working evidence register** are different snapshots. The 88/28/109 evidence-tier checkpoint measures verification depth and is not a screening flow or a count of studies independently read in full. Reconcile version/duplicate IDs before computing year distributions, acceptance fractions or any PRISMA-style figure. A proper flow requires logged **identified → deduplicated → title-screened → full-text assessed → included** counts with exclusions.

## Evaluation rubric

Separate: (a) output-format affordance, (b) qualitative editing demonstration, (c) controlled human editing efficiency, (d) quantitative edit instruction success, (e) necessary dependent reflow and protected-content preservation, and (f) native-format validity. Do not interpret FID/CLIP, SVG export, raster compositing or VLM aesthetic scores as interchangeable editing outcomes.
