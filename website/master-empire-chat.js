(function () {
  const CHAT_WEBHOOK_URL = 'https://n8n.automation-cango-app-empire.com/webhook/master-empire-chat-v1';
  const CHAT_POLL_URL = 'https://n8n.automation-cango-app-empire.com/webhook/master-empire-chat-poll-v1';
  const STORAGE_PREFIX = 'master_empire_chat_state:';
  const CLIENT_STORAGE_KEY = 'empire_client_identity';
  const CLIENT_TTL_MS = 365 * 24 * 60 * 60 * 1000;
  const POLL_INTERVAL_MS = 20000;
  const PRIVACY_URL = '/datenschutz.html';
  const CONTACT_URL = '/kontakt.html?intent=support&entry=chat-compliance-gate&topic=Chat%20Rückfrage';

  function safeParse(value, fallback) {
    try {
      return JSON.parse(value);
    } catch (_error) {
      return fallback;
    }
  }

  function uid(prefix) {
    if (window.crypto && window.crypto.randomUUID) {
      return prefix + window.crypto.randomUUID();
    }
    return prefix + Date.now();
  }

  function getStorageKey(root) {
    return STORAGE_PREFIX + (root.dataset.masterScope || root.dataset.masterPage || window.location.pathname || 'website');
  }

  function readPersistentClient() {
    try {
      const raw = window.localStorage.getItem(CLIENT_STORAGE_KEY);
      const parsed = raw ? safeParse(raw, null) : null;
      if (!parsed || !parsed.empire_client_id || !parsed.expires_at) {
        return null;
      }
      if (new Date(parsed.expires_at).getTime() <= Date.now()) {
        window.localStorage.removeItem(CLIENT_STORAGE_KEY);
        return null;
      }
      return parsed;
    } catch (_error) {
      return null;
    }
  }

  function persistClientIdentity(empireClientId) {
    const payload = {
      empire_client_id: empireClientId,
      first_seen_at: new Date().toISOString(),
      expires_at: new Date(Date.now() + CLIENT_TTL_MS).toISOString()
    };
    try {
      const existing = readPersistentClient();
      if (existing && existing.first_seen_at) {
        payload.first_seen_at = existing.first_seen_at;
      }
      window.localStorage.setItem(CLIENT_STORAGE_KEY, JSON.stringify(payload));
    } catch (_error) {
      // Falls localStorage blockiert ist, bleibt der Chat im Session-Modus.
    }
    return payload.empire_client_id;
  }

  function getPersistentClientId() {
    const existing = readPersistentClient();
    if (existing && existing.empire_client_id) {
      return persistClientIdentity(existing.empire_client_id);
    }
    return persistClientIdentity(uid('empire-'));
  }

  function normalizeState(state) {
    const base = state && typeof state === 'object' ? state : {};
    const persistentClientId = base.empire_client_id || getPersistentClientId();
    return {
      session_id: base.session_id || uid('website-'),
      thread_id: base.thread_id || '',
      customer_key: base.customer_key || persistentClientId,
      empire_client_id: persistentClientId,
      consent_given: Boolean(base.consent_given),
      consent_timestamp: base.consent_timestamp || '',
      consent_rejected: Boolean(base.consent_rejected)
    };
  }

  function getState(root) {
    const key = getStorageKey(root);
    const raw = window.sessionStorage.getItem(key);
    const parsed = raw ? safeParse(raw, null) : null;
    return normalizeState(parsed);
  }

  function saveState(root, state) {
    window.sessionStorage.setItem(getStorageKey(root), JSON.stringify(normalizeState(state)));
  }

  function parseMetadata(value) {
    if (!value) {
      return {};
    }
    if (typeof value === 'object') {
      return value;
    }
    return safeParse(value, {});
  }

  function setStatus(root, text) {
    const status = root.querySelector('[data-master-status]');
    if (status) {
      status.textContent = text;
    }
  }

  function roleLabel(message) {
    if (message.sender_type === 'human') {
      return 'CB';
    }
    if (message.sender_type === 'customer') {
      return 'DU';
    }
    if (message.sender_type === 'system') {
      return 'SYS';
    }
    return 'AI';
  }

  function providerLabel(message) {
    if (message.sender_type === 'human') {
      return 'Founder reply';
    }
    if (message.sender_type === 'customer') {
      return 'Du';
    }
    if (message.sender_type === 'system') {
      return 'System';
    }
    return message.provider || 'Master of Empire';
  }

  function complianceInfoLinks() {
    return [
      {
        label: 'Datenschutzerklaerung',
        url: PRIVACY_URL
      },
      {
        label: 'Direkter Kontakt',
        url: CONTACT_URL
      }
    ];
  }

  function preConsentMessage() {
    return {
      sender_type: 'system',
      provider: 'system',
      message_text: 'Bevor der Chat startet, bestaetige bitte die KI-Offenlegung, die Datenverarbeitung und den Hinweis zum Informationscharakter im Welcome-Gate.',
      metadata_json: JSON.stringify({
        links: complianceInfoLinks()
      })
    };
  }

  function greetingMessage(root) {
    return {
      sender_type: 'bot',
      provider: 'system',
      message_text: root.dataset.masterGreeting || 'Willkommen. Ich bin der CanGo App Empire Architect. Frag mich nach Preisen, Workflows, Setup, Support oder dem besten Einstieg für dein Unternehmen.',
      metadata_json: JSON.stringify({
        links: []
      })
    };
  }

  function renderMessages(root, messages, fallbackLinks) {
    const container = root.querySelector('[data-master-messages]');
    if (!container) {
      return;
    }
    const list = Array.isArray(messages) ? messages : [];
    container.innerHTML = '';
    list.forEach(function (message, index) {
      const meta = parseMetadata(message.metadata_json);
      const wrapper = document.createElement('div');
      const isUser = message.sender_type === 'customer';
      const isSystem = message.sender_type === 'system';
      wrapper.className = 'master-empire__message' + (isUser ? ' master-empire__message--user' : '') + (isSystem ? ' master-empire__message--system' : '');

      const avatar = document.createElement('div');
      avatar.className = 'master-empire__message-avatar' + (message.sender_type === 'human' ? ' master-empire__message-avatar--human' : '') + (isSystem ? ' master-empire__message-avatar--system' : '');
      avatar.textContent = roleLabel(message);

      const bubble = document.createElement('div');
      bubble.className = 'master-empire__message-bubble';
      bubble.textContent = message.message_text || '';

      const messageLinks = Array.isArray(meta.links) && meta.links.length
        ? meta.links
        : (index === list.length - 1 && Array.isArray(fallbackLinks) ? fallbackLinks : []);
      if (messageLinks.length) {
        const linksWrap = document.createElement('div');
        linksWrap.className = 'master-empire__message-links';
        messageLinks.forEach(function (item) {
          const link = document.createElement('a');
          link.className = 'master-empire__message-link';
          link.href = item.url;
          link.textContent = item.label;
          link.target = '_self';
          linksWrap.appendChild(link);
        });
        bubble.appendChild(linksWrap);
      }

      const metaLine = document.createElement('div');
      metaLine.className = 'master-empire__message-meta';
      metaLine.textContent = providerLabel(message);
      bubble.appendChild(metaLine);

      if (isUser) {
        wrapper.appendChild(bubble);
        wrapper.appendChild(avatar);
      } else {
        wrapper.appendChild(avatar);
        wrapper.appendChild(bubble);
      }

      container.appendChild(wrapper);
    });
    container.scrollTop = container.scrollHeight;
  }

  function updateComposerState(root, state) {
    const prompt = root.querySelector('[data-master-prompt]');
    const submit = root.querySelector('[data-master-submit]');
    const examples = root.querySelectorAll('[data-master-example]');
    const locked = !state.consent_given;

    root.classList.toggle('master-empire__chat--locked', locked);
    if (prompt) {
      prompt.disabled = locked;
    }
    if (submit) {
      submit.disabled = locked;
    }
    examples.forEach(function (button) {
      button.disabled = locked;
    });
  }

  function ensureComplianceUi(root) {
    if (!root.querySelector('[data-master-gate]')) {
      const gate = document.createElement('div');
      gate.className = 'master-empire__gate';
      gate.setAttribute('data-master-gate', 'true');
      gate.innerHTML = [
        '<div class="master-empire__gate-panel">',
        '<div class="master-empire__gate-eyebrow">Empire Compliance Gate</div>',
        '<h4 class="master-empire__gate-title" data-master-gate-title></h4>',
        '<p class="master-empire__gate-copy" data-master-gate-copy></p>',
        '<ul class="master-empire__gate-list">',
        '<li>Hallo! Ich bin der CanGo Empire Architect, eine kuenstliche Intelligenz. Moechten Sie mit mir fortfahren?</li>',
        '<li>Ich verarbeite Ihre Eingaben zur Beantwortung Ihrer Anfrage. Informationen dazu finden Sie in unserer <a href="' + PRIVACY_URL + '">Datenschutzerklaerung</a>.</li>',
        '<li>Wichtiger Hinweis: Meine Antworten dienen der Information über unsere Produkte und Workflows. Sie stellen keine Rechts- oder Finanzberatung dar.</li>',
        '</ul>',
        '<div class="master-empire__gate-actions">',
        '<button class="master-empire__gate-accept" data-master-gate-accept type="button">Akzeptieren und Chat starten</button>',
        '<button class="master-empire__gate-decline" data-master-gate-decline type="button">Ablehnen</button>',
        '</div>',
        '<div class="master-empire__gate-links">',
        '<a href="' + PRIVACY_URL + '">Datenschutzerklaerung</a>',
        '<a href="' + CONTACT_URL + '">Direktkontakt</a>',
        '</div>',
        '</div>'
      ].join('');
      root.appendChild(gate);
    }

    if (!root.querySelector('[data-master-disclaimer]')) {
      const form = root.querySelector('[data-master-form]');
      const disclaimer = document.createElement('div');
      disclaimer.className = 'master-empire__disclaimer';
      disclaimer.setAttribute('data-master-disclaimer', 'true');
      disclaimer.innerHTML = [
        '<div class="master-empire__disclaimer-row">',
        '<strong>KI-Hinweis</strong>',
        '<span>Ich bin eine kuenstliche Intelligenz und bearbeite Anfragen zu Produkten, Workflows und Support.</span>',
        '</div>',
        '<div class="master-empire__disclaimer-row">',
        '<strong>Datenschutz</strong>',
        '<span>Ihre Eingaben werden zur Bearbeitung Ihrer Anfrage verarbeitet. Details in der <a href="' + PRIVACY_URL + '">Datenschutzerklaerung</a>.</span>',
        '</div>',
        '<div class="master-empire__disclaimer-row">',
        '<strong>Disclaimer</strong>',
        '<span>KI kann Fehler machen. Bitte verifizieren Sie kritische Informationen mit unserem Team.</span>',
        '</div>'
      ].join('');
      if (form && form.parentNode) {
        form.parentNode.insertBefore(disclaimer, form.nextSibling);
      } else {
        root.appendChild(disclaimer);
      }
    }
  }

  function updateConsentGate(root, state) {
    const gate = root.querySelector('[data-master-gate]');
    const title = root.querySelector('[data-master-gate-title]');
    const copy = root.querySelector('[data-master-gate-copy]');
    if (!gate || !title || !copy) {
      return;
    }

    if (state.consent_given) {
      gate.hidden = true;
      return;
    }

    gate.hidden = false;
    if (state.consent_rejected) {
      title.textContent = 'Chat ist pausiert';
      copy.textContent = 'Ohne Zustimmung startet kein KI-Chat. Sie können später zustimmen oder direkt unser Team kontaktieren.';
    } else {
      title.textContent = 'Bevor wir starten: kurze Zustimmung';
      copy.textContent = 'Ohne Ihre Bestaetigung werden keine Chat-Anfragen an die KI gesendet. Erst danach startet der eigentliche Support- und Beratungsfluss.';
    }
  }

  function updateDisclaimerVisibility(root, state) {
    const disclaimer = root.querySelector('[data-master-disclaimer]');
    if (!disclaimer) {
      return;
    }
    const hideAfterConsent = root.dataset.masterHideDisclaimerOnConsent === 'true';
    disclaimer.hidden = Boolean(hideAfterConsent && state.consent_given);
  }

  function applyConsentState(root, state, options) {
    const nextState = normalizeState(state);
    const config = options || {};
    saveState(root, nextState);
    updateComposerState(root, nextState);
    updateConsentGate(root, nextState);
    updateDisclaimerVisibility(root, nextState);

    if (nextState.consent_given) {
      setStatus(root, 'Consent bestaetigt');
      if (config.showGreeting) {
        renderMessages(root, [greetingMessage(root)]);
      }
      if (nextState.thread_id) {
        pollThread(root, nextState);
      }
      return;
    }

    setStatus(root, nextState.consent_rejected ? 'Chat nicht gestartet' : 'Zustimmung erforderlich');
    if (config.showPreConsentMessage) {
      renderMessages(root, [preConsentMessage()]);
    }
  }

  function attachConsentActions(root) {
    const accept = root.querySelector('[data-master-gate-accept]');
    const decline = root.querySelector('[data-master-gate-decline]');

    if (accept) {
      accept.addEventListener('click', function () {
        const state = getState(root);
        state.consent_given = true;
        state.consent_rejected = false;
        state.consent_timestamp = new Date().toISOString();
        applyConsentState(root, state, { showGreeting: true });
      });
    }

    if (decline) {
      decline.addEventListener('click', function () {
        const state = getState(root);
        state.consent_given = false;
        state.consent_rejected = true;
        state.consent_timestamp = '';
        applyConsentState(root, state, { showPreConsentMessage: true });
      });
    }
  }

  async function pollThread(root, state) {
    if (!state.consent_given || !state.thread_id) {
      return;
    }
    try {
      const url = CHAT_POLL_URL
        + '?thread_id=' + encodeURIComponent(state.thread_id)
        + '&customer_key=' + encodeURIComponent(state.customer_key || '')
        + '&empire_client_id=' + encodeURIComponent(state.empire_client_id || '')
        + '&page=' + encodeURIComponent(root.dataset.masterPage || window.location.pathname || '/index.html');
      const response = await fetch(url, {
        method: 'GET',
        headers: {
          'Accept': 'application/json'
        }
      });
      if (!response.ok) {
        return;
      }
      const result = await response.json();
      if (result.thread_id) {
        state.thread_id = result.thread_id;
      }
      if (result.customer_key) {
        state.customer_key = result.customer_key;
      }
      if (result.consent_given) {
        state.consent_given = true;
        state.consent_timestamp = result.consent_timestamp || state.consent_timestamp;
      }
      saveState(root, state);
      renderMessages(root, result.messages || []);
      setStatus(root, result.status_text || 'AUTO_PILOT aktiv');
      updateComposerState(root, state);
      updateConsentGate(root, state);
      updateDisclaimerVisibility(root, state);
    } catch (_error) {
      // Polling darf still scheitern, damit die UI nicht flackert.
    }
  }

  async function sendMessage(root) {
    const state = getState(root);
    const prompt = root.querySelector('[data-master-prompt]');
    const submit = root.querySelector('[data-master-submit]');
    const text = prompt ? String(prompt.value || '').trim() : '';
    if (!state.consent_given) {
      applyConsentState(root, state, { showPreConsentMessage: true });
      return;
    }
    if (!text || !submit) {
      return;
    }

    submit.disabled = true;
    setStatus(root, 'Antwort wird erstellt...');

    try {
      const response = await fetch(CHAT_WEBHOOK_URL, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        },
        body: JSON.stringify({
          message: text,
          thread_id: state.thread_id || '',
          customer_key: state.customer_key || '',
          empire_client_id: state.empire_client_id || '',
          session_id: state.session_id,
          customer_name: root.dataset.masterCustomerName || 'Website Besucher',
          page: root.dataset.masterPage || window.location.pathname || '/index.html',
          referrer: document.referrer || '',
          consent_given: state.consent_given,
          consent_timestamp: state.consent_timestamp || ''
        })
      });

      if (!response.ok) {
        throw new Error('Webhook antwortete mit Status ' + response.status);
      }

      const result = await response.json();
      if (result.consent_required) {
        state.consent_given = false;
        state.consent_rejected = false;
        state.consent_timestamp = '';
        saveState(root, state);
        renderMessages(root, result.messages || [preConsentMessage()], result.links || complianceInfoLinks());
        setStatus(root, result.status_text || 'Zustimmung erforderlich');
        updateComposerState(root, state);
        updateConsentGate(root, state);
        return;
      }

      state.thread_id = result.thread_id || state.thread_id;
      state.customer_key = result.customer_key || state.customer_key;
      state.consent_given = result.consent_given !== false;
      state.consent_timestamp = result.consent_timestamp || state.consent_timestamp;
      saveState(root, state);
      renderMessages(root, result.messages || [], result.links || []);
      setStatus(root, result.status_text || (result.requires_human ? 'Founder takeover aktiv' : 'AUTO_PILOT aktiv'));
      updateComposerState(root, state);
      updateConsentGate(root, state);
      if (prompt) {
        prompt.value = '';
      }
    } catch (_error) {
      setStatus(root, 'Fallback aktiv');
      renderMessages(root, [
        {
          sender_type: 'system',
          provider: 'system',
          message_text: 'Der Live-Vertriebsleiter ist gerade nicht direkt erreichbar. Nutze bitte vorübergehend den direkten Kontaktpfad, damit dein Anliegen nicht liegen bleibt.',
          metadata_json: JSON.stringify({
            links: [
              {
                label: 'Direkt zu Canberk',
                url: '/kontakt.html?intent=sales&entry=master-of-empire&topic=Fallback%20Rückfrage'
              }
            ]
          })
        }
      ]);
    } finally {
      if (state.consent_given) {
        submit.disabled = false;
      }
    }
  }

  function attachExamples(root) {
    root.querySelectorAll('[data-master-example]').forEach(function (button) {
      button.addEventListener('click', function () {
        const state = getState(root);
        if (!state.consent_given) {
          applyConsentState(root, state, { showPreConsentMessage: true });
          return;
        }
        const prompt = root.querySelector('[data-master-prompt]');
        if (!prompt) {
          return;
        }
        prompt.value = button.getAttribute('data-master-example') || '';
        prompt.focus();
      });
    });
  }

  function bootstrap(root) {
    if (root.dataset.masterBooted === 'true') {
      return;
    }
    root.dataset.masterBooted = 'true';
    const state = getState(root);
    saveState(root, state);
    ensureComplianceUi(root);
    attachConsentActions(root);
    attachExamples(root);

    const form = root.querySelector('[data-master-form]');
    if (form) {
      form.addEventListener('submit', function (event) {
        event.preventDefault();
        sendMessage(root);
      });
    }

    if (state.consent_given) {
      renderMessages(root, [greetingMessage(root)]);
      setStatus(root, root.dataset.masterInitialStatus || 'AUTO_PILOT aktiv');
    } else {
      renderMessages(root, [preConsentMessage()]);
      setStatus(root, state.consent_rejected ? 'Chat nicht gestartet' : 'Zustimmung erforderlich');
    }

    updateComposerState(root, state);
    updateConsentGate(root, state);
    updateDisclaimerVisibility(root, state);
    pollThread(root, getState(root));
    window.setInterval(function () {
      pollThread(root, getState(root));
    }, Number(root.dataset.masterPollInterval || POLL_INTERVAL_MS));
  }

  function bootstrapAll() {
    document.querySelectorAll('[data-master-chat-root]').forEach(bootstrap);
  }

  window.CanGoMasterEmpireChat = window.CanGoMasterEmpireChat || {};
  window.CanGoMasterEmpireChat.bootstrapAll = bootstrapAll;

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', bootstrapAll);
  } else {
    bootstrapAll();
  }
})();
