---
name: liveportrait
version: 1.0.0
description: "LivePortrait — Efficient Portrait Animation with Stitching and Retargeting Control. PyTorch-based portrait animation for humans and animals. Used in production by Kuaishou, Douyin, Jianying, WeChat Channels."
author: KlingAIResearch (Kuaishou Technology)
source: https://github.com/KlingAIResearch/LivePortrait
license: MIT
type: agent-skill
tags:
  - portrait-animation
  - video-generation
  - deep-learning
  - pytorch
  - gradio
  - face
  - animals
---

# LivePortrait — Portrait Animation Skill

## Was ist LivePortrait?

LivePortrait ist eine effiziente Portrait-Animierungslösung (PyTorch) von Kuaishou Technology, die Portraits (Menschen + Tiere: Katzen, Hunde) durch ein Driving-Video oder -Bild animiert. Kernfeatures: Stitching, Retargeting Control, Image-Driven Mode, Regional Control, Portrait Video Editing (v2v).

**Eingesetzt von**: Kuaishou, Douyin (TikTok China), Jianying (CapCut), WeChat Channels — sowie zahlreichen Startups und Creators weltweit.

## Kernkonzepte

### Modi

| Modus | Beschreibung | Script |
|-------|-------------|--------|
| Humans (Standard) | Portrait-Animation für menschliche Gesichter | `inference.py` |
| Animals | Katzen & Hunde animieren (Linux/Windows + NVIDIA) | `inference_animals.py` |
| Image-Driven | Einzelbild als Driving-Quelle | `inference.py -d bild.jpg` |
| V2V (Video-to-Video) | Portrait-Video editieren | `inference.py -s video.mp4 -d driving.mp4` |
| Gradio UI | Web-Interface für interaktives Editing | `app.py` / `app_animals.py` |

### Stitching & Retargeting

- **Stitching**: Nahtloses Einfügen des animierten Gesichts in den Hintergrund
- **Retargeting**: Bewegungen des Driving-Videos auf das Source-Portrait übertragen
- **Motion Template** (`.pkl`): Vorberechnete Motion-Templates zum Schutz der Privatsphäre + Speedup

## Setup & Installation

### Voraussetzungen

- Python 3.10 (via conda)
- FFmpeg
- NVIDIA GPU (empfohlen; macOS Apple Silicon möglich, ~20x langsamer)
- CUDA 11.8 / 12.1 (für Animals mode)

### Installation

```bash
git clone https://github.com/KlingAIResearch/LivePortrait
cd LivePortrait

conda create -n LivePortrait python=3.10
conda activate LivePortrait

# Linux/Windows:
pip install -r requirements.txt

# macOS Apple Silicon:
pip install -r requirements_macOS.txt
```

### Pretrained Weights herunterladen

```bash
# Via HuggingFace Hub:
huggingface-cli download KlingTeam/LivePortrait \
  --local-dir pretrained_weights \
  --exclude "*.git*" "README.md" "docs"

# Bei kein HF-Zugang — via hf-mirror:
export HF_ENDPOINT=https://hf-mirror.com
huggingface-cli download KlingTeam/LivePortrait \
  --local-dir pretrained_weights \
  --exclude "*.git*" "README.md" "docs"
```

Alternativ: Google Drive oder Baidu Yun (siehe README).

## Inference — Schnellstart

### Humans Mode

```bash
# Standard (Demo-Video):
python inference.py

# Eigene Source + Driving:
python inference.py -s assets/examples/source/s9.jpg -d assets/examples/driving/d0.mp4

# Source als Video (V2V):
python inference.py -s assets/examples/source/s13.mp4 -d assets/examples/driving/d0.mp4

# Auto-Crop des Driving-Videos:
python inference.py -s assets/examples/source/s9.jpg \
  -d assets/examples/driving/d13.mp4 \
  --flag_crop_driving_video

# Motion Template (Privacy + Speed):
python inference.py -s assets/examples/source/s9.jpg -d assets/examples/driving/d5.pkl

# macOS Apple Silicon:
PYTORCH_ENABLE_MPS_FALLBACK=1 python inference.py
```

**Output**: `animations/<source>--<driving>_concat.mp4` (driving | input | result nebeneinander)

### Animals Mode (Linux/Windows + NVIDIA)

