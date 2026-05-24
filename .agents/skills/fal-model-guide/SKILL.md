---
name: fal-model-guide
description: fal.ai model selection guide for AI image generation (2026). PROACTIVELY activate for: (1) choosing between image generation models, (2) comparing model quality/speed/cost, (3) selecting models by use case (photorealism, text rendering, vector art, character consistency, editing), (4) looking up endpoint IDs, pricing, or resolution support, (5) checking recently added models. Covers: Nano Banana 2, FLUX.2 [pro], Seedream V4.5, Recraft V3/V4.1, Nano Banana Pro, Ideogram V3, GPT Image 1.5, FLUX 1.1 [pro] Ultra, Qwen Image Max, and 15+ recently added models.
license: reference
metadata:
  source: fal.ai blog — "10 Best AI Image Generators in 2026"
  author: John Ozuysal
  updated: 2026-03-05
  platform: fal.ai
compatibility: fal.ai API — use with fal-api-reference skill for integration details.
allowed-tools: Read
---

# fal.ai Model Guide — AI Image Generation (2026)

Quick reference for choosing the right image model on fal.ai. All models use the same API key and integration pattern — swap the endpoint string to switch models.

## Model Selection at a Glance

| Model | Best For | Price on fal | Endpoint |
|-------|----------|-------------|----------|
| Nano Banana 2 | Fast, vibrant, strong text + character consistency | $0.08/image (1K) | `fal-ai/nano-banana-2` |
| FLUX.2 [pro] | Photorealism, zero-config, multi-reference editing | $0.03/MP | `fal-ai/flux-pro/v2` |
| Seedream V4.5 | Photorealism + built-in editing, low cost | $0.04/image | `fal-ai/seedream/v4.5` |
| Recraft V3 | Text rendering, vector art, brand assets | $0.04 raster / $0.08 vector | `fal-ai/recraft-v3` |
| Nano Banana Pro | Semantic accuracy, character consistency, premium | $0.15/image | `fal-ai/nano-banana-pro` |
| Ideogram V3 | Posters, logos, marketing text | $0.03–$0.09/image | `fal-ai/ideogram/v3` |
| GPT Image 1.5 | Versatile, 3 quality tiers, budget drafts | $0.009–$0.133/image | `fal-ai/gpt-image-1.5` |
| FLUX 1.1 [pro] Ultra | Native 2K output, no upscaling step | $0.06/image | `fal-ai/flux/1.1-pro-ultra` |
| Qwen Image Max | Text rendering, LLM-based editing, LoRA | $0.075/image | `fal-ai/qwen-image-max` |

**Test prompt used in comparisons:**
> "A cinematic dusk scene in a floating coastal megacity carved into limestone cliffs. Bioluminescent turquoise water illuminates wet stone below. In the foreground, a weathered archivist with cybernetic eyes repairs a glowing glass memory sphere projecting holographic stars, birds, and manuscripts. Renaissance-inspired robes mixed with futuristic materials, intricate embroidery visible. Behind them: vertical gardens, neon alien signage, steam vents, and slow-moving airships in misty clouds. Lighting blends warm candlelight, cool twilight, and neon reflections; teal-and-amber color palette. Hyper-realistic digital painting, shallow depth of field, 50mm lens, soft film grain, cinematic sci-fi concept art."

---

## Decision Guide

**Need photorealism?** → FLUX.2 [pro] or Seedream V4.5
**Need text in images (logos, posters)?** → Recraft V3 or Ideogram V3
**Need vector art / SVG output?** → Recraft V3 ($0.08) or Recraft V4.1 Vector
**Need character consistency across generations?** → Nano Banana 2 or Nano Banana Pro (up to 5 people, no fine-tuning)
**Need semantic / compositional reasoning?** → Nano Banana Pro or Nano Banana 2 (Gemini backbone)
**Need native high-res (2K) without upscaling?** → FLUX 1.1 [pro] Ultra
**Need lowest cost for drafts?** → GPT Image 1.5 low tier ($0.009/image) or FLUX.1 [schnell] ($0.003/MP)
**Need multi-reference compositing (up to 9 images)?** → FLUX.2 [pro]
**Need LoRA fine-tuning?** → FLUX.2 [pro], Qwen Image Max, or Recraft V3
**Need LLM-based editing (text instructions)?** → Qwen Image Max or GPT Image 1.5

