---
name: motion-examples
description: Offizielle Motion (Framer Motion) Beispiele — 153 React-Beispieldateien aus dem motiondivision/motion Repository. Enthält fertige Code-Snippets für AnimatePresence, Animationen, Drag, Events, Layout-Transitionen, Shared Layout, SVG, WAAPI, LazyMotion und alle wichtigen Hooks. Nutze diesen Skill wenn du konkrete Implementierungsbeispiele für die Motion-Library brauchst.
license: MIT
metadata:
  author: motiondivision
  source: https://github.com/motiondivision/motion
  examples_url: https://motion.dev/examples
  total_examples: "153"
compatibility: Claude Code, any AI coding agent
allowed-tools: Bash, Read, Write, Edit
---

# Motion Examples — 153 offizielle Beispiele

Offizielle Beispiel-Sammlung aus dem `motiondivision/motion` Repository.
Alle Dateien unter `.agents/plugins/motion-examples/examples/`.

```bash
npm install motion
# Import:
import { motion, AnimatePresence } from "motion/react"
```

## AnimatePresence (10 Beispiele)

| Datei | Beschreibung |
|-------|-------------|
| `AnimatePresence.tsx` | Basis: Single-child Ein/Ausblenden |
| `AnimatePresence-image-gallery.tsx` | Bildergalerie mit Slide-Transitions |
| `AnimatePresence-layout-animations-siblings.tsx` | Layout + AnimatePresence kombiniert |
| `AnimatePresence-notifications-list.tsx` | Notification-Liste mit Enter/Exit |
| `AnimatePresence-notifications-list-pop.tsx` | Notification-Pop-Effekt |
| `AnimatePresence-parallel-children.tsx` | Parallele Kind-Animationen |
| `AnimatePresence-siblings.tsx` | Geschwister-Transitionen |
| `AnimatePresence-switch.tsx` | Page/Tab Switch Animation |
| `AnimatePresence-variants.tsx` | Variants mit AnimatePresence |
| `AnimatePresence-wait.tsx` | Wait-Modus (erst exit, dann enter) |

## Animation (30 Beispiele)

| Datei | Beschreibung |
|-------|-------------|
| `Animation-animate.tsx` | Basis animate-Prop |
| `Animation-CSS-variables.tsx` | CSS Custom Properties animieren |
| `Animation-batch-read-writes.tsx` | Batched DOM reads/writes |
| `Animation-between-value-types.tsx` | Zwischen px/% animieren |
| `Animation-between-value-types-x.tsx` | Transform-Typ-Konvertierung |
| `Animation-boxShadow.tsx` | Box-Shadow animieren |
| `Animation-cleanup.tsx` | Animation cleanup bei Unmount |
| `Animation-display-visibility.tsx` | display/visibility animieren |
| `Animation-filter.tsx` | CSS Filter (blur, brightness...) |
| `Animation-height-auto-display-none.tsx` | height: auto → 0 |
| `Animation-height-auto-padding.tsx` | height: auto mit Padding |
| `Animation-height-auto-rotate-scale.tsx` | height: auto + Transforms |
| `Animation-keyframes.tsx` | Keyframe-Animationen |
| `Animation-layout-delay-children.tsx` | Layout mit verzögerten Kindern |
| `Animation-layout-nested-position.tsx` | Verschachtelte Layout-Position |
| `Animation-layout-scale-correction.tsx` | Scale-Correction bei Layout |
| `Animation-layout-seperate-children.tsx` | Separate Kinder-Layouts |
| `Animation-layout-size.tsx` | Layout-Größen-Animation |
| `Animation-layout-text-size.tsx` | Text-Größe animieren |
| `Animation-layout-transform-template.tsx` | Custom Transform Templates |
| `Animation-layout-update-stress.tsx` | Stress-Test Layout-Updates |
| `Animation-repeat-spring.tsx` | Wiederholende Spring-Animation |
| `Animation-reverse.tsx` | Animation umkehren |
| `Animation-spring-css.tsx` | Spring via CSS linear() |
| `Animation-stagger.tsx` | Gestaffelte Animationen |
| `Animation-stagger-custom.tsx` | Custom Stagger-Timing |
| `Animation-stress-mount.tsx` | Mount-Stress-Test |
| `Animation-transition-tween.tsx` | Tween-Transitions |
| `Animation-useAnimate-initial-transform.tsx` | useAnimate mit Transform |
| `Animation-variants.tsx` | Variants-basierte Animationen |

