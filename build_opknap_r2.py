# Opknapronde 2 (11 okt 2026): drie EN-pagina's herschreven, what-to-expect samengevoegd in how-long-gambling-recovery-takes.
import json, re, os
from blogbuild import build, hero, cards
exec(open('blog_teksten_opknap_r2.py', encoding='utf-8').read())
TEMPLATE = 'blog/block-gambling-sites-and-payments.html'
CRISIS = ('<div class="crisis-footer"><p>In crisis right now? In the UK, call the <strong>National Gambling Helpline (GamCare) on 0808 8020 133</strong>, free, 24/7. '
          'In the Netherlands: <strong>OpenOverGokken 0800-2400022</strong>. Thinking about suicide? Call <strong>Samaritans on 116 123</strong>.</p></div>')
CTA = ('<div class="cta"><h3>{}</h3><p>{}</p><a href="https://app.afterbetting.com/onboarding" '
       'onclick="if(window.gtag)gtag(\'event\',\'cta_click\',{{cta_location:\'article_cta\',page_path:location.pathname}})">Start free</a></div>')
B = 'https://afterbetting.com/blog/'

def inline(t):
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    return re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', t)

def md(src):
    out = []
    for block in src.strip().split('\n\n'):
        lines = block.strip().split('\n')
        if lines[0].startswith('### '): out.append(f'<h3>{inline(lines[0][4:])}</h3>'); continue
        if lines[0].startswith('## '): out.append(f'<h2>{inline(lines[0][3:])}</h2>'); continue
        if all(l.startswith('> ') for l in lines):
            out.append('<div class="callout"><p><strong>From the founder:</strong> ' + inline(' '.join(l[2:] for l in lines)) + '</p></div>'); continue
        if all(l.startswith('- ') for l in lines):
            out.append('<ul>' + ''.join(f'<li>{inline(l[2:])}</li>' for l in lines) + '</ul>'); continue
        if all(re.match(r'\d+\. ', l) for l in lines):
            out.append('<ol>' + ''.join(f'<li>{inline(re.sub(r"^\d+\. ", "", l))}</li>' for l in lines) + '</ol>'); continue
        out.append('<p>' + inline(' '.join(lines)) + '</p>')
    return '\n'.join(out) + '\n'

def faq(items):
    html = '<h2>Frequently asked questions</h2>\n' + ''.join(f'<h3>{q}</h3>\n<p>{a}</p>\n' for q, a in items)
    ld = '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}, ensure_ascii=False) + '</script>\n'
    return html, ld

def src(items):
    return '<h2>Sources</h2>\n<ul>' + ''.join(f'<li><a href="{u}" rel="noopener">{t}</a></li>' for t, u in items) + '</ul>\n' if items else ''

def page(slug, title, desc, h1, crumb, cat, lead, mins, body, faqs, sources, cta, related):
    path = f'blog/{slug}.html'; url = B + slug
    old = open(path, encoding='utf-8').read()
    published = re.search(r'"datePublished": ?"([^"]+)"', old).group(1)
    href = '\n'.join(re.findall(r'<link rel="alternate" hreflang="[^"]+" href="[^"]+"/?>', old))
    if 'x-default' not in href:
        href = f'<link rel="alternate" hreflang="en" href="{url}"/>\n<link rel="alternate" hreflang="x-default" href="{url}"/>'
    fh, fld = faq(faqs)
    build(TEMPLATE, path, 'en', url, title, desc, h1, crumb, 'https://afterbetting.com', 'https://afterbetting.com/blog',
          hero('https://afterbetting.com', 'https://afterbetting.com/blog', 'Home', cat, h1, lead, f'By Afterbetting &middot; updated 11 October 2026 &middot; {mins} min read'),
          md(body) + fh + src(sources), CTA.format(*cta), cards(['Continue reading'] + related), CRISIS, href, '2026-10-11', fld)
    s = open(path, encoding='utf-8').read()
    s = s.replace('"datePublished": "2026-10-11"', f'"datePublished": "{published}"', 1)
    assert 'â€' not in s
    open(path, 'w', encoding='utf-8').write(s)

