---
name: bfl-flux2
description: Black Forest Labs FLUX.2 — nächste Generation Bildgenerierung und -bearbeitung. Umfasst FLUX.2 [dev] (32B, Maximalqualität) und die FLUX.2 [klein] Familie (4B/9B, sub-sekunden Inferenz auf Consumer-GPUs). Alle Modelle unterstützen Text-to-Image, Single-Reference- und Multi-Reference-Bildbearbeitung über CLI, diffusers-Integration oder BFL-API. Nutze diesen Skill für Bildgenerierung, interaktive Bildbearbeitung mit mehreren Referenzbildern, Prompt-Upsampling und KV-Cache-beschleunigte Inferenz.
license: Apache-2.0 (4B-Modelle); FLUX Non-Commercial License (9B- und dev-Modelle)
metadata:
  author: Black Forest Labs (bfl.ai)
  source: https://github.com/black-forest-labs/flux2
compatibility: Claude Code, any AI coding agent
allowed-tools: Bash, Read, Write, Edit
---

# FLUX.2 — Black Forest Labs

Frontier-Bildgenerierung und -bearbeitung. Alle Modelle unterstützen Text-to-Image (T2I), Single-Reference-Editing und Multi-Reference-Editing in einem einzigen Modell.

## Modellübersicht

| Modell | Params | Distilled | VRAM | Lizenz | Stärke |
|--------|--------|-----------|------|--------|--------|
| FLUX.2 [klein] 4B | 4B | ✅ (4 Steps) | ~8 GB | Apache-2.0 | Echtzeit, Consumer-GPU |
| FLUX.2 [klein] 9B | 9B | ✅ | — | Non-Commercial | Hohe Qualität |
| FLUX.2 [klein] 9B KV | 9B | ✅ | — | Non-Commercial | Multi-Ref-Editing mit KV-Cache |
| FLUX.2 [klein] 4B Base | 4B | ❌ (50 Steps) | ~8 GB | Apache-2.0 | Fine-Tuning / LoRA |
| FLUX.2 [klein] 9B Base | 9B | ❌ | — | Non-Commercial | Forschung / LoRA-Training |
| FLUX.2 [dev] | 32B | ❌ | 80 GB+ | Non-Commercial | Maximale Qualität |

**HuggingFace-Repos:** `black-forest-labs/FLUX.2-klein-4B`, `FLUX.2-klein-9B`, `FLUX.2-klein-9b-kv`, `FLUX.2-klein-base-4B`, `FLUX.2-klein-base-9B`, `FLUX.2-dev`

**Welches Modell wählen?**
- Echtzeit / Consumer-GPU → **klein 4B** (~8 GB VRAM)
- Bestes Qualität/Latenz-Verhältnis bei Multi-Ref-Editing → **klein 9B KV**
- Fine-Tuning auf begrenzter Hardware → **klein 4B Base**
- Maximale Qualität ohne Latenzbeschränkung → **FLUX.2 [dev]**

## Installation

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -e . --extra-index-url https://download.pytorch.org/whl/cu129 --no-cache-dir
```

Getestet auf GB200, CUDA 12.9, Python 3.12.

## Environment Variables

```bash
export FLUX2_MODEL_PATH="<pfad/zu/flux2-dev>"
export AE_MODEL_PATH="<pfad/zu/ae.safetensors>"
export KLEIN_4B_MODEL_PATH="<pfad/zu/klein-4b>"
export KLEIN_4B_BASE_MODEL_PATH="<pfad/zu/klein-4b-base>"
export KLEIN_9B_MODEL_PATH="<pfad/zu/klein-9b>"
export KLEIN_9B_KV_MODEL_PATH="<pfad/zu/klein-9b-kv>"
export KLEIN_9B_BASE_MODEL_PATH="<pfad/zu/klein-9b-base>"
```

Nicht gesetzt → Gewichte werden automatisch von HuggingFace heruntergeladen.

## CLI-Nutzung

```bash
# Interaktive Session (T2I + Bildbearbeitung)
PYTHONPATH=src python scripts/cli.py

