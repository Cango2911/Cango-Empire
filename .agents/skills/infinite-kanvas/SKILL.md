---
name: infinite-kanvas
description: Deploy and use Infinite Kanvas — an infinite canvas image editor with AI transformations powered by fal.ai. Use this skill when setting up, configuring, or extending the Infinite Kanvas Next.js app. Features include AI style transfer (Flux Kontext LoRA), background removal, image-to-video, video-to-video, real-time streaming, and multi-image manipulation on an infinite canvas.
license: MIT
metadata:
  author: fal-ai-community
  source: https://github.com/fal-ai-community/infinite-kanvas
compatibility: Node.js 20+. Requires FAL_KEY from fal.ai. Optional KV store (Upstash) for rate limiting.
allowed-tools: Bash(npm:*) Bash(npx:*) Read Write Edit
---

# Infinite Kanvas

Infinite canvas image editor with AI transformations via fal.ai.
Built with Next.js 15, React Konva, tRPC, Tailwind CSS.

## Setup

```bash
cd .agents/plugins/infinite-kanvas
npm install
```

Configure `.env`:
```env
FAL_KEY=your_fal_api_key

# Optional — Upstash KV for rate limiting (users without own key)
KV_REST_API_URL=https://your-kv.upstash.io
KV_REST_API_TOKEN=your_kv_token

NEXT_PUBLIC_APP_URL=http://localhost:3000
```

Get FAL_KEY: https://fal.ai/dashboard/keys

```bash
npm run dev      # http://localhost:3000
npm run build    # Production build
npm run start    # Serve production build
```

## Features

### Canvas
- Infinite pan/zoom canvas (React Konva)
- Drag & drop image upload
- Multi-select, move, resize, crop images
- Auto-save to IndexedDB (browser local storage)
- Undo/redo support
- Viewport culling for performance with many images

### AI Transformations (via fal.ai)

| Feature | Model | Description |
|---------|-------|-------------|
| Style Transfer | Flux Kontext LoRA | Apply 20+ art styles: anime, ghibli, pixel, clay, lego, watercolor, charcoal, etc. |
| Background Removal | fal-ai/birefnet | Isolate subjects, transparent background |
| Image Generation | Flux models | Text-to-image on canvas |
| Image-to-Video | Kling, Wan, etc. | Animate canvas images |
| Video-to-Video | Video models | Transform existing video |
| Extend Video | Kling extend | Add more seconds to a video |
| Face Retouch | Detailer model | Enhance facial detail |

### Available Style Presets
3D, abstract, American cartoon, anime, big head, charcoal, clay, cubist, detail enhancer, face retoucher, fluffy, Ghibli, glass prism, impressionist, JoJo, LEGO, light fix, low poly, minimalist, mosaic art, overlay, pencil drawing, pixel, plushie, Simpsons, Snoopy, watercolor, Wojak

### Architecture

**Proxy pattern** — uploads go through `/api/fal` proxy to bypass Vercel's 4.5MB request body limit:
```
Client → /api/fal (Next.js proxy) → fal.ai CDN
```

**Rate limiting** (3-tier, for users without own key):
- 5 requests/minute
- 15 requests/hour  
- 50 requests/day

Users with their own `FAL_KEY` (set in app settings) bypass all limits.

**Real-time streaming** — image generation streams live updates via fal.ai's streaming API.

**tRPC** — type-safe API layer between frontend and fal.ai.

## Deployment

### Vercel (recommended)
```bash
# Set env vars in Vercel dashboard
FAL_KEY=...
KV_REST_API_URL=...
KV_REST_API_TOKEN=...
NEXT_PUBLIC_APP_URL=https://your-domain.vercel.app
```

### Docker / Self-hosted
```bash
npm run build
npm run start  # port 3000
```

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Framework | Next.js 15 (App Router) |
| Canvas | React Konva |
| API | tRPC |
| Styling | Tailwind CSS + shadcn/ui |
| State | Zustand (canvas store) |
| Storage | IndexedDB (auto-save) |
| AI | fal.ai (Flux, Kling, Wan, BiRefNet) |
| Rate limit | Upstash KV (optional) |
| Runtime | Node.js 20+ |
