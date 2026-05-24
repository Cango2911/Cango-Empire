---
name: mcp-kling
description: Use Kling AI video and image generation directly in Claude via MCP. Use this skill to generate videos from text or images, extend videos, add lip-sync, apply video effects, generate images, perform virtual try-on, and manage Kling AI account resources — all through natural conversation. Requires MCP server setup with KLING_ACCESS_KEY and KLING_SECRET_KEY.
license: MIT
metadata:
  author: Boris Djordjevic / 199 Longevity
  version: "5.2.0"
  npm: mcp-kling
  source: https://github.com/199-mcp/mcp-kling
compatibility: Node.js 18+. Requires Kling AI API credentials (Access Key + Secret Key).
allowed-tools: Bash(npx:*) Bash(npm:*) Read Write
---

# MCP Kling — Kling AI MCP Server

Full Model Context Protocol server for Kling AI — 12 tools covering video generation, image generation, lip-sync, effects, virtual try-on, and account management.

## Setup

### Option A — Claude Desktop (recommended)

Add to `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS)
or `%APPDATA%\Claude\claude_desktop_config.json` (Windows):

```json
{
  "mcpServers": {
    "mcp-kling": {
      "command": "npx",
      "args": ["-y", "mcp-kling@latest"],
      "env": {
        "KLING_ACCESS_KEY": "your_access_key",
        "KLING_SECRET_KEY": "your_secret_key",
        "KLING_AUTO_DOWNLOAD": "true",
        "KLING_DOWNLOAD_PATH": "/Users/you/Downloads/kling"
      }
    }
  }
}
```

### Option B — Local source (from plugin)

```bash
cd .agents/plugins/mcp-kling
npm install
npm run build
```

Then in Claude Desktop config:
```json
{
  "mcpServers": {
    "mcp-kling": {
      "command": "node",
      "args": ["/path/to/.agents/plugins/mcp-kling/dist/index.js"],
      "env": {
        "KLING_ACCESS_KEY": "your_access_key",
        "KLING_SECRET_KEY": "your_secret_key"
      }
    }
  }
}
```

### Get API Keys

1. Go to https://app.klingai.com/global/dev/api-key
2. Click **"+ Create a new API Key"**
3. Save both **Access Key** and **Secret Key**

JWT tokens are auto-generated per request — no manual token management needed.

## Available Tools (12)

### Video Generation

| Tool | Description |
|------|-------------|
| `generate_video` | Text-to-video — prompt → video (v1.0/1.5/1.6/v2-master, 5s/10s, 16:9/9:16/1:1, standard/professional) |
| `generate_image_to_video` | Image-to-video — static image → dynamic video with motion control |
| `check_video_status` | Poll generation status + auto-download completed video |
| `extend_video` | Extend an existing video by 4–5 seconds with optional prompt |
| `apply_video_effect` | Apply cinematic effects: blur, zoom, pan, color grading |

### Image Generation

| Tool | Description |
|------|-------------|
| `generate_image` | Text-to-image with Kolors model (various ratios, batch count) |
| `check_image_status` | Poll image generation status + auto-download |

### Creative Tools

| Tool | Description |
|------|-------------|
| `create_lipsync` | Add lip-sync audio to a video from audio URL or TTS text |
| `virtual_try_on` | AI virtual clothing try-on — person image + garment image → result |

### Account Management

| Tool | Description |
|------|-------------|
| `get_account_balance` | Check remaining credits and billing info |
| `get_resource_packages` | List subscribed resource packages |
| `list_tasks` | List recent video/image tasks with status |

## Example Conversations

```
"Generate a 10-second cinematic video of a sunset over the ocean in 16:9"
→ uses generate_video with model kling-v1.6, duration=10, mode=professional

"Turn this image of my cat into a video where it's running"
→ uses generate_image_to_video with motion prompt

"Extend the video I just generated with a zoom-out effect"
→ uses extend_video with the task_id from the previous generation

"Add the voiceover 'Welcome to our product demo' to the video"
→ uses create_lipsync with TTS text

"Show me how this shirt would look on this person"
→ uses virtual_try_on with person_image_url + garment_image_url

"How many credits do I have left?"
→ uses get_account_balance
```

## Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `KLING_ACCESS_KEY` | Yes | — | Kling API Access Key |
| `KLING_SECRET_KEY` | Yes | — | Kling API Secret Key |
| `KLING_AUTO_DOWNLOAD` | No | `true` | Auto-download completed media |
| `KLING_DOWNLOAD_PATH` | No | `~/Downloads/kling-videos` | Where to save downloads |

## Supported Models

| Type | Models |
|------|--------|
| Video | kling-v1, kling-v1.5, kling-v1.6, kling-v2-master |
| Image | Kolors (KOLORS model) |
