---
name: bfl-flux
description: Black Forest Labs FLUX image generation models — text-to-image, image editing (Kontext), inpainting/outpainting (Fill), structural conditioning (Canny/Depth), and image variation (Redux). Use this skill when generating images from text prompts, editing existing images with text guidance, inpainting masked regions, applying canny/depth structural conditioning, or creating image variations with FLUX models. Covers CLI usage, diffusers integration, TensorRT inference, and the BFL API.
license: Apache-2.0 (schnell); FLUX.1-dev Non-Commercial (all other models)
metadata:
  author: Black Forest Labs (black-forest-labs.com)
  source: https://github.com/black-forest-labs/flux
compatibility: Claude Code, any AI coding agent
allowed-tools: Bash, Read, Write, Edit
---

# FLUX — Black Forest Labs Image Generation

Open-weight image generation library supporting text-to-image, image editing, inpainting, structural conditioning, and image variation.

## Installation

```bash
# Basic install
pip install -e "."

# With TensorRT support
pip install -e ".[tensorrt]"
```

## Models

| Model | HuggingFace Repo | License | Use Case |
|-------|-----------------|---------|----------|
| `FLUX.1 [schnell]` | black-forest-labs/FLUX.1-schnell | Apache-2.0 | Fast text-to-image (4 steps) |
| `FLUX.1 [dev]` | black-forest-labs/FLUX.1-dev | Non-Commercial | High-quality text-to-image |
| `FLUX.1 Krea [dev]` | black-forest-labs/FLUX.1-Krea-dev | Non-Commercial | Krea-tuned text-to-image |
| `FLUX.1 Kontext [dev]` | black-forest-labs/FLUX.1-Kontext-dev | Non-Commercial | Image editing with text |
| `FLUX.1 Fill [dev]` | black-forest-labs/FLUX.1-Fill-dev | Non-Commercial | Inpainting & outpainting |
| `FLUX.1 Canny [dev]` | black-forest-labs/FLUX.1-Canny-dev | Non-Commercial | Edge-map conditioning |
| `FLUX.1 Depth [dev]` | black-forest-labs/FLUX.1-Depth-dev | Non-Commercial | Depth-map conditioning |
| `FLUX.1 Canny [dev] LoRA` | black-forest-labs/FLUX.1-Canny-dev-lora | Non-Commercial | Canny LoRA for FLUX.1 [dev] |
| `FLUX.1 Depth [dev] LoRA` | black-forest-labs/FLUX.1-Depth-dev-lora | Non-Commercial | Depth LoRA for FLUX.1 [dev] |
| `FLUX.1 Redux [dev]` | black-forest-labs/FLUX.1-Redux-dev | Non-Commercial | Image variation adapter |

Weights download automatically to `checkpoints/` on first run. Or set env vars:

```bash
export FLUX_MODEL=<path>
export FLUX_AE=<path>       # autoencoder
export FLUX_REDUX=<path>    # for Redux
export FLUX_LORA=<path>     # for LoRA variants
```

## Text-to-Image (t2i)

```bash
# Interactive loop
python -m flux t2i --name flux-dev --loop
python -m flux t2i --name flux-schnell --loop

# Single sample
python -m flux t2i --name flux-dev \
  --height 1024 --width 1024 \
  --prompt "A cat holding a sign that says hello world"

# TRT inference
python -m flux t2i --name=flux-dev --loop --trt --trt_transformer_precision bf16
# precision: bf16, fp8, fp4 — height/width must be 768–1344 for ONNX exports
```

## Image Editing — Kontext

```bash
# Interactive loop
python -m flux kontext --loop

# Single sample
python -m flux kontext \
  --img_cond_path <path_to_input_image> \
  --prompt "change the background to a forest" \
  --num_steps 30 --aspect_ratio "16:9" --guidance 2.5 --seed 1

# TRT inference
python -m flux kontext --loop --trt --trt_transformer_precision bf16
# precision: bf16, fp8, fp4_sdvd32
```

## Inpainting & Outpainting — Fill

```bash
# Interactive (Streamlit)
streamlit run demo_st_fill.py

# Single sample
python -m flux fill \
  --img_cond_path <path_to_input_image> \
  --img_mask_path <path_to_mask>
# Mask: same size as input, black=keep, white=regenerate
```

## Structural Conditioning — Canny / Depth

```bash
# Interactive loop
python -m flux control --name flux-dev-canny --loop
python -m flux control --name flux-dev-depth --loop
python -m flux control --name flux-dev-canny-lora --loop
python -m flux control --name flux-dev-depth-lora --loop

# TRT inference
python flux control --name=flux-dev-canny --loop \
  --img_cond_path="assets/robot.webp" \
  --trt --static_shape=False --trt_transformer_precision bf16
# precision: bf16, fp8, fp4
```

LoRA variants (`flux-dev-canny-lora`, `flux-dev-depth-lora`) automatically download the base FLUX.1 [dev] model alongside the LoRA adapter.

## Image Variation — Redux

```bash
# Interactive loop
python -m flux redux --name flux-dev --loop
python -m flux redux --name flux-schnell --loop
```

## Diffusers Integration

```bash
pip install git+https://github.com/huggingface/diffusers.git
```

```python
import torch
from diffusers import FluxPipeline

pipe = FluxPipeline.from_pretrained(
    "black-forest-labs/FLUX.1-schnell",
    torch_dtype=torch.bfloat16
)
pipe.enable_model_cpu_offload()

image = pipe(
    "A cat holding a sign that says hello world",
    output_type="pil",
    num_inference_steps=4,
    generator=torch.Generator("cpu").manual_seed(42)
).images[0]
image.save("output.png")
```

See [diffusers FLUX docs](https://huggingface.co/docs/diffusers/main/en/api/pipelines/flux) for Canny, Depth, Kontext, Fill, and Redux pipeline variants.

## Gradio & Streamlit Demos

```bash
# Streamlit (t2i + image-to-image)
streamlit run demo_st.py

# Gradio
python demo_gr.py --name flux-schnell --device cuda
python demo_gr.py --name flux-dev --share   # public link

# Options: --offload (CPU offload), --share (public URL)
```

## TRT Engine Precision Notes

| Precision | Flag | Notes |
|-----------|------|-------|
| BF16 | `--trt_transformer_precision bf16` | Best compatibility |
| FP8 | `--trt_transformer_precision fp8` | Faster, slight quality tradeoff |
| FP4 | `--trt_transformer_precision fp4` | Fastest, requires TRT FP4 support |
| FP4 (Kontext) | `--trt_transformer_precision fp4_sdvd32` | Kontext-specific FP4 variant |

ONNX height/width must be within 768–1344 pixels for TRT exports.

## Environment Variables

| Variable | Purpose |
|----------|---------|
| `BFL_API_KEY` | Black Forest Labs API key for cloud inference |
| `FLUX_MODEL` | Local path to FLUX transformer checkpoint |
| `FLUX_AE` | Local path to autoencoder checkpoint |
| `FLUX_REDUX` | Local path to Redux adapter |
| `FLUX_LORA` | Local path to LoRA adapter |
| `HF_TOKEN` | HuggingFace token for gated model downloads |
