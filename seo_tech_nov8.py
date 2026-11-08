# 8 nov 2026: technische SEO-ronde. Geen tekstwijzigingen in artikelen.
# 1. og:locale op pagina's waar het ontbrak (EN: en_GB, zelfde als de rest).
# 2. Article-schema compleet: description, image, url, mainEntityOfPage, inLanguage,
#    publisher-logo, dateModified (gelijk aan datePublished als het ontbrak),
#    auteur als Person die verwijst naar de Over-pagina (sluit aan op het auteursblok).
# 3. Interne links naar gokken-en-alcohol / gambling-and-alcohol (hadden er 2).
# Veilig om opnieuw te draaien.
import glob, json, re

BASE = 'https://afterbetting.com'
LOGO = {'@type': 'ImageObject', 'url': BASE + '/apple-touch-icon.png'}
n_loc = n_schema = n_link = 0

def url_of(f):
    p = f[:-5]
    if p.endswith('/index'): p = p[:-5]
    if p == 'index': p = ''
    return BASE + '/' + p

files = ['index.html'] + glob.glob('blog/*.html') + glob.glob('nl/blog/*.html')
for f in files:
    s = open(f, encoding='utf-8').read(); o = s
    nl = f.startswith('nl/')
    if 'og:locale' not in s:
        loc = '<meta property="og:locale" content="nl_NL"/><meta property="og:locale:alternate" content="nl_BE"/>' if nl else '<meta property="og:locale" content="en_GB"/>'
        s = re.sub(r'(<meta property="og:type" content="[^"]*" ?/>)', lambda m: m.group(1) + loc, s, count=1)
        if s != o: n_loc += 1
    if f.endswith('index.html'):
        if s != o: open(f, 'w', encoding='utf-8').write(s)
        continue
    m = re.search(r'<meta name="description" content="([^"]*)"', s)
    desc = m.group(1) if m else ''
    u = url_of(f)
    def fix(mm):
        global n_schema
        j = json.loads(mm.group(1))
        if j.get('@type') != 'Article': return mm.group(0)
        j['description'] = j.get('description') or desc
        j['image'] = j.get('image') or BASE + '/og-image.png'
        j['url'] = u
        j['mainEntityOfPage'] = {'@type': 'WebPage', '@id': u}
        j['inLanguage'] = 'nl' if nl else 'en'
        j['dateModified'] = j.get('dateModified') or j.get('datePublished')
        j['author'] = {'@type': 'Person',
                       'name': 'Oprichter van Afterbetting' if nl else 'Founder of Afterbetting',
                       'url': BASE + ('/nl/about' if nl else '/about')}
        j['publisher'] = {'@type': 'Organization', 'name': 'Afterbetting', 'url': BASE, 'logo': LOGO}
        new = '<script type="application/ld+json">' + json.dumps(j, ensure_ascii=False) + '</script>'
        if new != mm.group(0): n_schema += 1
        return new
    s = re.sub(r'<script type="application/ld\+json">(.*?)</script>', fix, s, flags=re.S)
    if s != o: open(f, 'w', encoding='utf-8').write(s)

LINKS = {
    'blog/how-to-stop-gambling-urges-weekends.html': ('Also read:', BASE + '/blog/gambling-and-alcohol', 'Gambling and alcohol'),
    'blog/what-to-do-after-gambling-relapse.html': ('Also read:', BASE + '/blog/gambling-and-alcohol', 'Gambling and alcohol'),
    'nl/blog/terugval-na-gokverslaving.html': ('Lees ook:', BASE + '/nl/blog/gokken-en-alcohol', 'Gokken en alcohol'),
    'nl/blog/eerste-week-stoppen-met-gokken.html': ('Lees ook:', BASE + '/nl/blog/gokken-en-alcohol', 'Gokken en alcohol'),
}
for f, (label, href, text) in LINKS.items():
    s = open(f, encoding='utf-8').read()
    if href + '"' in s: continue
    m = re.search(r'<p><strong>' + re.escape(label) + r'</strong>(.*?)</p>', s, flags=re.S)
    if not m: print('geen', label, 'in', f); continue
    inner = m.group(1).rstrip()
    end = '.' if inner.endswith('.') else ''
    inner = inner[:-1] if end else inner
    new = '<p><strong>' + label + '</strong>' + inner + ' · <a href="' + href + '">' + text + '</a>' + end + '</p>'
    s = s[:m.start()] + new + s[m.end():]
    open(f, 'w', encoding='utf-8').write(s); n_link += 1

print('og:locale', n_loc, '| schema', n_schema, '| links', n_link)
