import re, glob
B = 'https://afterbetting.com'
PAIRS = [('terugval-na-gokverslaving', 'what-to-do-after-gambling-relapse'),
 ('dagelijkse-gewoonten-na-gokverslaving', 'daily-habits-that-replace-gambling'),
 ('slaapproblemen-stoppen-met-gokken', 'sleep-after-stopping-gambling'),
 ('sportgokken-verslaving', 'sports-betting-addiction-quit'),
 ('zelfuitsluiting-gokken-werkt-het', 'does-self-exclusion-work-gambling'),
 ('sneeuwbalmethode-gokschulden', 'snowball-debt-payoff-gambling'),
 ('hoe-vul-ik-mijn-tijd-zonder-gokken', 'what-to-do-instead-of-gambling'),
 ('gokverslaving-en-identiteit', 'gambling-addiction-identity-loss'),
 ('gokken-aan-je-familie-vertellen', 'how-to-tell-family-about-gambling-problem')]
SOLO = ['gokschuld-aflossen', 'gokverslaving-herkennen', 'hoe-stop-ik-met-gokken-met-schulden', 'stoppen-met-gokken']
TAG = re.compile(r'[ \t]*<link[^>]*hreflang[^>]*>\n?')

def setlinks(f, own, links):
    s = open(f, encoding='utf-8').read()
    c = re.findall(r'<link rel="canonical" href="([^"]+)"/>', s)
    assert c == [own], f'{f}: canonical {c}'
    s = TAG.sub('', s)
    new = ''.join(f'<link rel="alternate" hreflang="{l}" href="{u}"/>\n' for l, u in links)
    m = re.search(r'<link rel="canonical" href="[^"]+"/>\n', s)
    assert m, f'{f}: geen canonical-regel met newline'
    return s[:m.end()] + new + s[m.end():]

out = {}
for nl, en in PAIRS:
    N, E = f'{B}/nl/blog/{nl}', f'{B}/blog/{en}'
    L = [('nl', N), ('en', E), ('x-default', E)]
    out[f'nl/blog/{nl}.html'] = setlinks(f'nl/blog/{nl}.html', N, L)
    out[f'blog/{en}.html'] = setlinks(f'blog/{en}.html', E, L)
for nl in SOLO:
    N = f'{B}/nl/blog/{nl}'
    out[f'nl/blog/{nl}.html'] = setlinks(f'nl/blog/{nl}.html', N, [('nl', N), ('x-default', N)])
L = [('nl', f'{B}/nl/blog'), ('en', f'{B}/blog'), ('x-default', f'{B}/blog')]
out['nl/blog/index.html'] = setlinks('nl/blog/index.html', f'{B}/nl/blog', L)
out['blog/index.html'] = setlinks('blog/index.html', f'{B}/blog', L)
for f, s in out.items():
    open(f, 'w', encoding='utf-8').write(s)

def f2u(f):
    if f == 'index.html': return B
    if f.endswith('/index.html'): return B + '/' + f[:-11]
    return B + '/' + f[:-5]
H = {}
for f in glob.glob('**/*.html', recursive=True):
    s = open(f, encoding='utf-8').read()
    H[f2u(f).rstrip('/')] = [(re.search(r'hreflang="([^"]+)"', t).group(1), re.search(r'href="([^"]+)"', t).group(1))
                             for t in re.findall(r'<link[^>]*hreflang[^>]*>', s)]
sm = open('sitemap.xml', encoding='utf-8').read()
miss = []
def fix(m):
    blk = m.group(0)
    loc = re.search(r'<loc>([^<]+)</loc>', blk).group(1).rstrip('/')
    if loc not in H: miss.append(loc); return blk
    blk = re.sub(r'[ \t]*<xhtml:link[^>]*>\n', '', blk)
    links = ''.join(f'    <xhtml:link rel="alternate" hreflang="{l}" href="{u}"/>\n' for l, u in H[loc])
    return blk.replace('  </url>', links + '  </url>')
sm2, n = re.subn(r'  <url>\n.*?  </url>', fix, sm, flags=re.S)
assert n == 58 and not miss, f'urls {n}, geen html voor {miss}'
open('sitemap.xml', 'w', encoding='utf-8').write(sm2)
print('html aangepast:', len(out), '| sitemap urls:', n)
