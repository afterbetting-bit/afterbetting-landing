# 31 okt 2026: bronnen onderaan het artikel, klein en rustig. Ze stonden als grote h2 + lijst vlak boven de aanmeldknop.
# Nieuw: <aside class="sources"> als laatste blok in het artikel (na knop en auteursblok). Lege lijsten gaan weg.
# Veilig om opnieuw te draaien.
import glob, re
LABEL = {'en': 'Sources', 'nl': 'Bronnen'}
CSS = ('\n/* Bronnen onderaan artikelen, klein (31 okt 2026) */\n'
       'article .sources{margin:2rem 0 0;padding-top:1rem;border-top:1px solid var(--border)}\n'
       'article .sources-label{font-size:.72rem;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:var(--mid);opacity:.75;margin:0 0 .4rem}\n'
       'article .sources ul{margin:0;padding-left:1.1rem}\n'
       'article .sources li{font-size:.8rem;line-height:1.5;color:var(--mid);margin:.15rem 0}\n'
       'article .sources a{color:var(--mid) !important;text-decoration-color:var(--border) !important;text-decoration-thickness:1px !important;text-underline-offset:2px}\n')
moved = removed = 0
for f in glob.glob('blog/*.html') + glob.glob('nl/blog/*.html'):
    s = open(f, encoding='utf-8').read()
    m = re.search(r'<h2>(Sources|Bronnen)</h2>\s*(<ul>.*?</ul>)\s*', s, re.S)
    if not m: continue
    lang = 'nl' if f.startswith('nl/') else 'en'
    ul = m.group(2)
    s = s[:m.start()] + s[m.end():]
    if re.search(r'<li', ul):
        a = s.index('<article class="body">'); b = s.index('</article>', a)
        s = s[:b] + f'<aside class="sources"><p class="sources-label">{LABEL[lang]}</p>{ul}</aside>\n' + s[b:]
        moved += 1
    else:
        removed += 1
    assert '—' not in s
    open(f, 'w', encoding='utf-8').write(s)
th = open('theme.css', encoding='utf-8').read()
if 'article .sources{' not in th: open('theme.css', 'a', encoding='utf-8').write(CSS)
print('verplaatst:', moved, 'lege lijst weg:', removed)
