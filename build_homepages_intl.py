# Bouwt de DE/FR/ES-homepages opnieuw vanuit de huidige EN-homepage (11 okt 2026).
# Volgorde: python3 build_homepages_intl.py && python3 build_app_preview.py && python3 update_pricing_plus.py
import json, re, sys
from homepage_intl_teksten import TR, CRISIS, HEAD

LANGS = ('de', 'fr', 'es')
IDX = {'de': 0, 'fr': 1, 'es': 2}

# 1. Onjuiste claims op de EN-pagina zelf rechtzetten (idempotent)
en = open('index.html', encoding='utf-8').read()
OLD_FREE = 'Yes. The free plan includes your recovery streak, 3 journal prompts per week, 3 habit slots, and a basic dashboard. No credit card required'
NEW_FREE = 'Yes. The free plan includes your day counter and milestones, the recovery kit, 5 habits and 3 journal entries a week. No credit card required'
en = en.replace(OLD_FREE + ', no time limit.', NEW_FREE + ', no time limit.').replace(OLD_FREE + '.', NEW_FREE + ', no time limit.')
en = en.replace('<div class="trust-item">End-to-end encrypted</div>', '<div class="trust-item">Encrypted in transit and at rest</div>')
en = en.replace('financial data are private and encrypted. Afterbetting', 'financial data are private and encrypted in transit and at rest. Afterbetting')
open('index.html', 'w', encoding='utf-8').write(en)
nl = open('nl/index.html', encoding='utf-8').read()
nl = nl.replace('End-to-end versleuteld', 'Versleuteld verzonden en opgeslagen')
open('nl/index.html', 'w', encoding='utf-8').write(nl)

missing = set()

def tr_text(s, i):
    body_start = s.index('<body')
    head, body = s[:body_start], s[body_start:]
    def sub(m):
        raw = m.group(1); t = raw.strip()
        if not t or t not in TR:
            if t and re.search(r'[A-Za-z]{3}', t): missing.add(t)
            return m.group(0)
        lead = raw[:len(raw) - len(raw.lstrip())]; trail = raw[len(raw.rstrip()):]
        return '>' + lead + TR[t][i] + trail + '<'
    # alleen tekst buiten script/style/svg vertalen
    parts = re.split(r'(<(?:script|style|svg)[\s\S]*?</(?:script|style|svg)>)', body)
    for k in range(0, len(parts), 2):
        parts[k] = re.sub(r'>([^<>]+)<', sub, parts[k])
    return head + ''.join(parts)

for lang in LANGS:
    i = IDX[lang]; h = HEAD[lang]; url = f'https://afterbetting.com/{lang}/'
    s = en
    s = s.replace('<html lang="en">', f'<html lang="{lang}">', 1)
    # head: meta tot en met twitter:image vervangen
    a = s.index('  <title>'); b = s.index('\n', s.index('<meta name="twitter:image"')) + 1
    hreflang = re.search(r'(  <link rel="alternate" hreflang="en"[\s\S]*?hreflang="x-default"[^>]*>\n)', s).group(1)
    s = s[:a] + (
        f'  <title>{h["title"]}</title>\n'
        f'  <meta name="description" content="{h["desc"]}" />\n'
        f'  <meta name="robots" content="index, follow" />\n'
        f'  <link rel="canonical" href="{url}" />\n' + hreflang +
        f'  <meta property="og:type" content="website" />\n  <meta property="og:locale" content="{h["locale"]}" />\n'
        f'  <meta property="og:url" content="{url}" />\n  <meta property="og:title" content="{h["title"]}" />\n'
        f'  <meta property="og:description" content="{h["og"]}" />\n  <meta property="og:image" content="https://afterbetting.com/og-image.png" />\n'
        f'  <meta property="og:site_name" content="Afterbetting" />\n  <meta name="twitter:card" content="summary_large_image" />\n'
        f'  <meta name="twitter:title" content="{h["title"]}" />\n  <meta name="twitter:description" content="{h["desc"]}" />\n'
        f'  <meta name="twitter:image" content="https://afterbetting.com/og-image.png" />\n') + s[b:]
    # verzonnen of onbevestigde ervaringen niet meenemen
    s = re.sub(r'<section class="section section-alt" id="testimonials">[\s\S]*?</section>\s*', '', s)
    # tekst vertalen
    s = tr_text(s, i)
    # crisisregel per land
    s = re.sub(r'<p>In crisis right now\? UK:[\s\S]*?</p>', CRISIS[lang], s, count=1)
    # logo naar de eigen taalversie
    s = s.replace('<a href="https://afterbetting.com" class="logo">', f'<a href="/{lang}/" class="logo">', 1)
    # rekenhulp
    s = s.replace('btn.textContent=y>0?"Save €"+y.toLocaleString()+" this year":"Start saving";',
                  'btn.textContent=y>0?"' + h['calc_save'].replace('{c}', '€').replace('{y}', '"+y.toLocaleString()+"') + '":"' + h['calc_start'] + '";')
    # schema: SoftwareApplication-beschrijving en FAQ uit de vertaalde vragen
    s = re.sub(r'("@type":"SoftwareApplication",[\s\S]*?"description":")[^"]*(")', lambda m: m.group(1) + h['app'].replace('"', '\\"') + m.group(2), s, count=1)
    faq = re.findall(r'<div class="faq-q">(.*?)</div><p class="faq-a">(.*?)</p>', s)
    ld = json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub('<[^>]+>', '', a)}} for q, a in faq]}, ensure_ascii=False)
    s = re.sub(r'<script type="application/ld\+json">\{"@context":"https://schema.org","@type":"FAQPage"[\s\S]*?</script>', lambda m: f'<script type="application/ld+json">{ld}</script>', s, count=1)
    assert s.count('<title>') == 1 and 'In crisis right now' not in s and 'testimonials' not in s
    open(f'{lang}/index.html', 'w', encoding='utf-8').write(s)
    print(f'{lang}/index.html', len(s), 'bytes,', len(faq), 'FAQ')

# ook de EN FAQ-schema-tekst gelijk trekken met de pagina
en = open('index.html', encoding='utf-8').read()
en = en.replace('"text":"Yes. The free plan includes your recovery streak, 3 journal prompts per week, 3 habit slots, and a basic dashboard. No credit card required."',
                '"text":"' + NEW_FREE + ', no time limit."')
open('index.html', 'w', encoding='utf-8').write(en)

# wat niet vertaald is (preview en prijsblok worden daarna door hun eigen scripts gebouwd)
print('\nNIET VERTAALD:'); [print(' -', m[:90]) for m in sorted(missing)]
