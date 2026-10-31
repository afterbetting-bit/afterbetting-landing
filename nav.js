// Menu op mobiel: de navigatielinks zijn onder 768px verborgen. Deze knop klapt ze uit.
(function () {
  var nav = document.querySelector('body > nav');
  var links = nav && nav.querySelector('.nav-links');
  if (!nav || !links || nav.querySelector('.ab-menu')) return;
  var lang = (document.documentElement.lang || 'en').slice(0, 2).toLowerCase();
  var t = { nl: ['Menu', 'Sluiten'], de: ['Menü', 'Schließen'], fr: ['Menu', 'Fermer'], es: ['Menú', 'Cerrar'] }[lang] || ['Menu', 'Close'];
  var css = document.createElement('style');
  css.textContent =
    '.ab-menu{display:none;margin-left:auto;margin-right:.6rem;min-height:40px;padding:.4rem .9rem;border:1px solid #DCE3DE;border-radius:100px;background:#fff;color:#0F1A19;font:500 .875rem "DM Sans",sans-serif;cursor:pointer}' +
    '.ab-menu:focus-visible{outline:2px solid #0F1A19;outline-offset:2px}' +
    '@media(max-width:768px){.ab-menu{display:inline-flex;align-items:center}' +
    'nav.ab-open .nav-links{display:flex !important;flex-direction:column;align-items:stretch;gap:0;position:absolute;top:100%;left:0;right:0;background:#fff;border-bottom:1px solid #DCE3DE;box-shadow:0 12px 24px rgba(44,36,32,.08);padding:.25rem 1.25rem .75rem}' +
    'nav.ab-open .nav-links a{display:block;padding:.85rem 0;font-size:1rem;color:#0F1A19;border-bottom:1px solid #ECF0EC}' +
    'nav.ab-open .nav-links a:last-child{border-bottom:none}' +
    'nav.ab-open .nav-links a.btn{color:#fff;text-align:center;margin-top:.6rem;padding:.8rem 1rem;border-bottom:none;border-radius:100px}' +
    'nav.ab-open .nav-links a.btn-text{text-decoration:none}}';
  document.head.appendChild(css);
  if (!links.id) links.id = 'ab-nav-links';
  var btn = document.createElement('button');
  btn.type = 'button';
  btn.className = 'ab-menu';
  btn.setAttribute('aria-controls', links.id);
  btn.setAttribute('aria-expanded', 'false');
  btn.textContent = t[0];
  function set(open) {
    nav.classList.toggle('ab-open', open);
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    btn.textContent = open ? t[1] : t[0];
  }
  btn.addEventListener('click', function () { set(!nav.classList.contains('ab-open')); });
  links.addEventListener('click', function (e) { if (e.target.closest('a')) set(false); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && nav.classList.contains('ab-open')) { set(false); btn.focus(); } });
  document.addEventListener('click', function (e) { if (nav.classList.contains('ab-open') && !nav.contains(e.target)) set(false); });
  links.parentNode.insertBefore(btn, links.nextSibling);
})();

// 31 okt 2026: meten en de vaste balk onderaan (#abSticky, staat al in elk blogartikel).
// 1. Elke klik naar de aanmelding telt als cta_click. De knop in de navigatie had nog geen meting.
// 2. De balk gaat even weg zolang een andere aanmeldknop of de crisisregel in beeld is, zodat hij die niet afdekt.
(function () {
  var APP = 'app.afterbetting.com/onboarding';
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href*="' + APP + '"]');
    if (!a || a.hasAttribute('onclick')) return;
    try {
      var t = (a.getAttribute('href').match(/[?&]t=([a-z]+)/) || [])[1] || '';
      if (window.gtag) window.gtag('event', 'cta_click', { cta_location: a.closest('nav') ? 'nav' : 'link', cta_theme: t, page_path: location.pathname });
    } catch (err) { /* geen meting */ }
  }, true);

  var bar = document.getElementById('abSticky');
  if (!bar || !('IntersectionObserver' in window)) return;
  var css = document.createElement('style');
  css.textContent = '.ab-sticky.ab-hide{transform:translateY(110%) !important}';
  document.head.appendChild(css);
  var seen = new Set();
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) { if (en.isIntersecting) seen.add(en.target); else seen.delete(en.target); });
    bar.classList.toggle('ab-hide', seen.size > 0);
  });
  document.querySelectorAll('.mid-cta, .cta, .cta-block, .crisis-footer').forEach(function (el) { io.observe(el); });
})();
