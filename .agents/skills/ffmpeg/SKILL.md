---
name: ffmpeg
version: 8.0
description: "FFmpeg — Multimedia-Framework für Audio/Video-Verarbeitung (LGPL/GPL). Drei CLI-Tools: ffmpeg (konvertieren/filtern/streamen), ffprobe (analysieren), ffplay (abspielen). Sieben Bibliotheken: libavcodec, libavformat, libavfilter, libavutil, libavdevice, libswresample, libswscale. Hunderte Codecs, Container, Filter. Python-Integration via subprocess oder python-ffmpeg/ffmpeg-python."
author: FFmpeg Project (Open Source, LGPL/GPL)
source: https://github.com/FFmpeg/FFmpeg
license: LGPL-2.1+ / GPL-2.0+
type: agent-skill
tags:
  - multimedia
  - video
  - audio
  - codec
  - transcoding
  - streaming
  - filters
  - cli
---

# FFmpeg — Multimedia-Framework

## Was ist FFmpeg?

FFmpeg ist das führende Open-Source-Multimedia-Framework für Audio/Video-Verarbeitung. Es enthält:

- **`ffmpeg`** — CLI-Tool: konvertieren, filtern, streamen, transcodieren
- **`ffprobe`** — Analyse-Tool: Metadaten, Streams, Bitrate
- **`ffplay`** — Media-Player (SDL-basiert)
- **Bibliotheken**: libavcodec, libavformat, libavfilter, libavutil, libavdevice, libswresample, libswscale

**Docs**: https://ffmpeg.org/ffmpeg.html  
**Wiki**: https://trac.ffmpeg.org/wiki

## Installation

```bash
# macOS
brew install ffmpeg

# Debian/Ubuntu
sudo apt-get install ffmpeg

# Windows (Chocolatey)
choco install ffmpeg

# Conda
conda install -c conda-forge ffmpeg
```

## Grundstruktur ffmpeg-Kommando

```bash
ffmpeg [globale Optionen] {[Eingabe-Optionen] -i Eingabe} ... {[Ausgabe-Optionen] Ausgabe} ...
```

## ffprobe — Medien analysieren

```bash
# Überblick über Datei
ffprobe -v quiet -print_format json -show_format -show_streams input.mp4

# Nur Format-Info
ffprobe -v quiet -show_format -print_format json input.mp4

# Video-Stream-Info
ffprobe -v error -select_streams v:0 -show_entries stream=codec_name,width,height,r_frame_rate,bit_rate -of json input.mp4

# Dauer in Sekunden
ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 input.mp4
```

## Format-Konvertierung

```bash
# MP4 → MKV (Container-Wechsel, Stream-Copy)
ffmpeg -i input.mp4 -c copy output.mkv

# Video → GIF
ffmpeg -i input.mp4 -vf "fps=15,scale=480:-1:flags=lanczos" output.gif

# Video → WebM (VP9)
ffmpeg -i input.mp4 -c:v libvpx-vp9 -cq 30 -b:v 0 -c:a libopus -b:a 128k output.webm

# Audio extrahieren (MP3)
ffmpeg -i input.mp4 -vn -c:a libmp3lame -q:a 2 output.mp3

# Audio extrahieren (AAC/m4a)
ffmpeg -i input.mp4 -vn -c:a aac -b:a 192k output.m4a

# Bild-Sequenz → Video
ffmpeg -framerate 24 -i frame_%04d.png -c:v libx264 -pix_fmt yuv420p output.mp4

# Video → Bild-Sequenz
ffmpeg -i input.mp4 -vf "fps=1" frame_%04d.png
```

## Schneiden & Trimmen

```bash
# Trimmen (Start + Dauer) — schnell, vor -i
ffmpeg -ss 00:01:30 -t 00:00:45 -i input.mp4 -c copy output.mp4

# Trimmen (Start + Ende) — genau, nach -i
ffmpeg -i input.mp4 -ss 00:01:30 -to 00:02:15 -c:v libx264 -c:a copy output.mp4

# Erstes Standbild extrahieren
ffmpeg -i input.mp4 -vframes 1 -ss 0 thumbnail.png

# Thumbnail bei Sekunde 10
ffmpeg -ss 10 -i input.mp4 -vframes 1 thumb.jpg
```

