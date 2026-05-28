---
name: react-anim-framer-motion
description: Motion (ehem. Framer Motion) — mächtigste React/JS/Vue Animations-Library. Nutze diesen Skill wenn du Animationen, Transitions, Gesten, Scroll-Effekte, Layout-Animationen oder Spring-Physik in React/JavaScript/Vue implementieren willst. Deklarative API, 120fps GPU-beschleunigt, TypeScript, SSR, tree-shakable.
license: MIT
metadata:
  author: Framer
  source: https://github.com/framer/motion
  docs: https://motion.dev/docs/react
  npm: motion
  stars: "20.8K"
  weekly_downloads: "2.5M+"
compatibility: Claude Code, any AI coding agent
allowed-tools: Bash, Read, Write, Edit
---

# Motion (Framer Motion)

Mächtigste deklarative Animations-Library für React, JavaScript und Vue. Hybrid-Engine kombiniert JavaScript mit nativen Browser-APIs für 120fps GPU-beschleunigte Animationen.

## Installation

```bash
npm install motion
```

## React Quick Start

```jsx
import { motion } from "motion/react"

// Einfache Animation
function Component() {
  return <motion.div animate={{ x: 100 }} />
}

// Mit Initial- und Zielzustand
function FadeIn() {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
    />
  )
}

// Hover & Tap Gesten
function Button() {
  return (
    <motion.button
      whileHover={{ scale: 1.05 }}
      whileTap={{ scale: 0.95 }}
    >
      Klick mich
    </motion.button>
  )
}
```

> **Hinweis:** Framer Motion heißt jetzt Motion. Importiere aus `motion/react` statt `framer-motion`.

## JavaScript (ohne React)

```javascript
import { animate } from "motion"

animate("#box", { x: 100, opacity: 1 }, { duration: 0.5 })
```

## Vue

```html
<script>
  import { motion } from "motion-v"  // npm install motion-v
</script>
<template>
  <motion.div :animate="{ x: 100 }" />
</template>
```

## Kernkonzepte

### Variants — wiederverwendbare Animationszustände

```jsx
const variants = {
  hidden: { opacity: 0, x: -100 },
  visible: { opacity: 1, x: 0 },
}

<motion.div
  variants={variants}
  initial="hidden"
  animate="visible"
/>
```

### Layout-Animationen

```jsx
// Automatische Transition bei Layout-Änderungen
<motion.div layout />

// Shared Layout zwischen Komponenten
<motion.div layoutId="shared-element" />
```

### Scroll-linked Animationen

```jsx
import { useScroll, useTransform } from "motion/react"

function ParallaxComponent() {
  const { scrollYProgress } = useScroll()
  const y = useTransform(scrollYProgress, [0, 1], ["0%", "50%"])
  return <motion.div style={{ y }} />
}
```

### Springs & Transitions

```jsx
<motion.div
  animate={{ x: 100 }}
  transition={{
    type: "spring",
    stiffness: 260,
    damping: 20,
  }}
/>

// Oder Tween mit Easing
<motion.div
  animate={{ opacity: 1 }}
  transition={{ duration: 0.5, ease: "easeOut" }}
/>
```

### AnimatePresence — Ein/Ausblenden

```jsx
import { AnimatePresence, motion } from "motion/react"

function Modal({ isOpen }) {
  return (
    <AnimatePresence>
      {isOpen && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
        />
      )}
    </AnimatePresence>
  )
}
```

### Timelines (Sequenzen)

```javascript
import { animate } from "motion"

animate([
  ["#box", { x: 100 }],
  ["#box", { y: 100 }, { at: "-0.5" }],  // Überlappend
  ["#box", { rotate: 360 }],
])
```

## Empfohlene Hooks

| Hook | Zweck |
|------|-------|
| `useAnimation()` | Animationen programmatisch steuern |
| `useScroll()` | Scroll-Position tracken |
| `useTransform()` | Werte transformieren |
| `useSpring()` | Spring-basierte Werte |
| `useInView()` | Element im Viewport erkennen |
| `useMotionValue()` | Animierbare Einzelwerte |

## Transition-Typen

| Typ | Einsatz |
|-----|---------|
| `"spring"` | Natürliche, physikalische Bewegung (Standard) |
| `"tween"` | Feste Dauer + Easing-Kurve |
| `"inertia"` | Drag-/Swipe-Ausklang |

## Docs & Beispiele
- Docs: https://motion.dev/docs/react
- 330+ Beispiele: https://motion.dev/examples
- 3D-Animationen: Motion 3D (Framer Motion 3d)
