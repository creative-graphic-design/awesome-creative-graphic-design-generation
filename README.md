# Awesome Creative Graphic Design Generation [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![Catalog Check](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/workflows/catalog-check.yml/badge.svg)](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/workflows/catalog-check.yml)
[![Awesome Lint](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/workflows/awesome-lint.yml/badge.svg)](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/workflows/awesome-lint.yml)
![Total Resources](https://img.shields.io/badge/resources-220-informational)
![Papers](https://img.shields.io/badge/papers-165-informational)
![Datasets and Benchmarks](https://img.shields.io/badge/datasets%20%26%20benchmarks-39-informational)
![Reproducibility Audited](https://img.shields.io/badge/reproducibility%20audited-46-informational)
![Method Classified](https://img.shields.io/badge/method%20classified-165-informational)

<!-- This file is generated from data/*.csv by scripts/generate_readme.py. Do not edit it directly. -->

Curated resources for generating, editing, representing, and evaluating composed graphic-design artifacts such as posters, advertisements, social-media graphics, magazine layouts, scientific figures, graphical abstracts, scientific posters, slides, banners, and related visual compositions.

This list focuses on work where layout, typography, visual elements, editable structure, or design-specific evaluation is a first-class part of the problem. Generic text-to-image generation and generic image editing are out of scope unless they make a direct contribution to graphic-design generation.

Research resources are ordered by **first public appearance** within each category, from newest to oldest. The sort key is the earlier of the arXiv v1 date and the venue/presentation date when both are known; journal-only work uses its first public publication date.

Implementation metadata is tracked in [`data/paper_metadata.csv`](data/paper_metadata.csv). The orthogonal model/method taxonomy is tracked in [`data/paper_methods.csv`](data/paper_methods.csv). Verified implementation entries expose project pages, official code and weight-release status, method/base model, training and evaluation datasets, output representation, and the date the release status was last checked.

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
- [Method and Architecture Index](#method-and-architecture-index)
- [Datasets and Benchmarks](#datasets-and-benchmarks)
- [Evaluation Methods and Metrics](#evaluation-methods-and-metrics)
- [Models and Implementations](#models-and-implementations)
- [Relevant Venues and Workshops](#relevant-venues-and-workshops)
  - [Conferences](#conferences)
  - [Journals](#journals)
  - [Workshops](#workshops)
- [Related Resources](#related-resources)

## Surveys and Overviews

### 2025

- [From Fragment to One Piece: A Survey on AI-Driven Graphic Design](https://arxiv.org/abs/2503.18641) - Reviews AI-driven graphic-design generation across layout, visual content, text, and integrated systems (2025).
### 2023

- [Intelligent Layout Generation Based on Deep Generative Models: A Comprehensive Survey](https://doi.org/10.1016/j.inffus.2023.101940) - Reviews deep generative approaches to layout generation, their representations, conditions, datasets, and evaluation (Information Fusion 2023).
- [A Survey for Graphic Design Intelligence](https://arxiv.org/abs/2309.01371) - Surveys computational methods for understanding and generating graphic design artifacts (2023).
## Papers

Papers are classified by their **primary output and task**, rather than by model family. LLM-, VLM-, diffusion-, and agent-based approaches can therefore appear in any category.

<ul>
<li><strong>Layout Generation:</strong> Outputs structured element geometry or arrangement without relying on the visual content of a target canvas.</li>
<li><strong>Content-Aware Layout Generation:</strong> Still outputs layout or placement, but conditions that geometry on a background image, product/brand assets, saliency, element content, or another visual canvas.</li>
<li><strong>Graphic Design Generation:</strong> Goes beyond geometry to create a composed design artifact, such as backgrounds, imagery, typography, styles, layers, or editable HTML/CSS/PSD/PPTX structures.</li>
<li><strong>Composable and Layered Asset Generation:</strong> Produces transparent, separable, layered, chroma-keyed, or intentionally empty-space visual assets that can be independently composed or edited in downstream design workflows.</li>
<li><strong>Typography and Text Rendering:</strong> Focuses primarily on legible, faithful, or stylized text generation and placement within designed imagery.</li>
<li><strong>Graphic Design Editing and Reconstruction:</strong> Focuses on iterative editing, layer recovery, or conversion of rendered designs back into editable structures.</li>
<li><strong>Scientific Figure and Graphical Abstract Generation:</strong> Converts scientific papers or long-form technical content into methodology figures, diagrams, Figure 1-style summaries, or graphical abstracts, including editable vector outputs.</li>
<li><strong>Scientific Poster and Slide Generation:</strong> Covers research communication workflows that combine source-document understanding, content selection, layout, typography, rendering, and often editable poster or slide output.</li>
</ul>

### Layout Generation

#### 2026

- [i-Design](https://link.springer.com/chapter/10.1007/978-3-032-14826-1_18) - Optimizes graphic layout design step by step with progressive aesthetic policy optimization (ECCV 2026).
#### 2025

- [Sketch-to-Layout](https://arxiv.org/abs/2510.27632) - Generates layouts from intuitive user sketches and content assets with a multimodal Transformer and releases large-scale synthetic sketch supervision (ICCV 2025 HiGen Workshop).
- [LayoutRectifier](https://arxiv.org/abs/2508.11177) - Rectifies generated graphic layouts with two-stage optimization over grid alignment, overlap, and containment while limiting deviation from the input layout (Pacific Graphics 2025).
- [StructLayoutFormer](https://doi.org/10.1109/TVCG.2025.3574311) - Generates explicitly structured layouts with a Transformer using structure serialization and disentanglement for conditional structure control (TVCG 2025).
- [CLASS](https://openaccess.thecvf.com/content/WACV2025/html/Manandhar_CLASS_Conditional_Latent_Architecture_for_Search_and_Synthesis_of_Design_WACV_2025_paper.html) - Unifies layout synthesis and retrieval with a variational latent representation, an autoregressive Transformer layout decoder, and a raster decoder (WACV 2025).
- [LGGPT](https://arxiv.org/abs/2502.14005) - Unifies multiple layout-generation tasks and domains with compact instruction and response encodings for a 1.5B-parameter large language model.
#### 2024

- [LayoutKAG: Enhancing Layout Generation in Large Language Models Through Knowledge-Augmented Generation](https://doi.org/10.1109/AIHCIR65563.2024.00056) - Uses knowledge-augmented generation to improve large-language-model layout generation and control (AIHCIR 2024).
- [TextLap](https://arxiv.org/abs/2410.12844) - Generates graphic layouts from textual design requirements with language-model-based reasoning.
- [Layout-Corrector](https://arxiv.org/abs/2409.16689) - Corrects intermediate diffusion layouts to improve structure and constraint satisfaction (ECCV 2024).
- [CoLay](https://arxiv.org/abs/2405.13045) - Uses multi-conditional latent diffusion to generate layouts with style properties from flexible combinations of text, guidelines, element types, and partial designs.
- [LayoutFlow](https://arxiv.org/abs/2403.18187) - Uses flow matching for continuous structured layout generation (ECCV 2024). Project: — · [Code](https://github.com/JulianGuerreiro/LayoutFlow) (`training + inference`) · [Weights](https://huggingface.co/JulianGuerreiro/LayoutFlow) (`released`).<br>  **Method:** Flow-matching model for continuous layout generation · **Base:** Transformer-style layout backbone · **Train:** RICO; PubLayNet · **Eval:** RICO; PubLayNet · **Output:** Structured layout boxes · **Checked:** 2026-10-06.
- [LACE](https://arxiv.org/abs/2402.04754) - Introduces lightweight diffusion for controllable layout generation (ICLR 2024).
- [Spot the Error](https://arxiv.org/abs/2401.16375) - Improves non-autoregressive graphic-layout generation with a learned wireframe locator that identifies erroneous layout tokens for iterative refinement (AAAI 2024).
#### 2023

- [LayoutPrompter](https://arxiv.org/abs/2311.06495) - Prompts large language models for zero-shot and few-shot visual layout generation (NeurIPS 2023). Project: — · [Code](https://github.com/microsoft/LayoutGeneration/tree/main/LayoutPrompter) (`pipeline`) · Weights: `n/a`.<br>  **Method:** Training-free in-context LLM layout prompting · **Base:** GPT-family API models · **Train:** None · **Eval:** RICO; PubLayNet; PKU PosterLayout; WebUI · **Output:** Structured layout boxes · **Checked:** 2026-10-06.
- [Dolfin](https://arxiv.org/abs/2310.16305) - Uses a diffusion layout transformer without an autoencoder for structured layout generation (ECCV 2024).
- [LayoutNUWA](https://arxiv.org/abs/2309.09506) - Represents visual layouts as code for language-model-based generation and reasoning (ICLR 2024). Project: — · [Code](https://github.com/ProjectNUWA/LayoutNUWA) (`training + inference`) · Weights: `unknown`.<br>  **Method:** Code-generation formulation for layout generation · **Base:** LLaMA2-7B; CodeLLaMA-7B · **Train:** RICO; PubLayNet; Magazine · **Eval:** RICO; PubLayNet; Magazine · **Output:** HTML/code-form layout representation · **Checked:** 2026-10-06.
- [Parse-Then-Place](https://arxiv.org/abs/2308.12700) - Parses textual design descriptions into structured constraints before placing graphic elements (ICCV 2023).
- [Learn and Sample Together](https://www.ijcai.org/proceedings/2023/649) - Jointly trains a spatial-graph generator and graph-conditioned layout decoder with collaborative knowledge transfer for constrained graphic-layout generation (IJCAI 2023).
- [LayoutGPT](https://arxiv.org/abs/2305.15393) - Uses large language models with in-context demonstrations for layout generation (NeurIPS 2023).
- [LayoutDM: Transformer-Based Diffusion Model for Layout Generation](https://arxiv.org/abs/2305.02567) - Instantiates conditional DDPM layout generation with a purely Transformer-based denoiser for diverse, high-quality conditional layouts (CVPR 2023).
- [Layout Generation for Various Scenarios in Mobile Shopping Apps](https://doi.org/10.1145/3544548.3581446) - Introduces LayoutVQ-VAE, a discrete latent model for generating layouts under internal and scenario-level constraints in mobile shopping applications (CHI 2023).
- [FlexDM](https://arxiv.org/abs/2303.18248) - Supports flexible layout generation and completion through masked multi-field diffusion (CVPR 2023).
- [LayoutDiffusion](https://arxiv.org/abs/2303.11589) - Uses discrete diffusion for controllable layout generation (ICCV 2023).
- [LayoutDM](https://arxiv.org/abs/2303.08137) - Models layouts with discrete denoising diffusion and supports multiple conditional generation tasks (CVPR 2023). [Project](https://cyberagentailab.github.io/layout-dm) · [Code](https://github.com/CyberAgentAILab/layout-dm) (`training + inference`) · [Weights](https://github.com/CyberAgentAILab/layout-dm/releases/tag/v1.0.0) (`released`).<br>  **Method:** Discrete diffusion model for controllable layout generation · **Base:** Transformer-style discrete denoiser · **Train:** RICO; PubLayNet · **Eval:** RICO; PubLayNet · **Output:** Structured layout boxes · **Checked:** 2026-10-06.
- [LDGM](https://arxiv.org/abs/2303.05049) - Decouples discrete element attributes and continuous geometry in a diffusion model for unified layout generation (CVPR 2023).
- [DLT](https://arxiv.org/abs/2303.03755) - Applies diffusion modeling to structured layout generation (ICCV 2023).
- [LayoutAction](https://ojs.aaai.org/index.php/AAAI/article/view/26277) - Frames autoregressive layout generation as a sequence of placement actions (AAAI 2023).
- [PLay](https://arxiv.org/abs/2301.11529) - Uses parametrically conditioned latent diffusion for controllable layout generation (ICML 2023).
- [Machine Learning Model to Evaluate the Appropriateness of Layout for Automatic Generation of Graphic Design Works](https://doi.org/10.1109/IMCOM56909.2023.10035646) - Uses adversarial layout generation and a trained discriminator to generate and score graphic-design layouts conditioned on specified materials (IMCOM 2023).
#### 2022

- [LayoutFormer++](https://arxiv.org/abs/2208.08037) - Treats layout generation as a sequence-to-sequence task with unified conditioning (CVPR 2023). Project: — · [Code](https://github.com/microsoft/LayoutGeneration/tree/main/LayoutFormer%2B%2B) (`training + inference`) · [Weights](https://huggingface.co/jzy124/LayoutFormer) (`released`).<br>  **Method:** Conditional sequence-to-sequence layout generation · **Base:** Transformer encoder-decoder · **Train:** RICO; PubLayNet · **Eval:** RICO; PubLayNet · **Output:** Serialized/discretized layout boxes · **Checked:** 2026-10-06.
- [Coarse-to-Fine](https://ojs.aaai.org/index.php/AAAI/article/view/19994) - Generates layouts hierarchically from coarse global structure to fine element placement (AAAI 2022).
#### 2021

- [Layout-BLT](https://arxiv.org/abs/2112.05112) - Uses bidirectional layout transformers to generate and refine object arrangements (ECCV 2022).
- [LayoutMCL](https://arxiv.org/abs/2301.06629) - Uses an autoregressive multi-choice predictor with winner-takes-all learning to generate diverse multimedia layouts from the same input (ACM MM 2021).
- [CanvasVAE](https://arxiv.org/abs/2108.01249) - Uses a variational autoencoder to model element-level layouts for design documents (ICCV 2021).
- [Constrained Graphic Layout Generation via Latent Optimization](https://arxiv.org/abs/2108.00871) - Introduces LayoutGAN++ and constrained latent optimization for generating realistic layouts that satisfy alignment, overlap, and other explicit design constraints (ACM MM 2021). Project: — · [Code](https://github.com/ktrk115/const_layout) (`training + inference`) · Weights: `released`.<br>  **Method:** GAN-based structured layout generation · **Base:** Transformer generator and discriminator · **Train:** RICO; PubLayNet · **Eval:** RICO; PubLayNet · **Output:** Structured layout boxes · **Checked:** 2026-10-06.
- [VTN](https://arxiv.org/abs/2104.02416) - Combines self-attention with a variational autoencoder to learn global design rules and synthesize diverse layouts (CVPR 2021).
#### 2020

- [DeepLayout](https://arxiv.org/abs/2006.14615) - Models layouts autoregressively as sequences for conditional and unconditional generation (ICCV 2021).
- [AC-LayoutGAN](https://doi.org/10.1109/TVCG.2020.2999335) - Generates graphic layouts conditioned on element attributes such as area, aspect ratio, and reading order with an attribute-conditioned GAN (TVCG).
#### 2019

- [Neural Design Network](https://arxiv.org/abs/1912.09421) - Generates graphic layouts under explicit design constraints with a neural structured model (ECCV 2020).
- [READ: Recursive Autoencoders for Document Layout Generation](https://arxiv.org/abs/1909.00302) - Generates hierarchical document layouts with a recursive variational autoencoder and introduces a structural similarity metric for dense document compositions (CVPRW 2020).
- [LayoutVAE](https://arxiv.org/abs/1907.10719) - Uses a label-conditioned variational autoencoder for structured document layout generation (ICCV 2019).
- [LayoutGAN](https://openreview.net/forum?id=HJxB5sRcFQ) - Introduces a GAN formulation for synthesizing layouts represented by labeled geometric elements (ICLR 2019).
#### 2015

- [DesignScape](https://doi.org/10.1145/2702123.2702149) - Provides interactive refinement and brainstorming layout suggestions that improve position, scale, and alignment during graphic-design authoring (CHI 2015).
#### 2014

- [Learning Layouts for Single-Page Graphic Designs](https://doi.org/10.1109/TVCG.2014.48) - Learns layout relationships from existing single-page graphic designs to support automatic composition (TVCG 2014).
### Content-Aware Layout Generation

#### 2026

- [iPoster](https://arxiv.org/abs/2603.29469) - Supports interactive content-aware poster layout generation under flexible user-specified constraints (CHI EA 2026).
- [Seeing is Improving: Visual Feedback for Iterative Text Layout Refinement](https://arxiv.org/abs/2603.22187) - Introduces VFLM, which iteratively renders and visually critiques SVG text layouts over background images, using visually grounded reinforcement learning to improve readability and aesthetics (CVPR 2026). Project: — · [Code](https://github.com/FolSpark/VFLM) (`training + inference`) · Weights: `released`.<br>  **Method:** Visual-feedback multimodal layout refinement with supervised and reinforcement learning · **Base:** Qwen2.5-VL 3B/7B · **Eval:** Multiple text-layout benchmarks · **Output:** SVG layout · **Checked:** 2026-10-06.
#### 2025

- [UniLayDiff](https://arxiv.org/abs/2512.08897) - Unifies diverse content-aware layout constraints in a single multimodal diffusion transformer with relation-aware LoRA adaptation.
- [Learning Priority-Aware Controllable Poster Layout Generation](https://doi.org/10.1016/j.patcog.2026.113497) - Uses LLM- and vision-derived priorities, optimal-transport matching, and flow-based refinement for controllable poster layout generation (Pattern Recognition 2026).
- [SEGA](https://arxiv.org/abs/2510.15749) - Uses stepwise evolution for content-aware poster layout generation and introduces GenPoster-100K (ICCV 2025).
- [LLMs as Layout Designers (LaySPA)](https://arxiv.org/abs/2509.16891) - Augments language-model layout agents with reinforcement-learned spatial reasoning over geometric validity, structural fidelity, and visual quality.
- [Uni-Layout](https://arxiv.org/abs/2508.02374) - Unifies multiple layout-generation conditions with human-feedback-based evaluation and preference alignment (ACM MM 2025).
- [ReLayout: Relation Reasoning for Content-Aware Layout Generation](https://arxiv.org/abs/2507.05568) - Uses relation chain-of-thought and layout-prototype rebalancing to improve structure, diversity, and explainability in multimodal-LLM content-aware layouts.
- [CAL-RAG](https://arxiv.org/abs/2506.21934) - Combines multimodal retrieval, an LLM layout recommender, a vision-language grader, and feedback agents for iterative content-aware layout generation.
- [CreatiPoster](https://arxiv.org/abs/2506.10890) - Generates poster layouts from multimodal content and design requirements.
- [Scan-and-Print](https://arxiv.org/abs/2505.20649) - Uses patch-level image summarization and data augmentation for efficient content-aware poster layout generation (IJCAI 2025). [Project](https://thekinsley.github.io/Scan-and-Print/) · [Code](https://github.com/theKinsley/Scan-and-Print-IJCAI2025) (`training + inference`) · Weights: `unknown`.<br>  **Method:** Autoregressive content-aware layout generation · **Base:** DeiT3 visual encoder · **Train:** PKU PosterLayout; CGL · **Eval:** PKU PosterLayout; CGL · **Output:** Structured layout boxes · **Checked:** 2026-10-06.
- [PosterO](https://arxiv.org/abs/2505.07843) - Structures layouts as trees so language models can solve generalized layout-generation tasks (CVPR 2025).
- [AesthetiQ](https://arxiv.org/abs/2503.00591) - Aligns multimodal language models to aesthetic preferences for content-aware graphic layout prediction using preference optimization (CVPR 2025).
#### 2024

- [VASCAR](https://arxiv.org/abs/2412.04237) - Uses a large vision-language model to iteratively inspect rendered layouts and self-correct content-aware element placement without additional training.
- [Design Element Aware Poster Layout Generation](https://doi.org/10.1145/3627673.3679557) - Models poster design elements and their relationships for content-aware poster layout generation (CIKM 2024).
- [Iris: a multi-constraint graphic layout generation system](https://doi.org/10.1631/FITEE.2300312) - Combines an interactive graphic-layout design system with multi-constraint LayoutVQ-VAE for background-aware generation, editing, and rendering (FITEE 2024).
- [CGB-DM](https://arxiv.org/abs/2407.15233) - Uses a diffusion transformer for graphic-layout generation with content-aware conditioning.
- [Visual Layout Composer](https://openaccess.thecvf.com/content/CVPR2024/html/Shabani_Visual_Layout_Composer_Image-Vector_Dual_Diffusion_Model_for_Design_Layout_CVPR_2024_paper.html) - Couples image-space and vector-space diffusion to generate design layouts conditioned on visual content (CVPR 2024).
- [PosterLLaVA](https://arxiv.org/abs/2406.02884) - Uses multimodal instruction tuning for poster layout generation (IEEE TMM 2024).
- [Automatic Layout Planning for Visually-Rich Documents with Instruction-Following Models](https://arxiv.org/abs/2404.15271) - Uses a multimodal instruction-following model to arrange user-provided visual elements for posters, brochures, book covers, advertisements, and related visually rich documents (ALVR 2024).
- [Graphist](https://arxiv.org/abs/2404.14368) - Models graphic-design layouts with multimodal and structural context.
- [PosterLLaMA](https://arxiv.org/abs/2404.00995) - Adapts a multimodal language model to poster layout generation (ECCV 2024). [Project](https://lait-cvlab.github.io/PosterLlama/) · [Code](https://github.com/jaepoong/PosterLlama) (`training + inference`) · [Weights](https://huggingface.co/poong/PosterLlama) (`released`).<br>  **Method:** Vision-language model for content-aware poster layout generation · **Base:** LLaMA2-7B-chat; CodeLLaMA-7B; DINO visual features · **Train:** MiniGPT-4 synthetic caption data; CGL · **Eval:** CGL; poster-layout benchmarks · **Output:** HTML/code-form layout representation · **Checked:** 2026-10-06.
#### 2023

- [RALF](https://arxiv.org/abs/2311.13602) - Retrieves relevant design examples to guide content-aware layout generation (CVPR 2024). [Project](https://udonda.github.io/RALF/) · [Code](https://github.com/CyberAgentAILab/RALF) (`training + inference`) · Weights: `released`.<br>  **Method:** Retrieval-augmented autoregressive layout transformer · **Base:** ResNet50 image encoder; autoregressive transformer · **Train:** PKU PosterLayout; CGL · **Eval:** PKU PosterLayout; CGL · **Output:** Structured content-aware layouts · **Checked:** 2026-10-06.
- [Two-stage Content-Aware Layout Generation for Poster Designs](https://doi.org/10.1145/3581783.3612275) - Combines aesthetics-conditioned diffusion layout proposals with a learned ranking stage for poster designs over image backgrounds (ACM MM 2023).
- [RADM](https://arxiv.org/abs/2306.09086) - Generates content-aware advertising layouts with richer text and visual conditioning (CIKM 2023).
- [PosterLayout](https://arxiv.org/abs/2303.15937) - Introduces a benchmark and content-aware approach for visual-textual poster layout generation (CVPR 2023). Project: — · [Code](https://github.com/PKU-ICST-MIPL/PosterLayout-CVPR2023) (`training + inference`) · Weights: `released`.<br>  **Method:** Content-aware poster layout generation with DS-GAN · **Base:** Visual feature encoder; GAN layout generator · **Train:** PKU PosterLayout · **Eval:** PKU PosterLayout · **Output:** Structured poster layout boxes · **Checked:** 2026-10-06.
- [PDA-GAN](https://arxiv.org/abs/2303.14377) - Uses GAN-based unsupervised domain adaptation with a pixel-level discriminator to generate image-aware advertising-poster layouts (CVPR 2023).
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
- [Design Your Ad](https://arxiv.org/abs/2605.12138) - Jointly generates personalized advertising images and text from multimodal user histories with a unified autoregressive model and introduces PAd1M and PBS (CVPR 2026). Project: — · [Code](https://github.com/JD-GenX/Uni-AdGen) (`inference only`) · [Weights](https://3.cn/11f4I-YYG) (`released`).<br>  **Method:** Unified autoregressive personalized advertising image-text generation · **Base:** Janus-Pro-7B; DINOv2-small; SDXL-Base-1.0 · **Train:** PAd1M · **Eval:** PAd1M; PBS; BLEU; ROUGE · **Output:** Personalized advertising image and product text · **Checked:** 2026-10-06.
- [SIMPLEPOSTER](https://arxiv.org/abs/2605.08784) - Generates product posters with faithful subject preservation and position-controllable text rendering (CVPR 2026).
- [Brief2Design](https://arxiv.org/abs/2604.11019) - Supports prompt-based professional graphic design through requirement extraction, element exploration, and compositional recombination.
- [PSDesigner](https://arxiv.org/abs/2603.25738) - Automates layered graphic-design workflows with editable PSD structure and tool-use trajectories (CVPR 2026). [Project](https://henghuiding.com/PSDesigner) · [Code](https://github.com/FudanCVL/PSDesigner) (`announced`) · Weights: `announced`.<br>  **Method:** Tool-using layered graphic-design agent · **Base:** GraphicPlanner · **Train:** CreativePSD · **Eval:** Crello-v5; copyright-free PSD files · **Output:** Editable PSD · **Checked:** 2026-10-06.
- [Multi-Object Advertisement Creative Generation](https://arxiv.org/abs/2603.13745) - Introduces CreativeAds for scalable multi-product lifestyle advertising through product pairing, layout generation, background generation, and human oversight.
- [InnoAds-Composer](https://arxiv.org/abs/2603.05898) - Generates e-commerce product posters in a single stage with joint subject, glyph, and style conditioning (CVPR 2026).
- [PosterOmni](https://arxiv.org/abs/2602.12127) - Unifies local poster editing and global image-to-poster creation through task distillation and poster-specific reward feedback across six creation tasks (CVPR 2026). [Project](https://ephemeral182.github.io/PosterOmni/) · [Code](https://github.com/MeiGen-AI/PosterOmni) (`inference only`) · [Weights](https://huggingface.co/MeiGen-AI/PosterOmni_v1) (`released`).<br>  **Method:** Unified multi-task image-to-poster generation and editing via task distillation and reward feedback · **Base:** Qwen-Image-Edit / QwenImageEditPlusPipeline · **Train:** PosterOmni-200K · **Eval:** PosterOmni-Bench · **Output:** Raster poster image · **Checked:** 2026-10-06.
- [DesignAsCode](https://arxiv.org/abs/2602.17690) - Represents graphic designs as HTML/CSS and iteratively plans, implements, and visually refines editable designs (ACM MM 2026). [Project](https://liuziyuan1109.github.io/design-as-code/) · [Code](https://github.com/liuziyuan1109/design-as-code) (`training + inference`) · [Weights](https://huggingface.co/Tony1109/DesignAsCode-planner) (`released`).<br>  **Method:** Code-native agentic graphic-design generation · **Base:** Qwen3-8B planner; GPT-5; GPT-4o; gpt-image-1 · **Train:** DesignAsCode training data (~19K distilled Crello samples) · **Eval:** 546-sample test set; Broad test set · **Output:** Editable HTML/CSS · **Checked:** 2026-10-06.
- [PosterVerse](https://arxiv.org/abs/2601.03993) - Automates commercial poster creation with blueprint planning, background generation, and HTML-based scalable typography.
#### 2025

- [AutoPP](https://arxiv.org/abs/2512.21921) - Automates product-poster generation and CTR-oriented optimization using unified design generation and online-feedback preference learning (AAAI 2026). Project: — · [Code](https://github.com/JD-GenX/AutoPP) (`announced`) · Weights: `unknown`.<br>  **Method:** Automated product-poster generation plus CTR-oriented preference optimization · **Train:** AutoPP1M product-poster generation and optimization subsets · **Eval:** Offline poster-generation metrics; online CTR feedback · **Output:** Raster product poster · **Checked:** 2026-10-06.
- [RefAdGen](https://arxiv.org/abs/2508.11695) - Generates high-fidelity advertising images while preserving referenced product identity through spatial mask control and product-feature fusion (AAAI 2026). Project: — · [Code](https://github.com/Anonymous-Name-139/RefAdgen) (`training + inference`) · [Weights](https://huggingface.co/yiyun123/RefAdgen) (`released`).<br>  **Method:** Product-preserving advertising diffusion with spatial control and attention fusion · **Base:** Stable Diffusion v1.5; IP-Adapter; GroundingDINO; SAM2 · **Train:** AdProd-100K · **Eval:** AdProd-100K · **Output:** Raster product advertising image · **Checked:** 2026-10-06.
- [Rethinking Layered Graphic Design Generation with a Top-Down Approach](https://arxiv.org/abs/2507.05601) - Introduces Accordion, a top-down framework that creates editable layered graphic designs from user intent or sketches by using a VLM for reference creation, design planning, and layer generation (ICCV 2025).
- [DreamPoster](https://arxiv.org/abs/2507.04218) - Generates image-conditioned posters while preserving source content and supporting flexible resolution, layout, and typographic hierarchy with progressive multi-task training.
- [PosterCraft](https://arxiv.org/abs/2506.10741) - Generates high-aesthetic posters in a unified diffusion framework with staged text-rendering optimization, region-aware fine-tuning, preference optimization, and vision-language feedback (ICLR 2026). [Project](https://ephemeral182.github.io/PosterCraft/) · [Code](https://github.com/MeiGen-AI/PosterCraft) (`inference only`) · [Weights](https://huggingface.co/PosterCraft/PosterCraft-v1_RL) (`released`).<br>  **Method:** Unified diffusion poster generation with staged text and aesthetic optimization · **Base:** FLUX.1-dev · **Train:** Text-Render-2M; HQ-Poster100K · **Eval:** PosterCraft evaluation set · **Output:** Raster poster image · **Checked:** 2026-10-06.
- [CreatiDesign](https://arxiv.org/abs/2505.19114) - Uses a multi-conditional diffusion transformer to compose primary visuals, decorative elements, text, and layout for graphic design. [Project](https://huizhang0812.github.io/CreatiDesign/) · [Code](https://github.com/HuiZhang0812/CreatiDesign) (`inference only`) · [Weights](https://huggingface.co/HuiZhang0812/CreatiDesign) (`released`).<br>  **Method:** Multi-conditional diffusion transformer · **Base:** FLUX.1-dev · **Train:** CreatiDesign dataset (~400K designs) · **Eval:** CreatiDesign benchmark (1K samples) · **Output:** Raster graphic design · **Checked:** 2026-10-06.
- [BizGen](https://arxiv.org/abs/2503.20672) - Generates infographic and slide imagery from article-length prompts and ultra-dense layouts using layout-guided cross-attention and region-wise latent refinement (CVPR 2025).
- [POSTA](https://arxiv.org/abs/2503.14908) - Combines background diffusion, multimodal layout and typography planning, and stylized text generation for customizable artistic posters (CVPR 2025).
- [BannerAgency](https://arxiv.org/abs/2503.11060) - Uses collaborating multimodal LLM agents to plan and generate advertising banner designs from brand assets and requests (2025).
- [DesignDiffusion: High-Quality Text-to-Design Image Generation with Diffusion Models](https://arxiv.org/abs/2503.01645) - Generates complete design images directly from text with a one-stage diffusion model, character-aware embeddings and localization supervision, plus self-play preference optimization for visual-text quality (CVPR 2025).
- [PAID](https://arxiv.org/abs/2501.14316) - Generates product-centric advertising images through VLM prompt and layout experts, SDXL-based background generation, and final graphics rendering (2025).
#### 2024

- [LaDeCo](https://arxiv.org/abs/2412.19712) - Generates layered and editable graphic designs rather than flattened images (CVPR 2025).
- [Towards Reliable Advertising Image Generation Using Human Feedback](https://arxiv.org/abs/2408.00418) - Uses a learned reliable-feedback network, recurrent generation, and feedback-guided diffusion fine-tuning to improve usable e-commerce advertising images (ECCV 2024). Project: — · [Code](https://github.com/JD-GenX/Reliable_AD) (`inference only`) · [Weights](https://huggingface.co/ZhenbangDu/reliable_controlnet) (`released`).<br>  **Method:** Reliable-feedback-guided recurrent advertising generation and diffusion fine-tuning · **Base:** Stable Diffusion v1.5-compatible latent diffusion; ControlNet · **Train:** RF1M · **Eval:** RF1M; human availability feedback · **Output:** Raster product advertising image · **Checked:** 2026-10-06.
- [OpenCOLE](https://arxiv.org/abs/2406.08232) - Provides an open and reproducible pipeline for automatic layered graphic-design generation (CVPR Workshop 2024).
- [Desigen](https://arxiv.org/abs/2403.09093) - Jointly generates advertising backgrounds and foreground element layouts (CVPR 2024).
- [Chaining Text-to-Image and Large Language Model for Personalized E-commerce Banners](https://arxiv.org/abs/2403.05578) - Chains an LLM with text-to-image generation to turn shopper interaction and product metadata into personalized e-commerce banner imagery at scale (KDD 2024).
- [CG4CTR](https://arxiv.org/abs/2401.10934) - Builds a Stable-Diffusion-based advertising-creative generation pipeline that incorporates user preferences and downstream click-through-rate ranking (WWW 2024 Companion).
#### 2023

- [Planning and Rendering](https://arxiv.org/abs/2312.08822) - Separates semantic planning from visual rendering for end-to-end product-poster generation (2023).
- [COLE](https://arxiv.org/abs/2311.16974) - Uses a hierarchical generation framework to create multi-layered, editable graphic designs from high-level intent (2023).
- [AutoPoster](https://arxiv.org/abs/2308.01095) - Integrates content analysis and layout generation into an automatic advertising-poster design system (2023).
#### 2022

- [CreaGAN](https://doi.org/10.1145/3503161.3548763) - Automates display-ad creative adaptation with aesthetics-aware product placement and context-aware inpainting while reusing existing design elements (ACM MM 2022).
#### 2021

- [Vinci](https://doi.org/10.1145/3411764.3445117) - Introduces an intelligent graphic-design system that composes advertising posters from user-provided product assets and design intent (CHI 2021).
### Composable and Layered Asset Generation

#### 2026

- [MRT](https://arxiv.org/abs/2605.27235) - Unifies text-to-layers, image-to-layers, and layer-to-layer editing in a 20B masked-region diffusion model for scalable RGBA asset generation (CVPR 2026). [Project](https://mrt-cvpr.github.io/) · Code: `unknown` · Weights: `unknown`.<br>  **Method:** Masked-region diffusion for unified layered generation and editing · **Base:** Qwen-Image · **Train:** 10M+ multilingual layered design samples; 43M+ transparent layers · **Output:** RGBA canvas/background/foreground layer stack · **Checked:** 2026-10-06.
- [LaDe: Unified Multi-Layered Graphic Media Generation and Decomposition](https://arxiv.org/abs/2603.17965) - Jointly generates full graphic-media designs and a flexible number of semantically meaningful RGBA layers, while also supporting image-to-layers decomposition with a latent diffusion transformer and RGBA VAE.
- [Controllable Layered Image Generation for Real-World Editing](https://arxiv.org/abs/2601.15507) - Introduces LASAGNA, a unified controllable framework that jointly generates composites, clean backgrounds, and transparent foreground layers with physically grounded visual effects.
#### 2025

- [Qwen-Image-Layered](https://arxiv.org/abs/2512.15603) - Decomposes raster images into variable-length semantically separated RGBA layers for independently editable visual assets (CVPR 2026). [Project](https://qwen.ai/blog?id=qwen-image-layered&lid=1ami72hcYlwXGTTVQ) · [Code](https://github.com/QwenLM/Qwen-Image-Layered) (`inference only`) · [Weights](https://huggingface.co/Qwen/Qwen-Image-Layered) (`released`).<br>  **Method:** Variable-layer image decomposition diffusion model · **Base:** Qwen-Image · **Train:** Internal text-to-RGB/RGBA data; PSD-derived multilayer image corpus · **Eval:** Crello; LayerD decomposition protocol · **Output:** Variable-length RGBA layer stack; PSD/PPTX export · **Checked:** 2026-10-06.
- [OmniPSD: Layered PSD Generation with Diffusion Transformer](https://arxiv.org/abs/2512.09247) - Uses a unified FLUX-based diffusion-transformer framework for both text-to-PSD generation and flattened-image-to-PSD decomposition with editable transparent layers and an RGBA VAE. [Project](https://showlab.github.io/OmniPSD/) · [Code](https://github.com/showlab/OmniPSD) (`training + inference`) · Weights: `unknown`.<br>  **Method:** Unified layered PSD generation and decomposition · **Base:** FLUX.1-dev / FLUX.1-Kontext-dev with RGBA VAE · **Train:** OmniPSD Layered Poster dataset · **Eval:** Layered poster evaluation set · **Output:** Editable PSD; RGBA layers · **Checked:** 2026-10-06.
- [TAUE](https://arxiv.org/abs/2511.02580) - Generates coherent foreground, background, and composite layers without fine-tuning by transplanting and cultivating intermediate diffusion noise representations (CVPR Findings 2026). [Project](https://iyatomilab.github.io/TAUE/) · [Code](https://github.com/IyatomiLab/TAUE) (`unknown`) · Weights: `n/a`.<br>  **Method:** Training-free noise transplantation and cultivation for layer-wise generation · **Base:** SDXL · **Train:** None · **Eval:** Filtered MS-COCO · **Output:** Foreground; background; composite image · **Checked:** 2026-10-06.
- [SAWNA](https://www.siggraph.org/wp-content/uploads/2025/08/Posters.html) - Preserves user-specified negative-space regions during text-to-image generation so downstream text and interface elements can be composed cleanly (SIGGRAPH 2025 Poster).
- [PrismLayers](https://arxiv.org/abs/2505.22523) - Introduces PrismLayers and PrismLayersPro plus ART+ for high-quality multi-layer transparent image generation from text and layouts. [Project](https://prism-layers.github.io/) · [Code](https://github.com/redredsheep/PrismLayers) (`inference only`) · Weights: `released`.<br>  **Method:** ART+ multi-layer transparent image generation · **Base:** ART · **Train:** PrismLayersPro (20K high-quality subset of 200K PrismLayers) · **Output:** Multiple RGBA layers plus composite image · **Checked:** 2026-10-06.
- [PSDiffusion: Harmonized Multi-Layer Image Generation via Layout and Appearance Alignment](https://arxiv.org/abs/2505.11468) - Generates multiple transparent layers simultaneously with a unified diffusion framework and global-layer interaction for coherent layout, contacts, shadows, and reflections (WACV 2026). [Project](https://dingbang777.github.io/PSDiffusion_Website/) · [Code](https://github.com/dingbang777/PSDiffusion) (`announced`) · Weights: `announced`.<br>  **Method:** Simultaneous harmonized multi-layer diffusion generation · **Base:** Pretrained image diffusion model with global-layer interaction · **Train:** Inter-Layer Dataset (announced) · **Eval:** Layer-generation benchmark datasets · **Output:** RGB background + multiple RGBA foreground layers · **Checked:** 2026-10-06.
- [ART](https://arxiv.org/abs/2502.18364) - Generates variable numbers of transparent image layers from a global prompt and anonymous region layout using an Anonymous Region Transformer (CVPR 2025). Project: — · [Code](https://github.com/microsoft/art-msra) (`withdrawn`) · Weights: `withdrawn`.<br>  **Method:** Anonymous Region Transformer for variable multi-layer transparent generation · **Eval:** DESIGN-MULTI-LAYER-BENCH; PHOTO-MULTI-LAYER-BENCH · **Output:** Variable number of RGBA layers · **Checked:** 2026-10-06.
- [LayeringDiff: Layered Image Synthesis via Generation, then Disassembly with Generative Knowledge](https://arxiv.org/abs/2501.01197) - Synthesizes a composite image with an off-the-shelf generator and then disassembles it into foreground and background layers using pretrained generative priors and high-frequency alignment.
#### 2024

- [LayerFusion](https://arxiv.org/abs/2412.04460) - Generates harmonized foreground RGBA, background RGB, and composite images jointly using pretrained generative priors (CVPR Findings 2026). [Project](https://layerfusion.github.io/) · Code: `announced` · Weights: `n/a`.<br>  **Method:** Training-free harmonized multi-layer generation with generative priors · **Base:** Pretrained latent diffusion model · **Train:** None · **Output:** Foreground RGBA; background RGB; composite RGB · **Checked:** 2026-10-06.
- [Generative Image Layer Decomposition with Visual Effects](https://arxiv.org/abs/2411.17864) - Introduces LayerDecomp for decomposing images into clean backgrounds and transparent foreground layers while preserving visual effects such as shadows and reflections (CVPR 2025).
- [TKG-DM](https://arxiv.org/abs/2411.15580) - Generates foreground content over a controllable chroma-key background without training, enabling clean foreground-background separation (CVPR 2025). Project: — · [Code](https://github.com/ryugo417/TKG-DM) (`pipeline`) · Weights: `n/a`.<br>  **Method:** Training-free chroma-key content generation through initial-noise optimization · **Base:** Stable Diffusion XL 1.0 · **Train:** None · **Output:** RGB image with controlled chroma-key background · **Checked:** 2026-10-06.
- [Alfie](https://arxiv.org/abs/2408.14826) - Modifies the inference behavior of a pretrained Diffusion Transformer to generate easily isolated RGBA-style illustration assets without additional training (ECCV 2024 AI4VA Workshop).
- [LayerDiffuse](https://arxiv.org/abs/2402.17113) - Adds latent transparency to pretrained diffusion models for single- and multi-layer transparent image generation. [Project](https://github.com/lllyasviel/LayerDiffuse) · [Code](https://github.com/lllyasviel/LayerDiffuse_DiffusersCLI) (`inference only`) · [Weights](https://huggingface.co/LayerDiffusion/layerdiffusion-v1) (`released`).<br>  **Method:** Latent-transparency adaptation for transparent image generation · **Base:** Stable Diffusion v1.5 / SDXL · **Train:** 1M transparent image layer pairs · **Output:** Single or multiple transparent RGBA layers · **Checked:** 2026-10-06.
#### 2023

- [Text2Layer: Layered Image Generation using Latent Diffusion Model](https://arxiv.org/abs/2307.09781) - Jointly generates background, foreground, layer mask, and composed image in a learned layered latent space, establishing an early diffusion-based layered compositing formulation.
### Typography and Text Rendering

#### 2025

- [PosterMaker](https://arxiv.org/abs/2504.06632) - Generates product posters with explicit mechanisms for accurate text rendering and visual composition (CVPR 2025). [Project](https://poster-maker.github.io) · [Code](https://github.com/alimama-creative/PosterMaker) (`training + inference`) · [Weights](https://huggingface.co/alimama-creative/PosterMaker) (`released`).<br>  **Method:** Two-stage product-poster generation with scene synthesis and accurate text rendering · **Base:** Stable Diffusion 3 Medium · **Train:** Released e-commerce poster training data · **Eval:** Released stage-1 and stage-2 poster benchmarks · **Output:** Raster product poster with specified text regions · **Checked:** 2026-10-06.
#### 2024

- [GlyphDraw2](https://arxiv.org/abs/2407.02252) - Generates complex bilingual glyph posters with controllable fonts and precise text placement using LLM-guided SDXL conditioning (AAAI 2025). Project: — · [Code](https://github.com/OPPO-Mente-Lab/GlyphDraw2) (`training + inference`) · Weights: `unknown`.<br>  **Method:** LLM-guided triple-cross-attention diffusion for glyph poster generation · **Base:** SDXL; ControlNet; LLM planner · **Train:** GlyphDraw-3M · **Output:** Raster bilingual poster image · **Checked:** 2026-10-06.
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
- [CreatiParser: Generative Image Parsing of Raster Graphic Designs into Editable Layers](https://arxiv.org/abs/2604.19632) - Parses flattened graphic designs into editable text, background, and sticker layers using a VLM text-rendering protocol and multi-branch RGBA diffusion, with preference alignment via ParserReward.
- [ReLayout: Structure-Preserving Design Layout Editing](https://arxiv.org/abs/2602.01046) - Edits design layouts from natural-language intents while preserving unedited structure through relation graphs and self-supervised relation-aware design reconstruction.
#### 2025

- [PosterCopilot](https://arxiv.org/abs/2512.04082) - Combines layout reasoning with layer-controllable iterative editing for professional graphic-design workflows (ECCV 2026). [Project](https://postercopilot.github.io/) · [Code](https://github.com/JiazheWei/PosterCopilot) (`inference only`) · [Weights](https://huggingface.co/void-2024/PosterCopilot) (`released`).<br>  **Method:** LMM layout reasoning and layer-controllable editing · **Base:** Qwen2.5-VL-7B-Instruct · **Train:** PosterCopilot Dataset (160K posters, 2.6M layers) · **Output:** JSON layout; PNG; editable PSD · **Checked:** 2026-10-06.
- [LayerD](https://arxiv.org/abs/2509.25134) - Decomposes raster graphic designs into editable layers through iterative foreground extraction and refinement (ICCV 2025). [Project](https://cyberagentailab.github.io/LayerD/) · [Code](https://github.com/CyberAgentAILab/LayerD) (`training + inference`) · [Weights](https://huggingface.co/cyberagent/layerd-birefnet) (`released`).<br>  **Method:** Iterative raster-to-layer decomposition with matting and refinement · **Base:** BiRefNet · **Output:** RGBA layers; SVG; PSD · **Checked:** 2026-10-06.
- [Draw with Thought](https://arxiv.org/abs/2504.09479) - Reconstructs raster scientific diagrams into editable mxGraph XML through coarse-to-fine reasoning and structure-aware code generation.
#### 2024

- [Neural Contrast](https://arxiv.org/abs/2410.07211) - Uses diffusion-based generative editing to create low-saliency, high-contrast regions beneath design assets for improved graphic-design readability (PRICAI 2024).
- [Revision Matters](https://arxiv.org/abs/2406.18559) - Fine-tunes a Gemini multimodal backbone on human revision traces to iteratively refine generated layouts toward expert design edits.
#### 2021

- [De-Rendering Stylized Texts](https://arxiv.org/abs/2110.01890) - Vectorizes rasterized display text into editable content, geometry, font, styling, effects, and hidden-background parameters through differentiable rendering (ICCV 2021).
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
- [PostDoc](https://arxiv.org/abs/2405.20213) - Generates posters from long multimodal documents using learned submodular content selection, LLM paraphrasing, and content-conditioned template generation.
## Method and Architecture Index

The paper categories above describe **what a system produces**. This index describes **how it is implemented** and is deliberately multi-label: hybrid systems may appear under several method families. The vocabulary is a normalized taxonomy for the research represented in this catalog and can evolve as new model families emerge. Paper names correspond to the canonical entries above; links are intentionally not repeated so the Awesome list keeps one canonical external link per resource.

### Classical / Optimization

<table>
<thead>
<tr><th>Paper</th><th>Primary task/output</th><th>Architecture note</th></tr>
</thead>
<tbody>
<tr><td>LayoutRectifier</td><td>Layout Generation</td><td>Two-stage discrete and continuous layout optimization</td></tr>
<tr><td>PostDoc</td><td>Scientific Poster and Slide Generation</td><td>Deep submodular multimodal content selection</td></tr>
<tr><td>Constrained Graphic Layout Generation via Latent Optimization</td><td>Layout Generation</td><td>Constraint satisfaction through latent optimization</td></tr>
<tr><td>DesignScape</td><td>Layout Generation</td><td>Interactive layout suggestion and refinement system</td></tr>
<tr><td>Learning Layouts for Single-Page Graphic Designs</td><td>Layout Generation</td><td>Pre-deep-learning structured layout model</td></tr>
</tbody>
</table>

### VAE

<table>
<thead>
<tr><th>Paper</th><th>Primary task/output</th><th>Architecture note</th></tr>
</thead>
<tbody>
<tr><td>Human-aware Design Generation</td><td>Graphic Design Generation</td><td>VQ-VAE human-pose representation</td></tr>
<tr><td>LaDe: Unified Multi-Layered Graphic Media Generation and Decomposition</td><td>Composable and Layered Asset Generation</td><td>RGBA VAE for transparency-aware layer decoding</td></tr>
<tr><td>OmniPSD: Layered PSD Generation with Diffusion Transformer</td><td>Composable and Layered Asset Generation</td><td>Transparency-preserving RGBA VAE</td></tr>
<tr><td>CLASS</td><td>Layout Generation</td><td>Variational latent layout representation</td></tr>
<tr><td>Iris: a multi-constraint graphic layout generation system</td><td>Content-Aware Layout Generation</td><td>Multi-constraint LayoutVQ-VAE conditioned on background and design-element constraints</td></tr>
<tr><td>Text2Layer: Layered Image Generation using Latent Diffusion Model</td><td>Composable and Layered Asset Generation</td><td>Autoencoder learns a joint layered latent representation</td></tr>
<tr><td>Layout Generation for Various Scenarios in Mobile Shopping Apps</td><td>Layout Generation</td><td>LayoutVQ-VAE with discrete latent layout representation and multi-constraint conditioning</td></tr>
<tr><td>ICVT</td><td>Content-Aware Layout Generation</td><td>Geometry-aligned variational Transformer</td></tr>
<tr><td>Text2Poster</td><td>Typography and Text Rendering</td><td>Variational visual-textual poster composition model</td></tr>
<tr><td>Coarse-to-Fine</td><td>Layout Generation</td><td>Hierarchical variational layout generation</td></tr>
<tr><td>CanvasVAE</td><td>Layout Generation</td><td>Variational autoencoder</td></tr>
<tr><td>VTN</td><td>Layout Generation</td><td>—</td></tr>
<tr><td>Neural Design Network</td><td>Layout Generation</td><td>Variational structured design model</td></tr>
<tr><td>READ: Recursive Autoencoders for Document Layout Generation</td><td>Layout Generation</td><td>Recursive variational autoencoder (RvNN-VAE) over hierarchical document layouts</td></tr>
<tr><td>LayoutVAE</td><td>Layout Generation</td><td>Variational autoencoder</td></tr>
</tbody>
</table>

### GAN

<table>
<thead>
<tr><th>Paper</th><th>Primary task/output</th><th>Architecture note</th></tr>
</thead>
<tbody>
<tr><td>PosterLayout</td><td>Content-Aware Layout Generation</td><td>Content-aware poster layout generation with DS-GAN</td></tr>
<tr><td>PDA-GAN</td><td>Content-Aware Layout Generation</td><td>Image-aware GAN with pixel-level discriminator and domain adaptation</td></tr>
<tr><td>Machine Learning Model to Evaluate the Appropriateness of Layout for Automatic Generation of Graphic Design Works</td><td>Layout Generation</td><td>Adversarial layout generator and discriminator; discriminator also scores layout appropriateness</td></tr>
<tr><td>CreaGAN</td><td>Graphic Design Generation</td><td>Aesthetics-aware placement plus creative inpainting framework</td></tr>
<tr><td>CGL-GAN</td><td>Content-Aware Layout Generation</td><td>Content-aware generative adversarial model</td></tr>
<tr><td>Constrained Graphic Layout Generation via Latent Optimization</td><td>Layout Generation</td><td>GAN with differentiable rendering</td></tr>
<tr><td>AC-LayoutGAN</td><td>Layout Generation</td><td>—</td></tr>
<tr><td>ContentGAN</td><td>Content-Aware Layout Generation</td><td>Content-aware generative adversarial model</td></tr>
<tr><td>LayoutGAN</td><td>Layout Generation</td><td>Generative adversarial layout model</td></tr>
</tbody>
</table>

### Autoregressive / Transformer

<table>
<thead>
<tr><th>Paper</th><th>Primary task/output</th><th>Architecture note</th></tr>
</thead>
<tbody>
<tr><td>Human-aware Design Generation</td><td>Graphic Design Generation</td><td>Causal and bidirectional Transformer modules</td></tr>
<tr><td>i-Design</td><td>Layout Generation</td><td>Progressive autoregressive element placement</td></tr>
<tr><td>Mise-en-Scène</td><td>Graphic Design Generation</td><td>—</td></tr>
<tr><td>Design Your Ad</td><td>Graphic Design Generation</td><td>Unified autoregressive personalized advertising image-text generation</td></tr>
<tr><td>SIMPLEPOSTER</td><td>Graphic Design Generation</td><td>Diffusion Transformer backbone</td></tr>
<tr><td>LaDe: Unified Multi-Layered Graphic Media Generation and Decomposition</td><td>Composable and Layered Asset Generation</td><td>Latent Diffusion Transformer with 4D RoPE</td></tr>
<tr><td>PosterOmni</td><td>Graphic Design Generation</td><td>Unified multi-task image-to-poster generation and editing via task distillation and reward feedback</td></tr>
<tr><td>Controllable Layered Image Generation for Real-World Editing</td><td>Composable and Layered Asset Generation</td><td>Diffusion Transformer architecture with heterogeneous layer-role embeddings</td></tr>
<tr><td>OmniPSD: Layered PSD Generation with Diffusion Transformer</td><td>Composable and Layered Asset Generation</td><td>Diffusion Transformer backbone with spatial in-context layer modeling</td></tr>
<tr><td>UniLayDiff</td><td>Content-Aware Layout Generation</td><td>Diffusion Transformer backbone</td></tr>
<tr><td>Sketch-to-Layout</td><td>Layout Generation</td><td>Multimodal Transformer</td></tr>
<tr><td>PrismLayers</td><td>Composable and Layered Asset Generation</td><td>ART+ multi-layer Transformer component</td></tr>
<tr><td>Scan-and-Print</td><td>Content-Aware Layout Generation</td><td>Autoregressive content-aware layout generation</td></tr>
<tr><td>StructLayoutFormer</td><td>Layout Generation</td><td>Transformer with structure serialization and disentanglement</td></tr>
<tr><td>CreatiDesign</td><td>Graphic Design Generation</td><td>Multi-conditional diffusion transformer</td></tr>
<tr><td>Scientific Poster Generation A New Dataset and Approach</td><td>Scientific Poster and Slide Generation</td><td>Template-free sequence-to-sequence poster-layout generator</td></tr>
<tr><td>CLASS</td><td>Layout Generation</td><td>—</td></tr>
<tr><td>ART</td><td>Composable and Layered Asset Generation</td><td>Anonymous Region Transformer for variable multi-layer transparent generation</td></tr>
<tr><td>Design Element Aware Poster Layout Generation</td><td>Content-Aware Layout Generation</td><td>Design-element-aware structured layout modeling</td></tr>
<tr><td>Alfie</td><td>Composable and Layered Asset Generation</td><td>Diffusion Transformer backbone</td></tr>
<tr><td>CGB-DM</td><td>Content-Aware Layout Generation</td><td>—</td></tr>
<tr><td>Desigen</td><td>Graphic Design Generation</td><td>Autoregressive joint design generation</td></tr>
<tr><td>RALF</td><td>Content-Aware Layout Generation</td><td>Retrieval-augmented autoregressive layout transformer</td></tr>
<tr><td>Dolfin</td><td>Layout Generation</td><td>—</td></tr>
<tr><td>Parse-Then-Place</td><td>Layout Generation</td><td>Parsed constraints followed by sequential placement</td></tr>
<tr><td>LayoutDM: Transformer-Based Diffusion Model for Layout Generation</td><td>Layout Generation</td><td>Pure Transformer denoiser</td></tr>
<tr><td>LayoutDM</td><td>Layout Generation</td><td>Discrete diffusion model for controllable layout generation</td></tr>
<tr><td>LayoutAction</td><td>Layout Generation</td><td>—</td></tr>
<tr><td>LayoutDETR</td><td>Content-Aware Layout Generation</td><td>Detection-transformer-style multimodal layout generation</td></tr>
<tr><td>ICVT</td><td>Content-Aware Layout Generation</td><td>Transformer backbone</td></tr>
<tr><td>LayoutFormer++</td><td>Layout Generation</td><td>Conditional sequence-to-sequence layout generation</td></tr>
<tr><td>Layout-BLT</td><td>Layout Generation</td><td>—</td></tr>
<tr><td>LayoutMCL</td><td>Layout Generation</td><td>—</td></tr>
<tr><td>Constrained Graphic Layout Generation via Latent Optimization</td><td>Layout Generation</td><td>Transformer-based generative layout backbone</td></tr>
<tr><td>VTN</td><td>Layout Generation</td><td>Self-attention / Transformer backbone</td></tr>
<tr><td>DeepLayout</td><td>Layout Generation</td><td>—</td></tr>
</tbody>
</table>

### Diffusion

<table>
<thead>
<tr><th>Paper</th><th>Primary task/output</th><th>Architecture note</th></tr>
</thead>
<tbody>
<tr><td>InterIL</td><td>Graphic Design Generation</td><td>Coupled image and layout diffusion backbones</td></tr>
<tr><td>Mise-en-Scène</td><td>Graphic Design Generation</td><td>—</td></tr>
<tr><td>SciForma</td><td>Scientific Figure and Graphical Abstract Generation</td><td>Structure-faithful scientific diagram diffusion with M-DPO</td></tr>
<tr><td>Personalization as Inverse Planning</td><td>Scientific Poster and Slide Generation</td><td>—</td></tr>
<tr><td>MRT</td><td>Composable and Layered Asset Generation</td><td>Masked-region diffusion for unified layered generation and editing</td></tr>
<tr><td>SIMPLEPOSTER</td><td>Graphic Design Generation</td><td>FLUX-Fill diffusion-transformer poster generation</td></tr>
<tr><td>CreatiParser: Generative Image Parsing of Raster Graphic Designs into Editable Layers</td><td>Graphic Design Editing and Reconstruction</td><td>Multi-branch RGBA diffusion for background and sticker layers</td></tr>
<tr><td>iPoster</td><td>Content-Aware Layout Generation</td><td>Graph-enhanced content-aware diffusion</td></tr>
<tr><td>LaDe: Unified Multi-Layered Graphic Media Generation and Decomposition</td><td>Composable and Layered Asset Generation</td><td>Latent diffusion model for joint full-design and RGBA-layer generation</td></tr>
<tr><td>InnoAds-Composer</td><td>Graphic Design Generation</td><td>Single-stage subject/glyph/style-conditioned diffusion</td></tr>
<tr><td>PosterVerse</td><td>Graphic Design Generation</td><td>Diffusion background generation</td></tr>
<tr><td>Qwen-Image-Layered</td><td>Composable and Layered Asset Generation</td><td>Variable-layer image decomposition diffusion model</td></tr>
<tr><td>OmniPSD: Layered PSD Generation with Diffusion Transformer</td><td>Composable and Layered Asset Generation</td><td>FLUX-based unified text-to-PSD and image-to-PSD diffusion framework</td></tr>
<tr><td>UniLayDiff</td><td>Content-Aware Layout Generation</td><td>Multimodal diffusion transformer</td></tr>
<tr><td>TAUE</td><td>Composable and Layered Asset Generation</td><td>Training-free noise transplantation and cultivation for layer-wise generation</td></tr>
<tr><td>RefAdGen</td><td>Graphic Design Generation</td><td>Product-preserving advertising diffusion with spatial control and attention fusion</td></tr>
<tr><td>SAWNA</td><td>Composable and Layered Asset Generation</td><td>Training-free diffusion with negative-space-preserving noise control</td></tr>
<tr><td>DreamPoster</td><td>Graphic Design Generation</td><td>Seedream-based image-conditioned poster generation</td></tr>
<tr><td>PosterCraft</td><td>Graphic Design Generation</td><td>Unified diffusion poster generation with staged text and aesthetic optimization</td></tr>
<tr><td>PrismLayers</td><td>Composable and Layered Asset Generation</td><td>LayerFLUX and MultiLayerFLUX diffusion models</td></tr>
<tr><td>CreatiDesign</td><td>Graphic Design Generation</td><td>Multi-conditional diffusion transformer</td></tr>
<tr><td>PSDiffusion: Harmonized Multi-Layer Image Generation via Layout and Appearance Alignment</td><td>Composable and Layered Asset Generation</td><td>Unified simultaneous multi-layer diffusion with global-layer interaction</td></tr>
<tr><td>PosterMaker</td><td>Typography and Text Rendering</td><td>Two-stage product-poster generation with scene synthesis and accurate text rendering</td></tr>
<tr><td>BizGen</td><td>Graphic Design Generation</td><td>Layout-guided latent image generation with region-wise refinement</td></tr>
<tr><td>POSTA</td><td>Graphic Design Generation</td><td>—</td></tr>
<tr><td>DesignDiffusion: High-Quality Text-to-Design Image Generation with Diffusion Models</td><td>Graphic Design Generation</td><td>One-stage character-aware diffusion model with self-play DPO</td></tr>
<tr><td>PAID</td><td>Graphic Design Generation</td><td>SDXL-based layout-controlled background generation</td></tr>
<tr><td>LayeringDiff: Layered Image Synthesis via Generation, then Disassembly with Generative Knowledge</td><td>Composable and Layered Asset Generation</td><td>Pretrained generative priors for synthesis and layer decomposition</td></tr>
<tr><td>LayerFusion</td><td>Composable and Layered Asset Generation</td><td>Training-free harmonized multi-layer generation with generative priors</td></tr>
<tr><td>Generative Image Layer Decomposition with Visual Effects</td><td>Composable and Layered Asset Generation</td><td>Generative layer decomposition into clean background and transparent foreground</td></tr>
<tr><td>TKG-DM</td><td>Composable and Layered Asset Generation</td><td>Training-free chroma-key content generation through initial-noise optimization</td></tr>
<tr><td>Neural Contrast</td><td>Graphic Design Editing and Reconstruction</td><td>Generative diffusion editing beneath design assets</td></tr>
<tr><td>Layout-Corrector</td><td>Layout Generation</td><td>—</td></tr>
<tr><td>Alfie</td><td>Composable and Layered Asset Generation</td><td>Inference-time RGBA generation with a pretrained Diffusion Transformer</td></tr>
<tr><td>Towards Reliable Advertising Image Generation Using Human Feedback</td><td>Graphic Design Generation</td><td>Reliable-feedback-guided recurrent advertising generation and diffusion fine-tuning</td></tr>
<tr><td>CGB-DM</td><td>Content-Aware Layout Generation</td><td>—</td></tr>
<tr><td>GlyphDraw2</td><td>Typography and Text Rendering</td><td>LLM-guided triple-cross-attention diffusion for glyph poster generation</td></tr>
<tr><td>Visual Layout Composer</td><td>Content-Aware Layout Generation</td><td>—</td></tr>
<tr><td>CoLay</td><td>Layout Generation</td><td>Multi-conditional latent diffusion for controllable layouts</td></tr>
<tr><td>LayerDiffuse</td><td>Composable and Layered Asset Generation</td><td>Latent-transparency adaptation for transparent image generation</td></tr>
<tr><td>LACE</td><td>Layout Generation</td><td>—</td></tr>
<tr><td>CG4CTR</td><td>Graphic Design Generation</td><td>Stable-Diffusion-based advertising creative generation</td></tr>
<tr><td>TextDiffuser-2</td><td>Typography and Text Rendering</td><td>Language-model-assisted diffusion for flexible text rendering</td></tr>
<tr><td>Two-stage Content-Aware Layout Generation for Poster Designs</td><td>Content-Aware Layout Generation</td><td>—</td></tr>
<tr><td>Dolfin</td><td>Layout Generation</td><td>—</td></tr>
<tr><td>Text2Layer: Layered Image Generation using Latent Diffusion Model</td><td>Composable and Layered Asset Generation</td><td>Latent diffusion over layered representations</td></tr>
<tr><td>RADM</td><td>Content-Aware Layout Generation</td><td>Content-aware advertising layout diffusion</td></tr>
<tr><td>TextDiffuser</td><td>Typography and Text Rendering</td><td>Two-stage diffusion framework for text rendering</td></tr>
<tr><td>LayoutDM: Transformer-Based Diffusion Model for Layout Generation</td><td>Layout Generation</td><td>Conditional DDPM for layouts</td></tr>
<tr><td>FlexDM</td><td>Layout Generation</td><td>—</td></tr>
<tr><td>LayoutDiffusion</td><td>Layout Generation</td><td>—</td></tr>
<tr><td>LayoutDM</td><td>Layout Generation</td><td>Discrete diffusion model for controllable layout generation</td></tr>
<tr><td>LDGM</td><td>Layout Generation</td><td>—</td></tr>
<tr><td>DLT</td><td>Layout Generation</td><td>—</td></tr>
<tr><td>PLay</td><td>Layout Generation</td><td>—</td></tr>
</tbody>
</table>

### Flow Matching

<table>
<thead>
<tr><th>Paper</th><th>Primary task/output</th><th>Architecture note</th></tr>
</thead>
<tbody>
<tr><td>PosterText</td><td>Graphic Design Editing and Reconstruction</td><td>Text-patch generation/editing trained with a flow-matching objective</td></tr>
<tr><td>Controllable Layered Image Generation for Real-World Editing</td><td>Composable and Layered Asset Generation</td><td>Training objective follows flow matching for layer-conditional generation</td></tr>
<tr><td>Learning Priority-Aware Controllable Poster Layout Generation</td><td>Content-Aware Layout Generation</td><td>—</td></tr>
<tr><td>LayoutFlow</td><td>Layout Generation</td><td>Continuous flow-matching layout model</td></tr>
</tbody>
</table>

### LLM / VLM

<table>
<thead>
<tr><th>Paper</th><th>Primary task/output</th><th>Architecture note</th></tr>
</thead>
<tbody>
<tr><td>i-Design</td><td>Layout Generation</td><td>InternVL-based multimodal aesthetic policy</td></tr>
<tr><td>Figures as Programs</td><td>Scientific Figure and Graphical Abstract Generation</td><td>Program-generating multimodal agents</td></tr>
<tr><td>Any2Poster</td><td>Scientific Poster and Slide Generation</td><td>LLM analyzers/planner with VLM feedback</td></tr>
<tr><td>CreatiParser: Generative Image Parsing of Raster Graphic Designs into Editable Layers</td><td>Graphic Design Editing and Reconstruction</td><td>Vision-language model parses text into an editable rendering protocol</td></tr>
<tr><td>Design First Code Later</td><td>Scientific Poster and Slide Generation</td><td>Design-first template-free slide-generation workflow</td></tr>
<tr><td>PSDesigner</td><td>Graphic Design Generation</td><td>Multimodal planner</td></tr>
<tr><td>Seeing is Improving: Visual Feedback for Iterative Text Layout Refinement</td><td>Content-Aware Layout Generation</td><td>Qwen2.5-VL-based multimodal layout model with rendered visual feedback</td></tr>
<tr><td>LaDe: Unified Multi-Layered Graphic Media Generation and Decomposition</td><td>Composable and Layered Asset Generation</td><td>LLM prompt expander and VLM-based layer descriptions/evaluation</td></tr>
<tr><td>AutoFigure-Edit</td><td>Scientific Figure and Graphical Abstract Generation</td><td>LLM/VLM-guided scientific-figure parsing and refinement</td></tr>
<tr><td>DesignAsCode</td><td>Graphic Design Generation</td><td>Code-native agentic graphic-design generation</td></tr>
<tr><td>AutoFigure</td><td>Scientific Figure and Graphical Abstract Generation</td><td>Agentic scientific illustration generation and iterative refinement</td></tr>
<tr><td>ReLayout: Structure-Preserving Design Layout Editing</td><td>Graphic Design Editing and Reconstruction</td><td>MLLM-based relation-aware design reconstruction</td></tr>
<tr><td>PaperBanana</td><td>Scientific Figure and Graphical Abstract Generation</td><td>Reference-driven multi-agent academic illustration generation</td></tr>
<tr><td>PosterVerse</td><td>Graphic Design Generation</td><td>LLM blueprint planning and multimodal HTML generation</td></tr>
<tr><td>PosterCopilot</td><td>Graphic Design Editing and Reconstruction</td><td>LMM layout reasoning and layer-controllable editing</td></tr>
<tr><td>Learning Priority-Aware Controllable Poster Layout Generation</td><td>Content-Aware Layout Generation</td><td>—</td></tr>
<tr><td>SEGA</td><td>Content-Aware Layout Generation</td><td>LLaVA-based coarse and fine layout reasoning</td></tr>
<tr><td>LLMs as Layout Designers (LaySPA)</td><td>Content-Aware Layout Generation</td><td>LLM spatial reasoning with reinforcement learning</td></tr>
<tr><td>PosterForest</td><td>Scientific Poster and Slide Generation</td><td>Training-free multi-agent scientific-poster generation</td></tr>
<tr><td>PosterGen</td><td>Scientific Poster and Slide Generation</td><td>LLM/VLM-driven scientific poster generation</td></tr>
<tr><td>Uni-Layout</td><td>Content-Aware Layout Generation</td><td>Natural-language-conditioned unified layout generation and evaluation</td></tr>
<tr><td>ReLayout: Relation Reasoning for Content-Aware Layout Generation</td><td>Content-Aware Layout Generation</td><td>Relation-CoT with a multimodal large language model</td></tr>
<tr><td>Rethinking Layered Graphic Design Generation with a Top-Down Approach</td><td>Graphic Design Generation</td><td>VLM used across reference creation, design planning, and layer generation</td></tr>
<tr><td>CAL-RAG</td><td>Content-Aware Layout Generation</td><td>LLM/VLM retrieval-and-grading loop</td></tr>
<tr><td>CreatiPoster</td><td>Content-Aware Layout Generation</td><td>RGBA large multimodal model for layered poster planning</td></tr>
<tr><td>PosterCraft</td><td>Graphic Design Generation</td><td>Unified diffusion poster generation with staged text and aesthetic optimization</td></tr>
<tr><td>PosterO</td><td>Content-Aware Layout Generation</td><td>—</td></tr>
<tr><td>Draw with Thought</td><td>Graphic Design Editing and Reconstruction</td><td>MLLM chain-of-thought for diagram reconstruction</td></tr>
<tr><td>BannerAgency</td><td>Graphic Design Generation</td><td>Multimodal LLM agents</td></tr>
<tr><td>AesthetiQ</td><td>Content-Aware Layout Generation</td><td>Multimodal LLM preference alignment</td></tr>
<tr><td>LGGPT</td><td>Layout Generation</td><td>1.5B instruction-tuned LLM for unified layout generation</td></tr>
<tr><td>PAID</td><td>Graphic Design Generation</td><td>VLM prompt and layout expert models</td></tr>
<tr><td>LaDeCo</td><td>Graphic Design Generation</td><td>Large multimodal model for layer planning and attributes</td></tr>
<tr><td>VASCAR</td><td>Content-Aware Layout Generation</td><td>LVLM visual-aware self-correction</td></tr>
<tr><td>LayoutKAG: Enhancing Layout Generation in Large Language Models Through Knowledge-Augmented Generation</td><td>Layout Generation</td><td>Knowledge-augmented large-language-model layout generation</td></tr>
<tr><td>TextLap</td><td>Layout Generation</td><td>Customized language model for text-to-layout planning</td></tr>
<tr><td>SciPostLayout</td><td>Scientific Poster and Slide Generation</td><td>Scientific-poster layout analysis and generation baselines</td></tr>
<tr><td>GlyphDraw2</td><td>Typography and Text Rendering</td><td>LLM-guided triple-cross-attention diffusion for glyph poster generation</td></tr>
<tr><td>OpenCOLE</td><td>Graphic Design Generation</td><td>Multimodal planning for graphic-design generation</td></tr>
<tr><td>PosterLLaVA</td><td>Content-Aware Layout Generation</td><td>Multimodal instruction-tuned language model</td></tr>
<tr><td>PostDoc</td><td>Scientific Poster and Slide Generation</td><td>LLM paraphrasing for poster content</td></tr>
<tr><td>Revision Matters</td><td>Graphic Design Editing and Reconstruction</td><td>Gemini multimodal backbone fine-tuned on designer revisions</td></tr>
<tr><td>Automatic Layout Planning for Visually-Rich Documents with Instruction-Following Models</td><td>Content-Aware Layout Generation</td><td>mPLUG-Owl-based multimodal instruction-following layout planner (DocLap)</td></tr>
<tr><td>Graphist</td><td>Content-Aware Layout Generation</td><td>Multimodal structural context model</td></tr>
<tr><td>PosterLLaMA</td><td>Content-Aware Layout Generation</td><td>Multimodal language model</td></tr>
<tr><td>Chaining Text-to-Image and Large Language Model for Personalized E-commerce Banners</td><td>Graphic Design Generation</td><td>—</td></tr>
<tr><td>COLE</td><td>Graphic Design Generation</td><td>Language-model-guided hierarchical design planning</td></tr>
<tr><td>TextDiffuser-2</td><td>Typography and Text Rendering</td><td>Language-model-assisted diffusion for flexible text rendering</td></tr>
<tr><td>LayoutPrompter</td><td>Layout Generation</td><td>In-context LLM prompting</td></tr>
<tr><td>LayoutNUWA</td><td>Layout Generation</td><td>Code-oriented language model</td></tr>
<tr><td>LayoutGPT</td><td>Layout Generation</td><td>In-context language-model layout generation</td></tr>
</tbody>
</table>

### Agentic / Multi-stage System

<table>
<thead>
<tr><th>Paper</th><th>Primary task/output</th><th>Architecture note</th></tr>
</thead>
<tbody>
<tr><td>Designer-RSI</td><td>Graphic Design Generation</td><td>—</td></tr>
<tr><td>PosterVisor</td><td>Scientific Poster and Slide Generation</td><td>Orchestrated semantic-geometric contracts with validation and repair</td></tr>
<tr><td>Figures as Programs</td><td>Scientific Figure and Graphical Abstract Generation</td><td>Recursive SVG generation with render-critic refinement</td></tr>
<tr><td>PaperBanana-Interact</td><td>Scientific Figure and Graphical Abstract Generation</td><td>—</td></tr>
<tr><td>GenGA</td><td>Scientific Figure and Graphical Abstract Generation</td><td>Source-grounded hierarchical vector generation framework</td></tr>
<tr><td>PosterMELD</td><td>Scientific Poster and Slide Generation</td><td>—</td></tr>
<tr><td>ReDesign</td><td>Graphic Design Editing and Reconstruction</td><td>Agentic raster-to-editable design decomposition</td></tr>
<tr><td>Personalization as Inverse Planning</td><td>Scientific Poster and Slide Generation</td><td>—</td></tr>
<tr><td>Any2Poster</td><td>Scientific Poster and Slide Generation</td><td>Any-source poster generation agent</td></tr>
<tr><td>CreatiParser: Generative Image Parsing of Raster Graphic Designs into Editable Layers</td><td>Graphic Design Editing and Reconstruction</td><td>Hybrid text parsing, layer generation, and preference-alignment pipeline</td></tr>
<tr><td>Brief2Design</td><td>Graphic Design Generation</td><td>Requirement extraction, element exploration, and compositional recombination</td></tr>
<tr><td>PSDesigner</td><td>Graphic Design Generation</td><td>Tool-using graphic-design agent</td></tr>
<tr><td>Seeing is Improving: Visual Feedback for Iterative Text Layout Refinement</td><td>Content-Aware Layout Generation</td><td>Iterative render-observe-refine loop with reward-model-guided reinforcement learning</td></tr>
<tr><td>Multi-Object Advertisement Creative Generation</td><td>Graphic Design Generation</td><td>Product pairing, layout, and background-generation modules</td></tr>
<tr><td>AutoFigure-Edit</td><td>Scientific Figure and Graphical Abstract Generation</td><td>Multi-stage SVG reconstruction and refinement</td></tr>
<tr><td>DesignAsCode</td><td>Graphic Design Generation</td><td>Code-native agentic graphic-design generation</td></tr>
<tr><td>AutoFigure</td><td>Scientific Figure and Graphical Abstract Generation</td><td>Agentic scientific illustration generation and iterative refinement</td></tr>
<tr><td>PaperBanana</td><td>Scientific Figure and Graphical Abstract Generation</td><td>Reference-driven multi-agent academic illustration generation</td></tr>
<tr><td>PosterVerse</td><td>Graphic Design Generation</td><td>Blueprint/background/typography pipeline</td></tr>
<tr><td>AutoPP</td><td>Graphic Design Generation</td><td>Unified poster generation plus CTR-oriented preference optimization</td></tr>
<tr><td>SlideGen</td><td>Scientific Poster and Slide Generation</td><td>Collaborative multimodal slide-generation agents</td></tr>
<tr><td>SciPostGen</td><td>Scientific Poster and Slide Generation</td><td>Retrieval-augmented scientific-poster layout generation pipeline</td></tr>
<tr><td>SEGA</td><td>Content-Aware Layout Generation</td><td>Coarse-to-fine stepwise evolution pipeline</td></tr>
<tr><td>LayerD</td><td>Graphic Design Editing and Reconstruction</td><td>Iterative matting and inpainting decomposition pipeline</td></tr>
<tr><td>PosterForest</td><td>Scientific Poster and Slide Generation</td><td>Training-free multi-agent scientific-poster generation</td></tr>
<tr><td>PosterGen</td><td>Scientific Poster and Slide Generation</td><td>Parser/curator/layout/stylist/renderer agents</td></tr>
<tr><td>Uni-Layout</td><td>Content-Aware Layout Generation</td><td>Generator/evaluator preference-alignment framework</td></tr>
<tr><td>Rethinking Layered Graphic Design Generation with a Top-Down Approach</td><td>Graphic Design Generation</td><td>Accordion top-down three-stage layered-design pipeline with vision experts</td></tr>
<tr><td>CAL-RAG</td><td>Content-Aware Layout Generation</td><td>Retrieval-augmented collaborative agents</td></tr>
<tr><td>CreatiPoster</td><td>Content-Aware Layout Generation</td><td>Layer planning plus conditional background generation</td></tr>
<tr><td>Paper2Poster</td><td>Scientific Poster and Slide Generation</td><td>—</td></tr>
<tr><td>P2P</td><td>Scientific Poster and Slide Generation</td><td>—</td></tr>
<tr><td>Draw with Thought</td><td>Graphic Design Editing and Reconstruction</td><td>Coarse-to-fine code reconstruction pipeline</td></tr>
<tr><td>BannerAgency</td><td>Graphic Design Generation</td><td>Collaborating multimodal agents</td></tr>
<tr><td>PAID</td><td>Graphic Design Generation</td><td>Four-stage prompt/layout/background/rendering framework</td></tr>
<tr><td>LayeringDiff: Layered Image Synthesis via Generation, then Disassembly with Generative Knowledge</td><td>Composable and Layered Asset Generation</td><td>Generate-then-disassemble two-stage pipeline</td></tr>
<tr><td>Iris: a multi-constraint graphic layout generation system</td><td>Content-Aware Layout Generation</td><td>Interactive specification, layout generation, custom editing, and rendering system</td></tr>
<tr><td>OpenCOLE</td><td>Graphic Design Generation</td><td>Open layered design-generation pipeline</td></tr>
<tr><td>PostDoc</td><td>Scientific Poster and Slide Generation</td><td>Content selection, template generation, and harmonization pipeline</td></tr>
<tr><td>CG4CTR</td><td>Graphic Design Generation</td><td>Generation plus CTR-ranking pipeline</td></tr>
<tr><td>Planning and Rendering</td><td>Graphic Design Generation</td><td>Separated semantic planning and visual rendering</td></tr>
<tr><td>COLE</td><td>Graphic Design Generation</td><td>Hierarchical planning and layered rendering framework</td></tr>
<tr><td>TextPainter</td><td>Typography and Text Rendering</td><td>Text understanding and image-space stylized rendering framework</td></tr>
<tr><td>AutoPoster</td><td>Graphic Design Generation</td><td>Content analysis plus layout and rendering pipeline</td></tr>
<tr><td>CreaGAN</td><td>Graphic Design Generation</td><td>Two-stage placement and inpainting framework</td></tr>
<tr><td>De-Rendering Stylized Texts</td><td>Graphic Design Editing and Reconstruction</td><td>Neural vectorization plus differentiable rendering and reconstruction</td></tr>
<tr><td>SmartText</td><td>Content-Aware Layout Generation</td><td>Saliency and aesthetic-compatibility text-placement system</td></tr>
<tr><td>Vinci</td><td>Graphic Design Generation</td><td>End-to-end intelligent poster design system</td></tr>
</tbody>
</table>

### Graph Neural Network

<table>
<thead>
<tr><th>Paper</th><th>Primary task/output</th><th>Architecture note</th></tr>
</thead>
<tbody>
<tr><td>iPoster</td><td>Content-Aware Layout Generation</td><td>Graph-conditioned cross-content reasoning</td></tr>
</tbody>
</table>

### Encoder-only Neural Model

<table>
<thead>
<tr><th>Paper</th><th>Primary task/output</th><th>Architecture note</th></tr>
</thead>
<tbody>
<tr><td>Spot the Error</td><td>Layout Generation</td><td>Non-autoregressive token refinement with wireframe error locator</td></tr>
<tr><td>Learn and Sample Together</td><td>Layout Generation</td><td>BERT-like graph modeling in a collaborative two-stage generator</td></tr>
</tbody>
</table>

## Datasets and Benchmarks

Datasets provide reusable examples, assets, annotations, or corpora for training and evaluation. Benchmarks add a fixed task, split, protocol, or test set. Because many resources serve both roles, they are listed once in this combined section.

### 2026

- [MTPaperBananaBench](https://shirley-wu.github.io/PaperBanana-Interact/index.html) - Benchmarks multi-turn scientific diagram refinement with 292 images and 3,518 user requirements covering content, layout, and visual representation.
- [SciFigQual-Bench](https://arxiv.org/abs/2607.27084) - Benchmarks scientific-figure quality with 6,308 expert-scored images grounded in captions, citations, and full-manuscript context.
- [SciFormaBench-2K](https://huggingface.co/datasets/microsoft/SciFormaBench) - Provides 2,000 human-verified scientific diagram cases evaluated along component, arrow, and text structural-fidelity axes.
- [SciFormaData-700K](https://huggingface.co/datasets/microsoft/SciFormaData-700K) - Provides structure-aware scientific methodology-diagram training records with generation prompts, multi-resolution targets, and edit triplets.
- [TASTE](https://arxiv.org/abs/2605.20731) - Provides designer-panel preferences for AI-generated graphic designs across typography, hierarchy, color, layout, and brief fidelity.
- [PAd1M](https://github.com/JD-GenX/Uni-AdGen#3-pad1m-dataset) - Provides personalized advertising image-text examples and user-history conditioning for general and personalized advertisement generation; the test set and a training preview are public.
- [GENFIG1](https://arxiv.org/abs/2604.04172) - Benchmarks generating Figure 1-style visual summaries from scholarly paper context, targeting scientific abstraction, faithfulness, and visual communication.
- [Graphic-Design-Bench](https://arxiv.org/abs/2604.04192) - Benchmarks AI systems across professional graphic-design tasks including layout, typography, vector structure, semantics, and animation.
- [AIBench](https://deep-kaixun.github.io/aibench-page/) - Benchmarks academic illustration generation with 300 open-access papers and 5,704 hierarchical QA pairs for visual-logical consistency and aesthetics.
- [CreativePSD](https://huggingface.co/datasets/creative-graphic-design/CreativePSD) - PSD-derived graphic designs with layer trees, source assets, tool-call trajectories, and intermediate renders.
- [PosterIQ](https://huggingface.co/datasets/ArtmeScienceLab/PosterIQ) - Design-driven poster understanding and generation benchmark with 7,765 image-annotation instances and 822 generation prompts covering layout parsing, typography, design quality, semantic intent, and composition-aware synthesis (CVPR 2026).
- [LICA](https://huggingface.co/datasets/creative-graphic-design/LICA) - Rendered graphic designs with component-level specifications and natural-language design annotations.
- [AesEvalBench](https://arxiv.org/abs/2603.01083) - Evaluates graphic-design aesthetics through localized issue labels, region judgments, and vision-language-model assessments (ICLR 2026).
- [DesignSense](https://arxiv.org/abs/2602.23438) - Provides 10,235 human-annotated graphic-layout preference pairs and a specialized reward model for layout evaluation.
- [E-comIQ-ZH](https://arxiv.org/abs/2602.21698) - Evaluates Chinese e-commerce posters with expert-aligned multidimensional scores and chain-of-thought rationales through E-comIQ-18k and E-comIQ-Bench (CVPR 2026).
- [PosterBench](https://github.com/MeiGen-AI/PosterReward/tree/main/poster_bench) - Benchmarks text-to-image poster generation over 250 prompts with repeated sampling and poster-specific multi-stage scoring.
- [PosterRewardBench](https://github.com/MeiGen-AI/PosterReward/tree/main/poster_reward_bench) - Benchmarks poster-reward models on professionally reviewed preference pairs spanning basic and advanced generation quality regimes.
- [PosterOmni-Bench](https://github.com/MeiGen-AI/PosterOmni) - Benchmarks unified image-to-poster creation across local editing and global design tasks with reference adherence, composition, and aesthetic evaluation.
- [SciFlow-Bench](https://arxiv.org/abs/2602.09809) - Evaluates structure-aware scientific diagram generation by inverse-parsing rendered outputs into canonical graphs for round-trip structural comparison.
- [FigureBench](https://huggingface.co/datasets/WestlakeNLP/FigureBench) - Provides 3,300 long-form text–scientific-illustration pairs spanning papers, surveys, blogs, and textbooks for generation benchmarking.
- [AutoPP1M](https://github.com/JD-GenX/AutoPP#-datasets) - Provides one million product posters and online-feedback data for poster generation and CTR-oriented preference optimization.
### 2025

- [ProImage-Bench](https://github.com/kodenii/TechImage-Bench) - Provides rubric-based professional-image evaluation with 654 tasks, 6,076 criteria, and 44,131 binary checks across scientific and technical imagery.
- [PPTArena](https://arxiv.org/abs/2512.03042) - Benchmarks natural-language PowerPoint editing over real decks with structural and visual evaluation and introduces the PPTPilot editing agent (ECCV 2026).
- [GenPoster-100K](https://huggingface.co/datasets/creative-graphic-design/GenPoster100K) - Poster data with rendered backgrounds, PSD references, and layer-level typography, color, and geometry annotations.
- [AdProd-100K](https://github.com/Anonymous-Name-139/RefAdgen) - Provides product images, advertising images, masks, and text descriptions for high-fidelity product-preserving advertising generation.
- [SciGA-145k](https://huggingface.co/datasets/iyatomilab/SciGA) - Provides a large-scale scientific-paper and figure corpus with graphical abstracts plus intra-paper and inter-paper graphical-abstract recommendation tasks.
- [PrismLayersPro](https://huggingface.co/datasets/artplus/PrismLayersPro) - Provides 20K human-filtered multi-layer transparent images with RGBA layers, captions, layouts, and style labels for layered-generation research.
- [SridBench](https://arxiv.org/abs/2505.22126) - Benchmarks scientific illustration generation with 1,120 expert-curated instances across 13 disciplines and six quality dimensions.
- [BannerRequest400](https://huggingface.co/datasets/creative-graphic-design/BannerRequest400) - Advertising banner requests with brand logos, multimodal design instructions, and target designs.
- [Sci-PosterLayout](https://github.com/kitman0000/Sci-PosterLayout-Data) - Contains 1,226 scientific poster layouts spanning diverse domains and content attributes for scientific-poster generation.
- [PITA](https://tianchi.aliyun.com/dataset/209898) - Provides 38,017 product-centric e-commerce advertising designs with product masks, foreground/background prompts, and graphic and nongraphic element layouts.
### 2024

- [RF1M](https://github.com/JD-GenX/Reliable_AD#rf1m-dataset) - Provides more than one million human-annotated generated advertising images labeled for availability and common product-background generation failures.
- [DesignProbe](https://arxiv.org/abs/2404.14801) - Benchmarks multimodal large language models on graphic-design understanding and reasoning tasks (2024).
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
## Evaluation Methods and Metrics

Reusable scoring methods and evaluation procedures that compare generated designs independently of any single dataset or benchmark.

### 2026

- [PBS](https://github.com/JD-GenX/Uni-AdGen/tree/main/PBS_metrics) - Measures product-background similarity for evaluating advertising-image generation independently of text-generation metrics.
- [PosterReward](https://arxiv.org/abs/2603.29855) - Provides poster-specific reward models that score graphic designs across visual quality, artifacts, textual accuracy, prompt fidelity, and aesthetics (CVPR 2026).
### 2024

- [Design-o-Meter](https://arxiv.org/abs/2411.14959) - Scores graphic-design quality and proposes refinements within a unified learned evaluation-and-improvement framework (WACV 2025).
- [Graphic Design Evaluation](https://arxiv.org/abs/2410.08885) - Evaluates alignment, overlap, white space, and related graphic-design principles with absolute and pairwise judgments (SIGGRAPH Asia 2024).
- [LTSim](https://arxiv.org/abs/2407.12356) - Measures layout similarity through transportation-based matching of structured elements for layout-generation evaluation (2024).
### 2020

- [LayoutGCN](https://research.adobe.com/publication/learning-structural-similarity-of-user-interface-layouts-using-graph-networks/) - Learns structural layout-similarity embeddings with a graph-convolutional encoder and convolutional decoder for retrieval over interface layouts (ECCV 2020).
### Other

- [Layout FID](https://github.com/creative-graphic-design/design-generators/tree/main/models/layout-fid) - Provides a learned feature-space metric for comparing generated and real layout distributions.
## Models and Implementations

- [Creative Graphic Design Datasets](https://github.com/creative-graphic-design/huggingface-datasets) - Maintains reproducible Hugging Face loaders and dataset cards for graphic-design research datasets.
- [design-generators](https://github.com/creative-graphic-design/design-generators) - Ports layout, poster, and graphic-design generation research into consistent Transformers, Diffusers, and agent interfaces.
- [GPT Graphic Design Evaluator](https://github.com/creative-graphic-design/gpt-graphic-design-evaluator) - Implements vision-language-model-based evaluation for graphic-design outputs.
- [Graphic Design Evaluation](https://github.com/creative-graphic-design/Graphic-design-evaluation) - Provides evaluation assets and implementations for measuring graphic-design quality principles.
- [Qwen-Image EliGen Poster](https://huggingface.co/DiffSynth-Studio/Qwen-Image-EliGen-Poster) - Provides Qwen-Image LoRA weights specialized for e-commerce poster generation with precise region-mask control over poster entities.
## Relevant Venues and Workshops

Recurring publication venues and workshop series worth monitoring for work in this area. Inclusion here indicates relevance to the field, not that every paper from a venue is in scope.

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
- [Pacific Graphics](https://pg2025.nccu.edu.tw/) - Computer graphics; includes optimization, authoring, and graphic-layout research.
- [SIGGRAPH](https://www.siggraph.org/) - Computer graphics and interactive techniques; important for content-aware design and visual composition.
- [SIGGRAPH Asia](https://asia.siggraph.org/) - Computer graphics and interactive techniques; relevant for graphic-design generation and evaluation.
- [WACV](https://wacv.thecvf.com/) - Computer vision; includes graphic-design evaluation and multimodal visual-generation work.
### Journals

- [ACM Transactions on Graphics](https://dl.acm.org/journal/tog) - Graphics journal associated with SIGGRAPH research in visual synthesis and design.
- [IEEE Transactions on Multimedia](https://signalprocessingsociety.org/publications-resources/ieee-transactions-multimedia) - Multimedia journal covering visual composition, poster layout, and multimodal generation.
- [IEEE Transactions on Visualization and Computer Graphics](https://www.computer.org/csdl/journal/tg) - Visualization and graphics journal with foundational work on learned graphic layouts.
- [Information Fusion](https://www.sciencedirect.com/journal/information-fusion) - Information-fusion journal including surveys and multimodal generative methods.
- [Pattern Recognition](https://www.sciencedirect.com/journal/pattern-recognition) - Pattern-recognition journal publishing scientific-poster and controllable poster-layout generation research.
- [The Visual Computer](https://link.springer.com/journal/371) - Graphics and visual-computing journal with work on layout and graphic-design generation.
### Workshops

- [AI for Content Creation (AI4CC)](https://ai-for-content-creation.github.io/) - Recurring CVPR workshop on AI-assisted content creation across art, design, documents, advertising, photography, video, and related media.
- [AI for Creative Visual Content Generation, Editing and Understanding (CVEU)](https://openaccess.thecvf.com/CVPR2025_workshops/CVEU) - Workshop series on generative and editing technologies for creative visual content, with editions across CVPR, ICCV, ECCV, and SIGGRAPH-related venues.
- [Graphic Design Understanding and Generation (GDUG)](https://sites.google.com/view/gdug-workshop) - Dedicated graphic-design workshop series; held at CVPR 2024 and ICCV 2025 with topics spanning layout, typography, datasets, evaluation, and AI-assisted authoring.
- [Human-Interactive Generation and Editing (HiGen)](https://higen-2025.github.io/) - Human-interactive visual generation and editing workshop; first held at ICCV 2025 and second at CVPR 2026, including multimodal control and sketch-guided design generation.
## Related Resources

- [Creative Graphic Design](https://github.com/creative-graphic-design) - Organization hosting datasets, model ports, evaluation tools, and research infrastructure used by several entries in this list.
## Contributing

Contributions are welcome. Please read the [contribution guidelines](CONTRIBUTING.md) before opening a pull request.
