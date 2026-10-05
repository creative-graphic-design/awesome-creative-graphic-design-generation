# Awesome Creative Graphic Design Generation [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

Curated resources for generating, editing, representing, and evaluating composed graphic-design artifacts such as posters, advertisements, social-media graphics, magazine layouts, banners, and related visual compositions.

This list focuses on work where layout, typography, visual elements, editable structure, or design-specific evaluation is a first-class part of the problem. Generic text-to-image generation and generic image editing are out of scope unless they make a direct contribution to graphic-design generation.

## Contents

- [Papers](#papers)
  - [Layout Generation](#layout-generation)
  - [Content-Aware Graphic Design](#content-aware-graphic-design)
  - [Language and Multimodal Design Agents](#language-and-multimodal-design-agents)
  - [End-to-End Graphic Design Generation](#end-to-end-graphic-design-generation)
- [Datasets](#datasets)
- [Benchmarks and Evaluation](#benchmarks-and-evaluation)
- [Models and Implementations](#models-and-implementations)
- [Related Resources](#related-resources)

## Papers

### Layout Generation

- [CanvasVAE](https://arxiv.org/abs/2108.01249) - Uses a variational autoencoder to model element-level layouts for design documents (ICCV 2021).
- [Coarse-to-Fine](https://ojs.aaai.org/index.php/AAAI/article/view/19994) - Generates layouts hierarchically from coarse global structure to fine element placement (AAAI 2022).
- [DeepLayout](https://arxiv.org/abs/2006.14615) - Models layouts autoregressively as sequences for conditional and unconditional generation (ICCV 2021).
- [DLT](https://arxiv.org/abs/2303.03755) - Applies diffusion modeling to structured layout generation (ICCV 2023).
- [FlexDM](https://arxiv.org/abs/2303.18248) - Supports flexible layout generation and completion through masked multi-field diffusion (CVPR 2023).
- [LACE](https://arxiv.org/abs/2402.04754) - Introduces lightweight diffusion for controllable layout generation (ICLR 2024).
- [Layout-BLT](https://arxiv.org/abs/2112.05112) - Uses bidirectional layout transformers to generate and refine object arrangements (ECCV 2022).
- [Layout-Corrector](https://arxiv.org/abs/2409.16689) - Corrects intermediate diffusion layouts to improve structure and constraint satisfaction (ECCV 2024).
- [LayoutAction](https://ojs.aaai.org/index.php/AAAI/article/view/26277) - Frames autoregressive layout generation as a sequence of placement actions (AAAI 2023).
- [LayoutDiffusion](https://arxiv.org/abs/2303.11589) - Uses discrete diffusion for controllable layout generation (ICCV 2023).
- [LayoutDM](https://arxiv.org/abs/2303.08137) - Models layouts with discrete denoising diffusion and supports multiple conditional generation tasks (CVPR 2023).
- [LayoutFlow](https://arxiv.org/abs/2403.18187) - Uses flow matching for continuous structured layout generation (ECCV 2024).
- [LayoutFormer++](https://arxiv.org/abs/2208.08037) - Treats layout generation as a sequence-to-sequence task with unified conditioning (CVPR 2023).
- [LayoutGAN](https://openreview.net/forum?id=HJxB5sRcFQ) - Introduces a GAN formulation for synthesizing layouts represented by labeled geometric elements (ICLR 2019).
- [LayoutGAN++](https://arxiv.org/abs/2108.00871) - Improves GAN-based layout generation with differentiable rendering and stronger geometric reasoning (ACM MM 2021).
- [LayoutVAE](https://arxiv.org/abs/1907.10719) - Uses a label-conditioned variational autoencoder for structured document layout generation (ICCV 2019).

### Content-Aware Graphic Design

- [CGB-DM](https://arxiv.org/abs/2407.15233) - Uses a diffusion transformer for graphic-layout generation with content-aware conditioning.
- [CGL-GAN](https://arxiv.org/abs/2205.00303) - Generates advertising layouts conditioned on visual content and introduces the CGL dataset (IJCAI 2022).
- [CreatiPoster](https://arxiv.org/abs/2506.10890) - Generates poster layouts from multimodal content and design requirements.
- [Desigen](https://arxiv.org/abs/2403.09093) - Jointly generates advertising backgrounds and foreground element layouts (CVPR 2024).
- [Graphist](https://arxiv.org/abs/2404.14368) - Models graphic-design layouts with multimodal and structural context.
- [LaDeCo](https://arxiv.org/abs/2412.19712) - Generates layered and editable graphic designs rather than flattened images (CVPR 2025).
- [LayoutDETR](https://arxiv.org/abs/2212.09877) - Generates foreground layouts conditioned on content images for advertising design (ECCV 2024).
- [PosterLayout](https://arxiv.org/abs/2303.15937) - Introduces a benchmark and content-aware approach for visual-textual poster layout generation (CVPR 2023).
- [RADM](https://arxiv.org/abs/2306.09086) - Generates content-aware advertising layouts with richer text and visual conditioning (CIKM 2023).
- [RALF](https://arxiv.org/abs/2311.13602) - Retrieves relevant design examples to guide content-aware layout generation (CVPR 2024).
- [SciPostLayout](https://arxiv.org/abs/2407.19787) - Targets structured layout generation for scientific posters.
- [SEGA](https://arxiv.org/abs/2510.15749) - Uses stepwise evolution for content-aware poster layout generation and introduces GenPoster-100K (ICCV 2025).

### Language and Multimodal Design Agents

- [LayoutGPT](https://arxiv.org/abs/2305.15393) - Uses large language models with in-context demonstrations for layout generation (NeurIPS 2023).
- [LayoutNUWA](https://arxiv.org/abs/2309.09506) - Represents visual layouts as code for language-model-based generation and reasoning (ICLR 2024).
- [LayoutPrompter](https://arxiv.org/abs/2311.06495) - Prompts large language models for zero-shot and few-shot visual layout generation (NeurIPS 2023).
- [PosterLLaMA](https://arxiv.org/abs/2404.00995) - Adapts a multimodal language model to poster layout generation (ECCV 2024).
- [PosterLLaVA](https://arxiv.org/abs/2406.02884) - Uses multimodal instruction tuning for poster layout generation (IEEE TMM 2024).
- [PosterO](https://openaccess.thecvf.com/content/CVPR2025/html/Hsu_PosterO_Structuring_Layout_Trees_to_Enable_Language_Models_in_Generalized_CVPR_2025_paper.html) - Structures layouts as trees so language models can solve generalized layout-generation tasks (CVPR 2025).
- [TextLap](https://arxiv.org/abs/2410.12844) - Generates graphic layouts from textual design requirements with language-model-based reasoning.

### End-to-End Graphic Design Generation

- [CreatiDesign](https://arxiv.org/abs/2505.19114) - Uses a multi-conditional diffusion transformer to compose primary visuals, decorative elements, text, and layout for graphic design.
- [PSDesigner](https://arxiv.org/abs/2603.25738) - Automates layered graphic-design workflows with editable PSD structure and tool-use trajectories (CVPR 2026).

## Datasets

- [BannerRequest400](https://huggingface.co/datasets/creative-graphic-design/BannerRequest400) - Advertising banner requests with brand logos, multimodal design instructions, and target designs.
- [CGL Dataset](https://huggingface.co/datasets/creative-graphic-design/CGL-Dataset) - Advertising poster images, inpainted backgrounds, element categories, and bounding-box annotations.
- [CGL Dataset v2](https://huggingface.co/datasets/creative-graphic-design/CGL-Dataset-v2) - Poster backgrounds with text-aware element boxes, masks, and layout metadata.
- [CreativePSD](https://huggingface.co/datasets/creative-graphic-design/CreativePSD) - PSD-derived graphic designs with layer trees, source assets, tool-call trajectories, and intermediate renders.
- [CTXFont](https://huggingface.co/datasets/creative-graphic-design/CTXFont) - Web-design screenshots with text-element boxes, font properties, and contextual metadata.
- [GenPoster-100K](https://huggingface.co/datasets/creative-graphic-design/GenPoster100K) - Poster data with rendered backgrounds, PSD references, and layer-level typography, color, and geometry annotations.
- [LayoutDETR Dataset](https://huggingface.co/datasets/creative-graphic-design/LayoutDETR) - Advertising banners with foreground layouts and inpainted background assets.
- [LICA](https://huggingface.co/datasets/creative-graphic-design/LICA) - Rendered graphic designs with component-level specifications and natural-language design annotations.
- [Magazine](https://huggingface.co/datasets/creative-graphic-design/Magazine) - Contains fine-grained polygon layouts and semantic element labels for magazine pages.
- [PKU PosterLayout](https://huggingface.co/datasets/creative-graphic-design/PKU-PosterLayout) - Poster images with visual-textual element boxes, saliency maps, and inpainted canvases.

## Benchmarks and Evaluation

- [AesEvalBench](https://arxiv.org/abs/2603.01083) - Evaluates graphic-design aesthetics through localized issue labels, region judgments, and vision-language-model assessments (ICLR 2026).
- [Graphic Design Evaluation](https://arxiv.org/abs/2410.08885) - Evaluates alignment, overlap, white space, and related graphic-design principles with absolute and pairwise judgments (SIGGRAPH Asia 2024).
- [Layout FID](https://github.com/creative-graphic-design/design-generators/tree/main/models/layout-fid) - Provides a learned feature-space metric for comparing generated and real layout distributions.

## Models and Implementations

- [Creative Graphic Design Datasets](https://github.com/creative-graphic-design/huggingface-datasets) - Maintains reproducible Hugging Face loaders and dataset cards for graphic-design research datasets.
- [design-generators](https://github.com/creative-graphic-design/design-generators) - Ports layout, poster, and graphic-design generation research into consistent Transformers, Diffusers, and agent interfaces.
- [Graphic Design Evaluation](https://github.com/creative-graphic-design/Graphic-design-evaluation) - Provides evaluation assets and implementations for measuring graphic-design quality principles.
- [GPT Graphic Design Evaluator](https://github.com/creative-graphic-design/gpt-graphic-design-evaluator) - Implements vision-language-model-based evaluation for graphic-design outputs.

## Related Resources

- [Creative Graphic Design](https://github.com/creative-graphic-design) - Organization hosting datasets, model ports, evaluation tools, and research infrastructure used by several entries in this list.

## Contributing

Contributions are welcome. Please read the [contribution guidelines](CONTRIBUTING.md) before opening a pull request.
