#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CanGo Empire – Blog Generator v1.0
===================================
Läuft auf dem VPS, wird von n8n via "Execute Command" aufgerufen.

Ablauf:
  1. JSON-Payload aus stdin oder --b64-Argument lesen
  2. Depositphotos Enterprise API: Login → Suche (4 Bilder) → Download
  3. Slug generieren + Lesedauer berechnen
  4. Markdown → HTML konvertieren (H2-Abschnitte mit Bildern)
  5. Vollständige Blog-HTML-Datei schreiben
  6. blogs.html aktualisieren (neue Karte ganz oben)
  7. In Nginx-Verzeichnis deployen
  8. Ergebnis als JSON auf stdout ausgeben

Aufruf durch n8n:
  python3 /opt/cango/blog_generator.py --b64 <base64_encoded_json>

Env-Variablen (in /opt/cango/.env oder Systemumgebung):
  DP_API_KEY, DP_USER, DP_PASS
  CANGO_WWW_ROOT   (default: /docker/nginx-proxy-manager-5tiw/www)
  CANGO_SCRIPT_DIR (default: /opt/cango)
"""

import sys
import os
import re
import json
import base64
import argparse
import urllib.request
import urllib.parse
import urllib.error
import shutil
import time
from datetime import datetime
from pathlib import Path

# ── Konfiguration ────────────────────────────────────────────────────────────

BASE_URL = "https://automation-cango-app-empire.com"
AUTHOR   = "Canberk Umut Kıvılcım"

WWW_ROOT    = Path(os.environ.get("CANGO_WWW_ROOT", "/docker/nginx-proxy-manager-5tiw/www"))
BLOGS_DIR   = WWW_ROOT / "blogs"
IMAGES_DIR  = WWW_ROOT / "images" / "blog-sections"
BLOGS_INDEX = WWW_ROOT / "blogs.html"

DP_API      = "https://api.depositphotos.com"
DP_API_KEY  = os.environ.get("DP_API_KEY", "")
DP_USER     = os.environ.get("DP_USER", "")
DP_PASS     = os.environ.get("DP_PASS", "")

# Nischen → Verwandte Artikel
RELATED = {
    "ki-tech":             ["automationen.html",         "coaching-mindset.html",   "karriere-hr.html"],
    "automationen":        ["ki-tech.html",              "karriere-hr.html",        "coaching-mindset.html"],
    "karriere-hr":         ["coaching-mindset.html",     "ki-tech.html",            "finanzen-versicherung.html"],
    "coaching-mindset":    ["karriere-hr.html",          "ki-tech.html",            "automationen.html"],
    "immobilien":          ["finanzen-versicherung.html","energie-solar.html",      "karriere-hr.html"],
    "energie-solar":       ["immobilien.html",           "finanzen-versicherung.html", "ki-tech.html"],
    "finanzen-versicherung":["immobilien.html",          "crypto-web3.html",        "karriere-hr.html"],
    "crypto-web3":         ["finanzen-versicherung.html","ki-tech.html",            "trading.html"],
    "trading":             ["crypto-web3.html",          "finanzen-versicherung.html", "ki-tech.html"],
}

RELATED_LABELS = {
    "automationen.html":          "Automatisierungen",
    "ki-tech.html":               "KI & Tech",
    "karriere-hr.html":           "Karriere & HR",
    "coaching-mindset.html":      "Coaching & Mindset",
    "immobilien.html":            "Immobilien",
    "energie-solar.html":         "Energie & Solar",
    "finanzen-versicherung.html": "Finanzen & Versicherung",
    "crypto-web3.html":           "Crypto & Web3",
    "trading.html":               "Trading",
}

# ── Depositphotos API ─────────────────────────────────────────────────────────

def dp_request(params: dict, retries: int = 3) -> dict:
    """HTTP-POST gegen Depositphotos API, gibt geparste JSON-Antwort zurück."""
    params["dp_apikey"] = DP_API_KEY
    data = urllib.parse.urlencode(params).encode()
    for attempt in range(retries):
        try:
            req = urllib.request.Request(DP_API, data=data,
                                         headers={"Content-Type": "application/x-www-form-urlencoded"})
            with urllib.request.urlopen(req, timeout=20) as r:
                result = json.loads(r.read())
            if result.get("type") == "success":
                return result
            err = result.get("error", {}).get("errormsg", "unknown")
            log(f"DP API Fehler: {err} (Versuch {attempt+1})")
        except Exception as e:
            log(f"DP API Netzwerkfehler: {e} (Versuch {attempt+1})")
        if attempt < retries - 1:
            time.sleep(2 ** attempt)
    return {}

def dp_login() -> str:
    """Gibt session_id zurück oder leeren String bei Fehler."""
    result = dp_request({
        "dp_command":        "loginEnterprise",
        "dp_login_user":     DP_USER,
        "dp_login_password": DP_PASS,
    })
    return result.get("sessionid", "")

def dp_logout(session_id: str):
    dp_request({"dp_command": "logout", "dp_session_id": session_id})

def dp_search(session_id: str, query: str, limit: int = 4) -> list:
    """Gibt Liste von Item-Dicts zurück: {id, url2, title}"""
    result = dp_request({
        "dp_command":       "search",
        "dp_session_id":    session_id,
        "dp_search_query":  query,
        "dp_search_limit":  limit,
        "dp_search_sort":   1,         # best_match
        "dp_search_nudity": 0,
        "dp_search_photo":  1,
        "dp_search_vector": 0,
        "dp_watermark":     "neutral",
    })
    items = result.get("result", [])
    return [{"id": i.get("id"), "preview": i.get("url2", i.get("thumbnail", ""))} for i in items if i.get("id")]

def dp_download(session_id: str, item_id: int) -> str:
    """Gibt Download-URL zurück (complimentaryDownload, xl-Größe)."""
    result = dp_request({
        "dp_command":    "complimentaryDownload",
        "dp_session_id": session_id,
        "dp_item_id":    item_id,
        "dp_option":     "xl-2015",
    })
    return result.get("downloadLink", "")

def download_image(url: str, dest: Path) -> bool:
    """Lädt Bild von URL herunter und speichert es."""
    if not url:
        return False
    dest.parent.mkdir(parents=True, exist_ok=True)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "CanGoEmpire/1.0"})
        with urllib.request.urlopen(req, timeout=30) as r:
            dest.write_bytes(r.read())
        return True
    except Exception as e:
        log(f"Bild-Download fehlgeschlagen ({url[:60]}): {e}")
        return False

def fetch_depositphotos_images(keyword: str, section_keywords: list) -> dict:
    """
    Sucht und lädt 4 Bilder: hero + 3 Sections.
    Gibt {hero, s1, s2, s3} → Download-URLs zurück.
    """
    if not all([DP_API_KEY, DP_USER, DP_PASS]):
        log("⚠ Depositphotos-Credentials fehlen – überspringe Bilddownload")
        return {}

    session_id = dp_login()
    if not session_id:
        log("⚠ DP Login fehlgeschlagen")
        return {}

    urls = {}
    searches = [keyword] + section_keywords[:3]
    keys    = ["hero", "s1", "s2", "s3"]

    for key, query in zip(keys, searches):
        time.sleep(0.5)  # Rate-Limit einhalten
        items = dp_search(session_id, query, limit=2)
        if not items:
            log(f"  ⚠ Keine DP-Bilder für '{query}'")
            continue
        item_id = items[0]["id"]
        time.sleep(0.5)
        dl_url = dp_download(session_id, item_id)
        if dl_url:
            urls[key] = dl_url
            log(f"  ✓ DP Bild [{key}]: item_id={item_id}")
        else:
            # Fallback: Vorschau-URL (mit Wasserzeichen, besser als gar nichts)
            urls[key] = items[0]["preview"]
            log(f"  ~ DP Fallback-Preview [{key}]")

    dp_logout(session_id)
    return urls

# ── Slug & Hilfsfunktionen ────────────────────────────────────────────────────

def slugify(text: str) -> str:
    """Wandelt Text in URL-Slug um."""
    text = text.lower()
    # Deutsche Umlaute
    for a, b in [("ä","ae"),("ö","oe"),("ü","ue"),("ß","ss"),("é","e"),("è","e"),("à","a")]:
        text = text.replace(a, b)
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text).strip("-")
    return text[:70]

def reading_time(text: str) -> int:
    """Schätzt Lesezeit in Minuten (200 Wörter/Min)."""
    words = len(re.findall(r"\w+", text))
    return max(1, round(words / 200))

def extract_pullquote(content: str) -> str:
    """Findet einen geeigneten Satz für das Pullquote."""
    paragraphs = [p.strip() for p in content.split("\n") if len(p.strip()) > 80
                  and not p.strip().startswith("#") and not p.strip().startswith("-")]
    return paragraphs[1] if len(paragraphs) > 1 else (paragraphs[0] if paragraphs else "")

def html_escape(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

# ── Markdown → HTML Konverter ─────────────────────────────────────────────────

def md_inline(text: str) -> str:
    """Inline-Formatierung: **bold**, *italic*, `code`"""
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*(.+?)\*",     r"<em>\1</em>",         text)
    text = re.sub(r"`(.+?)`",       r"<code>\1</code>",     text)
    return text

def markdown_to_html(md: str, images: dict, slug: str) -> str:
    """
    Konvertiert Markdown zu HTML und injiziert Section-Bilder nach den ersten 3 H2s.
    """
    blocks  = re.split(r"\n{2,}", md.strip())
    parts   = []
    h2_count = 0
    section_keys = ["s1", "s2", "s3"]

    for block in blocks:
        block = block.strip()
        if not block:
            continue

        # H2
        if block.startswith("## "):
            heading = html_escape(block[3:].strip())
            parts.append(f'<h2>{heading}</h2>')
            # Section-Bild nach H2 (max 3)
            if h2_count < 3:
                key = section_keys[h2_count]
                img_path = f"../images/blog-sections/{slug}-{key}.jpg"
                figcap   = "© Depositphotos Enterprise"
                parts.append(
                    f'<figure class="section-visual">\n'
                    f'  <img src="{img_path}" alt="{heading}" loading="lazy" width="900" height="506"'
                    f' onerror="this.parentElement.style.display=\'none\'">\n'
                    f'  <figcaption>{figcap}</figcaption>\n'
                    f'</figure>'
                )
                h2_count += 1

        # H3
        elif block.startswith("### "):
            heading = html_escape(block[4:].strip())
            parts.append(f'<h3>{heading}</h3>')

        # Aufzählungsliste
        elif re.match(r"^[-*]\s", block):
            items = []
            for line in block.splitlines():
                m = re.match(r"^[-*]\s+(.+)", line.strip())
                if m:
                    items.append(f'  <li>{md_inline(m.group(1))}</li>')
            if items:
                parts.append("<ul>\n" + "\n".join(items) + "\n</ul>")

        # Nummerierte Liste
        elif re.match(r"^\d+\.\s", block):
            items = []
            for line in block.splitlines():
                m = re.match(r"^\d+\.\s+(.+)", line.strip())
                if m:
                    items.append(f'  <li>{md_inline(m.group(1))}</li>')
            if items:
                parts.append("<ol>\n" + "\n".join(items) + "\n</ol>")

        # Blockquote
        elif block.startswith("> "):
            text = md_inline(block[2:].strip())
            parts.append(f'<blockquote class="pullquote">{text}</blockquote>')

        # Normaler Absatz (mehrzeilig zusammenfassen)
        else:
            lines = [md_inline(l.strip()) for l in block.splitlines() if l.strip()]
            parts.append(f'<p>{" ".join(lines)}</p>')

    return "\n\n".join(parts)

# ── HTML Template ─────────────────────────────────────────────────────────────

def build_blog_html(payload: dict, image_urls: dict, body_html: str) -> str:
    slug        = payload["slug"]
    title       = payload["title"]
    niche       = payload["niche"]
    niche_slug  = payload.get("niche_slug", "ki-tech")
    date        = payload["date"]
    excerpt     = payload.get("excerpt", "")
    meta_desc   = payload.get("meta_description", excerpt[:155])
    tags        = payload.get("tags", [])
    read_time   = payload.get("read_time", 6)

    hero_path   = f"../images/blog-sections/{slug}-hero.jpg"
    abs_hero    = f"{BASE_URL}/images/blog-sections/{slug}-hero.jpg"
    canon_url   = f"{BASE_URL}/blogs/{slug}.html"

    schema = {
        "@context":       "https://schema.org",
        "@type":          "BlogPosting",
        "headline":       title,
        "image":          abs_hero,
        "url":            canon_url,
        "author":         {"@type": "Person", "name": AUTHOR},
        "publisher":      {"@type": "Organization", "name": "CanGo Empire"},
        "datePublished":  date,
        "inLanguage":     "de",
        "articleSection": niche,
    }

    related_pages = RELATED.get(niche_slug, list(RELATED.values())[0])
    related_html  = "\n".join(
        f'    <a href="{p}">{RELATED_LABELS.get(p, p)}</a>'
        for p in related_pages
    )

    tags_html = "\n".join(f'    <span class="tag">{html_escape(t)}</span>' for t in tags)

    pullquote = extract_pullquote(payload.get("content_markdown", ""))
    pullquote_html = (
        f'\n  <blockquote class="pullquote">{html_escape(pullquote[:200])}</blockquote>\n'
        if pullquote else ""
    )

    return f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{html_escape(title)} | CanGo Empire Blog</title>
<meta name="description" content="{html_escape(meta_desc[:155])}">
<meta name="robots" content="index,follow,max-image-preview:large">
<link rel="canonical" href="{canon_url}">
<meta property="og:type" content="article">
<meta property="og:title" content="{html_escape(title)}">
<meta property="og:image" content="{abs_hero}">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:url" content="{canon_url}">
<meta property="article:published_time" content="{date}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{abs_hero}">
<script type="application/ld+json">
{json.dumps(schema, ensure_ascii=False)}
</script>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400;1,600&family=Syne:wght@400;700;800&family=Inter:wght@300;400;500&display=swap" media="print" onload="this.media='all'">
<style>
:root{{--orange:#F97316;--navy:#0A0F1E;--navy-light:#1E293B;--text:#E2E8F0;--muted:#94A3B8;--gold:#D4A853;}}
*,*::before,*::after{{margin:0;padding:0;box-sizing:border-box;}}
body{{background:var(--navy);color:var(--text);font-family:'Inter',Georgia,sans-serif;font-weight:300;line-height:1.9;padding:2rem 1rem;-webkit-font-smoothing:antialiased;}}
article{{max-width:740px;margin:0 auto;}}
.breadcrumb{{font-size:.75rem;color:var(--muted);margin-bottom:1.5rem;letter-spacing:.05em;}}
.breadcrumb a{{color:var(--muted);text-decoration:none;}}
.breadcrumb a:hover{{color:var(--orange);}}
.breadcrumb span{{margin:0 .4rem;}}
.hero-img{{width:100%;height:auto;aspect-ratio:1200/630;object-fit:cover;border-radius:12px;margin-bottom:2.5rem;display:block;background:var(--navy-light);}}
.meta{{font-size:.72rem;letter-spacing:.18em;text-transform:uppercase;color:var(--orange);font-weight:500;margin-bottom:2rem;}}
h1{{font-family:'Cormorant Garamond',Georgia,serif;font-size:clamp(2rem,5vw,3.4rem);font-weight:600;line-height:1.15;color:#fff;margin-bottom:.5rem;}}
.byline{{font-size:.8rem;color:var(--muted);margin-bottom:2.5rem;padding-bottom:2.5rem;border-bottom:1px solid var(--navy-light);}}
.opening{{font-family:'Cormorant Garamond',Georgia,serif;font-size:clamp(1.1rem,2.5vw,1.35rem);font-style:italic;color:#CBD5E1;line-height:1.7;margin-bottom:2.5rem;}}
p{{font-size:clamp(.9rem,1.5vw,.97rem);margin-bottom:1.3rem;color:var(--text);}}
h2{{font-family:'Syne',sans-serif;font-size:clamp(.9rem,2vw,1.1rem);font-weight:700;color:var(--orange);margin:3rem 0 1.2rem;letter-spacing:.05em;text-transform:uppercase;}}
h3{{font-family:'Syne',sans-serif;font-size:clamp(.85rem,1.8vw,1rem);font-weight:600;color:#CBD5E1;margin:2rem 0 .8rem;}}
ul,ol{{padding-left:1.5rem;margin-bottom:1.3rem;}}
li{{font-size:clamp(.9rem,1.5vw,.97rem);margin-bottom:.4rem;color:var(--text);}}
code{{background:var(--navy-light);padding:.1rem .4rem;border-radius:4px;font-size:.85em;}}
.section-visual{{margin:0 0 2rem;border-radius:12px;overflow:hidden;}}
.section-visual img{{width:100%;height:auto;aspect-ratio:16/9;object-fit:cover;display:block;transition:transform .4s ease;}}
.section-visual:hover img{{transform:scale(1.02);}}
.section-visual figcaption{{font-size:.62rem;color:var(--muted);text-align:right;padding:.3rem .5rem;}}
.pullquote{{border-left:3px solid var(--orange);padding:1.5rem 1.5rem 1.5rem 2rem;margin:3rem 0;background:var(--navy-light);border-radius:0 12px 12px 0;font-family:'Cormorant Garamond',Georgia,serif;font-size:clamp(1.1rem,2.5vw,1.3rem);font-style:italic;color:var(--gold);line-height:1.6;}}
.cta-block{{background:linear-gradient(135deg,var(--navy-light) 0%,#1a2332 100%);border:1px solid var(--orange);border-radius:16px;padding:2.5rem;margin:4rem 0;text-align:center;}}
.cta-block h3{{font-family:'Cormorant Garamond',Georgia,serif;font-size:clamp(1.4rem,3vw,1.8rem);color:#fff;margin-bottom:1rem;}}
.cta-block p{{color:var(--muted);margin-bottom:1.5rem;font-size:.9rem;}}
.cta-btn{{display:inline-block;background:var(--orange);color:#fff;padding:.9rem 2.5rem;border-radius:50px;text-decoration:none;font-family:'Syne',sans-serif;font-weight:700;font-size:.9rem;letter-spacing:.05em;transition:transform .2s,box-shadow .2s;}}
.cta-btn:hover{{transform:translateY(-2px);box-shadow:0 8px 24px rgba(249,115,22,.35);}}
.related-articles{{margin-top:4rem;padding-top:2rem;border-top:1px solid var(--navy-light);}}
.related-articles h4{{font-family:'Syne',sans-serif;font-size:.75rem;text-transform:uppercase;letter-spacing:.2em;color:var(--muted);margin-bottom:1rem;}}
.related-articles a{{display:block;color:var(--text);text-decoration:none;padding:.6rem 0;border-bottom:1px solid var(--navy-light);font-size:.88rem;transition:color .2s;}}
.related-articles a:hover{{color:var(--orange);}}
.tags{{margin-top:3rem;display:flex;flex-wrap:wrap;gap:.5rem;}}
.tag{{background:var(--navy-light);color:var(--muted);padding:.3rem .8rem;border-radius:20px;font-size:.72rem;letter-spacing:.05em;}}
footer.blog-footer{{margin-top:4rem;padding-top:2rem;border-top:1px solid var(--navy-light);font-size:.75rem;color:var(--muted);text-align:center;}}
footer.blog-footer a{{color:var(--muted);text-decoration:none;}}
footer.blog-footer a:hover{{color:var(--orange);}}
@media(max-width:600px){{body{{padding:1rem .75rem;}}h1{{font-size:1.9rem;}}}}
</style>
</head>
<body>
<article>
  <nav class="breadcrumb">
    <a href="../index.html">CanGo Empire</a><span>›</span>
    <a href="../blogs.html">Blog</a><span>›</span>
    <span>{html_escape(niche)}</span>
  </nav>
  <img src="{hero_path}" alt="{html_escape(title)}" class="hero-img" width="1200" height="630" loading="eager" onerror="this.style.opacity='0.3'">
  <div class="meta">{html_escape(niche)} &nbsp;·&nbsp; {date} &nbsp;·&nbsp; {read_time} Min. Lesezeit</div>
  <h1>{html_escape(title)}</h1>
  <p class="byline">Von <strong>{AUTHOR}</strong> · CanGo Empire</p>
  <p class="opening">{html_escape(excerpt)}</p>

  {body_html}
  {pullquote_html}
  <div class="cta-block">
    <h3>Automatisiere dein Business</h3>
    <p>Erfahre, wie CanGo Empire Unternehmen beim Aufbau von KI-gestützten Systemen unterstützt.</p>
    <a href="../index.html#contact" class="cta-btn">Kostenlose Beratung</a>
  </div>
  <div class="tags">
{tags_html}
  </div>
  <div class="related-articles">
    <h4>Verwandte Artikel</h4>
{related_html}
  </div>
  <footer class="blog-footer">
    <p>© 2026 <a href="../index.html">CanGo Empire</a> · <a href="../index.html#impressum">Impressum</a> · <a href="../index.html#datenschutz">Datenschutz</a></p>
  </footer>
</article>
</body>
</html>"""

