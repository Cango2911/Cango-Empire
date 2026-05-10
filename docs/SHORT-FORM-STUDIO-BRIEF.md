# CanGo App Empire — „Short-Form AI Studio" (Freebie)
> **Gültiger Workspace:** `/Users/canberkkivilcim/PycharmProjects/Cango-Empire`
> Alle Pfade relativ zu diesem Root. Design-Tokens aus `website/index.html`.

---

## Stack-Kontext

- Reines HTML/CSS/JS — kein Node/React/Next.js
- Python-Backend-Scripts + Docker (`docker/docker-compose.yml`) auf Hostinger-VPS
- Design-System: `--gray-950: #030712`, `--primary-500: #F97316` (Orange), `--accent-500: #EF4444` (Rot)
- Fonts: `Instrument Sans` + `JetBrains Mono`
- Deployment: statische Dateien unter `website/`

---

## Ziel

Neue Seite `website/short-form-studio.html` als eigenständiges Freebie (kein Login erforderlich).

**UX-Referenz:**
- **Opus Clip** → Clip-Vorschläge mit Score aus langem Video
- **Caption AI** → Untertitel-Presets, Timing, Preview, burned-in Export
- **Kling AI** → optionale KI-B-Roll pro Segment (Feature-Flag, MVP deaktiviert)

Alles in einer durchgängigen User-Journey:
**Upload → Analyse → Captions → Export**

Brand: **CanGo App Empire** — Enterprise Dark, Orange-Akzente, keine Spielzeug-Optik.

---

## Phase 0 — Vor dem ersten Code

1. `website/index.html` lesen (Design-Tokens, Klassen-Konventionen)
2. `docker/docker-compose.yml` lesen (Dienste + Ports für Backend-Entscheidung)
3. Entscheidung: **ffmpeg.wasm** (vollständig clientseitig) **oder** **Python-FastAPI + ffmpeg** (Docker-Service)
   - Empfehlung: `ffmpeg.wasm` für MVP — kein Server-Aufwand, kein Auth nötig
   - Begründung in max. 8 Zeilen dokumentieren bevor Code beginnt

---

## UI-Flow (5 Steps)

### STEP 1 — INGEST

- Drag & Drop Zone: „Langes Video, Rohmaterial oder nur Skript — wir machen Shorts daraus."
- Akzeptiert: MP4/MOV (max. 500 MB) + Text/Skript (Textarea Fallback)
- Preset-Buttons: `TikTok` | `Reels` | `Shorts` (alle 9:16 — nur Metadaten-Label)
- Ziel-Länge pro Short: `15s` / `30s` / `60s` / `90s` (Toggle-Chips)

### STEP 2 — ANALYZE (Opus-Clip-artig)

- Transkription: MVP → Segment-Text aus Skript-Textarea (Whisper.wasm als optionale Erweiterung)
- Ausgabe: **Liste von Clip-Vorschlägen** — je Karte:
  - Clip-Titel (auto aus erstem Satz)
  - **Hook-Score 0–100** (Heuristik: Frage=+20, Zahl=+15, Kontrast-Wort=+10, Imperativ=+10 …)
  - Start/End Timestamp (editierbar, Range-Slider)
  - `reason` — ein Satz warum viral/klickstark
  - Tag: `[Aufreger | Beweis | FOMO | Mensch]` (auto + editierbar)
- Aktionen je Karte: ✓ Übernehmen | ✂ Trimmen | ⊕ Duplizieren | ✕ Löschen
- Sortierung per Drag & Drop

**Datenmodell (JSDoc):**
```js
/**
 * @typedef {{ id: string, title: string, hookScore: number,
 *             startMs: number, endMs: number, reason: string,
 *             tag: 'aufreger'|'beweis'|'fomo'|'mensch',
 *             captions: CaptionToken[] }} ClipSuggestion
 *
 * @typedef {{ text: string, startMs: number, endMs: number,
 *             styleId: string }} CaptionToken
 */
```

### STEP 3 — CAPTION STUDIO (Caption-AI-artig)

- Caption-Track pro Clip: aus Segment-Text (phrasenweise, 3–6 Wörter pro Frame)
- **Presets (visuell als Kacheln auswählbar):**
  - „CanGo Bold" — weiß/orange, fett, shadow, unteres Drittel
  - „Empire Yellow" — gelb Keyword-Highlight, dunkle bg-pill
  - „Clean White" — weiß, leicht transparent bg, universell
  - „Breaking News" — Großbuchstaben, roter Balken oben
- Caption-Editor: Timing-Verschiebung per Slider, Text inline editierbar
- **Safe Zone Overlay:** roter Rahmen zeigt TikTok-/Reels-UI-Bereiche (oben 15%, unten 20%)
- Live-Preview: 9:16 Canvas (`<canvas>` oder `<video>` + Overlay-DIV)

### STEP 4 — VISUAL / KI-LANE (Feature-Flag `AI_VISUAL=0`)

