// Reveal sections as they scroll into view (skipped when reduced motion is preferred).
(function () {
  document.documentElement.classList.remove('no-js');
  var els = document.querySelectorAll('.reveal');
  if (!('IntersectionObserver' in window) || window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    els.forEach(function (e) { e.classList.add('in'); });
    return;
  }
  // Anything already on screen at load shows immediately (no flash of empty content).
  var vh = window.innerHeight;
  els.forEach(function (e) { if (e.getBoundingClientRect().top < vh) e.classList.add('in'); });
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
  els.forEach(function (e) { io.observe(e); });
})();