---

## Detailed Model Profiles

### Nano Banana 2 (Google Gemini 3.1 Flash Image)

**Best for:** Fast, vibrant generation with strong text rendering and character consistency at mid-range price.

**Key differentiators:**
- Reasoning-guided generation (not just keyword matching) — interprets creative intent
- Character consistency for up to 5 people across generations without fine-tuning
- Up to 14 reference images for editing workflows
- Optional web search grounding (`enable_web_search` param, +$0.015/generation)
- All outputs include SynthID digital watermarking

**Pricing:**
| Resolution | Price |
|-----------|-------|
| 512×512 | $0.06/image |
| 1K | $0.08/image |
| 2K | $0.12/image |
| 4K | $0.16/image |

**Supported aspect ratios:** 21:9, 16:9, 3:2, 4:3, 5:4, 1:1, 4:5, 3:4, 2:3, 9:16

**When NOT to use:** Highly complex compositional prompts where full reasoning depth matters → use Nano Banana Pro instead. High-volume work where cost is critical → FLUX.2 [pro] cheaper.

---

### FLUX.2 [pro] (Black Forest Labs)

**Best for:** Production teams needing consistent studio-grade output with zero configuration.

**Key differentiators:**
- Zero-configuration pipeline (no steps or guidance scale to tune)
- Multi-reference editing with up to 9 source images in one generation
- Natural language image editing (no masks or layers)
- LoRA fine-tuning via fal's training pipeline
- Launched on fal on day one; cold starts 5–10s vs 20–60s elsewhere

**Pricing:**
- $0.03 for first megapixel
- +$0.015 per additional megapixel
- 1024×1024 = $0.03; 1920×1080 ≈ $0.045

**Supported sizes:** Custom, Square HD, Square, Portrait 3:4, Portrait 9:16, Landscape 4:3, Landscape 16:9

**When NOT to use:** If raw speed is the #1 priority — not the fastest option.

---

### Seedream V4.5 (ByteDance)

**Best for:** Photorealistic output with strong prompt adherence and built-in editing in one model.

**Key differentiators:**
- Unified generation + editing architecture (no model switching)
- Consistently follows 4–5 of 6 complex prompt elements on first try
- Competitive pricing vs FLUX.2 [pro]

**Pricing:** $0.04/image at standard resolution

**Supported sizes:** Custom, Square HD, Square, Portrait 3:4, Portrait 9:16, Landscape 4:3, Landscape 16:9, Auto 2K, Auto 4K

**When NOT to use:** Auto 4K can take 30+ seconds and output large files (12 MB+). Multi-reference compositing → FLUX.2 [pro] has deeper feature set.

---

### Recraft V3

