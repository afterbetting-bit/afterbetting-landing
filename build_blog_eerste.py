# Bouwt nl/blog/eerste-30-dagen-zonder-gokken en blog/first-week-without-gambling (11 okt 2026)
# en zet de hreflang-paren goed: eerste-30-dagen <-> first-30-days, eerste-week <-> first-week.
import json, re
from blogbuild import build, hero, cards
from opknap_en import md, faq as en_faq, src as en_src
exec(open('blog_tekst_eerste.py', encoding='utf-8').read())
NLB, ENB = 'https://afterbetting.com/nl/blog/', 'https://afterbetting.com/blog/'
PAIRS = [('eerste-30-dagen-zonder-gokken', 'first-30-days-without-gambling'), ('eerste-week-stoppen-met-gokken', 'first-week-without-gambling')]
ONCLICK = 'onclick="if(window.gtag)gtag(\'event\',\'cta_click\',{cta_location:\'article_cta\',page_path:location.pathname})"'
NL_CRISIS = '<div class="crisis-footer"><p>Zit je nu in crisis? Bel <strong>OpenOverGokken: 0800-2400022</strong>. Gratis, anoniem, 24 uur per dag. Denk je aan zelfmoord? Bel <strong>113</strong> (0800-0113).</p></div>'
EN_CRISIS = '<div class="crisis-footer"><p>In crisis right now? In the UK, call the <strong>National Gambling Helpline (GamCare) on 0808 8020 133</strong>, free, 24/7. In the Netherlands: <strong>OpenOverGokken 0800-2400022</strong>. Thinking about suicide? Call <strong>Samaritans on 116 123</strong>.</p></div>'

def href(nl, en):
    return (f'<link rel="alternate" hreflang="nl" href="{NLB}{nl}"/>\n<link rel="alternate" hreflang="en" href="{ENB}{en}"/>\n'
            f'<link rel="alternate" hreflang="x-default" href="{ENB}{en}"/>')

def nl_faq(items):
    html = '<h2>Veelgestelde vragen</h2>\n' + ''.join(f'<h3>{q}</h3>\n<p>{a}</p>\n' for q, a in items)
    ld = '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}, ensure_ascii=False) + '</script>\n'
    return html, ld

fh, fld = nl_faq(NL30_FAQ)
build('nl/blog/goksites-blokkeren.html', 'nl/blog/eerste-30-dagen-zonder-gokken.html', 'nl', NLB + PAIRS[0][0],
      'Eerste 30 dagen zonder gokken: week voor week',
      'De eerste 30 dagen zonder gokken, week voor week: wat je kunt verwachten, wat normaal is en wat helpt. Eerlijk, uit eigen ervaring.',
      'De eerste 30 dagen zonder gokken, week voor week', 'Eerste 30 dagen', 'https://afterbetting.com/nl/', 'https://afterbetting.com/nl/blog',
      hero('/nl/', '/nl/blog', 'Home', 'Herstel', 'De eerste 30 dagen zonder gokken, week voor week',
           'Wat je kunt verwachten in je eerste maand, en wat helpt. Zonder het mooier te maken dan het is.', 'Door Afterbetting &middot; 11 oktober 2026 &middot; 7 min lezen'),
      md(NL30) + fh + '<h2>Bronnen</h2>\n<ul>' + ''.join(f'<li><a href="{u}" rel="noopener">{t}</a></li>' for t, u in SOURCES_NL) + '</ul>\n',
      f'<div class="cta-block"><h3>Je eerste maand, dag voor dag</h3><p>Je dagen vrij, kleine gewoonten en hulp met één tik als de drang komt. Gratis te beginnen.</p><a href="https://app.afterbetting.com/onboarding" {ONCLICK}>Begin gratis</a></div>',
      cards(['Meer lezen', ('/nl/blog/eerste-week-stoppen-met-gokken', 'Herstel', 'Eerste week stoppen met gokken'),
             ('/nl/blog/drang-om-te-gokken', 'Drang', 'Drang om te gokken: wat je nu doet'),
             ('/nl/blog/hoe-vul-ik-mijn-tijd-zonder-gokken', 'Gewoonten', 'Hoe vul je je tijd zonder gokken?'),
             ('/nl/blog/hoe-lang-duurt-herstel-gokverslaving', 'Herstel', 'Hoe lang duurt herstel van gokverslaving?')]),
      NL_CRISIS, href(*PAIRS[0]), '2026-10-11', fld)

