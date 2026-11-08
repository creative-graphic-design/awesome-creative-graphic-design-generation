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

## T02 original empirical evidence (2026-11-05)

I inspected TKG-DM's original §§3–7, Table 1 and Figure 10 after checking the native spreadsheet. The added CVPR 2025 source (2024 first preprint) raises the manuscript to **198 bibliography entries**, with **169/225 uniquely linked** working study IDs and **56 pending**. This work generates chroma-key foreground imagery, not native editable text or vector objects. FID/mask metrics and user preferences test rendered generation, and Table 1's SDXL conditions favor LayerDiffuse on all four listed endpoints; no general editability or performance dominance is inferred. See `T02_TKGDM_SOURCE_AUDIT.md` for exact scope and methods/results locators.

## T03 dated source-audit checkpoint (2026-11-05; not systematic screening)

An original-methods/results review of **CGD-159 / Alfie** reconciles the 2024 ECCV workshop/preprint with the 2025 published LNCS record as **one study** and distinguishes compositable single-foreground RGBA generation from native multi-object editing claims. The methodology and original Table 1, Figure 6 and Figure 7 evidence are recorded in [T03_ALFIE_SOURCE_AUDIT.md](T03_ALFIE_SOURCE_AUDIT.md). The latest selected-source coverage is **199** BibTeX works, **170/225** matched study identities, **55** pending, with no automatic exclusions. The public 207-paper catalogue separately has **153** matches and **54** still needing identity review. Paper PDF #41871516836 passed and its 29-page anonymous PDF and maps received targeted visual QA.

These per-paper adjudications **do not** constitute an executed multi-database systematic search, fulltext screening or PRISMA inclusion flow; the protocol remains prospective.

## T04 original-source checkpoint (2026-11-05; not systematic screening)

I checked the actual CGD-174 / LayeringDiff record in the live 225-study Sheet and independently read the original methods/results in §§3–5 / Tables 1–4.
Its fixed initial generator followed by **trained FBDD/HFA decomposition** produces image layers; quality FID/KID/CLIP/FG-mIoU, a 24-person image-rating study, and synthetic reconstruction error do not measure post-export semantic edit instructions.
The current selected citation register has **200** works, **171/225** identities linked and **54** unresolved; the separate public 207-item catalogue matches 154.
I verified the source PDF and maps from [Paper PDF #41944766288](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/runs/41944766288), artifact 13379065431, and recorded evidence/limits in [T04 audit](T04_LAYERINGDIFF_SOURCE_AUDIT.md).
The planned multi-database search, deduplication and PRISMA screening flow **have not been executed**.

## Evidence depth after bibliographic closure — 2026-11-08

The frozen register contains **225 linked working study IDs with no unresolved bibliographic identity**, while the bibliography and separate citation-level audit contain **254 citations**. This is not a systematic-search or inclusion/exclusion flow.

At this dated checkpoint, citation-level evidence depths are **9 methods/results**, **98 abstract/index**, **3 catalogue-only** and **144 not verified in the citation-level register**. Earlier method-specific workbooks may contain additional source reading that has not yet been transferred. These are citation counts, not accepted systematic-review study counts.

Source-specific experimental statements require the original method or evaluation section, table, figure, or appendix locator. The remaining verification backlog must be audited in batches without falsely converting linked or abstract-only papers into primary-results verification. Bibliographic version aliases, systematic search/screening logs and author decisions remain separate unfinished steps.

## Transferred bounded prior-survey audits — 2026-11-08

Two original source audits, already documented in [T13_PRIOR_SURVEY_DENOMINATOR_AUDIT.md](T13_PRIOR_SURVEY_DENOMINATOR_AUDIT.md), were transferred to the *citation-level* register: `zou2025fragment` and `li2024criticalsurvey`. They are now labeled `methods_results` solely for **survey methodology, paper-count bookkeeping, source descriptions and bounded figure evidence**. This does not validate the 500-paper claim, reconcile the conflicting 267/500 denominators, check every individual underlying study or constitute our own systematic search. For Li, actual figure-image panels 4–6 remain uninspected; only captions and surrounding primary text were reviewed. Editing/evaluative performance of the underlying studies must not be inferred from these source-method checks.

The citation-level `empirical_claim_audit=verified` for these two items means **survey-methodology statements in the cited review were checked against its own original article**, not that all underlying studies' experimental results were replicated. Keep that restriction in the `notes` field and do not transfer the status to other bibliography keys by analogy.

Generate the still-unverified citation backlog with `python3 paper/scripts/report_citation_evidence.py` (optional `--limit 25` or `--json`). This is a read-only status report; it does not promote evidence automatically. Prioritize manuscripts' claims with numerical outcomes, representation-specific editing operations and survey denominator comparisons, and read their original table/figure before changing `source_depth`.

## Two original experiment-table audits (2026-11-08)

See [T08_POSTERMELD_CREATIPOSTER_SOURCE_AUDIT.md](T08_POSTERMELD_CREATIPOSTER_SOURCE_AUDIT.md) for the exact v2 CreatiPoster and v1 PosterMELD method/results locators. These change two citation-level rows from `abstract_index` to `methods_results`; neither converts the claimed editable output format into measured protected-object editing success. A bibliographic alias revision changed CreatiPoster's eight listed authors in v2; do not reuse the previous nine-author string.

## Core technique original-source audits — 2026-11-08

The source audit of LayoutDM, LayoutFlow, and COLE is documented in [T14_CORE_LAYOUT_AND_COLE_SOURCE_AUDIT.md](T14_CORE_LAYOUT_AND_COLE_SOURCE_AUDIT.md). Their exact original table/section locators justify upgrading the three cited keys from `not_verified` to `methods_results`, without changing study-screening status. In particular, source-specific FID feature backbones, element-count filters, and training splits differ across publications; COLE's editor demonstration does not quantify non-target preservation in post-export edits. Source-based comparisons in the manuscript explicitly state these distinctions.

## T15 bounded original-source synthesis — 2026-11-08

LayoutGAN (CGD-022), PosterLayout (CGD-046), and OpenCOLE (CGD-074) have original-methods/results locators documented in [T15_LAYOUTGAN_POSTERLAYOUT_OPENCOLE_SOURCE_AUDIT.md](T15_LAYOUTGAN_POSTERLAYOUT_OPENCOLE_SOURCE_AUDIT.md). Evaluation-specific trade-offs and methodological denominators are retained; `editability_audit=not_verified` remains for all three. Native PDF screenshot requests did not succeed, so original table text was inspected without claiming image-level figure validation.

## T16 vector evidence and DOI synchronization (2026-11-08)

The original result tables of DeepSVG, SVGformer and VectorFusion were checked against the papers and documented in [T16_VECTOR_REPRESENTATION_SOURCE_AUDIT.md](T16_VECTOR_REPRESENTATION_SOURCE_AUDIT.md). Their evaluation concerns interpolation, vector reconstruction/classification/retrieval, and caption alignment, not measured post-export edit-command performance. The PosterLayout citation's DOI was added to the acro metadata to match the official CVPR DOI already added to its BibTeX entry, resolving the concrete manuscript-checker mismatch on commit `a4dd3dc`. This does not resolve unrelated figure/logo CI checks.
