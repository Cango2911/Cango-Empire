/**
 * CanGo Marktplatz – Tool-Erklärvideos (YouTube-Embed)
 * Einbettung über den von Google bereitgestellten Player (youtube-nocookie);
 * Nutzung der Einbettungsfunktion gemäß geltender YouTube-Nutzungsbedingungen.
 */
(function () {
  function loadVideo(placeholder, videoId) {
    if (!videoId) return;
    var wrapper = placeholder.parentElement;
    if (!wrapper) return;
    var id = String(videoId).trim();
    var q =
      "autoplay=1&rel=0&hl=de&cc_load_policy=1&cc_lang_pref=de&modestbranding=1";
    var src =
      "https://www.youtube-nocookie.com/embed/" +
      encodeURIComponent(id) +
      "?" +
      q;
    wrapper.innerHTML =
      '<iframe src="' +
      src +
      '" title="YouTube-Video" loading="eager" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen referrerpolicy="strict-origin-when-cross-origin"></iframe>';
  }

  window.loadVideo = loadVideo;

  function addEmbedNotes() {
    document.querySelectorAll(".video-external-links").forEach(function (el) {
      if (el.querySelector(".video-embed-note")) return;
      el.appendChild(document.createElement("br"));
      var s = document.createElement("small");
      s.className = "video-embed-note";
      s.setAttribute("role", "note");
      s.textContent =
        "Hinweis: Wiedergabe über den von YouTube bereitgestellten eingebetteten Player (Nutzung gemäß YouTube-AGB). Videoinhalt und Marken liegen beim jeweiligen Anbieter; keine eigene Weiterverwendung des Videomaterials.";
      el.appendChild(s);
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", addEmbedNotes);
  } else {
    addEmbedNotes();
  }
})();
