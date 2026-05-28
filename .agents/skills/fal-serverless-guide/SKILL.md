---
name: fal-serverless-guide
description: Guide for deploying custom Python code to fal.ai serverless. PROACTIVELY activate for: (1) @fal.function decorator usage, (2) fal.App class with @fal.endpoint / @fal.realtime, (3) machine type selection (XS/S/M/L/XL/GPU), (4) environment setup (virtualenv/conda/container), (5) concurrency and scaling parameters, (6) setup_function for model loading, (7) fal toolkit usage (Image/Audio/Video/File/KV), (8) ContainerImage with Dockerfile, (9) secrets management, (10) fal CLI (run/deploy/auth/keys). Source: fal-ai/fal repo projects/fal/.
license: MIT
metadata:
  source: https://github.com/fal-ai/fal (projects/fal)
  package: pip install fal
compatibility: Python 3.8+. Requires FAL_KEY or `fal auth login`.
allowed-tools: Bash(pip:*) Bash(pip3:*) Bash(fal:*) Read Write Edit
---

# fal Serverless Guide

Deploy Python functions and ML apps to fal.ai serverless GPU/CPU infrastructure.

```bash
pip install fal
export FAL_KEY=your_key   # or: fal auth login
```

---

## @fal.function — Serverless Function Decorator

Run any Python function on fal.ai cloud hardware.

```python
import fal

@fal.function(
    machine_type="GPU-T4",          # Machine to run on
    requirements=["torch", "transformers"],  # pip packages
    keep_alive=300,                 # Seconds to stay warm after last request
)
def generate(prompt: str) -> dict:
    import torch
    # runs on fal GPU
    return {"result": prompt}

# Call it (blocks until done)
result = generate("hello world")

# Run locally for testing
generate.local("hello world")
```

### Full @fal.function signature

```python
@fal.function(
    # Environment kind
    kind="virtualenv",              # "virtualenv" (default) | "conda"

    # Environment
    python_version="3.11",          # Optional Python version
    requirements=["torch==2.1.0"],  # pip packages
    # For conda:
    # packages=["numpy"], pip=["torch"], channels=["conda-forge"]

    # Machine
    machine_type="GPU-T4",          # See machine types below
    num_gpus=1,                     # Number of GPUs (default: 1)
    regions=["us-east-1"],          # Optional region preference

    # Scaling
    keep_alive=60,                  # Seconds to keep worker warm (default: 10)
    max_concurrency=10,             # Max simultaneous requests (default: unlimited)
    min_concurrency=0,              # Min warm workers (default: 0)
    concurrency_buffer=2,           # Extra workers to pre-warm
    concurrency_buffer_perc=20,     # Alternative: buffer as percentage
    max_multiplexing=1,             # Requests per worker (default: 1)

    # Timeouts
    request_timeout=300,            # Seconds per request (default: no limit)
    startup_timeout=600,            # Seconds for cold start (default: 600)
    scaling_delay=None,             # Seconds before scaling down

    # Advanced
    setup_function=None,            # Called once at startup (model loading)
    serve=False,                    # Expose as HTTP endpoint
    exposed_port=8080,              # Port when serve=True
    force_env_build=False,          # Rebuild environment even if cached
    local_python_modules=[],        # Local modules to sync to worker
)
def my_function(x: int) -> int:
    return x * 2
```

### Machine Types

| Type | Hardware | Use Case |
|------|----------|---------|
| `XS` | CPU only | Light processing, scripting (default) |
| `S` | CPU | Standard compute |
| `M` | CPU | Medium compute |
| `L` | CPU | Heavy compute |
| `XL` | CPU | Very heavy compute |
| `GPU-T4` | NVIDIA T4 (16 GB) | Standard inference, fine-tuning |
| `GPU-A10G` | NVIDIA A10G (24 GB) | Mid-range GPU work |
| `GPU-A100` | NVIDIA A100 (80 GB) | Large models, training |
| `GPU-H100` | NVIDIA H100 (80 GB) | Cutting-edge inference |

Multi-GPU (list form):
```python
@fal.function(machine_type=["GPU-A100", "GPU-A100"])  # 2× A100
```

