---
name: ffmpeg-asm-lessons
version: 1.0.0
description: "FFmpeg School of Assembly Language — 3 Lektionen für x86-64 SIMD-Assembly in FFmpeg-Stil. Themen: GPR/SIMD-Register (xmm/ymm/zmm), x86inc.asm-Abstraktionsschicht, SIMD-Funktionen (paddb, movu, pxor), Schleifen/Sprünge/FLAGS, Konstanten (SECTION_RODATA, db/dw), Memory-Addressing [base+scale*index+disp], LEA, Instruktions-Sets (MMX→AVX512ICL), Pointer-Offset-Trick, Alignment (mova/movu), Range Extension (punpcklbw/punpckhbw), Sign Extension (pcmpgtb), Packing (packuswb), Shuffles (pshufb)."
author: FFmpeg Project (Open Source)
source: https://github.com/FFmpeg/asm-lessons
license: unknown
type: agent-skill
tags:
  - assembly
  - asm
  - simd
  - x86
  - x86-64
  - ffmpeg
  - performance
  - multimedia
  - low-level
---

# FFmpeg School of Assembly Language

## Übersicht

Diese Lektion-Sammlung vom FFmpeg-Projekt lehrt x86-64 SIMD-Assembly in dem Stil, wie er in FFmpeg, x264 und dav1d verwendet wird. Zielgruppe: C-Entwickler mit Zeigerkenntnis und Schulmathematik.

**Voraussetzungen**: C-Kenntnisse (insbesondere Zeiger), Schulmathematik  
**Ziel**: SIMD-Assembly-Funktionen für FFmpeg schreiben können  
**Discord**: https://discord.com/invite/Ks5MhUhqfB

---

## Lektion 1 — Grundlagen, Register, erste SIMD-Funktion

### Was ist Assembly?

Assembly ist eine Programmiersprache, die direkt auf CPU-Instruktionen abgebildet wird. In FFmpeg ist fast alles **SIMD (Single Instruction Multiple Data)** — eine Instruktion verarbeitet mehrere Datenpunkte gleichzeitig (Vektorprogrammierung).

**Warum Assembly?** 10× oder mehr Geschwindigkeitszuwachs bei Multimedia-Verarbeitung. Compiler-Intrinsics sind typisch 10–15% langsamer als handgeschriebenes Assembly.

**Syntax**: Intel-Syntax (nicht AT&T). Lowercase-Mnemonics, Großbuchstaben für Makros.

### Register

#### General Purpose Registers (GPR)

Enthält entweder Daten (bis 64-bit) oder Speicheradressen. x86inc.asm benennt sie als `r0`, `r1`, `r2`, ... (Scaffolding — Abstraktionsschicht).

Suffix `q` = als Quadword verwenden: `r0q`

#### SIMD/Vektorregister

| Register | Größe | Anmerkung |
|----------|-------|-----------|
| `mm0`–`mm7` | 64-bit (MMX) | historisch |
| `xmm0`–`xmm15` | 128-bit (SSE) | Standard |
| `ymm0`–`ymm15` | 256-bit (AVX2) | weit verbreitet |
| `zmm0`–`zmm31` | 512-bit (AVX-512) | limitierte Verfügbarkeit |

**Datentypen** (bold = Suffix-Buchstabe in Mnemonics):

| Name | Größe |
|------|-------|
| **b**yte | 8-bit |
| **w**ord | 16-bit |
| **d**oubleword | 32-bit |
| **q**uadword | 64-bit |
| **d**ouble**q**uadword | 128-bit |

xmm-Register als Byte-Tabelle (16 Einträge), als Word (8), als DWord (4), als QWord (2).

### x86inc.asm

