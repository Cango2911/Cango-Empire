/**
 * Caption-Preview auf Canvas (9:16), Brand-Presets CanGo Empire
 */
(function (global) {
  "use strict";

  var PRESETS = {
    cangoBold: {
      name: "CanGo Bold",
      bg: "rgba(3, 7, 18, 0.82)",
      color: "#F9FAFB",
      accent: "#F97316",
      fontTitle: "600 42px Instrument Sans, system-ui, sans-serif",
      fontSub: "400 28px Instrument Sans, system-ui, sans-serif",
      align: "center",
      padY: 0.78,
    },
    empireYellow: {
      name: "Empire Yellow",
      bg: "rgba(17, 24, 39, 0.88)",
      color: "#FDE68A",
      accent: "#F97316",
      fontTitle: "700 40px Instrument Sans, system-ui, sans-serif",
      fontSub: "500 26px Instrument Sans, system-ui, sans-serif",
      align: "center",
      padY: 0.76,
    },
    breakingNews: {
      name: "Breaking News",
      bg: "rgba(185, 28, 28, 0.92)",
      color: "#FFFFFF",
      accent: "#FDE047",
      fontTitle: "800 38px Instrument Sans, system-ui, sans-serif",
      fontSub: "600 24px Instrument Sans, system-ui, sans-serif",
      align: "center",
      padY: 0.74,
    },
    cleanWhite: {
      name: "Clean White",
      bg: "rgba(255,255,255,0.14)",
      color: "#FFFFFF",
      accent: "#F97316",
      fontTitle: "600 36px Instrument Sans, system-ui, sans-serif",
      fontSub: "400 24px Instrument Sans, system-ui, sans-serif",
      align: "center",
      padY: 0.78,
    },
  };

  /** Interne Auflösung halb-HD für Performance; Darstellung per CSS skaliert */
  function setupCanvas(canvas, logicalW, logicalH) {
    var w = logicalW || 540;
    var h = logicalH || 960;
    var dpr = Math.min(global.devicePixelRatio || 1, 2);
    canvas.width = Math.floor(w * dpr);
    canvas.height = Math.floor(h * dpr);
    canvas.style.width = w + "px";
    canvas.style.height = h + "px";
    var ctx = canvas.getContext("2d");
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    return { ctx: ctx, w: w, h: h };
  }

  function drawSafeZones(ctx, w, h) {
    ctx.save();
    ctx.strokeStyle = "rgba(239, 68, 68, 0.45)";
    ctx.lineWidth = 2;
    ctx.setLineDash([6, 6]);
    var topH = h * 0.15;
    var botH = h * 0.2;
    ctx.strokeRect(4, 4, w - 8, topH - 4);
    ctx.strokeRect(4, h - botH, w - 8, botH - 4);
    ctx.restore();
  }

  function wrapLines(ctx, text, maxW) {
    var words = String(text).split(/\s+/);
    var lines = [];
    var line = "";
    for (var i = 0; i < words.length; i++) {
      var test = line ? line + " " + words[i] : words[i];
      if (ctx.measureText(test).width > maxW && line) {
        lines.push(line);
        line = words[i];
      } else {
        line = test;
      }
    }
    if (line) lines.push(line);
    return lines.slice(0, 5);
  }

  function drawPreview(canvas, text, presetKey, options) {
    var preset = PRESETS[presetKey] || PRESETS.cangoBold;
    var o = options || {};
    var showZones = o.safeZones !== false;

    var x = setupCanvas(canvas, 540, 960);
    var ctx = x.ctx;
    var w = x.w;
    var h = x.h;

    var grd = ctx.createLinearGradient(0, 0, 0, h);
    grd.addColorStop(0, "#111827");
    grd.addColorStop(1, "#030712");
    ctx.fillStyle = grd;
    ctx.fillRect(0, 0, w, h);

    if (showZones) drawSafeZones(ctx, w, h);

    var headline = String(text || "").split(/\n/)[0].slice(0, 140);
    ctx.font = preset.fontTitle;
    var lines = wrapLines(ctx, headline, w - 80);
    ctx.fillStyle = preset.color;
    ctx.textAlign = "center";
    var cy = h * preset.padY;
    for (var i = 0; i < lines.length; i++) {
      ctx.fillText(lines[i], w / 2, cy + i * 48);
    }

    ctx.font = preset.fontSub;
    ctx.fillStyle = preset.accent;
    ctx.fillText("CanGo · Short-Form", w / 2, h - 120);

    return PRESETS[presetKey];
  }

  global.CanGoStudioCaptions = {
    PRESETS: PRESETS,
    drawPreview: drawPreview,
    setupCanvas: setupCanvas,
  };
})(typeof window !== "undefined" ? window : globalThis);