---

## fal.App — Multi-Endpoint App Class

Build structured apps with multiple HTTP endpoints.

```python
import fal
from pydantic import BaseModel

class Input(BaseModel):
    prompt: str
    num_steps: int = 28

class Output(BaseModel):
    image_url: str
    seed: int

class MyApp(fal.App, name="my-image-app"):
    machine_type = "GPU-T4"
    requirements = ["torch", "diffusers", "transformers", "accelerate"]
    keep_alive = 300

    def setup(self):
        """Called once at startup — load models here."""
        from diffusers import StableDiffusionPipeline
        self.pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
        self.pipe.to("cuda")

    @fal.endpoint("/")
    def generate(self, input: Input) -> Output:
        image = self.pipe(input.prompt, num_inference_steps=input.num_steps).images[0]
        url = fal.toolkit.Image.from_pil(image).url
        return Output(image_url=url, seed=42)

    @fal.endpoint("/health")
    def health(self) -> dict:
        return {"status": "ok"}
```

```bash
fal run my_app.py::MyApp          # Test (temporary URL)
fal deploy my_app.py::MyApp       # Deploy to production
```

---

## @fal.realtime — WebSocket Endpoint

```python
import fal
from pydantic import BaseModel

class Input(BaseModel):
    prompt: str

class Output(BaseModel):
    image_url: str

class RealtimeApp(fal.App, name="realtime-demo"):
    machine_type = "GPU-T4"
    requirements = ["torch", "diffusers"]

    def setup(self):
        from diffusers import LCMPipeline
        self.pipe = LCMPipeline.from_pretrained("SimianLuo/LCM_Dreamshaper_v7")
        self.pipe.to("cuda")

    @fal.realtime("/ws")
    def generate(self, input: Input) -> Output:
        image = self.pipe(input.prompt, num_inference_steps=4).images[0]
        url = fal.toolkit.Image.from_pil(image).url
        return Output(image_url=url)
```

Client-side (JS):
```typescript
const connection = fal.realtime.connect("your-username/realtime-demo", {
    onResult: (result) => console.log(result.image_url),
});
connection.send({ prompt: "a cat" });
```

---

## @fal.cached — In-Memory Cache

Cache expensive computations within a worker (survives across requests while worker is warm):

```python
import fal

@fal.cached
def load_model():
    import torch
    from transformers import AutoModelForCausalLM
    return AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-v0.1")

@fal.function(machine_type="GPU-A10G", requirements=["torch", "transformers"])
def generate(prompt: str) -> str:
    model = load_model()  # Only runs once per worker lifetime
    return model.generate(prompt)
```

---

## setup_function — Startup Initialization

Run code once per worker before serving requests:

```python
import fal

loaded_model = None

def load_pipeline():
    global loaded_model
    from diffusers import StableDiffusionPipeline
    loaded_model = StableDiffusionPipeline.from_pretrained(...)
    loaded_model.to("cuda")

@fal.function(
    machine_type="GPU-T4",
    requirements=["torch", "diffusers"],
    setup_function=load_pipeline,   # Called once at startup
    keep_alive=300,                 # Keep warm to amortize startup cost
)
def generate(prompt: str) -> str:
    return loaded_model(prompt).images[0]
```

---

## Environment Kinds

### virtualenv (default)

```python
@fal.function(
    kind="virtualenv",
    python_version="3.11",
    requirements=["torch==2.1.0", "transformers>=4.35"],
)
def run(): ...
```

### conda

```python
@fal.function(
    kind="conda",
    python_version="3.10",
    packages=["numpy", "scipy"],         # conda packages
    pip=["torch", "transformers"],       # pip packages inside conda env
    channels=["conda-forge", "pytorch"],
)
def run(): ...
```

### ContainerImage (custom Dockerfile)

```python
import fal
from fal import ContainerImage

@fal.function(
    machine_type="GPU-A100",
    image=ContainerImage.from_dockerfile_str("""
        FROM nvidia/cuda:12.1.0-runtime-ubuntu22.04
        RUN apt-get update && apt-get install -y python3 python3-pip
        RUN pip install torch transformers diffusers accelerate
    """),
)
def run(): ...
```