Leichtgewichtige Abstraktionsschicht für FFmpeg/x264/dav1d:
- GPRs als `r0`–`rN` (kein Merken von Registernamen)
- Makros: `INIT_XMM`, `cglobal`, `RET`, `SECTION_RODATA`, `mmsize`
- Vektorregister als `m0`–`mN` (abstrakt für xmm/ymm/zmm)
- Automatic CPU-Detection-kompatibel

### Einfaches Skalares Snippet

```assembly
mov  r0q, 3   ; r0q = 3
inc  r0q      ; r0q = 4
dec  r0q      ; r0q = 3
imul r0q, 5  ; r0q = 15
```

Intel-Syntax: Ziel links, Quelle rechts — wie `memcpy`.

### Erste SIMD-Funktion

```assembly
%include "x86inc.asm"

SECTION .text

;static void add_values(uint8_t *src, const uint8_t *src2)
INIT_XMM sse2
cglobal add_values, 2, 2, 2, src, src2
    movu  m0, [srcq]    ; 128-bit Load aus src
    movu  m1, [src2q]   ; 128-bit Load aus src2
    paddb m0, m1         ; 16 Bytes addieren (parallel!)
    movu  [srcq], m0    ; Store zurück
    RET
```

**Erklärung**:
- `INIT_XMM sse2` — XMM-Register mit SSE2-Instruktionen
- `cglobal add_values, 2, 2, 2, src, src2` — C-Funktion, 2 Args, 2 GPRs, 2 XMM-Regs, Labels
- `movu` — movdqu (128-bit unaligned load/store). `[srcq]` = Dereferenzierung wie `*src` in C
- `paddb` — **p**acked **add** **b**ytes: jedes der 16 Bytes wird parallel addiert
- `m0`, `m1` = abstrahierte Vektorregister (xmm0, xmm1 bei INIT_XMM)
- `RET` — Makro für Rücksprung

---

## Lektion 2 — Schleifen, Konstanten, Offsets, LEA

### Labels und Sprünge

```assembly
; Einfache Endlosschleife (nur Illustration):
mov  r0q, 3
.loop:
    dec  r0q
    jmp .loop
```

`.loop:` = lokales Label (wiederverwendbar über Funktionen hinweg).

### FLAGS-Register und bedingte Sprünge

`dec`, `add`, `cmp`, `inc` setzen FLAGS automatisch:

```assembly
; Countdown-Schleife (äquivalent zu do-while):
mov  r0q, 3
.loop:
    ; do something
    dec  r0q
    jg  .loop  ; jump if greater than zero
```

Äquivalent zu C: `int i = 3; do { ...; i--; } while(i > 0);`

```assembly
; Aufwärts-Zähler mit cmp:
xor r0q, r0q   ; r0q = 0 (schneller als mov r0q, 0)
.loop:
    ; do something
    inc r0q
    cmp r0q, 3
    jl  .loop   ; jump if r0q < 3
```

**`xor r0q, r0q`** = schnelles Null-Setzen (kein Load). Für SIMD: `pxor m0, m0`.

#### Sprung-Mnemonics

| Mnemonic | Bedeutung | FLAGS |
|----------|-----------|-------|
| `JE/JZ` | Equal/Zero | ZF=1 |
| `JNE/JNZ` | Not Equal/Not Zero | ZF=0 |
| `JG/JNLE` | Greater (signed) | ZF=0 and SF=OF |
| `JGE/JNL` | Greater or Equal (signed) | SF=OF |
| `JL/JNGE` | Less (signed) | SF≠OF |
| `JLE/JNG` | Less or Equal (signed) | ZF=1 or SF≠OF |

### Konstanten (Read-Only Data)

```assembly
SECTION_RODATA

constants_1: db 1,2,3,4         ; uint8_t  constants_1[4] = {1,2,3,4}
constants_2: times 2 dw 4,3,2,1 ; uint16_t constants_2[8] = {4,3,2,1,4,3,2,1}
```

- `SECTION_RODATA` = plattformunabhängiges Makro für Read-Only-Daten
- `db` = declare byte, `dw` = declare word, `dd` = declare doubleword
- `times N` = Wiederholung der Deklaration

