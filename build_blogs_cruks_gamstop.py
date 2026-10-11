# Bouwt twee artikelen (11 okt 2026): NL cruks-opzeggen en EN cancel-gamstop-early, met hreflang naar elkaar.
# Gebruikt een bestaand artikel per taal als sjabloon (CSS, nav, footer, sticky balk, theme.css) zodat alles gelijk blijft.
import json, re

DATE = '2026-10-11'
NL_URL = 'https://afterbetting.com/nl/blog/cruks-opzeggen'
EN_URL = 'https://afterbetting.com/blog/cancel-gamstop-early'
HREFLANG = (f'<link rel="alternate" hreflang="nl" href="{NL_URL}"/>\n'
            f'<link rel="alternate" hreflang="en" href="{EN_URL}"/>\n'
            f'<link rel="alternate" hreflang="x-default" href="{EN_URL}"/>')

def head(lang, url, title, desc, headline, crumb, home, blog):
    art = json.dumps({"@context": "https://schema.org", "@type": "Article", "headline": headline,
                      "author": {"@type": "Organization", "name": "Afterbetting"},
                      "publisher": {"@type": "Organization", "name": "Afterbetting", "url": "https://afterbetting.com"},
                      "datePublished": DATE, "dateModified": DATE, "inLanguage": lang, "url": url}, ensure_ascii=False)
    bc = json.dumps({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": home},
        {"@type": "ListItem", "position": 2, "name": "Blog", "item": blog},
        {"@type": "ListItem", "position": 3, "name": crumb, "item": url}]}, ensure_ascii=False)
    loc = '<meta property="og:locale" content="nl_NL"/>\n<meta property="og:locale:alternate" content="nl_BE"/>' if lang == 'nl' else '<meta property="og:locale" content="en_GB"/>'
    return (f'<title>{title}</title>\n<meta name="description" content="{desc}"/>\n<meta name="robots" content="index,follow"/>\n'
            f'<link rel="canonical" href="{url}"/>\n{HREFLANG}\n<meta property="og:type" content="article"/>\n{loc}\n'
            f'<meta property="og:url" content="{url}"/>\n<meta property="og:title" content="{title}"/>\n<meta property="og:description" content="{desc}"/>\n'
            f'<meta property="og:image" content="https://afterbetting.com/og-image.png"/>\n<meta name="twitter:card" content="summary_large_image"/>\n'
            f'<meta name="twitter:title" content="{title}"/>\n<meta name="twitter:description" content="{desc}"/>\n'
            f'<meta name="twitter:image" content="https://afterbetting.com/og-image.png"/>\n'
            f'<script type="application/ld+json">{art}</script>\n<script type="application/ld+json">{bc}</script>\n')

def build(template, out, lang, url, title, desc, headline, crumb, home, blog, hero, body, cta, related, crisis):
    s = open(template, encoding='utf-8').read()
    a = s.index('<title>'); b = s.index('<script async src="https://www.googletagmanager.com')
    s = s[:a] + head(lang, url, title, desc, headline, crumb, home, blog) + s[b:]
    # andere ld+json uit het sjabloon (na de stijl) weghalen; de onze staan boven GA
    first = s.index('<script async src="https://www.googletagmanager.com')
    s = s[:first] + re.sub(r'<script type="application/ld\+json">[\s\S]*?</script>\n?', '', s[first:])
    a = s.index('<section class="hero">'); b = s.index('<div class="crisis-footer">')
    s = s[:a] + hero + '\n<article class="body">\n' + body + '\n' + cta + '\n</article>\n' + related + '\n' + s[b:]
    s = re.sub(r'<div class="crisis-footer">[\s\S]*?</div>', crisis, s, count=1)
    assert s.count('<title>') == 1 and s.count('rel="canonical"') == 1 and '—' not in s
    open(out, 'w', encoding='utf-8').write(s)
    words = len(re.sub(r'<[^>]+>', ' ', body).split())
    print(out, len(s), 'bytes,', words, 'woorden, title', len(title), 'desc', len(desc))

def hero(bc_home, bc_blog, label_home, cat, h1, lead, meta):
    return (f'<section class="hero"><div class="hero-inner">\n<div class="bc"><a href="{bc_home}">{label_home}</a> &rarr; <a href="{bc_blog}">Blog</a> &rarr; {cat}</div>\n'
            f'<div class="tag">{cat}</div>\n<h1>{h1}</h1>\n<p style="font-size:1.1rem;color:var(--mid);line-height:1.7;margin-top:1rem">{lead}</p>\n'
            f'<div class="meta">{meta}</div>\n</div></section>')

def cards(items):
    return ('<section class="related"><div class="rel-inner"><h3>{}</h3><div class="rel-grid">'.format(items[0])
            + ''.join(f'<a href="{h}" class="rel-card"><div class="t">{t}</div><h4>{n}</h4></a>' for h, t, n in items[1:])
            + '</div></div></section>')

