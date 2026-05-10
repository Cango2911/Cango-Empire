#!/usr/bin/env python3
"""
CanGo Empire – Kostenlose Bilder ohne API-Key
Nutzt picsum.photos (Unsplash-Fotografen, kostenlos, kein Login nötig).
Jeder Blog bekommt konsistente, schöne Landscape-Fotos.
"""
import os, re, time, urllib.request
from pathlib import Path

ROOT = Path(__file__).parent.parent
BLOGS_DIR = ROOT / "website" / "blogs"
IMG_DIR   = ROOT / "website" / "images" / "blog-real"
IMG_DIR.mkdir(parents=True, exist_ok=True)

# Picsum seed-IDs: schöne, thematisch passende Fotos (picsum.photos/id/XXX)
# Vorab kuratiert – jedes Bild ist öffentlich lizenziert
BLOG_IMAGES = {
    "maschinen-die-dienen": {
        "hero": 1036,    # Technologie / futuristisch
        "s1":   442,     # Roboter / Automatisierung
        "s2":   325,     # Code / Digital
        "s3":   573,     # Natur / Freiheit
    },
    "automationen": {
        "hero": 1036,
        "s1":   442,
        "s2":   325,
        "s3":   96,
    },
    "coaching-mindset": {
        "hero": 1090,   # Motivation / Mensch
        "s1":   399,    # Meditation
        "s2":   260,    # Notizbuch / Planung
        "s3":   1024,   # Sonnenaufgang
    },
    "crypto-web3": {
        "hero": 730,    # Technologie / Lichter
        "s1":   180,    # Server / Daten
        "s2":   325,    # Code
        "s3":   442,    # Digital
    },
    "energie-solar": {
        "hero": 459,    # Natur / Energie
        "s1":   974,    # Solar
        "s2":   129,    # Architektur modern
        "s3":   1,      # Natur pur
    },
    "finanzen-versicherung": {
        "hero": 210,    # Business / Büro
        "s1":   260,    # Schreibtisch
        "s2":   172,    # Diagramm
        "s3":   534,    # Stadt / Finance
    },
    "immobilien": {
        "hero": 164,    # Haus / Architektur
        "s1":   129,    # Modernes Gebäude
        "s2":   547,    # Interior
        "s3":   1080,   # Stadtansicht
    },
    "karriere-hr": {
        "hero": 375,    # Team / Büro
        "s1":   210,    # Meeting
        "s2":   260,    # Laptop / Arbeit
        "s3":   399,    # Handshake
    },
    "ki-tech": {
        "hero": 442,    # KI / Technologie
        "s1":   325,    # Code
        "s2":   180,    # Server
        "s3":   730,    # Digital Future
    },
    "trading": {
        "hero": 534,    # Finance / Stadt
        "s1":   172,    # Chart
        "s2":   210,    # Büro modern
        "s3":   96,     # Abstrakt
    },
    "artikel-bitcoin-institutionen-2026": {
        "hero": 730,
        "s1":   325,
        "s2":   180,
        "s3":   534,
    },
    "artikel-claude-vs-chatgpt-unternehmen-2026": {
        "hero": 442,
        "s1":   325,
        "s2":   96,
        "s3":   573,
    },
    "artikel-eigentumswohnung-kaufen-2026": {
        "hero": 164,
        "s1":   547,
        "s2":   129,
        "s3":   1080,
    },
    "artikel-pkv-vs-gkv-2026": {
        "hero": 375,
        "s1":   260,
        "s2":   399,
        "s3":   1090,
    },
    "artikel-produktivitaet-adhs-systeme": {
        "hero": 1090,
        "s1":   260,
        "s2":   399,
        "s3":   573,
    },
    "artikel-solaranlage-ratgeber-2026": {
        "hero": 459,
        "s1":   974,
        "s2":   129,
        "s3":   1,
    },
    "maschinen-die-dienen-davinci-pfad": {
        "hero": 1036,
        "s1":   442,
        "s2":   573,
        "s3":   325,
    },
}

BENTO_CSS = """
  /* ── Bento Magazin ─────────────────────────────── */
  .bento-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 0.6rem;
    margin: 2rem 0 3rem;
  }
  .bento-item {
    position: relative;
    border-radius: 8px;
    overflow: hidden;
    aspect-ratio: 4/3;
    background: var(--navy-light);
  }
  .bento-item:first-child {
    grid-column: 1 / -1;
    aspect-ratio: 16/7;
  }
  .bento-item img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
    transition: transform 0.4s ease;
  }
  .bento-item:hover img { transform: scale(1.04); }
  .bento-item figcaption {
    position: absolute;
    bottom: 0; right: 0;
    background: rgba(10,15,30,0.65);
    color: rgba(148,163,184,0.8);
    font-size: 0.6rem;
    padding: 0.2rem 0.45rem;
    border-radius: 8px 0 0 0;
    letter-spacing: 0.03em;
  }
  @media (max-width: 600px) {
    .bento-grid { grid-template-columns: 1fr; }
    .bento-item:first-child { aspect-ratio: 16/9; }
  }
  /* ── /Bento ─────────────────────────────────────── */
"""

