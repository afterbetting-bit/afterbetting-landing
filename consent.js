// Cookietoestemming voor afterbetting.com en app.afterbetting.com (gedeelde keuze via een cookie op .afterbetting.com).
// Zonder keuze of na weigeren zet Google Analytics geen cookies (Consent Mode, standaard "denied").
(function () {
  var NAME = 'ab_consent';
  var m = document.cookie.match(/(?:^|; )ab_consent=(granted|denied)/);
  if (m) return;
  var nl = (document.documentElement.lang || '').toLowerCase().indexOf('nl') === 0;
  var t = nl
    ? { text: 'Mogen we meten hoe de site wordt gebruikt? We gebruiken daarvoor Google Analytics, zonder advertenties. Je keuze geldt ook in de app.', more: 'Privacy', no: 'Weigeren', yes: 'Accepteren' }
    : { text: 'May we measure how the site is used? We use Google Analytics for this, no advertising. Your choice also applies in the app.', more: 'Privacy', no: 'Decline', yes: 'Accept' };

  function save(v) {
    var dom = /(^|\.)afterbetting\.com$/.test(location.hostname) ? '; domain=.afterbetting.com' : '';
    document.cookie = NAME + '=' + v + '; max-age=' + (180 * 86400) + '; path=/; SameSite=Lax' + (location.protocol === 'https:' ? '; Secure' : '') + dom;
    if (typeof window.gtag === 'function') window.gtag('consent', 'update', { analytics_storage: v });
    var el;
    while ((el = document.getElementById('ab-consent'))) el.parentNode.removeChild(el);
  }

  function show() {
    if (document.getElementById('ab-consent')) return;
    var box = document.createElement('div');
    box.id = 'ab-consent';
    box.setAttribute('role', 'dialog');
    box.setAttribute('aria-label', nl ? 'Cookies' : 'Cookies');
    box.style.cssText = 'position:fixed;left:12px;right:12px;bottom:12px;z-index:1000;max-width:560px;margin:0 auto;background:#2C2420;color:#fff;border-radius:16px;padding:16px 18px;font-family:"DM Sans",sans-serif;box-shadow:0 8px 30px rgba(0,0,0,.25)';
    var p = document.createElement('p');
    p.style.cssText = 'margin:0 0 12px;font-size:14px;line-height:1.55;color:rgba(255,255,255,.9)';
    p.appendChild(document.createTextNode(t.text + ' '));
    var a = document.createElement('a');
    a.href = 'https://app.afterbetting.com/privacy';
    a.textContent = t.more;
    a.style.cssText = 'color:#E8C4B2;text-decoration:underline;text-underline-offset:3px';
    p.appendChild(a);
    var row = document.createElement('div');
    row.style.cssText = 'display:flex;gap:8px';
    var btn = function (label, v) {
      var b = document.createElement('button');
      b.type = 'button';
      b.textContent = label;
      b.style.cssText = 'flex:1;min-height:44px;border-radius:100px;font:500 14px "DM Sans",sans-serif;cursor:pointer;border:1px solid rgba(255,255,255,.5);background:transparent;color:#fff';
      b.onclick = function () { save(v); };
      return b;
    };
    row.appendChild(btn(t.no, 'denied'));
    row.appendChild(btn(t.yes, 'granted'));
    box.appendChild(p);
    box.appendChild(row);
    document.body.appendChild(box);
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', show);
  else show();
})();
