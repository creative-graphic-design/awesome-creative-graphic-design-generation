# T18 IconShop original source audit — 2026-11-08

- Original [IconShop arXiv manuscript](https://arxiv.org/pdf/2304.14400) is 13 pages; original §§3.2–3.4, 4.1–4.3 and Tables 1–2 were checked against extracted full paper text. I requested the PDF page screenshot, but the server returned a cache miss; no claim of visually seeing Table 2's page.
- Architecture: tokenizes SVG icons by flattening layered paths into sequences of MoveTo (M), LineTo (L), and Cubic Bézier (C) commands with a begin-of-path delimiter; trains an autoregressive transformer and supports fill-in-the-middle masking for qualitative icon editing (source §§3.2–3.3).
- Data (§4.1): based on FIGR-8-SVG 1.5 million monochrome icons, filters to about 1.1 million eligible sequences, selects 300,000 icons for experiments, uses 90/5/5 split, evaluates 20,000 unconditional / 7,000 conditional samples.
- **Text-conditioned Table 2(b)**: IconShop FID **4.65**, DeepSVG+GAN **12.01**, BERT **35.10** (lower better); CLIP score **25.74** versus **21.78** / **22.03** (higher better). But uniqueness is **68.29%** versus DeepSVG+GAN **97.59%** (lower) and novelty **68.60%** versus **99.01%** (lower). An unqualified “better on every metric” claim is false.
- Its “FID” relies on **CLIP encoder features**, not standard Inception embeddings; this must not be numerically conflated with natural-image FID or separate layout-FID networks.
- Qualitative icon completion and editing do not constitute a measured arbitrary professional graphic-document editing benchmark, and no native editor reopen-save transaction was independently tested.
- Citation-level audit upgraded only for these bounded original methods/results, while `editability_audit=not_verified` and scientific adjudication remain pending.
