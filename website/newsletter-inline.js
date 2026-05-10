/**
 * Newsletter-Anmeldung (inline auf Kontakt, FAQ, Blogs).
 * Sendet an n8n Webhook newsletter-signup.
 */
(function() {
  var WEBHOOK = 'https://n8n.automation-cango-app-empire.com/webhook/newsletter-signup';
  function init() {
    var form = document.querySelector('form[data-newsletter-form]');
    if (!form) return;
    var submitBtn = form.querySelector('[type="submit"]');
    var statusEl = form.querySelector('[data-newsletter-status]');
    var page = form.getAttribute('data-newsletter-source') || 'website';
    function setStatus(type, html) {
      if (!statusEl) return;
      statusEl.className = 'newsletter-inline__status newsletter-inline__status--' + type;
      statusEl.innerHTML = html;
      statusEl.style.display = 'block';
    }
    form.addEventListener('submit', function(e) {
      e.preventDefault();
      var email = (form.querySelector('[name="email"]').value || '').trim();
      var consent = form.querySelector('[name="consent"]');
      var consentChecked = consent ? consent.checked : false;
      if (!email) {
        setStatus('error', 'Bitte E-Mail angeben.');
        return;
      }
      if (consent && !consentChecked) {
        setStatus('error', 'Bitte Einwilligung aktivieren.');
        return;
      }
      if (submitBtn) submitBtn.disabled = true;
      setStatus('success', 'Wird gesendet …');
      var payload = {
        email: email,
        name: (form.querySelector('[name="name"]') && form.querySelector('[name="name"]').value) ? form.querySelector('[name="name"]').value.trim() : '',
        source: page,
        page: window.location.pathname || '/',
        consent: true
      };
      fetch(WEBHOOK, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      })
        .then(function(res) {
          if (!res.ok) throw new Error('Network ' + res.status);
          return res.json();
        })
        .then(function(data) {
          if (data && data.success) {
            setStatus('success', 'Danke! Du bist angemeldet.');
            form.reset();
          } else {
            setStatus('error', (data && data.message) || 'Fehler. Bitte später erneut versuchen.');
          }
        })
        .catch(function() {
          setStatus('error', 'Senden fehlgeschlagen. Bitte Verbindung prüfen.');
        })
        .finally(function() {
          if (submitBtn) submitBtn.disabled = false;
        });
    });
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
