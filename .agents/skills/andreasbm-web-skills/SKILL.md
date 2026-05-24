---
name: andreasbm-web-skills
description: Visuelle Web-Entwickler Lernroadmap von Andreas Mehlsen mit 14 Hauptkategorien und hunderten kuratierten Ressourcen. Enthält HTML, CSS, JavaScript, Browser-Grundlagen, Accessibility, Web Components, PWA, Build Tools, Frameworks (React/Angular/Vue/Svelte/Lit), Testing, Architecture, Team Collaboration, Design & UX, The Modern Web, Algorithms & Data Structures, Databases & Servers. Vollständiger Inhalt in blueprint.md (3274 Zeilen).
license: MIT
metadata:
  author: Andreas Mehlsen
  source: https://github.com/andreasbm/web-skills
  website: https://andreasbm.github.io/web-skills
compatibility: Claude Code, Claude.ai, any AI coding agent
allowed-tools: Read
---

# Web Skills (andreasbm)

Visuelle Lernroadmap für Web-Entwickler — 14 Kategorien, hunderte kuratierte Ressourcen.

Live: https://andreasbm.github.io/web-skills | Vollinhalt: `blueprint.md` (3274 Zeilen)

## Kategorien

### 1. Fundamentals

#### HTML
- **Syntax** — MDN HTML Basics, Introduction to HTML, Codecademy
- **Forms** — Form design, validation, UX
- **SEO** — Discoverable content, structured data, Open Graph
- **SVG** — Inline SVG, SMIL, SVG Sprites
- **Best Practices** — Validation, semantics

#### CSS
- **Syntax** — Specificity, cascading, inheritance
- **Selectors** — Basic, pseudo-classes, pseudo-elements, combinators
- **Box Model** — Margin, padding, border, box-sizing
- **Colors** — Color theory, HSL, `currentColor`, gradients
- **Calc** — Dynamic calculations, viewport units
- **Layout** — Flexbox, CSS Grid, positioning, floats
- **Transforms** — Perspective, 3D, transform-origin
- **Responsive Design** — Media queries, fluid typography, clamp()
- **CSS Variables** — Custom properties, cascading variables
- **Best Practices** — BEM, CSS-in-JS, performance

#### JavaScript
- **Syntax** — Variables, scope, closures, hoisting, strict mode
- **DOM** — Querying, manipulation, virtual DOM
- **Events** — Event listeners, bubbling, delegation
- **Objects** — Prototypes, classes, getters/setters, proxies, destructuring
- **Regex** — Expressions, groups, lookaheads
- **Template Literals** — Tagged templates
- **Promises** — Async/await, microtasks, Fetch API
- **Web Animations** — WAAPI, requestAnimationFrame, performance
- **Modules** — ES modules, tree shaking, dynamic imports
- **Intl** — Internationalization (dates, numbers, plurals)
- **Canvas** — 2D context, pixel manipulation
- **Documentation** — JSDoc, TypeScript, type definitions

#### The Browser
- **Standardization** — W3C, WHATWG, TC39, ECMA
- **Browser Engines** — Chromium, WebKit, SpiderMonkey
- **HTTP** — Headers, caching, HTTP/2, HTTP/3
- **The Internet** — DNS, TCP/UDP, TLS, CDN
- **Polyfills** — Feature detection, polyfill strategy
- **Debugging** — DevTools, breakpoints, performance profiling

### 2. Accessibility
- Screen Readers, Accessibility Tree, ARIA, Focus management
- Color contrast, keyboard navigation, skip links
- `prefers-reduced-motion`, Lighthouse audits

### 3. Web Components
- Custom Elements, Shadow DOM, HTML Templates, slots
- Lit Element, Stencil, Open WC
- CSS Custom Properties in Shadow DOM

### 4. Progressive Web Apps (PWA)
- Service Workers, Cache API, Background Sync, Push Notifications
- Web App Manifest, Add to Home Screen
- Workbox, offline-first strategies
- Storage: IndexedDB, localStorage, sessionStorage
- Performance: Lighthouse, Core Web Vitals

