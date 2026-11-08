# Bouwt het NL/EN-paar van 8 nov 2026: stoppen met gokken app / quit gambling app (doelgroep: zoekt een middel om te stoppen).
# Daarna interne links. Teksten goedgekeurd door de founder (8 nov).
import re, json, html
from blogbuild import build, hero, cards
from opknap_en import md, faq as en_faq, src as en_src
src20 = open('build_blog_okt20.py', encoding='utf-8').read()
exec(src20[src20.index("N = 'https"):src20.index('def pair(')])  # N, B, ONCLICK, crisis, nl_faq, nl_src
exec(open('blog_tekst_nov8.py', encoding='utf-8').read())
DATE, NL_DATE, EN_DATE = '2026-11-08', '8 november 2026', '8 November 2026'

def h1(path):  # kaarttekst uit de bestaande pagina
    return html.unescape(re.search(r'<h1>(.*?)</h1>', open(path, encoding='utf-8').read()).group(1))
def rel(items, lang):
    return [((N if lang == 'nl' else B) + slug if lang == 'en' else '/nl/blog/' + slug, cat, h1(('nl/blog/' if lang == 'nl' else 'blog/') + slug + '.html')) for slug, cat in items]
def mins(t): return max(5, round(len(t.split()) / 200))

def pair(nl_slug, en_slug, nl, en):
    href = (f'<link rel="alternate" hreflang="nl" href="{N}{nl_slug}"/>\n<link rel="alternate" hreflang="en" href="{B}{en_slug}"/>\n'
            f'<link rel="alternate" hreflang="x-default" href="{B}{en_slug}"/>')
    title, desc, head, crumb, cat, lead, body, faqs, sources, cta, related = nl
    fh, fld = nl_faq(faqs)
    build('nl/blog/goksites-blokkeren.html', f'nl/blog/{nl_slug}.html', 'nl', N + nl_slug, title, desc, head, crumb,
          'https://afterbetting.com/nl/', 'https://afterbetting.com/nl/blog',
          hero('/nl/', '/nl/blog', 'Home', cat, head, lead, f'Door Afterbetting &middot; {NL_DATE} &middot; {mins(body)} min lezen'),
          md(body) + fh + nl_src(sources),
          f'<div class="cta-block"><h3>{cta[0]}</h3><p>{cta[1]}</p><a href="https://app.afterbetting.com/onboarding" {ONCLICK}>Begin gratis</a></div>',
          cards(['Meer lezen'] + rel(related, 'nl')), NL_CRISIS, href, DATE, fld)
    title, desc, head, crumb, cat, lead, body, faqs, sources, cta, related = en
    fh, fld = en_faq(faqs)
    build('blog/block-gambling-sites-and-payments.html', f'blog/{en_slug}.html', 'en', B + en_slug, title, desc, head, crumb,
          'https://afterbetting.com', 'https://afterbetting.com/blog',
          hero('https://afterbetting.com', 'https://afterbetting.com/blog', 'Home', cat, head, lead, f'By Afterbetting &middot; {EN_DATE} &middot; {mins(body)} min read'),
          md(body) + fh + en_src(sources),
          f'<div class="cta"><h3>{cta[0]}</h3><p>{cta[1]}</p><a href="https://app.afterbetting.com/onboarding" {ONCLICK}>Start free</a></div>',
          cards(['Continue reading'] + rel(related, 'en')), EN_CRISIS, href, DATE, fld)


pair('stoppen-met-gokken-app', 'quit-gambling-app',
     ('Stoppen met gokken app: welke helpt echt? Eerlijk overzicht',
      'Blokkeer-apps, Cruks en herstel-apps: wat elk soort app doet, wat niet, en hoe je ze combineert. Van iemand die 8 jaar gokte.',
      'Stoppen met gokken app: welke helpt echt?', 'Stoppen met gokken app', 'Stoppen',
      'Blokkeer-apps, de gokstop en herstel-apps: wat elk doet, wat niet, en hoe je ze combineert.', NL_D, NL_D_FAQ,
      [('Cruks, landelijk register gokverslaving', 'https://cruks.nl/'), ('BetBlocker', 'https://www.betblocker.org/'), ('Gamban', 'https://gamban.com/')],
      ('Begin met je eerste dag', 'Afterbetting is gratis: een dagenteller, Nu hulp bij drang, gewoontes voor je risico-uren en je geld in beeld. Geen betaalgegevens nodig.'),
      [('goksites-blokkeren', 'Blokkeren'), ('zelfuitsluiting-gokken-werkt-het', 'Cruks'), ('waarom-kan-ik-niet-stoppen-met-gokken', 'Stoppen'), ('drang-om-te-gokken', 'Drang')]),
     ('Quit gambling app: which ones actually help? An honest guide',
      "Blockers, self-exclusion and recovery apps: what each kind of app does, what it doesn't, and how to combine them. From a former gambler.",
      'Quit gambling app: which ones actually help?', 'Quit gambling app', 'Quitting',
      "Blockers, self-exclusion and recovery apps: what each does, what it doesn't, and how to combine them.", EN_D, EN_D_FAQ,
      [('GamStop', 'https://www.gamstop.co.uk/'), ('BetBlocker', 'https://www.betblocker.org/'), ('Gamban', 'https://gamban.com/')],
      ('Start with your first day', 'Afterbetting is free: a day counter, Help now for urges, habits for your risky hours and your money in view. No card needed.'),
      [('block-gambling-sites-and-payments', 'Blocking'), ('does-self-exclusion-work-gambling', 'Self-exclusion'), ('why-cant-i-stop-gambling', 'Quitting'), ('do-gambling-urges-go-away', 'Urges')]))
print('gebouwd')

LINKS = [
 ('nl/blog/goksites-blokkeren.html', '/nl/blog/stoppen-met-gokken-app', 'Stoppen met gokken app: welke helpt echt?', 'Lees ook'),
 ('nl/blog/zelfuitsluiting-gokken-werkt-het.html', '/nl/blog/stoppen-met-gokken-app', 'Stoppen met gokken app: welke helpt echt?', 'Lees ook'),
 ('nl/blog/stoppen-met-gokken.html', '/nl/blog/stoppen-met-gokken-app', 'Stoppen met gokken app: welke helpt echt?', 'Lees ook'),
 ('nl/blog/eerste-week-stoppen-met-gokken.html', '/nl/blog/stoppen-met-gokken-app', 'Stoppen met gokken app: welke helpt echt?', 'Lees ook'),
 ('blog/block-gambling-sites-and-payments.html', B + 'quit-gambling-app', 'Quit gambling app: which ones actually help?', 'Read next'),
 ('blog/does-self-exclusion-work-gambling.html', B + 'quit-gambling-app', 'Quit gambling app: which ones actually help?', 'Read next'),
 ('blog/how-to-stop-gambling.html', B + 'quit-gambling-app', 'Quit gambling app: which ones actually help?', 'Read next'),
 ('blog/first-week-without-gambling.html', B + 'quit-gambling-app', 'Quit gambling app: which ones actually help?', 'Read next'),
]
for p, href, text, label in LINKS:
    s = open(p, encoding='utf-8').read()
    if href.split('/')[-1] + '"' in s: continue
    m = re.search(r'<div class="(cta-block|cta)">', s) or re.search(r'<aside class="author-box">', s)
    s = s[:m.start()] + f'<p><strong>{label}:</strong> <a href="{href}">{text}</a></p>\n' + s[m.start():]
    s = re.sub(r'"dateModified": ?"[^"]+"', f'"dateModified": "{DATE}"', s)
    open(p, 'w', encoding='utf-8').write(s)
    print('link toegevoegd:', p)
