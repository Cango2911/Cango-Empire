---
name: recammaster
version: 1.0.0
description: "ReCamMaster — Camera-Controlled Generative Rendering from a Single Video (ICCV'25 Oral, Best Paper Finalist). Re-captured in-the-wild Videos mit neuen Kamera-Trajektorien via Wan2.1. 10 Kamera-Bewegungstypen: Pan, Tilt, Zoom, Translate, Arc."
author: KlingAIResearch / KwaiVGI (Kuaishou Technology / Zhejiang University)
source: https://github.com/KlingAIResearch/ReCamMaster
license: Apache-2.0
type: agent-skill
tags:
  - camera-control
  - video-generation
  - diffusion
  - pytorch
  - wan2.1
  - diffsynth
---

# ReCamMaster — Camera-Controlled Video Re-Rendering

## Was ist ReCamMaster?

ReCamMaster ist ein **ICCV 2025 Oral Paper (Best Paper Finalist)** von Kuaishou Technology / Zhejiang University. Es ermöglicht das **Re-Capturing von In-the-Wild-Videos** mit neuen Kamera-Trajektorien — d.h. ein bestehendes Video wird mit einer anderen Kamerabewegung neu gerendert, ohne dass die Szene oder die Subjekte sich verändern.

**Kernidee**: Video Conditioning Scheme + Wan2.1 T2V-Modell → neues Video mit anderer Kameraperspektive.

