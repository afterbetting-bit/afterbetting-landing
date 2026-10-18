# 18 okt 2026: auteursblok onder elk artikel met link naar de Over-pagina (E-E-A-T). Alleen bevestigde founder-feiten.
import glob
NL = ('<aside class="author-box"><strong>Geschreven door de oprichter van Afterbetting</strong>'
      '<span>Begon op zijn 16e met gokken, gokte 8 jaar, vooral op sport, en bouwde ruim 40.000 euro schuld op. '
      'Betaalde alles terug in bijna twee jaar en is ruim twee jaar gestopt. Bouwde Afterbetting met 27, als het hulpmiddel dat hij toen miste. '
      '<a href="https://afterbetting.com/nl/about">Lees zijn verhaal</a>.</span></aside>\n')
EN = ('<aside class="author-box"><strong>Written by the founder of Afterbetting</strong>'
      '<span>Started gambling at 16, gambled for 8 years, mostly on sports, and ran up more than €40,000 in debt. '
      'Paid it all back in almost two years and has been gambling-free for more than two years. Built Afterbetting at 27, as the tool he was missing back then. '
      '<a href="https://afterbetting.com/about">Read his story</a>.</span></aside>\n')
CSS = ('\n/* Auteursblok onder artikelen (18 okt 2026) */\n'
       '.author-box{display:block;border-top:1px solid var(--border);margin:2.5rem 0 0;padding:1.25rem 0 0}\n'
       '.author-box strong{display:block;font-size:.95rem;color:var(--ink);margin-bottom:.35rem}\n'
       '.author-box span{display:block;font-size:.9rem;line-height:1.6;color:var(--mid)}\n')
n = 0
for f in glob.glob('blog/*.html') + glob.glob('nl/blog/*.html'):
    if f.endswith('index.html'): continue
    s = open(f, encoding='utf-8').read()
    if 'class="author-box"' in s or '<article class="body">' not in s: continue
    a = s.index('<article class="body">'); b = s.index('</article>', a)
    s = s[:b] + (NL if f.startswith('nl/') else EN) + s[b:]
    open(f, 'w', encoding='utf-8').write(s); n += 1
th = open('theme.css', encoding='utf-8').read()
if '.author-box{' not in th: open('theme.css', 'a', encoding='utf-8').write(CSS)
print('auteursblok op', n, "pagina's")
