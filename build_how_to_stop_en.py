# Bouwt de EN-pijler /blog/how-to-stop-gambling (19 okt 2026), tekst in content/stoppen_en.md (founder akkoord).
# Koppelt hreflang met nl/blog/stoppen-met-gokken, dat tot nu toe geen EN-tegenhanger had.
import re, json, html as H
from blogbuild import build, hero, cards
from opknap_en import md, inline
src = open('build_blog_okt18c.py', encoding='utf-8').read()
exec(src[src.index('src = open'):src.index('# ---------- rekenhulp')])   # ONCLICK, EN_CRISIS, parse, faq_block, B, N

NU = N + 'stoppen-met-gokken'; EU = B + 'how-to-stop-gambling'
HREF = (f'<link rel="alternate" hreflang="nl" href="{NU}"/>\n<link rel="alternate" hreflang="en" href="{EU}"/>\n'
        f'<link rel="alternate" hreflang="x-default" href="{EU}"/>')

title, desc, h1, body, fh, items = parse('content/stoppen_en.md')
assert len(title) <= 60 and len(desc) <= 155, (len(title), len(desc))
body = body.replace(' {#first-24-hours}', '')
bh = md(body).replace('<h2>Your first 24 hours</h2>', '<h2 id="first-24-hours">Your first 24 hours</h2>', 1)
assert 'id="first-24-hours"' in bh
fvis, fld = faq_block(fh, items)
hr = hero('https://afterbetting.com', 'https://afterbetting.com/blog', 'Home', 'Quitting', h1,
          'What actually works when willpower is not enough. From someone who gambled for 8 years and stopped.',
          'By the founder of Afterbetting &middot; 19 October 2026 &middot; 10 min read')
cta = (f'<div class="cta"><h3>Something for the hours in between</h3><p>A day counter, habits for the hours you used to gamble, '
       f'a money overview and Help now when the urge hits. Start free.</p><a href="https://app.afterbetting.com/onboarding" {ONCLICK}>Start free</a></div>')
rel = [(B + 'first-week-without-gambling', 'Recovery', 'Your first week without gambling'),
       (B + 'block-gambling-sites-and-payments', 'Tools', 'How to block gambling sites and payments'),
       (B + 'where-to-get-help-gambling-addiction', 'Support', 'Where to get help for gambling addiction'),
       (B + 'gambling-addiction-test', 'Self-test', 'Gambling addiction test')]
build('blog/block-gambling-sites-and-payments.html', 'blog/how-to-stop-gambling.html', 'en', EU, title, desc, h1, 'How to stop gambling',
      'https://afterbetting.com', 'https://afterbetting.com/blog', hr, bh + fvis, cta, cards(['Continue reading'] + rel), EN_CRISIS, HREF, '2026-10-19', fld)

# NL-pijler: hreflang naar de nieuwe EN-pagina
p = 'nl/blog/stoppen-met-gokken.html'; s = open(p, encoding='utf-8').read()
assert 'hreflang="en"' not in s
s = re.sub(r'(<link rel="alternate" hreflang="[^"]+" href="[^"]+"/?>\n?)+', HREF + '\n', s, count=1)
assert s.count('hreflang="en"') == 1 and s.count('hreflang="x-default"') == 1
open(p, 'w', encoding='utf-8').write(s); print('ok')
