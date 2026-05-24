---
name: react-anim-react-motion
description: React Motion — physics-basierte Animations-Library für React. Nutze diesen Skill wenn du spring-physikalische Animationen in React implementieren willst ohne feste Dauer oder Easing-Kurven. Definiere Steifigkeit (stiffness) und Dämpfung (damping) — die Physik erledigt den Rest. Unterstützt React Native v0.18+.
license: MIT
metadata:
  author: chenglou
  source: https://github.com/chenglou/react-motion
  npm: react-motion
  stars: "21.6K"
  weekly_downloads: "406K"
compatibility: Claude Code, any AI coding agent
allowed-tools: Bash, Read, Write, Edit
---

# React Motion

Physics-basierte Animations-Library für React. Statt fester Dauer und Easing-Kurven definierst du Federsteifigkeit und Dämpfung — die Physik-Simulation macht die Bewegung natürlich.

## Installation

```bash
npm install react-motion
```

## Grundprinzip

```jsx
import { Motion, spring } from 'react-motion'

// Animiert einen Wert von 0 auf 10
<Motion defaultStyle={{ x: 0 }} style={{ x: spring(10) }}>
  {value => <div style={{ transform: `translateX(${value.x}px)` }} />}
</Motion>
```

## Kernkomponenten

### `<Motion>` — Einzelnes Element animieren

```jsx
import { Motion, spring } from 'react-motion'

function AnimatedBox({ isOpen }) {
  return (
    <Motion
      defaultStyle={{ opacity: 0, x: -100 }}
      style={{
        opacity: spring(isOpen ? 1 : 0),
        x: spring(isOpen ? 0 : -100),
      }}
    >
      {({ opacity, x }) => (
        <div style={{
          opacity,
          transform: `translateX(${x}px)`,
        }} />
      )}
    </Motion>
  )
}
```

### `<StaggeredMotion>` — Gestaffelte Listenanimationen

```jsx
import { StaggeredMotion, spring } from 'react-motion'

function StaggeredList({ items }) {
  return (
    <StaggeredMotion
      defaultStyles={items.map(() => ({ y: -100 }))}
      styles={prevStyles => prevStyles.map((_, i) => ({
        y: spring(0, { stiffness: 120, damping: 17 })
      }))}
    >
      {styles => (
        <ul>
          {styles.map(({ y }, i) => (
            <li key={i} style={{ transform: `translateY(${y}px)` }}>
              {items[i]}
            </li>
          ))}
        </ul>
      )}
    </StaggeredMotion>
  )
}
```

### `<TransitionMotion>` — Ein/Ausblenden mit Lifecycle

```jsx
import { TransitionMotion, spring } from 'react-motion'

function TransitionList({ items }) {
  return (
    <TransitionMotion
      styles={items.map(item => ({
        key: item.id,
        style: { opacity: spring(1), height: spring(50) },
      }))}
      willLeave={() => ({ opacity: spring(0), height: spring(0) })}
      willEnter={() => ({ opacity: 0, height: 0 })}
    >
      {styles => (
        <ul>
          {styles.map(({ key, style, data }) => (
            <li key={key} style={style}>{data}</li>
          ))}
        </ul>
      )}
    </TransitionMotion>
  )
}
```

## Spring-Parameter

```jsx
// Vorgefertigte Presets
import { presets } from 'react-motion'

spring(value, presets.noWobble)   // { stiffness: 170, damping: 26 }
spring(value, presets.gentle)     // { stiffness: 120, damping: 14 }
spring(value, presets.wobbly)     // { stiffness: 180, damping: 12 }
spring(value, presets.stiff)      // { stiffness: 210, damping: 20 }

// Eigene Parameter
spring(value, { stiffness: 200, damping: 15 })
```

| Parameter | Effekt |
|-----------|--------|
| `stiffness` hoch | Schnelle, straffe Bewegung |
| `stiffness` niedrig | Langsame, weiche Bewegung |
| `damping` hoch | Kein Überschwingen |
| `damping` niedrig | Starkes Federn/Wobble |

## Exports

```jsx
import {
  Motion,           // Einzelelement-Animation
  StaggeredMotion,  // Gestaffelte Animationen
  TransitionMotion, // Mount/Unmount-Animationen
  spring,           // Spring-Wert-Funktion
  presets,          // Vordefinierte Spring-Parameter
} from 'react-motion'
```

## Demos
- Simple Transition, Chat Heads, Draggable Balls, TodoMVC List, Photo Gallery, Water Ripples, Draggable List
- https://github.com/chenglou/react-motion#demos
