#!/usr/bin/env python3
"""Ersetzt die alte Nav (nav__inner, nav__menu) durch die neue Empire-Nav (nav-inner, logo, nav-links) in allen Tool-*.html."""
import re
import os

NEW_NAV = '''    <nav>
  <div class="nav-inner">
    <a href="/index.html" class="logo"><div class="logo-c">C</div><div class="logo-text">CanGo <span>App Empire</span></div></a>
    <ul class="nav-links">
      <li><a href="/index.html">Startseite</a></li>
      <li><a href="/ueber-uns.html">Über Uns</a></li>
      <li><a href="/produkte.html">Produkte</a></li>
      <li><a href="/workflows.html">Workflows</a></li>
      <li><a href="/nischen.html">Marktplatz</a></li>
      <li><a href="/blogs.html">Blogs</a></li>
      <li><a href="/kontakt.html">Kontakt</a></li>
      <li><a href="/faq.html">FAQ</a></li>
      <li><a href="/login.html">Login</a></li>
    </ul>
    <div class="nav-right">
      <a href="/kasse.html" class="nav-cart">🛒 <span class="cart-badge">0</span></a>
      <a href="/kontakt.html#kontaktformular" class="btn btn-o">Jetzt anfragen</a>
    </div>
  </div>
</nav>'''

# Match old nav: first <nav> block that contains nav__inner, until its </nav>
OLD_NAV_PATTERN = re.compile(
    r'\s*<nav[^>]*>.*?</nav>',
    re.DOTALL
)

def main():
    dir_ = os.path.dirname(os.path.abspath(__file__))
    count = 0
    for name in os.listdir(dir_):
        if not name.endswith('.html') or name.startswith('replace'):
            continue
        path = os.path.join(dir_, name)
        with open(path, 'r', encoding='utf-8') as f:
            text = f.read()
        if 'nav__inner' not in text:
            continue

        def repl(m):
            return NEW_NAV if 'nav__inner' in m.group(0) else m.group(0)

        new_text = OLD_NAV_PATTERN.sub(repl, text, count=1)
        if new_text != text:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_text)
            print('OK:', name)
            count += 1
    print('Fertig. Ersetzt:', count)

if __name__ == '__main__':
    main()
