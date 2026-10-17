# Opknapronde 3 (11 okt 2026): geldartikelen.
# - rebuild-finances-after-gambling wordt de EN-hoofdpagina over gokschuld, paar met nl/blog/gokschuld-aflossen
# - debt-free-after-gambling samengevoegd (301) in rebuild-finances
# - snowball-debt-payoff-gambling wordt "snowball of avalanche", avalanche-debt-payoff-gambling samengevoegd (301)
# - nl/blog/gokschuld-aflossen: onjuiste of onbewijsbare zinnen aangepast, hreflang naar EN
import json, os, re
from opknap_en import page, B
exec(open('blog_teksten_opknap_r3.py', encoding='utf-8').read())
NLU = 'https://afterbetting.com/nl/blog/'

def set_href(path, nl_slug, en_slug):
    s = open(path, encoding='utf-8').read()
    s = re.sub(r'<link rel="alternate" hreflang="[^"]+" href="[^"]+"/?>\n?', '', s)
    h = (f'<link rel="alternate" hreflang="nl" href="{NLU}{nl_slug}"/>\n<link rel="alternate" hreflang="en" href="{B}{en_slug}"/>\n'
         f'<link rel="alternate" hreflang="x-default" href="{B}{en_slug}"/>\n')
    s = s.replace('<meta property="og:type"', h + '<meta property="og:type"', 1)
    assert s.count('hreflang="x-default"') == 1, path
    open(path, 'w', encoding='utf-8').write(s)

# eerst hreflang op de oude EN-pagina zetten, zodat page() die overneemt
set_href('blog/rebuild-finances-after-gambling.html', 'gokschuld-aflossen', 'rebuild-finances-after-gambling')

page('rebuild-finances-after-gambling', 'How to pay off gambling debt and rebuild your finances',
     'A step-by-step plan to pay off gambling debt: stop the leak, face the real number, free debt advice and Breathing Space. From someone with 40k in debt.',
     'How to pay off gambling debt and rebuild your finances', 'Pay off gambling debt', 'Money',
     'From the shapeless dread to a list you can work on. One step at a time.', 9, FINANCES, FINANCES_FAQ, FINANCES_SOURCES,
     ('Your debts, going down', 'See your debts next to your days free, and watch the line go down month by month. Start free.'),
     [(B + 'snowball-debt-payoff-gambling', 'Money', 'Snowball or avalanche for gambling debt?'),
      (B + 'gambled-away-paycheck-what-now', 'Crisis', 'Just gambled away my paycheck. What now?'),
      (B + 'block-gambling-sites-and-payments', 'Tools', 'How to block gambling sites, apps and bank payments'),
      (B + 'how-to-tell-family-about-gambling-problem', 'Support', 'How to tell someone you have a gambling problem')])

page('snowball-debt-payoff-gambling', 'Snowball or avalanche for gambling debt?',
     'Snowball or avalanche: which way to pay off gambling debt? Both methods explained, one worked example and how to choose the one you will stick to.',
     'Snowball or avalanche: which way to pay off gambling debt?', 'Snowball or avalanche', 'Money',
     'Smallest debt first, or highest interest first. One example, both ways.', 8, SNOWBALL, SNOWBALL_FAQ, SNOWBALL_SOURCES,
     ('Watch the snowball roll', 'Add your debts, choose your order and see each one disappear. Start free.'),
     [(B + 'rebuild-finances-after-gambling', 'Money', 'How to pay off gambling debt and rebuild your finances'),
      (B + 'gambled-away-paycheck-what-now', 'Crisis', 'Just gambled away my paycheck. What now?'),
      (B + 'block-gambling-sites-and-payments', 'Tools', 'How to block gambling sites, apps and bank payments'),
      (B + 'what-to-do-after-gambling-relapse', 'Relapse', 'What to do right after a gambling relapse')])

# NL gokschuld-aflossen: correcties en hreflang
p = 'nl/blog/gokschuld-aflossen.html'
s = open(p, encoding='utf-8').read()
FIX = [
 ('<p>In Nederland heeft 1 op de 5 huishoudens te maken met problematische schulden. Daar zijn structuren voor. Gratis. Officieel. Geen oplichters.</p>',
  '<p>Je bent niet de enige, en er is hulp voor. Gratis. Officieel. Geen oplichters.</p>'),
 ('<p>Voor zwaardere gevallen. Drie jaar leven van een minimumbedrag, daarna ben je schuldenvrij. Streng, maar werkt. Je gemeente kan je hierin begeleiden.</p>',
  '<p>Voor zwaardere gevallen, via de rechter. Je leeft een vaste periode van een beperkt bedrag en daarna kunnen de resterende schulden vervallen. Streng, maar het werkt. Je gemeente kan je hierin begeleiden.</p>'),
 ('<p>Niet één persoon in de geschiedenis van gokverslavingen heeft ooit "één keer gegokt om snel schulden af te lossen" en het laten lukken. Nul. Niemand.</p>',
  '<p>Ik had meer dan 40.000 euro schuld en ken die gedachte goed. Wat hem voor mij brak: als ik het terugwon, zou ik het weer vergokken. Terugwinnen was geen oplossing. Het was de inzet voor de volgende keer.</p>'),
 ('<p>Dat. Doet. Niemand.</p>', '<p>Doe het niet.</p>'),
 ('Omdat je hersenen pieken nodig hebben. Een schuld zien verdwijnen is een legale, gezonde piek.',
  'Omdat je dan snel een hele schuld ziet verdwijnen, en dat helpt om vol te houden.'),
]
for a, b in FIX:
    if a in s: s = s.replace(a, b)
