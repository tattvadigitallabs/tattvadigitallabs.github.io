// Reveal sections as they scroll into view (skipped when reduced motion is preferred).
(function () {
  document.documentElement.classList.remove('no-js');
  var els = document.querySelectorAll('.reveal');
  if (!('IntersectionObserver' in window) || window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    els.forEach(function (e) { e.classList.add('in'); });
  } else {
    // Anything already on screen at load shows immediately (no flash of empty content).
    var vh = window.innerHeight;
    els.forEach(function (e) { if (e.getBoundingClientRect().top < vh) e.classList.add('in'); });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    els.forEach(function (e) { io.observe(e); });
  }
})();

// App directory: filter by category and search. Without JavaScript every app is simply listed.
(function () {
  var grid = document.querySelector('[data-grid]');
  if (!grid) return;
  var cards = Array.prototype.slice.call(grid.querySelectorAll('a.app-card'));
  var chips = Array.prototype.slice.call(document.querySelectorAll('.chip[data-filter]'));
  var input = document.querySelector('[data-search-input]');
  var empty = document.querySelector('.no-results');
  var state = { cat: 'all', q: '' };

  function apply() {
    var shown = 0;
    cards.forEach(function (c) {
      var ok = (state.cat === 'all' || c.dataset.cat === state.cat) &&
        (!state.q || state.q.split(/\s+/).every(function (w) { return c.dataset.search.indexOf(w) !== -1; }));
      c.hidden = !ok;
      if (ok) shown++;
    });
    chips.forEach(function (ch) { ch.setAttribute('aria-pressed', String(ch.dataset.filter === state.cat)); });
    if (empty) empty.hidden = shown !== 0;
  }
  chips.forEach(function (ch) {
    ch.addEventListener('click', function () { state.cat = ch.dataset.filter; apply(); });
  });
  if (input) input.addEventListener('input', function () { state.q = input.value.trim().toLowerCase(); apply(); });
  var clear = document.querySelector('[data-clear]');
  if (clear) clear.addEventListener('click', function () { state = { cat: 'all', q: '' }; if (input) input.value = ''; apply(); });
})();
