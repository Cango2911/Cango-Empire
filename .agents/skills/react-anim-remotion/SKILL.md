---
name: react-anim-remotion
description: Remotion — Videos programmatisch mit React erstellen. Nutze diesen Skill wenn du animierte Videos, Erklärvideos, Datenvisualisierungen als Video, YouTube-Content oder personalisierte Videos mit React/HTML/CSS/SVG/WebGL erstellen willst. Frames werden zu echten MP4-Dateien gerendert. Kostenlos für Einzelpersonen.
license: Remotion License (kostenlos für Einzelpersonen, Firmenlizenz für Unternehmen)
metadata:
  author: remotion-dev
  source: https://github.com/remotion-dev/remotion
  docs: https://www.remotion.dev/docs
  npm: remotion
  stars: "18.1K"
  weekly_downloads: "34K"
compatibility: Claude Code, any AI coding agent
allowed-tools: Bash, Read, Write, Edit
---

# Remotion — Videos mit React erstellen

Framework zum programmatischen Erstellen von Videos mit React. Nutzt alle Web-Technologien (HTML, CSS, SVG, Canvas, WebGL) und rendert Frames zu echten Video-Dateien.

## Projekt starten

```bash
npx create-video@latest
```

## Kernkonzepte

### Composition — Video-Komposition definieren

```jsx
import { Composition } from 'remotion'

export const RemotionRoot = () => (
  <>
    <Composition
      id="MyVideo"
      component={MyVideoComponent}
      durationInFrames={150}   // 5 Sekunden bei 30fps
      fps={30}
      width={1920}
      height={1080}
    />
  </>
)
```

### useCurrentFrame — Frame-basierte Animationen

```jsx
import { useCurrentFrame, useVideoConfig, interpolate } from 'remotion'

function MyVideoComponent() {
  const frame = useCurrentFrame()
  const { durationInFrames, fps } = useVideoConfig()

  // Opacity von 0 auf 1 in den ersten 30 Frames
  const opacity = interpolate(frame, [0, 30], [0, 1], {
    extrapolateRight: 'clamp',
  })

  return (
    <div style={{ opacity, fontSize: 80, color: 'white' }}>
      Hallo Welt!
    </div>
  )
}
```

### interpolate — Werte über Zeit interpolieren

```jsx
import { interpolate } from 'remotion'

// frame 0-30: opacity 0→1, danach bleibt 1
const opacity = interpolate(frame, [0, 30], [0, 1], {
  extrapolateLeft: 'clamp',
  extrapolateRight: 'clamp',
})

// x-Position: frame 0 → x=0, frame 60 → x=500
const x = interpolate(frame, [0, 60], [0, 500])
```

### spring — Physikalische Feder-Animation

```jsx
import { spring, useCurrentFrame, useVideoConfig } from 'remotion'

function SpringBox() {
  const frame = useCurrentFrame()
  const { fps } = useVideoConfig()

  const scale = spring({
    frame,
    fps,
    config: { damping: 10, stiffness: 100, mass: 0.5 },
    from: 0,
    to: 1,
  })

  return <div style={{ transform: `scale(${scale})` }}>Box</div>
}
```

### Sequencing — Elemente zeitlich anordnen

```jsx
import { Sequence } from 'remotion'

function MyVideo() {
  return (
    <>
      {/* Startet bei Frame 0, dauert 60 Frames */}
      <Sequence from={0} durationInFrames={60}>
        <Title />
      </Sequence>

      {/* Startet bei Frame 30 (Überlappung möglich) */}
      <Sequence from={30} durationInFrames={90}>
        <Content />
      </Sequence>
    </>
  )
}
```

### Audio & Video einbetten

```jsx
import { Audio, Video, staticFile } from 'remotion'

function WithMedia() {
  return (
    <>
      <Audio src={staticFile('background.mp3')} volume={0.5} />
      <Video src={staticFile('clip.mp4')} />
    </>
  )
}
```

### AbsoluteFill — Vollbild-Container

```jsx
import { AbsoluteFill } from 'remotion'

function FullscreenOverlay() {
  return (
    <AbsoluteFill style={{ backgroundColor: 'rgba(0,0,0,0.5)' }}>
      <h1>Overlay Text</h1>
    </AbsoluteFill>
  )
}
```

## Rendern

```bash
# Vorschau im Browser
npx remotion studio

# Video rendern
npx remotion render MyVideo output.mp4

# Einzelnen Frame rendern
npx remotion still MyVideo --frame=30 frame.png

# Serverless rendern (Lambda)
npx remotion lambda render
```

## Typische Auflösungen

| Format | Breite | Höhe | FPS |
|--------|--------|------|-----|
| YouTube 1080p | 1920 | 1080 | 30 |
| YouTube 4K | 3840 | 2160 | 30 |
| Instagram Story | 1080 | 1920 | 30 |
| Twitter/X | 1280 | 720 | 30 |
| Square | 1080 | 1080 | 30 |

## Lizenz
Kostenlos für Einzelpersonen. Firmen benötigen eine Unternehmenslizenz.
Docs: https://www.remotion.dev/docs
