---
name: video-starter-kit
description: Deploy and use the AI Video Starter Kit — a browser-native video studio with timeline editor and 20+ AI models via fal.ai. Use this skill when building, running, or extending the video-starter-kit Next.js app. Features include multi-track video composition (Remotion), AI image/video/music/voiceover generation, keyframe timeline, IndexedDB auto-save, and optional file upload and sharing.
license: MIT
metadata:
  author: fal-ai-community
  source: https://github.com/fal-ai-community/video-starter-kit
compatibility: Node.js 20+. Requires FAL_KEY from fal.ai. Optional UploadThing token and Upstash KV for upload/sharing.
allowed-tools: Bash(npm:*) Bash(npx:*) Read Write Edit
---

# AI Video Starter Kit

Browser-native video studio with AI model integration via fal.ai.
Built with Next.js 14, Remotion, Tailwind CSS, and shadcn/ui.

## Setup

```bash
cd .agents/plugins/video-starter-kit
npm install
```

Configure `.env`:
```env
# Required — fal.ai API key: https://fal.ai/dashboard/keys
FAL_KEY=your_fal_api_key

# Optional — UploadThing for file upload: https://uploadthing.com
UPLOADTHING_TOKEN=

# Optional — Upstash KV for share links: https://upstash.com
KV_URL=
KV_REST_API_READ_ONLY_TOKEN=
KV_REST_API_TOKEN=
KV_REST_API_URL=
```

```bash
npm run dev      # http://localhost:3000
npm run build    # Production build
npm run start    # Serve production build
```

## Features

### Timeline Editor
- Multi-track composition: video, music, voiceover tracks
- Keyframe-based clip system with timestamps and durations
- Drag-and-drop media from gallery onto timeline
- Browser-native video rendering via Remotion

### Storage
- Auto-save to IndexedDB (no cloud DB required)
- UploadThing for file uploads (optional, requires `UPLOADTHING_TOKEN`)
- Share links via Upstash KV (optional, requires KV env vars)

### AI Models (via fal.ai)

| Category | Model | Endpoint |
|----------|-------|----------|
| Image | Flux Dev | `fal-ai/flux/dev` |
| Image | Flux Schnell | `fal-ai/flux/schnell` |
| Image | Flux Pro 1.1 Ultra | `fal-ai/flux-pro/v1.1-ultra` |
| Image | Stable Diffusion 3.5 Large | `fal-ai/stable-diffusion-v35-large` |
| Video | Minimax Video 01 Live | `fal-ai/minimax/video-01-live` |
| Video | Hunyuan | `fal-ai/hunyuan-video` |
| Video | Kling 1.5 Pro | `fal-ai/kling-video/v1.5/pro` |
| Video | Kling 1.0 Standard | `fal-ai/kling-video/v1/standard/text-to-video` |
| Video | Luma Dream Machine 1.5 | `fal-ai/luma-dream-machine` |
| Video | LTX Video v0.95 | `fal-ai/ltx-video-v095/multiconditioning` |
| Video | Veo 2 | `fal-ai/veo2` |
| Video | Topaz Video Upscale | `fal-ai/topaz/upscale/video` |
| Video | Lipsync (sync.so) | `fal-ai/sync-lipsync` |
| Audio | MMAudio V2 | `fal-ai/mmaudio-v2` |
| Music | Minimax Music | `fal-ai/minimax-music` |
| Music | Stable Audio | `fal-ai/stable-audio` |
| Voiceover | PlayHT TTS v3 | `fal-ai/playht/tts/v3` |
| Voiceover | PlayAI Dialog | `fal-ai/playai/tts/dialog` |
| Voiceover | F5 TTS | `fal-ai/f5-tts` |

### Architecture

**Proxy pattern** — fal.ai calls route through `/api/fal` server proxy:
```
Client → /api/fal (Next.js) → fal.ai
```
FAL_KEY is stored in localStorage (entered via key dialog) and used by the proxy.

**Data model** (IndexedDB via `idb`):
- `VideoProject` — title, description, aspectRatio (16:9 / 9:16 / 1:1)
- `VideoTrack` — type: video | music | voiceover
- `VideoKeyFrame` — timestamp, duration, data (prompt | image | video | voiceover | music)
- `MediaItem` — status: pending | running | completed | failed, url, input/output

**Key source files:**
- `src/lib/fal.ts` — fal.ai client + `AVAILABLE_ENDPOINTS` registry
- `src/data/schema.ts` — TypeScript types for project/track/keyframe/media
- `src/data/store.ts` — Zustand state management
- `src/data/db.ts` — IndexedDB operations via idb
- `src/data/mutations.ts` — CRUD operations
- `src/lib/ffmpeg.ts` — Browser-side ffmpeg for video processing
- `src/components/video/timeline.tsx` — Timeline editor UI
- `src/components/left-panel.tsx` — Media gallery + generation panel
- `src/components/right-panel.tsx` — Settings and export panel

## Deployment

### Vercel (recommended)
Set env vars in Vercel dashboard:
```
FAL_KEY=...
UPLOADTHING_TOKEN=...  # optional
KV_URL=...             # optional — for share links
KV_REST_API_TOKEN=...
KV_REST_API_URL=...
```

### Docker / Self-hosted
```bash
npm run build
npm run start  # port 3000
```

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Framework | Next.js 14 (App Router) |
| Video | Remotion 4.x |
| Styling | Tailwind CSS + shadcn/ui |
| State | Zustand |
| Storage | IndexedDB (idb, auto-save) |
| AI | fal.ai (20+ models) |
| Upload | UploadThing (optional) |
| Share | Upstash KV (optional) |
| Runtime | Node.js 20+ |
