# Helpers voor opknapronde 5 (17 okt 2026): bestaande pagina herschrijven met behoud van URL, hreflang en datePublished.
import json, re
from blogbuild import build, hero, cards
from opknap_en import md as en_md, faq as en_faq, src as en_src, CRISIS as EN_CRISIS
DATE = '2026-10-17'
NL_CRISIS = '<div class="crisis-footer"><p>Zit je nu in crisis? Bel <strong>OpenOverGokken: 0800-2400022</strong>. Gratis, anoniem, 24 uur per dag. Denk je aan zelfmoord? Bel <strong>113</strong> (0800-0113).</p></div>'
ONCLICK = 'onclick="if(window.gtag)gtag(\'event\',\'cta_click\',{cta_location:\'article_cta\',page_path:location.pathname})"'

def nl_faq(items):
    html = '<h2>Veelgestelde vragen</h2>\n' + ''.join(f'<h3>{q}</h3>\n<p>{a}</p>\n' for q, a in items)
    ld = '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}, ensure_ascii=False) + '</script>\n'
    return html, ld

def _keep(path):
    old = open(path, encoding='utf-8').read()
    pub = re.search(r'"datePublished": ?"([^"]+)"', old); pub = pub.group(1) if pub else DATE
    href = '\n'.join(re.findall(r'<link rel="alternate" hreflang="[^"]+" href="[^"]+"/?>', old))
    return pub, href

def _fix_pub(path, pub):
    s = open(path, encoding='utf-8').read()
    s = s.replace(f'"datePublished": "{DATE}"', f'"datePublished": "{pub}"', 1)
    open(path, 'w', encoding='utf-8').write(s)

def nl_page(slug, title, desc, h1, crumb, cat, lead, mins, body, faqs, sources, cta, related, href=None):
    path = f'nl/blog/{slug}.html'; url = f'https://afterbetting.com/nl/blog/{slug}'
    pub, old_href = _keep(path); href = href or old_href
    assert 'x-default' in href, path
    fh, fld = nl_faq(faqs)
    srcs = '<h2>Bronnen</h2>\n<ul>' + ''.join(f'<li><a href="{u}" rel="noopener">{t}</a></li>' for t, u in sources) + '</ul>\n' if sources else ''
    build('nl/blog/goksites-blokkeren.html', path, 'nl', url, title, desc, h1, crumb, 'https://afterbetting.com/nl/', 'https://afterbetting.com/nl/blog',
          hero('/nl/', '/nl/blog', 'Home', cat, h1, lead, f'Door de oprichter van Afterbetting &middot; bijgewerkt 17 oktober 2026 &middot; {mins} min lezen'),
          en_md(body).replace('<strong>From the founder:</strong>', '<strong>Van de oprichter:</strong>') + fh + srcs,
          f'<div class="cta-block"><h3>{cta[0]}</h3><p>{cta[1]}</p><a href="https://app.afterbetting.com/onboarding" {ONCLICK}>Begin gratis</a></div>',
          cards(['Meer lezen'] + related), NL_CRISIS, href, DATE, fld)
    _fix_pub(path, pub)

def en_page(slug, title, desc, h1, crumb, cat, lead, mins, body, faqs, sources, cta, related, href=None):
    path = f'blog/{slug}.html'; url = f'https://afterbetting.com/blog/{slug}'
    pub, old_href = _keep(path); href = href or old_href
    if 'x-default' not in href:
        href = f'<link rel="alternate" hreflang="en" href="{url}"/>\n<link rel="alternate" hreflang="x-default" href="{url}"/>'
    fh, fld = en_faq(faqs)
    build('blog/block-gambling-sites-and-payments.html', path, 'en', url, title, desc, h1, crumb, 'https://afterbetting.com', 'https://afterbetting.com/blog',
          hero('https://afterbetting.com', 'https://afterbetting.com/blog', 'Home', cat, h1, lead, f'By the founder of Afterbetting &middot; updated 17 October 2026 &middot; {mins} min read'),
          en_md(body) + fh + en_src(sources),
          f'<div class="cta"><h3>{cta[0]}</h3><p>{cta[1]}</p><a href="https://app.afterbetting.com/onboarding" {ONCLICK}>Start free</a></div>',
          cards(['Continue reading'] + related), EN_CRISIS, href, DATE, fld)
    _fix_pub(path, pub)
