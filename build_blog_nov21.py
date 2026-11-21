# Bouwt de artikelen van 21 nov 2026 (founder: "Plaats alle teksten!").
# EN-only: is-kalshi-gambling, is-trading-gambling, student-gambling-addiction.
# Paren: feestdagen-zonder-gokken / gambling-over-christmas, gokreclame-blokkeren / stop-gambling-emails-and-ads.
# Daarna: blogindexen, sitemap, inkomende links. Nabewerking via de bestaande idempotente scripts.
import re, html, json
from blogbuild import build, hero, cards
from opknap_en import md, faq as en_faq, src as en_src
src20 = open('build_blog_okt20.py', encoding='utf-8').read()
exec(src20[src20.index("N = 'https"):src20.index('def pair(')])  # N, B, ONCLICK, NL_CRISIS, EN_CRISIS, nl_faq, nl_src
exec(open('blog_tekst_nov21_en.py', encoding='utf-8').read())
exec(open('blog_tekst_nov21_paren.py', encoding='utf-8').read())
DATE, NL_DATE, EN_DATE = '2026-11-21', '21 november 2026', '21 November 2026'

CARD_EN = ('<div class="app-card"><div class="app-card-screen"><span class="app-card-label">Help now, one tap away</span><p class="app-card-quote">"{q}"</p>'
           '<div class="app-card-timer">15:00</div><p class="app-card-meta">A timer, your own reason to stop, a message to someone you trust and the helpline.</p></div>'
           '<a class="app-card-btn" href="https://app.afterbetting.com/onboarding?van=blog&t=drang" rel="noopener" onclick="if(window.gtag)gtag(\'event\',\'cta_click\',{{cta_location:\'app_card\',cta_theme:\'drang\',page_path:location.pathname}})">Try Help now free</a>'
           '<p class="app-card-note">Example. Afterbetting\'s basics are free, no card needed.</p></div>')
CARD_NL = ('<div class="app-card"><div class="app-card-screen"><span class="app-card-label">Nu hulp, met één tik</span><p class="app-card-quote">"{q}"</p>'
           '<div class="app-card-timer">15:00</div><p class="app-card-meta">Een timer, je eigen reden om te stoppen, een bericht aan je vertrouwenspersoon en de hulplijn.</p></div>'
           '<a class="app-card-btn" href="https://app.afterbetting.com/onboarding?van=blog&t=drang" rel="noopener" onclick="if(window.gtag)gtag(\'event\',\'cta_click\',{{cta_location:\'app_card\',cta_theme:\'drang\',page_path:location.pathname}})">Probeer Nu hulp gratis</a>'
           '<p class="app-card-note">Voorbeeld. De basis van Afterbetting is gratis, zonder betaalgegevens.</p></div>')

def body_html(lang, answer, text, quote):
    box = (f'<div class="answer-box" id="kort-antwoord"><h2>Het korte antwoord</h2><p>{answer}</p></div>\n' if lang == 'nl'
           else f'<div class="answer-box" id="short-answer"><h2>The short answer</h2><p>{answer}</p></div>\n')
    h = md(text)
    assert h.count('<p>APPCARD</p>') == 1
    return box + h.replace('<p>APPCARD</p>', (CARD_NL if lang == 'nl' else CARD_EN).format(q=quote))

def h1(path):
    return html.unescape(re.search(r'<h1>(.*?)</h1>', open(path, encoding='utf-8').read()).group(1))
def rel(items, lang):
    if lang == 'nl':
        return [('/nl/blog/' + s, c, h1('nl/blog/' + s + '.html')) for s, c in items]
    return [(B + s, c, h1('blog/' + s + '.html')) for s, c in items]
def mins(t): return max(5, round(len(t.split()) / 200))

