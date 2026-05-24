---
name: kling-video-tools
description: >
  Remove watermarks from KLing AI-generated videos and enhance video quality
  using STTN inpainting and Real-ESRGAN/GFPGAN super-resolution. Use when the
  user wants to remove a watermark from a video, enhance video resolution,
  improve face quality in video, or process KLing/AI-generated videos for
  production use. Triggers on: watermark remove, video enhance, upscale video,
  ESRGAN, GFPGAN, KLing watermark, video cleanup.
user-invocable: true
metadata:
  tags: [kling, video, watermark, enhance, esrgan, gfpgan, sttn, upscale]
  source: https://github.com/chenwr727/KLing-Video-WatermarkRemover-Enhancer
---

# KLing Video Tools — Watermark Removal & Enhancement

Python CLI tool to post-process KLing AI-generated videos:
- **Watermark removal** via STTN spatial-temporal inpainting
- **Video enhancement** via Real-ESRGAN (2× upscale) + GFPGAN (face restoration)

## Prerequisites

```bash
# 1. Clone with submodules
git clone --recurse-submodules https://github.com/chenwr727/KLing-Video-WatermarkRemover-Enhancer.git
cd KLing-Video-WatermarkRemover-Enhancer

# 2. Install dependencies
pip install -r requirements.txt

# 3. Download model weights into weights/
#    - weights/sttn.pth
#    - weights/RealESRGAN_x2plus.pth
#    - weights/GFPGANv1.4.pth
```

## Configuration

Edit `config.yaml` to set the watermark position:

```yaml
watermark:
  position: [556, 1233, 701, 1267]   # [xmin, ymin, xmax, ymax]
  ckpt_p: "./weights/sttn.pth"
  mask_expand: 30
  neighbor_stride: 10

enhance:
  RealESRGAN_model_path: "./weights/RealESRGAN_x2plus.pth"
  GFPGANer_model_path: "./weights/GFPGANv1.4.pth"
```

**Finding the watermark position:**
1. Open the video in any player
2. Note the pixel coordinates of the watermark corners
3. Set `position: [xmin, ymin, xmax, ymax]` in config.yaml

## Usage

```bash
# Remove watermark only
python main.py --input video.mp4 --remove-watermark

# Enhance video quality only (2× upscale + face restoration)
python main.py --input video.mp4 --enhance-video

# Both watermark removal AND enhancement
python main.py --input video.mp4 --remove-watermark --enhance-video

# Process entire folder of videos
python main.py --input /path/to/folder/ --remove-watermark --enhance-video
```

Output file is saved as `<original_name>_enhanced.mp4` in the same directory.

## Steps for Agent

1. **Identify the request** — watermark removal, enhancement, or both
2. **Check prerequisites** — ffmpeg installed? weights downloaded?
3. **Find watermark position** — ask user or inspect the video
4. **Update config.yaml** — set correct `position` values
5. **Run the command** — use appropriate flags
6. **Report output path** — confirm the `_enhanced.mp4` file was created

## Notes

- GPU (CUDA) is optional but strongly recommended — CPU is very slow
- `mask_expand: 30` adds padding around the watermark region
- For batch processing, point `--input` at a directory
- Supported formats: `.mp4`, `.avi`, `.mkv`
