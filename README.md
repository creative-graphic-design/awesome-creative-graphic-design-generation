# Awesome Creative Graphic Design Generation [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<!-- This file is generated from data/resources.csv by scripts/generate_readme.py. Do not edit it directly. -->

Curated resources for generating, editing, representing, and evaluating composed graphic-design artifacts such as posters, advertisements, social-media graphics, magazine layouts, banners, and related visual compositions.

This list focuses on work where layout, typography, visual elements, editable structure, or design-specific evaluation is a first-class part of the problem. Generic text-to-image generation and generic image editing are out of scope unless they make a direct contribution to graphic-design generation.

Research resources are ordered by **first public appearance** within each category, from oldest to newest. The sort key is the earlier of the arXiv v1 date and the venue/presentation date when both are known; journal-only work uses its first public publication date.

## Contents

- [Surveys and Overviews](#surveys-and-overviews)
- [Papers](#papers)
  - [Layout Generation](#layout-generation)
  - [Content-Aware Graphic Design](#content-aware-graphic-design)
  - [Typography and Text Rendering](#typography-and-text-rendering)
  - [Language and Multimodal Design Agents](#language-and-multimodal-design-agents)
  - [End-to-End Graphic Design Generation](#end-to-end-graphic-design-generation)
- [Datasets](#datasets)
- [Benchmarks and Evaluation](#benchmarks-and-evaluation)
- [Models and Implementations](#models-and-implementations)
- [Related Resources](#related-resources)

## Surveys and Overviews

### 2023

- [A Survey for Graphic Design Intelligence](https://arxiv.org/abs/2309.01371) - Surveys computational methods for understanding and generating graphic design artifacts (2023).
- [Intelligent Layout Generation Based on Deep Generative Models: A Comprehensive Survey](https://doi.org/10.1016/j.inffus.2023.101940) - Reviews deep generative approaches to layout generation, their representations, conditions, datasets, and evaluation (Information Fusion 2023).

### 2025

- [From Fragment to One Piece: A Survey on AI-Driven Graphic Design](https://arxiv.org/abs/2503.18641) - Reviews AI-driven graphic-design generation across layout, visual content, text, and integrated systems (2025).

## Papers

### Layout Generation

#### 2014

- [Learning Layouts for Single-Page Graphic Designs](https://doi.org/10.1109/TVCG.2014.48) - Learns layout relationships from existing single-page graphic designs to support automatic composition (TVCG 2014).

#### 2019

- [LayoutGAN](https://openreview.net/forum?id=HJxB5sRcFQ) - Introduces a GAN formulation for synthesizing layouts represented by labeled geometric elements (ICLR 2019).
- [LayoutVAE](https://arxiv.org/abs/1907.10719) - Uses a label-conditioned variational autoencoder for structured document layout generation (ICCV 2019).
- [Neural Design Network](https://arxiv.org/abs/1912.09421) - Generates graphic layouts under explicit design constraints with a neural structured model (ECCV 2020).

#### 2020

- [DeepLayout](https://arxiv.org/abs/2006.14615) - Models layouts autoregressively as sequences for conditional and unconditional generation (ICCV 2021).

#### 2021

- [LayoutGAN++](https://arxiv.org/abs/2108.00871) - Improves GAN-based layout generation with differentiable rendering and stronger geometric reasoning (ACM MM 2021).
- [CanvasVAE](https://arxiv.org/abs/2108.01249) - Uses a variational autoencoder to model element-level layouts for design documents (ICCV 2021).
- [Layout-BLT](https://arxiv.org/abs/2112.05112) - Uses bidirectional layout transformers to generate and refine object arrangements (ECCV 2022).

#### 2022

- [Coarse-to-Fine](https://ojs.aaai.org/index.php/AAAI/article/view/19994) - Generates layouts hierarchically from coarse global structure to fine element placement (AAAI 2022).
- [LayoutFormer++](https://arxiv.org/abs/2208.08037) - Treats layout generation as a sequence-to-sequence task with unified conditioning (CVPR 2023).

#### 2023

- [PLay](https://arxiv.org/abs/2301.11529) - Uses parametrically conditioned latent diffusion for controllable layout generation (ICML 2023).
- [LayoutAction](https://ojs.aaai.org/index.php/AAAI/article/view/26277) - Frames autoregressive layout generation as a sequence of placement actions (AAAI 2023).
- [DLT](https://arxiv.org/abs/2303.03755) - Applies diffusion modeling to structured layout generation (ICCV 2023).
- [LDGM](https://arxiv.org/abs/2303.05049) - Decouples discrete element attributes and continuous geometry in a diffusion model for unified layout generation (CVPR 2023).
- [LayoutDM](https://arxiv.org/abs/2303.08137) - Models layouts with discrete denoising diffusion and supports multiple conditional generation tasks (CVPR 2023).
- [LayoutDiffusion](https://arxiv.org/abs/2303.11589) - Uses discrete diffusion for controllable layout generation (ICCV 2023).
- [FlexDM](https://arxiv.org/abs/2303.18248) - Supports flexible layout generation and completion through masked multi-field diffusion (CVPR 2023).
- [Parse-Then-Place](https://arxiv.org/abs/2308.12700) - Parses textual design descriptions into structured constraints before placing graphic elements (ICCV 2023).
- [Dolfin](https://arxiv.org/abs/2310.16305) - Uses a diffusion layout transformer without an autoencoder for structured layout generation (ECCV 2024).

#### 2024

- [LACE](https://arxiv.org/abs/2402.04754) - Introduces lightweight diffusion for controllable layout generation (ICLR 2024).
- [LayoutFlow](https://arxiv.org/abs/2403.18187) - Uses flow matching for continuous structured layout generation (ECCV 2024).
- [Layout-Corrector](https://arxiv.org/abs/2409.16689) - Corrects intermediate diffusion layouts to improve structure and constraint satisfaction (ECCV 2024).

### Content-Aware Graphic Design

#### 2019

- [ContentGAN](https://doi.org/10.1145/3306346.3322971) - Generates graphic-design layouts conditioned on underlying visual content (SIGGRAPH 2019).

#### 2021

- [SmartText](https://doi.org/10.1109/TMM.2021.3097900) - Places text over natural images using saliency and learned aesthetic compatibility for harmonious poster composition (TMM 2021).

#### 2022

- [CGL-GAN](https://arxiv.org/abs/2205.00303) - Generates advertising layouts conditioned on visual content and introduces the CGL dataset (IJCAI 2022).
- [LayoutDETR](https://arxiv.org/abs/2212.09877) - Generates foreground layouts conditioned on content images for advertising design (ECCV 2024).

#### 2023

- [PosterLayout](https://arxiv.org/abs/2303.15937) - Introduces a benchmark and content-aware approach for visual-textual poster layout generation (CVPR 2023).
- [RADM](https://arxiv.org/abs/2306.09086) - Generates content-aware advertising layouts with richer text and visual conditioning (CIKM 2023).
- [AutoPoster](https://arxiv.org/abs/2308.01095) - Integrates content analysis and layout generation into an automatic advertising-poster design system (2023).
- [RALF](https://arxiv.org/abs/2311.13602) - Retrieves relevant design examples to guide content-aware layout generation (CVPR 2024).

#### 2024

- [Desigen](https://arxiv.org/abs/2403.09093) - Jointly generates advertising backgrounds and foreground element layouts (CVPR 2024).
- [Graphist](https://arxiv.org/abs/2404.14368) - Models graphic-design layouts with multimodal and structural context.
- [Visual Layout Composer](https://openaccess.thecvf.com/content/CVPR2024/html/Shabani_Visual_Layout_Composer_Image-Vector_Dual_Diffusion_Model_for_Design_Layout_CVPR_2024_paper.html) - Couples image-space and vector-space diffusion to generate design layouts conditioned on visual content (CVPR 2024).
- [CGB-DM](https://arxiv.org/abs/2407.15233) - Uses a diffusion transformer for graphic-layout generation with content-aware conditioning.
- [SciPostLayout](https://arxiv.org/abs/2407.19787) - Targets structured layout generation for scientific posters.
- [LaDeCo](https://arxiv.org/abs/2412.19712) - Generates layered and editable graphic designs rather than flattened images (CVPR 2025).

#### 2025

- [CreatiPoster](https://arxiv.org/abs/2506.10890) - Generates poster layouts from multimodal content and design requirements.
- [SEGA](https://arxiv.org/abs/2510.15749) - Uses stepwise evolution for content-aware poster layout generation and introduces GenPoster-100K (ICCV 2025).

### Typography and Text Rendering

#### 2022

- [Text2Poster](https://arxiv.org/abs/2301.02363) - Retrieves suitable imagery and places stylized text to construct poster designs from text input (ICASSP 2022).

#### 2023

- [TextDiffuser](https://arxiv.org/abs/2305.10855) - Introduces diffusion-based text rendering with explicit character-level layout guidance (NeurIPS 2023).
- [TextPainter](https://arxiv.org/abs/2308.04733) - Generates poster-oriented text imagery while balancing text comprehension and visual harmony (ACM MM 2023).
- [TextDiffuser-2](https://arxiv.org/abs/2311.16465) - Uses language-model planning to improve flexible text layout and rendering in generated images (2023).

#### 2025

- [PosterMaker](https://arxiv.org/abs/2504.06632) - Generates product posters with explicit mechanisms for accurate text rendering and visual composition (CVPR 2025).

### Language and Multimodal Design Agents

#### 2023

- [LayoutGPT](https://arxiv.org/abs/2305.15393) - Uses large language models with in-context demonstrations for layout generation (NeurIPS 2023).
- [LayoutNUWA](https://arxiv.org/abs/2309.09506) - Represents visual layouts as code for language-model-based generation and reasoning (ICLR 2024).
- [LayoutPrompter](https://arxiv.org/abs/2311.06495) - Prompts large language models for zero-shot and few-shot visual layout generation (NeurIPS 2023).

#### 2024

- [PosterLLaMA](https://arxiv.org/abs/2404.00995) - Adapts a multimodal language model to poster layout generation (ECCV 2024).
- [PosterLLaVA](https://arxiv.org/abs/2406.02884) - Uses multimodal instruction tuning for poster layout generation (IEEE TMM 2024).
- [TextLap](https://arxiv.org/abs/2410.12844) - Generates graphic layouts from textual design requirements with language-model-based reasoning.

#### 2025

- [BannerAgency](https://arxiv.org/abs/2503.11060) - Uses collaborating multimodal LLM agents to plan and generate advertising banner designs from brand assets and requests (2025).
- [PosterO](https://arxiv.org/abs/2505.07843) - Structures layouts as trees so language models can solve generalized layout-generation tasks (CVPR 2025).

### End-to-End Graphic Design Generation

#### 2023

- [COLE](https://arxiv.org/abs/2311.16974) - Uses a hierarchical generation framework to create multi-layered, editable graphic designs from high-level intent (2023).
- [Planning and Rendering](https://arxiv.org/abs/2312.08822) - Separates semantic planning from visual rendering for end-to-end product-poster generation (2023).

#### 2024

- [OpenCOLE](https://arxiv.org/abs/2406.08232) - Provides an open and reproducible pipeline for automatic layered graphic-design generation (CVPR Workshop 2024).

#### 2025

- [CreatiDesign](https://arxiv.org/abs/2505.19114) - Uses a multi-conditional diffusion transformer to compose primary visuals, decorative elements, text, and layout for graphic design.

#### 2026

- [PSDesigner](https://arxiv.org/abs/2603.25738) - Automates layered graphic-design workflows with editable PSD structure and tool-use trajectories (CVPR 2026).

## Datasets

### 2018

- [CTXFont](https://huggingface.co/datasets/creative-graphic-design/CTXFont) - Web-design screenshots with text-element boxes, font properties, and contextual metadata.

### 2019

- [Magazine](https://huggingface.co/datasets/creative-graphic-design/Magazine) - Contains fine-grained polygon layouts and semantic element labels for magazine pages.

### 2022

- [CGL Dataset](https://huggingface.co/datasets/creative-graphic-design/CGL-Dataset) - Advertising poster images, inpainted backgrounds, element categories, and bounding-box annotations.
- [LayoutDETR Dataset](https://huggingface.co/datasets/creative-graphic-design/LayoutDETR) - Advertising banners with foreground layouts and inpainted background assets.

### 2023

- [PKU PosterLayout](https://huggingface.co/datasets/creative-graphic-design/PKU-PosterLayout) - Poster images with visual-textual element boxes, saliency maps, and inpainted canvases.
- [CGL Dataset v2](https://huggingface.co/datasets/creative-graphic-design/CGL-Dataset-v2) - Poster backgrounds with text-aware element boxes, masks, and layout metadata.

### 2025

- [BannerRequest400](https://huggingface.co/datasets/creative-graphic-design/BannerRequest400) - Advertising banner requests with brand logos, multimodal design instructions, and target designs.
- [GenPoster-100K](https://huggingface.co/datasets/creative-graphic-design/GenPoster100K) - Poster data with rendered backgrounds, PSD references, and layer-level typography, color, and geometry annotations.

### 2026

- [LICA](https://huggingface.co/datasets/creative-graphic-design/LICA) - Rendered graphic designs with component-level specifications and natural-language design annotations.
- [CreativePSD](https://huggingface.co/datasets/creative-graphic-design/CreativePSD) - PSD-derived graphic designs with layer trees, source assets, tool-call trajectories, and intermediate renders.

## Benchmarks and Evaluation

### 2024

- [DesignProbe](https://arxiv.org/abs/2404.14801) - Benchmarks multimodal large language models on graphic-design understanding and reasoning tasks (2024).
- [LTSim](https://arxiv.org/abs/2407.12356) - Measures layout similarity through transportation-based matching of structured elements for layout-generation evaluation (2024).
- [Graphic Design Evaluation](https://arxiv.org/abs/2410.08885) - Evaluates alignment, overlap, white space, and related graphic-design principles with absolute and pairwise judgments (SIGGRAPH Asia 2024).

### 2026

- [AesEvalBench](https://arxiv.org/abs/2603.01083) - Evaluates graphic-design aesthetics through localized issue labels, region judgments, and vision-language-model assessments (ICLR 2026).

### Other

- [Layout FID](https://github.com/creative-graphic-design/design-generators/tree/main/models/layout-fid) - Provides a learned feature-space metric for comparing generated and real layout distributions.

## Models and Implementations

- [Creative Graphic Design Datasets](https://github.com/creative-graphic-design/huggingface-datasets) - Maintains reproducible Hugging Face loaders and dataset cards for graphic-design research datasets.
- [design-generators](https://github.com/creative-graphic-design/design-generators) - Ports layout, poster, and graphic-design generation research into consistent Transformers, Diffusers, and agent interfaces.
- [GPT Graphic Design Evaluator](https://github.com/creative-graphic-design/gpt-graphic-design-evaluator) - Implements vision-language-model-based evaluation for graphic-design outputs.
- [Graphic Design Evaluation](https://github.com/creative-graphic-design/Graphic-design-evaluation) - Provides evaluation assets and implementations for measuring graphic-design quality principles.

## Related Resources

- [Creative Graphic Design](https://github.com/creative-graphic-design) - Organization hosting datasets, model ports, evaluation tools, and research infrastructure used by several entries in this list.

## Contributing

Contributions are welcome. Please read the [contribution guidelines](CONTRIBUTING.md) before opening a pull request.
