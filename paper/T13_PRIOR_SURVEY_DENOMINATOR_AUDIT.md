# T13: primary-source denominator audit for prior graphic-design surveys

**Checked:** 2026-11-06. **Scope:** original study-selection and bibliography denominators only; not an executed retrieval/search update, bibliography inclusion decision, or new scientific approval. This is an audit of *surveys*, not a new item in the 225-study generation-paper screening queue.

## Primary source identities and locators

1. **Zou, Zhang & Zhao (2025)**, *From Fragment to One Piece: A Review on AI-Driven Graphic Design*, *Journal of Imaging* 11(9):289, DOI [10.3390/jimaging11090289](https://doi.org/10.3390/jimaging11090289). Verified original [journal HTML](https://www.mdpi.com/2313-433X/11/9/289) and [institutionally hosted 37-page journal PDF](https://ira.lib.polyu.edu.hk/bitstream/10397/117597/1/jimaging-11-00289.pdf), particularly original **p. 3, Table 1**; **p. 3–4, section 1 search-method paragraph**; and **p. 37, end of References**.
2. **Li et al. (2024)**, *The application and impact of artificial intelligence technology in graphic design: A critical interpretive synthesis*, *Heliyon* 10(21):e40037, DOI [10.1016/j.heliyon.2024.e40037](https://doi.org/10.1016/j.heliyon.2024.e40037). Verified [publisher full text](https://www.sciencedirect.com/science/article/pii/S2405844024160689) and [open-access article](https://pmc.ncbi.nlm.nih.gov/articles/PMC11570473/), especially **§2.3 Data extraction**, **Fig. 1**, **Table 2**, and the abstract.

## Three different denominators in Zou et al.

| Primary locator | Exact reported value | What it actually measures / states |
| --- | ---: | --- |
| Journal article p. 3–4, methodology paragraph | **500** | Described as the **final dataset following relevance-based inclusion/exclusion**, not an initial 500 candidates that were screened down to about 300. |
| Journal article p. 3, **Table 1**, “Ours” row, **Papers Reviewed** column | **267** | A second reported survey-size figure, with no explicit reconciliation to the 500 final-dataset statement in that table or neighboring method paragraph. |
| Journal article **References**, ending on p. 37 | **261** | The last numbered bibliographic item is **[261]**. This is a **reference count**, not an included-study count, and may contain general background, systems, duplicate versions, or other types of sources. It cannot be used to resolve the 500-versus-267 discrepancy. The bibliography also cites a **preprint version of the same survey as [253]**, illustrating why a numbered bibliography is not a clean systematic inclusion roster. |

**Audit judgment:** preserve this as a **three-way accounting ambiguity**, *not* evidence for a specific 500→267 screening funnel, a verified 261 included-study corpus, or a universal quality/coverage target. The journal text describes searching IEEE Xplore, ACM Digital Library, Scopus and Web of Science over 2000–2025 with two independent theme coders, but those statements do not supply a reconciled set of database retrieval counts, duplicate-removal counts, and per-record inclusion decisions.

## Cross-survey denominator contrast

[Li et al. (2024), §2.3](https://doi.org/10.1016/j.heliyon.2024.e40037) **explicitly distinguish 552 records identified** from **33 studies ultimately included** after title/abstract and full-text screening; they provide a screening diagram (Fig. 1) and an included-study list (Table 2, `n=33`). Their broader critical-interpretive-synthesis objective, time window (2010–October 2023), research questions and selection criteria differ from both Zou et al. and our generation/editability survey. Thus **552 and 33 are different pipeline stages**, not conflicting estimates of one denominator, and comparing our corpus size directly with either would be misleading.

## Implications for the present manuscript

- Existing [related-surveys prose](sections/03_related_surveys.tex) **already** says Zou reports 500 in its methodology and 267 in its comparison table and does not equate them. This is correct and **needs no forced numerical amendment** merely because the bibliography has 261 numbered references.
- The present **225 stable working-study IDs**, **202 BibTeX works** and **198 registered `acro` terms** are distinct inventory/identity/terminology sets. In particular, a bibliography count or `acro` term count is **not** the number of systematically included studies.
- Before drawing a PRISMA-like diagram or claiming systematic completeness, the project must log **query, database, timestamp, raw retrieved identifiers, duplicates, title/abstract decisions, full-text decisions, inclusion/exclusion reasons and adjudication**. Keep the prospective [review protocol](REVIEW_PROTOCOL.md) explicit until that work is executed.
- For future prior-survey comparison tables, report **denominator label** next to every count (retrieved / screened / included / referenced) instead of simply “papers reviewed.” Under an internal contradiction, use **not reconciled** rather than picking the larger or smaller number.
- **No update made** here to the live Google Sheet, 225-ID snapshot, source evidence tiers, bibliographic identity mappings, `references.bib`, `acro`, TeX narrative or research maps. This note is evidence for the author's T13 methodology review, not author approval to start the gated T07 study.

## Source-verification boundary

The original journal HTML and extracted numbered PDF references were available for checking the stated figures and locators; a direct web-PDF page screenshot request did not return an image, so no new PDF-image inspection is claimed. The source-register [Google Sheet](https://docs.google.com/spreadsheets/d/1PJtvX34FYoOnF8LS4-0WHpiR3B_KQ6n5fqRBtTeF3Zc/edit) was re-opened read-only and its **Evidence Matrix 225**, **225 Citation and R-E-V Coverage**, **225 Source Tier Reconciliation**, and **Prior Survey and Screening** headers/first rows were checked; the latter already records 500 as a claimed final selection count and notes that 500→300 is unsupported.
