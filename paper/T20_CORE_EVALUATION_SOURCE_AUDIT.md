# T20 original foundational and editing benchmark evidence — 2026-11-08

## `svgeditbench2024`

Depth: `methods_results`, editing operation audit: `verified`.

Source locus: Original CVPR Workshops PDF https://openaccess.thecvf.com/content/CVPR2024W/GDUG/papers/Nishina_SVGEditBench_A_Benchmark_Dataset_for_Quantitative_Assessment_of_LLMs_SVG_CVPRW_2024_paper.pdf Sections 3.2-4.2, Table 1.

Original 100 Twemoji SVG graphics x six edit tasks, 600 prompts/model. Original Table1 GPT-4/GPT-3.5 Change Color MSE 6.88e-5/0.0134; Compression MSE 0.0071/0.0023 with code length ratios 94.5%/96.1%. Failed or multiple SVG responses excluded from conditional averages. XML attribute/code editing tested, not general native document editing. Original PDF text table inspected but screenshot unavailable.

## `cglgan2022`

Depth: `methods_results`, editing operation audit: `not_verified`.

Source locus: Original IJCAI 2022 PDF https://www.ijcai.org/proceedings/2022/0692.pdf Sections 3-6, Tables 1-3.

Original full paper methods/results examined: 60,548 annotated advertising posters; 5 professional and 20 novice designers on 60 images; Table1 CGL-GAN vs ContentGAN subject occlusion 0.816/1.143, visual complexity 34.01/45.59, but alignment 0.0098/0.0071 (worse). Bounding-box composition not native editing. PDF textual extraction checked but screenshot unavailable.

## `layoutdiffusion2023`

Depth: `methods_results`, editing operation audit: `not_verified`.

Source locus: Original ICCV 2023 PDF https://openaccess.thecvf.com/content/ICCV2023/papers/Zhang_LayoutDiffusion_Improving_Graphic_Layout_Generation_by_Discrete_Diffusion_Probabilistic_Models_ICCV_2023_paper.pdf Sections 4.1-5.4, Tables 1-3.

Original ICCV methods/results inspected. Discrete type/coordinate token diffusion with plug-and-play conditional geometry generation. Table2 RICO unconditional FID 2.490 versus 3.174 for uniform coordinate noise; FID uses layout feature encoder rather than image Inception features. Original ICCV Table1 covers Rico/PubLayNet datasets with metric-specific tradeoffs. Native semantic document editing not measured. PDF screenshot unavailable.

## `yang2026infoedit`

Depth: `abstract_index`, editing operation audit: `not_verified`.

Source locus: https://aclanthology.org/2026.emnlp-main.2513/ original EMNLP 2026 publisher abstract and publication metadata.

Primary original ACL Anthology publisher abstract checked: 1000 infographics, eight logical-relation families, 4000 instructions/four tasks, reflow-aware scoring. Authors report GPT-Image-2 >60% average and no editor >36% on Swap-Block; detailed original experimental tables and appendices not inspected, so remains abstract-level; no independently verified per-task success claims.

## `mildedit2026`

Depth: `abstract_index`, editing operation audit: `not_verified`.

Source locus: https://arxiv.org/html/2601.04589 original author abstract and Figure 1; full methods/results inaccessible from retrieved HTML.

Primary original author abstract checked: >20k layered-document examples, four evaluation dimensions (instruction following, layout consistency, aesthetics, text rendering), 14 open and 2 closed models. Main result numeric tables uninspected, so remains abstract-level and no independent edit success or native file round-trip claimed.

No independent model replication, per-source visual PDF screenshot inspection or complete systematic screening is implied.