## Skalierung & Qualität

```bash
# Skalieren auf Breite 1280 (Höhe proportional)
ffmpeg -i input.mp4 -vf scale=1280:-2 output.mp4

# Skalieren mit lanczos-Filter (höhere Qualität)
ffmpeg -i input.mp4 -vf "scale=1920:1080:flags=lanczos" output.mp4

# CRF (Constant Rate Factor): 0 lossless, 18 visuell verlustfrei, 23 Standard, 51 schlechteste
ffmpeg -i input.mp4 -c:v libx264 -crf 23 -preset slow output.mp4

# Bitrate festlegen
ffmpeg -i input.mp4 -c:v libx264 -b:v 2M -maxrate 2.5M -bufsize 5M output.mp4

# H.265/HEVC (kleinere Dateien, langsamer)
ffmpeg -i input.mp4 -c:v libx265 -crf 28 -c:a aac -b:a 128k output.mp4

# Hardware-Encoding (NVIDIA NVENC)
ffmpeg -i input.mp4 -c:v h264_nvenc -preset p4 -cq 23 output.mp4

# Hardware-Encoding (Apple VideoToolbox)
ffmpeg -i input.mp4 -c:v h264_videotoolbox -b:v 4M output.mp4
```

## Video-Filter (-vf)

Filter werden als DAG (Directed Acyclic Graph) verkettet: `-vf "filter1,filter2,filter3"`

```bash
# Crop: Breite:Höhe:x_offset:y_offset
ffmpeg -i input.mp4 -vf "crop=640:360:100:50" output.mp4

# Flip
ffmpeg -i input.mp4 -vf "hflip" output.mp4   # horizontal
ffmpeg -i input.mp4 -vf "vflip" output.mp4   # vertikal

# Rotation
ffmpeg -i input.mp4 -vf "rotate=PI/4" output.mp4
ffmpeg -i input.mp4 -vf "transpose=1" output.mp4  # 90° im UZS

# Padding (Letterbox)
ffmpeg -i input.mp4 -vf "pad=1920:1080:(ow-iw)/2:(oh-ih)/2:black" output.mp4

# Geschwindigkeit (0.5 = halb so schnell, 2.0 = doppelt)
ffmpeg -i input.mp4 -vf "setpts=0.5*PTS" -af "atempo=2.0" output.mp4

# Deinterlace
ffmpeg -i input.mp4 -vf "yadif" output.mp4

# Denoise
ffmpeg -i input.mp4 -vf "nlmeans" output.mp4

# Unschärfe/Schärfe
ffmpeg -i input.mp4 -vf "unsharp=5:5:1.5" output.mp4

# Sättigung/Helligkeit/Kontrast
ffmpeg -i input.mp4 -vf "eq=brightness=0.1:contrast=1.2:saturation=1.5" output.mp4

# Thumbnail aus besten Frames auswählen
ffmpeg -i input.mp4 -vf "thumbnail=300" -frames:v 1 thumb.jpg

# Watermark (Bild rechts oben)
ffmpeg -i input.mp4 -i watermark.png -filter_complex "overlay=W-w-10:10" output.mp4

# Text-Overlay (drawtext)
ffmpeg -i input.mp4 -vf "drawtext=text='Hello':fontsize=48:fontcolor=white:x=10:y=10" output.mp4

# FPS ändern
ffmpeg -i input.mp4 -vf "fps=30" output.mp4

# Schwarzränder automatisch entfernen (cropdetect → crop)
ffmpeg -i input.mp4 -vf "cropdetect" -f null - 2>&1 | grep crop
ffmpeg -i input.mp4 -vf "crop=1280:720:0:0" output.mp4
```

## Audio-Filter (-af)

