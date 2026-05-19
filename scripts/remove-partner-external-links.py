#!/usr/bin/env python3
"""Entfernt externe Produktpartner-Links; CTAs → Bedarfsanalyse (Kontaktformular)."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "website"
KONTAKT = "/kontakt.html#kontaktformular"
PARTNER = re.compile(
    r"(?i)(myvi\.de|mitnorm\.de|mynorm\.de|mitnormfirmenberatung|"
    r"wir-?personalberater\.de|daskarriereinstitut|energyfinance|domicil-group|grsti\.de)"
)


def is_partner(href: str) -> bool:
    return bool(href and PARTNER.search(href))


def process(text: str) -> tuple[str, int]:
    count = 0

    def tag_span(m: re.Match[str]) -> str:
        nonlocal count
        count += 1
        attrs, inner = m.group(1), m.group(2)
        attrs = re.sub(r'\s*href="[^"]*"', "", attrs)
        attrs = re.sub(r'\s*target="_blank"', "", attrs)
        attrs = re.sub(r'\s*rel="[^"]*"', "", attrs)
        return f"<span{attrs}>{inner}</span>"

    text = re.sub(
        r'<a(\s+class="partner-tag"[^>]*)>([^<]*)</a>',
        tag_span,
        text,
    )

    def td_plain(m: re.Match[str]) -> str:
        nonlocal count
        href, label = m.group(1), m.group(2)
        if not is_partner(href):
            return m.group(0)
        count += 1
        return label

    text = re.sub(
        r'<a href="([^"]+)" target="_blank" rel="noopener">([^<]+)</a>',
        td_plain,
        text,
    )

    text, n = re.subn(
        r'<a(\s+class="hr-partner-card[^"]*")\s+href="[^"]*"\s+target="_blank"\s+rel="noopener">',
        r"<div\1>",
        text,
    )
    count += n

    def href_kontakt(m: re.Match[str]) -> str:
        nonlocal count
        href = m.group(1)
        if not is_partner(href):
            return m.group(0)
        count += 1
        return f'href="{KONTAKT}"'

    text = re.sub(r'href="([^"]*)"', href_kontakt, text)
    return text, count


def main() -> int:
    updated = []
    for path in sorted(ROOT.rglob("*.html")):
        orig = path.read_text(encoding="utf-8")
        new, n = process(orig)
        if new != orig:
            path.write_text(new, encoding="utf-8")
            updated.append((path.relative_to(ROOT), n))
    print(f"OK: {len(updated)} Dateien")
    for rel, n in updated:
        print(f"  {rel} ({n})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