def page(lang, slug, href, title, desc, head, crumb, cat, lead, answer, text, quote, faqs, sources, cta, related):
    body = body_html(lang, answer, text, quote)
    if lang == 'nl':
        fh, fld = nl_faq(faqs)
        build('nl/blog/goksites-blokkeren.html', f'nl/blog/{slug}.html', 'nl', N + slug, title, desc, head, crumb,
              'https://afterbetting.com/nl/', 'https://afterbetting.com/nl/blog',
              hero('/nl/', '/nl/blog', 'Home', cat, head, lead, f'Door Afterbetting &middot; {NL_DATE} &middot; {mins(text)} min lezen'),
              body + fh + nl_src(sources),
              f'<div class="cta-block"><h3>{cta[0]}</h3><p>{cta[1]}</p><a href="https://app.afterbetting.com/onboarding" {ONCLICK}>Begin gratis</a></div>',
              cards(['Meer lezen'] + rel(related, 'nl')), NL_CRISIS, href, DATE, fld)
    else:
        fh, fld = en_faq(faqs)
        build('blog/block-gambling-sites-and-payments.html', f'blog/{slug}.html', 'en', B + slug, title, desc, head, crumb,
              'https://afterbetting.com', 'https://afterbetting.com/blog',
              hero('https://afterbetting.com', 'https://afterbetting.com/blog', 'Home', cat, head, lead, f'By Afterbetting &middot; {EN_DATE} &middot; {mins(text)} min read'),
              body + fh + en_src(sources),
              f'<div class="cta"><h3>{cta[0]}</h3><p>{cta[1]}</p><a href="https://app.afterbetting.com/onboarding" {ONCLICK}>Start free</a></div>',
              cards(['Continue reading'] + rel(related, 'en')), EN_CRISIS, href, DATE, fld)

def en_only(slug):
    return f'<link rel="alternate" hreflang="en" href="{B}{slug}"/>\n<link rel="alternate" hreflang="x-default" href="{B}{slug}"/>'
def pair_href(nl, en):
    return (f'<link rel="alternate" hreflang="nl" href="{N}{nl}"/>\n<link rel="alternate" hreflang="en" href="{B}{en}"/>\n'
            f'<link rel="alternate" hreflang="x-default" href="{B}{en}"/>')

CTA_EN = ('Quitting is more than blocking', 'Afterbetting helps with the rest: a day counter, habits for your risky hours, your money and debt in view, and Help now when the urge hits. Free.')
CTA_NL = ('Stoppen is meer dan blokkeren', 'Afterbetting helpt met de rest: een dagenteller, gewoontes voor je risico-uren, je geld en schuld in beeld en Nu hulp bij drang. Gratis.')

