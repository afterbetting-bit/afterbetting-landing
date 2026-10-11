# Prijzen naar één betaald plan: Afterbetting Plus, €4,99 per maand of €39,99 per jaar (11 okt 2026).
# Vervangt de prijsblokken op de EN- en NL-homepage en de losse vermeldingen van Progress/Premium. Veilig om opnieuw te draaien.
import re

T = {
 'en': dict(fn='setBillingEn', mid='toggle-monthly-en', yid='toggle-yearly-en', sfx='-en', aria='Choose billing period',
            m='Monthly', y='Yearly', save='4 months free with yearly',
            free='Free', free_price='Free', free_per='/forever', free_billed='No cost, ever',
            free_desc='Everything you need for the first days. It stays free.',
            free_items=['Day counter and milestones', 'Recovery kit and the Help now button', '5 habits', '3 journal entries a week', 'Money overview with 3 fixed costs', 'Weekly email update'],
            free_cta='Start free', free_note='No card needed',
            plus_desc='Everything in the app, without limits. Including your support circle.',
            plus_items=['Everything in Free', 'Unlimited journal and habits', 'Full money overview: debts, payoff plan and subscriptions', 'Insight into which habits go with better days', 'Support circle: a weekly update to people you trust'],
            plus_cta='Try Plus free for 7 days', plus_note='No card needed for the trial. Cancel any time.',
            m_price='€4.99', m_billed='Billed monthly', y_price='€3.33', y_billed='€39.99 a year, billed upfront', per='/month', badge='7 days free'),
 'nl': dict(fn='setBilling', mid='toggle-monthly', yid='toggle-yearly', sfx='', aria='Kies betaalperiode',
            m='Per maand', y='Per jaar', save='4 maanden gratis per jaar',
            free='Gratis', free_price='Gratis', free_per='/altijd', free_billed='Geen kosten',
            free_desc='Alles wat je nodig hebt voor de eerste dagen. Het blijft gratis.',
            free_items=['Dagenteller en mijlpalen', 'Herstelkit en de knop Nu hulp', '5 gewoontes', '3 dagboekstukken per week', 'Geldoverzicht met 3 vaste lasten', 'Wekelijkse update per mail'],
            free_cta='Begin gratis', free_note='Geen betaalgegevens nodig',
            plus_desc='Alles in de app, zonder grenzen. Ook je steunkring.',
            plus_items=['Alles uit Gratis', 'Onbeperkt dagboek en gewoontes', 'Volledig geldoverzicht: schulden, aflosplan en abonnementen', 'Inzicht in welke gewoontes bij betere dagen horen', 'Steunkring: een wekelijkse update aan wie je vertrouwt'],
            plus_cta='Probeer Plus 7 dagen gratis', plus_note='Geen betaalgegevens nodig voor de proef. Altijd opzegbaar.',
            m_price='€4,99', m_billed='Per maand betaald', y_price='€3,33', y_billed='€39,99 per jaar, vooruit betaald', per='/maand', badge='7 dagen gratis'),
}
APP = 'https://app.afterbetting.com/onboarding'

def block(t):
    li = lambda xs: ''.join(f'\n          <li><span class="check">&#10003;</span> {x}</li>' for x in xs)
    s = t['sfx']
    return f'''<div style="text-align:center;margin-bottom:1rem">
      <div class="pricing-toggle" role="tablist" aria-label="{t['aria']}">
        <button type="button" id="{t['mid']}" onclick="{t['fn']}('monthly')" aria-pressed="false">{t['m']}</button>
        <button type="button" id="{t['yid']}" class="active" onclick="{t['fn']}('yearly')" aria-pressed="true">{t['y']}</button>
      </div>
      <span class="pricing-savings">{t['save']}</span>
    </div>
    <div class="pricing two">
      <div class="plan">
        <div class="plan-tier">{t['free']}</div>
        <div class="plan-price"><span class="price">{t['free_price']}</span> <span class="price-period">{t['free_per']}</span></div>
        <div class="plan-billed">{t['free_billed']}</div>
        <p class="plan-desc">{t['free_desc']}</p>
        <ul class="plan-features">{li(t['free_items'])}
        </ul>
        <a rel="noopener noreferrer" onclick="if(window.gtag)gtag('event','cta_click',{{cta_location:'pricing_free',page_path:location.pathname}})" href="{APP}" class="plan-cta outline">{t['free_cta']}</a>
        <p class="plan-note">{t['free_note']}</p>
      </div>
      <div class="plan featured">
        <div class="plan-badge">{t['badge']}</div>
        <div class="plan-tier">Plus</div>
        <div class="plan-price"><span class="price" id="price-plus{s}">{t['y_price']}</span> <span class="price-period">{t['per']}</span></div>
        <div class="plan-billed" id="billed-plus{s}">{t['y_billed']}</div>
        <p class="plan-desc">{t['plus_desc']}</p>
        <ul class="plan-features">{li(t['plus_items'])}
        </ul>
        <a rel="noopener noreferrer" onclick="if(window.gtag)gtag('event','cta_click',{{cta_location:'pricing_plus',page_path:location.pathname}})" href="{APP}?billing=yearly" id="cta-plus{s}" class="plan-cta filled">{t['plus_cta']}</a>
        <p class="plan-note">{t['plus_note']}</p>
      </div>
    </div>
    <script>
      function {t['fn']}(mode){{
        var m=document.getElementById("{t['mid']}"),y=document.getElementById("{t['yid']}");
        var p=document.getElementById("price-plus{s}"),b=document.getElementById("billed-plus{s}"),c=document.getElementById("cta-plus{s}");
        var monthly=mode==="monthly";
        m.classList.toggle("active",monthly);y.classList.toggle("active",!monthly);
        m.setAttribute("aria-pressed",monthly?"true":"false");y.setAttribute("aria-pressed",monthly?"false":"true");
        p.textContent=monthly?"{t['m_price']}":"{t['y_price']}";
        b.textContent=monthly?"{t['m_billed']}":"{t['y_billed']}";
        c.href="{APP}?billing="+(monthly?"monthly":"yearly");
      }}
    </script>'''

