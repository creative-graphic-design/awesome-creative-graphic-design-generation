# Awesome Creative Graphic Design Generation [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<!-- This file is generated from data/*.csv by scripts/generate_readme.py. Do not edit it directly. -->

Curated resources for generating, editing, representing, and evaluating composed graphic-design artifacts such as posters, advertisements, social-media graphics, magazine layouts, scientific posters, slides, banners, and related visual compositions.

This list focuses on work where layout, typography, visual elements, editable structure, or design-specific evaluation is a first-class part of the problem. Generic text-to-image generation and generic image editing are out of scope unless they make a direct contribution to graphic-design generation.

Research resources are ordered by **first public appearance** within each category, from newest to oldest. The sort key is the earlier of the arXiv v1 date and the venue/presentation date when both are known; journal-only work uses its first public publication date.

Implementation metadata is tracked separately in [`data/paper_metadata.csv`](data/paper_metadata.csv). Verified entries expose project pages, official code and weight-release status, method/base model, training and evaluation datasets, output representation, and the date the release status was last checked.

## Contents

- [Surveys and Overviews](#surveys-and-overviews)
- [Papers](#papers)
  - [Layout Generation](#layout-generation)
  - [Content-Aware Layout Generation](#content-aware-layout-generation)
  - [Graphic Design Generation](#graphic-design-generation)
  - [Typography and Text Rendering](#typography-and-text-rendering)
  - [Graphic Design Editing and Reconstruction](#graphic-design-editing-and-reconstruction)
  - [Scientific Poster and Slide Generation](#scientific-poster-and-slide-generation)
- [Datasets](#datasets)
- [Benchmarks and Evaluation](#benchmarks-and-evaluation)
- [Models and Implementations](#models-and-implementations)
- [Relevant Venues and Journals](#relevant-venues-and-journals)
  - [Conferences](#conferences)
  - [Journals](#journals)
- [Related Resources](#related-resources)

## Surveys and Overviews

### 2025

- [From Fragment to One Piece: A Survey on AI-Driven Graphic Design](https://arxiv.org/abs/2503.18641) - Reviews AI-driven graphic-design generation across layout, visual content, text, and integrated systems (2025).

### 2023

- [Intelligent Layout Generation Based on Deep Generative Models: A Comprehensive Survey](https://doi.org/10.1016/j.inffus.2023.101940) - Reviews deep generative approaches to layout generation, their representations, conditions, datasets, and evaluation (Information Fusion 2023).
- [A Survey for Graphic Design Intelligence](https://arxiv.org/abs/2309.01371) - Surveys computational methods for understanding and generating graphic design artifacts (2023).

## Papers

Papers are classified by their **primary output and task**, rather than by model family. LLM-, VLM-, diffusion-, and agent-based approaches can therefore appear in any category.

- **Layout Generation** outputs structured element geometry or arrangement without relying on the visual content of a target canvas.
- **Content-Aware Layout Generation** still outputs layout or placement, but conditions that geometry on a background image, product/brand assets, saliency, element content, or another visual canvas.
- **Graphic Design Generation** goes beyond geometry to create a composed design artifact, such as backgrounds, imagery, typography, styles, layers, or editable HTML/CSS/PSD/PPTX structures.
- **Typography and Text Rendering** focuses primarily on legible, faithful, or stylized text generation and placement within designed imagery.
- **Graphic Design Editing and Reconstruction** focuses on iterative editing, layer recovery, or conversion of rendered designs back into editable structures.
- **Scientific Poster and Slide Generation** covers research communication workflows that combine source-document understanding, content selection, layout, typography, rendering, and often editable output.

### Layout Generation

#### 2026

- [i-Design](https://link.springer.com/chapter/10.1007/978-3-032-14826-1_18) - Optimizes graphic layout design step by step with progressive aesthetic policy optimization (ECCV 2026).

#### 2025

- [PosterO](https://arxiv.org/abs/2505.07843) - Structures layouts as trees so language models can solve generalized layout-generation tasks (CVPR 2025).
- [TextLap](https://arxiv.org/abs/2410.12844) - Generates graphic layouts from textual design requirements with language-model-based reasoning.

#### 2024

- [Layout-Corrector](https://arxiv.org/abs/2409.16689) - Corrects intermediate diffusion layouts to improve structure and constraint satisfaction (ECCV 2024).
- [LayoutFlow](https://arxiv.org/abs/2403.18187) - Uses flow matching for continuous structured layout generation (ECCV 2024). Project: — · [Code](https://github.com/JulianGuerreiro/LayoutFlow) (`training + inference`) · [Weights](https://huggingface.co/JulianGuerreiro/LayoutFlow) (`released`).<br>  **Method:** Flow-matching model for continuous layout generation · **Base:** Transformer-style layout backbone · **Train:** RICO; PubLayNet · **Eval:** RICO; PubLayNet · **Output:** Structured layout boxes · **Checked:** 2026-10-06.
- [LACE](https://arxiv.org/abs/2402.04754) - Introduces lightweight diffusion for controllable layout generation (ICLR 2024).

#### 2023

- [LayoutPrompter](https://arxiv.org/abs/2311.06495) - Prompts large language models for zero-shot and few-shot visual layout generation (NeurIPS 2023). Project: — · [Code](https://github.com/microsoft/LayoutGeneration/tree/main/LayoutPrompter) (`pipeline`) · Weights: `n/a`.<br>  **Method:** Training-free in-context LLM layout prompting · **Base:** GPT-family API models · **Train:** None · **Eval:** RICO; PubLayNet; PKU PosterLayout; WebUI · **Output:** Structured layout boxes · **Checked:** 2026-10-06.
- [Dolfin](https://arxiv.org/abs/2310.16305) - Uses a diffusion layout transformer without an autoencoder for structured layout generation (ECCV 2024).
- [LayoutNUWA](https://arxiv.org/abs/2309.09506) - Represents visual layouts as code for language-model-based generation and reasoning (ICLR 2024). Project: — · [Code](https://github.com/ProjectNUWA/LayoutNUWA) (`training + inference`) · Weights: `unknown`.<br>  **Method:** Code-generation formulation for layout generation · **Base:** LLaMA2-7B; CodeLLaMA-7B · **Train:** RICO; PubLayNet; Magazine · **Eval:** RICO; PubLayNet; Magazine · **Output:** HTML/code-form layout representation · **Checked:** 2026-10-06.
- [Parse-Then-Place](https://arxiv.org/abs/2308.12700) - Parses textual design descriptions into structured constraints before placing graphic elements (ICCV 2023).
- [LayoutGPT](https://arxiv.org/abs/2305.15393) - Uses large language models with in-context demonstrations for layout generation (NeurIPS 2023).
- [FlexDM](https://arxiv.org/abs/2303.18248) - Supports flexible layout generation and completion through masked multi-field diffusion (CVPR 2023).
- [LayoutDiffusion](https://arxiv.org/abs/2303.11589) - Uses discrete diffusion for controllable layout generation (ICCV 2023).
- [LayoutDM](https://arxiv.org/abs/2303.08137) - Models layouts with discrete denoising diffusion and supports multiple conditional generation tasks (CVPR 2023). [Project](https://cyberagentailab.github.io/layout-dm) · [Code](https://github.com/CyberAgentAILab/layout-dm) (`training + inference`) · [Weights](https://github.com/CyberAgentAILab/layout-dm/releases/tag/v1.0.0) (`released`).<br>  **Method:** Discrete diffusion model for controllable layout generation · **Base:** Transformer-style discrete denoiser · **Train:** RICO; PubLayNet · **Eval:** RICO; PubLayNet · **Output:** Structured layout boxes · **Checked:** 2026-10-06.
- [LDGM](https://arxiv.org/abs/2303.05049) - Decouples discrete element attributes and continuous geometry in a diffusion model for unified layout generation (CVPR 2023).
- [DLT](https://arxiv.org/abs/2303.03755) - Applies diffusion modeling to structured layout generation (ICCV 2023).
- [LayoutAction](https://ojs.aaai.org/index.php/AAAI/article/view/26277) - Frames autoregressive layout generation as a sequence of placement actions (AAAI 2023).
- [PLay](https://arxiv.org/abs/2301.11529) - Uses parametrically conditioned latent diffusion for controllable layout generation (ICML 2023).
#### 2022

- [LayoutFormer++](https://arxiv.org/abs/2208.08037) - Treats layout generation as a sequence-to-sequence task with unified conditioning (CVPR 2023). Project: — · [Code](https://github.com/microsoft/LayoutGeneration/tree/main/LayoutFormer%2B%2B) (`training + inference`) · [Weights](https://huggingface.co/jzy124/LayoutFormer) (`released`).<br>  **Method:** Conditional sequence-to-sequence layout generation · **Base:** Transformer encoder-decoder · **Train:** RICO; PubLayNet · **Eval:** RICO; PubLayNet · **Output:** Serialized/discretized layout boxes · **Checked:** 2026-10-06.
- [Coarse-to-Fine](https://ojs.aaai.org/index.php/AAAI/article/view/19994) - Generates layouts hierarchically from coarse global structure to fine element placement (AAAI 2022).
#### 2021

- [Layout-BLT](https://arxiv.org/abs/2112.05112) - Uses bidirectional layout transformers to generate and refine object arrangements (ECCV 2022).
- [CanvasVAE](https://arxiv.org/abs/2108.01249) - Uses a variational autoencoder to model element-level layouts for design documents (ICCV 2021).
- [LayoutGAN++](https://arxiv.org/abs/2108.00871) - Improves GAN-based layout generation with differentiable rendering and stronger geometric reasoning (ACM MM 2021). Project: — · [Code](https://github.com/ktrk115/const_layout) (`training + inference`) · Weights: `released`.<br>  **Method:** GAN-based structured layout generation · **Base:** Transformer generator and discriminator · **Train:** RICO; PubLayNet · **Eval:** RICO; PubLayNet · **Output:** Structured layout boxes · **Checked:** 2026-10-06.
#### 2020

- [DeepLayout](https://arxiv.org/abs/2006.14615) - Models layouts autoregressively as sequences for conditional and unconditional generation (ICCV 2021).
#### 2019

- [Neural Design Network](https://arxiv.org/abs/1912.09421) - Generates graphic layouts under explicit design constraints with a neural structured model (ECCV 2020).
- [LayoutVAE](https://arxiv.org/abs/1907.10719) - Uses a label-conditioned variational autoencoder for structured document layout generation (ICCV 2019).
- [LayoutGAN](https://openreview.net/forum?id=HJxB5sRcFQ) - Introduces a GAN formulation for synthesizing layouts represented by labeled geometric elements (ICLR 2019).
#### 2014

- [Learning Layouts for Single-Page Graphic Designs](https://doi.org/10.1109/TVCG.2014.48) - Learns layout relationships from existing single-page graphic designs to support automatic composition (TVCG 2014).
### Content-Aware Layout Generation

#### 2026

- [iPoster](https://arxiv.org/abs/2603.29469) - Supports interactive content-aware poster layout generation under flexible user-specified constraints (CHI EA 2026).
#### 2025

- [Learning Priority-Aware Controllable Poster Layout Generation](https://doi.org/10.1016/j.patcog.2026.113497) - Uses LLM- and vision-derived priorities, optimal-transport matching, and flow-based refinement for controllable poster layout generation (Pattern Recognition 2026).
- [SEGA](https://arxiv.org/abs/2510.15749) - Uses stepwise evolution for content-aware poster layout generation and introduces GenPoster-100K (ICCV 2025).
- [Uni-Layout](https://arxiv.org/abs/2508.02374) - Unifies multiple layout-generation conditions with human-feedback-based evaluation and preference alignment (ACM MM 2025).
- [CreatiPoster](https://arxiv.org/abs/2506.10890) - Generates poster layouts from multimodal content and design requirements.
- [Scan-and-Print](https://arxiv.org/abs/2505.20649) - Uses patch-level image summarization and data augmentation for efficient content-aware poster layout generation (IJCAI 2025). [Project](https://thekinsley.github.io/Scan-and-Print/) · [Code](https://github.com/theKinsley/Scan-and-Print-IJCAI2025) (`training + inference`) · Weights: `unknown`.<br>  **Method:** Autoregressive content-aware layout generation · **Base:** DeiT3 visual encoder · **Train:** PKU PosterLayout; CGL · **Eval:** PKU PosterLayout; CGL · **Output:** Structured layout boxes · **Checked:** 2026-10-06.
#### 2024

- [Design Element Aware Poster Layout Generation](https://doi.org/10.1145/3627673.3679557) - Models poster design elements and their relationships for content-aware poster layout generation (CIKM 2024).
- [CGB-DM](https://arxiv.org/abs/2407.15233) - Uses a diffusion transformer for graphic-layout generation with content-aware conditioning.
- [Visual Layout Composer](https://openaccess.thecvf.com/content/CVPR2024/html/Shabani_Visual_Layout_Composer_Image-Vector_Dual_Diffusion_Model_for_Design_Layout_CVPR_2024_paper.html) - Couples image-space and vector-space diffusion to generate design layouts conditioned on visual content (CVPR 2024).
- [PosterLLaVA](https://arxiv.org/abs/2406.02884) - Uses multimodal instruction tuning for poster layout generation (IEEE TMM 2024).
- [Graphist](https://arxiv.org/abs/2404.14368) - Models graphic-design layouts with multimodal and structural context.
- [PosterLLaMA](https://arxiv.org/abs/2404.00995) - Adapts a multimodal language model to poster layout generation (ECCV 2024). [Project](https://lait-cvlab.github.io/PosterLlama/) · [Code](https://github.com/jaepoong/PosterLlama) (`training + inference`) · [Weights](https://huggingface.co/poong/PosterLlama) (`released`).<br>  **Method:** Vision-language model for content-aware poster layout generation · **Base:** LLaMA2-7B-chat; CodeLLaMA-7B; DINO visual features · **Train:** MiniGPT-4 synthetic caption data; CGL · **Eval:** CGL; poster-layout benchmarks · **Output:** HTML/code-form layout representation · **Checked:** 2026-10-06.
#### 2023

- [RALF](https://arxiv.org/abs/2311.13602) - Retrieves relevant design examples to guide content-aware layout generation (CVPR 2024). [Project](https://udonda.github.io/RALF/) · [Code](https://github.com/CyberAgentAILab/RALF) (`training + inference`) · Weights: `released`.<br>  **Method:** Retrieval-augmented autoregressive layout transformer · **Base:** ResNet50 image encoder; autoregressive transformer · **Train:** PKU PosterLayout; CGL · **Eval:** PKU PosterLayout; CGL · **Output:** Structured content-aware layouts · **Checked:** 2026-10-06.
- [Two-stage Content-Aware Layout Generation for Poster Designs](https://doi.org/10.1145/3581783.3612275) - Combines aesthetics-conditioned diffusion layout proposals with a learned ranking stage for poster designs over image backgrounds (ACM MM 2023).
- [RADM](https://arxiv.org/abs/2306.09086) - Generates content-aware advertising layouts with richer text and visual conditioning (CIKM 2023).
- [PosterLayout](https://arxiv.org/abs/2303.15937) - Introduces a benchmark and content-aware approach for visual-textual poster layout generation (CVPR 2023). Project: — · [Code](https://github.com/PKU-ICST-MIPL/PosterLayout-CVPR2023) (`training + inference`) · Weights: `released`.<br>  **Method:** Content-aware poster layout generation with DS-GAN · **Base:** Visual feature encoder; GAN layout generator · **Train:** PKU PosterLayout · **Eval:** PKU PosterLayout · **Output:** Structured poster layout boxes · **Checked:** 2026-10-06.
#### 2022

- [LayoutDETR](https://arxiv.org/abs/2212.09877) - Generates foreground layouts conditioned on content images for advertising design (ECCV 2024). Project: — · [Code](https://github.com/salesforce/LayoutDETR) (`training + inference`) · Weights: `released`.<br>  **Method:** Detection-transformer-style multimodal layout generation · **Base:** DETR-style multimodal conditioning; generative layout backbone · **Train:** LayoutDETR Ad Banner Dataset · **Eval:** LayoutDETR Ad Banner Dataset · **Output:** Structured foreground layout; rendered ad banner · **Checked:** 2026-10-06.
- [ICVT](https://arxiv.org/abs/2209.00852) - Generates layouts conditioned on image content with geometry-aligned variational transformers (ACM MM 2022).
- [CGL-GAN](https://arxiv.org/abs/2205.00303) - Generates advertising layouts conditioned on visual content and introduces the CGL dataset (IJCAI 2022). Project: — · [Code](https://github.com/minzhouGithub/CGL-GAN) (`announced`) · Weights: `unknown`.<br>  **Method:** Composition-aware GAN for visual-textual presentation layouts · **Base:** GAN with composition-aware visual conditioning · **Train:** CGL Dataset · **Eval:** CGL Dataset · **Output:** Structured advertising layout boxes · **Checked:** 2026-10-06.
#### 2021

- [SmartText](https://doi.org/10.1109/TMM.2021.3097900) - Places text over natural images using saliency and learned aesthetic compatibility for harmonious poster composition (TMM 2021).
#### 2019

- [ContentGAN](https://doi.org/10.1145/3306346.3322971) - Generates graphic-design layouts conditioned on underlying visual content (SIGGRAPH 2019).
### Graphic Design Generation

#### 2026

- [Designer-RSI](https://arxiv.org/abs/2609.22086) - Adapts a tool-using graphic-design agent through continually refined procedural memory learned from real user briefs.
- [Human-aware Design Generation](https://arxiv.org/abs/2609.17689) - Completes graphic designs by jointly composing 3D human poses, 2D framing, and human-image placement (ACM MM 2026).
- [InterIL](https://arxiv.org/abs/2609.11519) - Jointly generates background images and foreground layouts to model bidirectional image-layout interaction in design templates.
- [Mise-en-Scène](https://arxiv.org/abs/2608.19000) - Generates editable layered designs by letting layout emerge within a diffusion transformer while preserving source assets.
- [SIMPLEPOSTER](https://arxiv.org/abs/2605.08784) - Generates product posters with faithful subject preservation and position-controllable text rendering (CVPR 2026).
- [Brief2Design](https://arxiv.org/abs/2604.11019) - Supports prompt-based professional graphic design through requirement extraction, element exploration, and compositional recombination.
- [PSDesigner](https://arxiv.org/abs/2603.25738) - Automates layered graphic-design workflows with editable PSD structure and tool-use trajectories (CVPR 2026). [Project](https://henghuiding.com/PSDesigner) · [Code](https://github.com/FudanCVL/PSDesigner) (`announced`) · Weights: `announced`.<br>  **Method:** Tool-using layered graphic-design agent · **Base:** GraphicPlanner · **Train:** CreativePSD · **Eval:** Crello-v5; copyright-free PSD files · **Output:** Editable PSD · **Checked:** 2026-10-06.
- [DesignAsCode](https://arxiv.org/abs/2602.17690) - Represents graphic designs as HTML/CSS and iteratively plans, implements, and visually refines editable designs (ACM MM 2026). [Project](https://liuziyuan1109.github.io/design-as-code/) · [Code](https://github.com/liuziyuan1109/design-as-code) (`training + inference`) · [Weights](https://huggingface.co/Tony1109/DesignAsCode-planner) (`released`).<br>  **Method:** Code-native agentic graphic-design generation · **Base:** Qwen3-8B planner; GPT-5; GPT-4o; gpt-image-1 · **Train:** DesignAsCode training data (~19K distilled Crello samples) · **Eval:** 546-sample test set; Broad test set · **Output:** Editable HTML/CSS · **Checked:** 2026-10-06.
- [PosterVerse](https://arxiv.org/abs/2601.03993) - Automates commercial poster creation with blueprint planning, background generation, and HTML-based scalable typography.

## Datasets

### 2026

- [CreativePSD](https://huggingface.co/datasets/creative-graphic-design/CreativePSD) - PSD-derived graphic designs with layer trees, source assets, tool-call trajectories, and intermediate renders.

## Benchmarks and Evaluation

### 2026

- [AesEvalBench](https://arxiv.org/abs/2603.01083) - Evaluates graphic-design aesthetics through localized issue labels, region judgments, and vision-language-model assessments (ICLR 2026).

## Models and Implementations

- [Creative Graphic Design Datasets](https://github.com/creative-graphic-design/huggingface-datasets) - Maintains reproducible Hugging Face loaders and dataset cards for graphic-design research datasets.
- [design-generators](https://github.com/creative-graphic-design/design-generators) - Ports layout, poster, and graphic-design generation research into consistent Transformers, Diffusers, and agent interfaces.
- [Graphic Design Evaluation](https://github.com/creative-graphic-design/Graphic-design-evaluation) - Provides evaluation assets and implementations for measuring graphic-design quality principles.
- [GPT Graphic Design Evaluator](https://github.com/creative-graphic-design/gpt-graphic-design-evaluator) - Implements vision-language-model-based evaluation for graphic-design outputs.

## Relevant Venues and Journals

Recurring publication venues worth monitoring for work in this area. Inclusion here indicates relevance to the field, not that every paper at the venue is in scope.

### Conferences

- [AAAI](https://aaai.org/conference/aaai/) - Artificial intelligence conference with layout-generation and design-automation work.

### Journals

- [ACM Transactions on Graphics (TOG)](https://dl.acm.org/journal/tog) - Computer graphics journal covering visual synthesis and design systems.

## Related Resources

- [Creative Graphic Design](https://github.com/creative-graphic-design) - Organization hosting datasets, model ports, evaluation tools, and research infrastructure used by several entries in this list.

## Contributing

Contributions are welcome. Please read the [contribution guidelines](CONTRIBUTING.md) before opening a pull request.