def dl(url: str, dest: Path, label: str) -> bool:
    if dest.exists() and dest.stat().st_size > 10000:
        print(f"  ✓ {label}")
        return True
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "CanGoEmpire/1.0"})
        with urllib.request.urlopen(req, timeout=20) as r:
            dest.write_bytes(r.read())
        print(f"  ↓ {label}")
        return True
    except Exception as e:
        print(f"  ✗ {label}: {e}")
        return False

def picsum_url(photo_id: int, w: int, h: int) -> str:
    return f"https://picsum.photos/id/{photo_id}/{w}/{h}"

def patch_html(path: Path, slug: str, ids: dict) -> bool:
    html = path.read_text(encoding="utf-8")
    original = html
    rel = "../images/blog-real"

    # 1. Hero-Bild src ersetzen
    hero_src = f"{rel}/{slug}-hero.jpg"
    hero_tag = (
        f'<img\n    src="{hero_src}"\n'
        f'    alt="{slug.replace("-"," ").title()} Hero"\n'
        f'    class="hero-img"\n'
        f'    width="1200" height="630"\n'
        f'    loading="eager"\n'
        f'    onerror="this.style.opacity=\'0\'"\n  >'
    )
    html = re.sub(r'<img[^>]+class="hero-img"[^>]*>', hero_tag, html, flags=re.DOTALL)

    # 2. og:image + twitter:image
    abs_hero = f"https://automation-cango-app-empire.com/images/blog-real/{slug}-hero.jpg"
    html = re.sub(r'<meta property="og:image" content="[^"]*"',
                  f'<meta property="og:image" content="{abs_hero}"', html)
    html = re.sub(r'<meta name="twitter:image" content="[^"]*"',
                  f'<meta name="twitter:image" content="{abs_hero}"', html)
    html = re.sub(r'"image":\s*"[^"]*blog[^"]*"',
                  f'"image": "{abs_hero}"', html)

    # 3. Bento-CSS einmalig einfügen
    if "bento-grid" not in html:
        html = html.replace("</style>", BENTO_CSS + "\n</style>", 1)

    # 4. Bento-Block einfügen (nach byline oder nach hero-img)
    if "bento-grid" not in html:
        bento_html = f"""
<!-- BENTO MAGAZIN -->
<section class="bento-grid" aria-label="Bildergalerie">
  <figure class="bento-item">
    <img src="{rel}/{slug}-hero.jpg" alt="{slug} Visual 1" loading="lazy" width="1200" height="525">
    <figcaption>© Unsplash via Picsum</figcaption>
  </figure>
  <figure class="bento-item">
    <img src="{rel}/{slug}-s1.jpg" alt="{slug} Visual 2" loading="lazy" width="800" height="600">
    <figcaption>© Unsplash via Picsum</figcaption>
  </figure>
  <figure class="bento-item">
    <img src="{rel}/{slug}-s2.jpg" alt="{slug} Visual 3" loading="lazy" width="800" height="600">
    <figcaption>© Unsplash via Picsum</figcaption>
  </figure>
  <figure class="bento-item">
    <img src="{rel}/{slug}-s3.jpg" alt="{slug} Visual 4" loading="lazy" width="800" height="600">
    <figcaption>© Unsplash via Picsum</figcaption>
  </figure>
</section>
<!-- /BENTO -->
"""
        # Nach byline einfügen
        m = re.search(r'</div>\s*\n(\s*<p class="opening")', html)
        if m:
            html = html[:m.start()+6] + "\n" + bento_html + html[m.start()+6:]
        else:
            # Fallback: nach hero-img
            m2 = re.search(r'class="hero-img"[^>]*>', html)
            if m2:
                html = html[:m2.end()] + "\n" + bento_html + html[m2.end():]

    if html != original:
        path.write_text(html, encoding="utf-8")
        return True
    return False

def main():
    print("\n🚀 CanGo Empire – Kostenlose Fotos (kein API-Key nötig)\n")
    html_files = list(BLOGS_DIR.glob("*.html"))
    if not html_files:
        print("⚠ Keine Blog-HTML-Dateien gefunden.")
        return

    changed = 0
    for html_file in sorted(html_files):
        slug = html_file.stem
        ids = BLOG_IMAGES.get(slug, {
            "hero": 1036, "s1": 442, "s2": 325, "s3": 573
        })
        print(f"📄 {slug}")

        dl(picsum_url(ids["hero"], 1200, 630),  IMG_DIR / f"{slug}-hero.jpg", "hero 1200x630")
        dl(picsum_url(ids["s1"],   800, 600),   IMG_DIR / f"{slug}-s1.jpg",  "s1 800x600")
        dl(picsum_url(ids["s2"],   800, 600),   IMG_DIR / f"{slug}-s2.jpg",  "s2 800x600")
        dl(picsum_url(ids["s3"],   800, 600),   IMG_DIR / f"{slug}-s3.jpg",  "s3 800x600")
        time.sleep(0.2)

        if patch_html(html_file, slug, ids):
            print(f"  ✏ HTML aktualisiert")
            changed += 1
        print()

    print(f"✅ {changed}/{len(html_files)} Blogs aktualisiert.")
    print(f"\n▶ Jetzt deployen:")
    print(f'   cd "{ROOT}" && ./deploy-to-server.sh\n')

if __name__ == "__main__":
    main()