Pro Segment Quelle wählen:
- [x] Originalvideo-Segment (Smart Crop auf 9:16)
- [x] Bild-Upload + Ken-Burns-Effekt (CSS Animation)
- [ ] KI-B-Roll (MVP deaktiviert — Button greyed-out: „Kommt bald — KI-Szenen via Kling API")

Wenn `AI_VISUAL=1` (Umgebungsvariable):
- Prompt-Feld + API-Key aus ENV → KI-Video-API-Call → Clip einbetten

### STEP 5 — EXPORT

- Pro Clip: **9:16 MP4 Download** + optional **SRT-Datei** (Checkbox)
- Batch: alle genehmigten Clips als **ZIP**
- Export-Engine: `ffmpeg.wasm` (bevorzugt) oder `/api/export` Python-Route
- Progress: Fortschrittsbalken in `--primary-500` Orange, Abbruch-Button, Retry bei Fehler
- **Rate-Limit Client-Hint** (kein Hard-Block): `localStorage`-Check — nach 5 Exports/Tag:
  > „Du hast das Daily-Limit erreicht. Morgen wieder — oder hol dir die Pro-Version."

---

## Design-Vorgaben

```css
/* Exakt aus website/index.html übernehmen — NICHT neu erfinden */
--bg-base:    #030712;   /* gray-950  */
--primary:    #F97316;   /* orange    */
--accent:     #EF4444;   /* rot       */
--font-sans:  'Instrument Sans', sans-serif;
--font-mono:  'JetBrains Mono', monospace;

/* Komponenten-Pattern */
border-radius: 12px;
border: 1px solid rgba(255,255,255,0.08);
/* Hover-Glow */
box-shadow: 0 0 0 1px var(--primary);
```

- Navigation: identischer Header wie `index.html` — Link „Studio" als aktiv markieren
- Footer: identisch zu bestehenden Seiten
- Mobile-first: Stepper vertikal auf <768px, Preview neben Editor ab 1024px
- Kein Tailwind (nicht im Projekt) — reines CSS im `<style>`-Tag oder separates `.css`

---

## Texte / Copy (Deutsch, CanGo-Stil)

| Element | Text |
|---|---|
| Headline | **„Mach aus einem langen Video 10 Shorts. In Minuten. Kostenlos."** |
| Subline | „Upload. KI analysiert. Captions drauf. Export. Fertig." |
| Upload-CTA | „Video reinziehen oder klicken" |
| Analyse-Button | „Shorts vorschlagen lassen" |
| Export-Button | „Clip herunterladen" |
| Lead-Slot | `<!-- LEAD_MAGNET_SLOT -->` nach erstem erfolgreichen Download |

Lead-Magnet ist **optional** — kein Pflicht-Gate vor dem Export.

---

## Dateisystem-Ausgabe

```
website/
  short-form-studio.html     ← Hauptseite + Navigation-Link
  css/
    short-form-studio.css    ← falls Style zu groß für inline
  js/
    studio-core.js           ← Datenmodell, Segment-Splitting, Hook-Score-Heuristik
    studio-analyze.js        ← Transkript-Fallback, Clip-Vorschläge
    studio-captions.js       ← Caption-Editor, Presets, Safe-Zone-Overlay
    studio-export.js         ← ffmpeg.wasm Wrapper + ZIP-Builder
docs/
  SHORT-FORM-STUDIO.md       ← Setup, ENV-Variablen, Export-Pfad, Limits (nach Impl.)
```

Nav-Link auch eintragen in:
- `website/index.html` (Header-Navigation)
- `website/blogs.html` (Header-Navigation)

---

## Akzeptanzkriterien

1. Skript-Textarea → segmentierte Clip-Liste mit Hook-Scores sichtbar
2. Caption-Preset wechseln → Preview-Canvas aktualisiert sofort
3. Export eines Clips: 9:16 MP4 mit burned-in Captions herunterladbar
4. Seite öffnet ohne Server (`file://`) — Steps 1–3 vollständig funktional
5. Branding durchgehend CanGo App Empire (kein generisches „AI Studio")
6. Kein API-Key im Client — KI-Keys nur in ENV / Docker-Secret
7. Responsive auf 375px Breite ohne horizontalen Scroll

---

## Arbeitsweise (Reihenfolge einhalten)

1. Architektur-Notiz (max. 10 Zeilen) + vollständige Dateiliste
2. `studio-core.js` — Datenmodell + Splitting-Logik + Unit-Tests
3. HTML-Skeleton + CSS-Design-System (Design-Tokens aus `index.html`)
4. `studio-analyze.js` → `studio-captions.js` → `studio-export.js`
5. Vollständige Integration in `short-form-studio.html`
6. Nav-Links in `index.html` + `blogs.html` eintragen
7. `docs/SHORT-FORM-STUDIO.md` (Setup-Doku) erstellen

---

## Demo-Checkliste (manuelle Abnahme nach Implementierung)

1. [ ] Seite öffnet in Chrome ohne Konsolenfehler (`file://` oder localhost)
2. [ ] Skript eingeben → „Shorts vorschlagen lassen" → mind. 2 Clip-Karten erscheinen mit Hook-Score
3. [ ] Clip-Karte trimmen (Range-Slider) → Timestamp-Änderung wird in Karte angezeigt
4. [ ] Caption-Preset „Empire Yellow" wählen → Preview-Canvas ändert Style sofort
5. [ ] Einzelnen Clip exportieren → MP4-Download startet, Progress-Balken sichtbar
6. [ ] Alle Clips als ZIP exportieren → ZIP enthält alle MP4-Dateien
7. [ ] Auf iPhone-Viewport (375px) — kein horizontaler Scroll, alle Steps bedienbar
