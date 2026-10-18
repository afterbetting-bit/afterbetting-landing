# 18 okt 2026: Over-pagina NL en EN herschreven met alleen door de founder bevestigde feiten (content/about_*.md).
import re, json
from opknap_en import md
STATS = {
 'nl': [('2+', 'Jaar gestopt met gokken'), ('&euro;40K+', 'Schuld afgelost in bijna twee jaar'), ('0', 'Investeerders of reclame')],
 'en': [('2+', 'Years gambling-free'), ('&euro;40K+', 'Debt paid off in almost two years'), ('0', 'Investors or ads')],
}
for lang, f in (('nl', 'nl/about.html'), ('en', 'about.html')):
    t = open(f'content/about_{lang}.md', encoding='utf-8').read()
    title = re.search(r'^Title \(\d+\): (.+)$', t, re.M).group(1).strip()
    desc = re.search(r'^Meta \(\d+\): (.+)$', t, re.M).group(1).strip()
    h1 = re.search(r'^# (.+)$', t, re.M).group(1).strip()
    rest = t[t.index('\n', t.index('\n# ') + 1) + 1:].strip()
    lead, body = rest.split('\n\n', 1)
    assert len(title) <= 60 and len(desc) <= 155, (f, len(title), len(desc))
    s = open(f, encoding='utf-8').read()
    old_t = re.search(r'<title>([^<]*)</title>', s).group(1)
    old_d = re.search(r'name="description" content="([^"]*)"', s).group(1)
    s = s.replace(old_t, title).replace(old_d, desc)
    s = re.sub(r'("@type":"AboutPage"[^}]*?"description":")[^"]*(")', lambda m: m.group(1) + desc + m.group(2), s, count=1)
    a = s.index('<h1>'); b = s.index('</h1>', a) + 5
    s = s[:a] + f'<h1>{h1}</h1>' + s[b:]
    pa = s.index('<p', s.index('</h1>')); pb = s.index('</p>', pa) + 4
    s = s[:pa] + f'<p style="font-size:1.1rem;color:var(--mid);font-weight:300;line-height:1.7;margin-top:1rem">{lead}</p>' + s[pb:]
    stats = '<div class="stat-row">\n' + ''.join(f'<div class="stat"><div class="n">{n}</div><div class="l">{l}</div></div>\n' for n, l in STATS[lang]) + '</div>\n'
    html = md(body).replace('info@afterbetting.com', '<a href="mailto:info@afterbetting.com">info@afterbetting.com</a>')
    ba = s.index('<div class="body">') + len('<div class="body">'); bb = s.index('<div class="cta">', ba)
    s = s[:ba] + '\n\n' + stats + '\n' + html + '\n' + s[bb:]
    s = re.sub(r'(<meta property="og:description" content=")[^"]*(")', lambda m: m.group(1) + desc + m.group(2), s, count=1)
    assert '—' not in s and s.count('<h1>') == 1
    for blk in re.findall(r'<script type="application/ld\+json">([\s\S]*?)</script>', s): json.loads(blk)
    open(f, 'w', encoding='utf-8').write(s)
    print(f, len(title), len(desc), len(re.sub(r'<[^>]+>', ' ', html).split()), 'woorden')
