// ─── Ultrametric Quantum Computation — main.js ───
(function(){
  'use strict';

  // ── Theme ──────────────────────────────────────
  function initTheme() {
    var saved = localStorage.getItem('theme');
    var prefers = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    var theme = saved || prefers;
    document.documentElement.setAttribute('data-theme', theme);
    updateThemeIcons(theme);
  }

  function toggleTheme() {
    var current = document.documentElement.getAttribute('data-theme');
    var next = current === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('theme', next);
    updateThemeIcons(next);
  }

  function updateThemeIcons(theme) {
    var mb = document.getElementById('theme-toggle-mobile');
    if (mb) mb.textContent = theme === 'dark' ? '🌙' : '☀️';
  }

  // ── Sidebar Navigation ────────────────────────
  function buildSidebarNav(data) {
    var nav = document.getElementById('sidebar-nav');
    if (!nav || !data) return;
    nav.innerHTML = '';
    data.forEach(function(item) {
      var div = document.createElement('div');
      div.className = 'nav-item nav-h2';
      var a = document.createElement('a');
      a.href = '#' + item.id;
      a.textContent = item.title;
      div.appendChild(a);
      nav.appendChild(div);

      if (item.children) {
        item.children.forEach(function(child) {
          var childDiv = document.createElement('div');
          childDiv.className = 'nav-item nav-h3';
          var childA = document.createElement('a');
          childA.href = '#' + child.id;
          childA.textContent = child.title;
          childDiv.appendChild(childA);
          nav.appendChild(childDiv);
        });
      }
    });
  }

  // ── Active Heading (IntersectionObserver) ──────
  function initActiveHeading() {
    var headings = document.querySelectorAll('h2[id], h3[id]');
    if (!headings.length) return;

    var observer = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          // Update sidebar
          document.querySelectorAll('.nav-item.active').forEach(function(el) { el.classList.remove('active'); });
          var navItem = document.querySelector('.nav-item a[href="#' + entry.target.id + '"]');
          if (navItem) navItem.parentElement.classList.add('active');
          // Update in-page TOC
          document.querySelectorAll('.toc-list a.active').forEach(function(el) { el.classList.remove('active'); });
          var tocItem = document.querySelector('.toc-list a[href="#' + entry.target.id + '"]');
          if (tocItem) tocItem.classList.add('active');
        }
      });
    }, { rootMargin: '-80px 0px -70% 0px', threshold: 0 });

    headings.forEach(function(h) { observer.observe(h); });
  }

  // ── Progress Bar ──────────────────────────────
  function initProgressBar() {
    var bar = document.getElementById('progress-bar');
    if (!bar) return;
    var ticking = false;
    window.addEventListener('scroll', function() {
      if (!ticking) {
        requestAnimationFrame(function() {
          var scrollTop = window.scrollY;
          var docHeight = document.documentElement.scrollHeight - window.innerHeight;
          var pct = docHeight > 0 ? Math.min((scrollTop / docHeight) * 100, 100) : 0;
          bar.style.width = pct + '%';
          ticking = false;
        });
        ticking = true;
      }
    });
  }

  // ── Mobile Menu ────────────────────────────────
  function initMobileMenu() {
    var toggle = document.getElementById('menu-toggle');
    var sidebar = document.getElementById('sidebar');
    var overlay = document.getElementById('sidebar-overlay');
    if (!toggle || !sidebar || !overlay) return;

    toggle.addEventListener('click', function() {
      var open = sidebar.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open);
      overlay.classList.toggle('visible', open);
    });

    overlay.addEventListener('click', function() {
      sidebar.classList.remove('open');
      overlay.classList.remove('visible');
      toggle.setAttribute('aria-expanded', 'false');
    });

    // Close on nav link click (mobile)
    sidebar.addEventListener('click', function(e) {
      if (e.target.tagName === 'A' && window.innerWidth < 1025) {
        sidebar.classList.remove('open');
        overlay.classList.remove('visible');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });
  }

  // ── Floating Action Button ─────────────────────
  function initFab() {
    var fab = document.getElementById('fab');
    if (!fab) return;
    var pressTimer;

    // Show/hide
    window.addEventListener('scroll', function() {
      if (window.scrollY > 400) {
        fab.classList.add('visible');
      } else {
        fab.classList.remove('visible');
      }
    });

    // Short click → scroll to top
    fab.addEventListener('click', function() {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    // Long press → toggle theme
    fab.addEventListener('mousedown', function() {
      pressTimer = setTimeout(function() { toggleTheme(); }, 600);
    });
    fab.addEventListener('touchstart', function(e) {
      pressTimer = setTimeout(function() { toggleTheme(); }, 600);
    });
    fab.addEventListener('mouseup', function() { clearTimeout(pressTimer); });
    fab.addEventListener('touchend', function() { clearTimeout(pressTimer); });
    fab.addEventListener('mouseleave', function() { clearTimeout(pressTimer); });
  }

  // ── Smooth Scrolling ──────────────────────────
  function initSmoothScroll() {
    document.addEventListener('click', function(e) {
      var link = e.target.closest('a[href^="#"]');
      if (!link) return;
      var target = document.querySelector(link.getAttribute('href'));
      if (!target) return;
      e.preventDefault();
      var top = target.getBoundingClientRect().top + window.scrollY - 80;
      window.scrollTo({ top: top, behavior: 'smooth' });
      history.pushState(null, '', link.getAttribute('href'));
      // Fragment highlight
      target.classList.add('highlight-target');
      setTimeout(function() { target.classList.remove('highlight-target'); }, 2000);
    });
  }

  // ── Copy Buttons ──────────────────────────────
  function initCopyButtons() {
    document.querySelectorAll('pre code').forEach(function(code) {
      var pre = code.parentElement;
      var wrapper = document.createElement('div');
      wrapper.className = 'code-block-wrapper';
      pre.parentNode.insertBefore(wrapper, pre);
      wrapper.appendChild(pre);

      var btn = document.createElement('button');
      btn.className = 'copy-btn';
      btn.textContent = 'Copy';
      btn.setAttribute('aria-label', 'Copy code to clipboard');
      wrapper.appendChild(btn);

      btn.addEventListener('click', function() {
        var text = code.textContent;
        navigator.clipboard.writeText(text).then(function() {
          btn.textContent = '✓ Copied!';
          btn.classList.add('copied');
          setTimeout(function() {
            btn.textContent = 'Copy';
            btn.classList.remove('copied');
          }, 2000);
        }).catch(function() {
          // Fallback
          var ta = document.createElement('textarea');
          ta.value = text;
          ta.style.position = 'fixed';
          ta.style.opacity = '0';
          document.body.appendChild(ta);
          ta.select();
          document.execCommand('copy');
          document.body.removeChild(ta);
          btn.textContent = '✓ Copied!';
          btn.classList.add('copied');
          setTimeout(function() {
            btn.textContent = 'Copy';
            btn.classList.remove('copied');
          }, 2000);
        });
      });
    });
  }

  // ── Reading Time ───────────────────────────────
  function initReadingTime() {
    var el = document.querySelector('[data-reading-time] .reading-time-text');
    if (!el) return;
    var text = document.querySelector('.chapter-body') || document.querySelector('.main-content');
    if (!text) return;
    var words = text.textContent.trim().split(/\s+/).length;
    var minutes = Math.max(1, Math.round(words / 200));
    el.textContent = '~' + minutes + ' min read';
  }

  // ── Section Anchors ────────────────────────────
  function initSectionAnchors() {
    document.querySelectorAll('h2[id], h3[id]').forEach(function(h) {
      var a = document.createElement('a');
      a.className = 'heading-anchor';
      a.href = '#' + h.id;
      a.textContent = '#';
      a.setAttribute('aria-label', 'Link to this section');
      a.addEventListener('click', function(e) {
        e.preventDefault();
        navigator.clipboard.writeText(window.location.origin + window.location.pathname + '#' + h.id).then(function() {
          a.textContent = '✓';
          setTimeout(function() { a.textContent = '#'; }, 1500);
        });
      });
      h.appendChild(a);
    });
  }

  // ── In-Page TOC ────────────────────────────────
  function initInPageTOC() {
    var tocList = document.getElementById('toc-list');
    if (!tocList) return;
    var headings = document.querySelectorAll('.main-content h2[id], .main-content h3[id]');
    headings.forEach(function(h) {
      var a = document.createElement('a');
      a.href = '#' + h.id;
      a.textContent = h.textContent.replace(/\s*#\s*$/, '').replace(/\s*✓\s*$/, '');
      a.className = h.tagName === 'H2' ? 'toc-h2' : 'toc-h3';
      tocList.appendChild(a);
    });
  }

  // ── Proof Blocks ───────────────────────────────
  function initProofBlocks() {
    document.querySelectorAll('p, div').forEach(function(el) {
      if (el.textContent.trim().startsWith('*Proof.*') ||
          el.textContent.trim().startsWith('**Proof:**') ||
          el.textContent.trim().startsWith('**Proof.**')) {
        var wrapper = document.createElement('div');
        wrapper.className = 'proof-block';
        var header = document.createElement('div');
        header.className = 'proof-header';
        header.innerHTML = '<span>📐 Proof</span><span class="proof-toggle">▼</span>';
        var body = document.createElement('div');
        body.className = 'proof-body';

        var next = el.nextElementSibling;
        body.appendChild(el.cloneNode(true));
        while (next && !next.textContent.trim().match(/^(∎|□|QED|■|#|##)/)) {
          body.appendChild(next.cloneNode(true));
          var temp = next.nextElementSibling;
          next.remove();
          next = temp;
        }
        el.replaceWith(wrapper);
        wrapper.appendChild(header);
        wrapper.appendChild(body);

        header.addEventListener('click', function() {
          wrapper.classList.toggle('collapsed');
          header.querySelector('.proof-toggle').textContent = wrapper.classList.contains('collapsed') ? '▶' : '▼';
        });
      }
    });
  }

  // ── Diagram Zoom ───────────────────────────────
  function initDiagramZoom() {
    document.querySelectorAll('pre.diagram, .diagram pre').forEach(function(pre) {
      pre.addEventListener('click', function() {
        pre.classList.toggle('zoomed');
      });
    });
  }

  // ── Equation Modals ────────────────────────────
  function initEquationModals() {
    document.querySelectorAll('.MathJax_Display, mjx-container[display="true"]').forEach(function(el) {
      el.style.cursor = 'pointer';
      el.addEventListener('click', function() {
        var modal = document.createElement('div');
        modal.className = 'equation-modal open';
        var content = document.createElement('div');
        content.className = 'equation-modal-content';
        var close = document.createElement('button');
        close.className = 'equation-modal-close';
        close.textContent = '✕';
        close.setAttribute('aria-label', 'Close');
        content.appendChild(el.cloneNode(true));
        content.appendChild(close);
        modal.appendChild(content);
        document.body.appendChild(modal);

        function closeModal() {
          document.body.removeChild(modal);
        }
        close.addEventListener('click', closeModal);
        modal.addEventListener('click', function(e) { if (e.target === modal) closeModal(); });
        document.addEventListener('keydown', function escHandler(e) { if (e.key === 'Escape') { closeModal(); document.removeEventListener('keydown', escHandler); } });
      });
    });
  }

  // ── Image Lightbox ─────────────────────────────
  function initImageLightbox() {
    document.querySelectorAll('.main-content img').forEach(function(img) {
      if (img.closest('.lightbox') || img.closest('.equation-modal')) return;
      img.style.cursor = 'zoom-in';
      img.addEventListener('click', function() {
        var lb = document.createElement('div');
        lb.className = 'lightbox open';
        var lbImg = document.createElement('img');
        lbImg.className = 'lightbox-content';
        lbImg.src = img.src;
        lbImg.alt = img.alt;
        var close = document.createElement('button');
        close.className = 'lightbox-close';
        close.textContent = '✕';
        close.setAttribute('aria-label', 'Close');
        lb.appendChild(lbImg);
        lb.appendChild(close);
        document.body.appendChild(lb);

        function closeLb() { document.body.removeChild(lb); }
        close.addEventListener('click', closeLb);
        lb.addEventListener('click', function(e) { if (e.target === lb) closeLb(); });
        document.addEventListener('keydown', function escHandler(e) { if (e.key === 'Escape') { closeLb(); document.removeEventListener('keydown', escHandler); } });
      });
    });
  }

  // ── Footnote Popovers ──────────────────────────
  function initFootnotePopovers() {
    document.querySelectorAll('a[href^="#fn"]').forEach(function(link) {
      link.addEventListener('click', function(e) {
        var target = document.querySelector(link.getAttribute('href'));
        if (!target) return;
        e.preventDefault();
        var existing = document.querySelector('.footnote-popover');
        if (existing) { existing.remove(); return; }
        var popover = document.createElement('div');
        popover.className = 'footnote-popover';
        popover.style.cssText = 'position:absolute;background:var(--color-bg);border:1px solid var(--color-border);border-radius:8px;padding:12px 16px;max-width:320px;box-shadow:var(--shadow-elevated);z-index:500;font-size:0.85rem;';
        popover.textContent = target.textContent.replace('↩', '').trim();
        document.body.appendChild(popover);
        var rect = link.getBoundingClientRect();
        popover.style.left = rect.left + 'px';
        popover.style.top = (rect.bottom + 8 + window.scrollY) + 'px';
        popover.addEventListener('click', function() { popover.remove(); });
        setTimeout(function() {
          document.addEventListener('click', function rm() { if (popover.parentNode) popover.remove(); document.removeEventListener('click', rm); });
        }, 100);
      });
    });
  }

  // ── Skip Link ──────────────────────────────────
  function initSkipLink() {
    var skip = document.querySelector('.skip-link');
    if (!skip) return;
    skip.addEventListener('click', function(e) {
      var main = document.getElementById('main-content');
      if (main) {
        e.preventDefault();
        main.setAttribute('tabindex', '-1');
        main.focus();
      }
    });
  }

  // ── Standalone Search (404 page) ───────────────
  function initStandaloneSearch() {
    var input = document.getElementById('standalone-search');
    var results = document.getElementById('standalone-search-results');
    if (!input || !results) return;
    var data = null;
    fetch('/ultrametric-quantum/assets/search/search-data.json')
      .then(function(r) { return r.json(); })
      .then(function(d) { data = d; });

    input.addEventListener('input', function() {
      var q = input.value.trim().toLowerCase();
      if (!q || q.length < 2 || !data) { results.innerHTML = ''; return; }
      var hits = data.filter(function(item) {
        return item.title.toLowerCase().indexOf(q) > -1 || item.content.toLowerCase().indexOf(q) > -1;
      }).slice(0, 10);
      results.innerHTML = hits.map(function(h) {
        return '<div class="search-result-item"><a href="' + h.url + '" class="search-result-title">' + h.title + '</a><div class="search-result-snippet">' + h.content.substring(0, 150) + '...</div></div>';
      }).join('');
    });
  }

  // ── Initialization ─────────────────────────────
  function init() {
    initTheme();
    initProgressBar();
    initMobileMenu();
    initFab();
    initSmoothScroll();
    initSkipLink();
    initReadingTime();
    initSectionAnchors();
    initInPageTOC();

    // Fetch sidebar data
    fetch('/ultrametric-quantum/assets/js/nav/sidebar.json')
      .then(function(r) { return r.json(); })
      .then(function(data) {
        buildSidebarNav(data);
        initActiveHeading();
      })
      .catch(function() { console.log('Sidebar data not available'); });

    // Deferred: content-aware enhancements
    setTimeout(function() {
      initCopyButtons();
      initProofBlocks();
      initDiagramZoom();
      initEquationModals();
      initImageLightbox();
      initFootnotePopovers();
      initStandaloneSearch();
    }, 500);

    // Keyboard shortcut: Ctrl+K for search
    document.addEventListener('keydown', function(e) {
      if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        var searchInput = document.getElementById('search-input');
        if (searchInput) searchInput.focus();
      }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
