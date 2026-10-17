# 17 okt 2026: homepage korter en sterker. Bewijsregel in de hero, features-grid weg, founder-blokken samengevoegd,
# FAQ 8 naar 6 (EN/DE/FR/ES; NL had al 7 eigen vragen), FAQ-schema gelijk aan zichtbare vragen. Veilig om opnieuw te draaien.
import re, json, html

PROOF = {
 'index.html': 'Built by someone who gambled for 8 years, ran up €40k+ in debt, and paid every euro back.',
 'nl/index.html': 'Gebouwd door iemand die 8 jaar gokte, €40k+ schuld opbouwde en elke euro heeft terugbetaald.',
 'de/index.html': 'Entwickelt von jemandem, der 8 Jahre gespielt, über 40.000 € Schulden gemacht und jeden Euro zurückgezahlt hat.',
 'fr/index.html': 'Créé par quelqu’un qui a joué pendant 8 ans, accumulé plus de 40 000 € de dettes et tout remboursé.',
 'es/index.html': 'Creado por alguien que apostó durante 8 años, acumuló más de 40.000 € de deuda y devolvió cada euro.',
}
DROP_FAQ = {'index.html': [3, 4], 'de/index.html': [3, 4], 'fr/index.html': [3, 4], 'es/index.html': [3, 4], 'nl/index.html': []}
CSS = ('\n/* Bewijsregel in de hero en samengevoegd founder-blok (17 okt 2026) */\n'
       '.hero-proof { display: flex; gap: .6rem; align-items: flex-start; font-size: .95rem; font-weight: 600; color: var(--dark); margin: -.25rem 0 1.5rem; max-width: 520px; line-height: 1.5; }\n'
       '.hero-proof::before { content: ""; flex: 0 0 4px; align-self: stretch; border-radius: 2px; background: var(--apricot); }\n'
       '.founder-merged { display: grid; grid-template-columns: auto 1fr; gap: 2rem; align-items: start; max-width: 780px; margin: 0 auto; text-align: left; }\n'
       '@media (max-width: 640px) { .founder-merged { grid-template-columns: 1fr; gap: 1rem; } }\n'
       '/* Mobiel: app-schermen staan direct onder de hero, dus de hero-telefoon zou dubbel zijn (17 okt 2026) */\n'
       '@media (max-width: 768px) { .hero-phone { display: none; } }\n')

def section_span(s, sid):
    i = s.index(f'id="{sid}"'); a = s.rindex('<section', 0, i)
    b = s.index('</section>', i) + len('</section>')
    return a, b

for f, proof in PROOF.items():
    s = open(f, encoding='utf-8').read()
    # 1. bewijsregel onder de hero-tekst
    if 'class="hero-proof"' not in s:
        m = re.search(r'<p class="hero-sub">[\s\S]*?</p>', s); assert m, f
        s = s[:m.end()] + f'\n    <p class="hero-proof">{proof}</p>' + s[m.end():]
    # 2. features-grid weg (overlapt met de app-schermen)
    if 'id="features"' in s:
        a, b = section_span(s, 'features'); s = s[:a] + s[b:].lstrip('\n')
    # 3. founder-quote in het "waarom"-blok, statkaartjes en los founder-blok weg
    if 'id="founder"' in s and 'class="founder-merged"' not in s:
        fa, fb = section_span(s, 'founder'); fsec = s[fa:fb]
        svg = re.search(r'<svg[\s\S]*?</svg>', fsec).group(0)
        quote = re.search(r'<blockquote[\s\S]*?</blockquote>', fsec).group(0)
        who = re.search(r'</blockquote>\s*(<div[^>]*>[\s\S]*?</div>)', fsec).group(1)
        s = s[:fa] + s[fb:].lstrip('\n')
        ca, cb = section_span(s, 'founder-credibility'); csec = s[ca:cb]
        gi = csec.index('repeat(auto-fit,minmax(180px')
        start = csec.rindex('<div>', 0, gi)  # ouder-div van het raster
        depth, k = 0, start
        for m in re.finditer(r'<div\b|</div>', csec[start:]):
            depth += 1 if m.group(0) != '</div>' else -1
            if depth == 0:
                k = start + m.end(); break
        merged = f'<div class="founder-merged">{svg}<div>{quote}{who}</div></div>'
        csec = csec[:start] + merged + csec[k:]
        csec = re.sub(r'\n\s*<p [^>]*class="swipe-hint">[^<]*</p>', '', csec)
        s = s[:ca] + csec + s[cb:]
    # 4. FAQ inkorten en schema gelijk trekken met wat zichtbaar is
    items = list(re.finditer(r'\s*<div class="faq-item"><div class="faq-q">([\s\S]*?)</div><p class="faq-a">([\s\S]*?)</p></div>', s))
    drop = DROP_FAQ[f]
    if drop and len(items) == 8:
        for k in sorted(drop, reverse=True):
            m = items[k]; s = s[:m.start()] + s[m.end():]
        items = list(re.finditer(r'\s*<div class="faq-item"><div class="faq-q">([\s\S]*?)</div><p class="faq-a">([\s\S]*?)</p></div>', s))
    if not items: open(f, 'w', encoding='utf-8').write(s); print('ok', f, 'faq ongewijzigd'); continue
    clean = lambda x: html.unescape(re.sub(r'<[^>]+>', '', x)).strip()
    faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": clean(m.group(1)), "acceptedAnswer": {"@type": "Answer", "text": clean(m.group(2))}} for m in items]}
    s, n = re.subn(r'<script type="application/ld\+json">\{"@context": ?"https://schema.org", ?"@type": ?"FAQPage"[\s\S]*?</script>',
                   '<script type="application/ld+json">' + json.dumps(faq, ensure_ascii=False) + '</script>', s, count=1)
    assert n == 1, (f, 'faq-schema')
    assert '—' not in s
    open(f, 'w', encoding='utf-8').write(s)
    print('ok', f, 'faq', len(items))

th = open('theme.css', encoding='utf-8').read()
if '.hero-proof' not in th:
    open('theme.css', 'a', encoding='utf-8').write(CSS)

# vertaling van de bewijsregel voor een volgende rebuild van DE/FR/ES vanuit EN
t = open('homepage_intl_teksten.py', encoding='utf-8').read()
key = PROOF['index.html']
if key not in t:
    line = f" {key!r}: ({PROOF['de/index.html']!r}, {PROOF['fr/index.html']!r}, {PROOF['es/index.html']!r}),\n"
    t = t.replace(" 'GDPR compliant':", line + " 'GDPR compliant':", 1)
    open('homepage_intl_teksten.py', 'w', encoding='utf-8').write(t)