Erst XPose-Op bauen:
```bash
cd src/utils/dependencies/XPose/models/UniPose/ops
python setup.py build install
cd -
```

Dann:
```bash
python inference_animals.py \
  -s assets/examples/source/s39.jpg \
  -d assets/examples/driving/wink.pkl \
  --driving_multiplier 1.75 \
  --no_flag_stitching
```

### Gradio Web-Interface

```bash
# Humans:
python app.py

# Animals:
python app_animals.py

# Mit Share-Link (öffentlich zugänglich):
python app.py --share
```

## Wichtige Inference-Optionen

| Flag | Beschreibung |
|------|-------------|
| `-s` / `--source` | Source-Bild oder -Video (Portrait) |
| `-d` / `--driving` | Driving-Video, -Bild oder Motion-Template `.pkl` |
| `--flag_crop_driving_video` | Auto-Crop des Driving-Videos auf 1:1 |
| `--scale_crop_driving_video` | Scale für Auto-Crop |
| `--vy_ratio_crop_driving_video` | Vertikaler Offset für Auto-Crop |
| `--driving_multiplier` | Bewegungsstärke (Animals mode) |
| `--no_flag_stitching` | Stitching deaktivieren |
| `--flag_relative_motion` | Relative Bewegungsübertragung |
| `--flag_do_crop` | Source-Portrait automatisch croppen |

## Tipps für optimale Ergebnisse

### Driving-Video-Empfehlungen
- Auf **1:1** Seitenverhältnis zuschneiden (512×512 oder 256×256 px)
- Nur Kopfbereich — minimale Schulter-Bewegungen
- Erstes Frame: Frontales Gesicht mit **neutralem Ausdruck**
- Bei schlechtem Auto-Crop: `--scale_crop_driving_video` + `--vy_ratio_crop_driving_video` anpassen

### Motion Template (`.pkl`)
- Aus Driving-Video vorberechnet für Wiederverwendung
- Schützt Privatsphäre (kein Originalvideo nötig)
- Deutlich schnellere Inference

## Architektur / Pipeline

```
Source Portrait → Appearance Feature Extractor → Feature Map
Driving Video   → Motion Extractor             → Motion Keypoints
                                                        ↓
                         Dense Motion Network (Warping)
                                    ↓
                         SPADE Generator
                                    ↓
                    Stitching & Retargeting Network
                                    ↓
                         Animated Output
```

**Kernmodule** (in `src/modules/`):
- `appearance_feature_extractor.py` — Extrahiert visuelle Features
- `motion_extractor.py` — Extrahiert Motion Keypoints
- `dense_motion.py` — Dense Motion Field Berechnung
- `warping_network.py` — Feature Warping
- `spade_generator.py` — SPADE-basierter Decoder
- `stitching_retargeting_network.py` — Stitching + Retargeting

## Abhängigkeiten (Key)

```
torch / torchvision / torchaudio  — PyTorch
onnxruntime-gpu==1.18.0           — ONNX Runtime (GPU)
transformers==4.38.0              — HuggingFace Transformers
gradio                            — Web-Interface
insightface                       — Face Analysis
ffmpeg                            — Video Processing
```

## Use Cases

| Use Case | Beschreibung |
|----------|-------------|
| **Talking Head** | Portrait spricht/bewegt sich nach Driving-Video |
| **Portrait Video Editing** | Eigenes Video als Source + Driving-Video |
| **Animals Animation** | Katze/Hund nach Driving-Bewegungen animieren |
| **Regional Control** | Bestimmte Gesichtsregionen selektiv animieren |
| **Image-Driven** | Einzelbild als Driving-Quelle (kein Video nötig) |
| **Privacy-Preserving** | Motion Templates statt rohem Driving-Video |
| **Pose Editing** | Kopfpose des Source-Portraits editieren |

## Referenzen

- Paper: [arXiv 2407.03168](https://arxiv.org/pdf/2407.03168) — LivePortrait: Efficient Portrait Animation with Stitching and Retargeting Control
- Projektseite: https://liveportrait.github.io
- HuggingFace Space: https://huggingface.co/spaces/KlingTeam/LivePortrait
- GitHub: https://github.com/KlingAIResearch/LivePortrait
- Pretrained Weights: https://huggingface.co/KlingTeam/LivePortrait
