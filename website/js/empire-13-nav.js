/**
 * Empire 13 Seiten – Nav aus /data/empire-nav.json rendern
 * Einbinden: <script src="/js/empire-13-nav.js" defer></script>
 * Voraussetzung: Element mit id="empire-13-nav-placeholder" oder data-empire-13-nav="main"
 */
(function () {
  function renderNav(data) {
    var brand = data.brand;
    var links = data.mainNav || [];
    var html = '<div class="e13-nav__inner">';
    html += '<a class="e13-nav__brand" href="' + (brand.href || '/index.html') + '">';
    html += '<span class="e13-nav__brand-icon">' + (brand.icon || 'C') + '</span>';
    html += '<span>' + (brand.label || 'CanGo App Empire') + '</span></a>';
    html += '<button class="e13-nav__toggle" type="button" aria-label="Menü öffnen">☰</button>';
    html += '<ul class="e13-nav__menu">';
    links.forEach(function (item) {
      var cls = item.class ? ' class="' + item.class + '"' : '';
      var label = item.label;
      if (item.cartBadge) label = '🛒 <span id="cart-badge" class="cart-badge" aria-label="Artikel im Warenkorb">0</span>';
      html += '<li><a href="' + item.href + '"' + cls + '>' + label + '</a></li>';
    });
    html += '</ul></div>';
    return html;
  }

  function init() {
    var placeholder = document.getElementById('empire-13-nav-placeholder') || document.querySelector('[data-empire-13-nav="main"]');
    if (!placeholder) return;
    fetch('/data/empire-nav.json?v=1', { cache: 'no-store' })
      .then(function (r) { return r.ok ? r.json() : null; })
      .then(function (data) {
        if (!data) return;
        var nav = document.createElement('nav');
        nav.className = 'e13-nav';
        nav.setAttribute('aria-label', 'Hauptnavigation');
        nav.setAttribute('role', 'navigation');
        nav.innerHTML = renderNav(data);
        placeholder.parentNode.replaceChild(nav, placeholder);
        var toggle = nav.querySelector('.e13-nav__toggle');
        var menu = nav.querySelector('.e13-nav__menu');
        if (toggle && menu) toggle.addEventListener('click', function () { menu.classList.toggle('active'); });
      })
      .catch(function () {});
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
