# Original source audits: LayoutDM, LayoutFlow and COLE — 2026-11-08

This is a bounded direct inspection of original primary paper methods and results. It is not a replication, independent editor/format round-trip test, author approval, or systematic screening decision.

## LayoutDM (Inoue et al., CVPR 2023; CGD-019)

Original [CVPR open-access PDF](https://openaccess.thecvf.com/content/CVPR2023/papers/Inoue_LayoutDM_Discrete_Diffusion_Model_for_Controllable_Layout_Generation_CVPR_2023_paper.pdf), §§3.2–3.4, 4.1–4.5, Tables 1–4, Fig. 3. **The actual PDF page containing Table 1 was visually inspected**, not just its extracted text. The experiment distinguishes category-conditioned generation, completion, refinement and relational constraints. Results are for ordered boxes: element category/size/position, not editable image assets or semantic text nodes.

Original Table 1, Rico category→size+position: LayoutDM FID **3.55**, BART **3.97**, LayoutGAN++ **6.84**. But completion Rico LayoutDM **9.00**, LayoutTrans **3.71**. The paper explicitly warns against comparing already-published results across incompatible train/test splits or FID feature backbones. Rico split **35,851/2,109/4,218** and PubLayNet **315,757/16,619/11,142**, maximum 25 elements, three trials.

## LayoutFlow (Guerreiro et al., ECCV 2024; CGD-020)

Original [arXiv source HTML](https://arxiv.org/html/2403.18187), §§4–5 and Appendices 0.D–0.F, Tables 1–2, 9–11. Main matched-split experimental data use Rico and PubLayNet with **at most 20 elements**; source reports a separate 25-element split in Appendix 0.E, with retrained LayoutDM and DLT when necessary. Euler flow integration uses 100 steps.

Original Table 1 unconditional: Rico FID LayoutFlow **2.37** versus LayoutDiffusion **2.49**, but PubLayNet FID **8.87** versus **8.63** and Rico alignment **0.150** versus **0.069**. Original Table 2 completion: Rico FID **1.51** versus retrained LayoutDM **6.80**; Rico alignment **0.150** versus LayoutDM **0.054**, a further adverse metric.

These are matched-split comparisons **within the LayoutFlow paper**, not values that may be placed directly alongside LayoutDM's different preprocessing in the earlier CVPR paper.

## COLE (Jia et al., arXiv 2023 / v2 March 2024; CGD-062)

Original [arXiv v2 HTML](https://arxiv.org/html/2311.16974), §§3–4, Tables 1 and 3, Figs. 3, 9–11. The hierarchy maps natural-language intention to JSON and to separate background/object images and typography parameters. Section 3.6 uses SVG-Edit to compile layers to a single SVG and Justinmind for repositioning, resizing and typographic attribute edits. This is more than raster-only style-transfer, **but** it is a qualitative workflow demonstration, not tested arbitrary user instruction edits with non-target protections.

DesignerIntention comprises approximately 500 category prompts plus about 50 creative examples. The paper reports about 20 general participants and six designers. Original Table 1's author-reported GPT-4V layout metric: COLE **80.82** vs DALL-E 3 **80.29**; innovation **88.72** vs DALL-E 3 **90.61**, favoring the latter. Crello text placement Table 3 reports SingleText IoU **40.2**, MultiText IoU **17.2** for COLE's typography component. Original §4.2 openly acknowledges typography arrangement, limited number of editable visual elements, and limited color diversity as remaining problems.

## Review gates

For all three, `source_depth=methods_results` and the representation/empirical/evaluation claims recorded here are supported by inspected original sections or tables. `editability_audit=not_verified` remains because held-out post-export edit success and independent native-file round-trip checks were not demonstrated in this audit. `adjudication_status=pending` remains pending scientific author approval.

No claim is made that two FIDs from differing train/test splits are comparable, that FID alone measures overall layout quality, or that qualitative editor illustrations establish benchmarked edit reliability.