## Drag (15 Beispiele)

| Datei | Beschreibung |
|-------|-------------|
| `Drag-draggable.tsx` | Basis Drag-Funktionalität |
| `Drag-constraints-ref.tsx` | Drag-Grenzen per Ref |
| `Drag-constraints-relative.tsx` | Relative Drag-Grenzen |
| `Drag-constraints-resize.tsx` | Drag-Grenzen bei Resize |
| `Drag-constraints-ref-small-container.tsx` | Kleiner Container als Grenze |
| `Drag-constraints-ref-small-container-layout.tsx` | + Layout-Animation |
| `Drag-block-viewport-conditionally.tsx` | Viewport-Scrolling blockieren |
| `Drag-external-handlers.tsx` | Externe Drag-Handler |
| `Drag-nested.tsx` | Verschachteltes Drag |
| `Drag-svg-viewbox.tsx` | SVG-Viewbox Drag |
| `Drag-svg.tsx` | SVG-Element Drag |
| `Drag-to-reorder.tsx` | Drag-to-Reorder Liste |
| `Drag-useDragControls.tsx` | Programmatische Drag-Steuerung |
| `Drag-useDragControls-snapToCursor.tsx` | Snap-to-Cursor |
| `Drag-SharedLayout.tsx` | Drag + Shared Layout |

## Events (10 Beispiele)

| Datei | Beschreibung |
|-------|-------------|
| `Events-onTap.tsx` | onTap-Event |
| `Events-pan.tsx` | Pan-Geste |
| `Events-whileFocus.tsx` | whileFocus-Animation |
| `Events-whileFocus-variants.tsx` | whileFocus mit Variants |
| `Events-whileHover.tsx` | whileHover-Animation |
| `Events-whileHover-unit-conversion.tsx` | Einheiten-Konvertierung bei Hover |
| `Events-whileTap.tsx` | whileTap-Animation |
| `Events-whileTap-cancel-on-scroll.tsx` | Tap abbrechen bei Scroll |
| `Events-whileTap-global.tsx` | Globale Tap-Events |
| `Events-whileTap-variants.tsx` | whileTap mit Variants |

## Layout-Projection (9 Beispiele)

| Datei | Beschreibung |
|-------|-------------|
| `Layout-Projection-correct-style-border-radius.tsx` | Border-Radius Korrektur |
| `Layout-Projection-custom-values.tsx` | Custom Layout-Werte |
| `Layout-Projection-scale-correction-border-radius.tsx` | Scale + Border-Radius |
| `Layout-Projection-scale-correction-shadow.tsx` | Scale + Box-Shadow |
| `Layout-Projection-scale-position.tsx` | Scale-Position-Korrektur |
| `Layout-Projection-scale-size.tsx` | Scale-Größen-Korrektur |
| `Layout-SVG.tsx` | SVG Layout-Animation |
| `Layout-rotate.tsx` | Rotation mit Layout |
| `Layout-skew.tsx` | Skew mit Layout |

## Shared Layout (14 Beispiele)

