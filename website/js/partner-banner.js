/* CanGo App Empire – Einheitlicher Slider-Banner unter der Menüleiste
   4 Slides wechseln automatisch, gleicher Banner auf allen Seiten */
(function() {
  var SLIDES = [
    'Rabattcode <strong>«CanGo App Empire»</strong> auf externen Partnerseiten oder <strong>«CanGo App Empire»</strong> im Kontaktformular angeben – so erkennt unser System, woher du kommst.',
    'Rabattcode <strong>«CanGo App Empire»</strong> auf externen Partnerseiten – sicher dir Zusatz-Rabatte!',
    'Der Verkauf startet erst ab dem <strong>06.06.2026</strong> – diese Website befindet sich bis dahin in der Entwicklung.',
    '100+ Tools · 33 Master-Workflows · Über unsere Affiliate-Links erhältst du die besten Deals inkl. AppSumo Lifetime-Deals.',
    'Ein Verkauf findet derzeit noch nicht statt. Ab dem <strong>06.06.2026</strong> geht es los – wir freuen uns auf den Start!'
  ];
  var SLIDE_INTERVAL = 10000; /* 10s Wechsel */
  var currentSlide = 0;

  function buildBannerHTML() {
    var slidesHtml = SLIDES.map(function(text, i) {
      return '<span class="partner-banner__slide' + (i === 0 ? ' active' : '') + '" data-slide="' + i + '">' + text + '</span>';
    }).join('');
    return '<div class="partner-banner" id="partnerBanner" role="banner">' +
      '<span class="partner-banner__icon" aria-hidden="true">🎯</span>' +
      '<span class="partner-banner__text">' + slidesHtml + '</span>' +
      '<button class="partner-banner__close" aria-label="Banner schließen" type="button">×</button>' +
      '</div>';
  }

  function ensureBanner() {
    if (document.getElementById('partnerBanner')) return;
    var wrap = document.createElement('div');
    wrap.innerHTML = buildBannerHTML();
    var banner = wrap.firstElementChild;
    var nav = document.querySelector('nav');
    if (nav && nav.nextSibling) {
      nav.parentNode.insertBefore(banner, nav.nextSibling);
    } else if (nav) {
      nav.parentNode.appendChild(banner);
    } else {
      document.body.insertBefore(banner, document.body.firstChild);
    }
    var btn = banner.querySelector('.partner-banner__close');
    if (btn) btn.addEventListener('click', closePartnerBanner);
  }

  function showNextSlide() {
    var banner = document.getElementById('partnerBanner');
    if (!banner) return;
    var slides = banner.querySelectorAll('.partner-banner__slide');
    if (slides.length === 0) return;
    slides[currentSlide].classList.remove('active');
    currentSlide = (currentSlide + 1) % slides.length;
    slides[currentSlide].classList.add('active');
  }

  function initPartnerBanner() {
    ensureBanner();
    var b = document.getElementById('partnerBanner');
    if (!b) return;
    setTimeout(function() {
      b.classList.add('show');
      document.body.classList.add('has-banner');
    }, 300);
    setInterval(showNextSlide, SLIDE_INTERVAL);
  }

  window.closePartnerBanner = function() {
    var b = document.getElementById('partnerBanner');
    if (b) {
      b.classList.remove('show');
      setTimeout(function() {
        document.body.classList.remove('has-banner');
      }, 300);
    }
  };

  if (document.readyState !== 'loading') {
    initPartnerBanner();
  } else {
    document.addEventListener('DOMContentLoaded', initPartnerBanner);
  }
  window.addEventListener('pageshow', function(e) {
    if (e.persisted) initPartnerBanner();
  });
})();
