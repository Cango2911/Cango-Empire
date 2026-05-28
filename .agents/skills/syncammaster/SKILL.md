---
name: syncammaster
version: 1.0.0
description: "SynCamMaster — Synchronizing Multi-Camera Video Generation from Diverse Viewpoints (ICLR 2025). Generiert synchronisierte Multi-Kamera-Videos aus verschiedenen Blickwinkeln via Wan2.1. 3 Kamera-Typen: Azimuth, Elevation, Distance. SynCamVideo Dataset: 34K Videos, 3.4K UE5-Szenen, stationäre Kameras."
author: KlingAIResearch / KwaiVGI (Kuaishou Technology, Zhejiang University)
source: https://github.com/KlingAIResearch/SynCamMaster
license: Apache-2.0
type: agent-skill
tags:
  - multi-camera
  - video-generation
  - diffusion
  - pytorch
  - wan2.1
  - diffsynth
  - camera-control
  - synchronized-video
---

# SynCamMaster — Synchronized Multi-Camera Video Generation

## Was ist SynCamMaster?

SynCamMaster ist ein **ICLR 2025** Paper von Kuaishou Technology / Zhejiang University. Es liftet vortrainierte Text-to-Video-Modelle für **Multi-Kamera-Video-Generierung** aus diversen Blickwinkeln. Das System generiert synchronisierte Videos aus mehreren Kamerapositionen gleichzeitig — alle zeitlich ausgerichtet und inhaltlich konsistent.

**Kernunterschied zu ReCamMaster**: SynCamMaster generiert Videos mit **stationären Kameras** aus verschiedenen Winkeln. ReCamMaster re-rendert ein existierendes Video mit **bewegten Kamera-Trajektorien**.

**Basismodell**: Wan2.1 T2V + DiffSynth-Studio

## Kamera-Typen (cam_type)

| cam_type | Beschreibung | Kamera-Bewegung |
|----------|-------------|-----------------|
| `"az"` | **Azimuth** — horizontaler Winkel um die Szene | Stationär, verschiedene horizontale Positionen |
| `"el"` | **Elevation** — vertikaler Winkel (Höhe) | Stationär, verschiedene Höhenpositionen |
| `"dis"` | **Distance** — Distanz zur Szene | Stationär, verschiedene Abstände (nah/fern) |

## Setup & Installation

### Voraussetzungen

- Python 3.10+
- NVIDIA GPU (CUDA 11.8+ empfohlen)
- Rust + Cargo (für DiffSynth-Studio Extensions)
- ~50GB Speicher für Wan2.1 Checkpoints

### Schritt 1: Environment einrichten

```bash
# Rust/Cargo installieren (für DiffSynth-Studio)
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
. "$HOME/.cargo/env"

# Repo klonen und installieren
git clone https://github.com/KlingAIResearch/SynCamMaster.git
cd SynCamMaster
pip install -e .
```

### Schritt 2: Pretrained Checkpoints herunterladen

**Wan2.1 Basismodell:**
```bash
python download_wan2.1.py
```

