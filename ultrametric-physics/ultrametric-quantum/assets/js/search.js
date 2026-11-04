// ─── Ultrametric Quantum Computation — search.js ───
(function(){
  'use strict';

  var searchData = null;
  var resultsContainer = document.getElementById('search-results');
  var searchInput = document.getElementById('search-input');
  if (!searchInput || !resultsContainer) return;

  var debounceTimer;

  // Load search data
  fetch('/ultrametric-quantum/assets/search/search-data.json')
    .then(function(r) { return r.json(); })
    .then(function(data) {
      searchData = data;
      searchInput.disabled = false;
      searchInput.placeholder = 'Search… (Ctrl+K)';
    })
    .catch(function(err) {
      console.warn('Search data not available:', err);
      searchInput.placeholder = 'Search unavailable';
    });

  // Tokenize and normalize
  function tokenize(str) {
    return str.toLowerCase().replace(/[^a-z0-9\s]/g, '').split(/\s+/).filter(Boolean);
  }

  function search(query) {
    if (!searchData) return [];
    var tokens = tokenize(query);
    if (!tokens.length) return [];

    return searchData
      .map(function(item) {
        var titleLower = item.title.toLowerCase();
        var contentLower = item.content.toLowerCase();
        var score = 0;
        tokens.forEach(function(token) {
          if (titleLower.indexOf(token) > -1) score += 10;
          var idx = contentLower.indexOf(token);
          if (idx > -1) { score += 3; if (idx < 50) score += 2; }
          var regex = new RegExp('\\b' + token + '\\b', 'i');
          if (regex.test(titleLower)) score += 5;
          if (regex.test(contentLower)) score += 2;
        });
        return { item: item, score: score };
      })
      .filter(function(r) { return r.score > 0; })
      .sort(function(a, b) { return b.score - a.score; })
      .slice(0, 20)
      .map(function(r) { return r.item; });
  }

  function highlightMatches(text, query) {
    var tokens = tokenize(query);
    var result = text;
    tokens.forEach(function(token) {
      var regex = new RegExp('(' + token.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'gi');
      result = result.replace(regex, '<mark>$1</mark>');
    });
    return result;
  }

  function displayResults(results, query) {
    if (!results.length) {
      resultsContainer.innerHTML = '<div class="search-result-item"><div class="search-result-title">No results found</div></div>';
      resultsContainer.classList.add('visible');
      return;
    }
    resultsContainer.innerHTML = results.map(function(item) {
      return '<div class="search-result-item" data-url="' + item.url + '">' +
        '<div class="search-result-title">' + highlightMatches(item.title, query) + '</div>' +
        '<div class="search-result-snippet">' + highlightMatches(item.content.substring(0, 200), query) + '...</div>' +
        '</div>';
    }).join('');
    resultsContainer.classList.add('visible');

    // Click handler
    resultsContainer.querySelectorAll('.search-result-item').forEach(function(el) {
      el.addEventListener('click', function() {
        window.location.href = el.getAttribute('data-url');
        resultsContainer.classList.remove('visible');
        resultsContainer.innerHTML = '';
        searchInput.value = '';
      });
    });
  }

  searchInput.addEventListener('input', function() {
    clearTimeout(debounceTimer);
    var query = searchInput.value.trim();
    if (query.length < 2) {
      resultsContainer.classList.remove('visible');
      resultsContainer.innerHTML = '';
      return;
    }
    debounceTimer = setTimeout(function() {
      var results = search(query);
      displayResults(results, query);
    }, 300);
  });

  // Keyboard navigation
  var selectedIndex = -1;
  searchInput.addEventListener('keydown', function(e) {
    var items = resultsContainer.querySelectorAll('.search-result-item');
    if (e.key === 'ArrowDown') {
      e.preventDefault();
      selectedIndex = Math.min(selectedIndex + 1, items.length - 1);
      updateSelection(items);
    } else if (e.key === 'ArrowUp') {
      e.preventDefault();
      selectedIndex = Math.max(selectedIndex - 1, -1);
      updateSelection(items);
    } else if (e.key === 'Enter') {
      e.preventDefault();
      if (selectedIndex >= 0 && items[selectedIndex]) {
        items[selectedIndex].click();
      } else if (items.length > 0) {
        items[0].click();
      }
    } else if (e.key === 'Escape') {
      resultsContainer.classList.remove('visible');
      resultsContainer.innerHTML = '';
      selectedIndex = -1;
      searchInput.blur();
    }
  });

  function updateSelection(items) {
    items.forEach(function(item, i) {
      item.style.background = i === selectedIndex ? 'var(--color-bg-secondary)' : '';
    });
  }

  // Click outside closes results
  document.addEventListener('click', function(e) {
    if (!searchInput.contains(e.target) && !resultsContainer.contains(e.target)) {
      resultsContainer.classList.remove('visible');
      selectedIndex = -1;
    }
  });
})();