efh, efld = en_faq(EN7_FAQ)
build('blog/block-gambling-sites-and-payments.html', 'blog/first-week-without-gambling.html', 'en', ENB + PAIRS[1][1],
      'Your first week without gambling: day by day',
      'What the first week without gambling is like, day by day: the restlessness, the first real urge, the emptiness, and what helps on each day.',
      'Your first week without gambling, day by day', 'First week without gambling', 'https://afterbetting.com', 'https://afterbetting.com/blog',
      hero('https://afterbetting.com', 'https://afterbetting.com/blog', 'Home', 'Recovery', 'Your first week without gambling, day by day',
           'What you might run into, what is normal, and what to do on each day.', 'By Afterbetting &middot; 11 October 2026 &middot; 7 min read'),
      md(EN7) + efh + en_src(SOURCES_EN),
      f'<div class="cta"><h3>Get through this week</h3><p>A day counter, small habits and help one tap away when the urge comes. Start free.</p><a href="https://app.afterbetting.com/onboarding" {ONCLICK}>Start free</a></div>',
      cards(['Continue reading', ('https://afterbetting.com/blog/first-30-days-without-gambling', 'Recovery', 'First 30 days without gambling: an honest week by week'),
             ('https://afterbetting.com/blog/do-gambling-urges-go-away', 'Urges', 'Do gambling urges go away? What helps right now'),
             ('https://afterbetting.com/blog/block-gambling-sites-and-payments', 'Tools', 'How to block gambling sites, apps and bank payments'),
             ('https://afterbetting.com/blog/what-to-do-instead-of-gambling', 'Habits', 'What to do instead of gambling')]),
      EN_CRISIS, href(*PAIRS[1]), '2026-10-11', efld)

# bestaande pagina's: hreflang naar hun nieuwe paar
for path, (nl, en) in (('blog/first-30-days-without-gambling.html', PAIRS[0]), ('nl/blog/eerste-week-stoppen-met-gokken.html', PAIRS[1])):
    s = open(path, encoding='utf-8').read()
    first = s.index('<link rel="alternate" hreflang=')
    s = re.sub(r'<link rel="alternate" hreflang="[^"]+" href="[^"]+"\s*/?>\n?', '', s)
    s = s[:first] + href(nl, en) + '\n' + s[first:]
    assert s.count('hreflang="x-default"') == 1
    open(path, 'w', encoding='utf-8').write(s)

# sitemap: alle vier de URL's met het juiste paar
sm = open('sitemap.xml', encoding='utf-8').read()
def entry(loc, nl, en):
    return (f'  <url>\n    <loc>{loc}</loc>\n    <lastmod>2026-10-11</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.7</priority>\n'
            f'    <xhtml:link rel="alternate" hreflang="nl" href="{NLB}{nl}"/>\n    <xhtml:link rel="alternate" hreflang="en" href="{ENB}{en}"/>\n'
            f'    <xhtml:link rel="alternate" hreflang="x-default" href="{ENB}{en}"/>\n  </url>\n')
for nl, en in PAIRS:
    for loc in (NLB + nl, ENB + en):
        m = re.search(r'  <url>\s*<loc>' + re.escape(loc) + r'</loc>[\s\S]*?</url>\n', sm)
        sm = sm.replace(m.group(0), entry(loc, nl, en)) if m else sm.replace('</urlset>', entry(loc, nl, en) + '</urlset>')
open('sitemap.xml', 'w', encoding='utf-8').write(sm)
print('hreflang en sitemap bijgewerkt')
