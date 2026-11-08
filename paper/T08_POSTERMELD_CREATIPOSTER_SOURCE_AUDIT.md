# Focused primary-source audit: CreatiPoster and PosterMELD (2026-11-08)

These are **selected original methods/results and table checks**, not independent replication, complete supplement review, native-editor execution, systematic study screening, or author science approval.

## CreatiPoster — CGD-038

- Canonical preprint ID: [arXiv:2506.10890](https://arxiv.org/abs/2506.10890). The inspected [v2 HTML](https://arxiv.org/html/2506.10890) identifies eight authors: Dexiang Hong, Zhao Zhang, Weidong Chen, Yutao Cheng, Maoke Yang, Gonglei Shi, Hui Zhang, Zhendong Mao. The bibliography previously used a differing nine-person author list drawn from the earlier description and was corrected to the verified v2 authors. Year 2025 denotes the first preprint, not the inspected v2 revision date (2026-07-22).
- Original §3.1 and Eqs. (1–4): ordered JSON text/asset layer protocol and background-caption output; RGBA foreground is rendered separately from the generated background. §3.4/Table 1: prompt, asset, partial-canvas and re-layout modes, including specified locked layers. These are **supported system functions** in the inspected source; their existence is not a downstream editing benchmark.
- Original §4.2: 45 prompt-only, 39 single-asset and six multi-asset test cases. Four GPT-4.1 quality dimensions and ten human volunteer ratings are separate constructs.
- Original §4.3/Table 3: prompt-only human mean 2.80 for CreatiPoster-S versus 2.33 for Canva. Original §4.3/Table 4: asset-conditioned human mean 2.82 versus 2.33; **Canva layout 2.84 exceeds CreatiPoster-S layout 2.41**. Do not claim a clean sweep.
- The authors say the asset-conditioned comparison covers 84 of 90 cases because the six multiple-asset cases are unsupported by the baselines. Their quantitative visual quality results do not score held-out edit requests, preserved objects after unrelated edits, or reopened native exports. Supplement not comprehensively read.

## PosterMELD — CGD-122

- Canonical preprint: [arXiv:2608.02218v1](https://arxiv.org/html/2608.02218). Original §3 describes a template-conditioned pipeline returning an editable PPTX and PNG for accepted poster requests, and controlling templates, density and style.
- Original §4 (Benchmark and Evaluation) and Table 1: **621 requested papers**, including unsuccessful requests in the denominator; Print-Ready Rate (PRR) 81.3% for PosterMELD, 24.2% P2P, 15.8% PosterGen, 85.2% GPT-Image-2, 82.8% Codex+Skill.
- Original §4 Table 1: reported conditional CHE 3.247 and per-request mean cost USD 0.38. The non-editable GPT-Image-2 image baseline has a higher PRR; this is a trade-off rather than an unqualified system ranking.
- Original §4 Table 3: a frozen GPT-5.5 VLM judge with accuracy 0.840 and Cohen's kappa 0.683 against human print-ready labels. Universal gives zero for missing generations; BERTScore is conditional on successful generations. Do not pool their denominators with CHE or PRR.
- Native editability is assessed as availability of text/figure elements by the authors, not by our own PPTX reopen-and-edit test; no quantitative held-out semantic edit request success is established by this inspected section. Baseline models are not identical across all methods (Codex+Skill uses a different model).

## Editorial decision boundary

Both bibliographic identities remain linked and **editorial decisions remain pending**. The per-citation `source_depth` is raised from `abstract_index` to `methods_results` for these two **bounded inspected methods, result tables, and output claims**, with empirical/representation/evaluation checks verified only for those specific statements. The `editability_audit` remains `not_verified` because independent edit-operation scoring and native-file round-trip evidence were not confirmed. Neither study is declared globally superior across editability, generation quality, or print readiness.
