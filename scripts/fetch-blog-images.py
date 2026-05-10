#!/usr/bin/env python3
"""
CanGo Empire – Automatischer Blog-Bilder-Fetcher
Holt professionelle Fotos von Pexels API und baut Magazin-Bento-Layout ein.

Setup:
  1. Kostenlosen API-Key holen: https://www.pexels.com/api/
  2. In .env eintragen:  PEXELS_API_KEY=dein_key
  3. Ausführen:          python3 scripts/fetch-blog-images.py
"""

import os
import re
import sys
import json
import time
import shutil
import hashlib
import urllib.request
import urllib.parse
from pathlib import Path
from html.parser import HTMLParser

# ── Pfade ──────────────────────────────────────────────────────────────────────
ROOT = Path(__file__).parent.parent
BLOGS_DIR = ROOT / "website" / "blogs"
IMAGES_DIR = ROOT / "website" / "images" / "blog-real"
IMAGES_DIR.mkdir(parents=True, exist_ok=True)

# ── API-Key laden ───────────────────────────────────────────────────────────────
def load_api_key():
    # 1. Umgebungsvariable
    key = os.environ.get("PEXELS_API_KEY", "")
    if key:
        return key
    # 2. .env Datei
    env_file = ROOT / ".env"
    if env_file.exists():
        for line in env_file.read_text().splitlines():
            line = line.strip()
            if line.startswith("PEXELS_API_KEY="):
                key = line.split("=", 1)[1].strip().strip('"').strip("'")
                if key:
                    return key
    return ""

# ── Keywords pro Blog-Slug ──────────────────────────────────────────────────────
BLOG_KEYWORDS = {
    # ── Vorhandene Blogs ───────────────────────────────────────────────────────
    "maschinen-die-dienen": {
        "hero": "automation technology future",
        "bento": [
            "artificial intelligence robot",
            "workflow productivity software",
            "digital transformation business",
        ],
        "title": "Maschinen, die dienen – nicht beherrschen",
    },
    # ── Weitere Blogs (falls vorhanden) ───────────────────────────────────────
    "automationen": {
        "hero": "automation workflow business",
        "bento": ["n8n workflow automation", "digital tools productivity", "business automation robot"],
        "title": "Automatisierungen",
    },
    "coaching-mindset": {
        "hero": "life coaching mindset success",
        "bento": ["personal development growth", "mindset motivation coach", "success achievement goal"],
        "title": "Coaching & Mindset",
    },
    "crypto-web3": {
        "hero": "cryptocurrency bitcoin blockchain",
        "bento": ["web3 decentralized finance", "crypto trading chart", "blockchain technology future"],
        "title": "Crypto & Web3",
    },
    "energie-solar": {
        "hero": "solar energy panels renewable",
        "bento": ["solar panels rooftop", "clean energy sustainability", "photovoltaic installation"],
        "title": "Energie & Solar",
    },
    "finanzen-versicherung": {
        "hero": "finance investment money",
        "bento": ["insurance protection family", "financial planning savings", "stock market investment"],
        "title": "Finanzen & Versicherung",
    },
    "immobilien": {
        "hero": "real estate property house",
        "bento": ["modern apartment interior", "real estate investment building", "luxury home architecture"],
        "title": "Immobilien",
    },
    "karriere-hr": {
        "hero": "career business professional",
        "bento": ["job interview hiring", "team collaboration office", "professional development career"],
        "title": "Karriere & HR",
    },
    "ki-tech": {
        "hero": "artificial intelligence technology",
        "bento": ["machine learning data", "tech startup innovation", "ai future digital"],
        "title": "KI & Tech",
    },
    "trading": {
        "hero": "stock trading finance chart",
        "bento": ["forex trading screen", "investment portfolio growth", "financial market analysis"],
        "title": "Trading",
    },
    "artikel-bitcoin-institutionen-2026": {
        "hero": "bitcoin institutional investment",
        "bento": ["cryptocurrency gold bitcoin", "financial institution bank", "bitcoin chart bull"],
        "title": "Bitcoin Institutionen 2026",
    },
    "artikel-claude-vs-chatgpt-unternehmen-2026": {
        "hero": "artificial intelligence chatbot comparison",
        "bento": ["ai assistant technology", "business software comparison", "digital transformation ai"],
        "title": "Claude vs ChatGPT 2026",
    },
    "artikel-eigentumswohnung-kaufen-2026": {
        "hero": "apartment buying real estate",
        "bento": ["condominium interior modern", "real estate contract signing", "city apartment building"],
        "title": "Eigentumswohnung kaufen 2026",
    },
    "artikel-pkv-vs-gkv-2026": {
        "hero": "health insurance medical",
        "bento": ["doctor hospital healthcare", "insurance document contract", "medical technology health"],
        "title": "PKV vs GKV 2026",
    },
    "artikel-produktivitaet-adhs-systeme": {
        "hero": "productivity focus concentration",
        "bento": ["adhd focus study", "productivity system organization", "calm concentration work"],
        "title": "Produktivität & ADHS",
    },
    "artikel-solaranlage-ratgeber-2026": {
        "hero": "solar panel installation rooftop",
        "bento": ["solar energy house", "photovoltaic technology clean", "renewable energy solar"],
        "title": "Solaranlage Ratgeber 2026",
    },
    "maschinen-die-dienen-davinci-pfad": {
        "hero": "da vinci innovation technology art",
        "bento": ["renaissance technology fusion", "creative innovation future", "automation creativity blend"],
        "title": "DaVinci-Pfad",
    },
}