---

## fal Toolkit

### Image

```python
from fal.toolkit import Image
from PIL import Image as PILImage

class Output(BaseModel):
    image: Image   # Automatically uploaded to fal CDN

@fal.endpoint("/")
def generate(self, input: Input) -> Output:
    pil_img: PILImage.Image = self.pipe(input.prompt).images[0]
    return Output(image=Image.from_pil(pil_img))

# Or from URL:
img = Image(url="https://example.com/photo.jpg")
```

### File

```python
from fal.toolkit import File

class Output(BaseModel):
    file: File

@fal.endpoint("/convert")
def convert(self, input: Input) -> Output:
    with open("/tmp/output.pdf", "wb") as f:
        f.write(b"...")
    return Output(file=File.from_path("/tmp/output.pdf", content_type="application/pdf"))
```

### Audio / Video

```python
from fal.toolkit import Audio, Video

class Output(BaseModel):
    audio: Audio
    video: Video
```

### KVStore — Persistent Key-Value Store

```python
from fal.toolkit import KVStore

kv = KVStore("my-app-cache")

@fal.endpoint("/")
def handler(self, input: Input) -> Output:
    cached = kv.get(input.prompt)
    if cached:
        return Output(result=cached)
    result = expensive_operation(input.prompt)
    kv.set(input.prompt, result)
    return Output(result=result)
```

### Persistent Storage

```python
from fal.toolkit import FAL_MODEL_WEIGHTS_DIR, FAL_PERSISTENT_DIR, download_model_weights, clone_repository

# /data — persists across requests on the same worker
weights_dir = FAL_MODEL_WEIGHTS_DIR / "my-model"  # /data/.fal/model_weights/my-model
persistent = FAL_PERSISTENT_DIR                    # /data

# Download model weights (cached after first download)
download_model_weights("https://huggingface.co/...", "/data/models/my-model")

# Clone a git repo (cached)
clone_repository("https://github.com/org/repo", target_dir="/data/repos/repo")
```

---

## Secrets

```bash
# Set via CLI
fal secrets set HUGGINGFACE_TOKEN hf_xxxx
fal secrets set DATABASE_URL postgresql://...

# List / delete
fal secrets list
fal secrets delete HUGGINGFACE_TOKEN
```

Access in function:
```python
import os

@fal.function(machine_type="GPU-T4", requirements=["transformers"])
def load_private_model():
    token = os.environ["HUGGINGFACE_TOKEN"]  # Injected automatically
    from transformers import AutoModel
    return AutoModel.from_pretrained("private/model", token=token)
```

---

## CLI Reference

```bash
# Auth
fal auth login
fal auth logout
fal auth status

# Run (temporary test URL)
fal run app.py::MyFunction
fal run app.py::MyApp

# Deploy (persistent production URL)
fal deploy app.py::MyApp --app-name my-production-app

# Manage apps
fal apps list
fal apps logs <app-id>
fal apps delete <app-id>

# Keys
fal keys list
fal keys create --name ci-key
fal keys revoke <key-id>

# Secrets
fal secrets set MY_SECRET value
fal secrets list
fal secrets delete MY_SECRET

# Files
fal files upload path/to/file.bin
fal files list

# Queue
fal queue list
fal queue status <request-id>
fal queue cancel <request-id>
```

---

## Local Testing

```python
# Test locally before deploying
result = my_function.local("test input")  # Runs in local Python env
result = my_function("test input")        # Runs on fal.ai cloud
```

---

## Project Layout

```
my_project/
├── app.py          # fal.App or @fal.function definitions
├── requirements.txt
└── local_module.py # Sync to worker with local_python_modules=["local_module"]
```

```python
@fal.function(
    machine_type="GPU-T4",
    local_python_modules=["local_module"],  # Uploaded alongside function
)
def run():
    import local_module  # Available on remote worker
    local_module.do_something()
```

See `fal-api-reference` skill for calling deployed endpoints from JavaScript/Python.
See `fal-optimization` skill for performance tuning (keep_alive, inductor cache, GPU selection).
