# 8 nov 2026: pijler stoppen-met-gokken v2 (tekst akkoord founder), EN how-to-stop-gambling aanvullingen,
# ankerlinks "stoppen met gokken" vanaf ondersteunende NL-pagina's. Veilig om opnieuw te draaien.
import json, re
DATE = '2026-11-08'
NLF, ENF = 'nl/blog/stoppen-met-gokken.html', 'blog/how-to-stop-gambling.html'
URL = 'https://app.afterbetting.com/onboarding?van=blog&t=drang'
OC = "onclick=\"if(window.gtag)gtag('event','cta_click',{cta_location:'app_card',cta_theme:'drang',page_path:location.pathname})\""
def card(label, quote, meta, btn, note):
    return (f'<div class="app-card"><div class="app-card-screen"><span class="app-card-label">{label}</span>'
            f'<p class="app-card-quote">{quote}</p><div class="app-card-timer">15:00</div><p class="app-card-meta">{meta}</p></div>'
            f'<a class="app-card-btn" href="{URL}" rel="noopener" {OC}>{btn}</a><p class="app-card-note">{note}</p></div>')
def L(slug, text): return f'<a href="/nl/blog/{slug}">{text}</a>'

def set_faq(s, faqs):
    def fix(m):
        j = json.loads(m.group(1))
        if j.get('@type') == 'FAQPage':
            j['mainEntity'] = [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': re.sub('<[^>]+>', '', a)}} for q, a in faqs]
        elif j.get('@type') == 'Article':
            j['dateModified'] = DATE
            if HEAD: j['headline'] = HEAD; j['description'] = DESC
        else: return m.group(0)
        return '<script type="application/ld+json">' + json.dumps(j, ensure_ascii=False) + '</script>'
    return re.sub(r'<script type="application/ld\+json">(.*?)</script>', fix, s, flags=re.S)

# ---------- NL ----------
TITLE = 'Stoppen met gokken: hoe stop je echt? Eerlijke gids'
DESC = 'Stoppen met gokken lukt niet op wilskracht. Wat wel werkt, wat je vandaag nog doet en wanneer je hulp zoekt. Van iemand die 8 jaar gokte.'
HEAD = 'Stoppen met gokken: hoe stop je echt?'
from pijler_tekst_nov8 import NL_BODY, NL_FAQ
s = open(NLF, encoding='utf-8').read()
if 'id="kort-antwoord"' not in s:
    s = re.sub(r'<title>[^<]*</title>', f'<title>{TITLE}</title>', s)
    for k in ('og:title', 'twitter:title'):
        s = re.sub(r'(<meta (?:property|name)="%s" content=")[^"]*' % k, lambda m: m.group(1) + TITLE, s)
    for k in ('description', 'og:description', 'twitter:description'):
        s = re.sub(r'(<meta (?:property|name)="%s" content=")[^"]*' % k, lambda m: m.group(1) + DESC, s)
    s = re.sub(r'<h1>[^<]*</h1>', f'<h1>{HEAD}</h1>', s, count=1)
    s = re.sub(r'(<h1>[^<]*</h1>\n<p style="[^"]*">)[^<]*', lambda m: m.group(1) + 'Wat wel werkt, wat je vandaag nog doet en wanneer je hulp zoekt. Van iemand die 8 jaar gokte.', s, count=1)
    a = s.index('<article class="body">') + len('<article class="body">')
    mid = re.search(r'<div class="mid-cta">.*?</a></div>', s[a:], flags=re.S).group(0)
    tail = s.index('<div class="cta-block">', a)
    crd = card('Nu hulp, met één tik', '"Je hebt dit 3 keer eerder doorstaan. De drang zakt. Hij komt op, piekt en zakt."',
               'Een timer, je eigen reden om te stoppen, een bericht aan je vertrouwenspersoon en de hulplijn.',
               'Probeer Nu hulp gratis', 'Voorbeeld. De basis van Afterbetting is gratis, zonder betaalgegevens.')
    faq = '<h2>Veelgestelde vragen</h2>\n' + '\n'.join(f'<h3>{q}</h3>\n<p>{x}</p>' for q, x in NL_FAQ)
    body = NL_BODY.replace('{MID}', mid).replace('{CARD}', crd).replace('{FAQ}', faq)
    s = s[:a] + '\n' + body + '\n' + s[tail:]
    src = ('<aside class="sources"><p class="sources-label">Bronnen</p><ul>'
           '<li><a href="https://cruksregister.nl/" rel="noopener">Cruksregister</a></li>'
           '<li><a href="https://kansspelautoriteit.nl/" rel="noopener">Kansspelautoriteit</a></li>'
           '<li><a href="https://www.openovergokken.nl/" rel="noopener">OpenOverGokken</a></li>'
           '<li><a href="https://www.rijksoverheid.nl/onderwerpen/zorgverzekering/eigen-risico-zorgverzekering" rel="noopener">Rijksoverheid, eigen risico zorgverzekering</a></li></ul></aside>')
    if 'class="sources"' not in s:
        e = s.index('</aside>', s.index('class="author-box"')) + len('</aside>')
        s = s[:e] + '\n' + src + s[e:]
    s = set_faq(s, NL_FAQ)
    open(NLF, 'w', encoding='utf-8').write(s); print('NL pijler vervangen')

# ---------- EN ----------
HEAD = None
from pijler_tekst_nov8 import EN_SHORT, EN_FAQ_NEW
s = open(ENF, encoding='utf-8').read()
if 'id="short-answer"' not in s:
    anchor = 'The rest can wait until tomorrow.</p>'
    i = s.index(anchor, s.index('<article')) + len(anchor)
    s = s[:i] + '\n' + EN_SHORT + s[i:]
    i = s.index('<h2>When the urge hits</h2>'); i = s.index('</ul>', i) + len('</ul>')
    crd = card('Help now, one tap away', '"You got through this 3 times before. The urge passes. It rises, peaks and fades."',
               'A timer, your own reason to stop, a message to someone you trust and the helpline.',
               'Try Help now free', "Example. Afterbetting's basics are free, no card needed.")
    s = s[:i] + '\n' + crd + s[i:]
    q = '<h3>Why is it so hard to stop gambling?</h3>'
    i = s.index('</p>', s.index(q, s.index('<article'))) + 4
    s = s[:i] + '\n' + '\n'.join(f'<h3>{a}</h3>\n<p>{b}</p>' for a, b in EN_FAQ_NEW) + s[i:]
    m = re.search(r'"@type": "FAQPage".*?</script>', s, flags=re.S)
    j = json.loads(re.search(r'<script type="application/ld\+json">(\{[^<]*"FAQPage".*?)</script>', s, flags=re.S).group(1))
    old = [(x['name'], x['acceptedAnswer']['text']) for x in j['mainEntity']]
    s = set_faq(s, old + EN_FAQ_NEW)
    open(ENF, 'w', encoding='utf-8').write(s); print('EN aangevuld')

# ---------- ankerlinks naar de pijler ----------
LINK = '<a href="/nl/blog/stoppen-met-gokken">Stoppen met gokken: hoe stop je echt?</a>'
n = 0
for slug in ['stoppen-met-gokken-als-je-wint', 'hoe-stop-ik-met-gokken-met-schulden', 'slaapproblemen-stoppen-met-gokken',
             'gokverslaving-en-identiteit', 'stoppen-met-gokken-en-sparen', 'afkickverschijnselen-gokken']:
    f = f'nl/blog/{slug}.html'; s = open(f, encoding='utf-8').read()
    if 'nl/blog/stoppen-met-gokken"' in s: continue
    m = re.search(r'<p><strong>Lees ook:</strong>(.*?)</p>', s, flags=re.S)
    if m:
        inner = m.group(1).rstrip(); end = '.' if inner.endswith('.') else ''
        s = s[:m.start()] + '<p><strong>Lees ook:</strong>' + (inner[:-1] if end else inner) + ' · ' + LINK + end + '</p>' + s[m.end():]
    else:
        i = s.index('<div class="cta-block">') if '<div class="cta-block">' in s else s.index('<aside class="author-box">')
        s = s[:i] + '<p><strong>Lees ook:</strong> ' + LINK + '</p>\n' + s[i:]
    open(f, 'w', encoding='utf-8').write(s); n += 1
print('ankerlinks', n)

# CSS kort-antwoord-blok (herbruikbaar)
CSS = ('\n/* Kort antwoord bovenaan artikel (8 nov 2026) */\n'
       '.answer-box{background:#EEF5F2;border:1px solid #C2D8D0;border-radius:12px;padding:1.1rem 1.25rem;margin:0 0 1.75rem}\n'
       '.answer-box h2{font-size:1.1rem;margin:0 0 .5rem}\n.answer-box p{margin:0}\n')
th = open('theme.css', encoding='utf-8').read()
if '.answer-box{' not in th: open('theme.css', 'a', encoding='utf-8').write(CSS); print('css toegevoegd')
