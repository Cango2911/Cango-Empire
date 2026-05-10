(function () {
  function closeOthers(current) {
    document.querySelectorAll("[data-nav-dropdown].is-open").forEach(function (w) {
      if (w !== current) {
        w.classList.remove("is-open");
        var b = w.querySelector(".nav__dropdown-toggle");
        if (b) b.setAttribute("aria-expanded", "false");
      }
    });
  }

  function bindWrap(wrap) {
    var btn = wrap.querySelector(".nav__dropdown-toggle");
    var panel = wrap.querySelector(".nav__dropdown-panel");
    if (!btn || !panel || wrap.dataset.navDropdownBound) return;
    wrap.dataset.navDropdownBound = "1";

    btn.addEventListener("click", function (e) {
      if (window.matchMedia("(hover: hover) and (pointer: fine)").matches) {
        return;
      }
      e.preventDefault();
      e.stopPropagation();
      var open = !wrap.classList.contains("is-open");
      closeOthers(wrap);
      wrap.classList.toggle("is-open", open);
      btn.setAttribute("aria-expanded", open ? "true" : "false");
    });

    panel.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () {
        wrap.classList.remove("is-open");
        btn.setAttribute("aria-expanded", "false");
      });
    });
  }

  document.addEventListener("click", function (e) {
    if (window.matchMedia("(hover: hover) and (pointer: fine)").matches) return;
    document.querySelectorAll("[data-nav-dropdown].is-open").forEach(function (wrap) {
      if (!wrap.contains(e.target)) {
        wrap.classList.remove("is-open");
        var b = wrap.querySelector(".nav__dropdown-toggle");
        if (b) b.setAttribute("aria-expanded", "false");
      }
    });
  });

  document.addEventListener("keydown", function (e) {
    if (e.key !== "Escape") return;
    document.querySelectorAll("[data-nav-dropdown].is-open").forEach(function (wrap) {
      wrap.classList.remove("is-open");
      var b = wrap.querySelector(".nav__dropdown-toggle");
      if (b) b.setAttribute("aria-expanded", "false");
    });
  });

  function init() {
    document.querySelectorAll("[data-nav-dropdown]").forEach(bindWrap);
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
