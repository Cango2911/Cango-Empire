/* CanGo App Empire – Einheitlicher Release-Ribbon (Gelb-Orange-Kupfer)
   Wird unter der Menüleiste eingefügt, 5 Slides alle 5 Sek */
(function() {
  var MESSAGES = [
    'Rabattcode «CanGo App Empire» auf externen Partnerseiten oder «CanGo App Empire» im Kontaktformular angeben – so erkennt unser System, woher du kommst.',
    'Rabattcode «CanGo App Empire» auf externen Partnerseiten – sicher dir Zusatz-Rabatte!',
    'Der Verkauf startet erst ab dem 06.06.2026 – diese Website befindet sich bis dahin in der Entwicklung.',
    '100+ Tools · 33 Master-Workflows · Über unsere Affiliate-Links erhältst du die besten Deals inkl. AppSumo Lifetime-Deals.',
    'Ein Verkauf findet derzeit noch nicht statt. Ab dem 06.06.2026 geht es los – wir freuen uns auf den Start!'
  ];
  var INTERVAL = 10000; /* 10s Wechsel */
  function ensureRibbon() {
    if (document.getElementById('releaseRibbon')) return;
    var nav = document.querySelector('nav');
    var ribbon = document.createElement('div');
    ribbon.className = 'release-ribbon';
    ribbon.id = 'releaseRibbon';
    ribbon.setAttribute('role', 'banner');
    ribbon.innerHTML = '<span id="ribbon-slide-text" class="ribbon-slide-text"></span><span id="ribbon-countdown" class="ribbon-countdown"></span>';
    if (nav && nav.nextSibling) nav.parentNode.insertBefore(ribbon, nav.nextSibling);
    else if (nav) nav.parentNode.appendChild(ribbon);
    else document.body.insertBefore(ribbon, document.body.firstChild);
  }
  function runSlides() {
    var el = document.getElementById('ribbon-slide-text');
    if (!el) return;
    var idx = 0;
    el.textContent = MESSAGES[0];
    setInterval(function() {
      el.classList.add('fade');
      setTimeout(function() {
        idx = (idx + 1) % MESSAGES.length;
        el.textContent = MESSAGES[idx];
        el.classList.remove('fade');
      }, 400);
    }, INTERVAL);
  }
  function runCountdown() {
    var KEY = 'cango_release_start';
    var start = parseInt(localStorage.getItem(KEY) || Date.now(), 10);
    if (!localStorage.getItem(KEY)) localStorage.setItem(KEY, String(start));
    var end = start + (365 * 24 * 60 * 60 * 1000);
    function pad(n) { return n < 10 ? '0' + n : String(n); }
    function update() {
      var diff = Math.max(0, end - Date.now());
      var d = Math.floor(diff / 86400000);
      var h = Math.floor((diff % 86400000) / 3600000);
      var m = Math.floor((diff % 3600000) / 60000);
      var rEl = document.getElementById('ribbon-countdown');
      if (rEl) rEl.textContent = d + ' T ' + pad(h) + ':' + pad(m);
    }
    update();
    setInterval(update, 60000);
  }
  function init() {
    ensureRibbon();
    runSlides();
    runCountdown();
  }
  if (document.readyState !== 'loading') init();
  else document.addEventListener('DOMContentLoaded', init);
})();