# ── blogs.html Karte ──────────────────────────────────────────────────────────

def build_blog_card(payload: dict) -> str:
    slug     = payload["slug"]
    title    = html_escape(payload["title"])
    niche    = html_escape(payload["niche"])
    excerpt  = html_escape(payload.get("excerpt", "")[:120])
    img_path = f"../images/blog-sections/{slug}-hero.jpg"

    return (
        f'\n      <a class="blog-card" href="blogs/{slug}.html">\n'
        f'        <div class="card-img" style="background:url(\'{img_path}\') center/cover no-repeat;'
        f' aspect-ratio:16/9; border-radius:6px 6px 0 0;"></div>\n'
        f'        <div class="card-body" style="padding:1rem;">\n'
        f'          <div class="card-meta" style="font-size:.7rem;text-transform:uppercase;'
        f'letter-spacing:.1em;color:#F97316;margin-bottom:.5rem;">{niche}</div>\n'
        f'          <h3 style="font-size:1rem;color:#fff;margin-bottom:.4rem;">{title}</h3>\n'
        f'          <p style="font-size:.82rem;color:#94A3B8;line-height:1.5;">{excerpt}…</p>\n'
        f'        </div>\n'
        f'      </a>\n'
    )

def update_blogs_index(card_html: str):
    """Fügt neue Karte direkt nach dem Marker '<!-- NEUE BLOG-CARDS -->' ein."""
    MARKER = "<!-- NEUE BLOG-CARDS -->"
    if not BLOGS_INDEX.exists():
        log(f"⚠ blogs.html nicht gefunden: {BLOGS_INDEX}")
        return
    content = BLOGS_INDEX.read_text(encoding="utf-8")
    if MARKER not in content:
        log("⚠ Marker '<!-- NEUE BLOG-CARDS -->' nicht in blogs.html gefunden")
        return
    updated = content.replace(MARKER, MARKER + card_html, 1)
    BLOGS_INDEX.write_text(updated, encoding="utf-8")