# ── Pexels API Abfrage ──────────────────────────────────────────────────────────
def pexels_search(query: str, api_key: str, per_page: int = 3) -> list[dict]:
    """Gibt Liste von {'url': ..., 'photographer': ...} zurück."""
    encoded = urllib.parse.quote(query)
    url = f"https://api.pexels.com/v1/search?query={encoded}&per_page={per_page}&orientation=landscape"
    req = urllib.request.Request(url, headers={"Authorization": api_key})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read())
        photos = data.get("photos", [])
        return [
            {
                "url": p["src"]["large2x"],       # 1880px breit
                "url_medium": p["src"]["large"],   # 940px
                "photographer": p["photographer"],
                "id": p["id"],
            }
            for p in photos
        ]
    except Exception as e:
        print(f"  ⚠ Pexels Fehler für '{query}': {e}")
        return []

# ── Bild herunterladen ──────────────────────────────────────────────────────────
def download_image(url: str, dest: Path) -> bool:
    if dest.exists():
        print(f"  ✓ Bereits vorhanden: {dest.name}")
        return True
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "CanGoEmpire/1.0"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            dest.write_bytes(resp.read())
        print(f"  ↓ Geladen: {dest.name}")
        return True
    except Exception as e:
        print(f"  ✗ Download-Fehler: {e}")
        return False

# ── HTML-Bento-Block generieren ─────────────────────────────────────────────────
def make_bento_html(slug: str, images: list[dict], title: str) -> str:
    """Erzeugt einen Magazin-Bento-Block mit 3 Bildern."""
    if not images:
        return ""

    def img_path(idx):
        return f"../images/blog-real/{slug}-s{idx+1}.jpg"

    def credit(idx):
        if idx < len(images):
            return images[idx].get("photographer", "Pexels")
        return "Pexels"

    items = []
    for i in range(min(3, len(images))):
        items.append(f"""    <figure class="bento-item">
      <img src="{img_path(i)}" alt="{title} – Visual {i+1}" loading="lazy" width="800" height="500">
      <figcaption>© {credit(i)} via Pexels</figcaption>
    </figure>""")

    return f"""
<!-- BENTO MAGAZIN BILDER -->
<section class="bento-grid" aria-label="Visuals">
{chr(10).join(items)}
</section>
<!-- /BENTO -->
"""

BENTO_CSS = """
  /* ── Bento Magazin ─────────────────────────────── */
  .bento-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 0.75rem;
    margin: 2.5rem 0;
  }
  .bento-item {
    position: relative;
    border-radius: 8px;
    overflow: hidden;
    aspect-ratio: 16/10;
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
  .bento-item:hover img { transform: scale(1.03); }
  .bento-item figcaption {
    position: absolute;
    bottom: 0;
    right: 0;
    background: rgba(10,15,30,0.72);
    color: rgba(148,163,184,0.85);
    font-size: 0.62rem;
    padding: 0.25rem 0.5rem;
    border-radius: 8px 0 0 0;
    letter-spacing: 0.04em;
  }
  @media (max-width: 480px) {
    .bento-grid { grid-template-columns: 1fr; }
    .bento-item:first-child { aspect-ratio: 16/9; }
  }
  /* ── /Bento ─────────────────────────────────────── */
"""

