/* Think and Grow Rich — interactions (vanilla, 60fps, reduced-motion aware) */
(function () {
  'use strict';
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- scroll reveals ---------- */
  var reveals = document.querySelectorAll('.reveal');
  if (reduce || !('IntersectionObserver' in window)) {
    reveals.forEach(function (el) { el.classList.add('in'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { threshold: 0.16, rootMargin: '0px 0px -8% 0px' });
    reveals.forEach(function (el) { io.observe(el); });
    // immediate pass so above-the-fold content reveals on the first frame
    // (no flash-of-invisible-content while we wait for the observer's async tick)
    requestAnimationFrame(function () {
      var vh = window.innerHeight;
      reveals.forEach(function (el) {
        if (el.classList.contains('in')) return;
        var r = el.getBoundingClientRect();
        if (r.top < vh * 0.92 && r.bottom > 0) { el.classList.add('in'); io.unobserve(el); }
      });
    });
  }

  /* ---------- count-ups ---------- */
  function animateCount(el) {
    var target = parseFloat(el.getAttribute('data-count'));
    var suffix = el.getAttribute('data-suffix') || '';
    if (reduce) { el.textContent = target + suffix; return; }
    var dur = 1500, start = null;
    function step(ts) {
      if (start === null) start = ts;
      var p = Math.min((ts - start) / dur, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.round(target * eased) + suffix;
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }
  var counters = document.querySelectorAll('[data-count]');
  if ('IntersectionObserver' in window) {
    var cio = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { animateCount(e.target); cio.unobserve(e.target); }
      });
    }, { threshold: 0.6 });
    counters.forEach(function (el) { cio.observe(el); });
  } else {
    counters.forEach(animateCount);
  }

  /* ---------- nav condense ---------- */
  var nav = document.getElementById('nav');
  function onScroll() {
    if (window.scrollY > 24) nav.classList.add('scrolled');
    else nav.classList.remove('scrolled');
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* ---------- hero parallax ---------- */
  if (!reduce) {
    var deco = document.querySelector('.hero-deco');
    var book = document.querySelector('.hero-book');
    var ticking = false;
    window.addEventListener('scroll', function () {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(function () {
        var y = window.scrollY;
        if (deco && y < 1100) deco.style.transform = 'translate(-50%,-50%) translateY(' + (y * 0.12) + 'px)';
        if (book && y < 1100) book.style.transform = 'translateY(' + (y * -0.05) + 'px)';
        ticking = false;
      });
    }, { passive: true });
  }

  /* ---------- mobile drawer ---------- */
  var toggle = document.getElementById('navToggle');
  var drawer = document.getElementById('drawer');
  var drawerX = document.getElementById('drawerX');
  function openDrawer() {
    drawer.classList.add('open'); drawer.setAttribute('aria-hidden', 'false');
    toggle.setAttribute('aria-expanded', 'true'); document.body.style.overflow = 'hidden';
  }
  function closeDrawer() {
    drawer.classList.remove('open'); drawer.setAttribute('aria-hidden', 'true');
    toggle.setAttribute('aria-expanded', 'false'); document.body.style.overflow = '';
  }
  if (toggle) toggle.addEventListener('click', openDrawer);
  if (drawerX) drawerX.addEventListener('click', closeDrawer);
  if (drawer) drawer.querySelectorAll('a').forEach(function (a) { a.addEventListener('click', closeDrawer); });

  /* ---------- FAQ accordion ---------- */
  document.querySelectorAll('.faq button').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var item = btn.closest('.faq');
      var ans = item.querySelector('.ans');
      var open = item.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
      ans.style.maxHeight = open ? ans.scrollHeight + 'px' : '0';
    });
  });

  /* ---------- Esc closes drawer ---------- */
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && drawer && drawer.classList.contains('open')) closeDrawer();
  });

  /* keep open FAQ sized correctly on resize */
  window.addEventListener('resize', function () {
    document.querySelectorAll('.faq.open .ans').forEach(function (ans) {
      ans.style.maxHeight = ans.scrollHeight + 'px';
    });
  });
})();
