---
name: videoalign
version: 1.0.0
description: "VideoAlign / VideoReward — Improving Video Generation with Human Feedback (arXiv 2025). VLM-basiertes Reward-Modell (Qwen2-VL-2B) bewertet generierte Videos auf 3 Dimensionen: Visual Quality (VQ), Motion Quality (MQ), Text Alignment (TA). Für Data Filtering, Reject Sampling, DPO, RL. VideoGen-RewardBench Leaderboard."
author: KlingAIResearch / KwaiVGI (Kuaishou Technology)
source: https://github.com/KlingAIResearch/VideoAlign
license: MIT
type: agent-skill
tags:
  - reward-model
  - video-evaluation
  - human-feedback
  - rlhf
  - dpo
  - qwen2-vl
  - lora
  - deepspeed
---

# VideoAlign / VideoReward — Video Quality Reward Model

## Was ist VideoAlign?

VideoAlign ist ein Framework von Kuaishou Technology zur **Verbesserung der Video-Generierung durch menschliches Feedback**. Kernkomponente ist **VideoReward** — ein VLM-basiertes Reward-Modell (fine-getuned auf Qwen2-VL-2B-Instruct), das generierte Videos automatisch auf drei kritischen Dimensionen bewertet.

**Use Cases**: Data Filtering, Guidance, Reject Sampling, DPO (Direct Preference Optimization), RL-Methoden für Video-Generierungsmodelle.

**VideoGen-RewardBench**: Öffentlicher Evaluierungs-Benchmark + Leaderboard für Video-Generierungsmodelle auf HuggingFace.

## Die 3 Bewertungsdimensionen

| Dimension | Kürzel | Beschreibung |
|-----------|--------|-------------|
| **Visual Quality** | VQ | Klarheit, Ästhetik, biologische/logische Korrektheit, Detail-Reichtum, Sicherheit (kein schädlicher Content) |
| **Motion Quality** | MQ | Stabilität, Natürlichkeit, Bewegungsfluss, Fusion mit Hintergrund, Bewegungsausmaß |
| **Text Alignment** | TA | Relevanz zwischen Text-Prompt und Video-Inhalt/Bewegung/Umgebung/Stil/Kamerabewegung |

**Score-Range**: 0–10 pro Dimension. **Overall** = VQ + MQ + TA.

## Setup & Installation

```bash
git clone https://github.com/KlingAIResearch/VideoAlign
cd VideoAlign
conda env create -f environment.yaml
conda activate VideoReward
pip install flash-attn==2.5.8 --no-build-isolation
```

### Checkpoint herunterladen

```bash
cd checkpoints
git lfs install
git clone https://huggingface.co/KwaiVGI/VideoReward
cd ..
```

## Inference — Video-Scoring

### Schnellstart (einzelnes Video)

```bash
python inference.py
```

### Per Python API

```python
import torch
from inference import VideoVLMRewardInference

# Modell laden
inferencer = VideoVLMRewardInference(
    load_from_pretrained="./checkpoints",
    device="cuda:0",
    dtype=torch.bfloat16
)

video_paths = [
    "path/to/video_1.mp4",
    "path/to/video_2.mp4",
]
prompts = [
    "A girl in a pink dress sits down on a chair in a cozy bedroom.",
    "A young explorer walks through an abandoned building at night.",
]

with torch.no_grad():
    rewards = inferencer.reward(video_paths, prompts, use_norm=True)
    # rewards: [{'VQ': ..., 'MQ': ..., 'TA': ..., 'Overall': ...}, ...]
    print(rewards)
```

### Inference-Parameter

| Parameter | Default | Beschreibung |
|-----------|---------|-------------|
| `video_paths` | — | Liste von Video-Pfaden |
| `prompts` | — | Liste von Text-Prompts |
| `fps` | Config-Default | Frames pro Sekunde (Sampling-Rate) |
| `num_frames` | Config-Default | Feste Anzahl Frames (alternativ zu fps) |
| `max_pixels` | Config-Default | Max Pixel pro Frame |
| `use_norm` | `True` | Output-Rewards normalisieren |

**Hinweis**: `fps` und `num_frames` können nicht gleichzeitig gesetzt werden.

## Evaluation auf VideoGen-RewardBench

### 1. Benchmark herunterladen

```bash
cd datasets
git lfs install
git clone https://huggingface.co/datasets/KwaiVGI/VideoGen-RewardBench
cd ..
```

### 2. Evaluation starten

```bash
python eval_videogen_rewardbench.py
```

**Accuracy berechnen:**
```bash
python calc_accuracy.py
```

### Leaderboard

