# 31 okt 2026: alle aanmeldlinks op een blogpagina krijgen hetzelfde thema (t=), berekend zoals tag_app_links.py.
# Pagina's gebouwd op het sjabloon goksites-blokkeren erfden t=blok in navigatie en balk. Daarna balktekst opnieuw.
import glob, re
src = open('tag_app_links.py', encoding='utf-8').read(); ns = {}
exec(src[:src.index('n = 0')], ns)
n = 0
for f in glob.glob('blog/*.html') + glob.glob('nl/blog/*.html'):
    if f.endswith('index.html'): continue
    th = ns['theme'](f.split('/')[-1][:-5])
    s = open(f, encoding='utf-8').read()
    s2 = re.sub(r'(onboarding\?van=blog&(?:amp;)?t=)[a-z]+', r'\g<1>' + th, s)
    if s2 != s:
        open(f, 'w', encoding='utf-8').write(s2); n += 1; print(f, '->', th)
print('aangepast:', n)