| Datei | Beschreibung |
|-------|-------------|
| `Shared-layout-continuity.tsx` | Basis Shared Layout |
| `Shared-layout-continuity-crossfade.tsx` | Crossfade-Transition |
| `Shared-layout-lightbox.tsx` | Lightbox-Effekt |
| `Shared-layout-lightbox-crossfade.tsx` | Lightbox mit Crossfade |
| `Shared-layout-lists.tsx` | Listen mit Shared Layout |
| `Shared-layout-motion-value-continuity.tsx` | MotionValue Continuity |
| `Shared-layout-nested-inset-elements.tsx` | Verschachtelte Inset-Elemente |
| `Shared-layout-nested-inset-elements-no-layout.tsx` | Ohne Layout-Prop |
| `Shared-layout-reparenting.tsx` | Element zwischen Parents verschieben |
| `Shared-layout-reparenting-transform-template.tsx` | + Custom Transform |
| `Shared-layout-rotate.tsx` | Rotation Shared Layout |
| `Shared-layout-sibling-to-child.tsx` | Sibling → Child Transition |
| `Shared-layout-skew.tsx` | Skew Shared Layout |
| `Shared-layout-toggle-details.tsx` | Details-Toggle (Accordion) |

## SVG (6 Beispiele)

| Datei | Beschreibung |
|-------|-------------|
| `SVG-path.tsx` | SVG-Pfad animieren (pathLength, pathOffset) |
| `SVG-transform.tsx` | SVG Transform-Animationen |
| `SVG-MotionValue.tsx` | MotionValue in SVG |
| `SVG-Text-MotionValue-Child.tsx` | Text mit MotionValue |
| `SVG-layout-animation.tsx` | Layout in SVG |
| `SVG-without-initial-values.tsx` | SVG ohne Initial-Werte |

## WAAPI (4 Beispiele)

| Datei | Beschreibung |
|-------|-------------|
| `WAAPI-opacity.tsx` | Web Animations API Opacity |
| `WAAPI-background-color.tsx` | Hintergrundfarbe via WAAPI |
| `WAAPI-interrupt.tsx` | Animation unterbrechen |
| `WAAPI-opacity-orchestration.tsx` | WAAPI Orchestration |

## LazyMotion (2 Beispiele)

| Datei | Beschreibung |
|-------|-------------|
| `LazyMotion-async.tsx` | Asynchrones Feature-Loading |
| `LazyMotion-sync.tsx` | Synchrones Feature-Loading |

## Hooks (10 Beispiele)

| Datei | Beschreibung |
|-------|-------------|
| `useAnimation.tsx` | Programmatische Animation-Steuerung |
| `useAnimatedState.tsx` | Animierter State |
| `useInstantTransition.tsx` | Sofortige Transitions |
| `usePresence.tsx` | Exit-Animations aus Kindern heraus |
| `useReducedMotion.tsx` | Reduced-Motion Accessibility |
| `useScroll.tsx` | Scroll-Position tracken |
| `useSpring.tsx` | Spring-basierte MotionValues |
| `useTransform-with-useLayoutEffect.tsx` | useTransform + useLayoutEffect |
| `useVelocity.tsx` | Scroll-Geschwindigkeit |
| `useViewportScroll.tsx` | Viewport-Scroll (legacy) |

## Transition (2 Beispiele)

| Datei | Beschreibung |
|-------|-------------|
| `transition-arc-playground.tsx` | Arc-Transition Playground |
| `transition-arc-spring-playground.tsx` | Arc + Spring Playground |

## Typische Muster

### AnimatePresence mit Exit

```tsx
import { AnimatePresence, motion } from "motion/react"

<AnimatePresence>
  {isVisible && (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
    />
  )}
</AnimatePresence>
```

### Drag-to-Reorder

```tsx
// Siehe: Drag-to-reorder.tsx
import { Reorder } from "motion/react"

<Reorder.Group values={items} onReorder={setItems}>
  {items.map(item => (
    <Reorder.Item key={item} value={item}>{item}</Reorder.Item>
  ))}
</Reorder.Group>
```

### Shared Layout (layoutId)

```tsx
// Siehe: Shared-layout-lightbox.tsx
<motion.div layoutId="image" />
```

### SVG Path Animation

```tsx
// Siehe: SVG-path.tsx
<motion.path
  initial={{ pathLength: 0 }}
  animate={{ pathLength: 1 }}
  transition={{ duration: 2 }}
/>
```

Alle Beispiele unter: `.agents/plugins/motion-examples/examples/`
Docs: https://motion.dev/examples