# ── HTML patchen ────────────────────────────────────────────────────────────────
def patch_html(html_path: Path, slug: str, hero_img: dict | None,
               bento_images: list[dict], keywords: dict) -> bool:
    """
    Patcht eine Blog-HTML-Datei:
    - Hero-Bild src austauschen
    - Bento-Block nach dem Hero-Img einfügen (oder nach .byline)
    - og:image + twitter:image aktualisieren
    - Bento-CSS in <style> einfügen (falls nicht vorhanden)
    """
    content = html_path.read_text(encoding="utf-8")
    changed = False
    title = keywords.get("title", slug)

    # 1. Hero-Bild src
    if hero_img:
        hero_src = f"../images/blog-real/{slug}-hero.jpg"
        new_img_tag = (
            f'<img\n    src="{hero_src}"\n'
            f'    alt="{title} – Hero Bild"\n'
            f'    class="hero-img"\n'
            f'    width="1200"\n'
            f'    height="630"\n'
            f'    loading="eager"\n'
            f'    onerror="this.style.display=\'none\'"\n  >'
        )
        # Ersetze bestehenden hero-img Block
        pattern = r'<img[^>]+class="hero-img"[^>]*>'
        if re.search(pattern, content, re.DOTALL):
            content = re.sub(pattern, new_img_tag, content, flags=re.DOTALL)
            changed = True
        else:
            # Einfügen nach breadcrumb nav
            content = content.replace(
                '<!-- Hero Image -->',
                f'<!-- Hero Image -->\n  {new_img_tag}'
            )
            changed = True

        # og:image + twitter:image
        abs_hero = f"https://automation-cango-app-empire.com/images/blog-real/{slug}-hero.jpg"
        content = re.sub(
            r'<meta property="og:image" content="[^"]*"',
            f'<meta property="og:image" content="{abs_hero}"',
            content
        )
        content = re.sub(
            r'<meta name="twitter:image" content="[^"]*"',
            f'<meta name="twitter:image" content="{abs_hero}"',
            content
        )

    # 2. Bento-CSS in <style> einfügen
    if "bento-grid" not in content:
        content = content.replace("</style>", BENTO_CSS + "\n</style>", 1)
        changed = True

    # 3. Bento-Block einfügen (nach hero-img oder nach .byline div)
    bento_html = make_bento_html(slug, bento_images, title)
    if bento_html and "bento-grid" not in content:
        # Nach dem ersten h2 oder nach byline einfügen
        insert_after = re.search(r'<div class="byline">[^<]*</div>', content)
        if insert_after:
            pos = insert_after.end()
            content = content[:pos] + "\n" + bento_html + content[pos:]
            changed = True
        else:
            # Fallback: nach hero-img
            hero_end = re.search(r'class="hero-img"[^>]*>', content)
            if hero_end:
                pos = hero_end.end()
                content = content[:pos] + "\n" + bento_html + content[pos:]
                changed = True

    if changed:
        html_path.write_text(content, encoding="utf-8")
    return changed

# ── Haupt-Routine ───────────────────────────────────────────────────────────────
def main():
    api_key = load_api_key()
    if not api_key:
        print("\n❌ Kein Pexels API-Key gefunden!")
        print("\n📋 So bekommst du einen kostenlosen Key in 2 Minuten:")
        print("   1. https://www.pexels.com/api/ → 'Get Started'")
        print("   2. Kostenlosen Account anlegen (kein CC nötig)")
        print("   3. Key kopieren und in .env eintragen:")
        print("      echo 'PEXELS_API_KEY=dein_key_hier' >> .env")
        print("   4. Nochmal ausführen: python3 scripts/fetch-blog-images.py\n")
        sys.exit(1)

    print(f"\n🚀 CanGo Empire Blog-Bilder-Fetcher")
    print(f"   Bilder → {IMAGES_DIR}")
    print(f"   Blogs  → {BLOGS_DIR}\n")

    html_files = list(BLOGS_DIR.glob("*.html"))
    if not html_files:
        print("⚠ Keine HTML-Dateien in website/blogs/ gefunden.")
        sys.exit(0)

    total_changed = 0

    for html_file in sorted(html_files):
        slug = html_file.stem
        keywords = BLOG_KEYWORDS.get(slug, {
            "hero": slug.replace("-", " "),
            "bento": [slug.replace("-", " "), "business digital", "technology modern"],
            "title": slug.replace("-", " ").title(),
        })

        print(f"📄 {slug}")
        hero_img = None
        bento_images = []

        # Hero
        hero_dest = IMAGES_DIR / f"{slug}-hero.jpg"
        hero_results = pexels_search(keywords["hero"], api_key, per_page=1)
        if hero_results:
            hero_img = hero_results[0]
            download_image(hero_img["url"], hero_dest)
        time.sleep(0.3)  # Rate limit

        # Bento (3 Bilder)
        for i, query in enumerate(keywords.get("bento", [])[:3], 1):
            dest = IMAGES_DIR / f"{slug}-s{i}.jpg"
            results = pexels_search(query, api_key, per_page=1)
            if results:
                bento_images.append(results[0])
                download_image(results[0]["url_medium"], dest)
            time.sleep(0.3)

        # HTML patchen
        changed = patch_html(html_file, slug, hero_img, bento_images, keywords)
        if changed:
            print(f"  ✏ HTML aktualisiert: {html_file.name}")
            total_changed += 1
        else:
            print(f"  = Keine Änderungen nötig: {html_file.name}")

        print()

    print(f"✅ Fertig! {total_changed}/{len(html_files)} Blog(s) aktualisiert.")
    print(f"\n🚀 Jetzt deployen:")
    print(f"   cd '{ROOT}' && ./deploy-to-server.sh\n")

if __name__ == "__main__":
    main()
