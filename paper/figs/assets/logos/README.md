# Original university/company marks for the narrative research map

**Status (2026-11-07): One original CyberAgent textlogo is enabled for an anonymous draft preview; it is not publication-approved.** No official mark binary is checked into the repository. When the logo is enabled, `scripts/prepare_affiliation_logos.sh` downloads the 2016 Commons SVG, verifies SHA-1 `6e364a261c7cfc57a6f434fee0aeff3fb1184a88`, and converts it to a vector PDF for the figure. All four other institution slots remain text-only. The map retains source-checked institution names. This directory is the reserved asset location for the author's T16 request; see [candidate rights table](../../tex/logo_asset_candidates.csv) and [affiliation evidence](../../tex/affiliation_logo_provenance.csv).

The vector-only, source-editable TikZ figure at [research_map_narrative.tex](../../tex/research_map_narrative.tex) has **five explicit rights-gated institution slots** tied to three research cases:

- LayoutGAN (2019): Beijing Institute of Technology (`bit.pdf`) and Adobe (`adobe.pdf`).
- COLE (2023): Microsoft Research Asia (`msra.pdf`) and Peking University (`pku.pdf`).
- OpenCOLE (2024): CyberAgent (`cyberagent.pdf`).

Files are not distributed merely because an external site shows a downloadable logo. For each institution, independently check the **paper-date author affiliation**, authoritative asset/version, copyright and trademark/identity restrictions, permitted context, attribution, and whether use would wrongly suggest endorsement. **Do not draw, recolor, alter, approximate, or scrape a mark in its place.** A Commons `PD-textlogo` claim is not a corporate trademark license.

## Current reviewed examples

- **Adobe:** [official trademark policy](https://www.adobe.com/legal/permissions/trademarks.html) requires a specific license/authorization for Adobe logos. **Blocked pending permission**; a 2020 Commons logo is also not evidence of a 2019 affiliation-time mark.
- **Peking University:** [official visual identity downloads](https://vim.pku.edu.cn/xzzq/) also list noncommercial-use application and undertaking forms. **Do not assume permission from download availability.**
- **Beijing Institute of Technology:** [official identity/mark specification](https://www.bit.edu.cn/gbxxgk/dqgz_sjb/vixx/bzxhgf/index.htm) provides usage rules; rights for third-party scholarly reuse are not yet cleared.
- **UC Berkeley (future node):** [official asset toolkit](https://brand.berkeley.edu/downloads/brand-essentials-toolkit/) states that the primary logo is available only in limited instances with permission.
- **CyberAgent:** [historically relevant 2015 brand SVG](https://commons.wikimedia.org/wiki/File:CyberAgent_logo.svg) is indexed as `PD-textlogo` by Commons but remains trademarked. The current **draft-only figure preview** uses the unaltered SHA-1-pinned SVG solely as a factual OpenCOLE affiliation identifier. This is **not corporate authorization or a final publication-rights decision**; the author must review its publication context.

## Integration and reproducibility

1. Record authorization/approved nominative usage and attribution in `paper/figs/tex/logo_asset_candidates.csv` as `status=cleared_for_scholarly_use`. Keep a link to the specific authority and original asset.
2. Add the **unaltered** approved original vector PDF to `paper/figs/assets/logos/<stem>.pdf`; keep original SVG (if permitted by distribution terms) as an editable companion `<stem>.svg`. The PDF should be a faithful vector conversion, not a bitmap screenshot, with no asset format change altering colors or proportions.
3. Change **only that institution's** `\\AffilBrand{0}{stem}{.21cm}{label}` call to `\\AffilBrand{1}{stem}{.21cm}{label}`. The manuscript linter will fail if an unapproved or missing logo PDF is enabled.
4. Run `python3 paper/scripts/check_manuscript.py`, `cd paper && make pdf`, inspect the compiled 26-node map at full manuscript print width, both maps and the anonymous PDF; verify no clipping, unintended logo substitutions, endorsement impression, or attribution omissions. Update the figure caption only for marks actually incorporated.

**Non-endorsement:** organization marks (when authorized) identify the author affiliations of individual works. They do not imply institutional endorsement of this survey or the other papers.
