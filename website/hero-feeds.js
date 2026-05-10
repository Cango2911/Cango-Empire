/**
 * Hero-Bereich: Breaking News + Daily Blogs + Metrik-Animation
 * Wird auf allen Seiten mit gleichem Hero wie Startseite geladen.
 * Initialisiert nur, wenn #news-feed bzw. #blogs-feed vorhanden sind.
 */
(function() {
  var N8N_NEWS_WEBHOOK = 'https://n8n.automation-cango-app-empire.com/webhook/homepage-news';
  var FALLBACK_NEWS_JSON = '/data/homepage-news.json?v=20260313';
  var N8N_BLOGS_WEBHOOK = 'https://n8n.automation-cango-app-empire.com/webhook/website-blogs';
  var FALLBACK_BLOGS_JSON = '/data/homepage-blogs.json?v=20260313';
  var FEED_ROTATION_MS = 10000;
  var newsArticles = [], blogArticles = [];
  var currentNewsIndex = 0, currentBlogIndex = 0;
  var newsRotationInterval = null, blogRotationInterval = null;

  function formatDate(dateString) {
    try {
      var date = new Date(dateString);
      var now = new Date();
      var diff = now - date;
      var hours = Math.floor(diff / (1000 * 60 * 60));
      var minutes = Math.floor(diff / (1000 * 60));
      if (minutes < 1) return 'GERADE EBEN';
      if (minutes < 60) return 'VOR ' + minutes + ' MIN';
      if (hours < 24) return 'VOR ' + hours + ' STD';
      if (hours < 48) return 'GESTERN';
      return date.toLocaleDateString('de-DE', { day: '2-digit', month: 'short', year: 'numeric' }).toUpperCase().replace('.', '');
    } catch (e) {
      return 'HEUTE';
    }
  }

  function resolveFeedUrl(url) {
    if (!url || url === '#') return '#';
    if (/^https?:\/\//i.test(url)) return url;
    return url.startsWith('/') ? url : '/' + url;
  }

  function normalizeFeedIndex(index, length) {
    if (!length) return 0;
    return ((index % length) + length) % length;
  }

  function parseNewsPayload(data) {
    if (data.articles && Array.isArray(data.articles)) {
      return data.articles.map(function(item) {
        return {
          title: item.title || '',
          publisher: item.publisher || 'Google News',
          date: formatDate(item.date || item.scrapedAt || new Date()),
          url: item.url || '#',
          snippet: item.snippet || '',
          niche: item.niche || 'allgemein',
          nicheName: item.nicheName || 'Allgemein'
        };
      }).filter(function(item) { return item.title && item.title.length > 0; });
    }
    if (Array.isArray(data)) {
      return data.map(function(item) {
        return {
          title: item.title || '',
          publisher: item.publisher || 'Google News',
          date: formatDate(item.date || new Date()),
          url: item.url || '#',
          snippet: item.snippet || '',
          niche: item.niche || 'allgemein',
          nicheName: item.nicheName || 'Allgemein'
        };
      }).filter(function(item) { return item.title && item.title.length > 0; });
    }
    return [];
  }

  function parseBlogPayload(data) {
    if (data.articles && Array.isArray(data.articles)) {
      return data.articles.map(function(item) {
        return {
          title: item.title || '',
          excerpt: item.metaDescription || item.excerpt || (item.content ? item.content.substring(0, 120).replace(/<[^>]+>/g, '') : '') || '',
          date: formatDate(item.publishedAt || item.generatedAt || item.date || new Date()),
          url: item.url || item.slug || '#',
          category: item.nicheName || item.niche || 'Allgemein',
          keywords: item.secondaryKeywords || []
        };
      }).filter(function(item) { return item.title && item.title.length > 0; });
    }
    if (Array.isArray(data)) {
      return data.map(function(item) {
        return {
          title: item.title || '',
          excerpt: item.metaDescription || item.excerpt || '',
          date: formatDate(item.date || new Date()),
          url: item.url || '#',
          category: item.nicheName || 'Allgemein',
          keywords: []
        };
      }).filter(function(item) { return item.title && item.title.length > 0; });
    }
    return [];
  }

  function renderFeedDots(containerId, count, activeIndex, onSelect) {
    var dotsContainer = document.getElementById(containerId);
    if (!dotsContainer) return;
    dotsContainer.innerHTML = '';
    if (count <= 1) return;
    var prevBtn = document.createElement('button');
    prevBtn.type = 'button';
    prevBtn.className = 'hero__widget-dot';
    prevBtn.setAttribute('aria-label', 'Vorheriger Slide');
    prevBtn.textContent = '←';
    prevBtn.addEventListener('click', function() { onSelect(normalizeFeedIndex(activeIndex - 1, count)); });
    var nextBtn = document.createElement('button');
    nextBtn.type = 'button';
    nextBtn.className = 'hero__widget-dot hero__widget-dot--active';
    nextBtn.setAttribute('aria-label', 'Nächster Slide');
    nextBtn.textContent = '→';
    nextBtn.addEventListener('click', function() { onSelect(normalizeFeedIndex(activeIndex + 1, count)); });
    dotsContainer.appendChild(prevBtn);
    dotsContainer.appendChild(nextBtn);
  }

  function setupFeedSwipe(containerId, onPrev, onNext) {
    var container = document.getElementById(containerId);
    if (!container || container.dataset.swipeBound === 'true') return;
    container.dataset.swipeBound = 'true';
    var startX = 0, startY = 0, dragging = false;
    container.addEventListener('pointerdown', function(e) {
      if (e.pointerType === 'mouse' && e.button !== 0) return;
      startX = e.clientX; startY = e.clientY; dragging = true;
      container.classList.add('is-dragging');
    });
    container.addEventListener('pointerup', function(e) {
      if (!dragging) return;
      dragging = false;
      container.classList.remove('is-dragging');
      var dx = e.clientX - startX, dy = e.clientY - startY;
      if (Math.abs(dx) >= 40 && Math.abs(dx) >= Math.abs(dy)) { if (dx > 0) onPrev(); else onNext(); }
    });
    container.addEventListener('pointerleave', function(e) {
      if (dragging && e.pointerType === 'mouse') { dragging = false; container.classList.remove('is-dragging'); }
    });
  }

  function renderFeedSlide(containerId, itemClass, html, direction, onClickCode) {
    var container = document.getElementById(containerId);
    if (!container) return;
    direction = direction || 'next';
    var currentItem = container.querySelector('.hero__feed-card--active');
    var nextItem = document.createElement('div');
    nextItem.className = itemClass + ' hero__feed-card hero__feed-card--enter-' + direction;
    if (onClickCode) nextItem.setAttribute('onclick', onClickCode);
    nextItem.innerHTML = html;
    container.appendChild(nextItem);
    requestAnimationFrame(function() {
      nextItem.classList.add('hero__feed-card--active');
      nextItem.classList.remove('hero__feed-card--enter-' + direction);
    });
    if (currentItem) {
      currentItem.classList.remove('hero__feed-card--active');
      currentItem.classList.add('hero__feed-card--leaving-' + direction);
      setTimeout(function() { currentItem.remove(); }, 560);
    }
  }

  function displayNewsItem(index, direction) {
    var newsContainer = document.getElementById('news-feed');
    if (!newsContainer || newsArticles.length === 0) return;
    currentNewsIndex = normalizeFeedIndex(index, newsArticles.length);
    var article = newsArticles[currentNewsIndex];
    var clickHandler = article.url && article.url !== '#' ? "window.location.href='" + resolveFeedUrl(article.url) + "'" : '';
    var snippet = article.snippet ? '<div class="hero__news-snippet">' + article.snippet + '</div>' : '';
    renderFeedSlide('news-feed', 'hero__news-item',
      '<div class="hero__news-text">' + article.title + '</div>' + snippet +
      (article.url && article.url !== '#' ? '<span class="hero__news-mini-button">Artikel öffnen</span>' : ''),
      direction, clickHandler);
    renderFeedDots('news-feed-dots', newsArticles.length, currentNewsIndex, function(targetIndex) {
      if (targetIndex !== currentNewsIndex) {
        displayNewsItem(targetIndex, targetIndex > currentNewsIndex ? 'next' : 'prev');
        restartNewsRotation();
      }
    });
  }

  function restartNewsRotation() {
    if (newsRotationInterval) clearInterval(newsRotationInterval);
    if (newsArticles.length <= 1) return;
    newsRotationInterval = setInterval(function() { displayNewsItem(currentNewsIndex + 1, 'next'); }, FEED_ROTATION_MS);
  }

  function startNewsRotation() {
    if (newsArticles.length === 0) return;
    displayNewsItem(currentNewsIndex, 'next');
    restartNewsRotation();
    setupFeedSwipe('news-feed', function() { displayNewsItem(currentNewsIndex - 1, 'prev'); restartNewsRotation(); }, function() { displayNewsItem(currentNewsIndex + 1, 'next'); restartNewsRotation(); });
  }

  function displayBlogItem(index, direction) {
    var blogsContainer = document.getElementById('blogs-feed');
    if (!blogsContainer || blogArticles.length === 0) return;
    currentBlogIndex = normalizeFeedIndex(index, blogArticles.length);
    var blog = blogArticles[currentBlogIndex];
    var excerpt = blog.excerpt ? '<div class="hero__blogs-excerpt">' + blog.excerpt + '</div>' : '';
    var clickHandler = blog.url && blog.url !== '#' ? "window.location.href='" + resolveFeedUrl(blog.url) + "'" : '';
    renderFeedSlide('blogs-feed', 'hero__blogs-item',
      '<div class="hero__blogs-text">' + blog.title + '</div>' + excerpt +
      (blog.url && blog.url !== '#' ? '<span class="hero__blogs-mini-button">Artikel öffnen</span>' : ''),
      direction, clickHandler);
    renderFeedDots('blogs-feed-dots', blogArticles.length, currentBlogIndex, function(targetIndex) {
      if (targetIndex !== currentBlogIndex) {
        displayBlogItem(targetIndex, targetIndex > currentBlogIndex ? 'next' : 'prev');
        restartBlogRotation();
      }
    });
  }

  function restartBlogRotation() {
    if (blogRotationInterval) clearInterval(blogRotationInterval);
    if (blogArticles.length <= 1) return;
    blogRotationInterval = setInterval(function() { displayBlogItem(currentBlogIndex + 1, 'next'); }, FEED_ROTATION_MS);
  }

  function displayBlogs() {
    if (blogArticles.length === 0) return;
    displayBlogItem(currentBlogIndex, 'next');
    restartBlogRotation();
    setupFeedSwipe('blogs-feed', function() { displayBlogItem(currentBlogIndex - 1, 'prev'); restartBlogRotation(); }, function() { displayBlogItem(currentBlogIndex + 1, 'next'); restartBlogRotation(); });
  }

  function fetchGoogleNews() {
    var demoNews = [{ title: 'News werden geladen...', publisher: 'CanGo App Empire', date: 'Heute', url: '#', snippet: 'Die neuesten Artikel werden vom n8n Workflow geladen.', niche: 'allgemein', nicheName: 'Allgemein' }];
    fetch(N8N_NEWS_WEBHOOK, { method: 'GET', headers: { 'Accept': 'application/json' }, cache: 'no-cache' })
      .then(function(r) { return r.ok ? r.json() : null; })
      .catch(function() { return null; })
      .then(function(data) {
        if (!data) return fetch(FALLBACK_NEWS_JSON, { method: 'GET', headers: { 'Accept': 'application/json' }, cache: 'no-cache' }).then(function(r) { return r.ok ? r.json() : null; }).catch(function() { return null; });
        return data;
      })
      .then(function(data) {
        newsArticles = data ? parseNewsPayload(data) : [];
        if (newsArticles.length === 0) newsArticles = demoNews;
        startNewsRotation();
      })
      .catch(function() {
        newsArticles = demoNews;
        startNewsRotation();
      });
  }

  function fetchDailyBlogs() {
    var demoBlogs = [{ title: 'Daily Blogs werden geladen...', excerpt: 'Die neuesten SEO-optimierten Artikel werden täglich generiert.', date: 'Heute', url: '#', category: 'Allgemein', keywords: [] }];
    fetch(N8N_BLOGS_WEBHOOK, { method: 'GET', headers: { 'Accept': 'application/json' }, cache: 'no-cache' })
      .then(function(r) { return r.ok ? r.json() : null; })
      .catch(function() { return null; })
      .then(function(data) {
        if (!data) return fetch(FALLBACK_BLOGS_JSON, { method: 'GET', headers: { 'Accept': 'application/json' }, cache: 'no-cache' }).then(function(r) { return r.ok ? r.json() : null; }).catch(function() { return null; });
        return data;
      })
      .then(function(data) {
        blogArticles = data ? parseBlogPayload(data) : [];
        if (blogArticles.length === 0) blogArticles = demoBlogs;
        displayBlogs();
      })
      .catch(function() {
        blogArticles = demoBlogs;
        displayBlogs();
      });
  }

  function animateCounter(el) {
    var target = parseInt(el.getAttribute('data-count'), 10);
    var duration = parseInt(el.getAttribute('data-duration'), 10) || 2000;
    var current = 0;
    var increment = target / (duration / 16);
    var timer = setInterval(function() {
      current += increment;
      if (current >= target) { current = target; clearInterval(timer); }
      el.textContent = Math.floor(current);
    }, 16);
  }

  function initHeroFeeds() {
    if (document.getElementById('news-feed')) {
      fetchGoogleNews();
      setInterval(fetchGoogleNews, 5 * 60 * 1000);
    }
    if (document.getElementById('blogs-feed')) {
      fetchDailyBlogs();
      setInterval(fetchDailyBlogs, 10 * 60 * 1000);
    }
    document.querySelectorAll('.metric').forEach(function(metric) {
      var counter = metric.querySelector('.metric__icon-value[data-count]');
      if (counter && !counter.classList.contains('animated')) {
        var observer = new IntersectionObserver(function(entries) {
          entries.forEach(function(entry) {
            if (entry.isIntersecting) {
              counter.classList.add('animated');
              animateCounter(counter);
              observer.disconnect();
            }
          });
        }, { threshold: 0.5 });
        observer.observe(metric);
      }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initHeroFeeds);
  } else {
    initHeroFeeds();
  }
})();
