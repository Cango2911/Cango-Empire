---
name: eaglejs
version: 0.6.1
description: "Eagle.js — Slideshow Framework für Hacker (Vue 2). Programmatische Präsentationen mit Animationen, Themes, interaktiven Widgets. Slideshow-Mixin + Slide-Komponenten + 8 Widgets + 2 Plugins. Presenter-Mode, Zoom, Syntax-Highlighting, Touch/Mobile-Support."
author: Zulko et al. (Open Source, ISC)
source: https://github.com/Zulko/eagle.js
license: ISC
type: agent-skill
tags:
  - slideshow
  - presentation
  - vue2
  - javascript
  - animations
  - widgets
---

# Eagle.js — Slideshow Framework für Hacker

## Was ist Eagle.js?

Eagle.js ist ein Vue 2-basiertes Slideshow-Framework für programmatische Präsentationen. Statt PowerPoint oder Reveal.js schreibt man Slides als Vue Single File Components — maximale Hackability, volle Kontrolle über jeden Pixel.

**Status**: Feature-complete, nicht aktiv gewartet. Für Vue 3 Support → [Slidev](https://sli.dev/) empfohlen.  
**Install**: `npm install --save eagle.js`  
**Demo**: https://zulko.github.io/eaglejs-demo/#/introducing-eagle

## Installation

```bash
npm install --save eagle.js animate.css
# oder
yarn add eagle.js animate.css
```

## Schnellstart

```javascript
// main.js
import Eagle from 'eagle.js'
import 'animate.css'        // Peer-Dependency für Slide-Animationen

Vue.use(Eagle)
```

## Grundstruktur

Eagle.js besteht aus zwei Kernkomponenten:
1. **`Slideshow`** — Mixin für die Präsentations-Komponente (verwaltet Folien-Navigation)
2. **`Slide`** — Komponente/Mixin für einzelne Folien (verwaltet Steps)

### Minimales Slideshow-Beispiel (Pug)

```pug
.eg-slideshow
    slide
      h1 Meine Präsentation
      h4 von Eagle.js

    slide
      h3 Folie 2 — Bulletpoints
      p Absatz 1.
      p Absatz 2.

    slide(:steps=3)
      h3 Folie mit Animationen
      p(v-if='step >= 2') Erscheint als erstes.
      p(v-if='step >= 3') Erscheint als zweites.
```

### Minimales Slideshow-Beispiel (Vue SFC)

```vue
<template>
  <div class="eg-slideshow">
    <slide>
      <h1>Hallo Eagle.js</h1>
    </slide>

    <slide :steps="3">
      <h2>Animated Steps</h2>
      <p v-if="step >= 2">Schritt 2</p>
      <p v-if="step >= 3">Schritt 3</p>
    </slide>
  </div>
</template>

<script>
import { Slideshow } from 'eagle.js'
export default {
  mixins: [Slideshow]
}
</script>
```

## Slideshow-Konfiguration

`slideshow` als Mixin — konfigurierbare Props:

| Property | Default | Beschreibung |
|----------|---------|-------------|
| `firstSlide` | `1` | Erste Folie |
| `lastSlide` | `null` | Letzte Folie |
| `startStep` | `1` | Start-Step |
| `mouseNavigation` | `true` | Navigation per Mausklick/Scroll |
| `keyboardNavigation` | `true` | Navigation per Tastatur (Pfeiltasten) |
| `embedded` | `false` | Eingebetteter Modus |
| `inserted` | `false` | Eingefügter Modus (in anderer Slideshow) |
| `backBySlide` | `false` | Zurücknavigation: per Step (Standard) oder per Slide |
| `repeat` | `false` | Automatisch zur ersten Folie springen am Ende |
| `zoom` | `true` | Alt+Click zum Zoomen |
| `onStartExit` | `null` | Callback beim Verlassen durch die erste Folie |
| `onEndExit` | `null` | Callback beim Verlassen durch die letzte Folie |

### Slideshow-Methoden

```javascript
// In der Slideshow-Komponente verfügbar:
this.nextStep()        // Nächster Step (oder nächste Folie)
this.previousStep()    // Vorheriger Step (oder vorherige Folie)
this.nextSlide()       // Direkt zur nächsten Folie
this.previousSlide()   // Direkt zur vorherigen Folie
```

## Slide-Konfiguration

| Property | Default | Beschreibung |
|----------|---------|-------------|
| `steps` | `1` | Anzahl Steps dieser Folie |
| `skip` | `false` | Folie überspringen |
| `enter` | `null` | Standard Einblend-Animation (animate.css) |
| `leave` | `null` | Standard Ausblend-Animation (animate.css) |
| `enterPrev` | `null` | Einblend-Animation für Rückwärts-Richtung |
| `enterNext` | `null` | Einblend-Animation für Vorwärts-Richtung |
| `leavePrev` | `null` | Ausblend-Animation für Rückwärts-Richtung |
| `leaveNext` | `null` | Ausblend-Animation für Vorwärts-Richtung |
| `mouseNavigation` | `true` | Maus-Navigation auf dieser Folie |
| `keyboardNavigation` | `true` | Tastatur-Navigation auf dieser Folie |

### Slide mit Animationen

```vue
<slide enter="fadeIn" leave="fadeOut">
  <h2>Diese Folie blendet ein/aus</h2>
</slide>

<!-- Verschiedene Animationen für Vorwärts/Rückwärts: -->
<slide enter-next="slideInRight" leave-next="slideOutLeft"
       enter-prev="slideInLeft"  leave-prev="slideOutRight">
  <p>Animiert je nach Richtung</p>
</slide>
```

**Wichtig**: `enter` und `leave` immer als Paar setzen (beide oder keines).

## Eigene Slide-Komponente (SFC)

```vue
<!-- MyCustomSlide.vue -->
<template>
  <eg-transition :enter="enter" :leave="leave">
    <div class="eg-slide" v-if="active">
      <div class="eg-slide-content">
        <!-- Eigener Inhalt -->
        <slot></slot>
      </div>
    </div>
  </eg-transition>
</template>

<script>
import { Slide } from 'eagle.js'
export default {
  mixins: [Slide]
}
</script>
```

## Nested Slideshows

```
Slideshow
├── Slide 1
├── Slide 2 (mit eingebetteter Slideshow)
│   └── embedded Slideshow  ← :embedded="true"
│       ├── Slide A
│       └── Slide B
└── Slide 3
    └── inserted Slideshow  ← :inserted="true"  (in Slideshow, nicht in Slide)
```

- **`embedded`**: Slideshow in einem `<slide>` → eigene Events + eigene Styles
- **`inserted`**: Slideshow in einer anderen Slideshow → teilt Events des Parents

## Widgets (8 verfügbar)

Widgets importieren und registrieren:

```javascript
import Eagle, { Modal, CodeBlock, CodeComment, Toggle, RadioButton, TriggeredMessage, Timer, ImageSlide } from 'eagle.js'

Eagle.use(Modal)
Eagle.use(CodeBlock)
Eagle.use(CodeComment)
Eagle.use(Toggle)
Eagle.use(RadioButton)
Eagle.use(TriggeredMessage)
// Timer und ImageSlide analog
```

### Widget-Übersicht

| Widget | Tag | Beschreibung |
|--------|-----|-------------|
| `Modal` | `<eg-modal>` | Modaler Dialog |
| `CodeBlock` | `<eg-code-block>` | Syntax-Highlighted Code (highlight.js) |
| `CodeComment` | `<eg-code-comment>` | Kommentar für Code-Blöcke |
| `Toggle` | `<eg-toggle>` | Toggle-Switch |
| `RadioButton` | `<eg-radio-button>` | Radio-Button-Gruppe |
| `TriggeredMessage` | `<eg-triggered-message>` | Nachricht bei Trigger |
| `Timer` | `<eg-timer>` | Countdown/Timer |
| `ImageSlide` | `<eg-image-slide>` | Bild-Folie |

### CodeBlock mit highlight.js

```javascript
// Eigenes highlight.js einrichten:
import hljs from 'highlight.js/lib/highlight'
import javascript from 'highlight.js/lib/languages/javascript'
hljs.registerLanguage('javascript', javascript)

import { Options } from 'eagle.js'
Options.hljs = hljs
```

```html
<!-- In der Folie: -->
<eg-code-block lang="javascript">
  const greeting = "Hello Eagle.js!"
  console.log(greeting)
</eg-code-block>
```

## Plugins

### Presenter Plugin (Präsentationsmodus)

```javascript
import Eagle, { Presenter } from 'eagle.js'

Eagle.use(Presenter, {
  presenterModeKey: 'p'   // Standard: 'p'
})
```

In der Slideshow-Komponente:
```javascript
data: function () {
  return {
    childWindow: null,    // Pflicht für Presenter-Plugin
    parentWindow: null,   // Pflicht für Presenter-Plugin
  }
}
```

Zwei synchronisierte Fenster — Toggle mit konfigurierter Taste:
```pug
.eg-slideshow
  slide
    p Haupt-Inhalt
    p(v-if="parentWindow") Nur im Referenten-Fenster sichtbar (Notizen)
    p(v-if="childWindow")  Alternativ im anderen Fenster
```

### Zoom Plugin

```javascript
import Eagle, { Zoom } from 'eagle.js'

Eagle.use(Zoom, {
  scale: 2   // Standard: 2
})
```

`Option`+Click (Mac) / `Alt`+Click (Windows/Linux) zum Zoomen.

## Themes

```javascript
// Standard (kein Import nötig ab v0.6)
// Oder Theme importieren:
import 'eagle.js/dist/themes/gourmet/gourmet.css'
import 'eagle.js/dist/themes/agrume/agrume.css'
```

Theme-Wrapper in der Template:
```html
<div class="eg-theme-gourmet">
  <div class="eg-slideshow">
    <!-- Slides -->
  </div>
</div>
```

**Verfügbare Themes**: `gourmet`, `agrume`, `refuel-dark`

## Mobile-Support (Hammer.js)

```javascript
mounted () {
  const hammer = new Hammer(window)
  hammer.on('swiperight', () => { this.previousStep() })
  hammer.on('swipeleft',  () => { this.nextStep()     })
}
```

## Permalinks (vue-router)

```javascript
// router.js
const router = new VueRouter({
  routes: [{ path: '/:slide/:step', component: MySlideshow }]
})

// In MySlideshow:
methods: {
  updateSlides () {
    this.currentSlideIndex = +this.$route.params.slide
    this.$nextTick(() => { this.step = +this.$route.params.step })
  },
  updateURL () {
    this.$router.push(`/${this.currentSlideIndex}/${this.step}`)
  }
},
watch: {
  '$route': 'updateSlides',
  step: 'updateURL',
  currentSlideIndex: 'updateURL'
}
```

## Vue-CLI v4+ — CodeBlock Whitespace-Fix

```javascript
// vue.config.js
module.exports = {
  chainWebpack: config => {
    config.module.rule('vue').use('vue-loader').tap(args => {
      args.compilerOptions.whitespace = 'preserve'
    })
  }
}
```

## Entwicklung (Storybook)

```bash
git clone https://github.com/Zulko/eagle.js.git
npm install
npm run storybook
```

## Alternativen

| Tool | Vue-Version | Status |
|------|------------|--------|
| Eagle.js | Vue 2 | Feature-complete, nicht aktiv gewartet |
| [Slidev](https://sli.dev/) | Vue 3 | Aktiv, empfohlen |
| [Reveal.js](https://revealjs.com/) | Vanilla JS | Aktiv, weit verbreitet |

## Referenzen

- GitHub: https://github.com/Zulko/eagle.js
- npm: https://www.npmjs.com/package/eagle.js
- Demo: https://zulko.github.io/eaglejs-demo/#/introducing-eagle
- Demo-Repo: https://github.com/Zulko/eaglejs-demo
- Permalink-Demo: http://eaglejspermalink.surge.sh/
