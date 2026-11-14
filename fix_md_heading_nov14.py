# 14 nov 2026: losse markdown-kop ("<p># Titel</p>") weg uit artikelen. Die dubbelde de H1 als zichtbare tekst.
import glob, re
n = 0
for f in glob.glob('blog/*.html') + glob.glob('nl/blog/*.html'):
    s = open(f, encoding='utf-8').read()
    t = re.sub(r'\n?<p>#{1,3} [^<]*</p>', '', s)
    if t != s:
        open(f, 'w', encoding='utf-8').write(t); n += 1; print('fix', f)
print('aangepast', n)