# Bestimmtes Modell wählen
PYTHONPATH=src python scripts/cli.py --model_name flux.2-klein-4b
PYTHONPATH=src python scripts/cli.py --model_name flux.2-klein-9b
PYTHONPATH=src python scripts/cli.py --model_name flux.2-klein-9b-kv
PYTHONPATH=src python scripts/cli.py --model_name flux.2-dev
```

Interaktiv Bilder bearbeiten:
```
> input_images="ref1.jpg,ref2.jpg"
> prompt="a cat wearing sunglasses"
> run
```

## Prompt-Upsampling

Verbessert Ergebnisse deutlich bei komplexen Prompts (Text in Bildern, bildbasierte Anweisungen, Code/Mathe-Visualisierungen).

### API-basiert via OpenRouter (empfohlen)

```bash
export OPENROUTER_API_KEY="<api_key>"
PYTHONPATH=src python scripts/cli.py --upsample_prompt_mode=openrouter
# Modell wechseln:
PYTHONPATH=src python scripts/cli.py --upsample_prompt_mode=openrouter --openrouter_model=<modell>
```

### Lokal via Mistral-Small-3.2-24B

```bash
PYTHONPATH=src python scripts/cli.py --upsample_prompt_mode=local
# Kein API-Key nötig; nutzt dasselbe Mistral-Modell wie FLUX.2 [dev] für Text-Encoding
```

Für einfache direkte Prompts bringt Upsampling keinen großen Vorteil.

## KV-Cache (klein 9B KV)

Optimiert für Multi-Referenz-Editing durch Caching der Referenztoken-Attention (nur einmalig berechnet):

| #Referenzen (je 1024×1024) | 512×512 | 768×768 | 1024×1024 |
|:-:|:-:|:-:|:-:|
| 1 Ref | 1,78× | 1,57× | 1,40× |
| 2 Refs | 2,16× | 1,97× | 1,77× |
| 4 Refs | 2,66× | 2,44× | 2,22× |

```bash
export KLEIN_9B_KV_MODEL_PATH="/pfad/zum/modell.safetensors"
PYTHONPATH=src python scripts/cli.py --model_name flux.2-klein-9b-kv
```

## diffusers-Integration

```bash
pip install git+https://github.com/huggingface/diffusers.git
pip install --upgrade transformers accelerate bitsandbytes
hf auth login  # für FLUX.2-dev (gated)
```

### RTX 4090 (~18 GB VRAM) — 4-Bit + Remote Text-Encoder

```python
import torch, requests, io
from diffusers import Flux2Pipeline
from huggingface_hub import get_token

repo_id = "diffusers/FLUX.2-dev-bnb-4bit"

def remote_text_encoder(prompts):
    r = requests.post(
        "https://remote-text-encoder-flux-2.huggingface.co/predict",
        json={"prompt": prompts},
        headers={"Authorization": f"Bearer {get_token()}", "Content-Type": "application/json"}
    )
    return torch.load(io.BytesIO(r.content)).to("cuda:0")

pipe = Flux2Pipeline.from_pretrained(repo_id, text_encoder=None, torch_dtype=torch.bfloat16).to("cuda:0")
image = pipe(
    prompt_embeds=remote_text_encoder("your prompt here"),
    generator=torch.Generator("cuda:0").manual_seed(42),
    num_inference_steps=50,
    guidance_scale=4,
).images[0]
image.save("output.png")
```

### RTX 4090 (~20 GB VRAM) — vollständig 4-Bit quantisiert

```python
import torch
from diffusers import Flux2Pipeline, AutoModel
from transformers import Mistral3ForConditionalGeneration

repo_id = "diffusers/FLUX.2-dev-bnb-4bit"
text_encoder = Mistral3ForConditionalGeneration.from_pretrained(
    repo_id, subfolder="text_encoder", torch_dtype=torch.bfloat16, device_map="cpu"
)
dit = AutoModel.from_pretrained(
    repo_id, subfolder="transformer", torch_dtype=torch.bfloat16, device_map="cpu"
)
pipe = Flux2Pipeline.from_pretrained(repo_id, text_encoder=text_encoder, transformer=dit, torch_dtype=torch.bfloat16)
pipe.enable_model_cpu_offload()
image = pipe(prompt="your prompt", num_inference_steps=50, guidance_scale=4).images[0]
image.save("output.png")
```

### H100 / 80 GB+ VRAM

```python
import torch
from diffusers import Flux2Pipeline

pipe = Flux2Pipeline.from_pretrained("black-forest-labs/FLUX.2-dev", torch_dtype=torch.bfloat16)
pipe.enable_model_cpu_offload()  # bei H200/B200 stattdessen .to("cuda")
image = pipe(prompt="your prompt", num_inference_steps=50, guidance_scale=4).images[0]
image.save("output.png")
```

Multi-Referenz-Bildbearbeitung mit diffusers:
```python
image = pipe(
    prompt="a cat wearing sunglasses",
    image=[ref_image1, ref_image2],  # Liste von Referenzbildern
    num_inference_steps=50,
    guidance_scale=4,
).images[0]
```

## Autoencoder

FLUX.2 verfügt über einen deutlich verbesserten Autoencoder gegenüber FLUX.1.
- HF: `black-forest-labs/FLUX.2-dev` → `ae.safetensors`
- Lizenz: Apache-2.0