**Best for:** Designers needing accurate text rendering, vector art, and brand-consistent imagery. (#1 on Artificial Analysis Text-to-Image Arena, Oct 2024, ELO 1172)

**Key differentiators:**
- Style presets: `realistic_image`, `digital_illustration`, `vector_illustration`
- Brand color palette control via `colors` parameter
- Vector art generation (rare capability)
- Near-perfect spelling on multi-word text, brand slogans, product labels

**Pricing:**
- $0.04/image — raster styles (~25 generations per $1)
- $0.08/image — vector styles

**Supported sizes:** Square, Square HD, Portrait 4:3, Portrait 16:9, Landscape 4:3, Landscape 16:9

**When NOT to use:** Pure photorealism in portrait/product photography → FLUX.2 [pro] or Seedream.

---

### Recraft V4.1 (newer variants — recently added)

| Variant | Endpoint | Price | Notes |
|---------|----------|-------|-------|
| V4.1 | `recraft/v4.1/text-to-image` | — | Sharper prompt control, cleaner composition |
| V4.1 Pro | `recraft/v4.1/pro/text-to-image` | — | Up to 2048×2048, ultra-wide formats |
| V4.1 Vector | `recraft/v4.1/text-to-vector` | — | Editable SVG with structured layers |
| V4.1 Pro Vector | `recraft/v4.1/pro/text-to-vector` | — | Large-format SVG for poster/brand assets |
| V4.1 Utility | `recraft/v4.1/utility/text-to-image` | — | Faster/cheaper for A/B and pipelines |
| V4.1 Utility Pro | `recraft/v4.1/utility/pro/text-to-image` | — | High-res at utility speed |

---

### Nano Banana Pro (Google Gemini 3 Pro Image)

**Best for:** Creative teams needing maximum semantic accuracy, character consistency, and premium output quality.

**Key differentiators:**
- Full Gemini 3 Pro reasoning pipeline (not just Flash)
- Interprets concepts holistically (e.g., "1960s aesthetic" → grain + color palette + composition, not just a filter)
- Character consistency for up to 5 people without fine-tuning
- Multi-image blending with up to 14 reference images
- Batch processing up to 4 variations per request
- Industry-leading text rendering in multiple languages

**Pricing:**
- $0.15/image at standard (1K) resolution
- 4K = $0.30/image (2× rate)

**Supported aspect ratios:** 21:9, 16:9, 3:2, 4:3, 5:4, 1:1, 4:5, 3:4, 2:3, 9:16

**When NOT to use:** Budget-sensitive projects — 5× more expensive than FLUX.2 [pro]. Speed-sensitive pipelines (full reasoning pipeline prioritizes quality).

---

### Ideogram V3

**Best for:** Marketing materials, posters, logos, social media graphics with critical text accuracy.

**Key differentiators:**
- Near-perfect spelling accuracy on multi-word phrases in generated images
- Big quality jump from V2: better lighting, more natural compositions
- Also available on Ideogram's own platform (Plus at $20/month) — fal gives pay-per-use

**Pricing:**
| Tier | Price |
|------|-------|
| TURBO | $0.03/image |
| BALANCED | $0.06/image |
| QUALITY | $0.09/image |

**When NOT to use:** Pure photorealism → FLUX.2 [pro] or Seedream. Multi-reference compositing or LoRA → FLUX.2 [pro].

---

### GPT Image 1.5 (OpenAI)

**Best for:** Versatile generation with strong natural language prompt following; 3 quality tiers for budget control.

**Key differentiators:**
- Three quality tiers (low/medium/high) for precise cost-per-image control
- Conversational prompts work better here than models requiring structured prompt engineering
- Access through fal — no separate OpenAI account or API key needed

**Pricing:**
| Quality | 1024×1024 | 1024×1536 | 1536×1024 |
|---------|-----------|-----------|-----------|
| Low | $0.009 | $0.013 | $0.013 |
| Medium | $0.034 | $0.051 | $0.050 |
| High | $0.133 | $0.200 | $0.199 |

**When NOT to use:** LoRA fine-tuning, vector output, or multi-reference workflows → other models handle those better.

---

### FLUX 1.1 [pro] Ultra (Black Forest Labs)

**Best for:** Teams needing native 2K output without a separate upscaling step.

**Key differentiators:**
- Highest native resolution in FLUX lineup (up to 2K)
- Strong photorealism that holds up at large sizes
- Part of fal's FLUX ecosystem with LoRA support
- Same endpoint swap pattern as all FLUX models

**Pricing:** $0.06/image (flat rate)

**When NOT to use:** FLUX.2 [pro] now leads on editing versatility and zero-config quality. More expensive than most standard-resolution options.

---

### Qwen Image Max (Alibaba / Qwen series)

**Best for:** Strong text rendering and precise image editing from an LLM-based architecture at budget price.

**Key differentiators:**
- Autoregressive LLM architecture (not diffusion) → strong text + spatial reasoning
- LoRA fine-tuning support via fal's training pipeline
- Turbo mode for faster generation
- Webp output format option

**Pricing:** $0.075/image

**When NOT to use:** Pure photorealism → FLUX.2 [pro] or Seedream. Smaller community and fewer third-party resources.

---

## Recently Added Models (as of 2026-03-05)

| Model | Endpoint | Type | Notes |
|-------|----------|------|-------|
| Lyria 3 Pro | `lyria3/pro` | text-to-audio | Google's latest music model |
| FLUX Pro Erase | `flux-pro/v1/erase` | image-to-image | Remove objects/text (Black Forest Labs) |
| Marlin | `marlin` | vision | 2B video VLM — what is happening + when? |
| Marlin Find | `marlin/find` | vision | Temporal search in video |
| Nemotron Diffusion VLM | `nemotron-diffusion-vlm` | vision | 8B vision-language model (NVIDIA) |
| HeyGen Avatar V | `heygen/avatar5/digital-twin` | text-to-video | Digital twin videos with lip-sync |
| Meshy Rigging | `meshy/rigging` | 3d-to-3d | Rig humanoid 3D GLB models |
| ImagineArt 2.0 Edit | `imagineart/imagineart-2.0-edit-preview/image-to-image` | image-to-image | Prompt-guided editing at 2K |
| Mirelo SFX 1.6 (Video) | `mirelo-ai/sfx1.6/video-to-video` | video-to-video | Synced audio for video, up to 60s |
| Mirelo SFX 1.6 (Text) | `mirelo-ai/sfx1.6/text-to-audio` | text-to-audio | Ambient sounds + looping |
| Mirelo SFX 1.6 (Inpaint) | `mirelo-ai/sfx1.6/inpaint-audio` | audio-to-audio | Erase + replace audio moments |
| Mirelo SFX 1.6 (Extend) | `mirelo-ai/sfx1.6/extend-audio` | audio-to-audio | Extend sound effects |
| VEED Subtitles | `veed/subtitles` | video-to-video | Burned-in subtitles, $0.10/min |
| FLUX.2 [pro] Outpaint | `flux-2-pro/outpaint` | image-to-image | Outpainting with FLUX.2 [pro] |

---

## Pricing Summary (Image Generation)

| Model | Price | Notes |
|-------|-------|-------|
| FLUX.1 [schnell] | $0.003/MP | Fastest, lowest quality |
| FLUX.2 [dev] Turbo | ~$0.008/image | — |
| FLUX.1 [dev] | $0.025/MP | — |
| GPT Image 1.5 (low) | $0.009/image | Draft quality |
| Ideogram V3 Turbo | $0.03/image | — |
| FLUX.2 [pro] | $0.03/MP | ~$0.03 per 1024×1024 |
| Seedream V4.5 | $0.04/image | — |
| Recraft V3 raster | $0.04/image | — |
| Recraft V3 vector | $0.08/image | — |
| Ideogram V3 Balanced | $0.06/image | — |
| Nano Banana 2 (1K) | $0.08/image | — |
| FLUX 1.1 [pro] Ultra | $0.06/image | Native 2K |
| Ideogram V3 Quality | $0.09/image | — |
| Qwen Image Max | $0.075/image | — |
| Nano Banana Pro | $0.15/image | Premium |

Platform base: $0.003/megapixel. No subscriptions, no GPU management, no idle costs.

---

## Common Parameters Across Models

```typescript
// All fal.ai image models share this basic pattern:
const result = await fal.subscribe("fal-ai/flux-pro/v2", {
  input: {
    prompt: "...",
    image_size: "landscape_16_9",  // or { width: 1920, height: 1080 }
    num_images: 1,
    seed: 42,                       // for reproducibility
  }
});

console.log(result.data.images[0].url);
```

See `fal-api-reference` skill for full method signatures, queue management, webhooks, and file upload.