PAGES = [
 ('en', 'is-kalshi-gambling', en_only('is-kalshi-gambling'),
  'Is Kalshi Gambling? An Honest Answer From a Former Bettor',
  'Is Kalshi gambling? If you bet on outcomes, it works like a sportsbook. What that means if you are quitting, and how to self-exclude and block it.',
  'Is Kalshi gambling? An honest answer from a former bettor', 'Is Kalshi gambling', 'Sports',
  'Kalshi and Polymarket call it trading. If you are trying to quit sports betting, here is what that means for you.',
  KALSHI_ANSWER, KALSHI, 'You excluded from the sportsbooks for a reason. The urge passes.', KALSHI_FAQ, KALSHI_SRC, CTA_EN,
  [('sports-betting-addiction-quit', 'Sports'), ('block-gambling-sites-and-payments', 'Blocking'), ('does-self-exclusion-work-gambling', 'Self-exclusion'), ('what-to-do-after-gambling-relapse', 'Relapse')]),
 ('en', 'is-trading-gambling', en_only('is-trading-gambling'),
  'Is Day Trading Gambling? When Trading Becomes a Problem',
  'Is day trading gambling? Not by definition, but leverage, fast options and 24/7 crypto can work exactly like it. Signs, and what to do if it has.',
  'Is day trading gambling? When trading becomes a problem', 'Is trading gambling', 'Money',
  'Trading is not gambling by definition. But it can work exactly like it. How to tell, and what to do.',
  TRADING_ANSWER, TRADING, 'Close the app. The market will be there tomorrow. The urge will not.', TRADING_FAQ, TRADING_SRC, CTA_EN,
  [('chasing-losses-gambling', 'Money'), ('how-much-have-i-lost-gambling', 'Money'), ('gambling-addiction-symptoms-and-signs', 'Signs'), ('rebuild-finances-after-gambling', 'Money')]),
 ('en', 'student-gambling-addiction', en_only('student-gambling-addiction'),
  'Student Gambling Addiction: Signs, Numbers and Help',
  'Student gambling addiction: how common it is at university, the signs, and what to do this week. From someone who gambled from 16 to 24.',
  'Student gambling addiction: signs, numbers and where to get help', 'Student gambling', 'Signs',
  'Gambling is common at university. When it stops being a night out and starts running your life.',
  STUDENT_ANSWER, STUDENT, 'Your loan is for rent, not for the next match. The urge passes.', STUDENT_FAQ, STUDENT_SRC, CTA_EN,
  [('gambling-addiction-test', 'Test'), ('block-gambling-sites-and-payments', 'Blocking'), ('how-to-tell-family-about-gambling-problem', 'Support'), ('rebuild-finances-after-gambling', 'Money')]),
 ('nl', 'feestdagen-zonder-gokken', pair_href('feestdagen-zonder-gokken', 'gambling-over-christmas'),
  'Feestdagen zonder gokken: zo kom je december door',
  'De feestdagen zijn een trigger voor wie stopt met gokken: extra geld, vrije dagen, familie, eenzaamheid. Zo plan je december zonder gokken.',
  'Feestdagen zonder gokken: zo kom je december door', 'Feestdagen zonder gokken', 'Drang',
  'Extra geld, vrije dagen, familie en soms eenzaamheid. Hoe je de lastigste weken van het jaar plant.',
  KERST_NL_ANSWER, KERST_NL, 'De feestdagen zijn zwaar. Dat betekent niet dat je moet gokken. De drang zakt.', KERST_NL_FAQ, KERST_NL_SRC, CTA_NL,
  [('drang-om-te-gokken', 'Drang'), ('goksites-blokkeren', 'Blokkeren'), ('terugval-na-gokverslaving', 'Terugval'), ('gokken-en-alcohol', 'Alcohol')]),
 ('en', 'gambling-over-christmas', pair_href('feestdagen-zonder-gokken', 'gambling-over-christmas'),
  'Gambling Over Christmas: How to Get Through the Holidays',
  'Christmas is a trigger when you are quitting gambling: extra money, days off, family, loneliness, football. How to plan the holidays without betting.',
  'Gambling over Christmas: how to get through the holidays', 'Gambling over Christmas', 'Urges',
  'Extra money, days off, family and sometimes loneliness. How to plan the hardest weeks of the year.',
  KERST_EN_ANSWER, KERST_EN, 'Christmas is hard. That does not mean you have to bet. The urge passes.', KERST_EN_FAQ, KERST_EN_SRC, CTA_EN,
  [('do-gambling-urges-go-away', 'Urges'), ('block-gambling-sites-and-payments', 'Blocking'), ('what-to-do-after-gambling-relapse', 'Relapse'), ('gambling-and-alcohol', 'Alcohol')]),
 ('nl', 'gokreclame-blokkeren', pair_href('gokreclame-blokkeren', 'stop-gambling-emails-and-ads'),
  'Gokreclame blokkeren: mails, sms en advertenties stoppen',
  'Gokreclame blokkeren in 7 stappen: uitschrijven, bezwaar via de AVG, afzenders blokkeren en gokadvertenties uitzetten bij Google en YouTube.',
  'Gokreclame blokkeren: mails, sms en advertenties stoppen', 'Gokreclame blokkeren', 'Blokkeren',
  'Je bent gestopt, maar de bonusmails blijven komen. Zo stop je zoveel mogelijk.',
  RECLAME_NL_ANSWER, RECLAME_NL, 'Een bonus is geen gratis geld. Het is een uitnodiging om terug te komen. De drang zakt.', RECLAME_NL_FAQ, RECLAME_NL_SRC, CTA_NL,
  [('goksites-blokkeren', 'Blokkeren'), ('zelfuitsluiting-gokken-werkt-het', 'Cruks'), ('cruks-omzeilen-wat-nu', 'Cruks'), ('drang-om-te-gokken', 'Drang')]),
 ('en', 'stop-gambling-emails-and-ads', pair_href('gokreclame-blokkeren', 'stop-gambling-emails-and-ads'),
  'How to Stop Gambling Emails, Texts and Ads',
  'How to stop gambling emails, texts and ads in 7 steps: unsubscribe, object to marketing, block senders, forward to 7726 and turn off ads on Google.',
  'How to stop gambling emails, texts and ads', 'Stop gambling emails and ads', 'Blocking',
  'You stopped, but the bonus emails keep coming. How to stop as much of it as you can.',
  RECLAME_EN_ANSWER, RECLAME_EN, 'A bonus is not free money. It is an invitation to come back. The urge passes.', RECLAME_EN_FAQ, RECLAME_EN_SRC, CTA_EN,
  [('block-gambling-sites-and-payments', 'Blocking'), ('does-self-exclusion-work-gambling', 'Self-exclusion'), ('casino-not-on-gamstop', 'Crisis'), ('do-gambling-urges-go-away', 'Urges')]),
]
for p in PAGES:
    page(*p)

# Blogindexen
EN_IDX = [(p[1], p[7], p[8]) for p in PAGES if p[0] == 'en']
NL_IDX = [(p[1], p[7], p[8]) for p in PAGES if p[0] == 'nl']
s = open('blog/index.html', encoding='utf-8').read()
add = ''.join(f'<a href="{B}{slug}" class="card"><div class="card-body"><div class="t">{cat}</div><h2>{h1(f"blog/{slug}.html")}</h2><p>{lead}</p><div class="rm">Read article &rarr;</div></div></a>'
              for slug, cat, lead in EN_IDX if f'{B}{slug}"' not in s)
