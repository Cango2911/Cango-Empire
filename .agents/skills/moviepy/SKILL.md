---
name: moviepy
version: 2.2.0
description: "MoviePy v2 — Python Video Editing Library. Schneiden, Verketten, Compositing, Textoverlay, Effekte, Audio-Editing, GIF-Export. Vollständige API für Video/Audio-Clips mit 34 Video-FX, 7 Audio-FX. FFmpeg-basiert, numpy-Arrays für pixel-genaue Kontrolle."
author: Zulko et al. (Open Source, MIT)
source: https://github.com/Zulko/moviepy
license: MIT
type: agent-skill
tags:
  - video-editing
  - python
  - ffmpeg
  - compositing
  - effects
  - audio
  - gif
---

# MoviePy v2 — Python Video Editing

## Was ist MoviePy?

MoviePy ist eine Python-Bibliothek für programmatisches Video-Editing: Schneiden, Verketten, Compositing, Textüberlagerungen, Effekte, Audio-Bearbeitung und GIF-Export. Unter der Haube werden alle Frames als numpy-Arrays verarbeitet — jeder Pixel ist direkt zugänglich.

**Version**: 2.0+ (Breaking Changes gegenüber v1 — [Migration Guide](https://zulko.github.io/moviepy/getting_started/updating_to_v2.html))  
**Docs**: https://zulko.github.io/moviepy/  
**Install**: `pip install moviepy`

## Installation

```bash
pip install moviepy

# Für Entwicklung:
pip install -e ".[doc,test,lint]"
```

**Dependencies**: `imageio`, `imageio_ffmpeg`, `numpy`, `pillow`, `opencv-python-headless`, `decorator`, `proglog`, `python-dotenv`

## Schnellstart

```python
from moviepy import VideoFileClip, TextClip, CompositeVideoClip

# Video laden, zuschneiden, Audio anpassen
clip = (
    VideoFileClip("video.mp4")
    .subclipped(10, 20)          # Sekunden 10–20
    .with_volume_scaled(0.8)     # Lautstärke 80%
)

# Textoverlay erstellen
txt = (
    TextClip(font="Arial.ttf", text="Hello!", font_size=70, color="white")
    .with_duration(10)
    .with_position("center")
)

# Compositing
final = CompositeVideoClip([clip, txt])
final.write_videofile("result.mp4")
```

## Kern-Klassen

### VideoClip / VideoFileClip

```python
from moviepy import VideoFileClip, ImageClip, ColorClip

# Datei laden
clip = VideoFileClip("video.mp4")
print(clip.duration, clip.fps, clip.size)   # Dauer, FPS, (width, height)

# Standbild
img = ImageClip("photo.jpg").with_duration(5)

# Farb-Clip (Hintergrund)
bg = ColorClip(size=(1920, 1080), color=(0, 0, 0), duration=10)
```

### AudioClip / AudioFileClip

```python
from moviepy import AudioFileClip

audio = AudioFileClip("music.mp3")
clip = clip.with_audio(audio)
clip = clip.without_audio()   # Audio entfernen
```

### TextClip

```python
from moviepy import TextClip

txt = TextClip(
    font="Arial.ttf",           # Pfad zur Schriftdatei
    text="Mein Text",
    font_size=60,
    color="white",
    stroke_color="black",
    stroke_width=2,
    method="caption",           # "label" (standard) oder "caption" (Zeilenumbruch)
    size=(640, None),           # Breite fixiert, Höhe auto
    duration=5,
)
```

## Clip-Methoden (Chaining)

```python
clip = VideoFileClip("video.mp4")

# Zeitsteuerung
clip.subclipped(start=2, end=8)     # Start/End in Sekunden oder "00:00:02"
clip.with_start(5)                   # Clip beginnt bei t=5s im Timeline
clip.with_end(10)
clip.with_duration(6)

# Transformationen
clip.resized(width=1280)             # Breite fixiert, Höhe proportional
clip.resized((1920, 1080))           # Exakte Größe
clip.cropped(x1=100, y1=50, x2=700, y2=400)
clip.rotated(45)                     # Rotation in Grad
clip.with_position(("center", "bottom"))
clip.with_position(lambda t: (t*10, 50))  # Animierte Position

# Audio
clip.with_volume_scaled(0.5)
clip.with_audio(audio_clip)
clip.without_audio()

# FPS / Zeitsteuerung
clip.with_fps(30)
clip.with_speed_scaled(2.0)          # 2× beschleunigen
clip.time_transform(lambda t: t * 2) # Custom Zeit-Mapping
```

## Compositing

```python
from moviepy import CompositeVideoClip, concatenate_videoclips, clips_array

# Clips übereinanderlegen (letzter = vorderste Ebene)
composite = CompositeVideoClip([background, overlay, text_clip])

# Hintereinander abspielen
sequence = concatenate_videoclips([clip1, clip2, clip3])

# Nebeneinander / Grid
grid = clips_array([[clip1, clip2], [clip3, clip4]])
```

## Video-Effekte (34 FX)

Alle Effekte werden mit `.with_effects([Effect(...)])` angewendet:

```python
from moviepy.video.fx import (
    FadeIn, FadeOut, CrossFadeIn, CrossFadeOut,
    BlackAndWhite, GammaCorrection, LumContrast,
    Crop, Resize, Rotate, MirrorX, MirrorY,
    Blur, HeadBlur, InvertColors, Painting,
    MultiplySpeed, MultiplyColor,
    Scroll, SlideIn, SlideOut, Freeze, Blink,
    Loop, MakeLoopable, TimeMirror, TimeSymmetrize,
    Margin, AccelDecel, EvenSize, SuperSample,
    MaskColor, MasksAnd, MasksOr, FreezeRegion,
)

clip = clip.with_effects([
    FadeIn(1),           # 1 Sekunde Fade-In
    FadeOut(0.5),        # 0.5s Fade-Out
    BlackAndWhite(),     # Schwarz/Weiß
    Resize(width=720),   # Größe ändern
    Rotate(90),          # Drehen
    Loop(n=3),           # 3× loopen
])
```

### Wichtige Video-FX im Detail

| Effekt | Parameter | Beschreibung |
|--------|-----------|-------------|
| `FadeIn(t)` | Dauer in s | Einblenden |
| `FadeOut(t)` | Dauer in s | Ausblenden |
| `CrossFadeIn(t)` | Dauer in s | Cross-Fade beim Einblenden |
| `Crop(x1,y1,x2,y2)` | Pixel-Koordinaten | Ausschnitt |
| `Resize(w,h)` | width/height | Größe ändern |
| `Rotate(angle)` | Grad | Rotation |
| `MirrorX()` / `MirrorY()` | — | Spiegeln |
| `BlackAndWhite()` | — | Graustufen |
| `GammaCorrection(gamma)` | Float | Helligkeit (gamma=2.0 = heller) |
| `LumContrast(lum, contrast)` | Float | Helligkeit + Kontrast |
| `MultiplySpeed(factor)` | Float | Geschwindigkeit (2.0 = 2× schneller) |
| `MultiplyColor(factor)` | Float | Farb-Intensität |
| `SlideIn(t, side)` | Dauer, "left"/"right"/"top"/"bottom" | Einfahren |
| `SlideOut(t, side)` | Dauer, Seite | Ausfahren |
| `Scroll(speed_x, speed_y)` | Float | Scrollen |
| `Freeze(t)` | Sekunde | Frame einfrieren |
| `Loop(n)` | Anzahl | Video loopen |
| `TimeMirror()` | — | Zeitlich spiegeln (rückwärts) |
| `Margin(margin, color)` | Pixel, RGB | Rand hinzufügen |
| `Painting(saturation)` | Float | Gemälde-Effekt |
| `InvertColors()` | — | Farben invertieren |
| `Blink(on, off)` | Sekunden | Blinken |
| `SuperSample(d, n_frames)` | — | Anti-Aliasing |
| `HeadBlur(x,y,r)` | Koordinaten + Radius | Kopf/Gesicht blurren |

## Audio-Effekte (7 FX)

```python
from moviepy.audio.fx import (
    AudioFadeIn, AudioFadeOut, AudioNormalize,
    AudioDelay, AudioLoop,
    MultiplyVolume, MultiplyStereoVolume,
)

audio = audio.with_effects([
    AudioFadeIn(2),           # 2s Fade-In
    AudioFadeOut(1),          # 1s Fade-Out
    AudioNormalize(),         # Lautstärke normalisieren
    MultiplyVolume(0.5),      # Lautstärke halbieren
    AudioDelay(0.5, n=3),     # Echo-Effekt
    AudioLoop(n=3),           # 3× loopen
    MultiplyStereoVolume(left=1.0, right=0.5),  # Stereo-Balance
])
```

## Export

```python
# MP4 exportieren
clip.write_videofile(
    "output.mp4",
    fps=30,
    codec="libx264",         # "libx264", "libx265", "libvpx-vp9"
    audio_codec="aac",       # "aac", "mp3", "libvorbis"
    bitrate="5000k",
    preset="medium",         # "ultrafast" … "veryslow"
    threads=4,
    logger="bar",            # "bar" (Fortschrittsbalken) oder None
)

# GIF exportieren
clip.write_gif("output.gif", fps=10)

# Nur Audio exportieren
clip.audio.write_audiofile("output.mp3")

# Einzelnen Frame exportieren
clip.save_frame("frame.png", t=5.5)   # Frame bei t=5.5s
```

## FFmpeg-Tools

```python
from moviepy.video.io.ffmpeg_tools import (
    ffmpeg_extract_subclip,
    ffmpeg_merge_video_audio,
    ffmpeg_version,
)

# Subclip direkt mit FFmpeg (schnell, kein Re-Encoding)
ffmpeg_extract_subclip("video.mp4", start_time=10, end_time=20, targetname="sub.mp4")

# Video + Audio zusammenführen
ffmpeg_merge_video_audio("video.mp4", "audio.mp3", "merged.mp4")

# FFmpeg-Version
full, numeric = ffmpeg_version()
print(f"FFmpeg {numeric}")
```

## Eigene Effekte erstellen

```python
from moviepy import Effect
import numpy as np

class Pixelate(Effect):
    """Pixelisierungs-Effekt."""
    def __init__(self, pixel_size=10):
        self.pixel_size = pixel_size

    def apply(self, clip):
        def filter_frame(frame):
            p = self.pixel_size
            # Frame verkleinern + hochskalieren
            small = frame[::p, ::p]
            return np.repeat(np.repeat(small, p, axis=0), p, axis=1)[:frame.shape[0], :frame.shape[1]]
        return clip.image_transform(filter_frame)

clip = clip.with_effects([Pixelate(pixel_size=20)])
```

## Jupyter Notebook Vorschau

```python
from moviepy import ipython_display
ipython_display(clip, fps=15, width=480)
```

## Häufige Anwendungsfälle

### Talking Head Video (Untertitel)

```python
from moviepy import VideoFileClip, TextClip, CompositeVideoClip

clip = VideoFileClip("interview.mp4")
sub = (
    TextClip(font="Arial.ttf", text="Das ist ein Untertitel", font_size=40,
             color="white", stroke_color="black", stroke_width=2, method="caption",
             size=(clip.w - 100, None))
    .with_position(("center", 0.85), relative=True)
    .with_duration(clip.duration)
)
CompositeVideoClip([clip, sub]).write_videofile("with_subtitles.mp4")
```

### Intro + Outro + Hauptvideo

```python
from moviepy import VideoFileClip, concatenate_videoclips
from moviepy.video.fx import FadeIn, FadeOut, CrossFadeIn

intro = VideoFileClip("intro.mp4")
main  = VideoFileClip("main.mp4").with_effects([FadeIn(0.5), FadeOut(0.5)])
outro = VideoFileClip("outro.mp4").with_effects([CrossFadeIn(1)])

final = concatenate_videoclips([intro, main, outro], method="compose")
final.write_videofile("full_video.mp4")
```

### Highlight-Reel (mehrere Clips zusammenführen)

```python
clips = [
    VideoFileClip("clip1.mp4").subclipped(0, 5),
    VideoFileClip("clip2.mp4").subclipped(10, 15),
    VideoFileClip("clip3.mp4").subclipped(2, 8),
]
highlight = concatenate_videoclips(clips)
highlight.write_videofile("highlight.mp4", fps=30)
```

### GIF aus Video-Clip

```python
VideoFileClip("video.mp4").subclipped(5, 8).resized(width=480).write_gif("clip.gif", fps=15)
```

## Migration von v1 → v2

| v1 | v2 |
|----|-----|
| `clip.fl_image(func)` | `clip.image_transform(func)` |
| `clip.fl_time(func)` | `clip.time_transform(func)` |
| `clip.fl(func)` | `clip.transform(func)` |
| `clip.fx(effect, args)` | `clip.with_effects([Effect(args)])` |
| `clip.set_duration(t)` | `clip.with_duration(t)` |
| `clip.set_fps(fps)` | `clip.with_fps(fps)` |
| `clip.set_start(t)` | `clip.with_start(t)` |
| `clip.set_audio(audio)` | `clip.with_audio(audio)` |
| `clip.resize(w)` | `clip.resized(w)` |
| `clip.crop(x1,y1)` | `clip.cropped(x1,y1)` |
| `clip.rotate(a)` | `clip.rotated(a)` |
| `clip.subclip(s,e)` | `clip.subclipped(s,e)` |
| `clip.cutout(s,e)` | `clip.with_section_cut_out(s,e)` |
| `TextClip(txt, fontsize=)` | `TextClip(text=, font_size=)` |

## Referenzen

- Docs: https://zulko.github.io/moviepy/
- GitHub: https://github.com/Zulko/moviepy
- PyPI: https://pypi.org/project/moviepy/
- v1 Docs (legacy): https://zulko.github.io/moviepy/v1.0.3/
- Reddit: https://www.reddit.com/r/moviepy/
