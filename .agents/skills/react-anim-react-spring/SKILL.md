---
name: react-anim-react-spring
description: React Spring — spring-physics-first cross-platform Animations-Library. Nutze diesen Skill für flüssige, physikalische Animationen in React (Web, Native, Three.js, Konva, Zdog). Vermeidet unnötige Re-Renders, SSR-Support, vollständiges TypeScript. Hooks-basierte API (useSpring, useSprings, useTrail, useTransition, useChain).
license: MIT
metadata:
  author: pmndrs (Poimandres)
  source: https://github.com/pmndrs/react-spring
  docs: https://www.react-spring.dev
  npm: "@react-spring/web"
  stars: "26.8K"
  weekly_downloads: "726K"
compatibility: Claude Code, any AI coding agent
allowed-tools: Bash, Read, Write, Edit
---

# React Spring

Spring-physics-first cross-platform Animations-Library für React. 26.8K Stars — beliebteste physics-basierte React-Animations-Library.

## Installation

```bash
# Nur für Web (empfohlen — kleineres Bundle)
npm install @react-spring/web

# Vollständige Library (alle Targets)
npm install react-spring
```

## Targets

| Package | Plattform |
|---------|-----------|
| `@react-spring/web` | React DOM |
| `@react-spring/native` | React Native |
| `@react-spring/three` | React Three Fiber / Three.js |
| `@react-spring/konva` | React Konva |
| `@react-spring/zdog` | React Zdog |

## Hooks-Übersicht

### `useSpring` — Einzelwert animieren

```jsx
import { animated, useSpring } from '@react-spring/web'

function FadeIn({ isVisible }) {
  const styles = useSpring({
    opacity: isVisible ? 1 : 0,
    y: isVisible ? 0 : 24,
  })

  return <animated.div style={styles}>Inhalt</animated.div>
}
```

### `useSprings` — Mehrere unabhängige Springs

```jsx
import { animated, useSprings } from '@react-spring/web'

function AnimatedList({ items }) {
  const springs = useSprings(
    items.length,
    items.map((_, i) => ({
      from: { opacity: 0, x: -50 },
      to: { opacity: 1, x: 0 },
      delay: i * 100,
    }))
  )

  return springs.map((style, i) => (
    <animated.div key={i} style={style}>{items[i]}</animated.div>
  ))
}
```

### `useTrail` — Gestaffelte Animationen (Kettenreaktion)

```jsx
import { animated, useTrail } from '@react-spring/web'

function TrailList({ items, open }) {
  const trail = useTrail(items.length, {
    opacity: open ? 1 : 0,
    x: open ? 0 : 20,
    from: { opacity: 0, x: 20 },
  })

  return trail.map((style, i) => (
    <animated.div key={i} style={style}>{items[i]}</animated.div>
  ))
}
```

### `useTransition` — Mount/Unmount animieren

```jsx
import { animated, useTransition } from '@react-spring/web'

function Modal({ show, children }) {
  const transitions = useTransition(show, {
    from: { opacity: 0, transform: 'scale(0.9)' },
    enter: { opacity: 1, transform: 'scale(1)' },
    leave: { opacity: 0, transform: 'scale(0.9)' },
  })

  return transitions((style, item) =>
    item ? <animated.div style={style}>{children}</animated.div> : null
  )
}
```

### `useChain` — Springs sequenziell verketten

```jsx
import { useSpring, useTrail, useChain, useSpringRef } from '@react-spring/web'

function ChainedAnimation() {
  const springRef = useSpringRef()
  const trailRef = useSpringRef()

  const spring = useSpring({ ref: springRef, opacity: 1 })
  const trail = useTrail(3, { ref: trailRef, x: 0 })

  // Erst spring, dann trail mit 0.1s Überlappung
  useChain([springRef, trailRef], [0, 0.9])
}
```

## Imperative API (ohne State-Änderungen)

```jsx
import { useSpring, animated } from '@react-spring/web'

function ImmediateControl() {
  const [styles, api] = useSpring(() => ({ x: 0 }))

  return (
    <>
      <animated.div style={styles} />
      <button onClick={() => api.start({ x: 100 })}>Starten</button>
      <button onClick={() => api.stop()}>Stoppen</button>
      <button onClick={() => api.set({ x: 0 })}>Reset</button>
    </>
  )
}
```

## Spring-Konfiguration

```jsx
const config = {
  mass: 1,        // Trägheit
  tension: 170,   // Stärke der Feder
  friction: 26,   // Dämpfung
  precision: 0.01,
  velocity: 0,
}

useSpring({ x: 100, config })

// Vorgefertigte Configs
import { config } from '@react-spring/web'
config.default    // { tension: 170, friction: 26 }
config.gentle     // { tension: 120, friction: 14 }
config.wobbly     // { tension: 180, friction: 12 }
config.stiff      // { tension: 210, friction: 20 }
config.slow       // { tension: 280, friction: 60 }
config.molasses   // { tension: 280, friction: 120 }
```

## Docs
- https://www.react-spring.dev
- Playground: https://react-spring.dev/examples