### Memory Addressing

```assembly
[base + scale*index + disp]
```

| Teil | Beschreibung |
|------|-------------|
| `base` | GPR (meist Zeiger aus C-Argument) |
| `scale` | 1, 2, 4 oder 8 (default: 1) |
| `index` | GPR (meist Loop-Counter) |
| `disp` | Ganzzahl bis 32-bit (Offset) |

`mmsize` = Makro für die Größe des aktiven SIMD-Registers (16 bei XMM, 32 bei YMM).

```assembly
;static void simple_loop(const uint8_t *src)
INIT_XMM sse2
cglobal simple_loop, 1, 2, 2, src
     movq r1q, 3
.loop:
     movu m0, [srcq]
     movu m1, [srcq+2*r1q+3+mmsize]
     ; ...
     add srcq, mmsize
     dec r1q
     jg .loop
     RET
```

### LEA — Load Effective Address

Multiplikation und Addition in einer Instruktion. Verändert FLAGS nicht, beeinflusst Quellregister nicht.

```assembly
lea r0q, [base + scale*index + disp]

; Beispiel: r0q = r1q + 8*r2q + 5
lea r0q, [r1q + 8*r2q + 5]

; Ohne LEA (4 Instruktionen statt 1):
movq r0q, r1q
movq r3q, r2q
sal  r3q, 3    ; * 8
add  r3q, 5
add  r0q, r3q
```

**scale-Werte**: 1, 2, 4, 8 (passend zu Byte/Word/DWord/QWord-Alignment).

---

## Lektion 3 — Instruktions-Sets, Pointer-Trick, Alignment, Range Extension, Shuffles

### Instruktions-Set-Geschichte (x86 SIMD)

| Set | Jahr | Register | Wichtigstes Feature |
|-----|------|----------|---------------------|
| MMX | 1997 | mm (64-bit) | Erstes SIMD in Intel |
| SSE | 1999 | xmm (128-bit) | — |
| SSE2 | 2000 | xmm | Viele neue Instruktionen |
| SSE3 | 2004 | xmm | Erste horizontale Instruktionen |
| SSSE3 | 2006 | xmm | **pshufb** (wichtigste Video-Instruktion!) |
| SSE4 | 2008 | xmm | min/max für packed integers |
| AVX | 2011 | ymm (256-bit) | Drei-Operanden-Syntax, float only |
| AVX2 | 2013 | ymm | 256-bit Integer-Instruktionen |
| AVX-512 | 2017 | zmm (512-bit) | Operation masks, vpermb |
| AVX512ICL | 2019 | zmm | Kein Takt-Downscaling mehr |
| AVX10 | upcoming | — | — |

**CPU-Verfügbarkeit** (Steam Survey Nov 2024):

| Set | Verfügbarkeit |
|-----|--------------|
| SSE2 | 100% |
| SSE3 | 100% |
| SSSE3 | 99.86% |
| SSE4.1 | 99.80% |
| AVX | 97.39% |
| AVX2 | 94.44% |
| AVX-512 | 14.09% |

FFmpeg erkennt CPU-Fähigkeiten zur Laufzeit und wählt die optimale Funktion.

### Pointer-Offset-Trick (Schleife ohne cmp)

```assembly
;static void add_values(uint8_t *src, const uint8_t *src2, ptrdiff_t width)
INIT_XMM sse2
cglobal add_values, 3, 3, 2, src, src2, width
   add srcq, widthq     ; Zeiger ans Ende verschieben
   add src2q, widthq
   neg widthq            ; width negieren

.loop:
    movu  m0, [srcq+widthq]    ; Lade von (Ende - |width|)
    movu  m1, [src2q+widthq]
    paddb m0, m1
    movu  [srcq+widthq], m0
    add   widthq, mmsize        ; width nähert sich 0
    jl .loop                    ; springe wenn width noch < 0

    RET
```

