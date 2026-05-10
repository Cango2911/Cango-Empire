/**
 * CanGo App Empire — KPI-Events mit Conversion-Kontext (Trichter, Bereich, Platzierung)
 *
 * Die fünf Kern-KPIs (unverändert):
 * 1) kpi_kontakt_cta
 * 2) kpi_kontakt_submit
 * 3) kpi_pakete_section
 * 4) kpi_marktplatz_entry
 * 5) kpi_checkout_start
 *
 * Zusätzlich pro Hit (dataLayer + CustomEvent):
 * - cango_funnel_step — Zuordnung zur Analyse (discovery → conversion)
 * - cango_page_bereich — Seitenrolle (aus body data-cango-page-bereich oder Pfad-Inferenz)
 * - cango_placement — wo geklickt (nav | sticky_bar | footer | hero | content | form_submit)
 * - cango_content_bereich — optional data-cango-bereich am Element/Ancestor oder section[id]
 *
 * HTML (optional):
 *   data-cango-kpi="kpi_…"
 *   data-cango-kpi-placement="nav"  (überschreibt Auto-Erkennung)
 *   data-cango-bereich="pakete"     (Inhalts-Label für Reporting)
 * <body data-cango-page-bereich="produkte">  (überschreibt Pfad-Inferenz)
 *
 * Programm: window.CANGO_emitKpi('kpi_kontakt_submit', { cango_placement: 'form_submit' });
 *
 * DSGVO: window.CANGO_KPI_ALLOWED = false; setzen, wenn keine Messung erlaubt ist.
 */
(function () {
  'use strict';

  var FUNNEL_BY_KPI = {
    kpi_marktplatz_entry: 'discovery',
    kpi_pakete_section: 'interest',
    kpi_kontakt_cta: 'intent',
    kpi_checkout_start: 'commerce',
    kpi_kontakt_submit: 'conversion'
  };

  function kpiAllowed() {
    return window.CANGO_KPI_ALLOWED !== false;
  }

  function inferPageBereich() {
    var body = document.body;
    if (body) {
      var ex = body.getAttribute('data-cango-page-bereich');
      if (ex) return ex;
    }
    var path = window.location.pathname || '/';
    var file = (path.split('/').pop() || '').toLowerCase();
    if (!file || file === 'index.html' || path.endsWith('/')) return 'hauptseite';
    if (file === 'nischen.html' || file === 'marktplatz.html') return 'marktplatz';
    if (file === 'produkte.html') return 'produkte';
    if (file === 'workflows.html') return 'workflows';
    if (file === 'blogs.html') return 'blogs';
    if (file === 'kontakt.html') return 'kontakt';
    if (file === 'faq.html' || file === 'cyber-assistant.html') return 'support';
    if (file === 'login.html') return 'login';
    if (file === 'kasse.html' || file === 'checkout.html') return 'checkout';
    if (file === 'ueber-uns.html') return 'unternehmen';
    if (file === 'hq.html') return 'intern';
    if (/impressum|datenschutz|\bagb\b|widerruf|disclaimer/i.test(file)) return 'rechtlich';
    if (file === 'selfmade-empire.html' || file === 'workflow-detail.html') return 'selfmade';
    return 'branche';
  }

  function detectPlacement(el) {
    if (!el || typeof el.getAttribute !== 'function') return 'content';
    var manual = el.getAttribute('data-cango-kpi-placement');
    if (manual) return manual;
    if (el.closest && el.closest('.primary-cta-mobile-bar')) return 'sticky_bar';
    if (el.closest && el.closest('nav')) return 'nav';
    if (el.closest && (el.closest('.cango-footer') || el.closest('footer'))) return 'footer';
    if (el.closest && el.closest('.hero, .hr-hero, .phero, [class*="hero__"]'))
      return 'hero';
    return 'content';
  }

  function detectContentBereich(el) {
    if (!el) return '';
    var direct = el.getAttribute && el.getAttribute('data-cango-bereich');
    if (direct) return direct;
    if (el.closest) {
      var wrap = el.closest('[data-cango-bereich]');
      if (wrap) return wrap.getAttribute('data-cango-bereich') || '';
    }
    if (el.closest) {
      var sec = el.closest('section[id]');
      if (sec && sec.id) return sec.id;
    }
    return '';
  }

  function emit(name, extra) {
    if (!kpiAllowed() || !name) return;
    var payload = {
      event: 'cango_kpi',
      kpi_name: name,
      page_path: window.location.pathname || '/',
      cango_funnel_step: FUNNEL_BY_KPI[name] || 'engagement',
      cango_page_bereich: inferPageBereich()
    };
    if (extra && typeof extra === 'object') {
      for (var k in extra) {
        if (Object.prototype.hasOwnProperty.call(extra, k)) payload[k] = extra[k];
      }
    }
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push(payload);
    try {
      window.dispatchEvent(new CustomEvent('cango-kpi', { detail: { name: name, payload: payload } }));
    } catch (e) { /* noop */ }
  }

  window.CANGO_emitKpi = emit;

  document.addEventListener('click', function (ev) {
    if (!kpiAllowed()) return;
    var t = ev.target;
    if (!t || typeof t.closest !== 'function') return;
    var el = t.closest('[data-cango-kpi]');
    if (!el) return;
    var name = el.getAttribute('data-cango-kpi');
    if (!name) return;
    var contentBereich = detectContentBereich(el);
    var clickExtra = {
      trigger: el.tagName,
      cango_placement: detectPlacement(el)
    };
    if (contentBereich) clickExtra.cango_content_bereich = contentBereich;
    emit(name, clickExtra);
  }, true);
})();
