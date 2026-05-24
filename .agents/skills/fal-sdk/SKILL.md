---
name: fal-sdk
description: Use the official fal.ai Python SDK and CLI. This skill covers `fal-client` (calling model endpoints — run, submit, stream, realtime, upload) and `fal` (deploying serverless Python apps to fal.ai — functions, app classes, endpoints, CLI). Use when building integrations with fal.ai models, deploying custom ML apps, or managing keys/secrets/files via the fal CLI.
license: MIT
metadata:
  author: fal-ai (Features & Labels)
  source: https://github.com/fal-ai/fal
  pypi_fal: https://pypi.org/project/fal
  pypi_fal_client: https://pypi.org/project/fal-client
compatibility: Python 3.8+. Requires FAL_KEY environment variable.
allowed-tools: Bash(pip:*) Bash(pip3:*) Bash(fal:*) Read Write Edit
---

# fal.ai Python SDK

Official monorepo for fal.ai Python packages:
- **`fal-client`** — call model endpoints (lightweight, minimal deps)
- **`fal`** — deploy serverless Python apps + full CLI
- **`isolate-proto`** — gRPC definitions (internal, auto-installed as dep)

## Authentication

```bash
export FAL_KEY=your_fal_api_key
# or interactive login:
fal auth login
```

Get your key: https://fal.ai/dashboard/keys

---

## fal-client — Calling Model Endpoints

```bash
pip install fal-client
```

### Sync usage

```python
import fal_client

# Simple run (blocking)
result = fal_client.run(
    "fal-ai/flux/dev",
    arguments={"prompt": "a photo of a cat on the moon"}
)
print(result["images"][0]["url"])
```

### Async usage

```python
import asyncio
import fal_client

async def main():
    result = await fal_client.run_async(
        "fal-ai/flux/dev",
        arguments={"prompt": "a photo of a cat on the moon"}
    )
    print(result["images"][0]["url"])

asyncio.run(main())
```

### Queue + polling (long-running jobs)

```python
import fal_client

# Submit to queue (returns immediately)
handle = fal_client.submit("fal-ai/hunyuan-video", arguments={"prompt": "..."})

# Poll until done
result = fal_client.result(handle.request_id, handle.endpoint_id)

# Or subscribe with callback
def on_queue_update(update):
    if isinstance(update, fal_client.InProgress):
        print("Running:", update.logs)

result = fal_client.subscribe(
    "fal-ai/flux/dev",
    arguments={"prompt": "..."},
    on_queue_update=on_queue_update,
)
```

### Streaming (SSE)

```python
import fal_client

for event in fal_client.stream("fal-ai/flux-lora-fast-training", arguments={...}):
    print(event)
```

### Realtime WebSocket

```python
import fal_client

with fal_client.realtime("fal-ai/flux/dev") as conn:
    result = conn.run({"prompt": "..."})
    print(result)
```

### File upload

```python
import fal_client

# Upload a local file → returns CDN URL
url = fal_client.upload_file("path/to/image.png")

# Or encode as data URL (no upload)
data_url = fal_client.encode_image("path/to/image.png")

result = fal_client.run("fal-ai/birefnet", arguments={"image_url": url})
```

### Cancel / status / result

```python
handle = fal_client.submit("fal-ai/flux/dev", arguments={"prompt": "..."})

status = fal_client.status(handle.endpoint_id, handle.request_id)
result = fal_client.result(handle.endpoint_id, handle.request_id)
fal_client.cancel(handle.endpoint_id, handle.request_id)
```

---

## fal — Serverless Python SDK + CLI

```bash
pip install fal
```

### Deploy a function

```python
import fal

@fal.function(
    machine_type="GPU-T4",
    requirements=["torch", "transformers"],
)
def generate(prompt: str) -> dict:
    # runs on fal.ai GPU
    return {"result": f"Generated: {prompt}"}
```

```bash
fal run my_app.py::generate -- --prompt "hello"
fal deploy my_app.py::generate --app-name my-generator
```

### Build a multi-endpoint App

```python
import fal
from pydantic import BaseModel

class Input(BaseModel):
    prompt: str

class Output(BaseModel):
    image_url: str

class MyApp(fal.App, name="my-app"):
    @fal.endpoint("/")
    def generate(self, input: Input) -> Output:
        # ... model inference
        return Output(image_url="https://...")

    @fal.endpoint("/health")
    def health(self) -> dict:
        return {"status": "ok"}
```

```bash
fal run my_app.py::MyApp
fal deploy my_app.py::MyApp
```

### Realtime WebSocket endpoint

```python
import fal

class RealtimeApp(fal.App):
    @fal.realtime("/ws")
    def process(self, input: dict) -> dict:
        return {"result": input}
```

### Toolkit — Image, Audio, Video, File

```python
from fal.toolkit import Image, Audio, Video, File

# Image (PIL-backed, converts to fal CDN URL)
img = Image.from_pil(pil_image)
img_url = img.url

# File upload
f = File.from_path("model.ckpt")
url = f.url

# KV store (key-value per user/app)
from fal.toolkit import KV
kv = KV()
kv.set("key", "value")
val = kv.get("key")
```

### CLI commands

```bash
# Auth
fal auth login
fal auth logout
fal auth status

# Keys
fal keys list
fal keys create --name my-key
fal keys revoke <key-id>

# Secrets
fal secrets set MY_SECRET value
fal secrets list
fal secrets delete MY_SECRET

# Files
fal files upload path/to/file.bin
fal files list

# Apps
fal run app.py::MyApp
fal deploy app.py::MyApp --app-name production-app
fal apps list
fal apps logs <app-id>

# Queue
fal queue list
fal queue status <request-id>
fal queue cancel <request-id>

# Runners (GPU machines)
fal runners list
```

### Install from source

```bash
git clone https://github.com/fal-ai/fal
pip install -e 'projects/fal[dev]'
pip install -e 'projects/fal_client'
```

### Run tests

```bash
pytest -n auto -v projects/fal/tests/unit
pytest projects/fal_client/tests/
```

## Package structure

| Path | Package | PyPI |
|------|---------|------|
| `projects/fal/src/fal/` | `fal` | `pip install fal` |
| `projects/fal_client/src/fal_client/` | `fal-client` | `pip install fal-client` |
| `projects/isolate_proto/src/isolate_proto/` | `isolate-proto` | (dep of fal) |

## Key modules (fal-client)

| Module | Purpose |
|--------|---------|
| `fal_client/client.py` | `SyncClient`, `AsyncClient` — all API methods |
| `fal_client/auth.py` | FAL_KEY env var resolution |
| `fal_client/_headers.py` | User-Agent, auth headers |

## Key modules (fal SDK)

| Module | Purpose |
|--------|---------|
| `fal/api/api.py` | `@fal.function` decorator |
| `fal/app.py` | `fal.App`, `@fal.endpoint`, `@fal.realtime` |
| `fal/cli/main.py` | CLI entry point |
| `fal/toolkit/` | Image, Audio, Video, File, KV helpers |
| `fal/auth/` | Auth0 + local key auth |
| `fal/api/deploy.py` | Deployment pipeline |
| `fal/api/secrets.py` | Secrets management |
| `fal/realtime.py` | WebSocket realtime support |
