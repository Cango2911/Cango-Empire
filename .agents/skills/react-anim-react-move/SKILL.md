---
name: react-anim-react-move
description: React Move — datengetriebene Animationen für React. Nur 3.5kb gzipped. Nutze diesen Skill für präzise Animationen mit fester Dauer, Delay, Easing und Lifecycle-Events (start/interrupt/end). Animiert HTML, SVG und React Native. Ideal für Datenvisualisierungen und D3-Integration. TypeScript-kompatibel.
license: MIT
metadata:
  author: sghall
  source: https://github.com/sghall/react-move
  docs: https://react-move-docs.netlify.app
  npm: react-move
  stars: "6.6K"
  weekly_downloads: "98K"
  size: "3.5kb gzipped"
compatibility: Claude Code, any AI coding agent
allowed-tools: Bash, Read, Write, Edit
---

# React Move

Datengetriebene Animations-Library für React. Nur 3.5kb (gzipped). Klassische CSS-Animations-Logik: Dauer, Delays, Easing-Funktionen und Lifecycle-Events.

## Installation

```bash
npm install react-move

# Optional: D3-Interpolation für Farben, SVG-Transforms
npm install d3-interpolate
```

## Kernkomponenten

### `<Animate>` — Einzelelement animieren

```jsx
import { Animate } from 'react-move'

function AnimatedBox({ show }) {
  return (
    <Animate
      show={show}
      start={() => ({
        opacity: 0,
        x: -100,
      })}
      enter={() => ({
        opacity: [1],           // Zielwert in Array
        x: [0],
        timing: { duration: 500, ease: easeQuadInOut },
      })}
      leave={() => ({
        opacity: [0],
        x: [-100],
        timing: { duration: 300 },
      })}
    >
      {({ opacity, x }) => (
        <div style={{
          opacity,
          transform: `translateX(${x}px)`,
        }}>
          Inhalt
        </div>
      )}
    </Animate>
  )
}
```

### `<NodeGroup>` — Listen/Arrays animieren

```jsx
import { NodeGroup } from 'react-move'
import { easeExpInOut } from 'd3-ease'

function AnimatedList({ data }) {
  return (
    <NodeGroup
      data={data}
      keyAccessor={d => d.id}

      start={(d, i) => ({
        opacity: 0,
        x: -200,
      })}

      enter={(d, i) => ([
        {
          opacity: [0.5],
          timing: { duration: 300 },
        },
        {
          opacity: [1],
          x: [0],
          timing: { delay: i * 50, duration: 500, ease: easeExpInOut },
        },
      ])}

      update={(d) => ({
        opacity: [1],
        x: [d.x],
        timing: { duration: 400 },
      })}

      leave={() => ({
        opacity: [0],
        x: [200],
        timing: { duration: 300 },
      })}
    >
      {nodes => (
        <ul>
          {nodes.map(({ key, data, state: { opacity, x } }) => (
            <li key={key} style={{ opacity, transform: `translateX(${x}px)` }}>
              {data.name}
            </li>
          ))}
        </ul>
      )}
    </NodeGroup>
  )
}
```

## Animation-Objekt Syntax

```jsx
// Einfach: direkt zum Zielwert
enter={() => ({
  opacity: [1],
  timing: { duration: 500 },
})}

// Array von Schritten: Sequenz
enter={() => ([
  {
    opacity: [0.5],
    timing: { duration: 200 },
  },
  {
    opacity: [1],
    timing: { delay: 100, duration: 300 },
  },
])}
```

## Timing-Optionen

```jsx
timing: {
  duration: 500,          // Millisekunden
  delay: 200,             // Verzögerung
  ease: easeQuadInOut,    // D3 Easing-Funktion
}
```

## D3-Easing Funktionen (empfohlen)

```bash
npm install d3-ease
```

```jsx
import {
  easeLinear,
  easeQuadIn, easeQuadOut, easeQuadInOut,
  easeCubicIn, easeCubicOut, easeCubicInOut,
  easeExpIn, easeExpOut, easeExpInOut,
  easeElasticOut,
  easeBounceOut,
  easeBackOut,
} from 'd3-ease'
```

## Mit D3-Interpolation (Farben, SVG-Transforms)

```jsx
import { NodeGroup } from 'react-move'
import { interpolate, interpolateTransformSvg } from 'd3-interpolate'

<NodeGroup
  interpolation={(begValue, endValue, attr) => {
    if (attr === 'transform') return interpolateTransformSvg(begValue, endValue)
    return interpolate(begValue, endValue)
  }}
  // ...
/>
```

## Lifecycle-Events

```jsx
<Animate
  start={...}
  enter={{
    opacity: [1],
    timing: { duration: 500 },
    events: {
      start() { console.log('Animation startet') },
      interrupt() { console.log('Animation unterbrochen') },
      end() { console.log('Animation fertig') },
    },
  }}
/>
```

## Wann React Move wählen?

- Präzise Zeitsteuerung (Dauer, Delay) wichtiger als Physik
- Datenvisualisierungen mit D3-Integration
- Kleines Bundle nötig (3.5kb gzipped)
- Lifecycle-Events (start/interrupt/end) benötigt
- SVG- oder React Native-Animationen

Docs: https://react-move-docs.netlify.app
