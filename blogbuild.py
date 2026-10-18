# Gedeelde bouwstenen voor blogartikelen: sjabloon, meta, schema, hero, gerelateerd.
import json, re

def head(lang, url, title, desc, headline, crumb, home, blog, hreflang, date, extra_ld=''):
    art = json.dumps({"@context": "https://schema.org", "@type": "Article", "headline": headline,
                      "author": {"@type": "Organization", "name": "Afterbetting"},
                      "publisher": {"@type": "Organization", "name": "Afterbetting", "url": "https://afterbetting.com"},
                      "datePublished": date, "dateModified": date, "inLanguage": lang, "url": url}, ensure_ascii=False)
    bc = json.dumps({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": home},
        {"@type": "ListItem", "position": 2, "name": "Blog", "item": blog},
        {"@type": "ListItem", "position": 3, "name": crumb, "item": url}]}, ensure_ascii=False)
    loc = '<meta property="og:locale" content="nl_NL"/>\n<meta property="og:locale:alternate" content="nl_BE"/>' if lang == 'nl' else '<meta property="og:locale" content="en_GB"/>'
    return (f'<title>{title}</title>\n<meta name="description" content="{desc}"/>\n<meta name="robots" content="index,follow"/>\n'
            f'<link rel="canonical" href="{url}"/>\n{hreflang}\n<meta property="og:type" content="article"/>\n{loc}\n'
            f'<meta property="og:url" content="{url}"/>\n<meta property="og:title" content="{title}"/>\n<meta property="og:description" content="{desc}"/>\n'
            f'<meta property="og:image" content="https://afterbetting.com/og-image.png"/>\n<meta name="twitter:card" content="summary_large_image"/>\n'
            f'<meta name="twitter:title" content="{title}"/>\n<meta name="twitter:description" content="{desc}"/>\n'
            f'<meta name="twitter:image" content="https://afterbetting.com/og-image.png"/>\n'
            f'<script type="application/ld+json">{art}</script>\n<script type="application/ld+json">{bc}</script>\n' + extra_ld)

def build(template, out, lang, url, title, desc, headline, crumb, home, blog, hero, body, cta, related, crisis, hreflang, date, extra_ld=''):
    s = open(template, encoding='utf-8').read()
    a = s.index('<title>'); b = s.index('<script>window.addEventListener("load",function(){setTimeout(function(){var s=document.createElement("script");')
    s = s[:a] + head(lang, url, title, desc, headline, crumb, home, blog, hreflang, date, extra_ld) + s[b:]
    # andere ld+json uit het sjabloon (na de stijl) weghalen; de onze staan boven GA
    first = s.index('<script>window.addEventListener("load",function(){setTimeout(function(){var s=document.createElement("script");')
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

