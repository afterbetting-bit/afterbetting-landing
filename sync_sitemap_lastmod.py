# Zet <lastmod> in sitemap.xml gelijk aan de nieuwste dateModified van elke pagina (18 okt 2026). Veilig om na elke ronde te draaien.
import re, os
sm = open('sitemap.xml', encoding='utf-8').read()
n = 0
def fix(m):
    global n
    loc, lm = m.group(1), m.group(2)
    p = loc.replace('https://afterbetting.com', '').strip('/') or 'index'
    f = p + '.html' if os.path.exists(p + '.html') else p + '/index.html'
    if not os.path.exists(f): return m.group(0)
    dm = re.findall(r'"dateModified": ?"([0-9]{4}-[0-9]{2}-[0-9]{2})"', open(f, encoding='utf-8').read())
    if dm and max(dm) > lm:
        n += 1; return m.group(0).replace(f'<lastmod>{lm}</lastmod>', f'<lastmod>{max(dm)}</lastmod>')
    return m.group(0)
sm = re.sub(r'<loc>([^<]+)</loc>\s*<lastmod>([^<]+)</lastmod>', fix, sm)
open('sitemap.xml', 'w', encoding='utf-8').write(sm)
print('lastmod bijgewerkt:', n)
