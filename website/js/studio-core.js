/**
 * CanGo Short-Form Studio — Kernlogik (Segmentierung, Hook-Score, Tags)
 * Heuristik orientiert am internen Playbook (Frage, Zahl, Trigger, Kontrast).
 */
(function (global) {
  "use strict";

  var TRIGGERS = [
    "du ", "dein ", "deine ", "dir ", "niemals", "nie ", "fakt", "wahrheit",
    "warum ", "geheim", "fehler", "jetzt", "heute", "morgen", "konkurrenz",
    "kostenlos", "zerstör", "panik", "angst", "beweis", "beweise", "stop",
    "hör auf", "vergiss", "2026", "2025", "milli", "leer", "niemand"
  ];

  function splitScript(text) {
    if (!text || !String(text).trim()) return [];
    var t = String(text).trim();
    var blocks = t.split(/\n\s*---\s*\n/g);
    if (blocks.length === 1) {
      blocks = t.split(/\n{2,}/);
    }
    return blocks
      .map(function (s) { return s.trim(); })
      .filter(Boolean);
  }

  function scoreHook(text) {
    if (!text || !String(text).trim()) return 0;
    var s = 15; // lower baseline — differentiation matters
    var low = text.toLowerCase();
    var first = (text.split(/[.!?]/)[0] || text).trim();
    if (/\?/.test(text))                                                   s += 20; // question = stop + think
    if (/\d/.test(text))                                                   s += 14; // number = credibility
    if (/!/.test(text))                                                    s +=  8; // exclamation = energy
    if (text.length <= 120)                                                s +=  6; // short = hard hook
    if (text.length > 400)                                                 s -=  8; // too long = retention drop
    if (/\b(vs|gegen|nicht|stattdessen|aber|nein|stopp)\b/i.test(text))   s += 10; // contrast
    if (/^(mach|schau|h[oö]r|starte|wähle|hol|nimm|zeig)/i.test(first))  s += 10; // imperative opener
    if (first.split(/\s+/).length <= 8)                                    s += 12; // ultra-short first line
    for (var i = 0; i < TRIGGERS.length; i++) {
      if (low.indexOf(TRIGGERS[i]) !== -1) s += 5;
    }
    // Weak opener penalty
    if (/^(so |und |aber |hier |wenn )/i.test(text))                      s -=  5;
    return Math.max(0, Math.min(100, Math.round(s)));
  }

  function reasonFor(text, score) {
    var parts = [];
    if (/\?/.test(text)) parts.push("Frage = Stop & Denken");
    if (/\d/.test(text)) parts.push("Zahlen = Glaubwürdigkeit");
    if (score >= 75) parts.push("Starker Opener / Kontrast");
    if (text.length < 100) parts.push("Kurz = harter Hook");
    if (!parts.length) parts.push("Solider Aufhänger — mit Schnitt noch schärfbar");
    return parts.slice(0, 2).join(" · ");
  }

  function tagFor(text, score) {
    var low = text.toLowerCase();
    if (/\?|!/.test(text) && score >= 70) return "Aufreger";
    if (/\d|%|€|\$|x\b|mal\b/i.test(text)) return "Beweis";
    if (/jetzt|heute|morgen|letzte chance|verpasst|zu spät/i.test(low)) return "FOMO";
    return "Mensch";
  }

  /** Estimate clip duration in seconds (2.5 words/sec average German speech) */
  function estimateDuration(text) {
    var words = String(text).trim().split(/\s+/).length;
    return Math.max(5, Math.min(90, Math.round(words / 2.5)));
  }

  /** Build a simple cumulative timeline for SRT export */
  function buildTimeline(clips) {
    var cursor = 0;
    return clips.map(function (c) {
      var start = cursor;
      var dur = c.durationSec || estimateDuration(c.body);
      cursor += dur + 0.5; // 0.5s gap between clips
      return { startSec: start, endSec: start + dur };
    });
  }

  function buildClips(scriptText) {
    var segs = splitScript(scriptText);
    var ts = Date.now();
    var clips = segs.map(function (body, i) {
      var title = body.split(/[.!?\n]/)[0].trim().slice(0, 72) || "Clip " + (i + 1);
      var hook = scoreHook(body);
      var dur = estimateDuration(body);
      return {
        id: "clip-" + i + "-" + ts,
        title: title,
        body: body,
        hookScore: hook,
        reason: reasonFor(body, hook),
        tag: tagFor(body, hook),
        durationSec: dur,
      };
    });
    // Attach timeline
    var timeline = buildTimeline(clips);
    clips.forEach(function (c, i) {
      c.startSec = timeline[i].startSec;
      c.endSec   = timeline[i].endSec;
    });
    return clips;
  }

  global.CanGoStudioCore = {
    splitScript: splitScript,
    scoreHook: scoreHook,
    reasonFor: reasonFor,
    tagFor: tagFor,
    buildClips: buildClips,
  };
})(typeof window !== "undefined" ? window : globalThis);
