---
name: fal-optimization
description: Performance optimization guide for fal.ai deployments. PROACTIVELY activate for: (1) reducing cold start times, (2) keep_alive and concurrency tuning, (3) GPU selection for cost/speed tradeoffs, (4) PyTorch Inductor compilation cache (torch.compile), (5) model weight caching with persistent storage, (6) warm worker strategies, (7) setup_function vs @fal.cached patterns, (8) request timeout configuration, (9) scaling parameters (min_concurrency, concurrency_buffer). Source: fal-ai/fal repo toolkit/compilation.py + api.py.
license: MIT
metadata:
  source: https://github.com/fal-ai/fal (projects/fal)
  package: pip install fal
compatibility: Python 3.8+. GPU optimization requires NVIDIA GPU machine_type.
allowed-tools: Read Write Edit
---

# fal Optimization Guide

Performance patterns for fast, cost-efficient fal.ai serverless deployments.

---

## Cold Start Reduction

### 1. keep_alive — Keep Workers Warm

The single most impactful setting. Workers stay alive N seconds after last request.

```python
@fal.function(
    machine_type="GPU-T4",
    requirements=["torch", "diffusers"],
    keep_alive=300,   # 5 minutes — good for low-frequency apps
    # keep_alive=60,  # 1 minute — for moderate traffic
    # keep_alive=10,  # Default — minimal idle cost
)
def generate(prompt: str) -> dict: ...
```

**Rule of thumb:**
- Low traffic (< 1 req/min): `keep_alive=300`
- Moderate traffic (1–10 req/min): `keep_alive=60`
- High traffic (> 10 req/min): use `min_concurrency` instead

### 2. min_concurrency — Always-On Workers

Keep N workers running at all times. Eliminates cold starts completely for guaranteed capacity.

```python
@fal.function(
    machine_type="GPU-T4",
    keep_alive=60,
    min_concurrency=1,    # Always have 1 warm worker ready
    max_concurrency=10,   # Scale up to 10 under load
    concurrency_buffer=2, # Pre-warm 2 extra workers when approaching limit
)
def generate(prompt: str) -> dict: ...
```

**Cost:** `min_concurrency` workers run 24/7 — factor this into pricing.

### 3. concurrency_buffer — Pre-warm on Traffic Spike

```python
@fal.function(
    machine_type="GPU-T4",
    max_concurrency=10,
    concurrency_buffer=3,       # Start warming 3 workers before hitting limit
    concurrency_buffer_perc=30, # Alternative: 30% of max_concurrency
)
def generate(prompt: str) -> dict: ...
```

---

## Model Loading Optimization

### setup_function — Load Once Per Worker

```python
import fal

_model = None

def load_models():
    """Runs once at worker startup, not per request."""
    global _model
    import torch
    from diffusers import StableDiffusionXLPipeline

    _model = StableDiffusionXLPipeline.from_pretrained(
        "stabilityai/stable-diffusion-xl-base-1.0",
        torch_dtype=torch.float16,
        use_safetensors=True,
    ).to("cuda")
    _model.unet = torch.compile(_model.unet, mode="reduce-overhead", fullgraph=True)
    # Run warmup to trigger compilation
    _model("warmup", num_inference_steps=1)

@fal.function(
    machine_type="GPU-A10G",
    requirements=["torch", "diffusers", "transformers", "accelerate"],
    setup_function=load_models,
    keep_alive=600,  # Long keep_alive to amortize loading cost
)
def generate(prompt: str, steps: int = 20) -> dict:
    images = _model(prompt, num_inference_steps=steps).images
    return {"url": fal.toolkit.Image.from_pil(images[0]).url}
```

### @fal.cached — Lazy Load with Caching

Use when you want to defer loading until first request (simpler pattern):

```python
import fal

@fal.cached
def get_pipeline():
    import torch
    from diffusers import StableDiffusionPipeline
    pipe = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5",
        torch_dtype=torch.float16,
    ).to("cuda")
    return pipe

@fal.function(machine_type="GPU-T4", requirements=["torch", "diffusers"])
def generate(prompt: str) -> str:
    pipe = get_pipeline()  # Cached after first call on this worker
    return fal.toolkit.Image.from_pil(pipe(prompt).images[0]).url
```

**setup_function vs @fal.cached:**
- `setup_function` → runs at worker startup, before any request arrives
- `@fal.cached` → runs on first request, result cached for worker lifetime
- Prefer `setup_function` when you want the worker ready before the first request

---

## PyTorch Inductor Cache (torch.compile)

`torch.compile()` generates optimized CUDA kernels on first run (20–30 seconds). Share compiled kernels across workers via persistent storage to cut startup to ~2 seconds.

### Manual cache management

```python
from fal.toolkit import load_inductor_cache, sync_inductor_cache

def setup():
    import torch
    from diffusers import StableDiffusionXLPipeline

    # 1. Load compiled kernels from /data cache (GPU-specific)
    dir_hash = load_inductor_cache("sdxl/v1")

    pipe = StableDiffusionXLPipeline.from_pretrained(...).to("cuda")
    pipe.unet = torch.compile(pipe.unet, mode="reduce-overhead", fullgraph=True)

    # 2. Warmup — triggers compilation (fast if cache was loaded)
    pipe("warmup", num_inference_steps=1)

    # 3. Sync updated cache back to persistent storage
    sync_inductor_cache("sdxl/v1", dir_hash)

    return pipe
```

### Context manager (automatic)

```python
from fal.toolkit import synchronized_inductor_cache

def setup():
    import torch

    with synchronized_inductor_cache("mymodel/v1"):
        pipe = load_my_model()
        pipe.unet = torch.compile(pipe.unet, mode="reduce-overhead")
        pipe("warmup", num_inference_steps=1)
    # Cache auto-synced on exit
    return pipe
```

