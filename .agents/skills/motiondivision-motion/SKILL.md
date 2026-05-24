---
name: motiondivision-motion
description: Motion (motiondivision) — offizielle Open-Source-Animations-Library für React, JavaScript und Vue. Hybrid-Engine kombiniert JavaScript mit nativen Browser-APIs für 120fps GPU-beschleunigte Animationen. Enthält Springs, Gesten, Layout-Transitions, Scroll-Effekte, Timelines, LazyMotion, Pfad-Animationen und arc(). Nutze diesen Skill wenn du Animationen in React/JS/Vue implementieren willst.
license: MIT
metadata:
  author: motiondivision
  source: https://github.com/motiondivision/motion
  docs: https://motion.dev/docs
  npm: motion
  version: "12.40.0"
  stars: "20.8K"
  weekly_downloads: "2.5M+"
compatibility: Claude Code, any AI coding agent
allowed-tools: Bash, Read, Write, Edit
---

# Motion (motiondivision)

Offizielle Open-Source-Animations-Library für React, JavaScript und Vue. Entwickelt von motiondivision (ehemals Framer). Hybrid-Engine: JavaScript + native Browser-APIs für 120fps GPU-beschleunigte Animationen.

## Installation

```bash
# React / JavaScript
npm install motion

# Vue
npm install motion-v

# Legacy (weiterhin kompatibel)
npm install framer-motion
```

> **Hinweis:** `framer-motion` ist jetzt `motion`. Import aus `motion/react` statt `framer-motion`.

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

## JavaScript (ohne Framework)

```javascript
import { animate } from "motion"

animate("#box", { x: 100, opacity: 1 }, { duration: 0.5 })
```

## Vue

```html
<script setup>
  import { motion } from "motion-v"
</script>
<template>
  <motion.div :animate="{ x: 100 }" />
</template>
```

## Kernkonzepte

### Variants — wiederverwendbare Zustände

```jsx
const variants = {
  hidden: { opacity: 0, x: -100 },
  visible: { opacity: 1, x: 0 },
}

<motion.div
  variants={variants}
  initial="hidden"
  animate="visible"
  transition={{ duration: 0.5 }}
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

### Layout-Animationen

```jsx
// Automatische Transition bei Layout-Änderungen
<motion.div layout />

// Shared Layout zwischen Komponenten (z.B. Tab-Indicator)
<motion.div layoutId="underline" />
```

### Scroll-linked Animationen

```jsx
import { useScroll, useTransform } from "motion/react"

function ParallaxSection() {
  const { scrollYProgress } = useScroll()
  const y = useTransform(scrollYProgress, [0, 1], ["0%", "50%"])
  return <motion.div style={{ y }} />
}
```

### Springs & Transitions

```jsx
// Spring (Standard)
<motion.div
  animate={{ x: 100 }}
  transition={{ type: "spring", stiffness: 260, damping: 20 }}
/>

// Tween mit Easing
<motion.div
  animate={{ opacity: 1 }}
  transition={{ duration: 0.5, ease: "easeOut" }}
/>

// Pfad-Animation (neu in v12)
<motion.div
  animate={{ x: 100 }}
  transition={{ path: pathElement }}
/>

// Arc-Animation (neu in v12.40)
import { arc } from "motion"
<motion.div animate={{ x: arc(0, 100, 50) }} />
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

### Pfad-Animationen (SVG)

```jsx
import { motion } from "motion/react"

<svg>
  <motion.path
    initial={{ pathLength: 0 }}
    animate={{ pathLength: 1 }}
    transition={{ duration: 2 }}
    d="M 0 0 L 100 100"
  />
</svg>
```

## Hooks-Übersicht

| Hook | Zweck |
|------|-------|
| `useAnimation()` | Animationen programmatisch steuern |
| `useScroll()` | Scroll-Position tracken |
| `useTransform()` | Werte transformieren |
| `useSpring()` | Spring-basierte Werte |
| `useInView()` | Element im Viewport erkennen |
| `useMotionValue()` | Animierbare Einzelwerte |
| `useAnimate()` | Imperative Animations-API mit Selector-Support |

## Gesten

```jsx
<motion.div
  drag                          // Draggable
  dragConstraints={{ left: -100, right: 100 }}
  whileHover={{ scale: 1.1 }}
  whileTap={{ scale: 0.9 }}
  whileDrag={{ opacity: 0.8 }}
  whileFocus={{ outline: "2px solid blue" }}
  onHoverStart={() => console.log("hover")}
  onTap={() => console.log("tap")}
/>
```

## LazyMotion (Bundle-Optimierung)

```jsx
import { LazyMotion, domAnimation, m } from "motion/react"

// Nur domAnimation Features laden (kleineres Bundle)
function App() {
  return (
    <LazyMotion features={domAnimation}>
      <m.div animate={{ x: 100 }} />
    </LazyMotion>
  )
}
```

## Packages

| Package | Zweck |
|---------|-------|
| `motion` | React + JavaScript (Haupt-Package) |
| `framer-motion` | Legacy (identisch mit motion) |
| `motion-v` | Vue-Integration |
| `motion-dom` | DOM ohne Framework |
| `motion-utils` | Utilities |

## Docs & Beispiele

- Docs: https://motion.dev/docs/react
- 330+ Beispiele: https://motion.dev/examples
- Changelog: https://github.com/motiondivision/motion/blob/main/CHANGELOG.md