page('what-to-do-after-gambling-relapse', 'What to do right after a gambling relapse',
     'Gambled again after stopping? What to do in the first hour, the first day and the first week, how to tell your family and when to get more help.',
     'What to do right after a gambling relapse', 'Gambling relapse', 'Relapse',
     'The next hour, the next day and the next week. Not how bad you should feel.', 8, RELAPSE, RELAPSE_FAQ, RELAPSE_SOURCES,
     ('Start again without the shame', 'Set a new start date in a few taps. Your journal, habits and money overview stay as they were.'),
     [(B + 'casino-not-on-gamstop', 'Crisis', 'Found a casino not on GamStop? Read this first'),
      (B + 'block-gambling-sites-and-payments', 'Tools', 'How to block gambling sites, apps and bank payments'),
      (B + 'how-to-tell-family-about-gambling-problem', 'Support', 'How to tell someone you have a gambling problem'),
      (B + 'how-long-gambling-recovery-takes', 'Recovery', 'How long does gambling recovery take?')])

page('sleep-after-stopping-gambling', "Can't sleep after quitting gambling? What helps",
     "Can't sleep since you stopped gambling? Why the nights are hard, what helps from tonight, and when to see your GP. From someone who went through it.",
     "Can't sleep after quitting gambling? What helps", 'Sleep after quitting gambling', 'Recovery',
     'Why the nights are hard after stopping, and what you can change from tonight.', 7, SLEEP, SLEEP_FAQ, SLEEP_SOURCES,
     ('Your evenings, with a plan', 'Set an evening wind-down habit and a daily check-in. Help is one tap away when the urge comes at night.'),
     [(B + 'how-to-stop-gambling-urges-weekends', 'Urges', 'How to stop gambling urges at the weekend'),
      (B + 'what-to-do-instead-of-gambling', 'Habits', 'What to do instead of gambling'),
      (B + 'rebuild-finances-after-gambling', 'Money', 'Rebuilding your finances after gambling'),
      (B + 'how-long-gambling-recovery-takes', 'Recovery', 'How long does gambling recovery take?')])

page('gambling-addiction-identity-loss', 'Who am I without gambling? Identity after quitting',
     'Feeling empty after you stopped gambling? Why gambling becomes part of who you are, and four places to start rebuilding. From a former sports bettor.',
     'Who are you without gambling?', 'Identity after gambling', 'Recovery',
     'Why stopping can leave you feeling empty, and how you start building someone new.', 8, IDENTITY, IDENTITY_FAQ, IDENTITY_SOURCES,
     ('Build it one day at a time', 'Habits, a daily check-in and a journal. The small things you repeat become who you are.'),
     [(B + 'daily-habits-that-replace-gambling', 'Habits', 'Daily habits that replace gambling'),
      (B + 'what-to-do-instead-of-gambling', 'Habits', 'What to do instead of gambling'),
      (B + 'how-to-tell-family-about-gambling-problem', 'Support', 'How to tell someone you have a gambling problem'),
      (B + 'how-long-gambling-recovery-takes', 'Recovery', 'How long does gambling recovery take?')])

# what-to-expect overlapt met how-long-gambling-recovery-takes: samenvoegen met een 301
OLD, NEW = 'gambling-recovery-what-to-expect', 'how-long-gambling-recovery-takes'
if os.path.exists(f'blog/{OLD}.html'):
    os.remove(f'blog/{OLD}.html')
vj = json.load(open('vercel.json', encoding='utf-8'))
if not any(r.get('source') == f'/blog/{OLD}' for r in vj['redirects']):
    vj['redirects'].insert(1, {"source": f"/blog/{OLD}", "destination": f"/blog/{NEW}", "permanent": True})
    open('vercel.json', 'w', encoding='utf-8').write(json.dumps(vj, indent=2, ensure_ascii=False) + '\n')
sm = open('sitemap.xml', encoding='utf-8').read()
sm = re.sub(r'  <url>\s*<loc>https://afterbetting.com/blog/' + OLD + r'</loc>[\s\S]*?</url>\n', '', sm)
open('sitemap.xml', 'w', encoding='utf-8').write(sm)
n = 0
for root, _, files in os.walk('.'):
    if root.startswith(('./.git', './node_modules')): continue
    for f in files:
        if not f.endswith('.html'): continue
        p = os.path.join(root, f); s = open(p, encoding='utf-8').read()
        if OLD not in s: continue
        # kaart in de blogindex weghalen, anders de link omzetten
        s2 = re.sub(r'<a href="[^"]*' + OLD + r'"[^>]*class="card"[\s\S]*?</a>', '', s)
        s2 = s2.replace(f'/blog/{OLD}', f'/blog/{NEW}')
        if s2 != s: open(p, 'w', encoding='utf-8').write(s2); n += 1
print('links naar', OLD, 'aangepast in', n, 'bestanden')
