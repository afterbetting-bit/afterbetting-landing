# Verbeteringen drang-pagina's (8 nov 2026): founder-ervaring (bevestigd), app-kaart Nu hulp, 2 FAQ's, interne links.
import json, re
DATE = '2026-11-08'
def oc(theme='drang'):
    return ("onclick=\"if(window.gtag)gtag('event','cta_click',{cta_location:'app_card',cta_theme:'%s',page_path:location.pathname})\"" % theme)
URL = 'https://app.afterbetting.com/onboarding?van=blog&t=drang'
def card(title, quote, meta, btn, note):
    return (f'<div class="app-card"><div class="app-card-screen"><span class="app-card-label">{title}</span>'
            f'<p class="app-card-quote">{quote}</p><div class="app-card-timer">15:00</div><p class="app-card-meta">{meta}</p></div>'
            f'<a class="app-card-btn" href="{URL}" rel="noopener" {oc()}>{btn}</a><p class="app-card-note">{note}</p></div>')
PAGES = {
 'nl/blog/drang-om-te-gokken.html': dict(
  after_body='<p><strong>Je lijf.</strong> Moe, honger, te weinig geslapen.</p>',
  trigger='<p><strong>Alcohol en lege uren.</strong> Bij mij maakten twee dingen de drang een stuk groter: alcohol, en een dag zonder invulling. Leegte, niets te doen. Weet je dat je wilt stoppen, wees dan extra voorzichtig op avonden dat je drinkt of niets gepland hebt.</p>',
  after_peaks='Je herkent ze sneller.</p>',
  moment="<p>Bij mij was het in de eerste weken het zwaarst. Ik werd 's nachts wakker en de zin om te gokken was er al, nog voor ik goed wakker was. Na een paar weken werd dat minder. Mijn slaap kwam als eerste terug.</p>",
  kit='<p>In de gratis Herstelkit in de app staan deze oefeningen bij elkaar, met een timer en de hulplijn onder één knop.</p>',
  card=card('Nu hulp, met één tik', '"Je hebt dit 3 keer eerder doorstaan. De drang zakt. Hij komt op, piekt en zakt."',
            'Een timer, je eigen reden om te stoppen, een bericht aan je vertrouwenspersoon en de hulplijn.',
            'Probeer Nu hulp gratis', 'Voorbeeld. De basis van Afterbetting is gratis, zonder betaalgegevens.'),
  will='<p><strong>Alleen op wilskracht varen.</strong> Wilskracht is op een slechte avond op. Sloten, mensen en plannen houden het langer vol.</p>',
  will_link='<p>Waarom wilskracht alleen zo vaak niet genoeg is, lees je in <a href="/nl/blog/waarom-kan-ik-niet-stoppen-met-gokken">waarom kan ik niet stoppen met gokken?</a></p>',
  faqhead='<h2>Veelgestelde vragen</h2>',
  faqs=[("Waarom heb ik 's nachts zin om te gokken?",
         "'s Nachts is het stil, ben je moe en ligt je telefoon binnen handbereik. Veel mensen merken dat in de eerste weken na het stoppen. Bij mij werd het na een paar weken minder. Leg je telefoon 's nachts buiten je slaapkamer en zet een blokkade aan, zodat er een drempel is als je wakker wordt.", None),
        ("Is er een app die helpt bij drang om te gokken?",
         "Ja. Een herstel-app zoals Afterbetting heeft een knop voor het moment zelf, met een timer, je eigen redenen en de hulplijn. Een blokkeer-app houdt goksites tegen. Ze werken het best samen.",
         ' Lees <a href="/nl/blog/stoppen-met-gokken-app">stoppen met gokken app: welke helpt echt?</a>')]),
 'blog/do-gambling-urges-go-away.html': dict(
  after_body='<p><strong>Your body.</strong> Tired, hungry, short on sleep.</p>',
  trigger="<p><strong>Alcohol and empty hours.</strong> For me, two things made the urge a lot bigger: alcohol, and a day with nothing in it. Emptiness, nothing to do. If you're trying to stop, be extra careful on nights you drink or have nothing planned.</p>",
  after_peaks='You recognise them faster.</p>',
  moment="<p>For me, the first weeks were the hardest. I'd wake up at night and the urge was already there, before I was even properly awake. After a few weeks that eased. My sleep came back first.</p>",
  kit='<p>The free recovery kit in the app has these exercises in one place, with a timer and the helpline one tap away.</p>',
  card=card('Help now, one tap away', '"You got through this 3 times before. The urge passes. It rises, peaks and fades."',
            'A timer, your own reason to stop, a message to someone you trust and the helpline.',
            'Try Help now free', "Example. Afterbetting's basics are free, no card needed."),
  will='<p><strong>Rely on willpower alone.</strong> Willpower runs out on a bad evening. Locks, people and plans last longer.</p>',
  will_link='<p>Why willpower alone so often isn\'t enough is in <a href="/blog/why-cant-i-stop-gambling">why can\'t I stop gambling?</a></p>',
  faqhead='<h2>Frequently asked questions</h2>',
  faqs=[("Why do I get gambling urges at night?",
         "At night it's quiet, you're tired and your phone is within reach. A lot of people notice it in the first weeks after stopping. For me it eased after a few weeks. Keep your phone out of the bedroom at night and switch on a blocker, so there's a barrier when you wake up.", None),
        ("Is there an app that helps with gambling urges?",
         "Yes. A recovery app like Afterbetting has a button for the moment itself, with a timer, your own reasons and the helpline. A blocking app stops gambling sites from opening. They work best together.",
         ' Read <a href="/blog/quit-gambling-app">quit gambling app: which ones actually help?</a>')]),
}
def rep(s, old, new):
    assert s.count(old) == 1, old[:60]; return s.replace(old, new)
