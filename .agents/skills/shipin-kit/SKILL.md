---
name: shipin-kit
description: Integrate AI video generation into Swift/Apple apps using ShipinKit — unified Swift SDK for LumaAI (Dream Machine) and RunwayML (Gen-3 Alpha). Use when building iOS, macOS, tvOS, watchOS, or visionOS apps that need AI video generation. Supports text-to-video, image-to-video, async/await, cancellation, and task management.
license: MIT
metadata:
  author: rryam (Rudrank Riyam)
  version: "1.0.0"
  source: https://github.com/rryam/ShipinKit
compatibility: Swift 6.0+, iOS 16+, macOS 14+, tvOS 16+, watchOS 9+, visionOS 1+
allowed-tools: Read Write Bash(swift:*) Bash(xcodebuild:*)
---

# ShipinKit — Swift SDK for AI Video Generation

Unified Swift interface for LumaAI Dream Machine and RunwayML Gen-3 Alpha.
The name comes from 视频 (shìpín) — Chinese for "video".

## Installation (Swift Package Manager)

In `Package.swift`:
```swift
dependencies: [
    .package(url: "https://github.com/rryam/ShipinKit.git", from: "1.0.0")
]
// Add to target:
.target(name: "YourApp", dependencies: ["ShipinKit"])
```

Or use the local plugin source:
```swift
.package(path: ".agents/plugins/shipin-kit")
```

In Xcode: File → Add Package Dependencies → paste repo URL.

## Quick Start

```swift
import ShipinKit

// --- LumaAI Dream Machine ---
let kit = ShipinKit(service: .lumaAI(apiKey: "your-luma-key"))

let response = try await kit.generate(
    prompt: "A serene lake at sunset with gentle waves",
    aspectRatio: "16:9",
    loop: false,
    keyframes: [:]
)

// --- RunwayML Gen-3 Alpha ---
let kit = ShipinKit(service: .runwayML(apiKey: "your-runway-key"))

let videoURL = try await kit.generate(
    prompt: "A bustling city transforming through seasons",
    aspectRatio: "16:9",
    image: { ShipinImage(uiImage: UIImage(named: "input")!) },
    duration: .short,   // .short (5s) or .long (10s)
    watermark: false,
    seed: 42
) as! URL
```

## LumaAI Direct API

```swift
import ShipinKit

let luma = LumaAI(apiKey: "your-luma-key")

// Text-to-video with keyframes
let generation = try await luma.createGeneration(
    prompt: "Epic mountain landscape with dramatic lighting",
    aspectRatio: "16:9",
    loop: true,
    keyframes: [
        "frame0": LumaAIKeyframeData(type: .generation, url: nil, id: nil),
        "frame1": LumaAIKeyframeData(type: .generation, url: "https://example.com/end.jpg", id: nil)
    ]
)
print("Generation ID:", generation.id)
print("State:", generation.state)

// Get generation status
let updated = try await luma.getGeneration(id: generation.id)

// List all generations
let generations = try await luma.listGenerations(limit: 10, offset: 0)

// Delete a generation
try await luma.deleteGeneration(id: generation.id)
```

## RunwayML Direct API

```swift
import ShipinKit

let runway = RunwayML(apiKey: "your-runway-key")

// Image-to-video from UIImage
let image = UIImage(named: "input-image.jpg")!
let videoURL = try await runway.generateVideo(
    prompt: "Camera slowly pans across the scene",
    image: ShipinImage(uiImage: image),
    duration: .medium,          // .short (5s), .medium, .long (10s)
    aspectRatio: .widescreen,   // .widescreen (16:9), .vertical (9:16)
    watermark: false,
    seed: nil
)

// Image-to-video from URL
let imageURL = URL(string: "https://example.com/image.jpg")!
let videoURL = try await runway.generateVideo(
    prompt: "Slow zoom into the scene",
    image: ShipinImage(url: imageURL),
    duration: .long,
    aspectRatio: .vertical,
    watermark: false
)

// Get task details
let task = try await runway.getTask(id: "task-id")
let description = try await runway.processTask(task)

// Cancel/delete a task
try await runway.cancelTask(id: "task-id")
try await runway.deleteTask(id: "task-id")
```

## SwiftUI Example

```swift
import SwiftUI
import ShipinKit

struct VideoGeneratorView: View {
    @State private var videoURL: URL?
    @State private var isGenerating = false
    @State private var error: Error?

    var body: some View {
        VStack {
            if isGenerating {
                ProgressView("Generating video...")
            } else if let url = videoURL {
                VideoPlayer(player: AVPlayer(url: url))
            }
            Button("Generate") { Task { await generate() } }
        }
    }

    func generate() async {
        isGenerating = true
        defer { isGenerating = false }
        do {
            let kit = ShipinKit(service: .runwayML(apiKey: ProcessInfo.processInfo.environment["RUNWAY_API_KEY"]!))
            videoURL = try await kit.generate(
                prompt: "A peaceful forest with light filtering through the trees",
                image: { ShipinImage(url: URL(string: "https://example.com/forest.jpg")!) },
                duration: .short,
                watermark: false
            ) as? URL
        } catch {
            self.error = error
        }
    }
}
```

## API Keys

| Service | Get Key |
|---------|---------|
| LumaAI | https://lumalabs.ai/dream-machine/api |
| RunwayML | https://app.runwayml.com/account/api-keys |

**Security:** Never hardcode API keys. Use environment variables, Keychain, or a secrets manager.

## Supported Platforms

| Platform | Min Version |
|----------|-------------|
| iOS | 16.0 |
| macOS | 14.0 |
| tvOS | 16.0 |
| watchOS | 9.0 |
| visionOS | 1.0 |