for path, lang in (('index.html', 'en'), ('nl/index.html', 'nl')):
    s = open(path, encoding='utf-8').read()
    a = s.index('id="pricing"'); a = s.index('<div style="text-align:center;margin-bottom:1rem">', a)
    b = s.index('</script>', a) + len('</script>')
    s = s[:a] + block(T[lang]) + s[b:]
    if lang == 'en':
        s = s.replace('Try Progress free for 7 days</a><p>No card needed. After 7 days you choose: free plan or Progress.',
                      'Try Plus free for 7 days</a><p>No card needed. After 7 days you choose: free or Plus, €4.99 a month.')
    else:
        s = s.replace('Probeer Progress 7 dagen gratis</a><p>Geen betaalgegevens nodig. Na 7 dagen kies je zelf: gratis of Progress.',
                      'Probeer Plus 7 dagen gratis</a><p>Geen betaalgegevens nodig. Na 7 dagen kies je zelf: gratis of Plus, €4,99 per maand.')
        s = s.replace('margin-left:.4rem;font-weight:500">Premium</span>', 'margin-left:.4rem;font-weight:500">Plus</span>')
    assert 'Progress' not in re.sub(r'Progress dashboard', '', s) and 'Premium' not in s, path
    assert not re.search(r'(?<![0-9])(9|14|79|119)[.,]99', s), path
    open(path, 'w', encoding='utf-8').write(s)
    print(path, 'bijgewerkt')

# Blog: één vermelding van de oude plannen
p = 'blog/rebuild-finances-after-gambling.html'
s = open(p, encoding='utf-8').read()
s = s.replace('Available on Progress and Premium plans.', 'Available on Plus.')
open(p, 'w', encoding='utf-8').write(s)

# Prijzen alleen in euro: Stripe rekent in EUR, dus geen pond of dollar meer tonen.
open('currency.js', 'w', encoding='utf-8').write('''// Afterbetting rekent af in euro. Alleen het valutateken in de rekenhulp volgt de bezoeker.
(function(){
  var tz = Intl.DateTimeFormat().resolvedOptions().timeZone || '';
  var lang = navigator.language || '';
  var calcSymbol = '\\u20ac';
  if (tz.indexOf('London') > -1 || tz.indexOf('Dublin') > -1 || lang.indexOf('en-GB') > -1) calcSymbol = '\\u00a3';
  else if (tz.indexOf('America') > -1 || lang.indexOf('en-US') > -1) calcSymbol = '$';
  else if (tz.indexOf('Australia') > -1 || lang.indexOf('en-AU') > -1) calcSymbol = 'A$';
  else if (tz.indexOf('Canada') > -1 || lang.indexOf('en-CA') > -1) calcSymbol = 'C$';
  document.addEventListener('DOMContentLoaded', function(){
    document.querySelectorAll('.calc-currency').forEach(function(el){ el.textContent = calcSymbol; });
  });
})();
''')

css = open('theme.css', encoding='utf-8').read()
if '.pricing.two' not in css:
    css += '''
/* Prijzen: twee plannen naast elkaar (Gratis en Plus) */
.pricing.two { grid-template-columns: repeat(2, minmax(0, 1fr)) !important; max-width: 860px; margin-left: auto; margin-right: auto; }
.pricing.two .plan-note { font-size: .8rem; color: var(--muted); margin-top: .75rem; text-align: center; }
@media (max-width: 768px) { .pricing.two { grid-template-columns: 1fr !important; } }
'''
    open('theme.css', 'w', encoding='utf-8').write(css)
print('klaar')
