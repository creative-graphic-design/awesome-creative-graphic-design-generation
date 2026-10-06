# Awesome Creative Graphic Design Generation [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![Catalog Check](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/workflows/catalog-check.yml/badge.svg)](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/workflows/catalog-check.yml)
[![Awesome Lint](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/workflows/awesome-lint.yml/badge.svg)](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/workflows/awesome-lint.yml)
![Papers](https://img.shields.io/badge/papers-114-informational)
![Datasets and Benchmarks](https://img.shields.io/badge/datasets%20%26%20benchmarks-35-informational)
![Reproducibility Audited](https://img.shields.io/badge/reproducibility%20audited-41-informational)

<!-- This file is generated from data/resources.csv and data/paper_metadata.csv by scripts/generate_readme.py. Do not edit it directly. -->

Curated resources for generating, editing, representing, and evaluating composed graphic-design artifacts such as posters, advertisements, social-media graphics, magazine layouts, scientific figures, graphical abstracts, scientific posters, slides, banners, and related visual compositions.

This list focuses on work where layout, typography, visual elements, editable structure, or design-specific evaluation is a first-class part of the problem. Generic text-to-image generation and generic image editing are out of scope unless they make a direct contribution to graphic-design generation.

Research resources are ordered by **first public appearance** within each category, from newest to oldest. The sort key is the earlier of the arXiv v1 date and the venue/presentation date when both are known; journal-only work uses its first public publication date.

Implementation metadata is tracked in [`data/paper_metadata.csv`](data/paper_metadata.csv). Verified entries expose project pages, official code and weight-release status, method/base model, training and evaluation datasets, output representation, and the date the release status was last checked.

## Contents

- [Surveys and Overviews](#surveys-and-overviews)
- [Papers](#papers)
  - [Layout Generation](#layout-generation)
  - [Content-Aware Layout Generation](#content-aware-layout-generation)
  - [Graphic Design Generation](#graphic-design-generation)
  - [Composable and Layered Asset Generation](#composable-and-layered-asset-generation)
  - [Typography and Text Rendering](#typography-and-text-rendering)
  - [Graphic Design Editing and Reconstruction](#graphic-design-editing-and-reconstruction)
  - [Scientific Figure and Graphical Abstract Generation](#scientific-figure-and-graphical-abstract-generation)
  - [Scientific Poster and Slide Generation](#scientific-poster-and-slide-generation)
- [Datasets and Benchmarks](#datasets-and-benchmarks)
- [Evaluation Methods and Metrics](#evaluation-methods-and-metrics)
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

**Composable and Layered Asset Generation:** Produces transparent, separable, layered, chroma-keyed, or intentionally empty-space visual assets that can be independently composed or edited in downstream design workflows.

**Typography and Text Rendering:** Focuses primarily on legible, faithful, or stylized text generation and placement within designed imagery.

**Graphic Design Editing and Reconstruction:** Focuses on iterative editing, layer recovery, or conversion of rendered designs back into editable structures.

**Scientific Figure and Graphical Abstract Generation:** Converts scientific papers or long-form technical content into methodology figures, diagrams, Figure 1-style summaries, or graphical abstracts, including editable vector outputs.

**Scientific Poster and Slide Generation:** Covers research communication workflows that combine source-document understanding, content selection, layout, typography, rendering, and often editable poster or slide output.

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
- [Two-stage Content-Aware Layout Generation for Poster Designs](https://doi.org/10.1145/3581783.3613817) - Uses a two-stage generation process to place design elements while conditioning on poster content (ACM MM 2023).
- [LayoutDETR](https://arxiv.org/abs/2212.09877) - Generates content-aware graphic layouts with transformer-based adversarial learning (SIGGRAPH Asia 2023). Project: — · [Code](https://github.com/salesforce/LayoutDETR) (`training + inference`) · Weights: `unknown`.<br>  **Method:** Transformer-based generative adversarial network for content-aware layout · **Base:** DETR-style transformer; ResNet image features · **Train:** PKU PosterLayout; CGL · **Eval:** PKU PosterLayout; CGL · **Output:** Structured graphic-design layouts · **Checked:** 2026-10-06.
#### 2022

- [CGL-GAN](https://openaccess.thecvf.com/content/CVPR2022/html/Zhou_Composition-Aware_Graphic_Layout_GAN_for_Visual-Textual_Presentation_Design_CVPR_2022_paper.html) - Uses composition-aware adversarial learning for graphic-layout generation conditioned on visual content (CVPR 2022). Project: — · [Code](https://github.com/bcmi/Content-aware-Graphic-Layout) (`training + inference`) · Weights: `released`.<br>  **Method:** Composition-aware GAN for content-conditioned layout generation · **Base:** GAN with composition-aware discriminator · **Train:** CGL · **Eval:** CGL · **Output:** Structured graphic-design layouts · **Checked:** 2026-10-06.
- [PosterLayout](https://arxiv.org/abs/2203.15937) - Generates content-aware poster layouts that respect salient regions and visual composition (CVPR 2022). [Project](https://pkucpk.github.io/PosterLayout-CVPR2022/) · [Code](https://github.com/PKU-ICST-MIPL/PosterLayout-CVPR2022) (`training + inference`) · [Weights](https://github.com/PKU-ICST-MIPL/PosterLayout-CVPR2022/tree/main/pretrained) (`released`).<br>  **Method:** Content-aware generative layout transformer · **Base:** Transformer-style generator with saliency conditioning · **Train:** PKU PosterLayout · **Eval:** PKU PosterLayout · **Output:** Structured poster-layout boxes · **Checked:** 2026-10-06.
- [LayoutDETR](https://arxiv.org/abs/2212.09877) - Generates content-aware graphic layouts with transformer-based adversarial learning (SIGGRAPH Asia 2023). Project: — · [Code](https://github.com/salesforce/LayoutDETR) (`training + inference`) · Weights: `unknown`.<br>  **Method:** Transformer-based generative adversarial network for content-aware layout · **Base:** DETR-style transformer; ResNet image features · **Train:** PKU PosterLayout; CGL · **Eval:** PKU PosterLayout; CGL · **Output:** Structured graphic-design layouts · **Checked:** 2026-10-06.
### Graphic Design Generation

#### 2026

- [Design Your Ad](https://arxiv.org/abs/2605.12138) - Jointly generates personalized advertising images and text from multimodal user histories with a unified autoregressive model and introduces PAd1M and PBS (CVPR 2026). Project: — · [Code](https://github.com/JD-GenX/Uni-AdGen) (`inference only`) · [Weights](https://3.cn/11f4I-YYG) (`released`).<br>  **Method:** Unified autoregressive personalized advertising image-text generation · **Base:** Janus-Pro-7B; DINOv2-small; SDXL-Base-1.0 · **Train:** PAd1M · **Eval:** PAd1M; PBS; BLEU; ROUGE · **Output:** Personalized advertising image and product text · **Checked:** 2026-10-06.
- [Multi-Object Advertisement Creative Generation](https://arxiv.org/abs/2603.13745) - Introduces CreativeAds for scalable multi-product lifestyle advertising through product pairing, layout generation, background generation, and human oversight.
- [InnoAds-Composer](https://arxiv.org/abs/2603.05898) - Generates e-commerce product posters in a single stage with joint subject, glyph, and style conditioning (CVPR 2026).
- [SIMPLEPOSTER](https://arxiv.org/abs/2605.08784) - Performs end-to-end poster generation with product identity, text fidelity, and style control (CVPR 2026).
- [BannerAgency](https://arxiv.org/abs/2601.17699) - Uses a multi-agent framework to plan, generate, and refine advertising banners with multimodal feedback (CVPR 2026).
#### 2025

- [AutoPP](https://arxiv.org/abs/2512.21921) - Automates product-poster generation and CTR-oriented optimization using unified design generation and online-feedback preference learning (AAAI 2026). Project: — · [Code](https://github.com/JD-GenX/AutoPP) (`announced`) · Weights: `unknown`.<br>  **Method:** Automated product-poster generation plus CTR-oriented preference optimization · **Train:** AutoPP1M product-poster generation and optimization subsets · **Eval:** Offline poster-generation metrics; online CTR feedback · **Output:** Raster product poster · **Checked:** 2026-10-06.
- [RefAdGen](https://arxiv.org/abs/2508.11695) - Generates high-fidelity advertising images while preserving referenced product identity through spatial mask control and product-feature fusion (AAAI 2026). Project: — · [Code](https://github.com/Anonymous-Name-139/RefAdgen) (`training + inference`) · [Weights](https://huggingface.co/yiyun123/RefAdgen) (`released`).<br>  **Method:** Product-preserving advertising diffusion with spatial control and attention fusion · **Base:** Stable Diffusion v1.5; IP-Adapter; GroundingDINO; SAM2 · **Train:** AdProd-100K · **Eval:** AdProd-100K · **Output:** Raster product advertising image · **Checked:** 2026-10-06.
- [PosterVerse](https://arxiv.org/abs/2506.14864) - Uses a multimodal large language model to generate and edit posters through natural-language interaction.
- [PosterMaker](https://arxiv.org/abs/2504.06632) - Generates high-quality product posters with explicit scene synthesis and accurate text rendering (CVPR 2025). [Project](https://poster-maker.github.io) · [Code](https://github.com/alimama-creative/PosterMaker) (`training + inference`) · [Weights](https://huggingface.co/alimama-creative/PosterMaker) (`released`).<br>  **Method:** Two-stage product-poster generation with scene synthesis and accurate text rendering · **Base:** Stable Diffusion 3 Medium · **Train:** Released e-commerce poster training data · **Eval:** Released stage-1 and stage-2 poster benchmarks · **Output:** Raster product poster with specified text regions · **Checked:** 2026-10-06.
- [T-Stars-Poster](https://arxiv.org/abs/2501.14316) - Provides an end-to-end product-centric advertising-design framework covering prompting, layout, background synthesis, and final rendering (CIKM 2025).
- [COLE](https://arxiv.org/abs/2501.01494) - Uses hierarchical multimodal reasoning to generate graphic-design artifacts with coordinated content and layout.
#### 2024

- [Towards Reliable Advertising Image Generation Using Human Feedback](https://arxiv.org/abs/2408.00418) - Uses a learned reliable-feedback network, recurrent generation, and feedback-guided diffusion fine-tuning to improve usable e-commerce advertising images (ECCV 2024). Project: — · [Code](https://github.com/JD-GenX/Reliable_AD) (`inference only`) · [Weights](https://huggingface.co/ZhenbangDu/reliable_controlnet) (`released`).<br>  **Method:** Reliable-feedback-guided recurrent advertising generation and diffusion fine-tuning · **Base:** Stable Diffusion v1.5-compatible latent diffusion; ControlNet · **Train:** RF1M · **Eval:** RF1M; human availability feedback · **Output:** Raster product advertising image · **Checked:** 2026-10-06.
- [GlyphDraw2](https://arxiv.org/abs/2407.02252) - Generates bilingual poster images with accurate Chinese and English glyph rendering using glyph and position conditioning (AAAI 2025). [Project](https://github.com/OPPO-Mente-Lab/GlyphDraw2) · [Code](https://github.com/OPPO-Mente-Lab/GlyphDraw2) (`training + inference`) · Weights: `unknown`.<br>  **Method:** Bilingual glyph-conditioned poster diffusion · **Base:** Stable Diffusion XL · **Train:** LaionGlyph-10M; ChineseGlyph-2M · **Output:** Raster poster image with rendered Chinese/English text · **Checked:** 2026-10-06.
- [OpenCOLE](https://arxiv.org/abs/2406.08232) - Provides an open framework for hierarchical graphic-design generation with multimodal language models and rendering tools.
- [Planning and Rendering: Towards End-to-End Text-Based Image Generation](https://arxiv.org/abs/2403.08495) - Separates planning from rendering to improve text-heavy graphic image generation (AAAI 2024).
#### 2023

- [CreatiDesign](https://arxiv.org/abs/2307.14643) - Generates complete graphic-design images from multimodal conditioning with controllable composition.
### Composable and Layered Asset Generation

#### 2026

- [MRT](https://arxiv.org/abs/2603.15697) - Unifies multi-layer image generation and editing with masked-region modeling over variable RGBA layer stacks (CVPR 2026). [Project](https://mrt-cvpr.github.io/) · Code: `unknown` · Weights: `unknown`.<br>  **Method:** Masked-region diffusion for unified layered generation and editing · **Base:** Qwen-Image · **Train:** 10M+ multilingual layered design samples; 43M+ transparent layers · **Output:** RGBA canvas/background/foreground layer stack · **Checked:** 2026-10-06.
- [Qwen-Image-Layered](https://arxiv.org/abs/2512.15603) - Decomposes images into a variable number of semantic RGBA layers and supports composable layer-level editing. [Project](https://qwen.ai/blog?id=qwen-image-layered&lid=1ami72hcYlwXGTTVQ) · [Code](https://github.com/QwenLM/Qwen-Image-Layered) (`inference only`) · [Weights](https://huggingface.co/Qwen/Qwen-Image-Layered) (`released`).<br>  **Method:** Variable-layer image decomposition diffusion model · **Base:** Qwen-Image · **Train:** Internal text-to-RGB/RGBA data; PSD-derived multilayer image corpus · **Eval:** Crello; LayerD decomposition protocol · **Output:** Variable-length RGBA layer stack; PSD/PPTX export · **Checked:** 2026-10-06.
#### 2025

- [TAUE](https://arxiv.org/abs/2511.02580) - Performs training-free layered foreground/background/composite generation by exploiting a text-to-image model's understanding and editing capabilities. [Project](https://iyatomilab.github.io/TAUE/) · Code: `announced` · Weights: `n/a`.<br>  **Method:** Training-free layered image generation · **Base:** Pretrained text-to-image model · **Train:** None · **Output:** Foreground; background; composite image · **Checked:** 2026-10-06.
- [PrismLayers](https://arxiv.org/abs/2510.21890) - Extends ART with higher-quality multi-layer transparent-image data and modeling for controllable layered generation (NeurIPS 2025). [Project](https://prism-layers.github.io/) · [Code](https://github.com/redredsheep/PrismLayers) (`inference only`) · Weights: `released`.<br>  **Method:** ART+ multi-layer transparent image generation · **Base:** ART · **Train:** PrismLayersPro (20K high-quality subset of 200K PrismLayers) · **Output:** Multiple RGBA layers plus composite image · **Checked:** 2026-10-06.
- [ART](https://arxiv.org/abs/2502.18364) - Generates a variable number of transparent image layers jointly with their composite using an Anonymous Region Transformer (CVPR 2025). Project: — · [Code](https://github.com/microsoft/art-msra) (`withdrawn`) · Weights: `withdrawn`.<br>  **Method:** Anonymous Region Transformer for variable multi-layer transparent generation · **Eval:** DESIGN-MULTI-LAYER-BENCH; PHOTO-MULTI-LAYER-BENCH · **Output:** Variable number of RGBA layers · **Checked:** 2026-10-06.
#### 2024

- [LayerDiffuse](https://arxiv.org/abs/2402.17113) - Enables latent diffusion models to synthesize images with transparent alpha channels and composable RGBA layers. [Project](https://github.com/lllyasviel/LayerDiffuse) · [Code](https://github.com/lllyasviel/LayerDiffuse_DiffusersCLI) (`inference only`) · [Weights](https://huggingface.co/LayerDiffusion/layerdiffusion-v1) (`released`).<br>  **Method:** Latent-transparency adaptation for transparent image generation · **Base:** Stable Diffusion v1.5 / SDXL · **Train:** 1M transparent image layer pairs · **Output:** Single or multiple transparent RGBA layers · **Checked:** 2026-10-06.
- [LayerFusion](https://arxiv.org/abs/2402.15226) - Performs training-free generation and harmonization of foreground/background layers with pretrained generative priors. [Project](https://layerfusion.github.io/) · Code: `announced` · Weights: `n/a`.<br>  **Method:** Training-free harmonized multi-layer generation with generative priors · **Base:** Pretrained latent diffusion model · **Train:** None · **Output:** Foreground RGBA; background RGB; composite RGB · **Checked:** 2026-10-06.
- [SAWNA](https://arxiv.org/abs/2404.10569) - Generates visually coherent images while preserving blank or controllable regions for later design composition.
- [TKG-DM](https://arxiv.org/abs/2404.02603) - Generates chroma-key visual assets through training-free initial-noise optimization for easy downstream extraction and composition. Project: — · [Code](https://github.com/ryugo417/TKG-DM) (`pipeline`) · Weights: `n/a`.<br>  **Method:** Training-free chroma-key content generation through initial-noise optimization · **Base:** Stable Diffusion XL 1.0 · **Train:** None · **Output:** RGB image with controlled chroma-key background · **Checked:** 2026-10-06.
### Typography and Text Rendering

#### 2026

- [PosterText](https://arxiv.org/abs/2608.16289) - Generates posters with semantically styled text, combining layout, typography, and visual rendering in a unified framework.
#### 2025

- [TextCrafter](https://arxiv.org/abs/2505.15735) - Improves text rendering in diffusion-generated images through character-aware conditioning and refinement (SIGGRAPH 2025).
- [PosterMaker](https://arxiv.org/abs/2504.06632) - Generates product posters with separate scene and text-rendering stages for accurate e-commerce typography (CVPR 2025). [Project](https://poster-maker.github.io) · [Code](https://github.com/alimama-creative/PosterMaker) (`training + inference`) · [Weights](https://huggingface.co/alimama-creative/PosterMaker) (`released`).<br>  **Method:** Two-stage product-poster generation with scene synthesis and accurate text rendering · **Base:** Stable Diffusion 3 Medium · **Train:** Released e-commerce poster training data · **Eval:** Released stage-1 and stage-2 poster benchmarks · **Output:** Raster product poster with specified text regions · **Checked:** 2026-10-06.
- [GlyphDraw2](https://arxiv.org/abs/2407.02252) - Generates bilingual poster images with accurate Chinese and English glyph rendering using glyph and position conditioning (AAAI 2025). [Project](https://github.com/OPPO-Mente-Lab/GlyphDraw2) · [Code](https://github.com/OPPO-Mente-Lab/GlyphDraw2) (`training + inference`) · Weights: `unknown`.<br>  **Method:** Bilingual glyph-conditioned poster diffusion · **Base:** Stable Diffusion XL · **Train:** LaionGlyph-10M; ChineseGlyph-2M · **Output:** Raster poster image with rendered Chinese/English text · **Checked:** 2026-10-06.
- [TextSSR](https://arxiv.org/abs/2502.09969) - Refines text regions for accurate scene-text rendering in generated images (CVPR 2025).
#### 2024

- [Glyph-ByT5](https://arxiv.org/abs/2403.09622) - Encodes glyph-aware character information with ByT5 for multilingual visual text generation (NeurIPS 2024).
- [TextDiffuser-2](https://arxiv.org/abs/2311.16465) - Uses a language model to plan text layouts before diffusion rendering for controllable text-rich image generation (ECCV 2024). [Project](https://microsoft.github.io/TextDiffuser-2/) · [Code](https://github.com/microsoft/unilm/tree/master/textdiffuser-2) (`training + inference`) · [Weights](https://huggingface.co/JingyeChen22/textdiffuser2-full-ft) (`released`).<br>  **Method:** LLM-guided text layout planning plus diffusion rendering · **Base:** Vicuna-7B-v1.5; Stable Diffusion 1.5 · **Train:** MARIO-10M; internal OCR-derived layout data · **Eval:** MARIO-Eval; DrawBenchText; user study · **Output:** Raster images with planned text layout · **Checked:** 2026-10-06.
- [Brush Your Text](https://arxiv.org/abs/2312.12232) - Edits rendered text regions in images while preserving surrounding visual content (AAAI 2024).
#### 2023

- [AnyText](https://arxiv.org/abs/2311.03054) - Supports multilingual visual text generation and editing with glyph and position conditioning (ICLR 2024).
- [GlyphControl](https://arxiv.org/abs/2305.18259) - Uses glyph-conditioned ControlNet-style guidance for accurate text rendering in diffusion-generated images (NeurIPS 2023).
- [TextDiffuser](https://arxiv.org/abs/2305.10855) - Decomposes text-rich image generation into layout prediction and character-level diffusion denoising (NeurIPS 2023). [Project](https://jingyechen.github.io/textdiffuser/) · [Code](https://github.com/microsoft/unilm/tree/master/textdiffuser) (`training + inference`) · [Weights](https://huggingface.co/JingyeChen22/textdiffuser) (`released`).<br>  **Method:** Two-stage text-region layout plus diffusion rendering · **Base:** Stable Diffusion · **Train:** MARIO-10M · **Eval:** MARIO-Eval; DrawBenchText · **Output:** Raster images with readable text · **Checked:** 2026-10-06.
- [TextPainter](https://arxiv.org/abs/2305.15880) - Renders multilingual text in complex visual contexts with language-aware glyph conditioning (ACM MM 2023).
- [SmartText](https://arxiv.org/abs/2304.14644) - Generates text-rich images while improving spelling and spatial consistency through character-level guidance (NeurIPS 2023).
- [Text2Poster](https://arxiv.org/abs/2204.04449) - Generates complete posters from text descriptions using controllable text and visual rendering (ICASSP 2022).
### Graphic Design Editing and Reconstruction

#### 2026

- [DesignCoder](https://arxiv.org/abs/2601.03640) - Reconstructs rendered graphic designs as editable HTML and supports instruction-driven edits through a multimodal code-generation model (CVPR 2026). [Project](https://design-coder.github.io/) · [Code](https://github.com/favotter/DesignCoder) (`inference only`) · [Weights](https://huggingface.co/favotter/DesignCoder-7B) (`released`).<br>  **Method:** Multimodal design-to-code reconstruction and instruction editing · **Base:** Qwen2.5-VL-7B-Instruct · **Train:** 108K rendered design webpages plus edit instruction pairs · **Output:** Editable HTML/CSS · **Checked:** 2026-10-06.
#### 2025

- [PosterCopilot](https://arxiv.org/abs/2512.04082) - Combines layout reasoning with layer-controllable iterative editing for professional graphic-design workflows (ECCV 2026). [Project](https://postercopilot.github.io/) · [Code](https://github.com/JiazheWei/PosterCopilot) (`inference only`) · [Weights](https://huggingface.co/void-2024/PosterCopilot) (`released`).<br>  **Method:** LMM layout reasoning and layer-controllable editing · **Base:** Qwen2.5-VL-7B-Instruct · **Train:** PosterCopilot Dataset (160K posters, 2.6M layers) · **Output:** JSON layout; PNG; editable PSD · **Checked:** 2026-10-06.
- [LayerD](https://arxiv.org/abs/2509.25134) - Decomposes raster graphic designs into editable layers through iterative foreground extraction and refinement (ICCV 2025). [Project](https://cyberagentailab.github.io/LayerD/) · [Code](https://github.com/CyberAgentAILab/LayerD) (`training + inference`) · [Weights](https://huggingface.co/cyberagent/layerd-birefnet) (`released`).<br>  **Method:** Iterative raster-to-layer decomposition with matting and refinement · **Base:** BiRefNet · **Output:** RGBA layers; SVG; PSD · **Checked:** 2026-10-06.
- [Draw with Thought](https://arxiv.org/abs/2504.09479) - Reconstructs raster scientific diagrams into editable mxGraph XML through coarse-to-fine reasoning and structure-aware code generation.
### Scientific Figure and Graphical Abstract Generation

#### 2026

- [Figures as Programs](https://arxiv.org/abs/2609.01006) - Generates editable scientific methodology figures as recursively composed SVG programs with source grounding and render-critic refinement.
- [PaperBanana-Interact](https://arxiv.org/abs/2608.30241) - Supports multi-turn scientific diagram refinement with human feedback using a critique-and-refine multi-agent workflow.
- [GenGA](https://arxiv.org/abs/2608.05478) - Generates data-grounded graphical abstracts as hierarchical vector elements for element-level post-editing and introduces the SIC editability metric.
- [SciForma](https://arxiv.org/abs/2607.18091) - Generates structure-faithful scientific methodology diagrams by optimizing component, arrow, and text correctness with structured preference learning. [Project](https://microsoft.github.io/SciForma/index.html) · [Code](https://github.com/microsoft/SciForma) (`training + inference`) · [Weights](https://huggingface.co/LoYuXrqw/SciForma-9B) (`released`).<br>  **Method:** Structure-faithful scientific diagram diffusion with M-DPO · **Base:** FLUX.2-klein-base-9B · **Train:** SciFormaData-700K · **Eval:** SciFormaBench-2K; AIBench · **Output:** Raster scientific methodology diagram · **Checked:** 2026-10-06.
- [AutoFigure-Edit](https://arxiv.org/abs/2603.06674) - Generates fully editable SVG scientific illustrations from long-form scientific text with reference-guided styling and interactive refinement. [Project](https://deepscientist.cc/) · [Code](https://github.com/ResearAI/AutoFigure-Edit) (`pipeline`) · Weights: `n/a`.<br>  **Method:** Editable scientific illustration generation and refinement · **Base:** Configurable multimodal and segmentation models · **Train:** None · **Output:** Editable SVG · **Checked:** 2026-10-06.
- [AutoFigure](https://arxiv.org/abs/2602.03828) - Uses an agentic planning, recombination, validation, and rendering pipeline to generate publication-ready scientific illustrations from long-form text (ICLR 2026). [Project](https://deepscientist.cc/) · [Code](https://github.com/ResearAI/AutoFigure) (`pipeline`) · Weights: `n/a`.<br>  **Method:** Agentic scientific illustration generation and iterative refinement · **Base:** Configurable LLM and image-generation APIs · **Train:** None · **Eval:** FigureBench · **Output:** SVG; mxGraph XML; PNG preview · **Checked:** 2026-10-06.
- [PaperBanana](https://arxiv.org/abs/2601.23265) - Uses specialized retrieval, planning, styling, visualization, and critique agents to generate publication-ready academic illustrations. [Project](https://dwzhu-pku.github.io/PaperBanana/) · [Code](https://github.com/google-research/papervizagent) (`pipeline`) · Weights: `n/a`.<br>  **Method:** Reference-driven multi-agent academic illustration generation · **Base:** Configurable VLM and image-generation models · **Train:** None · **Eval:** PaperBananaBench · **Output:** Raster methodology diagrams and statistical plots · **Checked:** 2026-10-06.
### Scientific Poster and Slide Generation

#### 2026

- [PosterForest](https://arxiv.org/abs/2608.13149) - Uses a multi-agent retrieval and layout pipeline to generate editable scientific posters from academic papers.
- [Paper2Poster](https://arxiv.org/abs/2606.04105) - Converts scholarly papers into structured academic posters with content selection, layout planning, and rendering.
- [PosterGen](https://arxiv.org/abs/2605.11528) - Generates research posters with LLM-guided content extraction, visual planning, and iterative refinement.
#### 2025

- [P2P](https://arxiv.org/abs/2505.17104) - Uses a multi-agent pipeline to generate HTML academic posters from papers and introduces instruction data and fine-grained evaluation.
- [Scientific Poster Generation A New Dataset and Approach](https://doi.org/10.1016/j.patcog.2025.111507) - Introduces the 1,226-poster Sci-PosterLayout dataset and a template-free sequence generator with a Design Pattern Schema for scientific-poster layouts (Pattern Recognition 2025).
#### 2024

- [SciPostLayout](https://arxiv.org/abs/2407.19787) - Targets structured layout generation for scientific posters. Project: — · [Code](https://github.com/omron-sinicx/scipostlayout) (`training + inference`) · Weights: `n/a`.<br>  **Method:** Scientific-poster layout analysis and generation baselines · **Base:** LayoutLMv3; DiT; LayoutDM; LayoutFormer++; GPT-4 · **Train:** SciPostLayout · **Eval:** SciPostLayout · **Output:** Scientific-poster layouts · **Checked:** 2026-10-06.
## Datasets and Benchmarks

Datasets provide reusable examples, assets, annotations, or corpora for training and evaluation. Benchmarks add a fixed task, split, protocol, or test set. Because many resources serve both roles, they are listed once in this combined section.

### 2026

- [PAd1M](https://github.com/JD-GenX/Uni-AdGen#3-pad1m-dataset) - Provides personalized advertising image-text examples and user-history conditioning for general and personalized advertisement generation; the test set and a training preview are public.
- [E-comIQ-ZH](https://arxiv.org/abs/2602.21698) - Evaluates Chinese e-commerce posters with expert-aligned multidimensional scores and chain-of-thought rationales through E-comIQ-18k and E-comIQ-Bench (CVPR 2026).
- [AutoPP1M](https://github.com/JD-GenX/AutoPP#-datasets) - Provides one million product posters and online-feedback data for poster generation and CTR-oriented preference optimization.
- [SciFormaData-700K](https://huggingface.co/datasets/microsoft/SciFormaData-700K) - Provides 661K scientific-diagram generation pairs and 70K editing triplets for structure-faithful diagram modeling.
- [SciFormaBench](https://huggingface.co/datasets/microsoft/SciFormaBench) - Provides 2,000 human-verified scientific-diagram prompts across simple, medium, and hard splits with component, arrow, and text inventories.
- [GENFIG1](https://arxiv.org/abs/2604.15278) - Benchmarks source-to-figure generation with more than 10,000 expert-annotated scientific figures and paper context across eight disciplines.
- [AIBench](https://arxiv.org/abs/2602.11920) - Provides 1,200 publication-quality scientific methodology figures with prompts and structured human evaluation for academic illustration generation.
- [FigureBench](https://huggingface.co/datasets/WestlakeNLP/FigureBench) - Provides 3,300 long-form paper, survey, blog, and textbook inputs for evaluating publication-ready scientific illustration generation.
- [SciFlow-Bench](https://arxiv.org/abs/2603.22059) - Evaluates scientific diagram generation on structural topology, semantic alignment, and visual quality across multidisciplinary methodology figures.
### 2025

- [AdProd-100K](https://github.com/Anonymous-Name-139/RefAdgen) - Provides product images, advertising images, masks, and text descriptions for high-fidelity product-preserving advertising generation.
- [PITA](https://tianchi.aliyun.com/dataset/209898) - Provides 38,017 product-centric e-commerce advertising designs with product masks, foreground/background prompts, and graphic and nongraphic element layouts.
- [ProImage-Bench](https://github.com/kodenii/TechImage-Bench) - Provides rubric-based professional-image evaluation with 654 tasks, 6,076 criteria, and 44,131 binary checks across scientific and technical imagery.
- [PPTArena](https://arxiv.org/abs/2512.03042) - Benchmarks natural-language PowerPoint editing over real decks with structural and visual evaluation and introduces the PPTPilot editing agent (ECCV 2026).
- [GenPoster-100K](https://huggingface.co/datasets/creative-graphic-design/GenPoster100K) - Poster data with rendered backgrounds, PSD references, and layer-level typography, color, and geometry annotations.
- [SciGA-145k](https://huggingface.co/datasets/iyatomilab/SciGA) - Provides a large-scale scientific-paper and figure corpus with graphical abstracts plus intra-paper and inter-paper graphical-abstract recommendation tasks.
- [PrismLayersPro](https://huggingface.co/datasets/artplus/PrismLayersPro) - Provides 20K human-filtered multi-layer transparent images with RGBA layers, captions, layouts, and style labels for layered-generation research.
- [SridBench](https://arxiv.org/abs/2505.22126) - Benchmarks scientific illustration generation with 1,120 expert-curated instances across 13 disciplines and six quality dimensions.
- [BannerRequest400](https://huggingface.co/datasets/creative-graphic-design/BannerRequest400) - Advertising banner requests with brand logos, multimodal design instructions, and target designs.
- [Sci-PosterLayout](https://github.com/kitman0000/Sci-PosterLayout-Data) - Contains 1,226 scientific poster layouts spanning diverse domains and content attributes for scientific-poster generation.
### 2024

- [RF1M](https://github.com/JD-GenX/Reliable_AD#rf1m-dataset) - Provides more than one million human-annotated generated advertising images labeled for availability and common product-background generation failures.
- [LayerD Demo Dataset](https://huggingface.co/datasets/cyberagent/crello-l2i-demo) - Provides Crello-derived examples for raster-to-layer decomposition demos and evaluation.
- [SciPostLayout](https://github.com/omron-sinicx/scipostlayout) - Provides structured scientific-poster layouts and associated metadata for analyzing and generating academic posters.
- [CGL](https://huggingface.co/datasets/creative-graphic-design/CGL) - Contains content-aware graphic-layout examples with background images, foreground elements, text, and element geometry.
- [PKU PosterLayout](https://huggingface.co/datasets/creative-graphic-design/PKU-PosterLayout) - Poster images, saliency/content inputs, and annotated element boxes for content-aware poster layout generation.
- [Crello](https://huggingface.co/datasets/creative-graphic-design/Crello) - Provides template-based vector graphic designs with editable elements, text, geometry, and visual attributes.
- [SciFigQual-Bench](https://arxiv.org/abs/2409.02518) - Evaluates scientific-figure quality with expert-derived criteria covering correctness, readability, aesthetics, and communicative effectiveness.
### 2021

- [RICO](https://huggingface.co/datasets/creative-graphic-design/RICO) - Contains mobile application UI layouts used extensively to train and evaluate structured layout-generation models.
### 2018

- [PubLayNet](https://huggingface.co/datasets/creative-graphic-design/PubLayNet) - Provides large-scale document-layout annotations derived from PubMed Central articles.
- [Magazine](https://huggingface.co/datasets/creative-graphic-design/Magazine) - Contains fine-grained polygon layouts and semantic element labels for magazine pages.
- [CTXFont](https://huggingface.co/datasets/creative-graphic-design/CTXFont) - Web-design screenshots with text-element boxes, font properties, and contextual metadata.
## Evaluation Methods and Metrics

Reusable scoring methods and evaluation procedures that compare generated designs independently of any single dataset or benchmark.

### 2026

- [PBS](https://github.com/JD-GenX/Uni-AdGen/tree/main/PBS_metrics) - Measures product-background similarity for evaluating advertising-image generation independently of text-generation metrics.
### 2024

- [LTSim](https://arxiv.org/abs/2405.17888) - Measures layout similarity with a learned transformer representation that better reflects structural correspondence (ECCV 2024).
- [Graphic Design Evaluation](https://arxiv.org/abs/2402.14103) - Evaluates graphic designs against established visual-design principles using multimodal models.
- [Layout FID](https://arxiv.org/abs/2401.16316) - Proposes a learned Fréchet-style metric for comparing generated and real layout distributions (CVPR 2024).
## Models and Implementations

- [CreatiDesign](https://github.com/creative-graphic-design/CreatiDesign) - Research implementation and tooling for multimodal creative graphic-design generation.
- [design-generators](https://github.com/creative-graphic-design/design-generators) - Unified ports of layout and graphic-design generation models to transformers, diffusers, and pydantic-ai.
- [Graphic-design-evaluation](https://github.com/creative-graphic-design/Graphic-design-evaluation) - Evaluation code and resources for visual-design quality assessment.
- [gpt-graphic-design-evaluator](https://github.com/creative-graphic-design/gpt-graphic-design-evaluator) - Multimodal evaluator for graphic-design outputs using GPT-family models.
- [Qwen-Image EliGen Poster](https://huggingface.co/DiffSynth-Studio/Qwen-Image-EliGen-Poster) - Provides Qwen-Image LoRA weights specialized for e-commerce poster generation with precise region-mask control over poster entities.
## Relevant Venues and Journals

Recurring publication venues worth monitoring for work in this area. Inclusion here indicates relevance to the field, not that every paper at the venue is in scope.

### Conferences

- [AAAI Conference on Artificial Intelligence (AAAI)](https://aaai.org/conference/aaai/) - Artificial intelligence conference where multimodal generation, planning, and design systems regularly appear.
- [ACM Conference on Human Factors in Computing Systems (CHI)](https://chi.acm.org/) - Human-computer interaction venue for design tools, creative assistance, and authoring workflows.
- [ACM International Conference on Multimedia (ACM MM)](https://acmmm2026.org/) - Multimedia venue that frequently publishes layout, poster, multimodal-generation, and evaluation work.
- [ACM SIGGRAPH](https://www.siggraph.org/) - Computer graphics venue relevant to visual synthesis, authoring, and design systems.
- [ACM SIGGRAPH Asia](https://asia.siggraph.org/) - Computer graphics venue relevant to visual synthesis, authoring, and design systems in the Asia-Pacific community.
- [Computer Vision and Pattern Recognition Conference (CVPR)](https://cvpr.thecvf.com/) - Computer vision venue with frequent work on layout, text rendering, multimodal generation, and evaluation.
- [European Conference on Computer Vision (ECCV)](https://eccv.ecva.net/) - Computer vision venue with frequent work on layout, visual generation, and multimodal design.
- [International Conference on Computer Vision (ICCV)](https://iccv.thecvf.com/) - Computer vision venue with frequent work on layout, poster generation, multimodal design, and evaluation.
- [International Conference on Learning Representations (ICLR)](https://iclr.cc/) - Machine-learning venue relevant to generative modeling, structured generation, and multimodal reasoning.
- [International Conference on Machine Learning (ICML)](https://icml.cc/) - Machine-learning venue relevant to generative modeling, structured prediction, and optimization for design.
- [International Joint Conference on Artificial Intelligence (IJCAI)](https://www.ijcai.org/) - Artificial intelligence venue relevant to multimodal generation and design automation.
- [Neural Information Processing Systems (NeurIPS)](https://neurips.cc/) - Machine-learning venue relevant to generative modeling, multimodal systems, and evaluation.
### Journals

- [ACM Transactions on Graphics (TOG)](https://dl.acm.org/journal/tog) - Graphics journal associated with SIGGRAPH and graphics/authoring research.
- [IEEE Transactions on Visualization and Computer Graphics (TVCG)](https://www.computer.org/csdl/journal/tg) - Visualization and graphics journal with work on layout, design tools, and visual communication.
- [International Journal of Computer Vision (IJCV)](https://link.springer.com/journal/11263) - Computer vision journal relevant to visual generation and multimodal understanding.
- [Pattern Recognition](https://www.sciencedirect.com/journal/pattern-recognition) - Pattern-recognition journal that publishes layout, multimodal, and visual-generation research.
## Related Resources

- [Awesome Layout Generation](https://github.com/PKU-ICST-MIPL/awesome-layout-generation) - Related curated list focused specifically on layout generation research.
## Contributing

Contributions are welcome. Please read the [contribution guidelines](CONTRIBUTING.md) before opening a pull request.
