# Gedeelde bouwstenen voor het herschrijven van bestaande EN-blogpagina's (opknaprondes).
import json, re, os
from blogbuild import build, hero, cards
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