s = s.replace('<div class="grid">\n', '<div class="grid">\n' + add, 1)
open('blog/index.html', 'w', encoding='utf-8').write(s)
s = open('nl/blog/index.html', encoding='utf-8').read()
add = ''.join(f'<a href="/nl/blog/{slug}" class="blog-card">\n<div class="cat">{cat}</div>\n<h2>{h1(f"nl/blog/{slug}.html")}</h2>\n<p>{lead}</p>\n<div class="meta">{NL_DATE} &middot; 7 min lezen</div>\n</a>'
              for slug, cat, lead in NL_IDX if f'/nl/blog/{slug}"' not in s)
s = s.replace('<div class="blog-grid">', '<div class="blog-grid">' + add, 1)
open('nl/blog/index.html', 'w', encoding='utf-8').write(s)

# Sitemap
s = open('sitemap.xml', encoding='utf-8').read()
block = ''
for p in PAGES:
    url = (N if p[0] == 'nl' else B) + p[1]
    if f'<loc>{url}</loc>' in s: continue
    alts = ''.join(f'\n    <xhtml:link rel="alternate" hreflang="{l}" href="{h}"/>' for l, h in re.findall(r'hreflang="([^"]+)" href="([^"]+)"', p[2]))
    block += f'\n  <url>\n    <loc>{url}</loc>\n    <lastmod>{DATE}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.7</priority>{alts}\n  </url>'
s = s.replace('\n</urlset>', block + '\n</urlset>')
open('sitemap.xml', 'w', encoding='utf-8').write(s)

# Inkomende links
LINKS = [
 ('blog/sports-betting-addiction-quit.html', B + 'is-kalshi-gambling', 'Is Kalshi gambling? An honest answer from a former bettor', 'Read next'),
 ('blog/does-self-exclusion-work-gambling.html', B + 'is-kalshi-gambling', 'Is Kalshi gambling? An honest answer from a former bettor', 'Also read'),
 ('blog/block-gambling-sites-and-payments.html', B + 'stop-gambling-emails-and-ads', 'How to stop gambling emails, texts and ads', 'Also read'),
 ('blog/chasing-losses-gambling.html', B + 'is-trading-gambling', 'Is day trading gambling?', 'Also read'),
 ('blog/how-much-have-i-lost-gambling.html', B + 'is-trading-gambling', 'Is day trading gambling?', 'Also read'),
 ('blog/gambling-addiction-test.html', B + 'student-gambling-addiction', 'Student gambling addiction: signs, numbers and help', 'Also read'),
 ('blog/gambling-addiction-symptoms-and-signs.html', B + 'student-gambling-addiction', 'Student gambling addiction: signs, numbers and help', 'Also read'),
 ('blog/do-gambling-urges-go-away.html', B + 'gambling-over-christmas', 'Gambling over Christmas: how to get through the holidays', 'Also read'),
 ('blog/how-to-stop-gambling.html', B + 'gambling-over-christmas', 'Gambling over Christmas: how to get through the holidays', 'Also read'),
 ('nl/blog/drang-om-te-gokken.html', '/nl/blog/feestdagen-zonder-gokken', 'Feestdagen zonder gokken: zo kom je december door', 'Lees ook'),
 ('nl/blog/stoppen-met-gokken.html', '/nl/blog/feestdagen-zonder-gokken', 'Feestdagen zonder gokken: zo kom je december door', 'Lees ook'),
 ('nl/blog/goksites-blokkeren.html', '/nl/blog/gokreclame-blokkeren', 'Gokreclame blokkeren: mails, sms en advertenties stoppen', 'Lees ook'),
 ('nl/blog/zelfuitsluiting-gokken-werkt-het.html', '/nl/blog/gokreclame-blokkeren', 'Gokreclame blokkeren: mails, sms en advertenties stoppen', 'Lees ook'),
]
for p, href, text, label in LINKS:
    s = open(p, encoding='utf-8').read()
    if href.split('/')[-1] + '"' in s: continue
    m = re.search(r'<div class="(cta-block|cta)">', s) or re.search(r'<aside class="author-box">', s)
    s = s[:m.start()] + f'<p><strong>{label}:</strong> <a href="{href}">{text}</a></p>\n' + s[m.start():]
    s = re.sub(r'"dateModified": ?"[^"]+"', f'"dateModified": "{DATE}"', s)
    open(p, 'w', encoding='utf-8').write(s)
    print('link toegevoegd:', p)
