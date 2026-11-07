# Original institution marks in individual research nodes (T16)

**Figure-design contract (2026-11-07):** place the institution identity mark **inside the corresponding study card**, beside the paper name and citation year. Do not create a detached, footnote-like "Affiliation provenance" strip. All enabled marks occupy an identical **0.46 cm × 0.46 cm square layout slot**, with `keepaspectratio` (no stretching, recoloring or invented redraws). If no suitable square icon exists, keep that institution as plain text in the provenance registry; do not squeeze a horizontal wordmark into the card.

The current author-drawn narrative map uses only two prototype marks for factual study identification:

| Study node | Mark | Vector artifact | Source / verification | Publication status |
| --- | --- | --- | --- | --- |
| OpenCOLE (2024) | CyberAgent independent **CA symbol** (not horizontal wordmark) | `cyberagent-symbol.pdf` | [2015 original combined SVG](https://commons.wikimedia.org/wiki/File:CyberAgent_logo.svg), SHA-1 `6e364a261c7cfc57a6f434fee0aeff3fb1184a88`; source PDF's intact left-hand CA mark clipped without distorting or redrawing into a **57 bp square vector canvas** (trimmed before the black wordmark begins) using `cyberagent-symbol.tex` | **Draft only**; corporate trademark review open |
| COLE (2023) | Peking University **square seal** | `pku.pdf` | [Original-VIS-derived SVG](https://commons.wikimedia.org/wiki/File:Peking_University_seal.svg), actual downloaded SVG SHA-1 `14ffd592f63fb7231f71639e37b586467be667ea` (35,658 bytes) | **Draft only**; university emblem reuse review open |

No original company/university binaries are checked into Git. The CI runner downloads only the two enabled SVGs, verifies their exact byte hashes, converts them to vector PDFs, and derives the square CA preview with `pdflatex`. **The crop affects only the viewport around the CA symbol, not its paths or colors.** A separate symbol file is also listed by [CompaniesLogo](https://companieslogo.com/cyberagent/logo/), but this build deliberately avoids depending on that third-party download and retains a cryptographically pinned original.

Other institution affiliations are source-indexed but their logo assets are **not enabled**:

- LayoutGAN (2019): Beijing Institute of Technology and Adobe. Adobe's [brand policy](https://www.adobe.com/legal/permissions/trademarks.html) requires permissions to reproduce the logo, and the [BIT identity guidance](https://www.bit.edu.cn/gbxxgk/dqgz_sjb/vixx/bzxhgf/index.htm) needs further use review.
- COLE (2023): Microsoft Research Asia. The dated original square/compact mark and use terms have not yet been verified.
- Berkeley's primary logo, if needed in a later study, is [permission-restricted](https://brand.berkeley.edu/downloads/brand-essentials-toolkit/).

Provenance and per-institution decisions are recorded in [logo_asset_candidates.csv](../../tex/logo_asset_candidates.csv) and [affiliation_logo_provenance.csv](../../tex/affiliation_logo_provenance.csv).

## Implementation and acceptance

1. Verify the exact *original-paper author* affiliation (not just project sponsorship), publication-year-appropriate identity mark, authoritative vector source and copyright/trademark permission context.
2. Prefer an **authentic symbol/seal variant with an approximately 1:1 bounding box**. Do not use horizontal wordmarks, rasterized screenshots, stretched/cropped arbitrary text, or manually redrawn lookalikes.
3. Pin the upstream bytes. For CA, `cyberagent-symbol.tex` uses a square canvas around the original CA symbol; if the official identity changes, re-audit its glyph boundary instead of silently reusing the crop.
4. Add the new identity to the corresponding `\MapPaperBrand` study node, not an unrelated caption/footer. Keep the node name and year readable. Keep all other study nodes untouched.
5. Run `python3 paper/scripts/check_manuscript.py` and `cd paper && make pdf`, extract the **actual** generated vector map and check at manuscript print size for overlaps and small unreadable marks.
6. Before final publication, independently review authorization, university insignia law, trademark/nominative identification, attribution, and non-endorsement. Commons `PD-textlogo` or public-domain copyright status **does not** grant trademark permissions.

**Non-endorsement:** marks, if validly used, identify the affiliated author organizations of individual studies; they do not endorse the survey or other listed papers. The current two marks are **provisional review-draft prototypes**, not permission sign-off.
