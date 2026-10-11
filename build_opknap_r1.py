# Opknapronde 1 (11 okt 2026): herschrijft drie bestaande NL-pagina's. URL, hreflang en datePublished blijven gelijk.
import json, re
from blogbuild import build, hero, cards
exec(open('blog_teksten_opknap_r1.py', encoding='utf-8').read())
TEMPLATE = 'nl/blog/goksites-blokkeren.html'
CRISIS = '<div class="crisis-footer"><p>Zit je nu in crisis? Bel <strong>OpenOverGokken: 0800-2400022</strong>. Gratis, anoniem, 24 uur per dag. Denk je aan zelfmoord? Bel <strong>113</strong> (0800-0113).</p></div>'
CTA = ('<div class="cta-block"><h3>{}</h3><p>{}</p><a href="https://app.afterbetting.com/onboarding" '
       'onclick="if(window.gtag)gtag(\'event\',\'cta_click\',{{cta_location:\'article_cta\',page_path:location.pathname}})">Begin gratis</a></div>')

def inline(t):
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    return re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', t)

def md(src):
    out, lst = [], None
    for block in src.strip().split('\n\n'):
        lines = block.strip().split('\n')
        if lines[0].startswith('## '):
            out.append(f'<h2>{inline(lines[0][3:])}</h2>'); continue
        if all(l.startswith('- ') for l in lines):
            out.append('<ul>' + ''.join(f'<li>{inline(l[2:])}</li>' for l in lines) + '</ul>'); continue
        if all(re.match(r'\d+\. ', l) for l in lines):
            out.append('<ol>' + ''.join(f'<li>{inline(re.sub(r"^\d+\. ", "", l))}</li>' for l in lines) + '</ol>'); continue
        out.append('<p>' + inline(' '.join(lines)) + '</p>')
    return '\n'.join(out) + '\n'

def faq(items):
    html = '<h2>Veelgestelde vragen</h2>\n' + ''.join(f'<h3>{q}</h3>\n<p>{a}</p>\n' for q, a in items)
    ld = '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}, ensure_ascii=False) + '</script>\n'
    return html, ld

def src(items):
    return '<h2>Bronnen</h2>\n<ul>' + ''.join(f'<li><a href="{u}" rel="noopener">{t}</a></li>' for t, u in items) + '</ul>\n' if items else ''

def page(slug, title, desc, h1, crumb, cat, lead, mins, body, faqs, sources, cta, related):
    path = f'nl/blog/{slug}.html'; url = f'https://afterbetting.com/nl/blog/{slug}'
    old = open(path, encoding='utf-8').read()
    published = re.search(r'"datePublished": ?"([^"]+)"', old).group(1)
    href = '\n'.join(re.findall(r'<link rel="alternate" hreflang="[^"]+" href="[^"]+"/>', old))
    assert 'hreflang="x-default"' in href
    fh, fld = faq(faqs)
    build(TEMPLATE, path, 'nl', url, title, desc, h1, crumb, 'https://afterbetting.com/nl/', 'https://afterbetting.com/nl/blog',
          hero('/nl/', '/nl/blog', 'Home', cat, h1, lead, f'Door Afterbetting &middot; bijgewerkt 11 oktober 2026 &middot; {mins} min lezen'),
          md(body) + fh + src(sources), CTA.format(*cta), cards(['Meer lezen'] + related), CRISIS, href, '2026-10-11', fld)
    s = open(path, encoding='utf-8').read()
    s = s.replace('"datePublished": "2026-10-11"', f'"datePublished": "{published}"', 1)
    open(path, 'w', encoding='utf-8').write(s)

page('hoe-vul-ik-mijn-tijd-zonder-gokken',
     'Hoe vul je je tijd zonder gokken? Avonden en weekend',
     'Hoe vul je je tijd zonder gokken? Een plan voor de avonden en het weekend, de uren waarop de drang het sterkst is. Uit eigen ervaring.',
     'Hoe vul je je tijd zonder gokken? De avonden en het weekend', 'Tijd vullen zonder gokken', 'Gewoonten',
     'Een plan voor de uren waarop het vroeger altijd misging: de avond en het weekend.', 8, TIJD, TIJD_FAQ, [],
     ('Een plan voor vanavond', 'In de app plan je je dag en je gewoonten, en heb je bij drang met één tik een timer en de hulplijn.'),
     [('/nl/blog/dagelijkse-gewoonten-na-gokverslaving', 'Gewoonten', 'Dagelijkse gewoonten na gokverslaving'),
      ('/nl/blog/sportgokken-verslaving', 'Herkennen', 'Sportgokken verslaving: hoe je hier eerlijk naar kijkt'),
      ('/nl/blog/goksites-blokkeren', 'Tools', 'Goksites blokkeren: telefoon, laptop en je bank'),
      ('/nl/blog/terugval-na-gokverslaving', 'Terugval', 'Terugval na gokverslaving. Wat nu?')])

page('dagelijkse-gewoonten-na-gokverslaving',
     'Dagelijkse gewoonten na gokverslaving: ritme opbouwen',
     'Dagelijkse gewoonten na gokverslaving: hoe je een nieuw ritme opbouwt, klein begint en volhoudt. Met een voorbeelddag en wat onderzoek zegt.',
     'Dagelijkse gewoonten na gokverslaving: zo bouw je een nieuw ritme', 'Dagelijkse gewoonten', 'Gewoonten',
     'Gokken had een vaste plek in je dag. Zo zet je er bewust een ander ritme voor in de plaats.', 8, GEWOONTEN, GEWOONTEN_FAQ, GEWOONTEN_SOURCES,
     ('Je ritme op één plek', 'Gewoonten, je dagelijkse check-in en je dagen vrij. Gratis te beginnen.'),
     [('/nl/blog/hoe-vul-ik-mijn-tijd-zonder-gokken', 'Gewoonten', 'Hoe vul je je tijd zonder gokken?'),
      ('/nl/blog/terugval-na-gokverslaving', 'Terugval', 'Terugval na gokverslaving. Wat nu?'),
      ('/nl/blog/slaapproblemen-stoppen-met-gokken', 'Herstel', 'Slaapproblemen na stoppen met gokken'),
      ('/nl/blog/gokschuld-aflossen', 'Geld', 'Gokschuld aflossen')])

page('hoe-stop-ik-met-gokken-met-schulden',
     'Stoppen met gokken met schulden: niet terugwinnen',
     'Hoe stop je met gokken als je schulden hebt? Waarom terugwinnen niet werkt, hoe je de kraan dichtzet en waar je gratis hulp krijgt.',
     'Hoe stop ik met gokken als ik schulden heb?', 'Stoppen met gokken met schulden', 'Geld &amp; schulden',
     'Over de gedachte dat je het nog één keer kunt terugwinnen. En hoe je stopt terwijl de schuld er nog is.', 8, SCHULDEN, SCHULDEN_FAQ, SCHULDEN_SOURCES,
     ('Je geld weer in beeld', 'In de app zie je wat er deze maand over is en hoe je schulden dalen. Gratis te beginnen.'),
     [('/nl/blog/gokschuld-aflossen', 'Geld', 'Gokschuld aflossen'),
      ('/nl/blog/salaris-vergokt-wat-nu', 'Geld', 'Salaris vergokt, wat nu?'),
      ('/nl/blog/geld-terugvragen-online-casino', 'Geld', 'Geld terugvragen van een online casino'),
      ('/nl/blog/goksites-blokkeren', 'Tools', 'Goksites blokkeren: telefoon, laptop en je bank')])