**Online-Demo**: [Kling AI Website](https://app.klingai.com/global/) | [Eigene Videos testen](https://docs.google.com/forms/d/e/1FAIpQLSezOzGPbm8JMXQDq6EINiDf6iXn7rV4ozj6KcbQCSAzE8Vsnw/viewform)

## Kamera-Trajektorien (cam_type)

| cam_type | Trajektorie |
|----------|-------------|
| 1 | Pan Right |
| 2 | Pan Left |
| 3 | Tilt Up |
| 4 | Tilt Down |
| 5 | Zoom In |
| 6 | Zoom Out |
| 7 | Translate Up (mit Rotation) |
| 8 | Translate Down (mit Rotation) |
| 9 | Arc Left (mit Rotation) |
| 10 | Arc Right (mit Rotation) |

## Setup & Installation

### Voraussetzungen

- Python 3.10+
- NVIDIA GPU (empfohlen, CUDA 11.8+)
- Rust + Cargo (für DiffSynth-Studio Extensions)
- ~50GB Speicher für Wan2.1 Checkpoints

### Schritt 1: Environment einrichten

```bash
# Rust/Cargo installieren (für DiffSynth-Studio)
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
. "$HOME/.cargo/env"

# Repo klonen und installieren
git clone https://github.com/KlingAIResearch/ReCamMaster.git
cd ReCamMaster
pip install -e .
```

### Schritt 2: Pretrained Checkpoints herunterladen

**Wan2.1 Basismodell:**
```bash
python download_wan2.1.py
```

**ReCamMaster Checkpoint:**
Von [HuggingFace](https://huggingface.co/KwaiVGI/ReCamMaster-Wan2.1/blob/main/step20000.ckpt) herunterladen und in `models/ReCamMaster/checkpoints/` ablegen.

## Inference

### Schnellstart mit Beispiel-Videos

```bash
# cam_type 1 = Pan Right
python inference_recammaster.py --cam_type 1

# Anderen Kamera-Typ wählen
python inference_recammaster.py --cam_type 5  # Zoom In
```

### Eigene Videos testen

**Datenstruktur vorbereiten** (wie `example_test_data/`):
```
my_data/
├── videos/
│   ├── 1.mp4   # mind. 81 Frames
│   ├── 2.mp4
│   └── ...
├── cameras/    # optional: Kamera-Parameter
└── metadata.csv  # Format: file_name,text
```

`metadata.csv` Format:
```csv
file_name,text
1.mp4,"Beschreibung des Videos..."
2.mp4,"Weitere Beschreibung..."
```

Dann Inference starten:
```bash
python inference_recammaster.py \
  --cam_type 1 \
  --dataset_path path/to/my_data
```

### Mit eigenem Checkpoint

```bash
python inference_recammaster.py \
  --cam_type 1 \
  --ckpt_path path/to/checkpoint.ckpt
```

## Training

### Schritt 1: Zusätzliche Dependencies

```bash
pip install lightning pandas websockets
```

### Schritt 2: MultiCamVideo Dataset

```bash
# Von HuggingFace herunterladen:
# https://huggingface.co/datasets/KwaiVGI/MultiCamVideo-Dataset
```

### Schritt 3: VAE Features extrahieren

```bash
CUDA_VISIBLE_DEVICES="0,1,2,3,4,5,6,7" python train_recammaster.py \
  --task data_process \
  --dataset_path path/to/MultiCamVideo/Dataset \
  --output_path ./models \
  --text_encoder_path "models/Wan-AI/Wan2.1-T2V-1.3B/models_t5_umt5-xxl-enc-bf16.pth" \
  --vae_path "models/Wan-AI/Wan2.1-T2V-1.3B/Wan2.1_VAE.pth" \
  --tiled \
  --num_frames 81 \
  --height 480 \
  --width 832 \
  --dataloader_num_workers 2
```

### Schritt 4: Training starten

```bash
CUDA_VISIBLE_DEVICES="0,1,2,3,4,5,6,7" python train_recammaster.py \
  --task train \
  --dataset_path recam_train_data \
  --output_path ./models/train \
  --dit_path "models/Wan-AI/Wan2.1-T2V-1.3B/diffusion_pytorch_model.safetensors" \
  --steps_per_epoch 8000 \
  --max_epochs 100 \
  --learning_rate 1e-4 \
  --accumulate_grad_batches 1 \
  --use_gradient_checkpointing \
  --dataloader_num_workers 4
```

## Kamera-Visualisierung

```bash
python vis_cam.py
```

## Architektur

```
Input Video (Source) ──────────────────────────────────────┐
                                                            │
Camera Trajectory (cam_type 1-10) ─→ Camera Conditioning   │
                                            │               │
                               Wan2.1 DiT + ReCamMaster     │
                               (Video Conditioning Scheme)  │
                                            │               │
                               Output: Re-captured Video ←──┘
```

**Technischer Aufbau:**
- Basismodell: Wan2.1 T2V (1.3B oder größer)
- DiffSynth-Studio: Inference + Training Framework
- Video Conditioning: Source-Video als bedingtes Signal
- Camera Control: Vorberechnete Kamera-Extrinsics als zusätzliches Conditioning

## MultiCamVideo Dataset

- **Umfang**: 136K Videos, 13.6K Szenen
- **Rendering**: Unreal Engine 5
- **Kameras**: 10 synchronisierte Kameras pro Szene
- **Szenentypen**: Stadtstraßen, Einkaufszentren, Cafés, Büroräume, Landschaft
- **Charaktere**: 66 menschliche 3D-Modelle (von Fab + Mixamo)
- **Animationen**: 93 verschiedene (Winken, Tanzen, Jubeln, ...)
- **Download**: [HuggingFace Dataset](https://huggingface.co/datasets/KwaiVGI/MultiCamVideo-Dataset)

## Video-Tipps

- **Mindest-Frames**: 81 Frames pro Input-Video (≈ 3,3s bei 25fps)
- **Auflösung**: 480×832 (Standard für Training)
- **Captions**: Für beste Ergebnisse detaillierte Video-Beschreibungen verwenden ([Wan2.1 Prompt Extension](https://github.com/Wan-Video/Wan2.1#prompt-extension))
- **Kamera-Auswahl**: Pan/Tilt für einfache Bewegungen, Arc für dramatische Kamerafahrten

## Verwandte Projekte

- [SynCamMaster](https://github.com/KwaiVGI/SynCamMaster) — Synchronisierte Multi-Kamera-Videos mit stationären Kameras
- [LivePortrait](https://github.com/KlingAIResearch/LivePortrait) — Portrait Animation (selbes Labor)
- [Wan2.1](https://github.com/Wan-Video/Wan2.1) — Basismodell für ReCamMaster

## Referenzen

- Paper: [arXiv 2503.11647](https://arxiv.org/abs/2503.11647) — ReCamMaster: Camera-Controlled Generative Rendering from A Single Video
- Projektseite: https://jianhongbai.github.io/ReCamMaster/
- GitHub: https://github.com/KlingAIResearch/ReCamMaster
- Checkpoint: https://huggingface.co/KwaiVGI/ReCamMaster-Wan2.1
- Dataset: https://huggingface.co/datasets/KwaiVGI/MultiCamVideo-Dataset