### 5. Build Tools
- **Package Managers** — npm, Yarn, pnpm
- **Bundlers** — Webpack, Rollup, esbuild, Vite, Parcel, Snowpack
- **Transpilers** — Babel, TypeScript
- **Task Runners** — npm scripts, Makefiles
- **Linting** — ESLint, Prettier, Stylelint
- **CI/CD** — GitHub Actions, Travis CI, deployment pipelines

### 6. Frameworks & Libraries
- **React** — JSX, hooks, context, Suspense, React Router, Next.js
- **Angular** — Components, directives, services, NgRx, Angular Material
- **Vue** — Options API, Composition API, Vuex, Nuxt
- **Svelte** — Reactivity, stores, SvelteKit
- **Lit** — Lit Element, Lit HTML, decorators
- **State Management** — Redux, MobX, Recoil, Zustand

### 7. Testing
- **Unit Testing** — Jest, Mocha, Chai, Jasmine
- **Integration Testing** — Testing Library, Enzyme
- **E2E Testing** — Cypress, Playwright, Puppeteer
- **Visual Regression** — Percy, Chromatic
- **Performance Testing** — Lighthouse CI, WebPageTest
- **TDD / BDD** — Test-driven development methodology

### 8. Architecture & Paradigms
- **Design Patterns** — MVC, MVVM, Observer, Factory, Singleton
- **Functional Programming** — Pure functions, immutability, currying, compose
- **OOP** — SOLID, DRY, encapsulation, polymorphism
- **Micro Frontends** — Module federation, independent deployments
- **Monorepos** — Nx, Turborepo, Lerna

### 9. Team Collaboration
- **Git** — Branching strategies, rebase, merge, Git Flow
- **Code Reviews** — PR best practices, automated checks
- **Documentation** — README, ADRs, Storybook
- **Agile** — Scrum, Kanban, retrospectives
- **Communication** — async/sync tools, RFC process

### 10. Design & UX
- **Color Theory** — Palettes, accessibility contrast ratios
- **Typography** — Scale, variable fonts, font loading
- **Design Systems** — Tokens, component libraries, Storybook
- **Figma** — Component design, prototyping, design-to-code
- **UX Principles** — Mental models, affordances, Gestalt

### 11. The Modern Web
- **Web Assembly** — WASM, Rust/C++ compilation, performance
- **WebRTC** — Peer-to-peer, video/audio, data channels
- **Web Sockets** — Real-time communication
- **Speech Synthesis / Recognition** — Web Speech API
- **Payment Request API** — Web payments standard
- **Credential Management** — Passkeys, WebAuthn
- **Web Bluetooth / USB / NFC**
- **Media Capture** — getUserMedia, Screen Capture, MediaStream

### 12. Algorithms & Data Structures
- **Complexity** — Big O notation, time/space analysis
- **Searching** — Binary search, linear search
- **Sorting** — Quicksort, mergesort, heapsort
- **Trees** — BST, AVL, Red-Black, B-trees
- **Graphs** — BFS, DFS, Dijkstra, A*
- **Dynamic Programming** — Memoization, tabulation
- **Heaps / Priority Queues, Hash Maps, Linked Lists**

### 13. Databases & Servers
- **SQL** — Queries, joins, indexes, transactions, PostgreSQL, MySQL
- **NoSQL** — MongoDB, Redis, Cassandra, DynamoDB
- **ORMs** — Prisma, TypeORM, Sequelize
- **GraphQL** — Schema, resolvers, Apollo, subscriptions
- **REST API design** — Resources, status codes, versioning
- **Node.js** — Express, Fastify, middleware, streams
- **Authentication** — JWT, OAuth2, session management
- **Serverless** — Cloudflare Workers, AWS Lambda, Vercel Functions
- **Deployment** — Docker, Kubernetes, CI/CD, monitoring

## Vollinhalt

Der vollständige Inhalt mit allen kuratierten Links ist in:
`blueprint.md` (3274 Zeilen) im Plugin-Verzeichnis

Quelle: https://github.com/andreasbm/web-skills