Online-Leaderboard: [HuggingFace Space](https://huggingface.co/spaces/KwaiVGI/VideoGen-RewardBench)

## Training — Eigenes Reward-Modell

### Datenvorbereitung

Trainings-Daten als Pairwise-Comparisons strukturieren:

```
datasets/train/
├── example.csv
└── videos/
    ├── video_1_A.mp4    # Video-Paar A
    ├── video_1_B.mp4    # Video-Paar B
    └── ...
```

**CSV-Format** (`example.csv`):

| Spalte | Beschreibung | Werte |
|--------|-------------|-------|
| `path_A` | Pfad zu Video A | `./videos/example_1_A.mp4` |
| `path_B` | Pfad zu Video B | `./videos/example_1_B.mp4` |
| `prompt` | Text-Prompt | String |
| `VQ` | Visual Quality Präferenz | `A`, `B`, `same` |
| `MQ` | Motion Quality Präferenz | `A`, `B`, `same` |
| `TA` | Text Alignment Präferenz | `A`, `B`, `same` |
| `fps_A` | FPS von Video A | Float |
| `num_frames_A` | Frame-Anzahl von Video A | Int |
| `fps_B` | FPS von Video B | Float |
| `num_frames_B` | Frame-Anzahl von Video B | Int |

### Training starten

```bash
sh train.sh
```

Oder manuell mit DeepSpeed:
```bash
deepspeed --master_port=28500 train_reward.py \
    --lora_enable True \
    --model_name_or_path Qwen/Qwen2-VL-2B-Instruct \
    --meta_data "./datasets/train/example.csv" \
    --data_dir "./datasets/train" \
    --output_dir rm_output \
    --eval_dim "VQ" "MQ" "TA" \
    --output_dim 3 \
    --loss_type "btt" \
    --deepspeed ds_config/zero0.json
```

### Wichtige Training-Parameter

| Parameter | Default | Beschreibung |
|-----------|---------|-------------|
| `--lora_r` | `64` | LoRA Rank |
| `--lora_alpha` | `128` | LoRA Alpha |
| `--fps` | `2` | Frame-Sampling-Rate |
| `--max_frame_pixels` | `200704` (448×448) | Max Pixel/Frame |
| `--loss_type` | `"btt"` | BTT (Bradley-Terry-Thurstone) Loss |
| `--output_dim` | `3` | Anzahl Ausgabe-Dimensionen (VQ+MQ+TA) |
| `--reward_token` | `"special"` | Special Token für Reward-Ausgabe |
| `--use_tied_data` | `True` | Tied Data für Training |
| `--learning_rate` | `2e-6` | Lernrate |
| `--per_device_train_batch_size` | `1` | Batch-Size pro GPU |
| `--gradient_accumulation_steps` | `4` | Gradient Accumulation |

### DeepSpeed Konfigurationen

| Config | Beschreibung |
|--------|-------------|
| `ds_config/zero0.json` | ZeRO Stage 0 (Standard) |
| `ds_config/zero2.json` | ZeRO Stage 2 |
| `ds_config/zero3.json` | ZeRO Stage 3 (maximale GPU-Effizienz) |

## Prompt-Evaluierungs-Sets (`datasets/video_eval_prompts/`)

| Dataset | Prompts | Beschreibung |
|---------|---------|-------------|
| `vbench.csv` | 946 | VBench-Benchmark (rewritten) |
| `videogen_eval.csv` | 400 | VideoGen-Eval für Allzweck-Evaluation |
| `ta_hard.csv` | 72 | TA-Hard: GPT-4o generiert, schwierige Fälle (2 Subjekte + ungewöhnliche Aktionen) |

Alle Prompts enthalten **Englisch + Chinesisch**.

## Prompt-Templates

VideoReward unterstützt 5 Prompt-Template-Typen:

| `template_type` | Beschreibung |
|-----------------|-------------|
| `"none"` | Nur Text-Prompt, kein Template |
| `"simple"` | Kurzes Bewertungs-Prompt |
| `"video_score"` | VideoScore-Stil (1.0–5.0 Score) |
| `"detailed_special"` | Ausführlich + Special Tokens `<\|VQ_reward\|>` etc. |
| `"detailed"` | Ausführlich ohne Special Tokens |

Standard für Training: `"detailed_special"` (mit `<|VQ_reward|>`, `<|MQ_reward|>`, `<|TA_reward|>` Tokens).

## Architektur

```
Video + Text-Prompt
        │
Qwen2-VL-2B-Instruct (VLM)
  + LoRA Fine-Tuning
  + Reward Head (rm_head)
  + Special Reward Tokens
        │
Scores: VQ, MQ, TA (je 0–10)
        │
    Overall = VQ + MQ + TA
```

**Basismodell**: [Qwen/Qwen2-VL-2B-Instruct](https://huggingface.co/Qwen/Qwen2-VL-2B-Instruct)  
**Training-Framework**: TRL + Qwen2-VL-Finetune  
**Loss**: BTT (Bradley-Terry-Thurstone) — Pairwise Preference Learning  

## Flow-DPO

Für Flow-DPO (Text-to-Image) separates Repository: [flow_grpo](https://github.com/yifan123/flow_grpo/blob/main/scripts/single_node/dpo.sh)

## Verwandte Projekte (KlingAI / KwaiVGI)

- [ReCamMaster](https://github.com/KlingAIResearch/ReCamMaster) — Video Re-Rendering (ICCV 2025 Oral)
- [SynCamMaster](https://github.com/KlingAIResearch/SynCamMaster) — Multi-Kamera Video (ICLR 2025)
- [GameFactory](https://github.com/KlingAIResearch/GameFactory) — Game Video Generation
- [LivePortrait](https://github.com/KlingAIResearch/LivePortrait) — Portrait Animation

## Referenzen

- Paper: [arXiv 2501.13918](https://arxiv.org/abs/2501.13918) — Improving Video Generation with Human Feedback
- Projektseite: https://gongyeliu.github.io/videoalign/
- GitHub: https://github.com/KlingAIResearch/VideoAlign
- Checkpoint: https://huggingface.co/KwaiVGI/VideoReward
- Eval Dataset: https://huggingface.co/datasets/KwaiVGI/VideoGen-RewardBench
- Leaderboard: https://huggingface.co/spaces/KwaiVGI/VideoGen-RewardBench
