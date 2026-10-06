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

**Layout Generation:** Outputs structured element geometry or arrangement without relying on the visual content of a target canvas.

**Content-Aware Layout Generation:** Still outputs layout or placement, but conditions that geometry on a background image, product/brand assets, saliency, element content, or another visual canvas.

**Graphic Design Generation:** Goes beyond geometry to create a composed design artifact, such as backgrounds, imagery, typography, styles, layers, or editable HTML/CSS/PSD/PPTX structures.

**Typography and Text Rendering:** Focuses primarily on legible, faithful, or stylized text generation and placement within designed imagery.

**Graphic Design Editing and Reconstruction:** Focuses on iterative editing, layer recovery, or conversion of rendered designs back into editable structures.

**Scientific Poster and Slide Generation:** Covers research communication workflows that combine source-document understanding, content selection, layout, typography, rendering, and often editable output.

### Layout Generation

#### 2026

- [i-Design](https://link.springer.com/chapter/10.1007/978-3-032-14826-1_18) - Optimizes graphic layout design step by step with progressive aesthetic policy optimization (ECCV 2026).
#### 2025

- [PosterO](https://arxiv.org/abs/2505.07843) - Structures layouts as trees so language models can solve generalized layout-generation tasks (CVPR 2025).
#### 2024

- [TextLap](https://arxiv.org/abs/2410.12844) - Generates graphic layouts from textual design requirements with language-model-based reasoning.
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
#### 2025

- [CreatiDesign](https://arxiv.org/abs/2505.19114) - Uses a multi-conditional diffusion transformer to compose primary visuals, decorative elements, text, and layout for graphic design. [Project](https://huizhang0812.github.io/CreatiDesign/) · [Code](https://github.com/HuiZhang0812/CreatiDesign) (`inference only`) · [Weights](https://huggingface.co/HuiZhang0812/CreatiDesign) (`released`).<br>  **Method:** Multi-conditional diffusion transformer · **Base:** FLUX.1-dev · **Train:** CreatiDesign dataset (~400K designs) · **Eval:** CreatiDesign benchmark (1K samples) · **Output:** Raster graphic design · **Checked:** 2026-10-06.
- [POSTA](https://arxiv.org/abs/2503.14908) - Combines background diffusion, multimodal layout and typography planning, and stylized text generation for customizable artistic posters (CVPR 2025).
- [BannerAgency](https://arxiv.org/abs/2503.11060) - Uses collaborating multimodal LLM agents to plan and generate advertising banner designs from brand assets and requests (2025).
#### 2024

- [LaDeCo](https://arxiv.org/abs/2412.19712) - Generates layered and editable graphic designs rather than flattened images (CVPR 2025).
- [OpenCOLE](https://arxiv.org/abs/2406.08232) - Provides an open and reproducible pipeline for automatic layered graphic-design generation (CVPR Workshop 2024).
- [Desigen](https://arxiv.org/abs/2403.09093) - Jointly generates advertising backgrounds and foreground element layouts (CVPR 2024).
#### 2023

- [Planning and Rendering](https://arxiv.org/abs/2312.08822) - Separates semantic planning from visual rendering for end-to-end product-poster generation (2023).
- [COLE](https://arxiv.org/abs/2311.16974) - Uses a hierarchical generation framework to create multi-layered, editable graphic designs from high-level intent (2023).
- [AutoPoster](https://arxiv.org/abs/2308.01095) - Integrates content analysis and layout generation into an automatic advertising-poster design system (2023).
### Typography and Text Rendering

#### 2025

- [PosterMaker](https://arxiv.org/abs/2504.06632) - Generates product posters with explicit mechanisms for accurate text rendering and visual composition (CVPR 2025).
#### 2023

- [TextDiffuser-2](https://arxiv.org/abs/2311.16465) - Uses language-model planning to improve flexible text layout and rendering in generated images (2023). [Project](https://jingyechen.github.io/textdiffuser2/) · [Code](https://github.com/microsoft/unilm/tree/master/textdiffuser-2) (`training + inference`) · [Weights](https://huggingface.co/JingyeChen22/textdiffuser2-full-ft) (`released`).<br>  **Method:** Language-model-assisted diffusion for flexible text rendering · **Base:** Stable Diffusion v1.5; LLM layout planner · **Train:** MARIO-style text-image data; layout-planner instruction data · **Eval:** Text rendering and inpainting benchmarks · **Output:** Raster image with rendered text · **Checked:** 2026-10-06.
- [TextPainter](https://arxiv.org/abs/2308.04733) - Generates poster-oriented text imagery while balancing text comprehension and visual harmony (ACM MM 2023).
- [TextDiffuser](https://arxiv.org/abs/2305.10855) - Introduces diffusion-based text rendering with explicit character-level layout guidance (NeurIPS 2023). Project: — · [Code](https://github.com/microsoft/unilm/tree/master/textdiffuser) (`training + inference`) · [Weights](https://huggingface.co/datasets/JingyeChen22/TextDiffuser) (`released`).<br>  **Method:** Two-stage diffusion framework for text rendering · **Base:** Stable Diffusion v2.1 · **Train:** MARIO-LAION / MARIO-10M · **Eval:** MARIO-Eval · **Output:** Raster image with rendered text · **Checked:** 2026-10-06.
#### 2022

- [Text2Poster](https://arxiv.org/abs/2301.02363) - Retrieves suitable imagery and places stylized text to construct poster designs from text input (ICASSP 2022).
### Graphic Design Editing and Reconstruction

#### 2026

- [PosterText](https://arxiv.org/abs/2608.16289) - Unifies text-patch generation and editing for e-commerce posters with addition, deletion, modification, and style control.
- [ReDesign](https://arxiv.org/abs/2607.25565) - Recovers editable layer hierarchies, typography, geometry, colors, and grouping from raster design images (ECCV 2026).
#### 2025

- [PosterCopilot](https://arxiv.org/abs/2512.04082) - Combines layout reasoning with layer-controllable iterative editing for professional graphic-design workflows (ECCV 2026). [Project](https://postercopilot.github.io/) · [Code](https://github.com/JiazheWei/PosterCopilot) (`inference only`) · [Weights](https://huggingface.co/void-2024/PosterCopilot) (`released`).<br>  **Method:** LMM layout reasoning and layer-controllable editing · **Base:** Qwen2.5-VL-7B-Instruct · **Train:** PosterCopilot Dataset (160K posters, 2.6M layers) · **Output:** JSON layout; PNG; editable PSD · **Checked:** 2026-10-06.
### Scientific Poster and Slide Generation

#### 2026

- [PosterVisor](https://arxiv.org/abs/2609.17326) - Uses persistent semantic-geometric contracts to control scientific-poster content, layout, validation, and repair.
- [PosterMELD](https://arxiv.org/abs/2608.02218) - Generates controllable, diverse scientific posters with multi-agent planning and editable print-ready PPTX outputs.
- [Personalization as Inverse Planning](https://arxiv.org/abs/2607.00407) - Learns latent page-level design intents for agentic slide personalization through structural denoising and multi-agent reinforcement learning (ECCV 2026).
- [Any2Poster](https://arxiv.org/abs/2606.02915) - Introduces an any-source poster benchmark and agent spanning multiple input modalities and content domains.
- [Design First Code Later](https://arxiv.org/abs/2605.26451) - Introduces DeepSlides, a template-free design-first slide-generation workflow with SlideDesign data and reinforcement-learned SlideQwen models. Project: — · [Code](https://github.com/sxswz213/DeepSlides) (`pipeline`) · Weights: `unknown`.<br>  **Method:** Design-first template-free slide-generation workflow · **Base:** Configurable LLMs plus SlideQwen design/implementation models · **Train:** SlideDesign · **Output:** Editable PPTX; slide images · **Checked:** 2026-10-06.
#### 2025

- [SlideGen](https://arxiv.org/abs/2512.04529) - Coordinates multimodal agents to transform scientific papers into editable PPTX slide decks with visual-in-the-loop refinement (ACM MM 2026). [Project](https://y-research-sbu.github.io/SlideGen/) · [Code](https://github.com/Y-Research-SBU/SlideGen) (`pipeline`) · Weights: `n/a`.<br>  **Method:** Collaborative multimodal slide-generation agents · **Base:** API-based multimodal agents · **Train:** None · **Eval:** Scientific slide-generation benchmarks · **Output:** Editable PPTX · **Checked:** 2026-10-06.
- [SciPostGen](https://arxiv.org/abs/2511.22490) - Introduces a large-scale paper-poster dataset and retrieval-augmented scientific-poster layout generation (CVPR Findings 2026).
- [PosterForest](https://arxiv.org/abs/2508.21720) - Uses a hierarchical Poster Tree and collaborating agents to jointly optimize scientific-poster content, structure, and layout (ACL 2026). Project: — · [Code](https://github.com/kaist-cvml/poster-forest) (`pipeline`) · Weights: `n/a`.<br>  **Method:** Training-free multi-agent scientific-poster generation · **Base:** GPT-4o or local Qwen3/Qwen2.5 models · **Train:** None · **Eval:** Paper2Poster-style evaluation · **Output:** Editable PPTX; JPG · **Checked:** 2026-10-06.
- [PosterGen](https://arxiv.org/abs/2508.17188) - Uses specialized agents for paper parsing, curation, layout, styling, and rendering to generate scientific posters.
- [Paper2Poster](https://arxiv.org/abs/2505.21497) - Introduces a multimodal paper-to-poster benchmark and a visual-in-the-loop multi-agent system that exports editable PPTX posters (NeurIPS 2025).
- [P2P](https://arxiv.org/abs/2505.17104) - Uses a multi-agent pipeline to generate HTML academic posters from papers and introduces instruction data and fine-grained evaluation.
- [Scientific Poster Generation A New Dataset and Approach](https://doi.org/10.1016/j.patcog.2025.111507) - Introduces the 1,226-poster Sci-PosterLayout dataset and a template-free sequence generator with a Design Pattern Schema for scientific-poster layouts (Pattern Recognition 2025).
#### 2024

- [SciPostLayout](https://arxiv.org/abs/2407.19787) - Targets structured layout generation for scientific posters. Project: — · [Code](https://github.com/omron-sinicx/scipostlayout) (`training + inference`) · Weights: `n/a`.<br>  **Method:** Scientific-poster layout analysis and generation baselines · **Base:** LayoutLMv3; DiT; LayoutDM; LayoutFormer++; GPT-4 · **Train:** SciPostLayout · **Eval:** SciPostLayout · **Output:** Scientific-poster layouts · **Checked:** 2026-10-06.
## Datasets

### 2026

- [CreativePSD](https://huggingface.co/datasets/creative-graphic-design/CreativePSD) - PSD-derived graphic designs with layer trees, source assets, tool-call trajectories, and intermediate renders.
- [LICA](https://huggingface.co/datasets/creative-graphic-design/LICA) - Rendered graphic designs with component-level specifications and natural-language design annotations.
### 2025

- [GenPoster-100K](https://huggingface.co/datasets/creative-graphic-design/GenPoster100K) - Poster data with rendered backgrounds, PSD references, and layer-level typography, color, and geometry annotations.
- [BannerRequest400](https://huggingface.co/datasets/creative-graphic-design/BannerRequest400) - Advertising banner requests with brand logos, multimodal design instructions, and target designs.
- [Sci-PosterLayout](https://github.com/kitman0000/Sci-PosterLayout-Data) - Contains 1,226 scientific poster layouts spanning diverse domains and content attributes for scientific-poster generation.
### 2023

- [CGL Dataset v2](https://huggingface.co/datasets/creative-graphic-design/CGL-Dataset-v2) - Poster backgrounds with text-aware element boxes, masks, and layout metadata.
- [PKU PosterLayout](https://huggingface.co/datasets/creative-graphic-design/PKU-PosterLayout) - Poster images with visual-textual element boxes, saliency maps, and inpainted canvases.
### 2022

- [LayoutDETR Dataset](https://huggingface.co/datasets/creative-graphic-design/LayoutDETR) - Advertising banners with foreground layouts and inpainted background assets.
- [CGL Dataset](https://huggingface.co/datasets/creative-graphic-design/CGL-Dataset) - Advertising poster images, inpainted backgrounds, element categories, and bounding-box annotations.
### 2019

- [Magazine](https://huggingface.co/datasets/creative-graphic-design/Magazine) - Contains fine-grained polygon layouts and semantic element labels for magazine pages.
### 2018

- [CTXFont](https://huggingface.co/datasets/creative-graphic-design/CTXFont) - Web-design screenshots with text-element boxes, font properties, and contextual metadata.
## Benchmarks and Evaluation

### 2026

- [TASTE](https://arxiv.org/abs/2605.20731) - Provides designer-panel preferences for AI-generated graphic designs across typography, hierarchy, color, layout, and brief fidelity.
- [Graphic-Design-Bench](https://arxiv.org/abs/2604.04192) - Benchmarks AI systems across professional graphic-design tasks including layout, typography, vector structure, semantics, and animation.
- [AesEvalBench](https://arxiv.org/abs/2603.01083) - Evaluates graphic-design aesthetics through localized issue labels, region judgments, and vision-language-model assessments (ICLR 2026).
- [DesignSense](https://arxiv.org/abs/2602.23438) - Provides 10,235 human-annotated graphic-layout preference pairs and a specialized reward model for layout evaluation.
### 2025

- [PPTArena](https://arxiv.org/abs/2512.03042) - Benchmarks natural-language PowerPoint editing over real decks with structural and visual evaluation and introduces the PPTPilot editing agent (ECCV 2026).
### 2024

- [Graphic Design Evaluation](https://arxiv.org/abs/2410.08885) - Evaluates alignment, overlap, white space, and related graphic-design principles with absolute and pairwise judgments (SIGGRAPH Asia 2024).
- [LTSim](https://arxiv.org/abs/2407.12356) - Measures layout similarity through transportation-based matching of structured elements for layout-generation evaluation (2024).
- [DesignProbe](https://arxiv.org/abs/2404.14801) - Benchmarks multimodal large language models on graphic-design understanding and reasoning tasks (2024).
### Other

- [Layout FID](https://github.com/creative-graphic-design/design-generators/tree/main/models/layout-fid) - Provides a learned feature-space metric for comparing generated and real layout distributions.
## Models and Implementations

- [Creative Graphic Design Datasets](https://github.com/creative-graphic-design/huggingface-datasets) - Maintains reproducible Hugging Face loaders and dataset cards for graphic-design research datasets.
- [design-generators](https://github.com/creative-graphic-design/design-generators) - Ports layout, poster, and graphic-design generation research into consistent Transformers, Diffusers, and agent interfaces.
- [GPT Graphic Design Evaluator](https://github.com/creative-graphic-design/gpt-graphic-design-evaluator) - Implements vision-language-model-based evaluation for graphic-design outputs.
- [Graphic Design Evaluation](https://github.com/creative-graphic-design/Graphic-design-evaluation) - Provides evaluation assets and implementations for measuring graphic-design quality principles.
## Relevant Venues and Journals

Recurring publication venues worth monitoring for work in this area. Inclusion here indicates relevance to the field, not that every paper at the venue is in scope.

### Conferences

- [AAAI](https://aaai.org/conference/aaai/) - Artificial intelligence; includes structured and controllable layout-generation research.
- [ACL](https://aclanthology.org/venues/acl/) - Natural language processing; increasingly relevant to paper-to-poster and document-to-design agent systems.
- [ACM Multimedia](https://acmmm.hosting2.acm.org/) - Multimedia; recurring venue for layout generation, poster generation, typography, slide generation, and multimodal design systems.
- [BMVC](https://bmvc2026.org/) - Computer vision; includes scientific-poster layout datasets and document-layout research.
- [CHI](https://chi.acm.org/) - Human-computer interaction; relevant for interactive and human-centered graphic-design systems.
- [CIKM](https://www.cikmconference.org/) - Information and knowledge management; has published industrial poster-layout and content-aware design work.
- [CVPR](https://cvpr.thecvf.com/) - Computer vision; frequently publishes layout, poster, multimodal generation, and evaluation work.
- [ECCV](https://eccv.ecva.net/) - Computer vision; strong coverage of layout, editable design, slide design, and image-generation research.
- [ICASSP](https://2026.ieeeicassp.org/) - Signal processing and multimedia; includes poster and text-layout generation work.
- [ICCV](https://iccv.thecvf.com/) - Computer vision; relevant for layout generation, content-aware design, and structured visual generation.
- [ICLR](https://iclr.cc/) - Machine learning; relevant for generative models, language-based layout generation, scientific-poster agents, and evaluation.
- [ICME](https://www.2026.ieeeicme.org/) - Multimedia; relevant for multimodal content generation and visual-design systems.
- [ICML](https://icml.cc/) - Machine learning; relevant for generative modeling and controllable structured generation.
- [IJCAI](https://www.ijcai.org/) - Artificial intelligence; includes content-aware advertising and poster-layout generation.
- [NeurIPS](https://neurips.cc/) - Machine learning; relevant for generative modeling, multimodal agents, evaluation, and scientific-poster automation.
- [SIGGRAPH](https://www.siggraph.org/) - Computer graphics and interactive techniques; important for content-aware design and visual composition.
- [SIGGRAPH Asia](https://asia.siggraph.org/) - Computer graphics and interactive techniques; relevant for graphic-design generation and evaluation.
### Journals

- [ACM Transactions on Graphics](https://dl.acm.org/journal/tog) - Graphics journal associated with SIGGRAPH research in visual synthesis and design.
- [IEEE Transactions on Multimedia](https://signalprocessingsociety.org/publications-resources/ieee-transactions-multimedia) - Multimedia journal covering visual composition, poster layout, and multimodal generation.
- [IEEE Transactions on Visualization and Computer Graphics](https://www.computer.org/csdl/journal/tg) - Visualization and graphics journal with foundational work on learned graphic layouts.
- [Information Fusion](https://www.sciencedirect.com/journal/information-fusion) - Information-fusion journal including surveys and multimodal generative methods.
- [Pattern Recognition](https://www.sciencedirect.com/journal/pattern-recognition) - Pattern-recognition journal publishing scientific-poster and controllable poster-layout generation research.
- [The Visual Computer](https://link.springer.com/journal/371) - Graphics and visual-computing journal with work on layout and graphic-design generation.
## Related Resources

- [Creative Graphic Design](https://github.com/creative-graphic-design) - Organization hosting datasets, model ports, evaluation tools, and research infrastructure used by several entries in this list.
## Contributing

Contributions are welcome. Please read the [contribution guidelines](CONTRIBUTING.md) before opening a pull request.
