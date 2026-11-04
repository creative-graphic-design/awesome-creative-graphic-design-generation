# T02 / CGD-092 — TKG-DM primary-source audit

Reviewed 2026-11-05 JST. This is an **original-methods/results review**, not an independent replication or exhaustive supplementary-material audit.

## Identity and provenance

- Live spreadsheet: **Evidence Matrix 225, row 93**, plus the **225 Citation and R-E-V Coverage**, **225 Source Tier Reconciliation**, and **Prior Survey and Screening** tabs.
- Ryugo Morita, Stanislav Frolov, Brian Bernhard Moser, Takahiro Shirakawa, Ko Watanabe, Andreas Dengel, and Jinjia Zhou: **TKG-DM: Training-free Chroma Key Content Generation Diffusion Model**.
- CVPR **2025**, pp. 13031–13040; DOI **10.1109/CVPR52734.2025.01216**.
- Original methods/results HTML: https://arxiv.org/html/2411.15580 ; official proceedings: https://openaccess.thecvf.com/content/CVPR2025/html/Morita_TKG-DM_Training-free_Chroma_Key_Content_Generation_Diffusion_Model_CVPR_2025_paper.html
- First preprint published **2024-11-23**; the 2025 CVPR venue and 2024 arXiv release refer to **one contribution**.
- Project repository referenced by the spreadsheet: https://github.com/ryugo417/TKG-DM

## Method, representation and editing boundary

Sections 3.1–3.2 and Figure 2 describe a **training-free channel-wise mean shift** of diffusion's initial noise, combined with a Gaussian spatial mask to control foreground object placement and the monochromatic keyed background.
The deliverable is a **rendered RGB image with chroma-key background** which can later be matted or composited; the study does not claim a native SVG, DOM, PSD or editable text/object tree.
Section 6 and Figure 10 demonstrate generation-time position/size control and multiple foreground objects, not a quantitative post-export design-edit benchmark.

## Evidence inspected

| Original locator | Result / observation | Interpretation |
|---|---|---|
| §5.1 | SD1.5 and SDXL setups, 50 denoising steps, fine-tuned and prompting comparisons | Generation settings, not native editing |
| §5.2 | 3,000 MAGICK-derived images; FID, m-FID (foreground-mask based), CLIP-I/CLIP-S | Evaluates rendered-image quality, extracted masks and semantic alignment |
| Table 1, SD1.5 | TKG-DM FID **56.32**, m-FID **40.75** vs GB LoRA **60.29** and **49.03** | Improvement in this setting does not establish general superiority |
| **Table 1, SDXL** | TKG-DM FID **41.81**, m-FID **31.43**, CLIP-I **0.763**, CLIP-S **0.273** vs LayerDiffuse **29.34**, **29.82**, **0.778**, **0.276** | **LayerDiffuse is stronger on all four reported metrics for this particular comparison** |
| §5.5, Figure 8 | 100 participants in a two-alternative preference evaluation | Foreground quality/text relevance, **not** semantic edit success |
| §6, Figure 10 | Mask-controlled object location and size, multiple masks; other generation applications | Conditional asset creation is not document-edit validity |
| §7, Figure 11 | Failure to create a foreground for overly small masks or missing object description | Keep limitations visible |

No new claim of independent replication, method robustness over all prompts, complete supplementary verification, human edit-time measurement or semantic object preservation is made.

## Decision and synchronization

**Include** as a source-grounded chroma-key asset-generation contribution relevant to the boundary between composition affordance and editing performance.
Citation audit sets `source_depth=methods_results`, `empirical_claim_audit=verified`, `representation_audit=verified`, `evaluation_audit=verified`, but leaves **`editability_audit=not_verified`**.
Added `tkgdm2025` and source-linked `tkgdm`, updated original scientific comparison prose and both identity crosswalks.
The **225** frozen study records are unchanged; the new state is **198 BibTeX references / 189 acro terms / 169 linked studies / 56 pending (6 P1, 13 P2, 37 P3)**.
An additional negative unit test now corrupts TKG-DM's arXiv/publication identity and verifies that the check fails.
Next individual review: **T03 / CGD-159 / Alfie** after PDF inspection and author feedback.

## Compiled-PDF verification (2026-11-05)

The original scientific-source commit `aa9579f80a71700eeff58817a361775909f033c3` passed **Paper PDF**, **Catalog Check**, and **Awesome Lint**: [Paper PDF run #41857746475](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/runs/41857746475), artifact ID **13339058432** (the artifact name uses the CI test-merge SHA `ca1cabe08bf759c8e93715968f83620722dec331`).
I downloaded and inspected the actual **29-page anonymous-review PDF**, checking the TKG-DM synthesis/evaluation discussion on **pp. 11–12**, its source-linked `acro` entry on **p. 21**, bibliography entry on **p. 26**, and the narrative-map embedding on **p. 3**.
I also rendered the standalone **26-study narrative map** and **67-study detailed atlas** and inspected their labels and boundaries.
On the pages inspected, I found no visible collisions or clipped text; the final LaTeX log did not report undefined citations/references or overfull/underfull boxes.
This is a **targeted visual QA**, not a page-by-page inspection of all 29 pages or a new experiment replication.
Author scientific approval of this interpretation is **still pending**; do not start T03 as though this is an author sign-off.