exec(open('blog_teksten_cruks_gamstop.py', encoding='utf-8').read())

build('nl/blog/zelfuitsluiting-gokken-werkt-het.html', 'nl/blog/cruks-opzeggen.html', 'nl', NL_URL,
      'Cruks opzeggen: zo werkt het, en lees dit eerst',
      'Kun je Cruks eerder opzeggen? De regels (minimaal 6 maanden, 8 dagen bedenktijd) en wat je kunt doen als de zin om te spelen nu groot is.',
      'Cruks opzeggen: zo werkt het, en lees dit eerst', 'Cruks opzeggen', 'https://afterbetting.com/nl/', 'https://afterbetting.com/nl/blog',
      hero('/nl/', '/nl/blog', 'Home', 'Crisis', 'Cruks opzeggen: zo werkt het, en lees dit eerst',
           'De regels van de Kansspelautoriteit, eerlijk uitgelegd. En wat je kunt doen als de zin om te spelen nu groot is.',
           'Door Afterbetting &middot; 11 oktober 2026 &middot; 8 min lezen'),
      NL_BODY,
      '<div class="cta-block"><h3>Hulp bij drang, met één tik</h3><p>De Herstelkit in de app is gratis: 15 minuten uitstellen met timer, een bericht aan je vertrouwenspersoon en de hulplijn.</p><a href="https://app.afterbetting.com/onboarding" onclick="if(window.gtag)gtag(\'event\',\'cta_click\',{cta_location:\'article_cta\',page_path:location.pathname})">Begin gratis</a></div>',
      cards(['Meer lezen', ('/nl/blog/cruks-omzeilen-wat-nu', 'Crisis', 'Cruks omzeilen lukt me. En toch wil ik stoppen.'),
             ('/nl/blog/zelfuitsluiting-gokken-werkt-het', 'Tools', 'Werkt zelfuitsluiting bij gokken?'),
             ('/nl/blog/terugval-na-gokverslaving', 'Terugval', 'Terugval na gokverslaving. Wat nu?'),
             ('/nl/blog/hoe-lang-duurt-herstel-gokverslaving', 'Herstel', 'Hoe lang duurt herstel van gokverslaving?')]),
      '<div class="crisis-footer"><p>Zit je nu in crisis? Bel <strong>OpenOverGokken: 0800-2400022</strong>. Gratis, anoniem, 24 uur per dag. Denk je aan zelfmoord? Bel <strong>113</strong> (0800-0113).</p></div>')

build('blog/does-self-exclusion-work-gambling.html', 'blog/cancel-gamstop-early.html', 'en', EN_URL,
      'Can you cancel GamStop early? Read this first',
      'Can you cancel GamStop early? The real rules, what happens when your exclusion ends, and what to do if the urge to gamble is strong right now.',
      'Can you cancel GamStop early? Read this first', 'Cancel GamStop early', 'https://afterbetting.com', 'https://afterbetting.com/blog',
      hero('https://afterbetting.com', 'https://afterbetting.com/blog', 'Home', 'Crisis', 'Can you cancel GamStop early? Read this first',
           'The GamStop rules, explained honestly. And what you can do if the urge to gamble is strong right now.',
           'By Afterbetting &middot; 11 October 2026 &middot; 8 min read'),
      EN_BODY,
      '<div class="cta"><h3>Help with an urge, one tap away</h3><p>The recovery kit in the app is free: a 15-minute delay timer, a message to your person and the helpline.</p><a href="https://app.afterbetting.com/onboarding" onclick="if(window.gtag)gtag(\'event\',\'cta_click\',{cta_location:\'article_cta\',page_path:location.pathname})">Start free</a></div>',
      cards(['Continue reading', ('https://afterbetting.com/blog/does-self-exclusion-work-gambling', 'Tools', 'Does self-exclusion actually work for gambling addiction?'),
             ('https://afterbetting.com/blog/what-to-do-after-gambling-relapse', 'Relapse', 'What to do immediately after a gambling relapse'),
             ('https://afterbetting.com/blog/how-to-stop-gambling-urges-weekends', 'Urges', 'How to stop gambling urges at the weekend'),
             ('https://afterbetting.com/blog/how-long-gambling-recovery-takes', 'Recovery', 'How long does gambling recovery take?')]),
      '<div class="crisis-footer"><p>In crisis right now? In the UK, call the <strong>National Gambling Helpline (GamCare) on 0808 8020 133</strong>, free, 24/7. In the Netherlands: <strong>OpenOverGokken 0800-2400022</strong>. Thinking about suicide? Call <strong>Samaritans on 116 123</strong>.</p></div>')