```bash
# Lautstärke anpassen (dB oder Faktor)
ffmpeg -i input.mp4 -af "volume=2.0" output.mp4    # × 2
ffmpeg -i input.mp4 -af "volume=6dB" output.mp4    # +6 dB

# Audio normalisieren (EBU R128, -23 LUFS)
ffmpeg -i input.mp4 -af "loudnorm=I=-23:TP=-1.5:LRA=11" output.mp4

# Fadeout am Ende (ab Sekunde 50, 5s Dauer)
ffmpeg -i input.mp4 -af "afade=type=out:start_time=50:duration=5" output.mp4

# Rauschunterdrückung
ffmpeg -i input.mp4 -af "anlmdn" output.mp4

# Equalizer (Bass boost)
ffmpeg -i input.mp4 -af "equalizer=f=100:t=o:w=100:g=5" output.mp4

# Stereo → Mono
ffmpeg -i input.mp4 -af "pan=mono|c0=0.5*c0+0.5*c1" output.mp4

# Samplerate ändern
ffmpeg -i input.mp4 -af "aresample=44100" output.mp4

# Audio-Geschwindigkeit (pitch-preserving)
ffmpeg -i input.mp4 -af "atempo=1.5" output.mp4    # max factor 2.0 je atempo
ffmpeg -i input.mp4 -af "atempo=2.0,atempo=1.5" output.mp4  # 3× beschleunigt
```

## Complex Filtergraph (-filter_complex)

```bash
# Zwei Videos nebeneinander (side by side)
ffmpeg -i left.mp4 -i right.mp4 \
  -filter_complex "[0:v][1:v]hstack=inputs=2[v]" \
  -map "[v]" -map 0:a output.mp4

# Vier Videos in 2×2-Raster
ffmpeg -i a.mp4 -i b.mp4 -i c.mp4 -i d.mp4 \
  -filter_complex "[0:v][1:v]hstack[top];[2:v][3:v]hstack[bot];[top][bot]vstack[v]" \
  -map "[v]" output.mp4

# Videos übereinander (overlay mit Transparenz)
ffmpeg -i background.mp4 -i overlay.png \
  -filter_complex "[0:v][1:v]overlay=x=10:y=10[v]" \
  -map "[v]" -map 0:a output.mp4

# PiP (Picture in Picture)
ffmpeg -i main.mp4 -i pip.mp4 \
  -filter_complex "[1:v]scale=320:-2[small];[0:v][small]overlay=W-w-10:10[v]" \
  -map "[v]" -map 0:a output.mp4

# Split und verschiedene Filter anwenden
ffmpeg -i input.mp4 \
  -filter_complex "[0:v]split=2[original][blurred];[blurred]gblur=sigma=5[blurred_out]" \
  -map "[original]" part_original.mp4 \
  -map "[blurred_out]" part_blurred.mp4
```

## Videos zusammenfügen (Concat)

```bash
# Methode 1: concat demuxer (Stream Copy, schnell)
# Liste erstellen:
printf "file 'part1.mp4'\nfile 'part2.mp4'\nfile 'part3.mp4'\n" > filelist.txt
ffmpeg -f concat -safe 0 -i filelist.txt -c copy output.mp4

# Methode 2: concat filter (Re-encode, flexibler)
ffmpeg -i part1.mp4 -i part2.mp4 \
  -filter_complex "[0:v][0:a][1:v][1:a]concat=n=2:v=1:a=1[v][a]" \
  -map "[v]" -map "[a]" output.mp4
```

## Streaming

```bash
# RTMP-Stream (z.B. zu Twitch)
ffmpeg -i input.mp4 -c:v libx264 -b:v 3M -c:a aac -b:a 128k \
  -f flv rtmp://live.twitch.tv/app/STREAM_KEY

# HLS-Output erzeugen
ffmpeg -i input.mp4 -c:v libx264 -c:a aac \
  -f hls -hls_time 10 -hls_list_size 0 output.m3u8

# UDP-Stream
ffmpeg -i input.mp4 -c:v libx264 -f mpegts udp://192.168.1.100:1234

# Screen Capture (Linux/X11)
ffmpeg -f x11grab -r 25 -s 1920x1080 -i :0.0 output.mp4

# Webcam aufnehmen (Linux)
ffmpeg -f v4l2 -i /dev/video0 -c:v libx264 output.mp4
```

## Python-Integration

### Via subprocess (empfohlen)