**SynCamMaster Checkpoint:**
Von [HuggingFace](https://huggingface.co/KwaiVGI/SynCamMaster-Wan2.1/blob/main/step20000.ckpt) herunterladen und in `models/SynCamMaster/checkpoints/` ablegen.

## Inference

### Schnellstart mit Beispiel-Daten

```bash
# Azimuth (Standard) — horizontale Kamerawinkel
python inference_syncammaster.py --cam_type "az"

# Elevation — vertikale Kamerawinkel
python inference_syncammaster.py --cam_type "el"

# Distance — verschiedene Abstände
python inference_syncammaster.py --cam_type "dis"
```

### Eigene Videos/Texte testen

Datenstruktur wie `example_test_data/` aufbauen:
```
my_data/
├── cameras/
│   └── camera_extrinsics.json   # Kamera-Extrinsics (81 Frames, 10 Kameras)
└── metadata.csv                 # Format: file_name,text
```

`metadata.csv` Format:
```csv
file_name,text
vid_01.mp4,"Eine Person tanzt auf einer Stadtstraße bei Sonnenuntergang."
```

Dann Inference starten:
```bash
python inference_syncammaster.py \
  --cam_type "az" \
  --dataset_path path/to/my_data

# Mit eigenem Checkpoint:
python inference_syncammaster.py \
  --cam_type "az" \
  --ckpt_path path/to/checkpoint.ckpt
```

### Inference-Parameter

| Flag | Default | Beschreibung |
|------|---------|-------------|
| `--cam_type` | `"az"` | Kamera-Typ: `az`, `el`, `dis` |
| `--ckpt_path` | — | Pfad zum SynCamMaster-Checkpoint |
| `--dataset_path` | `./example_test_data` | Pfad zu Testdaten |
| `--cfg_scale` | `5.0` | Classifier-Free Guidance Scale |
| `--num_frames` | `81` | Anzahl der Frames |
| `--height` | `480` | Video-Höhe |
| `--width` | `832` | Video-Breite |

## Training

### Schritt 1: Zusätzliche Dependencies

```bash
pip install lightning pandas websockets
```

### Schritt 2: SynCamVideo Dataset herunterladen

Von [HuggingFace](https://huggingface.co/datasets/KwaiVGI/SynCamVideo-Dataset) herunterladen.

Dataset-Struktur:
```
SynCamVideo-Dataset/
├── train/
│   └── f24_aperture5/
│       ├── scene1/
│       │   ├── videos/
│       │   │   ├── cam01.mp4   # 81 Frames, 1280×1280, 15fps
│       │   │   ├── cam02.mp4
│       │   │   └── ... (cam10.mp4)
│       │   └── cameras/
│       │       └── camera_extrinsics.json
│       └── ... (scene3400/)
└── val/
    └── basic/
        ├── videos/ + cameras/
```

### Schritt 3: VAE Features extrahieren

```bash
CUDA_VISIBLE_DEVICES="0,1,2,3,4,5,6,7" python train_syncammaster.py \
  --task data_process \
  --dataset_path path/to/SynCamVideo/Dataset \
  --output_path ./models \
  --text_encoder_path "models/Wan-AI/Wan2.1-T2V-1.3B/models_t5_umt5-xxl-enc-bf16.pth" \
  --vae_path "models/Wan-AI/Wan2.1-T2V-1.3B/Wan2.1_VAE.pth" \
  --tiled \
  --num_frames 81 \
  --height 480 \
  --width 832 \
  --dataloader_num_workers 2
```

### Schritt 4: Sample-Liste berechnen

```bash
python generate_sample_list.py
```

### Schritt 5: Training starten

```bash
CUDA_VISIBLE_DEVICES="0,1,2,3,4,5,6,7" python train_syncammaster.py \
  --task train \
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

## SynCamVideo Dataset

| Eigenschaft | Wert |
|-------------|------|
| Szenen | 3.400 dynamische Szenen |
| Kameras/Szene | 10 synchronisierte, stationäre Kameras |
| Gesamt-Videos | 34.000 |
| Auflösung | 1280×1280 |
| Frames | 81 Frames @ 15fps |
| Rendering | Unreal Engine 5 |
| Brennweite | 24mm, Aperture 5.0 |

**Kamera-Positionierung**: Jede Kamera wird zufällig auf einer hemisphärischen Oberfläche um den Charakter herum gesampelt.

**Enthält**: 37 UE5-Umgebungen, 66 menschliche Charaktere, 93 Animationen (Wehen, Tanzen, Jubeln).

**Zentral-Crop-Tipp**: Dataset hat 1:1 Auflösung → mit Center Crop auf 16:9, 9:16, 4:3 anpassen.

## Architektur

```
Text-Prompt ──────────────────────────┐
                                       │
Camera Extrinsics (10 Kameras) ───→   │
Relative Pose Embedding               │
          │                            │
          └──→ Wan2.1 DiT +            │
               SynCamMaster ←──────────┘
               (Pose Conditioning)
                    │
          Synchronisierte Videos
          (alle 10 Kameraperspektiven)
```

**Pipeline**: `WanVideoSynCamMasterPipeline` (in `diffsynth/pipelines/`)

**Kamera-Einbettung**: Camera-to-World (C2W) Matrizen → Relative Poses → Pose Embedding → DiT Conditioning

## SynCamMaster vs. ReCamMaster

| Eigenschaft | SynCamMaster | ReCamMaster |
|-------------|-------------|-------------|
| Task | Multi-Kamera-Generierung | Video Re-Rendering |
| Eingabe | Text-Prompt + Kameraposen | Bestehendes Video |
| Kameras | Stationär, diverse Winkel | Bewegte Trajektorien |
| Ausgabe | N synchronisierte Videos | 1 Video, neue Kamera |
| Paper | ICLR 2025 | ICCV 2025 Oral |
| Dataset | SynCamVideo (34K Videos) | MultiCamVideo (136K Videos) |

## Verwandte Projekte

- [ReCamMaster](https://github.com/KlingAIResearch/ReCamMaster) — Video Re-Rendering mit neuen Kamera-Trajektorien (Nachfolgeprojekt)
- [3DTrajMaster](http://fuxiao0719.github.io/projects/3dtrajmaster) — 6DoF Entity Motion Control
- [StyleMaster](https://zixuan-ye.github.io/stylemaster/) — Stil-gesteuertes Video
- [GCD](https://gcd.cs.columbia.edu/) — Novel Viewpoints aus monokularem Video
- [CVD](https://collaborativevideodiffusion.github.io) — Multi-View Video mit mehreren Kamera-Trajektorien

## Referenzen

- Paper: [arXiv 2412.07760](https://arxiv.org/abs/2412.07760) — SynCamMaster: Synchronizing Multi-Camera Video Generation from Diverse Viewpoints
- Projektseite: https://jianhongbai.github.io/SynCamMaster/
- GitHub: https://github.com/KlingAIResearch/SynCamMaster
- Checkpoint: https://huggingface.co/KwaiVGI/SynCamMaster-Wan2.1
- Dataset: https://huggingface.co/datasets/KwaiVGI/SynCamVideo-Dataset
