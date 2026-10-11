# Sitemap en blogindexen bijwerken voor de artikelen van okt 2026. Veilig om opnieuw te draaien.
PAIRS = [  # (nl-slug, en-slug, datum)
    ('cruks-opzeggen', 'cancel-gamstop-early', '2026-10-11'),
    ('goksites-blokkeren', 'block-gambling-sites-and-payments', '2026-10-11'),
    ('cruks-omzeilen-wat-nu', 'casino-not-on-gamstop', '2026-10-11'),
]
NL_CARDS = {'goksites-blokkeren': ('Tools', 'Goksites blokkeren: telefoon, laptop en je bank', 'Wat er echt kan op je telefoon, je laptop en bij je bank. En wat niet bestaat, al lees je online van wel.', '11 oktober 2026', '9 min lezen'),
            'cruks-opzeggen': ('Crisis', 'Cruks opzeggen: zo werkt het, en lees dit eerst', 'De regels van de Kansspelautoriteit, eerlijk uitgelegd. En wat je doet als de zin om te spelen nu groot is.', '11 oktober 2026', '8 min lezen')}
EN_CARDS = {'casino-not-on-gamstop': ('Crisis', 'Found a casino not on GamStop? Read this first', 'What it means that you found a way around your own exclusion. And what to do tonight and tomorrow.'),
            'block-gambling-sites-and-payments': ('Tools', 'How to block gambling sites, apps and bank payments', 'What works on your phone, your laptop and your bank card. Which UK banks have a gambling block, and where the gaps are.'),
            'cancel-gamstop-early': ('Crisis', 'Can you cancel GamStop early? Read this first', 'The GamStop rules, explained honestly. And what to do if the urge to gamble is strong right now.')}

def entry(loc, nl, en, date):
    if en is None:
        return (f'  <url>\n    <loc>{loc}</loc>\n    <lastmod>{date}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.7</priority>\n'
                f'    <xhtml:link rel="alternate" hreflang="nl" href="{nl}"/>\n    <xhtml:link rel="alternate" hreflang="x-default" href="{nl}"/>\n  </url>\n')
    return (f'  <url>\n    <loc>{loc}</loc>\n    <lastmod>{date}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.7</priority>\n'
            f'    <xhtml:link rel="alternate" hreflang="nl" href="{nl}"/>\n    <xhtml:link rel="alternate" hreflang="en" href="{en}"/>\n'
            f'    <xhtml:link rel="alternate" hreflang="x-default" href="{en}"/>\n  </url>\n')

sm = open('sitemap.xml', encoding='utf-8').read()
for nl_slug, en_slug, date in PAIRS:
    nl = f'https://afterbetting.com/nl/blog/{nl_slug}'; en = f'https://afterbetting.com/blog/{en_slug}' if en_slug else None
    for loc in [x for x in (nl, en) if x]:
        if f'<loc>{loc}</loc>' in sm and en and f'<loc>{loc}</loc>' in sm and f'hreflang="en" href="{en}"' not in sm.split(f'<loc>{loc}</loc>')[1].split('</url>')[0]:
            a = sm.rindex('  <url>', 0, sm.index(f'<loc>{loc}</loc>')); b = sm.index('</url>', a) + len('</url>\n')
            sm = sm[:a] + entry(loc, nl, en, date) + sm[b:]
        if f'<loc>{loc}</loc>' not in sm:
            sm = sm.replace('</urlset>', entry(loc, nl, en, date) + '</urlset>')
open('sitemap.xml', 'w', encoding='utf-8').write(sm)

ix = open('nl/blog/index.html', encoding='utf-8').read()
for slug, (cat, h2, p, date, mins) in NL_CARDS.items():
    if f'/nl/blog/{slug}"' in ix: continue
    card = f'<a href="/nl/blog/{slug}" class="blog-card">\n<div class="cat">{cat}</div>\n<h2>{h2}</h2>\n<p>{p}</p>\n<div class="meta">{date} &middot; {mins}</div>\n</a>'
    ix = ix.replace('<div class="blog-grid">', '<div class="blog-grid">' + card, 1)
open('nl/blog/index.html', 'w', encoding='utf-8').write(ix)

ix = open('blog/index.html', encoding='utf-8').read()
for slug, (cat, h2, p) in EN_CARDS.items():
    if f'/blog/{slug}"' in ix: continue
    card = f'<a href="https://afterbetting.com/blog/{slug}" class="card"><div class="card-body"><div class="t">{cat}</div><h2>{h2}</h2><p>{p}</p><div class="rm">Read article &rarr;</div></div></a>'
    i = ix.index('<a href="https://afterbetting.com/blog/', ix.index('class="card"') - 200)
    i = ix.rfind('<a href="https://afterbetting.com/blog/', 0, ix.index('class="card"') + 1)
    ix = ix[:i] + card + ix[i:]
open('blog/index.html', 'w', encoding='utf-8').write(ix)
print('klaar')