### How it works

| Location | Path | Purpose |
|----------|------|---------|
| Local cache | `/tmp/inductor-cache/` | Active CUDA kernels for current worker |
| Global cache | `/data/inductor-caches/<GPU_TYPE>/<cache_key>.zip` | Shared across workers |
| Persistent temp | `/data/tmp/` | Temp dir for zip operations |

Cache is GPU-type-specific (H100 cache ≠ A100 cache). `get_gpu_type()` detects the GPU automatically.

```python
from fal.toolkit import get_gpu_type
gpu = get_gpu_type()  # "H100", "A100", "T4", etc.
```

---

## Persistent Model Weight Storage

Avoid re-downloading model weights on every cold start:

```python
from fal.toolkit import FAL_MODEL_WEIGHTS_DIR, FAL_PERSISTENT_DIR, download_model_weights

WEIGHTS_PATH = FAL_MODEL_WEIGHTS_DIR / "my-sdxl"  # /data/.fal/model_weights/my-sdxl

@fal.cached
def get_model():
    import torch
    from diffusers import StableDiffusionXLPipeline

    if not WEIGHTS_PATH.exists():
        # First worker: download and cache to /data
        download_model_weights(
            "https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0",
            str(WEIGHTS_PATH),
        )

    return StableDiffusionXLPipeline.from_pretrained(
        str(WEIGHTS_PATH),
        torch_dtype=torch.float16,
    ).to("cuda")
```

**Persistent directories (survive cold starts, shared across workers on same account):**
- `/data` → `FAL_PERSISTENT_DIR`
- `/data/.fal/model_weights/` → `FAL_MODEL_WEIGHTS_DIR`
- `/data/.fal/repos/` → `FAL_REPOSITORY_DIR`

---

## GPU Selection Guide

| GPU | VRAM | Best For | Relative Cost |
|-----|------|---------|---------------|
| `GPU-T4` | 16 GB | SDXL, ViTs, 7B LLMs (float16) | $ |
| `GPU-A10G` | 24 GB | SDXL + ControlNet, 13B LLMs | $$ |
| `GPU-A100` | 80 GB | Large diffusion models, 30–70B LLMs | $$$$ |
| `GPU-H100` | 80 GB | Fastest inference, training | $$$$$ |

**Practical rules:**
- Start with `GPU-T4` — cheapest, covers most inference use cases
- Move to `GPU-A10G` when you hit VRAM limits with float16 models
- `GPU-A100` / `GPU-H100` for 30B+ LLMs, video models, or training runs
- Use `num_gpus=2` for multi-GPU tensor parallelism (A100/H100)

**Float precision tradeoffs:**
```python
# float16 — 2× memory reduction, ~1% quality loss, 30-50% faster
pipe = pipe.to(torch.float16)

# bfloat16 — better numerical stability than float16
pipe = pipe.to(torch.bfloat16)

# float8 (requires GPU with float8 support: H100)
# Use transformers' load_in_8bit=True for LLMs
```

---

## Concurrency Tuning

### max_multiplexing — Multiple Requests Per Worker

Allow one worker to handle N requests simultaneously (only for I/O-bound work):

```python
@fal.function(
    machine_type="S",
    max_multiplexing=4,    # 1 worker handles 4 concurrent requests
    max_concurrency=100,
)
def fetch_data(url: str) -> dict: ...  # I/O bound — safe to multiplex
```

**Do NOT multiplex GPU inference** — GPU ops are sequential; multiplexing adds latency without benefit.

### Scaling for burst traffic

```python
@fal.function(
    machine_type="GPU-T4",
    keep_alive=120,
    min_concurrency=2,        # Always 2 warm
    max_concurrency=50,       # Scale to 50 under load
    concurrency_buffer=5,     # Pre-warm 5 when approaching limit
    scaling_delay=30,         # Wait 30s before scaling down idle workers
)
def generate(prompt: str) -> dict: ...
```

---

## Timeout Configuration

```python
@fal.function(
    machine_type="GPU-A100",
    request_timeout=600,      # Max 10 minutes per request
    startup_timeout=900,      # Max 15 minutes for cold start (large models)
)
def train(data: dict) -> dict: ...
```

**Defaults:** `request_timeout=None` (no limit), `startup_timeout=600` (10 min)

---

## Cost Optimization Checklist

1. **Right-size the machine** — start with `GPU-T4`, only upgrade if VRAM limited
2. **Use float16** — halves VRAM usage, negligible quality loss for inference
3. **Set keep_alive appropriately** — don't pay for idle time on rarely-used endpoints
4. **Cache model weights in `/data`** — avoid re-downloading on every cold start
5. **Use inductor cache** — cuts `torch.compile()` startup from 30s → 2s
6. **Batch requests when possible** — process multiple inputs per GPU call
7. **Use `min_concurrency=0`** unless you need zero cold starts
8. **Profile first** — measure actual bottlenecks before optimizing

---

## Debugging Performance

```python
from fal.toolkit import get_gpu_type
import time

@fal.function(machine_type="GPU-T4", requirements=["torch"])
def benchmark() -> dict:
    gpu = get_gpu_type()
    t0 = time.time()
    import torch
    x = torch.randn(1000, 1000).cuda()
    y = x @ x.T
    elapsed = time.time() - t0
    return {"gpu": gpu, "matmul_ms": elapsed * 1000}
```

See `fal-serverless-guide` skill for full deployment reference.
See `fal-api-reference` skill for calling deployed endpoints.
