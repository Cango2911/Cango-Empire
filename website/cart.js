/**
 * CanGo Empire – Zentraler Warenkorb
 * Unterstützt: Workflows, Produkte/Tools, Pakete
 * Mit Mengensteuerung und animiertem Badge
 */
(function() {
  'use strict';

  const CART_KEY = 'cango_empire_cart';
  const UNIFIED_SHELL_STYLE_ID = 'cango-unified-shell-style';
  const EXCLUDED_SHELL_PATHS = new Set([
    '/',
    '/index.html'
  ]);

  function shouldApplyUnifiedShell() {
    const p = (window.location.pathname || '').toLowerCase();
    if (EXCLUDED_SHELL_PATHS.has(p)) return false;
    if (!p.endsWith('.html')) return false;
    // Redirect-/Maintenance-Seiten nicht umschreiben.
    if (document.querySelector('meta[http-equiv="refresh"]')) return false;
    return true;
  }

  function ensureUnifiedShellStyles() {
    if (document.getElementById(UNIFIED_SHELL_STYLE_ID)) return;
    const style = document.createElement('style');
    style.id = UNIFIED_SHELL_STYLE_ID;
    style.textContent = `
      .cango-shell-nav{position:sticky;top:0;z-index:100;background:rgba(8,13,26,.88);-webkit-backdrop-filter:blur(20px);backdrop-filter:blur(20px);border-bottom:1px solid rgba(78,99,130,0.25);padding:0 24px;height:68px;display:flex;align-items:center;justify-content:center}
      .cango-shell-nav .nav-inner{max-width:1200px;width:100%;display:flex;align-items:center;justify-content:space-between}
      .cango-shell-nav .logo{font-size:18px;font-weight:800;display:flex;align-items:center;gap:10px;text-decoration:none;color:inherit}
      .cango-shell-nav .logo-c{width:34px;height:34px;background:#F97316;color:#000;border-radius:8px;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:16px}
      .cango-shell-nav .logo-text{color:#fff}
      .cango-shell-nav .logo-text span{color:#7a91ab;font-weight:400}
      .cango-shell-nav .nav-links{display:flex;align-items:center;gap:2px;list-style:none}
      .cango-shell-nav .nav-links a{font-size:13px;font-weight:500;color:#7a91ab;text-decoration:none;padding:6px 11px;border-radius:8px;transition:all .2s}
      .cango-shell-nav .nav-links a:hover,.cango-shell-nav .nav-links a.active{color:#fff;background:#162238}
      .cango-shell-nav .nav-links a.active{color:#F97316}
      .cango-shell-nav .nav-right{display:flex;align-items:center;gap:10px}
      .cango-shell-nav .nav-cart{font-size:13px;color:#7a91ab;border:1px solid rgba(78,99,130,0.25);padding:6px 14px;border-radius:8px;cursor:pointer;background:#111c30;transition:all .2s;text-decoration:none;display:inline-flex;align-items:center;gap:6px}
      .cango-shell-nav .nav-cart:hover{border-color:#F97316;color:#F97316}
      .cango-shell-nav .nav-cart .cart-badge{background:#F97316;color:#000;font-size:10px;font-weight:800;min-width:18px;height:18px;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-family:'JetBrains Mono',monospace}
      .cango-shell-nav .btn{display:inline-flex;align-items:center;justify-content:center;font-family:'Outfit',sans-serif;font-weight:600;font-size:13px;padding:10px 22px;border-radius:10px;cursor:pointer;transition:all .2s;text-decoration:none;border:none;letter-spacing:.01em}
      .cango-shell-nav .btn-o{background:#F97316;color:#000}
      .cango-shell-nav .btn-o:hover{background:#fb923c;transform:translateY(-1px);box-shadow:0 8px 24px rgba(249,115,22,.3)}
      .cango-shell-nav .nav-toggle{display:none;background:none;border:none;color:#fff;font-size:24px;cursor:pointer;padding:8px}
      .cango-shell-footer{background:#080d1a;border-top:1px solid rgba(78,99,130,.25);padding:72px 24px 40px;position:relative;z-index:1}
      .cango-shell-footer .footer-wrap{max-width:1200px;margin:0 auto}
      .cango-shell-footer .ftop{display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:48px;margin-bottom:56px}
      .cango-shell-footer .fbrand p{font-size:14px;color:#7a91ab;line-height:1.75;margin-top:14px;max-width:260px}
      .cango-shell-footer .logo{font-size:18px;font-weight:800;display:flex;align-items:center;gap:10px;text-decoration:none}
      .cango-shell-footer .logo-c{width:34px;height:34px;background:#F97316;color:#000;border-radius:8px;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:16px}
      .cango-shell-footer .logo-text{color:#ffffff}
      .cango-shell-footer .logo-text span{color:#7a91ab;font-weight:400}
      .cango-shell-footer .fcol h5{font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:#F97316;margin-bottom:18px}
      .cango-shell-footer .fcol ul{list-style:none}
      .cango-shell-footer .fcol ul li{margin-bottom:10px}
      .cango-shell-footer .fcol ul li a{font-size:14px;color:#7a91ab;text-decoration:none;transition:color .2s}
      .cango-shell-footer .fcol ul li a:hover{color:#ffffff}
      .cango-shell-footer .fbot{border-top:1px solid rgba(78,99,130,.12);padding-top:28px;display:flex;justify-content:space-between;align-items:center}
      .cango-shell-footer .fcopy{font-size:13px;color:#4a607a}
      .cango-shell-footer .fcopy em{display:block;font-style:italic;font-size:12px;margin-top:2px;opacity:.6}
      @media(max-width:960px){.cango-shell-nav{padding:0 16px}.cango-shell-nav .nav-toggle{display:block}.cango-shell-nav .nav-links{display:none;position:absolute;top:68px;left:0;right:0;background:rgba(8,13,26,.98);padding:16px;flex-direction:column;align-items:flex-start;border-bottom:1px solid rgba(78,99,130,0.25)}.cango-shell-nav .nav-links.nav-open{display:flex}.cango-shell-nav .nav-right{display:none}}
      @media(max-width:900px){.cango-shell-footer .ftop{grid-template-columns:1fr 1fr;gap:40px}}
      @media(max-width:600px){.cango-shell-footer .ftop{grid-template-columns:1fr;gap:32px}}
    `;
    document.head.appendChild(style);
  }

  function linkIsActive(targetHref, path) {
    if (targetHref === '/index.html#branchen') return false;
    if (targetHref === '/nischen.html') {
      return path === '/nischen.html' || path.startsWith('/marktplatz/');
    }
    return path === targetHref;
  }

  function renderUnifiedNav() {
    const path = (window.location.pathname || '').toLowerCase();
    const nav = document.createElement('nav');
    nav.className = 'cango-shell-nav';
    nav.setAttribute('data-cango-unified-nav', '1');
    nav.setAttribute('aria-label', 'Hauptnavigation');
    nav.innerHTML = `
      <div class="nav-inner">
        <a href="/index.html" class="logo"><div class="logo-c">C</div><div class="logo-text">CanGo <span>App Empire</span></div></a>
        <button type="button" class="nav-toggle" id="navToggle" aria-label="Menü öffnen oder schließen">☰</button>
        <ul class="nav-links">
          <li><a href="/index.html">Startseite</a></li>
          <li><a href="/ueber-uns.html">Über Uns</a></li>
          <li><a href="/produkte.html">Produkte</a></li>
          <li><a href="/workflows.html">Workflows</a></li>
          <li><a href="/nischen.html">Marktplatz</a></li>
          <li><a href="/index.html#branchen">Branchen</a></li>
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
    `;

    nav.querySelectorAll('.nav-links a').forEach(function(a) {
      const href = (a.getAttribute('href') || '').toLowerCase();
      if (linkIsActive(href, path)) a.classList.add('active');
    });

    const toggle = nav.querySelector('#navToggle');
    const links = nav.querySelector('.nav-links');
    if (toggle && links) {
      toggle.addEventListener('click', function() {
        links.classList.toggle('nav-open');
      });
    }
    return nav;
  }

  function renderUnifiedFooter() {
    const footer = document.createElement('footer');
    footer.className = 'cango-shell-footer';
    footer.setAttribute('data-cango-unified-footer', '1');
    footer.innerHTML = `
      <div class="footer-wrap">
        <div class="ftop">
          <div class="fbrand">
            <a href="/index.html" class="logo"><div class="logo-c">C</div><div class="logo-text">CanGo <span>App Empire</span></div></a>
            <p>Marketing-Automatisierung für den DACH-Markt. 33 Content-Maschinen. 30 KI-Systeme. Kein Bullshit.</p>
          </div>
          <div class="fcol"><h5>Produkt</h5><ul><li><a href="/nischen.html">Marktplatz</a></li><li><a href="/index.html#pakete">Preise</a></li></ul></div>
          <div class="fcol"><h5>Unternehmen</h5><ul><li><a href="/ueber-uns.html">Über uns</a></li><li><a href="/karriere-hr.html">Karriere</a></li></ul></div>
          <div class="fcol"><h5>Rechtliches</h5><ul><li><a href="/impressum.html">Impressum</a></li><li><a href="/datenschutz.html">Datenschutz</a></li><li><a href="/disclaimer.html">Disclaimer</a></li><li><a href="/agb.html">AGB</a></li><li><a href="/widerruf.html">Widerrufserklärung</a></li></ul></div>
        </div>
        <div class="fbot">
          <div class="fcopy">© 2026 CanGo App Empire. Alle Rechte vorbehalten.<em>Kopieren hilft dir nicht – du brauchst die Maschine.</em></div>
        </div>
      </div>
    `;
    return footer;
  }

  function initUnifiedShell() {
    if (!shouldApplyUnifiedShell()) return;
    if (document.body && document.body.getAttribute('data-cango-keep-shell') === '1') return;

    ensureUnifiedShellStyles();

    const existingNav = document.querySelector('nav');
    if (existingNav && existingNav.getAttribute('data-cango-unified-nav') !== '1') {
      existingNav.parentNode.replaceChild(renderUnifiedNav(), existingNav);
    } else if (!existingNav) {
      document.body.insertBefore(renderUnifiedNav(), document.body.firstChild);
    }

    const existingFooter = document.querySelector('footer');
    if (existingFooter && existingFooter.getAttribute('data-cango-unified-footer') !== '1') {
      existingFooter.parentNode.replaceChild(renderUnifiedFooter(), existingFooter);
    } else if (!existingFooter) {
      document.body.appendChild(renderUnifiedFooter());
    }
  }

  /** Gültiger Eintrag hat mindestens type, id, workflowId, toolId oder tier (keine Phantom-Einträge nur mit quantity). */
  function isValidItem(item) {
    if (!item || typeof item !== 'object') return false;
    return !!(item.type || item.id || item.workflowId || item.toolId || item.tier);
  }

  function getCart() {
    try {
      const raw = localStorage.getItem(CART_KEY);
      let items = raw ? JSON.parse(raw) : [];
      if (!Array.isArray(items)) return [];
      items = items.filter(isValidItem);
      if (items.length === 0 && raw) {
        try {
          var parsed = JSON.parse(raw);
          if (Array.isArray(parsed) && parsed.length > 0) {
            localStorage.setItem(CART_KEY, '[]');
          }
        } catch (e) {}
      }
      return items;
    } catch {
      return [];
    }
  }

  function setCart(items) {
    localStorage.setItem(CART_KEY, JSON.stringify(items));
    updateCartBadge();
    if (typeof window.onCartChange === 'function') window.onCartChange(items);
  }

  function itemKey(item) {
    if (item.type === 'workflow') return `wf:${item.workflowId || item.id}`;
    if (item.type === 'package') return `pkg:${item.tier || item.id}`;
    return `tool:${item.toolId || item.id}:${item.planName || ''}`;
  }

  function addToCart(item, qty = 1) {
    const cart = getCart();
    const key = itemKey(item);
    const existing = cart.find(i => itemKey(i) === key);
    if (existing) {
      existing.quantity = (existing.quantity || 1) + qty;
    } else {
      cart.push({ ...item, quantity: qty });
    }
    setCart(cart);
    animateBadge();
    return cart;
  }

  function updateQuantity(key, delta) {
    const cart = getCart();
    const idx = cart.findIndex(i => itemKey(i) === key);
    if (idx < 0) return cart;
    const item = cart[idx];
    item.quantity = Math.max(1, (item.quantity || 1) + delta);
    if (item.quantity <= 0) {
      cart.splice(idx, 1);
    }
    setCart(cart);
    return cart;
  }

  function removeFromCart(key) {
    const cart = getCart().filter(i => itemKey(i) !== key);
    setCart(cart);
    return cart;
  }

  function getTotalItems() {
    return getCart().reduce((sum, i) => sum + (i.quantity || 1), 0);
  }

  function getTotalPrice() {
    return getCart().reduce((sum, i) => {
      const p = (i.price || 0) * (i.quantity || 1);
      const setup = (i.setup || 0) * (i.quantity || 1);
      return sum + p + setup;
    }, 0);
  }

  function updateCartBadge() {
    const n = getTotalItems();
    // Alle Badges aktualisieren (auch bei doppelten IDs auf manchen Seiten)
    const badges = document.querySelectorAll('.cart-badge');
    badges.forEach(function(badge) {
      badge.textContent = n;
      badge.style.display = n > 0 ? 'flex' : 'none';
    });
  }

  function animateBadge() {
    const badge = document.querySelector('.cart-badge');
    if (!badge) return;
    badge.classList.remove('cart-badge--bump');
    void badge.offsetWidth;
    badge.classList.add('cart-badge--bump');
    setTimeout(() => badge.classList.remove('cart-badge--bump'), 400);
  }

  window.CanGoCart = {
    getCart,
    setCart,
    addToCart,
    updateQuantity,
    removeFromCart,
    getTotalItems,
    getTotalPrice,
    itemKey,
    updateCartBadge,
    animateBadge,
    CART_KEY
  };

  // Badge beim Laden aktualisieren – einheitliche Darstellung auf allen Seiten
  function initBadge() {
    initUnifiedShell();
    updateCartBadge();
  }
  function scheduleInit() {
    initBadge();
    // Retry falls DOM noch nicht fertig (z.B. bei langen Seiten)
    setTimeout(initBadge, 50);
    setTimeout(initBadge, 200);
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', scheduleInit);
  } else {
    scheduleInit();
  }
  window.addEventListener('load', initBadge);
  window.addEventListener('pageshow', function(e) { if (e.persisted) scheduleInit(); });
  window.addEventListener('focus', initBadge);
  // Cross-Tab Sync: wenn Warenkorb in anderem Tab geändert wird
  window.addEventListener('storage', function(e) {
    if (e.key === CART_KEY) initBadge();
  });
})();