s = re.sub(r'"dateModified": ?"[^"]+"', '"dateModified": "2026-10-11"', s)
open(p, 'w', encoding='utf-8').write(s)
set_href(p, 'gokschuld-aflossen', 'rebuild-finances-after-gambling')
assert 'Nul. Niemand' not in open(p, encoding='utf-8').read()

# Samenvoegen met 301
MERGE = [('debt-free-after-gambling', 'rebuild-finances-after-gambling'), ('avalanche-debt-payoff-gambling', 'snowball-debt-payoff-gambling')]
vj = json.load(open('vercel.json', encoding='utf-8'))
sm = open('sitemap.xml', encoding='utf-8').read()
for old, new in MERGE:
    if os.path.exists(f'blog/{old}.html'): os.remove(f'blog/{old}.html')
    if not any(r.get('source') == f'/blog/{old}' for r in vj['redirects']):
        vj['redirects'].insert(1, {"source": f"/blog/{old}", "destination": f"/blog/{new}", "permanent": True})
    sm = re.sub(r'  <url>\s*<loc>https://afterbetting.com/blog/' + old + r'</loc>[\s\S]*?</url>\n', '', sm)
open('vercel.json', 'w', encoding='utf-8').write(json.dumps(vj, indent=2, ensure_ascii=False) + '\n')

# sitemap: rebuild-finances en gokschuld-aflossen als paar
def entry(loc):
    return (f'  <url>\n    <loc>{loc}</loc>\n    <lastmod>2026-10-11</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.7</priority>\n'
            f'    <xhtml:link rel="alternate" hreflang="nl" href="{NLU}gokschuld-aflossen"/>\n    <xhtml:link rel="alternate" hreflang="en" href="{B}rebuild-finances-after-gambling"/>\n'
            f'    <xhtml:link rel="alternate" hreflang="x-default" href="{B}rebuild-finances-after-gambling"/>\n  </url>\n')
for loc in (NLU + 'gokschuld-aflossen', B + 'rebuild-finances-after-gambling'):
    m = re.search(r'  <url>\s*<loc>' + re.escape(loc) + r'</loc>[\s\S]*?</url>\n', sm)
    sm = sm.replace(m.group(0), entry(loc)) if m else sm.replace('</urlset>', entry(loc) + '</urlset>')
open('sitemap.xml', 'w', encoding='utf-8').write(sm)

# interne links en blogindex
n = 0
for root, _, files in os.walk('.'):
    if root.startswith(('./.git', './node_modules')): continue
    for f in files:
        if not f.endswith('.html'): continue
        p = os.path.join(root, f); s = open(p, encoding='utf-8').read(); s2 = s
        for old, new in MERGE:
            if old not in s2: continue
            s2 = re.sub(r'<a href="[^"]*/blog/' + old + r'"[^>]*class="card"[\s\S]*?</a>', '', s2)
            s2 = s2.replace(f'/blog/{old}', f'/blog/{new}')
        if s2 != s: open(p, 'w', encoding='utf-8').write(s2); n += 1
print('interne links aangepast in', n, 'bestanden')

# blogindex: ItemList ontdubbelen en kaarten/titels bijwerken
p = 'blog/index.html'; s = open(p, encoding='utf-8').read()
m = re.search(r'<script type="application/ld\+json">(\{[^<]*"ItemList"[^<]*\})</script>', s)
d = json.loads(m.group(1)); lst = d['itemListElement']; seen = set(); new = []
for it in lst:
    if it['url'] in seen: continue
    seen.add(it['url']); new.append(it)
for i, it in enumerate(new, 1): it['position'] = i
for it in new:
    if it['url'].endswith('rebuild-finances-after-gambling'): it['name'] = 'How to pay off gambling debt and rebuild your finances'
    if it['url'].endswith('snowball-debt-payoff-gambling'): it['name'] = 'Snowball or avalanche for gambling debt?'
d['itemListElement'] = new
s = s.replace(m.group(1), json.dumps(d, ensure_ascii=False, separators=(',', ':')))
open(p, 'w', encoding='utf-8').write(s)
print('blogindex:', len(lst), '->', len(new), 'items')
