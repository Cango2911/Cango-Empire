---
name: gizeh
version: 0.1.12
description: "gizeh — Cairo-basierte Vektorgrafik-Bibliothek für Python. Surface/PDFSurface als Zeichenfläche, 10 Shape-Funktionen (circle, rectangle, square, arc, polyline, regular_polygon, bezier_curve, ellipse, star, text), immutable Transformationen (rotate/translate/scale), ColorGradient, ImagePattern, Group. Kompatibel mit MoviePy für Animationen."
author: Zulko (Open Source, MIT)
source: https://github.com/Zulko/gizeh
license: MIT
type: agent-skill
tags:
  - cairo
  - vector-graphics
  - svg
  - python
  - animation
  - moviepy
---

# gizeh — Cairo für Touristen

## Was ist gizeh?

gizeh ist eine Python-Bibliothek für Vektorgrafik auf Basis von [`cairocffi`](https://cairocffi.readthedocs.io/) (Cairo-Bindings). Cairo ist mächtig aber komplex; gizeh bietet eine einfache, intuitive API für häufige Zeichenoperationen.

**Install**: `pip install gizeh`  
**Voraussetzung (System)**: Cairo-Bibliothek muss installiert sein  
- macOS: `brew install cairo pkg-config`  
- Debian/Ubuntu: `sudo apt-get install -y libcairo2-dev pkg-config`

## Schnellstart

```python
import gizeh

surface = gizeh.Surface(width=320, height=260)
circle = gizeh.circle(r=30, xy=[40, 40], fill=(1, 0, 0))
circle.draw(surface)
surface.write_to_png("circle.png")
```

## Surface — Zeichenfläche

```python
import gizeh

# Leere Surface erstellen
surface = gizeh.Surface(width=320, height=260)

# Mit Hintergrundfarbe
surface = gizeh.Surface(width=320, height=260, bg_color=(0, 0, 0))

# Aus NumPy-Array erstellen
surface = gizeh.Surface.from_image(numpy_rgb_array)

# Exportieren
surface.write_to_png("output.png")
surface.write_to_png("output.png", y_origin="bottom")  # (0,0) unten-links
arr = surface.get_npimage()                            # (H x W x 3) uint8
arr = surface.get_npimage(transparent=True)            # (H x W x 4) mit Alpha
html = surface.get_html_embed_code()                   # <img src="data:image/png;base64,...">
```

### PDFSurface

```python
surface = gizeh.PDFSurface(filename="output.pdf", width=320, height=260)
circle.draw(surface)
surface.flush()  # Seite finalisieren
```

## Shape-Funktionen

Alle Shapes geben ein `Element`-Objekt zurück. Zeichnen mit `element.draw(surface)`.

### Gemeinsame Parameter

| Parameter | Beschreibung |
|-----------|-------------|
| `xy` | Mittelpunkt `[x, y]` |
| `angle` | Rotation in Radiant um `xy` |
| `fill` | Innenfarbe: RGB, RGBA, Gradient, ImagePattern |
| `stroke` | Konturfarbe: wie `fill` |
| `stroke_width` | Konturbreite in Pixeln (Default: 0) |

### circle

```python
circ = gizeh.circle(r=30, xy=(50, 50), fill=(1, 1, 1))
circ = gizeh.circle(r=30, xy=(50, 50), fill=(1, 0, 0, 0.5), stroke=(0, 0, 0), stroke_width=2)
```

### rectangle

```python
rect = gizeh.rectangle(lx=60, ly=40, xy=(100, 80), fill=(0, 1, 0))
rect = gizeh.rectangle(lx=60, ly=40, xy=(100, 80), fill=(0, 1, 0), angle=3.14/4)
```

### square

```python
sqr = gizeh.square(l=30, xy=(50, 50), fill=(0, 0, 1))
sqr = gizeh.square(l=30, stroke=(1, 1, 1), stroke_width=1.5)
```

### arc

```python
import numpy as np
Pi = np.pi

arc = gizeh.arc(r=40, a1=0, a2=Pi, xy=(100, 100), fill=(1, 0, 1))
arc = gizeh.arc(r=40, a1=Pi/4, a2=3*Pi/4, fill=(1, 1, 0), stroke=(0, 0, 0), stroke_width=2)
```

### polyline

```python
line = gizeh.polyline(
    points=[(0, 0), (20, 30), (40, 40), (0, 10)],
    stroke_width=3,
    stroke=(1, 0, 0),
    fill=(0, 1, 0)
)
```

### regular_polygon

```python
poly = gizeh.regular_polygon(r=40, n=5, angle=np.pi/4, xy=[40, 50], fill=(1, 0, 1))
# r = Umkreisradius, n = Anzahl Ecken, angle = Startwinkel
```

### bezier_curve

```python
bezier = gizeh.bezier_curve(
    points=[(0, 0), (50, 100), (100, 0), (150, 100)],
    stroke_width=2,
    stroke=(1, 0, 0)
)
```

### ellipse

```python
ell = gizeh.ellipse(rx=60, ry=30, xy=(100, 100), fill=(0, 0.5, 1))
ell = gizeh.ellipse(rx=60, ry=30, xy=(100, 100), fill=(0, 0.5, 1), angle=np.pi/6)
```

### star

```python
star = gizeh.star(
    r1=20,     # Innenradius
    r2=40,     # Außenradius
    n=5,       # Anzahl Zacken
    xy=(100, 100),
    fill=(1, 1, 0)
)
```

### text

```python
txt = gizeh.text(
    "Hello World",
    fontfamily="Impact",
    fontsize=40,
    fill=(1, 1, 1),
    xy=(100, 100),
    angle=np.pi/12,
    h_align="center",    # "left", "center", "right"
    v_align="center"     # "top", "center", "bottom"
)
```

## Fill und Stroke

`fill` und `stroke` akzeptieren:

```python
# RGB (Werte 0–1)
fill=(1, 0, 0)

# RGBA (mit Transparenz)
fill=(1, 0, 0, 0.5)

# ColorGradient (linear oder radial)
gradient = gizeh.ColorGradient(
    type="linear",
    begin=(0, 0), end=(100, 100),
    stops_colors=[(0, (1, 0, 0)), (1, (0, 0, 1))]
)

gradient = gizeh.ColorGradient(
    type="radial",
    begin=(50, 50), begin_radius=0,
    end=(50, 50), end_radius=50,
    stops_colors=[(0, (1, 1, 1, 1)), (1, (0, 0, 0, 0))]
)

# ImagePattern (Bild als Füllung)
pattern = gizeh.ImagePattern(surface)          # aus Surface
pattern = gizeh.ImagePattern(numpy_array)      # aus numpy-Array
```

## Transformationen (immutable — geben Kopie zurück)

```python
el = gizeh.circle(r=30, xy=(50, 50), fill=(1, 0, 0))

# Rotation
el2 = el.rotate(angle=np.pi/4)                    # um Ursprung (0,0)
el3 = el.rotate(angle=np.pi/4, center=[50, 50])   # um eigenen Mittelpunkt

# Translation
el4 = el.translate(xy=[20, 30])

# Skalierung
el5 = el.scale(rx=2)                              # gleichmäßig × 2
el6 = el.scale(rx=2, ry=3)                        # x × 2, y × 3
el7 = el.scale(rx=2, center=[50, 50])             # um Zentrum skalieren

# Verkettung möglich
el8 = el.translate([10, 0]).rotate(np.pi/8).scale(1.5)
```

## Group — Elemente gruppieren

```python
square = gizeh.square(l=20, fill=(1, 0, 0), xy=(40, 40))
circle = gizeh.circle(r=20, fill=(1, 1, 0), xy=(50, 30))

group = gizeh.Group([square, circle])

# Gruppe transformieren (alle Elemente bewegen sich zusammen)
group2 = group.translate(xy=[30, 30]).rotate(np.pi/4)

# Verschachtelte Gruppen
group3 = gizeh.Group([circle, group])

surface = gizeh.Surface(width=300, height=200)
group.draw(surface)
group2.draw(surface)
surface.write_to_png("output.png")
```

## MoviePy-Integration für Animationen

gizeh und MoviePy (gleicher Autor) arbeiten nahtlos zusammen:

```python
import gizeh
import moviepy.editor as mpy

def make_frame(t):
    surface = gizeh.Surface(width=400, height=400, bg_color=(0, 0, 0))
    # Animation: Kreis bewegt sich mit Zeit t
    x = 200 + 100 * np.cos(2 * np.pi * t)
    y = 200 + 100 * np.sin(2 * np.pi * t)
    circle = gizeh.circle(r=30, xy=(x, y), fill=(1, 1, 0))
    circle.draw(surface)
    return surface.get_npimage()

clip = mpy.VideoClip(make_frame, duration=2)  # 2 Sekunden
clip.write_videofile("animation.mp4", fps=24)
clip.write_gif("animation.gif", fps=15)
```

## Vollständiges Beispiel — Yin-Yang

```python
import numpy as np
import gizeh

W, H = 300, 300

surface = gizeh.Surface(W, H)

# Hintergrund
gizeh.circle(r=200, xy=(W//2, H//2), fill=(1, 1, 1)).draw(surface)

# Hälften
gizeh.arc(r=100, a1=-np.pi/2, a2=np.pi/2, xy=(W//2, H//2), fill=(0, 0, 0)).draw(surface)
gizeh.circle(r=50, xy=(W//2, H//2 - 50), fill=(0, 0, 0)).draw(surface)
gizeh.circle(r=50, xy=(W//2, H//2 + 50), fill=(1, 1, 1)).draw(surface)
gizeh.circle(r=15, xy=(W//2, H//2 - 50), fill=(1, 1, 1)).draw(surface)
gizeh.circle(r=15, xy=(W//2, H//2 + 50), fill=(0, 0, 0)).draw(surface)

# Umrandung
gizeh.circle(r=100, xy=(W//2, H//2), stroke=(0, 0, 0), stroke_width=3).draw(surface)

surface.write_to_png("yin_yang.png")
```

## Referenzen

- GitHub: https://github.com/Zulko/gizeh
- Blog (Animationen mit MoviePy): http://zulko.github.io/blog/2014/09/20/vector-animations-with-python/
- Cairo: https://www.cairographics.org/
- cairocffi: https://cairocffi.readthedocs.io/
- PyPI: https://pypi.org/project/gizeh/
