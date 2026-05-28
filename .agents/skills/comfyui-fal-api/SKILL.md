---
name: comfyui-fal-api
description: Install and use ComfyUI custom nodes for fal.ai API — image generation (Flux Pro/Dev/Schnell/Ultra, NanoBanana, Recraft, Ideogram, Imagen4, Wan, Seedream), video generation (Kling v1–v3/O3, Veo2/3, Wan 2.x, Runway, Luma, Sora, Seedance), LLMs, VLMs, LoRA trainers, and video upscalers. All via a single FAL_KEY.
license: MIT
metadata:
  author: gokayfem
  version: "1.0.12"
  source: https://github.com/gokayfem/ComfyUI-fal-API
  comfy_registry: https://registry.comfy.org/publishers/gokayfem/nodes/fal-api
compatibility: ComfyUI with Python 3.9+. Requires FAL_KEY from fal.ai.
allowed-tools: Bash(pip:*) Bash(git:*) Read Write
---

# ComfyUI fal API Nodes

Custom nodes for using fal.ai models directly in ComfyUI — one API key for everything.

## Installation (in ComfyUI)

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/gokayfem/ComfyUI-fal-API.git
# or use the plugin source:
cp -r .agents/plugins/comfyui-fal-api ComfyUI/custom_nodes/ComfyUI-fal-API

cd ComfyUI/custom_nodes/ComfyUI-fal-API
pip install -r requirements.txt
```

## Configuration

**Option A — config.ini:**
```ini
[API]
FAL_KEY = your_actual_fal_api_key
```

**Option B — environment variable:**
```bash
export FAL_KEY=your_actual_fal_api_key
```

Get your key at: https://fal.ai/dashboard/keys

Restart ComfyUI after setup. Nodes appear under the **FAL** category in the node browser.

## Available Nodes

### Image Generation
| Node | Model | Notes |
|------|-------|-------|
| Flux Pro (fal) | fal-ai/flux-pro | High quality, commercial |
| Flux Dev (fal) | fal-ai/flux/dev | Open weights |
| Flux Schnell (fal) | fal-ai/flux/schnell | Fast, 4 steps |
| Flux Pro 1.1 (fal) | fal-ai/flux-pro/v1.1 | Improved pro |
| Flux Pro 1.1 Fill | fal-ai/flux-pro/v1.1-ultra/inpainting | Inpainting |
| Flux Ultra | fal-ai/flux-pro/v1.1-ultra | Max quality |
| Flux LoRA | fal-ai/flux-lora | Custom LoRA |
| Flux General | fal-ai/flux-general | General purpose |
| Flux Kontext | fal-ai/flux-pro/kontext | Context editing |
| Flux Kontext Multi | fal-ai/flux-pro/kontext/multi | Multi-image context |
| NanoBanana Pro | fal-ai/nano-banana-pro | Character consistency |
| NanoBanana 2 | fal-ai/nano-banana-2 | Character v2 |
| Recraft | fal-ai/recraft-v3 | Vector/design |
| Ideogram v3 | fal-ai/ideogram/v3 | Text in images |
| HiDream Full | fal-ai/hidream-i1-full | High detail |
| Sana | fal-ai/sana | Efficient generation |
| Imagen4 Preview | fal-ai/imagen4/preview | Google Imagen4 |
| Qwen Image Edit | fal-ai/qwen2-vl/image-edit | Edit via VLM |
| SeedEdit v3 | fal-ai/seededit-v3 | Seed-based edit |
| Seedream v4 Edit | fal-ai/seedream-v4/edit | Edit |
| Reve Text-to-Image | fal-ai/reve/text-to-image | Reve model |

### Video Generation
| Node | Model |
|------|-------|
| Kling 2.1 Pro Image-to-Video | fal-ai/kling-video/v2.1/pro/image-to-video |
| Kling 2.5 Turbo Pro | fal-ai/kling-video/v2.5/turbo/image-to-video |
| Kling 2.6 Pro | fal-ai/kling-video/v2.6/pro/image-to-video |
| Kling v3 Standard/Pro Video | fal-ai/kling-video/v3/... |
| Kling v3 Motion Control | fal-ai/kling-video/v3/.../motion-control |
| Kling O3 Standard/Pro | fal-ai/kling-video/o3/... |
| Kling Omni (reference, edit, video-to-video) | fal-ai/kling-video/omni/... |
| Veo 2 Image-to-Video | fal-ai/veo2/image-to-video |
| Veo 3 | fal-ai/veo3 |
| Veo 3.1 First-Last Frame | fal-ai/veo3.1/first-last-frame |
| Wan Pro | fal-ai/wan-pro |
| Wan 2.5 | fal-ai/wan2.5 |
| Wan 2.6 | fal-ai/wan2.6/... |
| Wan VACE Edit | fal-ai/wan/vace |
| Wan 2.2 Animate Replace/Move | fal-ai/wan22/... |
| Runway Gen3 | fal-ai/runway-gen3/turbo/image-to-video |
| Luma Dream Machine | fal-ai/luma-dream-machine |
| Sora 2 Pro | fal-ai/sora2/pro/image-to-video |
| Seedance Image/Text-to-Video | fal-ai/seedance/... |
| Seedance Pro | fal-ai/seedance-pro/... |
| InfinityStar Text-to-Video | fal-ai/infinity-star |

### Video Upscaling / Enhancement
| Node | Notes |
|------|-------|
| Seedvr Upscaler | Video super-resolution |
| Seedvr Upscale Video | Full video pipeline |
| Bria Video Increase Resolution | Bria upscale |
| Topaz Upscale Video | Topaz AI upscale |
| Video Upscaler (combined) | General purpose |
| DY-Wan Upscaler | DY Wan model |

### LoRA Trainers
- Flux LoRA Trainer
- HunyuanVideo LoRA Trainer
- Wan LoRA Trainer
- LTX-Video LoRA Trainer

### LLM / VLM
- LLM Node (OpenAI, Claude, Llama, Gemini via fal)
- VLM Node (vision language models)

### Utilities
- Upload Video / File nodes
- Load Video from URL
- Combined Video Generation (multi-model)
- Pixverse Swap

## Example Workflows

Pre-built JSON workflows in `example_workflows/`:
- `Flux-Kontext-Workflow.json` — Flux Kontext context editing
- `Flux-v1-Fill.json` — Flux inpainting fill
- `Nano-Banana-Pro-14_Images.json` — 14 parallel NanoBanana images
- `Video-Bria-Increase-Resolution.json` — Bria video upscale
- `Video-Seedvr-Upscale.json` — Seedvr upscale pipeline
- `Video-Workflow-Veo2.json` — Veo2 image-to-video

## Workflow Tips

- All nodes accept image tensors directly from ComfyUI's standard nodes
- Images are auto-uploaded to fal CDN before API calls
- Multiple image inputs batch-submit concurrently for speed
- Seed parameter available for reproducibility
- Output is a standard ComfyUI image/video tensor
