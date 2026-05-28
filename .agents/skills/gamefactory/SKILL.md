---
name: gamefactory
version: 1.0.0
description: "GameFactory — Creating New Games with Generative Interactive Videos. Framework für action-controllable Game-Video-Generierung via Pre-trained T2V-Modelle. GF-Minecraft Dataset: 70h Gameplay, 2000+ Clips. Utility-Scripts: Invalid-Jump/Collision-Detection, Action-Visualisierung (WASD + Maus)."
author: KlingAIResearch / KwaiVGI (Kuaishou Technology, University of Hong Kong)
source: https://github.com/KlingAIResearch/GameFactory
license: MIT
type: agent-skill
tags:
  - game-generation
  - world-model
  - video-generation
  - minecraft
  - action-control
  - dataset
---

# GameFactory — Generative Interactive Game Video Creation

## Was ist GameFactory?

GameFactory ist ein Framework von Kuaishou Technology / University of Hong Kong (arXiv 2025), das **neue Spiele durch generative interaktive Videos** erschafft. Es kombiniert die offene Generierungskraft vortrainierter T2V-Modelle mit einem Action-Control-Modul — trainiert auf dem **GF-Minecraft Dataset**.

**Kernidee**: Spielstil-Lernen und Action-Kontrolle werden entkoppelt. Das Modell lernt Actions aus einem kleinen, hochwertigen Dataset, während die visuelle Generalisierung vom vortrainierten T2V-Modell kommt. Dadurch kann GameFactory Actions auf neue Spielumgebungen (jenseits von Minecraft) übertragen.

**Potenzial als World Model**: Autonomes Fahren, Embodied AI — Actions aus Spielen auf reale Domänen generalisieren.

**Hinweis**: Das Trainings-/Inferenz-Code ist nicht open-source (Firmen-Policy). Das Repository enthält das Dataset und Utility-Scripts.

## GF-Minecraft Dataset

### Überblick

| Eigenschaft | Wert |
|-------------|------|
| Gesamtdauer | 70 Stunden Gameplay-Video |
| Video-Clips | 2.000+ |
| Frames/Clip | 2.000 Frames |
| Biome | Forest, Plains, Desert |
| Wetter | Clear, Rain, Thunder |
| Tageszeiten | 6 (Sunrise, Noon, Sunset, Night-Start, Midnight, Dawn) |
| Plattform | Minecraft (MineDojo API) |
| Annotierung | MiniCPM-V (multimodal LLM) |