# ── Deploy ────────────────────────────────────────────────────────────────────

def deploy(slug: str):
    """
    WWW_ROOT ist bereits das Nginx-Verzeichnis auf dem VPS.
    Wenn du lokal arbeitest und rsync brauchst, passe diese Funktion an.
    Aktuell: Dateien werden direkt in WWW_ROOT geschrieben → sofort live.
    """
    log(f"  ✓ Deploy: {BASE_URL}/blogs/{slug}.html")

# ── Logging ───────────────────────────────────────────────────────────────────

def log(msg: str):
    print(msg, file=sys.stderr)

# ── Hauptroutine ──────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="CanGo Blog Generator")
    parser.add_argument("--b64", help="Base64-kodierter JSON-Payload")
    parser.add_argument("--file", help="Pfad zu JSON-Payload-Datei")
    args = parser.parse_args()

    # Payload laden
    if args.b64:
        raw = base64.b64decode(args.b64).decode("utf-8")
        payload = json.loads(raw)
    elif args.file:
        payload = json.loads(Path(args.file).read_text(encoding="utf-8"))
    else:
        payload = json.loads(sys.stdin.read())

    # Pflichtfelder prüfen
    for field in ["title", "niche", "content_markdown"]:
        if not payload.get(field):
            print(json.dumps({"success": False, "error": f"Fehlendes Feld: {field}"}))
            sys.exit(1)

    # Slug & Datum
    date = payload.get("date") or datetime.now().strftime("%Y-%m-%d")
    title_slug = slugify(payload["title"])
    slug = f"{date}-{title_slug}"
    payload["slug"] = slug
    payload["date"] = date
    payload["read_time"] = reading_time(payload["content_markdown"])

    log(f"\n{'='*60}")
    log(f"CanGo Blog Generator – {slug}")
    log(f"{'='*60}")

    # Verzeichnisse sicherstellen
    BLOGS_DIR.mkdir(parents=True, exist_ok=True)
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)

    # Depositphotos-Bilder
    keyword         = payload.get("dp_keyword") or payload["title"]
    section_kws     = payload.get("section_keywords", [payload["niche"]] * 3)
    image_urls      = fetch_depositphotos_images(keyword, section_kws)

    # Bilder herunterladen
    for key in ["hero", "s1", "s2", "s3"]:
        if key in image_urls:
            suffix = "hero" if key == "hero" else f"section-{key[1]}"
            dest   = IMAGES_DIR / f"{slug}-{suffix}.jpg"
            ok     = download_image(image_urls[key], dest)
            if ok:
                log(f"  ✓ Bild gespeichert: {dest.name}")

    # HTML generieren
    body_html = markdown_to_html(payload["content_markdown"], image_urls, slug)
    full_html = build_blog_html(payload, image_urls, body_html)

    # Blog-HTML schreiben
    blog_file = BLOGS_DIR / f"{slug}.html"
    blog_file.write_text(full_html, encoding="utf-8")
    log(f"  ✓ Blog-HTML: {blog_file}")

    # blogs.html updaten
    card_html = build_blog_card(payload)
    update_blogs_index(card_html)
    log(f"  ✓ blogs.html aktualisiert")

    # Deploy
    deploy(slug)

    result = {
        "success":  True,
        "slug":     slug,
        "url":      f"{BASE_URL}/blogs/{slug}.html",
        "title":    payload["title"],
        "niche":    payload["niche"],
        "date":     date,
        "read_time": payload["read_time"],
        "images":   list(image_urls.keys()),
    }
    print(json.dumps(result, ensure_ascii=False))

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        import traceback
        traceback.print_exc(file=sys.stderr)
        print(json.dumps({"success": False, "error": str(e)}))
        sys.exit(1)
