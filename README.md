# Awesome Creative Graphic Design Generation [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![Catalog Check](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/workflows/catalog-check.yml/badge.svg)](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/workflows/catalog-check.yml)
[![Awesome Lint](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/workflows/awesome-lint.yml/badge.svg)](https://github.com/creative-graphic-design/awesome-creative-graphic-design-generation/actions/workflows/awesome-lint.yml)

![Total Resources](https://img.shields.io/badge/resources-241-informational)
![Papers](https://img.shields.io/badge/papers-185-informational)
![Datasets and Benchmarks](https://img.shields.io/badge/datasets%20%26%20benchmarks-40-informational)
![Reproducibility Audited](https://img.shields.io/badge/reproducibility%20audited-96-informational)

<!-- This file is generated from data/*.csv by scripts/generate_readme.py. Do not edit it directly. -->

Curated resources for generating, editing, representing, and evaluating composed graphic-design artifacts such as posters, advertisements, social-media graphics, magazine layouts, scientific figures, graphical abstracts, scientific posters, slides, banners, and related visual compositions.

This list focuses on work where layout, typography, visual elements, editable structure, or design-specific evaluation is a first-class part of the problem. Generic text-to-image generation and generic image editing are out of scope unless they make a direct contribution to graphic-design generation.

Research resources are ordered by **first public appearance** within each category, from newest to oldest. The sort key is the earlier of the arXiv v1 date and the venue/presentation date when both are known; journal-only work uses its first public publication date.

Short paper architecture labels are stored directly in [`data/resources.csv`](data/resources.csv) and rendered with each paper. Implementation metadata is tracked separately in [`data/paper_metadata.csv`](data/paper_metadata.csv), including project pages, official code and weight-release status, base models, training and evaluation datasets, output representation, and the date the release status was last checked.

## Contents

- [Surveys and Overviews](#surveys-and-overviews)
- [Papers](#papers)
  - [Content-Agnostic Layout Generation](#content-agnostic-layout-generation)
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
- [Relevant Venues and Workshops](#relevant-venues-and-workshops)
  - [Conferences](#conferences)
  - [Journals](#journals)
  - [Workshops](#workshops)
- [Related Resources](#related-resources)

## Surveys and Overviews

### 2025

- [From Fragment to One Piece: A Review on AI-Driven Graphic Design](https://doi.org/10.3390/jimaging11090289) - Reviews AI-driven graphic-design generation across layout, visual content, text, and integrated systems (Journal of Imaging 2025).
### 2023

- [Intelligent Layout Generation Based on Deep Generative Models: A Comprehensive Survey](https://doi.org/10.1016/j.inffus.2023.101940) - Reviews deep generative approaches to layout generation, their representations, conditions, datasets, and evaluation (Information Fusion 2023).
- [A Survey for Graphic Design Intelligence](https://arxiv.org/abs/2309.01371) - Surveys computational methods for understanding and generating graphic design artifacts (2023).

## Papers

Papers are classified by their **primary output and task**, rather than by model family. LLM-, VLM-, diffusion-, and agent-based approaches can therefore appear in any category.

<ul>
<li><strong>Content-Agnostic Layout Generation:</strong> Outputs structured element geometry or arrangement without relying on the visual content of a target canvas.</li>
<li><strong>Content-Aware Layout Generation:</strong> Still outputs layout or placement, but conditions that geometry on a background image, product/brand assets, saliency, element content, or another visual canvas.</li>
<li><strong>Graphic Design Generation:</strong> Goes beyond geometry to create a composed design artifact, such as backgrounds, imagery, typography, styles, layers, or editable HTML/CSS/PSD/PPTX structures.</li>
<li><strong>Composable and Layered Asset Generation:</strong> Produces transparent, separable, layered, chroma-keyed, or intentionally empty-space visual assets that can be independently composed or edited in downstream design workflows.</li>
<li><strong>Typography and Text Rendering:</strong> Focuses primarily on legible, faithful, or stylized text generation and placement within designed imagery.</li>
<li><strong>Graphic Design Editing and Reconstruction:</strong> Focuses on iterative editing, layer recovery, or conversion of rendered designs back into editable structures.</li>
<li><strong>Scientific Figure and Graphical Abstract Generation:</strong> Converts scientific papers or long-form technical content into methodology figures, diagrams, Figure 1-style summaries, or graphical abstracts, including editable vector outputs.</li>
<li><strong>Scientific Poster and Slide Generation:</strong> Covers research communication workflows that combine source-document understanding, content selection, layout, typography, rendering, and often editable poster or slide output.</li>
</ul>

### Content-Agnostic Layout Generation

#### 2026

- [i-Design](https://link.springer.com/chapter/10.1007/978-3-032-14826-1_18) - Optimizes graphic layout design step by step with progressive aesthetic policy optimization (ECCV 2026). **Architecture:** Autoregressive; Transformer; VLM.
#### 2025

- [Sketch-to-Layout](https://arxiv.org/abs/2510.27632) - Generates layouts from intuitive user sketches and content assets with a multimodal Transformer and releases large-scale synthetic sketch supervision (ICCV 2025 HiGen Workshop). **Architecture:** Transformer. [Project](https://github.com/google-deepmind/sketch_to_layout) · Code: `unknown` · Weights: `unknown`.<br>  **Base:** PaLI Gemma 3B · **Train:** PubLayNet; DocLayNet; SlideVQA · **Eval:** PubLayNet; DocLayNet; SlideVQA · **Output:** Structured graphic layouts conditioned on sketches and content assets.
- [LayoutRectifier](https://arxiv.org/abs/2508.11177) - Rectifies generated graphic layouts with two-stage optimization over grid alignment, overlap, and containment while limiting deviation from the input layout (Pacific Graphics 2025). **Architecture:** Optimization. [Project](https://jdily.github.io/layoutrectifier.github.io/) · Code: `announced` · Weights: `n/a`.<br>  **Train:** None · **Eval:** PubLayNet; Magazine; CGL · **Output:** Rectified structured layout boxes.
- [StructLayoutFormer](https://doi.org/10.1109/TVCG.2025.3574311) - Generates explicitly structured layouts with a Transformer using structure serialization and disentanglement for conditional structure control (TVCG 2025). **Architecture:** Transformer. Project: — · [Code](https://github.com/Teagrus/StructLayoutFormer) (`announced`) · Weights: `announced`.<br>  **Base:** Transformer · **Train:** RICO; WebForest · **Eval:** RICO; WebForest · **Output:** Hierarchical structured layouts and serialized layout sequences.
- [CLASS](https://openaccess.thecvf.com/content/WACV2025/html/Manandhar_CLASS_Conditional_Latent_Architecture_for_Search_and_Synthesis_of_Design_WACV_2025_paper.html) - Unifies layout synthesis and retrieval with a variational latent representation, an autoregressive Transformer layout decoder, and a raster decoder (WACV 2025). **Architecture:** Autoregressive; Transformer; VAE. [Project](https://research.adobe.com/publication/class-conditional-latent-architecture-for-search-and-synthesis-of-design-layouts/) · Code: `unknown` · Weights: `unknown`.<br>  **Base:** Autoregressive Transformer layout decoder; CNN raster decoder · **Train:** RICO; PubLayNet · **Eval:** RICO; PubLayNet · **Output:** Structured layouts; raster reconstruction; latent layout embeddings.
- [LGGPT](https://doi.org/10.1007/s11263-025-02353-2) - Unifies multiple layout-generation tasks and domains with compact instruction and response encodings for a 1.5B-parameter large language model (IJCV 2025). **Architecture:** LLM. Project: — · [Code](https://github.com/NiceRingNode/LGGPT) (`training + inference`) · Weights: `unknown`.<br>  **Base:** GPT2-XL (1.5B) · **Train:** PubLayNet; RICO; Magazine; WiSe; SPaSe · **Eval:** PubLayNet; RICO; Magazine · **Output:** Serialized layout responses and structured layout boxes.
#### 2024

- [LayoutKAG: Enhancing Layout Generation in Large Language Models Through Knowledge-Augmented Generation](https://doi.org/10.1109/AIHCIR65563.2024.00056) - Uses knowledge-augmented generation to improve large-language-model layout generation and control (AIHCIR 2024). **Architecture:** LLM.
- [TextLap](https://arxiv.org/abs/2410.12844) - Generates graphic layouts from textual design requirements with language-model-based reasoning (EMNLP Findings 2024). **Architecture:** LLM. Project: — · [Code](https://github.com/puar-playground/TextLap) (`training + inference`) · [Weights](https://huggingface.co/puar-playground/TextLap-Graphic) (`released`).<br>  **Base:** Vicuna-7B-v1.5 · **Train:** InstLap; Crello-cap; COCO layout data · **Eval:** Crello; COCO · **Output:** JSON graphic-design layouts; CSS-like image-layout plans.
- [Layout-Corrector](https://arxiv.org/abs/2409.16689) - Corrects intermediate diffusion layouts to improve structure and constraint satisfaction (ECCV 2024). **Architecture:** Diffusion. [Project](https://iwa-shi.github.io/Layout-Corrector-Project-Page/) · [Code](https://github.com/line/Layout-Corrector) (`training + inference`) · [Weights](https://drive.google.com/file/d/1og3l0enR67rDwiAN44K4RchcFYAgsbNq/view) (`released`).<br>  **Base:** Layout-Corrector classifier with LayoutDM, VQDiffusion, or MaskGIT generators · **Train:** PubLayNet; RICO; Crello · **Eval:** PubLayNet; RICO; Crello · **Output:** Structured corrected layout boxes.
- [CoLay](https://arxiv.org/abs/2405.13045) - Uses multi-conditional latent diffusion to generate layouts with style properties from flexible combinations of text, guidelines, element types, and partial designs. **Architecture:** Diffusion. Project: — · Code: `unknown` · Weights: `unknown`.<br>  **Base:** VAE; Transformer-based latent diffusion denoiser · **Train:** CLAY; C4 · **Eval:** CLAY; C4 · **Output:** Structured UI/web layouts with geometry and style attributes.
- [LayoutFlow](https://arxiv.org/abs/2403.18187) - Uses flow matching for continuous structured layout generation (ECCV 2024). **Architecture:** Flow Matching. Project: — · [Code](https://github.com/JulianGuerreiro/LayoutFlow) (`training + inference`) · [Weights](https://huggingface.co/JulianGuerreiro/LayoutFlow) (`released`).<br>  **Base:** Transformer-style layout backbone · **Train:** RICO; PubLayNet · **Eval:** RICO; PubLayNet · **Output:** Structured layout boxes.
- [LACE](https://arxiv.org/abs/2402.04754) - Introduces lightweight diffusion for controllable layout generation (ICLR 2024). **Architecture:** Diffusion. Project: — · [Code](https://github.com/puar-playground/LACE) (`training + inference`) · [Weights](https://huggingface.co/datasets/puar-playground/LACE/tree/main) (`released`).<br>  **Base:** Transformer diffusion denoiser · **Train:** PubLayNet; RICO; Magazine · **Eval:** PubLayNet; RICO; Magazine · **Output:** Structured layout boxes.
- [Spot the Error](https://arxiv.org/abs/2401.16375) - Improves non-autoregressive graphic-layout generation with a learned wireframe locator that identifies erroneous layout tokens for iterative refinement (AAAI 2024). **Architecture:** Encoder-only Neural Model. Project: — · [Code](https://github.com/ffffatgoose/SpotError) (`announced`) · Weights: `unknown`.<br>  **Base:** Non-autoregressive decoder; wireframe locator · **Train:** PubLayNet; RICO · **Eval:** PubLayNet; RICO · **Output:** Structured layout tokens and boxes.
#### 2023

- [LayoutPrompter](https://arxiv.org/abs/2311.06495) - Prompts large language models for zero-shot and few-shot visual layout generation (NeurIPS 2023). **Architecture:** LLM. Project: — · [Code](https://github.com/microsoft/LayoutGeneration/tree/main/LayoutPrompter) (`pipeline`) · Weights: `n/a`.<br>  **Base:** GPT-family API models · **Train:** None · **Eval:** RICO; PubLayNet; PKU PosterLayout; WebUI · **Output:** Structured layout boxes.
- [Dolfin](https://arxiv.org/abs/2310.16305) - Uses a diffusion layout transformer without an autoencoder for structured layout generation (ECCV 2024). **Architecture:** Autoregressive; Transformer; Diffusion. Project: — · Code: `unknown` · Weights: `unknown`.<br>  **Base:** Transformer diffusion encoder; autoregressive Dolfin-AR variant · **Train:** PubLayNet; RICO; ShanghaiTech Wireframe · **Eval:** PubLayNet; RICO; ShanghaiTech Wireframe · **Output:** Structured layout boxes; line-segment structures.
- [LayoutNUWA](https://arxiv.org/abs/2309.09506) - Represents visual layouts as code for language-model-based generation and reasoning (ICLR 2024). **Architecture:** LLM. Project: — · [Code](https://github.com/ProjectNUWA/LayoutNUWA) (`training + inference`) · Weights: `unknown`.<br>  **Base:** LLaMA2-7B; CodeLLaMA-7B · **Train:** RICO; PubLayNet; Magazine · **Eval:** RICO; PubLayNet; Magazine · **Output:** HTML/code-form layout representation.
- [Parse-Then-Place](https://arxiv.org/abs/2308.12700) - Parses textual design descriptions into structured constraints before placing graphic elements (ICCV 2023). **Architecture:** Autoregressive; Transformer. Project: — · [Code](https://github.com/microsoft/LayoutGeneration/tree/main/Parse-Then-Place) (`training + inference`) · [Weights](https://huggingface.co/datasets/KyleLin/Parse-Then-Place) (`released`).<br>  **Base:** T5-v1_1-base semantic parser; learned layout-placement model · **Train:** RICO; WebUI · **Eval:** RICO; WebUI · **Output:** Intermediate representation plus structured layout boxes.
- [Learn and Sample Together](https://www.ijcai.org/proceedings/2023/649) - Jointly trains a spatial-graph generator and graph-conditioned layout decoder with collaborative knowledge transfer for constrained graphic-layout generation (IJCAI 2023). **Architecture:** Encoder-only Neural Model.
- [LayoutGPT](https://arxiv.org/abs/2305.15393) - Uses large language models with in-context demonstrations for layout generation (NeurIPS 2023). **Architecture:** LLM. [Project](https://layoutgpt.github.io/) · [Code](https://github.com/UCSB-AI/LayoutGPT) (`pipeline`) · Weights: `n/a`.<br>  **Base:** GPT-4 / GPT-3.5; optional Llama-2 · **Train:** None · **Eval:** NSR-1K; 3D-FRONT/3D-FUTURE · **Output:** Structured 2D image layouts; 3D scene layouts.
- [LayoutDM: Transformer-Based Diffusion Model for Layout Generation](https://arxiv.org/abs/2305.02567) - Instantiates conditional DDPM layout generation with a purely Transformer-based denoiser for diverse, high-quality conditional layouts (CVPR 2023). **Architecture:** Transformer; Diffusion. Project: — · Code: `unknown` · Weights: `unknown`.<br>  **Base:** 8-layer Transformer layout denoiser with 8-head attention · **Train:** Rico; PubLayNet; Magazine; COCO; TextLogo3K · **Eval:** Rico; PubLayNet; Magazine; COCO; TextLogo3K · **Output:** Structured layout boxes; text-logo character layouts.
- [Layout Generation for Various Scenarios in Mobile Shopping Apps](https://doi.org/10.1145/3544548.3581446) - Introduces LayoutVQ-VAE, a discrete latent model for generating layouts under internal and scenario-level constraints in mobile shopping applications (CHI 2023). **Architecture:** VAE.
- [FlexDM](https://arxiv.org/abs/2303.18248) - Supports flexible layout generation and completion through masked multi-field diffusion (CVPR 2023). **Architecture:** Diffusion. [Project](https://cyberagentailab.github.io/flex-dm/) · [Code](https://github.com/CyberAgentAILab/flex-dm) (`training + inference`) · [Weights](https://storage.googleapis.com/ailab-public/flexdm/pretrained_weights/crello.zip) (`released`).<br>  **Base:** Encoder-decoder with multimodal field heads · **Train:** Crello; RICO · **Eval:** Crello; RICO · **Output:** Vector-graphic document fields and layouts.
- [LayoutDiffusion](https://arxiv.org/abs/2303.11589) - Uses discrete diffusion for controllable layout generation (ICCV 2023). **Architecture:** Diffusion. [Project](https://layoutdiffusion.github.io/) · [Code](https://github.com/microsoft/LayoutGeneration/tree/main/LayoutDiffusion) (`training + inference`) · [Weights](https://huggingface.co/Junyi42/layoutdiffusion) (`released`).<br>  **Base:** Transformer discrete-diffusion denoiser · **Train:** RICO; PubLayNet · **Eval:** RICO; PubLayNet · **Output:** Structured layout sequences and boxes.
- [LayoutDM](https://arxiv.org/abs/2303.08137) - Models layouts with discrete denoising diffusion and supports multiple conditional generation tasks (CVPR 2023). **Architecture:** Transformer; Diffusion. [Project](https://cyberagentailab.github.io/layout-dm) · [Code](https://github.com/CyberAgentAILab/layout-dm) (`training + inference`) · [Weights](https://github.com/CyberAgentAILab/layout-dm/releases/tag/v1.0.0) (`released`).<br>  **Base:** Transformer-style discrete denoiser · **Train:** RICO; PubLayNet · **Eval:** RICO; PubLayNet · **Output:** Structured layout boxes.
- [LDGM](https://arxiv.org/abs/2303.05049) - Decouples discrete element attributes and continuous geometry in a diffusion model for unified layout generation (CVPR 2023). **Architecture:** Diffusion. Project: — · Code: `unknown` · Weights: `unknown`.<br>  **Base:** Transformer-based reverse-diffusion model over layout attributes · **Train:** Magazine; Rico; PubLayNet · **Eval:** Magazine; Rico; PubLayNet · **Output:** Structured layout attributes and bounding boxes.
- [DLT](https://arxiv.org/abs/2303.03755) - Applies diffusion modeling to structured layout generation (ICCV 2023). **Architecture:** Diffusion. [Project](https://wix-incubator.github.io/DLT/) · [Code](https://github.com/wix-incubator/DLT) (`training + inference`) · Weights: `unknown`.<br>  **Base:** Transformer diffusion model over categorical and geometric layout variables · **Train:** RICO; PubLayNet; Magazine · **Eval:** RICO; PubLayNet; Magazine · **Output:** Structured layout samples.
- [LayoutAction](https://ojs.aaai.org/index.php/AAAI/article/view/26277) - Frames autoregressive layout generation as a sequence of placement actions (AAAI 2023). **Architecture:** Autoregressive; Transformer. Project: — · [Code](https://github.com/microsoft/KC/tree/main/papers/LayoutAction) (`announced`) · Weights: `unknown`.<br>  **Base:** 6-layer Transformer (hidden size 512; 8 heads) · **Train:** Rico; PubLayNet; InfoPPT · **Eval:** Rico; PubLayNet; InfoPPT · **Output:** Intermediate action sequences; structured layout boxes.
- [PLay](https://arxiv.org/abs/2301.11529) - Uses parametrically conditioned latent diffusion for controllable layout generation (ICML 2023). **Architecture:** Diffusion. Project: — · Code: `unknown` · Weights: `unknown`.<br>  **Base:** Transformer first-stage encoder/decoder; Transformer latent-diffusion denoiser · **Train:** CLAY; RICO-Semantic; PubLayNet · **Eval:** CLAY; RICO-Semantic; PubLayNet · **Output:** Structured vector-graphic layouts conditioned on guidelines.
- [Machine Learning Model to Evaluate the Appropriateness of Layout for Automatic Generation of Graphic Design Works](https://doi.org/10.1109/IMCOM56909.2023.10035646) - Uses adversarial layout generation and a trained discriminator to generate and score graphic-design layouts conditioned on specified materials (IMCOM 2023). **Architecture:** GAN.
#### 2022

- [LayoutFormer++](https://arxiv.org/abs/2208.08037) - Treats layout generation as a sequence-to-sequence task with unified conditioning (CVPR 2023). **Architecture:** Autoregressive; Transformer. Project: — · [Code](https://github.com/microsoft/LayoutGeneration/tree/main/LayoutFormer%2B%2B) (`training + inference`) · [Weights](https://huggingface.co/jzy124/LayoutFormer) (`released`).<br>  **Base:** Transformer encoder-decoder · **Train:** RICO; PubLayNet · **Eval:** RICO; PubLayNet · **Output:** Serialized/discretized layout boxes.
- [Coarse-to-Fine](https://ojs.aaai.org/index.php/AAAI/article/view/19994) - Generates layouts hierarchically from coarse global structure to fine element placement (AAAI 2022). **Architecture:** VAE. Project: — · [Code](https://github.com/microsoft/LayoutGeneration/tree/main/Coarse-to-Fine) (`training + inference`) · [Weights](https://huggingface.co/jzy124/Coarse2Fine/tree/main) (`released`).<br>  **Train:** RICO; PubLayNet · **Eval:** RICO; PubLayNet · **Output:** Structured layout boxes.
#### 2021

- [Layout-BLT](https://arxiv.org/abs/2112.05112) - Uses bidirectional layout transformers to generate and refine object arrangements (ECCV 2022). **Architecture:** Transformer. [Project](https://shawnkx.github.io/blt) · [Code](https://github.com/google-research/google-research/tree/master/layout-blt) (`training + inference`) · Weights: `unknown`.<br>  **Base:** Bidirectional Transformer · **Train:** COCO; RICO; PubLayNet; Magazine · **Eval:** COCO; RICO; PubLayNet; Magazine · **Output:** Structured layout boxes.
- [LayoutMCL](https://arxiv.org/abs/2301.06629) - Uses an autoregressive multi-choice predictor with winner-takes-all learning to generate diverse multimedia layouts from the same input (ACM MM 2021). **Architecture:** Autoregressive. Project: — · Code: `unknown` · Weights: `unknown`.<br>  **Base:** Autoregressive neural layout predictor with multi-choice heads · **Train:** Magazine; PubLayNet; RICO · **Eval:** Magazine; PubLayNet; RICO · **Output:** Ordered multimedia element bounding-box layouts.
- [CanvasVAE](https://arxiv.org/abs/2108.01249) - Uses a variational autoencoder to model element-level layouts for design documents (ICCV 2021). **Architecture:** VAE. Project: — · [Code](https://github.com/CyberAgentAILab/canvas-vae) (`training + inference`) · Weights: `unknown`.<br>  **Base:** CanvasVAE with learned PixelVAE image embeddings · **Train:** Crello; RICO · **Eval:** Crello; RICO · **Output:** Vector-graphic document structure and element attributes.
- [Constrained Graphic Layout Generation via Latent Optimization](https://arxiv.org/abs/2108.00871) - Introduces LayoutGAN++ and constrained latent optimization for generating realistic layouts that satisfy alignment, overlap, and other explicit design constraints (ACM MM 2021). **Architecture:** Transformer; Optimization; GAN. Project: — · [Code](https://github.com/ktrk115/const_layout) (`training + inference`) · Weights: `released`.<br>  **Base:** Transformer generator and discriminator · **Train:** RICO; PubLayNet · **Eval:** RICO; PubLayNet · **Output:** Structured layout boxes.
- [VTN](https://arxiv.org/abs/2104.02416) - Combines self-attention with a variational autoencoder to learn global design rules and synthesize diverse layouts (CVPR 2021). **Architecture:** Transformer; VAE. Project: — · Code: `unknown` · Weights: `unknown`.<br>  **Base:** Self-attention VAE encoder-decoder; autoregressive decoder variant · **Train:** PubLayNet; RICO; COCO-Stuff; SUN RGB-D · **Eval:** PubLayNet; RICO; COCO-Stuff; SUN RGB-D · **Output:** Variable-length labeled bounding-box layouts.
#### 2020

- [LayoutTransformer: Layout Generation and Completion With Self-Attention](https://arxiv.org/abs/2006.14615) - Uses self-attention to autoregressively generate and complete layouts by modeling contextual relationships among layout elements across multiple structured-layout domains (ICCV 2021). **Architecture:** Autoregressive; Transformer. [Project](https://kampta.github.io/layout) · [Code](https://github.com/kampta/DeepLayout) (`training + inference`) · Weights: `unknown`.<br>  **Base:** GPT-style Transformer decoder · **Train:** COCO; PubLayNet; RICO; PartNet · **Eval:** COCO; PubLayNet; RICO; PartNet · **Output:** Serialized layout primitives and structured boxes.
- [AC-LayoutGAN](https://doi.org/10.1109/TVCG.2020.2999335) - Generates graphic layouts conditioned on element attributes such as area, aspect ratio, and reading order with an attribute-conditioned GAN (TVCG). **Architecture:** GAN. Project: — · Code: `unknown` · Weights: `unknown`.<br>  **Base:** Attribute-conditioned generator; global and element-dropout local discriminators · **Train:** Approximately 17K professionally designed advertisement layouts · **Eval:** Approximately 17K advertisement layouts; user study · **Output:** Advertisement bounding-box layouts conditioned on area aspect ratio and reading order.
#### 2019

- [Neural Design Network](https://arxiv.org/abs/1912.09421) - Generates graphic layouts under explicit design constraints with a neural structured model (ECCV 2020). **Architecture:** VAE. [Project](https://research.google/pubs/neural-design-network-graphic-layout-generation-with-constraints/) · Code: `unknown` · Weights: `unknown`.<br>  **Base:** Graph relation completion; sequential layout generator; graph-convolutional refinement · **Train:** Magazine; RICO; Image banner ads · **Eval:** Magazine; RICO; Image banner ads · **Output:** Component-relation graphs and structured bounding-box layouts.
- [READ: Recursive Autoencoders for Document Layout Generation](https://arxiv.org/abs/1909.00302) - Generates hierarchical document layouts with a recursive variational autoencoder and introduces a structural similarity metric for dense document compositions (CVPRW 2020). **Architecture:** VAE. [Project](https://www.amazon.science/publications/read-recursive-autoencoders-for-document-layout-generation) · Code: `unknown` · Weights: `unknown`.<br>  **Base:** Recursive neural network VAE over document hierarchies · **Train:** ICDAR2015; User-Solicited forms dataset · **Eval:** ICDAR2015; User-Solicited forms dataset · **Output:** Hierarchical document structure and labeled bounding-box layouts.
- [LayoutVAE](https://arxiv.org/abs/1907.10719) - Uses a label-conditioned variational autoencoder for structured document layout generation (ICCV 2019). **Architecture:** VAE. Project: — · Code: `unknown` · Weights: `unknown`.<br>  **Base:** CountVAE; autoregressive BBoxVAE · **Train:** MNIST-Layouts; COCO 2017 Panoptic · **Eval:** MNIST-Layouts; COCO 2017 Panoptic · **Output:** Label-conditioned object bounding-box layouts.
- [LayoutGAN](https://openreview.net/forum?id=HJxB5sRcFQ) - Introduces a GAN formulation for synthesizing layouts represented by labeled geometric elements (ICLR 2019). **Architecture:** GAN. Project: — · [Code](https://github.com/JiananLi2016/LayoutGAN-Tensorflow) (`training + inference`) · Weights: `unknown`.<br>  **Base:** Self-attention generator; CNN wireframe discriminator · **Train:** MNIST; document layouts; clipart; tangram · **Eval:** MNIST; document layouts; clipart; tangram · **Output:** Point and bounding-box graphic layouts.
#### 2015

- [DesignScape](https://doi.org/10.1145/2702123.2702149) - Provides interactive refinement and brainstorming layout suggestions that improve position, scale, and alignment during graphic-design authoring (CHI 2015). **Architecture:** Optimization.
#### 2014

- [Learning Layouts for Single-Page Graphic Designs](https://doi.org/10.1109/TVCG.2014.48) - Learns layout relationships from existing single-page graphic designs to support automatic composition (TVCG 2014). **Architecture:** Optimization.
#### 2012

- [Automatic Stylistic Manga Layout](https://doi.org/10.1145/2366145.2366160) - Generates stylistic manga page layouts from input artworks and user-specified semantics with parametric style models, probabilistic initialization, and joint geometry refinement (SIGGRAPH Asia 2012). **Architecture:** Optimization.
#### 2007

- [Specifying Label Layout Style by Example](https://doi.org/10.1145/1294211.1294252) - Learns a designer-specified label-layout style from an example via nonlinear inverse optimization, then synthesizes new labeled-diagram layouts in the learned style (UIST 2007). **Architecture:** Optimization.
#### 2003

- [Adaptive Grid-Based Document Layout](https://doi.org/10.1145/882262.882353) - Adapts grid-based magazine and newspaper page designs to different display sizes using reusable adaptive layout templates (SIGGRAPH 2003). **Architecture:** Template-Based; Optimization.
#### 1994

- [Interactive Graphic Design Using Automatic Presentation Knowledge](https://doi.org/10.1145/191666.191719) - Introduces SageBrush, SageBook, and SAGE to combine knowledge-based automatic presentation with interactive construction, retrieval, and customization of data graphics (CHI 1994). **Architecture:** Knowledge-Based.
#### 1988

- [Applying a Theory of Graphical Presentation to the Graphic Design of User Interfaces](https://doi.org/10.1145/62402.62431) - Extends automatic graphical-presentation theory to theory-driven design of graphical user interfaces (UIST 1988). **Architecture:** Knowledge-Based.
#### 1986

- [Automating the Design of Graphical Presentations of Relational Information](https://doi.org/10.1145/22949.22950) - Codifies expressiveness and effectiveness criteria plus a composition algebra in APT to automatically synthesize graphical presentations of relational information (ACM TOG 1986). **Architecture:** Knowledge-Based.

### Content-Aware Layout Generation

#### 2026

- [iPoster](https://arxiv.org/abs/2603.29469) - Supports interactive content-aware poster layout generation under flexible user-specified constraints (CHI EA 2026). **Architecture:** Diffusion; Graph Neural Network.
- [Seeing is Improving: Visual Feedback for Iterative Text Layout Refinement](https://arxiv.org/abs/2603.22187) - Introduces VFLM, which iteratively renders and visually critiques SVG text layouts over background images, using visually grounded reinforcement learning to improve readability and aesthetics (CVPR 2026). **Architecture:** VLM; Multi-stage System. Project: — · [Code](https://github.com/FolSpark/VFLM) (`training + inference`) · Weights: `released`.<br>  **Base:** Qwen2.5-VL 3B/7B · **Eval:** Multiple text-layout benchmarks · **Output:** SVG layout.
#### 2025

- [Content-Aware Ad Banner Layout Generation with Two-Stage Chain-of-Thought in Vision Language Models](https://arxiv.org/abs/2512.12596) - Uses a VLM to analyze advertisement background content and plan text and logo placement before rendering an HTML layout. **Architecture:** VLM; Multi-stage System.
- [UniLayDiff](https://arxiv.org/abs/2512.08897) - Unifies diverse content-aware layout constraints in a single multimodal diffusion transformer with relation-aware LoRA adaptation (CVPR Findings 2026). **Architecture:** Transformer; Diffusion.
- [SEGA](https://arxiv.org/abs/2510.15749) - Uses stepwise evolution for content-aware poster layout generation and introduces GenPoster-100K (ICCV 2025). **Architecture:** Multi-stage System; VLM. [Project](https://brucew91.github.io/SEGA.github.io) · [Code](https://github.com/BruceW91/SEGA) (`inference only`) · [Weights](https://pan.baidu.com/s/1jW7jMjWEOWCgSTU-jUjsNw) (`released`).<br>  **Base:** LLaVA-1.5 7B/13B; CLIP ViT-L/14-336 · **Train:** GenPoster-100K; Crello · **Eval:** Crello · **Output:** Structured poster layout.
- [LLMs as Layout Designers (LaySPA)](https://arxiv.org/abs/2509.16891) - Augments language-model layout agents with reinforcement-learned spatial reasoning over geometric validity, structural fidelity, and visual quality. **Architecture:** LLM.
- [Uni-Layout](https://arxiv.org/abs/2508.02374) - Unifies multiple layout-generation conditions with human-feedback-based evaluation and preference alignment (ACM MM 2025). **Architecture:** Multi-stage System; VLM. [Project](https://github.com/JD-GenX/Uni-Layout) · [Code](https://github.com/JD-GenX/Uni-Layout) (`evaluation only`) · [Weights](https://drive.google.com/drive/folders/1evrHmorHW7CBLRhxrV3-3qvFki1ovoJ3?usp=drive_link) (`partial`).<br>  **Base:** LLaVA-family multimodal evaluator · **Train:** Layout Generator dataset; Reward Model CoT dataset · **Eval:** Layout Evaluator dataset · **Output:** Structured layout boxes; binary layout-quality judgments.
- [ReLayout: Relation Reasoning for Content-Aware Layout Generation](https://arxiv.org/abs/2507.05568) - Uses relation chain-of-thought and layout-prototype rebalancing to improve structure, diversity, and explainability in multimodal-LLM content-aware layouts. **Architecture:** VLM.
- [CAL-RAG](https://sigirgennext.github.io/GENNEXT-SIGIR-25/submissions/gennext_sigir25_5.pdf) - Combines multimodal retrieval, an LLM layout recommender, a vision-language grader, and feedback agents for iterative content-aware layout generation (SIGIR GENNEXT 2025). **Architecture:** Agentic; LLM; VLM.
- [CreatiPoster](https://arxiv.org/abs/2506.10890) - Generates poster layouts from multimodal content and design requirements. **Architecture:** Multi-stage System; VLM. [Project](https://github.com/graphic-design-ai/creatiposter) · [Code](https://github.com/graphic-design-ai/creatiposter) (`announced`) · Weights: `announced`.<br>  **Base:** RGBA large multimodal protocol model; conditional background generator · **Train:** Copyright-free 100K multi-layer graphic-design corpus · **Eval:** CreatiPoster benchmark · **Output:** Editable multi-layer design specification; raster background/composite.
- [Scan-and-Print](https://arxiv.org/abs/2505.20649) - Uses patch-level image summarization and data augmentation for efficient content-aware poster layout generation (IJCAI 2025). **Architecture:** Autoregressive; Transformer. [Project](https://thekinsley.github.io/Scan-and-Print/) · [Code](https://github.com/theKinsley/Scan-and-Print-IJCAI2025) (`training + inference`) · Weights: `unknown`.<br>  **Base:** DeiT3 visual encoder · **Train:** PKU PosterLayout; CGL · **Eval:** PKU PosterLayout; CGL · **Output:** Structured layout boxes.
- [PosterO](https://arxiv.org/abs/2505.07843) - Structures layouts as trees so language models can solve generalized layout-generation tasks (CVPR 2025). **Architecture:** LLM.
- [AesthetiQ](https://arxiv.org/abs/2503.00591) - Aligns multimodal language models to aesthetic preferences for content-aware graphic layout prediction using preference optimization (CVPR 2025). **Architecture:** VLM.
#### 2024

- [VASCAR](https://arxiv.org/abs/2412.04237) - Uses a large vision-language model to iteratively inspect rendered layouts and self-correct content-aware element placement without additional training. **Architecture:** VLM.
- [Design Element Aware Poster Layout Generation](https://doi.org/10.1145/3627673.3679557) - Models poster design elements and their relationships for content-aware poster layout generation (CIKM 2024). **Architecture:** Transformer.
- [Image-aware layout generation with user constraints for poster design](https://doi.org/10.1007/s00371-024-03657-z) - Generates poster layouts conditioned on a product image while satisfying user-specified element and partial-layout constraints (The Visual Computer 2025).
- [Iris: a multi-constraint graphic layout generation system](https://doi.org/10.1631/FITEE.2300312) - Combines an interactive graphic-layout design system with multi-constraint LayoutVQ-VAE for background-aware generation, editing, and rendering (FITEE 2024). **Architecture:** Multi-stage System; VAE.
- [CGB-DM](https://arxiv.org/abs/2407.15233) - Uses a diffusion transformer for graphic-layout generation with content-aware conditioning. **Architecture:** Transformer; Diffusion.
- [Visual Layout Composer](https://openaccess.thecvf.com/content/CVPR2024/html/Shabani_Visual_Layout_Composer_Image-Vector_Dual_Diffusion_Model_for_Design_Layout_CVPR_2024_paper.html) - Couples image-space and vector-space diffusion to generate design layouts conditioned on visual content (CVPR 2024). **Architecture:** Diffusion.
- [PosterLLaVA](https://arxiv.org/abs/2406.02884) - Uses multimodal instruction tuning for poster layout generation (IEEE TMM 2026). **Architecture:** VLM. [Project](https://huggingface.co/spaces/posterllava/PosterLLaVA) · [Code](https://github.com/posterllava/PosterLLaVA) (`training + inference`) · [Weights](https://huggingface.co/posterllava/posterllava_v0) (`released`).<br>  **Base:** LLaVA-v1.5-7B; CLIP ViT-L/14-336 · **Train:** Ad Banner; CGL; PosterLayout; QB-Poster · **Eval:** QB-Poster; User-Constrained; CGL; PosterLayout · **Output:** JSON poster layout.
- [Automatic Layout Planning for Visually-Rich Documents with Instruction-Following Models](https://arxiv.org/abs/2404.15271) - Uses a multimodal instruction-following model to arrange user-provided visual elements for posters, brochures, book covers, advertisements, and related visually rich documents (ALVR 2024). **Architecture:** VLM.
- [Graphist](https://doi.org/10.1609/aaai.v39i3.32249) - Models graphic-design layouts with multimodal and structural context (AAAI 2025). **Architecture:** VLM. [Project](https://github.com/graphic-design-ai/graphist) · [Code](https://github.com/graphic-design-ai/graphist) (`no release`) · Weights: `announced`.<br>  **Train:** Crello · **Eval:** Crello · **Output:** JSON draft protocol with element coordinates, dimensions, and layer order.
- [PosterLLaMA](https://arxiv.org/abs/2404.00995) - Adapts a multimodal language model to poster layout generation (ECCV 2024). **Architecture:** VLM. [Project](https://lait-cvlab.github.io/PosterLlama/) · [Code](https://github.com/jaepoong/PosterLlama) (`training + inference`) · [Weights](https://huggingface.co/poong/PosterLlama) (`released`).<br>  **Base:** LLaMA2-7B-chat; CodeLLaMA-7B; DINO visual features · **Train:** MiniGPT-4 synthetic caption data; CGL · **Eval:** CGL; poster-layout benchmarks · **Output:** HTML/code-form layout representation.
#### 2023

- [RALF](https://arxiv.org/abs/2311.13602) - Retrieves relevant design examples to guide content-aware layout generation (CVPR 2024). **Architecture:** Autoregressive; Transformer. [Project](https://udonda.github.io/RALF/) · [Code](https://github.com/CyberAgentAILab/RALF) (`training + inference`) · Weights: `released`.<br>  **Base:** ResNet50 image encoder; autoregressive transformer · **Train:** PKU PosterLayout; CGL · **Eval:** PKU PosterLayout; CGL · **Output:** Structured content-aware layouts.
- [DensityLayout](https://doi.org/10.1007/978-3-031-46308-2_16) - Generates visual-textual presentation layouts over given images with density-aware conditioning for automated poster design (ICIG 2023). **Architecture:** GAN.
- [RADM](https://arxiv.org/abs/2306.09086) - Generates content-aware advertising layouts with richer text and visual conditioning (CIKM 2023). **Architecture:** Diffusion.
- [PosterLayout](https://arxiv.org/abs/2303.15937) - Introduces a benchmark and content-aware approach for visual-textual poster layout generation (CVPR 2023). **Architecture:** GAN. Project: — · [Code](https://github.com/PKU-ICST-MIPL/PosterLayout-CVPR2023) (`training + inference`) · Weights: `released`.<br>  **Base:** Visual feature encoder; GAN layout generator · **Train:** PKU PosterLayout · **Eval:** PKU PosterLayout · **Output:** Structured poster layout boxes.
- [PDA-GAN](https://arxiv.org/abs/2303.14377) - Uses GAN-based unsupervised domain adaptation with a pixel-level discriminator to generate image-aware advertising-poster layouts (CVPR 2023). **Architecture:** GAN.
#### 2022

- [LayoutDETR](https://arxiv.org/abs/2212.09877) - Generates foreground layouts conditioned on content images for advertising design (ECCV 2024). **Architecture:** Transformer. Project: — · [Code](https://github.com/salesforce/LayoutDETR) (`training + inference`) · Weights: `released`.<br>  **Base:** DETR-style multimodal conditioning; generative layout backbone · **Train:** LayoutDETR Ad Banner Dataset · **Eval:** LayoutDETR Ad Banner Dataset · **Output:** Structured foreground layout; rendered ad banner.
- [ICVT](https://arxiv.org/abs/2209.00852) - Generates layouts conditioned on image content with geometry-aligned variational transformers (ACM MM 2022). **Architecture:** Autoregressive; Transformer; VAE.
- [CGL-GAN](https://arxiv.org/abs/2205.00303) - Generates advertising layouts conditioned on visual content and introduces the CGL dataset (IJCAI 2022). **Architecture:** GAN. Project: — · [Code](https://github.com/minzhouGithub/CGL-GAN) (`announced`) · Weights: `unknown`.<br>  **Base:** GAN with composition-aware visual conditioning · **Train:** CGL Dataset · **Eval:** CGL Dataset · **Output:** Structured advertising layout boxes.
#### 2021

- [SmartText](https://doi.org/10.1109/TMM.2021.3097900) - Places text over natural images using saliency and learned aesthetic compatibility for harmonious poster composition (TMM 2022). **Architecture:** Multi-stage System.
#### 2019

- [ContentGAN](https://doi.org/10.1145/3306346.3322971) - Generates graphic-design layouts conditioned on underlying visual content (SIGGRAPH 2019). **Architecture:** GAN. [Project](https://xtqiao.com/projects/content_aware_layout/) · [Code](https://portland-my.sharepoint.com/:f:/g/personal/xqiao6-c_my_cityu_edu_hk/EoOt-X32-BlNmdpTPlhNVvEBxEBEHFfTwL1RHWAE_Em-0A?e=U1FYRa) (`unknown`) · Weights: `unknown`.<br>  **Train:** Magazine · **Eval:** Magazine · **Output:** Structured content-aware graphic-design layouts.
#### Other

- [Learning Priority-Aware Controllable Poster Layout Generation](https://doi.org/10.1016/j.patcog.2026.113497) - Uses LLM- and vision-derived priorities, optimal-transport matching, and flow-based refinement for controllable poster layout generation (Pattern Recognition 2026). **Architecture:** Flow Matching; LLM.
- [Two-stage Content-Aware Layout Generation for Poster Designs](https://doi.org/10.1145/3581783.3612275) - Combines aesthetics-conditioned diffusion layout proposals with a learned ranking stage for poster designs over image backgrounds (ACM MM 2023). **Architecture:** Diffusion.

### Graphic Design Generation

#### 2026

- [Designer-RSI](https://arxiv.org/abs/2609.22086) - Adapts a tool-using graphic-design agent through continually refined procedural memory learned from real user briefs. **Architecture:** Agentic.
- [Human-aware Design Generation](https://arxiv.org/abs/2609.17689) - Completes graphic designs by jointly composing 3D human poses, 2D framing, and human-image placement (ACM MM 2026). **Architecture:** Autoregressive; Transformer; VAE.
- [InterIL](https://arxiv.org/abs/2609.11519) - Jointly generates background images and foreground layouts to model bidirectional image-layout interaction in design templates. **Architecture:** Diffusion.
- [Editable Visual Design](https://arxiv.org/abs/2609.04034) - Generates complete editable posters, infographics, and marketing designs with a coding agent that uses VLM-guided planning and aesthetic review, on-demand visual assets, native HTML/CSS, and iterative rendered feedback. **Architecture:** Agentic; VLM. Project: — · [Code](https://github.com/yejy53/Editable-Design) (`pipeline`) · Weights: `n/a`.<br>  **Base:** Coding agent; VLM; image-generation API · **Train:** None · **Output:** Editable HTML/CSS; PNG; editable PPTX.
- [Mise-en-Scène](https://arxiv.org/abs/2608.19000) - Generates editable layered designs by letting layout emerge within a diffusion transformer while preserving source assets. **Architecture:** Transformer; Diffusion.
- [PosterAgent: Agentic Poster Generation via Stage-Aware Reinforcement Learning](https://proceedings.mlr.press/v306/yu26br.html) - Frames poster creation as an agentic draft-and-iterative-refinement workflow trained with stage-aware reinforcement learning (ICML 2026). **Architecture:** Agentic.
- [Design Your Ad](https://arxiv.org/abs/2605.12138) - Jointly generates personalized advertising images and text from multimodal user histories with a unified autoregressive model and introduces PAd1M and PBS (CVPR 2026). **Architecture:** Autoregressive; Transformer. Project: — · [Code](https://github.com/JD-GenX/Uni-AdGen) (`inference only`) · [Weights](https://3.cn/11f4I-YYG) (`released`).<br>  **Base:** Janus-Pro-7B; DINOv2-small; SDXL-Base-1.0 · **Train:** PAd1M · **Eval:** PAd1M; PBS; BLEU; ROUGE · **Output:** Personalized advertising image and product text.
- [SIMPLEPOSTER](https://arxiv.org/abs/2605.08784) - Generates product posters with faithful subject preservation and position-controllable text rendering (CVPR 2026). **Architecture:** Transformer; Diffusion.
- [Brief2Design](https://arxiv.org/abs/2604.11019) - Supports prompt-based professional graphic design through requirement extraction, element exploration, and compositional recombination. **Architecture:** Multi-stage System.
- [ReContraster](https://aclanthology.org/2026.acl-long.98/) - Generates visually salient posters with a compositional multi-agent system that plans regional contrast and layout, synthesizes candidates with diffusion, and critiques rendered outputs (ACL 2026). **Architecture:** Agentic; Diffusion; VLM.
- [PSDesigner](https://arxiv.org/abs/2603.25738) - Automates layered graphic-design workflows with editable PSD structure and tool-use trajectories (CVPR 2026). **Architecture:** Agentic; VLM. [Project](https://henghuiding.com/PSDesigner) · [Code](https://github.com/FudanCVL/PSDesigner) (`announced`) · Weights: `announced`.<br>  **Base:** GraphicPlanner · **Train:** CreativePSD · **Eval:** Crello-v5; copyright-free PSD files · **Output:** Editable PSD.
- [Multi-Object Advertisement Creative Generation](https://arxiv.org/abs/2603.13745) - Introduces CreativeAds for scalable multi-product lifestyle advertising through product pairing, layout generation, background generation, and human oversight. **Architecture:** Multi-stage System.
- [InnoAds-Composer](https://arxiv.org/abs/2603.05898) - Generates e-commerce product posters in a single stage with joint subject, glyph, and style conditioning (CVPR 2026). **Architecture:** Diffusion.
- [PosterOmni](https://arxiv.org/abs/2602.12127) - Unifies local poster editing and global image-to-poster creation through task distillation and poster-specific reward feedback across six creation tasks (CVPR 2026). **Architecture:** Transformer; Diffusion. [Project](https://ephemeral182.github.io/PosterOmni/) · [Code](https://github.com/MeiGen-AI/PosterOmni) (`inference only`) · [Weights](https://huggingface.co/MeiGen-AI/PosterOmni_v1) (`released`).<br>  **Base:** Qwen-Image-Edit / QwenImageEditPlusPipeline · **Train:** PosterOmni-200K · **Eval:** PosterOmni-Bench · **Output:** Raster poster image.
- [DesignAsCode](https://arxiv.org/abs/2602.17690) - Represents graphic designs as HTML/CSS and iteratively plans, implements, and visually refines editable designs (ACM MM 2026). **Architecture:** Multi-stage System; LLM; VLM. [Project](https://liuziyuan1109.github.io/design-as-code/) · [Code](https://github.com/liuziyuan1109/design-as-code) (`training + inference`) · [Weights](https://huggingface.co/Tony1109/DesignAsCode-planner) (`released`).<br>  **Base:** Qwen3-8B planner; GPT-5; GPT-4o; gpt-image-1 · **Train:** DesignAsCode training data (~19K distilled Crello samples) · **Eval:** 546-sample test set; Broad test set · **Output:** Editable HTML/CSS.
- [PosterVerse](https://arxiv.org/abs/2601.03993) - Automates commercial poster creation with blueprint planning, background generation, and HTML-based scalable typography (AAAI 2026). **Architecture:** Multi-stage System; Diffusion; LLM; VLM.
#### 2025

- [AutoPP](https://arxiv.org/abs/2512.21921) - Automates product-poster generation and CTR-oriented optimization using unified design generation and online-feedback preference learning (AAAI 2026). **Architecture:** Multi-stage System. Project: — · [Code](https://github.com/JD-GenX/AutoPP) (`announced`) · Weights: `unknown`.<br>  **Train:** AutoPP1M product-poster generation and optimization subsets · **Eval:** Offline poster-generation metrics; online CTR feedback · **Output:** Raster product poster.
- [RefAdGen](https://arxiv.org/abs/2508.11695) - Generates high-fidelity advertising images while preserving referenced product identity through spatial mask control and product-feature fusion (AAAI 2026). **Architecture:** Diffusion. Project: — · [Code](https://github.com/Anonymous-Name-139/RefAdgen) (`training + inference`) · [Weights](https://huggingface.co/yiyun123/RefAdgen) (`released`).<br>  **Base:** Stable Diffusion v1.5; IP-Adapter; GroundingDINO; SAM2 · **Train:** AdProd-100K · **Eval:** AdProd-100K · **Output:** Raster product advertising image.
- [Rethinking Layered Graphic Design Generation with a Top-Down Approach](https://arxiv.org/abs/2507.05601) - Introduces Accordion, a top-down framework that creates editable layered graphic designs from user intent or sketches by using a VLM for reference creation, design planning, and layer generation (ICCV 2025). **Architecture:** VLM; Multi-stage System.
- [DreamPoster](https://arxiv.org/abs/2507.04218) - Generates image-conditioned posters while preserving source content and supporting flexible resolution, layout, and typographic hierarchy with progressive multi-task training. **Architecture:** Diffusion.
- [Mirror in the Model: Ad Banner Image Generation via Reflective Multi-LLM and Multi-modal Agents](https://aclanthology.org/2025.emnlp-industry.17/) - Uses hierarchical multimodal agents and iterative reflection to generate and refine advertising banners from a prompt and logo image. **Architecture:** Agentic; VLM. Project: — · [Code](https://github.com/sony/mimo) (`pipeline`) · Weights: `n/a`.<br>  **Base:** Configurable Gemini or GPT multimodal/image-generation API models · **Train:** None · **Output:** Raster advertising banner image.
- [PosterCraft](https://arxiv.org/abs/2506.10741) - Generates high-aesthetic posters in a unified diffusion framework with staged text-rendering optimization, region-aware fine-tuning, preference optimization, and vision-language feedback (ICLR 2026). **Architecture:** Diffusion; VLM. [Project](https://ephemeral182.github.io/PosterCraft/) · [Code](https://github.com/MeiGen-AI/PosterCraft) (`inference only`) · [Weights](https://huggingface.co/PosterCraft/PosterCraft-v1_RL) (`released`).<br>  **Base:** FLUX.1-dev · **Train:** Text-Render-2M; HQ-Poster100K · **Eval:** PosterCraft evaluation set · **Output:** Raster poster image.
- [CreatiDesign](https://arxiv.org/abs/2505.19114) - Uses a multi-conditional diffusion transformer to compose primary visuals, decorative elements, text, and layout for graphic design (ICLR 2026). **Architecture:** Transformer; Diffusion. [Project](https://huizhang0812.github.io/CreatiDesign/) · [Code](https://github.com/HuiZhang0812/CreatiDesign) (`inference only`) · [Weights](https://huggingface.co/HuiZhang0812/CreatiDesign) (`released`).<br>  **Base:** FLUX.1-dev · **Train:** CreatiDesign dataset (~400K designs) · **Eval:** CreatiDesign benchmark (1K samples) · **Output:** Raster graphic design.
- [BizGen](https://arxiv.org/abs/2503.20672) - Generates infographic and slide imagery from article-length prompts and ultra-dense layouts using layout-guided cross-attention and region-wise latent refinement (CVPR 2025). **Architecture:** Diffusion.
- [POSTA](https://arxiv.org/abs/2503.14908) - Combines background diffusion, multimodal layout and typography planning, and stylized text generation for customizable artistic posters (CVPR 2025). **Architecture:** Diffusion.
- [BannerAgency](https://arxiv.org/abs/2503.11060) - Uses collaborating multimodal LLM agents to plan and generate advertising banner designs from brand assets and requests (EMNLP 2025). **Architecture:** Agentic; VLM.
- [DesignDiffusion: High-Quality Text-to-Design Image Generation with Diffusion Models](https://arxiv.org/abs/2503.01645) - Generates complete design images directly from text with a one-stage diffusion model, character-aware embeddings and localization supervision, plus self-play preference optimization for visual-text quality (CVPR 2025). **Architecture:** Diffusion.
- [T-Stars-Poster](https://doi.org/10.1145/3746252.3761554) - Generates product-centric advertising images through VLM-guided prompt and layout planning, SDXL background generation, and final graphics rendering (CIKM 2025; arXiv preprint titled PAID). **Architecture:** Multi-stage System; Diffusion; VLM.
#### 2024

- [LaDeCo](https://arxiv.org/abs/2412.19712) - Generates layered and editable graphic designs rather than flattened images (CVPR 2025). **Architecture:** VLM.
- [Towards Reliable Advertising Image Generation Using Human Feedback](https://arxiv.org/abs/2408.00418) - Uses a learned reliable-feedback network, recurrent generation, and feedback-guided diffusion fine-tuning to improve usable e-commerce advertising images (ECCV 2024). **Architecture:** Diffusion. Project: — · [Code](https://github.com/JD-GenX/Reliable_AD) (`inference only`) · [Weights](https://huggingface.co/ZhenbangDu/reliable_controlnet) (`released`).<br>  **Base:** Stable Diffusion v1.5-compatible latent diffusion; ControlNet · **Train:** RF1M · **Eval:** RF1M; human availability feedback · **Output:** Raster product advertising image.
- [OpenCOLE](https://arxiv.org/abs/2406.08232) - Provides an open and reproducible pipeline for automatic layered graphic-design generation (CVPR Workshop 2024). **Architecture:** Multi-stage System; Diffusion; LLM; VLM. Project: — · [Code](https://github.com/CyberAgentAILab/OpenCOLE) (`training + inference`) · [Weights](https://huggingface.co/cyberagent/opencole-stable-diffusion-xl-base-1.0-finetune) (`released`).<br>  **Base:** K-shot LLM; SDXL fine-tune; LLaVA-v1.5-7B typography LoRA; renderer · **Train:** OpenCOLE dataset v1 · **Eval:** GPT-4V-based generated-design evaluation · **Output:** Rendered graphic design.
- [Desigen](https://arxiv.org/abs/2403.09093) - Jointly generates advertising backgrounds and foreground element layouts (CVPR 2024). **Architecture:** Autoregressive; Transformer.
- [Chaining Text-to-Image and Large Language Model for Personalized E-commerce Banners](https://arxiv.org/abs/2403.05578) - Chains an LLM with text-to-image generation to turn shopper interaction and product metadata into personalized e-commerce banner imagery at scale (KDD 2024). **Architecture:** LLM.
- [CG4CTR](https://arxiv.org/abs/2401.10934) - Builds a Stable-Diffusion-based advertising-creative generation pipeline that incorporates user preferences and downstream click-through-rate ranking (WWW 2024 Companion). **Architecture:** Multi-stage System; Diffusion.
#### 2023

- [Planning and Rendering](https://arxiv.org/abs/2312.08822) - Separates semantic planning from visual rendering for end-to-end product-poster generation (2023). **Architecture:** Multi-stage System.
- [COLE](https://arxiv.org/abs/2311.16974) - Uses a hierarchical generation framework to create multi-layered, editable graphic designs from high-level intent (2023). **Architecture:** Multi-stage System; Diffusion; LLM; VLM. [Project](https://graphic-design-generation.github.io/) · Code: `announced` · Weights: `unknown`.<br>  **Base:** Fine-tuned LLMs; large multimodal models; diffusion models · **Train:** Proprietary design data (not publicly released) · **Eval:** DESIGNINTENTION benchmark · **Output:** Multi-layer editable graphic design.
- [AutoPoster](https://arxiv.org/abs/2308.01095) - Integrates content analysis and layout generation into an automatic advertising-poster design system (2023). **Architecture:** Multi-stage System.
#### 2022

- [CreaGAN](https://doi.org/10.1145/3503161.3548763) - Automates display-ad creative adaptation with aesthetics-aware product placement and context-aware inpainting while reusing existing design elements (ACM MM 2022). **Architecture:** Multi-stage System; GAN.
#### 2021

- [Vinci](https://doi.org/10.1145/3411764.3445117) - Introduces an intelligent graphic-design system that composes advertising posters from user-provided product assets and design intent (CHI 2021). **Architecture:** Multi-stage System.

### Composable and Layered Asset Generation

#### 2026

- [UniWorld-Design](https://arxiv.org/abs/2608.03971) - Treats semantic RGBA layers as the native design representation, with text-to-RGBA asset generation and instruction-controlled image-to-layer decomposition into ordered complete layers. **Architecture:** Flow Matching; Transformer.
- [MRT](https://arxiv.org/abs/2605.27235) - Unifies text-to-layers, image-to-layers, and layer-to-layer editing in a 20B masked-region diffusion model for scalable RGBA asset generation (CVPR 2026). **Architecture:** Diffusion. [Project](https://mrt-cvpr.github.io/) · Code: `unknown` · Weights: `unknown`.<br>  **Base:** Qwen-Image · **Train:** 10M+ multilingual layered design samples; 43M+ transparent layers · **Output:** RGBA canvas/background/foreground layer stack.
- [LaDe: Unified Multi-Layered Graphic Media Generation and Decomposition](https://openaccess.thecvf.com/content/CVPR2026W/CVEU/html/Lungu-Stan_LaDe_Unified_Multi-Layered_Graphic_Media_Generation_and_Decomposition_CVPRW_2026_paper.html) - Jointly generates full graphic-media designs and a flexible number of semantically meaningful RGBA layers, while also supporting image-to-layers decomposition with a latent diffusion transformer and RGBA VAE (CVPRW 2026). **Architecture:** Diffusion; Transformer; LLM; VAE.
- [Controllable Layered Image Generation for Real-World Editing](https://arxiv.org/abs/2601.15507) - Introduces LASAGNA, a unified controllable framework that jointly generates composites, clean backgrounds, and transparent foreground layers with physically grounded visual effects. **Architecture:** Flow Matching; Transformer.
#### 2025

- [Qwen-Image-Layered](https://arxiv.org/abs/2512.15603) - Decomposes raster images into variable-length semantically separated RGBA layers for independently editable visual assets (CVPR 2026). **Architecture:** Diffusion. [Project](https://qwen.ai/blog?id=qwen-image-layered&lid=1ami72hcYlwXGTTVQ) · [Code](https://github.com/QwenLM/Qwen-Image-Layered) (`inference only`) · [Weights](https://huggingface.co/Qwen/Qwen-Image-Layered) (`released`).<br>  **Base:** Qwen-Image · **Train:** Internal text-to-RGB/RGBA data; PSD-derived multilayer image corpus · **Eval:** Crello; LayerD decomposition protocol · **Output:** Variable-length RGBA layer stack; PSD/PPTX export.
- [OmniPSD: Layered PSD Generation with Diffusion Transformer](https://arxiv.org/abs/2512.09247) - Uses a unified FLUX-based diffusion-transformer framework for both text-to-PSD generation and flattened-image-to-PSD decomposition with editable transparent layers and an RGBA VAE. **Architecture:** Diffusion; Transformer; VAE. [Project](https://showlab.github.io/OmniPSD/) · [Code](https://github.com/showlab/OmniPSD) (`training + inference`) · Weights: `unknown`.<br>  **Base:** FLUX.1-dev / FLUX.1-Kontext-dev with RGBA VAE · **Train:** OmniPSD Layered Poster dataset · **Eval:** Layered poster evaluation set · **Output:** Editable PSD; RGBA layers.
- [TAUE](https://arxiv.org/abs/2511.02580) - Generates coherent foreground, background, and composite layers without fine-tuning by transplanting and cultivating intermediate diffusion noise representations (CVPR Findings 2026). **Architecture:** Diffusion. [Project](https://iyatomilab.github.io/TAUE/) · [Code](https://github.com/IyatomiLab/TAUE) (`unknown`) · Weights: `n/a`.<br>  **Base:** SDXL · **Train:** None · **Eval:** Filtered MS-COCO · **Output:** Foreground; background; composite image.
- [SAWNA](https://www.siggraph.org/wp-content/uploads/2025/08/Posters.html) - Preserves user-specified negative-space regions during text-to-image generation so downstream text and interface elements can be composed cleanly (SIGGRAPH 2025 Poster). **Architecture:** Diffusion.
- [PrismLayers](https://arxiv.org/abs/2505.22523) - Introduces PrismLayers and PrismLayersPro plus ART+ for high-quality multi-layer transparent image generation from text and layouts. **Architecture:** Transformer; Diffusion. [Project](https://prism-layers.github.io/) · [Code](https://github.com/redredsheep/PrismLayers) (`inference only`) · Weights: `released`.<br>  **Base:** ART · **Train:** PrismLayersPro (20K high-quality subset of 200K PrismLayers) · **Output:** Multiple RGBA layers plus composite image.
- [PSDiffusion: Harmonized Multi-Layer Image Generation via Layout and Appearance Alignment](https://arxiv.org/abs/2505.11468) - Generates multiple transparent layers simultaneously with a unified diffusion framework and global-layer interaction for coherent layout, contacts, shadows, and reflections (WACV 2026). **Architecture:** Diffusion. [Project](https://dingbang777.github.io/PSDiffusion_Website/) · [Code](https://github.com/dingbang777/PSDiffusion) (`announced`) · Weights: `announced`.<br>  **Base:** Pretrained image diffusion model with global-layer interaction · **Train:** Inter-Layer Dataset (announced) · **Eval:** Layer-generation benchmark datasets · **Output:** RGB background + multiple RGBA foreground layers.
- [ART](https://arxiv.org/abs/2502.18364) - Generates variable numbers of transparent image layers from a global prompt and anonymous region layout using an Anonymous Region Transformer (CVPR 2025). **Architecture:** Transformer; Diffusion. Project: — · [Code](https://github.com/microsoft/art-msra) (`withdrawn`) · Weights: `withdrawn`.<br>  **Eval:** DESIGN-MULTI-LAYER-BENCH; PHOTO-MULTI-LAYER-BENCH · **Output:** Variable number of RGBA layers.
- [LayeringDiff: Layered Image Synthesis via Generation, then Disassembly with Generative Knowledge](https://arxiv.org/abs/2501.01197) - Synthesizes a composite image with an off-the-shelf generator and then disassembles it into foreground and background layers using pretrained generative priors and high-frequency alignment. **Architecture:** Diffusion; Multi-stage System.
#### 2024

- [LayerFusion](https://arxiv.org/abs/2412.04460) - Generates harmonized foreground RGBA, background RGB, and composite images jointly using pretrained generative priors (CVPR Findings 2026). **Architecture:** Diffusion. [Project](https://layerfusion.github.io/) · Code: `announced` · Weights: `n/a`.<br>  **Base:** Pretrained latent diffusion model · **Train:** None · **Output:** Foreground RGBA; background RGB; composite RGB.
- [Generative Image Layer Decomposition with Visual Effects](https://arxiv.org/abs/2411.17864) - Introduces LayerDecomp for decomposing images into clean backgrounds and transparent foreground layers while preserving visual effects such as shadows and reflections (CVPR 2025). **Architecture:** Diffusion.
- [TKG-DM](https://arxiv.org/abs/2411.15580) - Generates foreground content over a controllable chroma-key background without training, enabling clean foreground-background separation (CVPR 2025). **Architecture:** Diffusion. Project: — · [Code](https://github.com/ryugo417/TKG-DM) (`pipeline`) · Weights: `n/a`.<br>  **Base:** Stable Diffusion XL 1.0 · **Train:** None · **Output:** RGB image with controlled chroma-key background.
- [Alfie](https://arxiv.org/abs/2408.14826) - Modifies the inference behavior of a pretrained Diffusion Transformer to generate easily isolated RGBA-style illustration assets without additional training (ECCV 2024 AI4VA Workshop). **Architecture:** Transformer; Diffusion.
- [LayerDiffuse](https://doi.org/10.1145/3658150) - Adds latent transparency to pretrained diffusion models for single- and multi-layer transparent image generation (ACM TOG 2024). **Architecture:** Diffusion. [Project](https://github.com/lllyasviel/LayerDiffuse) · [Code](https://github.com/lllyasviel/LayerDiffuse_DiffusersCLI) (`inference only`) · [Weights](https://huggingface.co/LayerDiffusion/layerdiffusion-v1) (`released`).<br>  **Base:** Stable Diffusion v1.5 / SDXL · **Train:** 1M transparent image layer pairs · **Output:** Single or multiple transparent RGBA layers.
#### 2023

- [Text2Layer: Layered Image Generation using Latent Diffusion Model](https://arxiv.org/abs/2307.09781) - Jointly generates background, foreground, layer mask, and composed image in a learned layered latent space, establishing an early diffusion-based layered compositing formulation. **Architecture:** Diffusion; VAE.

### Typography and Text Rendering

#### 2026

- [FreeText](https://proceedings.mlr.press/v306/zhang26ge.html) - Improves precise multi-line and dense text rendering in Diffusion Transformer image generators through attention-based localization and spectral glyph injection without retraining (ICML 2026). **Architecture:** Transformer; Diffusion.
#### 2025

- [UTDesign](https://doi.org/10.1145/3757377.3763923) - Unifies stylized text editing and conditional text generation for graphic-design images and integrates the model into a text-to-design pipeline (SIGGRAPH Asia 2025). **Architecture:** Diffusion; VLM. [Project](https://utdesign-official.github.io/home/) · [Code](https://github.com/ZYM-PKU/UTDesign) (`training + inference`) · [Weights](https://huggingface.co/UTDesign/UTDesign_v1.0) (`released`).<br>  **Base:** Diffusers; FLUX VAE; DINOv2 visual conditioning; CLIP style encoder; multimodal layout planner · **Train:** Gray-scale and colored font data; annotated design-image data including Kingsoft-provided data · **Output:** RGBA foreground glyphs; raster graphic-design images.
- [PosterMaker](https://arxiv.org/abs/2504.06632) - Generates product posters with explicit mechanisms for accurate text rendering and visual composition (CVPR 2025). **Architecture:** Diffusion. [Project](https://poster-maker.github.io) · [Code](https://github.com/alimama-creative/PosterMaker) (`training + inference`) · [Weights](https://huggingface.co/alimama-creative/PosterMaker) (`released`).<br>  **Base:** Stable Diffusion 3 Medium · **Train:** Released e-commerce poster training data · **Eval:** Released stage-1 and stage-2 poster benchmarks · **Output:** Raster product poster with specified text regions.
#### 2024

- [GlyphDraw2](https://arxiv.org/abs/2407.02252) - Generates complex bilingual glyph posters with controllable fonts and precise text placement using LLM-guided SDXL conditioning (AAAI 2025). **Architecture:** Diffusion; LLM. Project: — · [Code](https://github.com/OPPO-Mente-Lab/GlyphDraw2) (`training + inference`) · Weights: `unknown`.<br>  **Base:** SDXL; ControlNet; LLM planner · **Train:** GlyphDraw-3M · **Output:** Raster bilingual poster image.
#### 2023

- [TextDiffuser-2](https://arxiv.org/abs/2311.16465) - Uses language-model planning to improve flexible text layout and rendering in generated images (ECCV 2024). **Architecture:** Diffusion; LLM. [Project](https://jingyechen.github.io/textdiffuser2/) · [Code](https://github.com/microsoft/unilm/tree/master/textdiffuser-2) (`training + inference`) · [Weights](https://huggingface.co/JingyeChen22/textdiffuser2-full-ft) (`released`).<br>  **Base:** Stable Diffusion v1.5; LLM layout planner · **Train:** MARIO-style text-image data; layout-planner instruction data · **Eval:** Text rendering and inpainting benchmarks · **Output:** Raster image with rendered text.
- [TextPainter](https://arxiv.org/abs/2308.04733) - Generates poster-oriented text imagery while balancing text comprehension and visual harmony (ACM MM 2023). **Architecture:** Multi-stage System.
- [TextDiffuser](https://arxiv.org/abs/2305.10855) - Introduces diffusion-based text rendering with explicit character-level layout guidance (NeurIPS 2023). **Architecture:** Diffusion. Project: — · [Code](https://github.com/microsoft/unilm/tree/master/textdiffuser) (`training + inference`) · [Weights](https://huggingface.co/datasets/JingyeChen22/TextDiffuser) (`released`).<br>  **Base:** Stable Diffusion v2.1 · **Train:** MARIO-LAION / MARIO-10M · **Eval:** MARIO-Eval · **Output:** Raster image with rendered text.
#### 2022

- [Text2Poster](https://arxiv.org/abs/2301.02363) - Retrieves suitable imagery and places stylized text to construct poster designs from text input (ICASSP 2022). **Architecture:** VAE.

### Graphic Design Editing and Reconstruction

#### 2026

- [PosterText](https://arxiv.org/abs/2608.16289) - Unifies text-patch generation and editing for e-commerce posters with addition, deletion, modification, and style control. **Architecture:** Flow Matching.
- [ReDesign](https://arxiv.org/abs/2607.25565) - Recovers editable layer hierarchies, typography, geometry, colors, and grouping from raster design images (ECCV 2026). **Architecture:** Multi-stage System.
- [CreatiParser: Generative Image Parsing of Raster Graphic Designs into Editable Layers](https://arxiv.org/abs/2604.19632) - Parses flattened graphic designs into editable text, background, and sticker layers using a VLM text-rendering protocol and multi-branch RGBA diffusion, with preference alignment via ParserReward. **Architecture:** Diffusion; VLM; Multi-stage System.
- [ReLayout: Structure-Preserving Design Layout Editing](https://arxiv.org/abs/2602.01046) - Edits design layouts from natural-language intents while preserving unedited structure through relation graphs and self-supervised relation-aware design reconstruction. **Architecture:** VLM.
- [APEX](https://arxiv.org/abs/2601.04794) - Edits existing academic posters in PPTX format with a multi-agent planning, API-execution, and visual review-and-adjustment workflow under natural-language instructions. **Architecture:** Agentic; VLM. Project: — · [Code](https://github.com/Breesiu/APEX) (`pipeline`) · Weights: `n/a`.<br>  **Base:** Configurable Gemini or Qwen vision-language APIs · **Train:** None · **Eval:** APEX-Bench · **Output:** Editable PPTX.
#### 2025

- [PosterCopilot](https://arxiv.org/abs/2512.04082) - Combines layout reasoning with layer-controllable iterative editing for professional graphic-design workflows (ECCV 2026). **Architecture:** VLM. [Project](https://postercopilot.github.io/) · [Code](https://github.com/JiazheWei/PosterCopilot) (`inference only`) · [Weights](https://huggingface.co/void-2024/PosterCopilot) (`released`).<br>  **Base:** Qwen2.5-VL-7B-Instruct · **Train:** PosterCopilot Dataset (160K posters, 2.6M layers) · **Output:** JSON layout; PNG; editable PSD.
- [LayerD](https://arxiv.org/abs/2509.25134) - Decomposes raster graphic designs into editable layers through iterative foreground extraction and refinement (ICCV 2025). **Architecture:** Multi-stage System. [Project](https://cyberagentailab.github.io/LayerD/) · [Code](https://github.com/CyberAgentAILab/LayerD) (`training + inference`) · [Weights](https://huggingface.co/cyberagent/layerd-birefnet) (`released`).<br>  **Base:** BiRefNet · **Output:** RGBA layers; SVG; PSD.
- [Draw with Thought](https://arxiv.org/abs/2504.09479) - Reconstructs raster scientific diagrams into editable mxGraph XML through coarse-to-fine reasoning and structure-aware code generation (ACM MM 2025). **Architecture:** Multi-stage System; VLM.
#### 2024

- [Neural Contrast](https://arxiv.org/abs/2410.07211) - Uses diffusion-based generative editing to create low-saliency, high-contrast regions beneath design assets for improved graphic-design readability (PRICAI 2024). **Architecture:** Diffusion.
- [Revision Matters](https://arxiv.org/abs/2406.18559) - Fine-tunes a Gemini multimodal backbone on human revision traces to iteratively refine generated layouts toward expert design edits. **Architecture:** VLM.
#### 2021

- [De-Rendering Stylized Texts](https://arxiv.org/abs/2110.01890) - Vectorizes rasterized display text into editable content, geometry, font, styling, effects, and hidden-background parameters through differentiable rendering (ICCV 2021). **Architecture:** Multi-stage System.

### Scientific Figure and Graphical Abstract Generation

#### 2026

- [Figures as Programs](https://arxiv.org/abs/2609.01006) - Generates editable scientific methodology figures as recursively composed SVG programs with source grounding and render-critic refinement. **Architecture:** Multi-stage System; LLM; VLM.
- [PaperBanana-Interact](https://arxiv.org/abs/2608.30241) - Supports multi-turn scientific diagram refinement with human feedback using a critique-and-refine multi-agent workflow. **Architecture:** Agentic.
- [GenGA](https://arxiv.org/abs/2608.05478) - Generates data-grounded graphical abstracts as hierarchical vector elements for element-level post-editing and introduces the SIC editability metric. **Architecture:** Multi-stage System.
- [SciForma](https://arxiv.org/abs/2607.18091) - Generates structure-faithful scientific methodology diagrams by optimizing component, arrow, and text correctness with structured preference learning. **Architecture:** Diffusion. [Project](https://microsoft.github.io/SciForma/index.html) · [Code](https://github.com/microsoft/SciForma) (`training + inference`) · [Weights](https://huggingface.co/LoYuXrqw/SciForma-9B) (`released`).<br>  **Base:** FLUX.2-klein-base-9B · **Train:** SciFormaData-700K · **Eval:** SciFormaBench-2K; AIBench · **Output:** Raster scientific methodology diagram.
- [AutoFigure-Edit](https://aclanthology.org/2026.acl-demo.6/) - Generates fully editable SVG scientific illustrations from long-form scientific text with reference-guided styling and interactive refinement (ACL System Demonstrations 2026). **Architecture:** Multi-stage System; VLM. [Project](https://deepscientist.cc/) · [Code](https://github.com/ResearAI/AutoFigure-Edit) (`pipeline`) · Weights: `n/a`.<br>  **Base:** Configurable multimodal and segmentation models · **Train:** None · **Output:** Editable SVG.
- [AutoFigure](https://arxiv.org/abs/2602.03828) - Uses an agentic planning, recombination, validation, and rendering pipeline to generate publication-ready scientific illustrations from long-form text (ICLR 2026). **Architecture:** Agentic; VLM. [Project](https://deepscientist.cc/) · [Code](https://github.com/ResearAI/AutoFigure) (`pipeline`) · Weights: `n/a`.<br>  **Base:** Configurable LLM and image-generation APIs · **Train:** None · **Eval:** FigureBench · **Output:** SVG; mxGraph XML; PNG preview.
- [PaperBanana](https://proceedings.mlr.press/v306/zhu26ag.html) - Uses specialized retrieval, planning, styling, visualization, and critique agents to generate publication-ready academic illustrations (ICML 2026). **Architecture:** Agentic; VLM. [Project](https://dwzhu-pku.github.io/PaperBanana/) · [Code](https://github.com/google-research/papervizagent) (`pipeline`) · Weights: `n/a`.<br>  **Base:** Configurable VLM and image-generation models · **Train:** None · **Eval:** PaperBananaBench · **Output:** Raster methodology diagrams and statistical plots.
- [SciFig](https://arxiv.org/abs/2601.04390) - Generates visually rich, fully editable scientific methodology figures from paper text using planning, layout, component, and feedback agents with VLM-in-the-loop refinement. **Architecture:** Agentic; VLM. [Project](https://shramanpramanick.github.io/SciFig/) · Code: `announced` · Weights: `unknown`.<br>  **Train:** None · **Eval:** SciFig-Bench (announced) · **Output:** Editable XML.

### Scientific Poster and Slide Generation

#### 2026

- [PosterVisor](https://arxiv.org/abs/2609.17326) - Uses persistent semantic-geometric contracts to control scientific-poster content, layout, validation, and repair. **Architecture:** Multi-stage System.
- [PosterMELD](https://arxiv.org/abs/2608.02218) - Generates controllable, diverse scientific posters with multi-agent planning and editable print-ready PPTX outputs. **Architecture:** Agentic; LLM; VLM. [Project](https://jackey0903.github.io/PosterMELD/) · [Code](https://github.com/Shannon4Science/PosterMELD) (`pipeline`) · Weights: `n/a`.<br>  **Base:** Configurable text model; VLM review; image-generation API · **Train:** None · **Eval:** 621-paper benchmark · **Output:** Editable PPTX; PNG.
- [Personalization as Inverse Planning](https://arxiv.org/abs/2607.00407) - Learns latent page-level design intents for agentic slide personalization through structural denoising and multi-agent reinforcement learning (ECCV 2026). **Architecture:** Agentic; Diffusion.
- [Any2Poster](https://arxiv.org/abs/2606.02915) - Introduces an any-source poster benchmark and agent spanning multiple input modalities and content domains. **Architecture:** Agentic; LLM; VLM. [Project](https://any2poster.github.io/) · [Code](https://github.com/Any2Poster/Any2Poster) (`pipeline`) · Weights: `n/a`.<br>  **Base:** Configurable OpenRouter LLM/VLM models; Gemini 3 Pro visual synthesis; Playwright rendering · **Train:** None · **Eval:** Any2Poster Bench; BenchQuiz; VLM-as-Judge · **Output:** HTML artifact; PDF; PNG.
- [ArcDeck](https://arxiv.org/abs/2604.11969) - Generates polished academic slide decks from papers by reconstructing narrative structure with discourse parsing, multi-agent outline critique, layout planning, and PPTX rendering (ECCV 2026). **Architecture:** Agentic; LLM. [Project](https://arcdeck.org/) · [Code](https://github.com/RehgLab/ArcDeck) (`pipeline`) · Weights: `n/a`.<br>  **Base:** Configurable GPT/Claude/Qwen/vLLM language models; python-pptx/PptxGenJS rendering · **Train:** None · **Eval:** ArcBench · **Output:** Editable PPTX; slide-planning JSON intermediates.
- [Design First Code Later](https://aclanthology.org/2026.findings-acl.1524/) - Introduces DeepSlides, a template-free design-first slide-generation workflow with SlideDesign data and reinforcement-learned SlideQwen models (ACL Findings 2026). **Architecture:** LLM. Project: — · [Code](https://github.com/sxswz213/DeepSlides) (`pipeline`) · Weights: `unknown`.<br>  **Base:** Configurable LLMs plus SlideQwen design/implementation models · **Train:** SlideDesign · **Output:** Editable PPTX; slide images.
#### 2025

- [SlideTailor](https://arxiv.org/abs/2512.20292) - Generates personalized editable presentation slides from scientific papers by distilling user preferences from paper-slide examples and visual templates with an agentic multimodal pipeline (AAAI 2026). **Architecture:** Agentic; VLM. Project: — · [Code](https://github.com/nusnlp/SlideTailor) (`pipeline`) · Weights: `n/a`.<br>  **Base:** GPT-4o-2024-08-06; PPTAgent-derived slide rendering pipeline · **Train:** None · **Eval:** SlideTailor-PSP dataset · **Output:** Editable PPTX.
- [SlideGen](https://arxiv.org/abs/2512.04529) - Coordinates multimodal agents to transform scientific papers into editable PPTX slide decks with visual-in-the-loop refinement (ACM MM 2026). **Architecture:** Agentic. [Project](https://y-research-sbu.github.io/SlideGen/) · [Code](https://github.com/Y-Research-SBU/SlideGen) (`pipeline`) · Weights: `n/a`.<br>  **Base:** API-based multimodal agents · **Train:** None · **Eval:** Scientific slide-generation benchmarks · **Output:** Editable PPTX.
- [SciPostGen](https://arxiv.org/abs/2511.22490) - Introduces a large-scale paper-poster dataset and retrieval-augmented scientific-poster layout generation (CVPR Findings 2026). **Architecture:** Multi-stage System.
- [PosterForest](https://arxiv.org/abs/2508.21720) - Uses a hierarchical Poster Tree and collaborating agents to jointly optimize scientific-poster content, structure, and layout (ACL 2026). **Architecture:** Agentic; LLM; VLM. Project: — · [Code](https://github.com/kaist-cvml/poster-forest) (`pipeline`) · Weights: `n/a`.<br>  **Base:** GPT-4o or local Qwen3/Qwen2.5 models · **Train:** None · **Eval:** Paper2Poster-style evaluation · **Output:** Editable PPTX; JPG.
- [PosterGen](https://arxiv.org/abs/2508.17188) - Uses specialized agents for paper parsing, curation, layout, styling, and rendering to generate scientific posters. **Architecture:** Agentic; LLM.
- [Paper2Poster](https://arxiv.org/abs/2505.21497) - Introduces a multimodal paper-to-poster benchmark and a visual-in-the-loop multi-agent system that exports editable PPTX posters (NeurIPS 2025). **Architecture:** Agentic. [Project](https://paper2poster.github.io/) · [Code](https://github.com/Paper2Poster/Paper2Poster) (`pipeline`) · Weights: `n/a`.<br>  **Base:** Configurable GPT-4o or Qwen-2.5 LLM/VLM backends; PPTX rendering · **Train:** None · **Eval:** Paper2Poster dataset; PaperQuiz; VLM-as-Judge · **Output:** Editable PPTX.
- [P2P](https://arxiv.org/abs/2505.17104) - Uses a multi-agent pipeline to generate HTML academic posters from papers and introduces instruction data and fine-grained evaluation. **Architecture:** Agentic. Project: — · [Code](https://github.com/multimodal-art-projection/P2P) (`pipeline`) · Weights: `n/a`.<br>  **Base:** Configurable API language models such as GPT-4o-mini or Claude · **Train:** P2PInstruct · **Eval:** P2PEval · **Output:** Poster JSON; HTML; PNG.
- [Scientific Poster Generation A New Dataset and Approach](https://doi.org/10.1016/j.patcog.2025.111507) - Introduces the 1,226-poster Sci-PosterLayout dataset and a template-free sequence generator with a Design Pattern Schema for scientific-poster layouts (Pattern Recognition 2025). **Architecture:** Autoregressive.
#### 2024

- [SciPostLayout](https://arxiv.org/abs/2407.19787) - Introduces a scientific-poster dataset and targets structured layout analysis and generation for scientific posters (BMVC 2024). **Architecture:** LLM. Project: — · [Code](https://github.com/omron-sinicx/scipostlayout) (`training + inference`) · Weights: `n/a`.<br>  **Base:** LayoutLMv3; DiT; LayoutDM; LayoutFormer++; GPT-4 · **Train:** SciPostLayout · **Eval:** SciPostLayout · **Output:** Scientific-poster layouts.
- [PostDoc](https://arxiv.org/abs/2405.20213) - Generates posters from long multimodal documents using learned submodular content selection, LLM paraphrasing, and content-conditioned template generation (AAAI 2025). **Architecture:** Multi-stage System; Optimization; LLM.

## Datasets and Benchmarks

Datasets provide reusable examples, assets, annotations, or corpora for training and evaluation. Benchmarks add a fixed task, split, protocol, or test set. Because many resources serve both roles, they are listed once in this combined section.

### 2026

- [MTPaperBananaBench](https://shirley-wu.github.io/PaperBanana-Interact/index.html) - Benchmarks multi-turn scientific diagram refinement with 292 images and 3,518 user requirements covering content, layout, and visual representation.
- [CoDeLayout](https://hukcc.github.io/Beyond-Atomic-Layouts/) - Provides 20,009 training and 387 manually verified test multi-layer graphic designs with rendered images, structured layer metadata, and QA annotations for compositional element pairs and design intent (ECCV 2026).
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
- [BMVC](https://www.bmva.org/bmvc) - Computer vision; annual BMVA conference with an official proceedings archive and relevant scientific-poster/document-layout research.
- [CHI](https://chi.acm.org/) - Human-computer interaction; relevant for interactive and human-centered graphic-design systems.
- [CIKM](https://www.cikmconference.org/) - Information and knowledge management; has published industrial poster-layout and content-aware design work.
- [CVPR](https://cvpr.thecvf.com/) - Computer vision; frequently publishes layout, poster, multimodal generation, and evaluation work.
- [ECCV](https://eccv.ecva.net/) - Computer vision; strong coverage of layout, editable design, slide design, and image-generation research.
- [ICASSP](https://signalprocessingsociety.org/event-names/icassp) - Signal processing and multimedia; annual IEEE Signal Processing Society flagship series that includes poster and text-layout generation work.
- [ICCV](https://iccv.thecvf.com/) - Computer vision; relevant for layout generation, content-aware design, and structured visual generation.
- [ICLR](https://iclr.cc/) - Machine learning; relevant for generative models, language-based layout generation, scientific-poster agents, and evaluation.
- [ICME](https://ieee-cas.org/media-bookdirectory/icme) - Multimedia; recurring IEEE flagship series since 2000 and relevant for multimodal content generation and visual-design systems.
- [ICML](https://icml.cc/) - Machine learning; relevant for generative modeling and controllable structured generation.
- [IJCAI](https://www.ijcai.org/) - Artificial intelligence; includes content-aware advertising and poster-layout generation.
- [NeurIPS](https://neurips.cc/) - Machine learning; relevant for generative modeling, multimodal agents, evaluation, and scientific-poster automation.
- [Pacific Graphics](https://asiagraphics.org/) - Annual flagship conference of the Asia Graphics Association; includes optimization, authoring, and graphic-layout research.
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

- [AI for Content Creation (AI4CC)](https://ai-for-content-creation.github.io/) - Recurring CVPR workshop series; the official archive lists annual editions from 2020 through 2025 and CVPR 2026 hosted another edition, covering art, design, documents, advertising, photography, video, and related media.
- [AI for Creative Visual Content Generation, Editing and Understanding (CVEU)](https://cveu.github.io/) - Long-running creative-visual-content workshop series with verified editions across ICCV, ECCV, CVPR, SIGGRAPH, and SIGGRAPH Asia; the official series site tracks the continuing edition history.
- [Graphic Design Understanding and Generation (GDUG)](https://sites.google.com/view/gdug-workshop) - Recurring dedicated graphic-design workshop; CVF proceedings verify editions at CVPR 2024 and ICCV 2025 spanning layout, typography, datasets, evaluation, and AI-assisted authoring.
- [Human-Interactive Generation and Editing (HiGen)](https://higen-2025.github.io/) - Recurring human-interactive generation/editing workshop; ICCV 2025 was the first edition and CVPR 2026 explicitly hosted the 2nd workshop, including multimodal control and sketch-guided design generation.

## Related Resources

- [Creative Graphic Design](https://github.com/creative-graphic-design) - Organization hosting datasets, model ports, evaluation tools, and research infrastructure used by several entries in this list.

## Contributing

Contributions are welcome. Please read the [contribution guidelines](CONTRIBUTING.md) before opening a pull request.