```python
import subprocess
import json

def run_ffmpeg(args: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["ffmpeg"] + args,
        check=True,
        capture_output=True,
        text=True
    )

def ffprobe_info(filepath: str) -> dict:
    result = subprocess.run(
        ["ffprobe", "-v", "quiet", "-print_format", "json",
         "-show_format", "-show_streams", filepath],
        check=True, capture_output=True, text=True
    )
    return json.loads(result.stdout)

# Konvertieren
run_ffmpeg(["-i", "input.mp4", "-c:v", "libx264", "-crf", "23", "output.mp4"])

# Trimmen
run_ffmpeg(["-ss", "30", "-t", "60", "-i", "input.mp4", "-c", "copy", "clip.mp4"])

# Thumbnail
run_ffmpeg(["-ss", "5", "-i", "input.mp4", "-vframes", "1", "thumb.jpg"])

# Metadaten lesen
info = ffprobe_info("video.mp4")
duration = float(info["format"]["duration"])
width = info["streams"][0]["width"]
height = info["streams"][0]["height"]
```

### Via python-ffmpeg (typisierte API)

```bash
pip install python-ffmpeg
```

```python
import asyncio
from ffmpeg import FFmpeg, Progress

# Einfache Konvertierung
ffmpeg = (
    FFmpeg()
    .input("input.mp4")
    .output("output.mp4", {"c:v": "libx264", "crf": 23})
)
ffmpeg.execute()

# Mit Progress-Callback
@ffmpeg.on("progress")
def on_progress(progress: Progress):
    print(f"Frame: {progress.frame}, FPS: {progress.fps}, Zeit: {progress.time}")

ffmpeg.execute()

# Async
async def transcode():
    ffmpeg = FFmpeg().input("input.mp4").output("output.mp4")
    await ffmpeg.execute()

asyncio.run(transcode())
```

### Via ffmpeg-python (ältere Alternative)

```bash
pip install ffmpeg-python
```

```python
import ffmpeg

# Pipeline aufbauen
stream = ffmpeg.input("input.mp4")
stream = ffmpeg.filter(stream, "scale", 640, -2)
stream = ffmpeg.output(stream, "output.mp4")
ffmpeg.run(stream)

# Mit Optionen
(
    ffmpeg
    .input("input.mp4", ss=30, t=60)
    .filter("scale", 1280, -2)
    .output("output.mp4", vcodec="libx264", crf=23)
    .run(overwrite_output=True)
)

# Metadaten
probe = ffmpeg.probe("input.mp4")
video_stream = next(s for s in probe["streams"] if s["codec_type"] == "video")
width = video_stream["width"]
height = video_stream["height"]
```

## Wichtige Optionen (Referenz)

| Option | Beschreibung |
|--------|-------------|
| `-i <file>` | Eingabedatei |
| `-c copy` | Stream-Copy (kein Re-encode) |
| `-c:v <codec>` | Video-Codec (libx264, libx265, libvpx-vp9, av1, copy) |
| `-c:a <codec>` | Audio-Codec (aac, libmp3lame, libopus, flac, copy) |
| `-crf <0-51>` | Qualität (H.264/H.265, 0=lossless, 23=Standard) |
| `-b:v <rate>` | Video-Bitrate (z.B. 2M, 500k) |
| `-b:a <rate>` | Audio-Bitrate (z.B. 128k, 192k) |
| `-r <fps>` | Frame-Rate |
| `-s WxH` | Auflösung |
| `-ss <zeit>` | Start-Position (00:01:30 oder 90) |
| `-t <dauer>` | Dauer |
| `-to <zeit>` | End-Position |
| `-vn` | Kein Video |
| `-an` | Kein Audio |
| `-sn` | Keine Untertitel |
| `-map 0` | Alle Streams |
| `-map 0:v:0` | Erster Video-Stream |
| `-vf <filter>` | Video-Filter |
| `-af <filter>` | Audio-Filter |
| `-filter_complex` | Komplexer Multi-Stream-Filter |
| `-preset <p>` | Encoding-Preset (ultrafast→veryslow) |
| `-pix_fmt yuv420p` | Pixel-Format (Kompatibilität) |
| `-movflags faststart` | MP4: Metadaten vorne (für Web-Streaming) |
| `-y` | Ausgabe ohne Rückfrage überschreiben |
| `-n` | Ausgabe nie überschreiben |
| `-v quiet` | Keine Log-Ausgabe |
| `-loglevel error` | Nur Fehler ausgeben |
| `-threads 0` | Alle CPU-Kerne nutzen |