for p, d in PAGES.items():
    s = open(p, encoding='utf-8').read()
    if 'app-card' in s: print('al gedaan:', p); continue
    s = rep(s, d['after_body'], d['after_body'] + '\n' + d['trigger'])
    s = rep(s, d['after_peaks'], d['after_peaks'] + '\n' + d['moment'])
    s = rep(s, d['kit'], d['card'])
    s = rep(s, d['will'], d['will'] + '\n' + d['will_link'])
    # zichtbare FAQ: achteraan de bestaande lijst (voor het eerste blok na de laatste FAQ-p)
    i = s.index(d['faqhead']); j = s.index('\n<', s.index('</p>', s.rindex('<h3>', i, s.index('class="cta', i)))) 
    add = ''.join(f'\n<h3>{q}</h3>\n<p>{a}{l or ""}</p>' for q, a, l in d['faqs'])
    s = s[:j] + add + s[j:]
    # JSON-LD
    m = re.search(r'<script type="application/ld\+json">(\{"@context": "https://schema.org", "@type": "FAQPage".*?)</script>', s)
    data = json.loads(m.group(1))
    for q, a, l in d['faqs']:
        data['mainEntity'].append({"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}})
    s = s[:m.start(1)] + json.dumps(data, ensure_ascii=False) + s[m.end(1):]
    s = re.sub(r'"dateModified": ?"[^"]+"', f'"dateModified": "{DATE}"', s)
    assert '—' not in s
    open(p, 'w', encoding='utf-8').write(s); print('bijgewerkt:', p)
css = open('theme.css', encoding='utf-8').read()
if '.app-card{' not in css:
    css += ('\n/* app-kaart Nu hulp (8 nov 2026) */\n'
     '.app-card{background:var(--clay-bg);border-radius:18px;padding:1.25rem;margin:2rem 0;text-align:center}\n'
     '.app-card-screen{max-width:320px;margin:0 auto 1rem;background:#fff;border:1px solid rgba(0,0,0,.08);border-radius:22px;padding:1.25rem 1.1rem;box-shadow:0 6px 20px rgba(0,0,0,.06)}\n'
     '.app-card-label{display:block;font-size:.8rem;font-weight:700;letter-spacing:.04em;text-transform:uppercase;color:var(--mid)}\n'
     '.app-card-quote{font-size:1rem;line-height:1.5;color:var(--ink);margin:.6rem 0}\n'
     '.app-card-timer{font-size:2.4rem;font-weight:700;color:var(--ink);font-variant-numeric:tabular-nums;margin:.2rem 0}\n'
     '.app-card-meta{font-size:.85rem;line-height:1.45;color:#6b6b6b;margin:.4rem 0 0}\n'
     '.app-card-btn{display:inline-block;background:var(--ink);color:#fff;font-weight:700;border-radius:999px;padding:.75rem 1.4rem;text-decoration:none}\n'
     '.app-card-note{font-size:.8rem;color:var(--mid);margin:.7rem 0 0}\n'
     'article a.app-card-btn,.app-card a.app-card-btn{color:#fff !important;text-decoration:none !important;border-bottom:0 !important;background-image:none !important}\n')
    open('theme.css', 'w', encoding='utf-8').write(css); print('css toegevoegd')