**Trick**: `widthq` dient gleichzeitig als Zeigeroffset UND Loop-Counter. Spart `cmp`-Instruktion.  
`ptrdiff_t` statt `int` vermeidet obere 32-bit Probleme bei 64-bit Zeigerarithmetik.

### Alignment

- `movu` = Unaligned Load/Store (movdqu)
- `mova` = Aligned Load/Store (movdqa) — schneller, aber Segfault bei falschem Alignment!
- Alignment = SIMD-Registergröße: 16 Byte (XMM), 32 Byte (YMM), 64 Byte (ZMM)
- `av_malloc` in FFmpeg liefert aligned Speicher
- `DECLARE_ALIGNED` für Stack-Variablen

```assembly
SECTION_RODATA 64   ; RODATA 64-Byte-aligned
```

### Range Extension (Byte → Word)

Overflow-Schutz: Byte (0–255) auf Word (0–65535) erweitern für Zwischenrechnungen.

#### Zero Extension (unsigned bytes)

```assembly
pxor      m2, m2      ; m2 = 0

movu      m0, [srcq]  ; 16 Bytes laden
movu      m1, m0      ; Kopie in m1

punpcklbw m0, m2      ; Low-Bytes zero-extend → Words in m0
punpckhbw m1, m2      ; High-Bytes zero-extend → Words in m1
```

**punpcklbw**: Interleaved die Low-Bytes aus `dst` mit Bytes aus `src` (hier 0). Ergebnis: unsigned Bytes als Words.

#### Sign Extension (signed bytes)

```assembly
pxor      m2, m2
movu      m0, [srcq]
movu      m1, m0

pcmpgtb   m2, m0      ; m2[i] = (0 > src[i]) ? 0xFF : 0x00
punpcklbw m0, m2      ; Low-Bytes sign-extend
punpckhbw m1, m2      ; High-Bytes sign-extend
```

Eine Instruktion mehr als unsigned — `pcmpgtb` erzeugt das Vorzeichen-Byte.

### Packing (Word → Byte, zurück)

```assembly
packuswb dst, src   ; Words → unsigned bytes (saturiert bei Überlauf)
packsswb dst, src   ; Words → signed bytes (saturiert)
```

### Shuffles — pshufb (SSSE3)

Die wichtigste Instruktion in der Videoverarbeitung. Permutiert Bytes anhand eines Masken-Registers.

```
dst[i] = (src[i] & 0x80) ? 0 : dst[src[i]]
```

Äquivalenter C-Code (in SIMD parallel):
```c
uint8_t tmp[16];
memcpy(tmp, dst, 16);
for(int i = 0; i < 16; i++) {
    dst[i] = (src[i] & 0x80) ? 0 : tmp[src[i]];
}
```

```assembly
SECTION_DATA 64

shuffle_mask: db 4, 3, 1, 2, -1, 2, 3, 7, 5, 4, 3, 8, 12, 13, 15, -1
; -1 als Byte = 0b11111111 → MSB gesetzt → Output-Byte wird 0

section .text

movu m0, [srcq]
movu m1, [shuffle_mask]
pshufb m0, m1   ; Permutiere m0 basierend auf m1
```

---

## Referenzen

- Intel Instruction Manual: https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html
- Unofficial Web-Referenz: https://www.felixcloutier.com/x86/
- SIMD-Visualisierung: https://www.officedaytime.com/simd512e/
- Art of 64-bit Assembly (SIMD-Diagramme): https://artofasm.randallhyde.com/
- FFmpeg FATE Testsuite: https://fate.ffmpeg.org/
- dav1d Projekt: https://www.videolan.org/projects/dav1d.html
- Negamax Wikipedia: https://en.wikipedia.org/wiki/Sign_extension
- Discord: https://discord.com/invite/Ks5MhUhqfB