## Codec-Übersicht

### Video-Codecs

| Codec | FFmpeg-Name | Anwendung |
|-------|-------------|-----------|
| H.264 | `libx264` | Standard, beste Kompatibilität |
| H.265/HEVC | `libx265` | 50% kleiner als H.264 |
| AV1 | `libaom-av1`, `libsvtav1` | Modernst, langsam |
| VP9 | `libvpx-vp9` | Web, YouTube |
| VP8 | `libvpx` | Älteres WebM |
| ProRes | `prores_ks` | Apple Editing |
| DNxHD | `dnxhd` | Avid Editing |
| MPEG-4 | `mpeg4` | Ältere Geräte |

### Audio-Codecs

| Codec | FFmpeg-Name | Anwendung |
|-------|-------------|-----------|
| AAC | `aac` | Standard für MP4 |
| MP3 | `libmp3lame` | Universell |
| Opus | `libopus` | Web, VoIP |
| Vorbis | `libvorbis` | OGG |
| FLAC | `flac` | Lossless |
| WAV | `pcm_s16le` | Lossless |
| AC-3 | `ac3` | Dolby |

## Bibliotheken (C-API)

| Bibliothek | Funktion |
|-----------|---------|
| `libavcodec` | Encoder/Decoder für alle Codecs |
| `libavformat` | Container-Formate (MP4, MKV, AVI...) + Demuxer/Muxer |
| `libavfilter` | Audio/Video-Filter-Graph |
| `libavutil` | Hilfsfunktionen (Hash, Mathe, Datenstrukturen) |
| `libavdevice` | Capture-Geräte (Webcam, Screen, ALSA) |
| `libswresample` | Audio-Resampling + Mixing |
| `libswscale` | Bild-Skalierung + Farbraum-Konvertierung |

## Häufige Rezepte

```bash
# Web-optimiertes MP4 (FastStart)
ffmpeg -i input.mp4 -c:v libx264 -crf 23 -preset slow \
  -c:a aac -b:a 128k -movflags faststart output.mp4

# Instagram-Format (1:1, 1080×1080)
ffmpeg -i input.mp4 \
  -vf "scale=1080:1080:force_original_aspect_ratio=decrease,pad=1080:1080:(ow-iw)/2:(oh-ih)/2" \
  -c:v libx264 -crf 23 output.mp4

# Stummschalten und Musik hinzufügen
ffmpeg -i video.mp4 -i music.mp3 -map 0:v -map 1:a \
  -c:v copy -c:a aac -shortest output.mp4

# GIF mit guter Qualität
ffmpeg -i input.mp4 -vf "fps=15,scale=480:-1:flags=lanczos,palettegen" palette.png
ffmpeg -i input.mp4 -i palette.png \
  -vf "fps=15,scale=480:-1:flags=lanczos,paletteuse" output.gif

# Variable Framerate → Konstante Framerate
ffmpeg -i input.mp4 -vf "fps=30" -vsync cfr output.mp4

# Metadaten entfernen
ffmpeg -i input.mp4 -map_metadata -1 -c copy output.mp4

# Zwei Audio-Spuren zusammenführen
ffmpeg -i input.mp4 -filter_complex "[0:a:0][0:a:1]amix=inputs=2[aout]" \
  -map 0:v -map "[aout]" -c:v copy output.mp4
```

## Audio-Normalisierung (normalize.py)

Das Tool `tools/normalize.py` führt automatische EBU R128-Normalisierung durch:

```bash
python tools/normalize.py -i input.mp4 -o output.mp4
python tools/normalize.py -i input.mp4 -o output.mp4 --target-loudness -16  # Streaming
python tools/normalize.py -i input.mp4 -o output.mp4 --dry-run              # Nur Analyse
```

## Referenzen

- Docs: https://ffmpeg.org/ffmpeg.html
- Filter-Doku: https://ffmpeg.org/ffmpeg-filters.html
- Wiki-Rezepte: https://trac.ffmpeg.org/wiki
- Codec-Guide: https://trac.ffmpeg.org/wiki/Encode/H.264
- Python-Binding: https://github.com/livingbio/typed-ffmpeg