**Download**: [HuggingFace Dataset](https://huggingface.co/datasets/KwaiVGI/GameFactory-Dataset)

### Dataset-Teile

| Ordner | Inhalt | Actions |
|--------|--------|---------|
| `data_2003/` | 2003 Clips — erster Teil | Maus + Tastatur |
| `data_269/` | 269 Clips — zweiter Teil | Nur Tastatur |

### Dataset entpacken

```bash
# data_2003/ (mehrteilig):
cd GF-Minecraft/data_2003
cat part_* > data_2003.zip
unzip data_2003.zip

# data_269/:
unzip data_269.zip
```

### Dataset-Struktur

```
GF-Minecraft/
├── data_2003/
│   ├── annotation.csv          # Textbeschreibungen aller Clips
│   ├── metadata/
│   │   ├── seed_1_part_1.json  # Action-Sequenzen pro Clip
│   │   └── ...
│   └── video/
│       ├── seed_1_part_1.mp4   # 2000-Frame-Videos
│       └── ...
└── data_269/
    ├── annotation.csv
    ├── metadata/ + video/
```

`annotation.csv` Spalten: `original_video_name`, `start_frame_index`, `end_frame_index`, `prompt`

### Action-Format (JSON Metadata)

Jedes JSON enthält Kontext + `actions`-Dictionary (Index 0–1999):

```json
{
  "biome": "plains",
  "initial_weather": "rain",
  "start_time": "Sunset",
  "actions": {
    "1": {
      "ws": 2,      // 0=still, 1=vorwärts(W), 2=rückwärts(S)
      "ad": 1,      // 0=still, 1=links(A), 2=rechts(D)
      "scs": 3,     // 0=nichts, 1=jump(Space), 2=sneak(Shift), 3=sprint(Ctrl)
      "pitch": 0.0,        // Kamera vertikal (absolut)
      "yaw": 0.0,          // Kamera horizontal (absolut)
      "pitch_delta": 0.0,  // Delta × 15 = Grad
      "yaw_delta": 0.0,
      "pos": [-228.5, 75.0, 246.4]  // 3D-Weltposition [x, y, z]
    }
  }
}
```

**Wichtig**: `"0"`-Eintrag ignorieren — entspricht keinem Video-Frame. Frames 1–1999 = Actions 1–1999.

**Delta-Konvertierung**: `pitch_delta` / `yaw_delta` × 15 = Kamerawinkel in Grad.

## Utility Scripts

### 1. Invalid Jump & Collision Detection (`detection.py`)

Verarbeitet alle JSON-Dateien im `metadata/`-Verzeichnis und ergänzt:
- `collision`: 1 wenn Agent mit Hindernis kollidiert (x/z-Delta unter Threshold)
- `jump_invalid`: 1 wenn Jump-Action ineffektiv (Agent bereits in der Luft, kein Höhenzuwachs)
- `delta_pos`: Positionsdifferenz zum vorherigen Frame

```bash
python detection.py --dir_name /path/to/dataset_split

# Mit angepassten Thresholds:
python detection.py \
  --dir_name /path/to/dataset_split \
  --threshold 0.01 \
  --height_threshold 0.01
```

**Eingabe**: Verzeichnis mit `video/` + `metadata/`  
**Ausgabe**: `metadata-detection/` (neue JSON-Dateien mit Detection-Feldern)

**Warum wichtig?**
- **Invalid Jumps**: Mehrere konsekutive Jump-Frames = Agent bereits in der Luft → ungültig. Bereinigung vereinfacht das Modelltraining.
- **Collisions**: Kollisionen als einzigartiges Action-Signal → besseres Verstehen von Umgebungsconstraints.

### 2. Action Visualization (`visualize.py`)

Überlagert Input-Video mit WASD-Tasten-Overlay + Maus-Cursor-Animation.

```bash
python visualize.py
```

Action-Config Format:
```python
# [[end_frame, "w s a d shift ctrl collision delta_pitch delta_yaw"], ..., "space_frames"]
selected_config = [
    [25, "0 0 0 0 0 0 0 0 0.5"],   # Bis Frame 25: nur Maus-Bewegung
    [77, "1 0 0 0 0 0 0 0 0"],     # Frame 26–77: vorwärts (W)
    "15 30 50"                      # Jump (Space) bei Frame 15, 30, 50
]
```

Output: `output.mp4` mit Tasten-Overlay (grün = gedrückt, grau = nicht gedrückt) + Maus-Cursor.

#### Config-Parameter anpassen

In `visualize.py`:
```python
mouse_icon_path = "./mouse.png"
input_video  = "./input.mp4"
output_video = "./output.mp4"
selected_config = [[...], "..."]
process_video(input_video, output_video, selected_config,
              mouse_icon_path,
              mouse_scale=0.2,     # Maus-Cursor-Größe
              mouse_rotation=-20)  # Maus-Cursor-Rotation
```

## Action-String-Format

Visualize-Script verwendet `"w s a d shift ctrl collision delta_pitch delta_yaw"`:

| Position | Key | Werte |
|----------|-----|-------|
| 1 | W (vorwärts) | 0/1 |
| 2 | S (rückwärts) | 0/1 |
| 3 | A (links) | 0/1 |
| 4 | D (rechts) | 0/1 |
| 5 | Shift (sneak) | 0/1 |
| 6 | Ctrl (sprint) | 0/1 |
| 7 | Collision | 0/1 |
| 8 | delta_pitch | Float (×15 = Grad) |
| 9 | delta_yaw | Float (×15 = Grad) |

## Training (Nicht open-source)

Das Modell-Training ist nicht veröffentlicht (Firmen-Policy von Kuaishou). Für Batch-Inferenz-Anfragen: E-Mail an [jianhongbai@zju.edu.cn](mailto:jianhongbai@zju.edu.cn).

**Multi-Phase Training-Strategie**:
1. Vortrainiertes T2V-Modell einfrieren
2. Action-Control-Modul auf GF-Minecraft Dataset trainieren
3. → Decoupling von Spielstil und Action-Kontrolle

## Use Cases

| Use Case | Beschreibung |
|----------|-------------|
| **Game Video Generation** | Neue Spielumgebungen mit kontrollierten Actions generieren |
| **World Model** | Aktionen auf neue Domänen generalisieren (Autonomes Fahren, Embodied AI) |
| **Dataset-Nutzung** | GF-Minecraft für eigene Action-Control-Modelle |
| **Action Visualization** | Gameplay-Videos mit Action-Overlay annotieren |
| **Data Cleaning** | Invalid Jumps + Kollisionen im Dataset detektieren |

## Verwandte Projekte (KlingAI / KwaiVGI)

- [ReCamMaster](https://github.com/KlingAIResearch/ReCamMaster) — Video Re-Rendering (ICCV 2025 Oral)
- [SynCamMaster](https://github.com/KlingAIResearch/SynCamMaster) — Multi-Kamera Video (ICLR 2025)
- [LivePortrait](https://github.com/KlingAIResearch/LivePortrait) — Portrait Animation

## Referenzen

- Paper: [arXiv 2501.08325](https://arxiv.org/abs/2501.08325) — GameFactory: Creating New Games with Generative Interactive Videos
- Projektseite: https://yujiwen.github.io/gamefactory/
- GitHub: https://github.com/KlingAIResearch/GameFactory
- Dataset: https://huggingface.co/datasets/KwaiVGI/GameFactory-Dataset
