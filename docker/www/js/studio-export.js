/**
 * Export: Skript/Manifest als .txt — Video (ffmpeg.wasm) später andockbar
 */
(function (global) {
  "use strict";

  function downloadText(filename, content, mime) {
    var blob = new Blob([content], {
      type: mime || "text/plain;charset=utf-8",
    });
    var url = URL.createObjectURL(blob);
    var a = document.createElement("a");
    a.href = url;
    a.download = filename || "export.txt";
    a.rel = "noopener";
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  }

  /** Format seconds → SRT timestamp HH:MM:SS,mmm */
  function toSRTTime(sec) {
    var ms  = Math.round((sec % 1) * 1000);
    var s   = Math.floor(sec) % 60;
    var m   = Math.floor(sec / 60) % 60;
    var h   = Math.floor(sec / 3600);
    function p(n, len) { return String(n).padStart(len || 2, "0"); }
    return p(h) + ":" + p(m) + ":" + p(s) + "," + p(ms, 3);
  }

  /** Build SRT subtitle file from clips (phrase-level, 5 words per frame) */
  function buildSRT(clips) {
    var lines = [];
    var idx   = 1;
    var WPF   = 5; // words per subtitle frame
    var WPS   = 2.5; // words per second (German speech estimate)
    clips.forEach(function (c) {
      var words   = String(c.body || "").trim().split(/\s+/).filter(Boolean);
      var startSec = c.startSec || 0;
      var frameDur = WPF / WPS;
      var cursor   = startSec;
      for (var i = 0; i < words.length; i += WPF) {
        var phrase  = words.slice(i, i + WPF).join(" ");
        var endSec  = Math.min(cursor + frameDur, c.endSec || cursor + frameDur);
        lines.push(String(idx));
        lines.push(toSRTTime(cursor) + " --> " + toSRTTime(endSec));
        lines.push(phrase);
        lines.push("");
        idx++;
        cursor = endSec;
      }
    });
    return lines.join("\n");
  }

  /** Build full project JSON (clips + meta + preset) */
  function buildJSON(clips, meta) {
    var project = {
      meta: {
        generator: "CanGo Short-Form AI Studio",
        created: (meta && meta.date) ? meta.date : new Date().toISOString(),
        video: (meta && meta.video) ? meta.video : null,
        preset: (meta && meta.preset) ? meta.preset : null,
        format: "9:16 · 1080×1920",
      },
      clips: clips.map(function (c) {
        return {
          id:          c.id,
          title:       c.title,
          body:        c.body,
          hookScore:   c.hookScore,
          tag:         c.tag,
          reason:      c.reason,
          durationSec: c.durationSec,
          startSec:    c.startSec,
          endSec:      c.endSec,
        };
      }),
    };
    return JSON.stringify(project, null, 2);
  }

  function buildTxtManifest(clips, meta) {
    var lines = [];
    lines.push("# CanGo Short-Form Export");
    lines.push("# " + (meta && meta.date ? meta.date : new Date().toISOString()));
    lines.push("");
    clips.forEach(function (c, i) {
      lines.push("--- Clip " + (i + 1) + " ---");
      lines.push("Titel: " + (c.title || ""));
      lines.push("Hook-Score: " + (c.hookScore != null ? c.hookScore : ""));
      lines.push("Tag: " + (c.tag || ""));
      lines.push("Grund: " + (c.reason || ""));
      lines.push("");
      lines.push(c.body || "");
      lines.push("");
    });
    return lines.join("\n");
  }

  global.CanGoStudioExport = {
    downloadText: downloadText,
    buildTxtManifest: buildTxtManifest,
    buildSRT: buildSRT,
    buildJSON: buildJSON,
    toSRTTime: toSRTTime,
  };
})(typeof window !== "undefined" ? window : globalThis);
