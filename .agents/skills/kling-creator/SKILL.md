---
name: kling-creator
description: Generate AI images and videos using Kling AI (klingai.kuaishou.com / klingai.com). Use this skill when the user wants to create images or videos with Kling AI — text-to-image, image-to-image, text-to-video, or image-to-video. Supports Kling models 1.0, 1.5, 1.6, 2.0, 2.1 and Kolors image models.
license: MIT
metadata:
  author: yihong0618
  version: "0.6.0"
  source: https://github.com/yihong0618/klingCreator
compatibility: Python 3.9+. Requires KLING_COOKIE env var (browser cookie from klingai.com) or KLING_EMAIL + KLING_PASSWORD for programmatic auth.
allowed-tools: Bash(python:*) Bash(pip:*) Read Write
---

# Kling AI Creator

Reverse-engineered Python API client for Kling AI image and video generation.

## Setup

### Install
```bash
pip install -U kling-creator
# or from plugin source:
pip install -r .agents/plugins/kling-creator/requirements.txt
```

### Authentication (choose one)

**Option A — Browser cookie (recommended):**
1. Login at https://klingai.com (international) or https://klingai.kuaishou.com (China)
2. Open DevTools → Network → XHR → copy the `Cookie` header
3. `export KLING_COOKIE='your_full_cookie_string'`

**Option B — Email/password (international only):**
```python
from kling import Authorizator
a = Authorizator()
a.auth("your@email.com", "password")
# Then use a.cookies as your cookie string
```

## CLI Usage

```bash
# Image generation (text-to-image)
python -m kling --prompt 'a big dog'

# Image-to-image
python -m kling --prompt 'wear a yellow hat' -I dog.png

# Video generation (text-to-video)
python -m kling --type video --prompt 'a big running cat'

# High quality video
python -m kling --type video --prompt 'a big running cat' --high-quality

# Image-to-video
python -m kling --type video --prompt 'make this picture alive' -I cat.png

# High quality image-to-video
python -m kling --type video --prompt 'make this picture alive' -I cat.png --high-quality

# Extend video to 10s
python -m kling --type video --prompt 'make this picture alive' -I cat.png --high-quality --extend

# Use Kling 1.5 model (requires --high-quality)
python -m kling --type video --prompt '一只奔跑的狗' --high-quality --model_name 1.5

# Use Kling 2.1 model
python -m kling --type video --prompt 'a running dog' --high-quality --model_name 2.1
```

## Python API

```python
from kling import ImageGen, VideoGen, Authorizator
import os

cookie = os.environ["KLING_COOKIE"]

# --- Image Generation ---
i = ImageGen(cookie)

# Text-to-image (saves to ./output/)
i.save_images("a blue cyber dream", './output')

# Image-to-image with reference
i.save_images("a blue cyber dream", './output', image_url="https://example.com/dog.png")
i.save_images("a blue cyber dream", './output', image_path="./dog.png")

# With options
i.save_images(
    prompt="a futuristic city",
    output_dir='./output',
    ratio="16:9",       # 1:1, 16:9, 4:3, 3:2, 2:3, 3:4, 9:16, 21:9
    count=4,            # 1-9 images
    model_name="2.1",  # 1.0, 1.5, 2.0, 2.1
)

# --- Video Generation ---
v = VideoGen(cookie)

# Text-to-video
v.save_video("a big running cat", './output')

# Image-to-video (URL)
v.save_video("make this picture alive", './output', image_url="https://example.com/cat.png")

# High quality + extend to 10s
v.save_video(
    "make this alive",
    './output',
    image_path="./cat.png",
    is_high_quality=True,
    auto_extend=True,
    model_name="2.1"  # 1.0, 1.5, 1.6, 2.1
)

# Check account balance
print(f"Points: {v.get_account_point()}")
```

## Models

| Type | Model | Notes |
|------|-------|-------|
| Image | Kolors 1.0, 1.5, 2.0, 2.1 | Default: 2.1 |
| Video | Kling 1.0, 1.5, 1.6, 2.1 | Default: 1.0; 1.5+ needs --high-quality |

## Tips

- Cookies expire — re-copy from browser if you get auth errors
- Video generation takes 2–5 minutes; 10-min timeout
- High-quality mode required for Kling 1.5+ models
- Image output: PNG format; Video output: MP4 format
- Account points are consumed per generation
