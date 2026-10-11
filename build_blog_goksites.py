# Bouwt nl/blog/goksites-blokkeren (11 okt 2026). EN-tegenhanger volgt; dan hreflang aanvullen.
import json
from blogbuild import build, hero, cards
exec(open('blog_tekst_goksites.py', encoding='utf-8').read())
URL = 'https://afterbetting.com/nl/blog/goksites-blokkeren'
HREF = f'<link rel="alternate" hreflang="nl" href="{URL}"/>\n<link rel="alternate" hreflang="x-default" href="{URL}"/>'
faq_html = '<h2>Veelgestelde vragen</h2>\n' + ''.join(f'<h3>{q}</h3>\n<p>{a}</p>\n' for q, a in FAQ)
src_html = '<h2>Bronnen</h2>\n<ul>' + ''.join(f'<li><a href="{u}" rel="noopener">{t}</a></li>' for t, u in SOURCES) + '</ul>'
faq_ld = '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
    {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}, ensure_ascii=False) + '</script>\n'
build('nl/blog/zelfuitsluiting-gokken-werkt-het.html', 'nl/blog/goksites-blokkeren.html', 'nl', URL,
      'Goksites blokkeren: telefoon, laptop en je bank',
      'Goksites blokkeren op je iPhone, Android, laptop en via je bank. Wat echt werkt, wat niet bestaat, en hoe je de sleutel uit eigen handen geeft.',
      'Goksites blokkeren: telefoon, laptop en je bank', 'Goksites blokkeren', 'https://afterbetting.com/nl/', 'https://afterbetting.com/nl/blog',
      hero('/nl/', '/nl/blog', 'Home', 'Tools', 'Goksites blokkeren: telefoon, laptop en je bank',
           'Wat er echt kan op je telefoon, je laptop en bij je bank. En wat niet bestaat, al lees je online van wel.',
           'Door Afterbetting &middot; 11 oktober 2026 &middot; 9 min lezen'),
      NL_BODY + faq_html + src_html,
      '<div class="cta-block"><h3>Blokkeren is stap één</h3><p>De app helpt met de rest: je dagen, je geld weer op orde en hulp met één tik als de drang komt.</p><a href="https://app.afterbetting.com/onboarding" onclick="if(window.gtag)gtag(\'event\',\'cta_click\',{cta_location:\'article_cta\',page_path:location.pathname})">Begin gratis</a></div>',
      cards(['Meer lezen', ('/nl/blog/cruks-opzeggen', 'Crisis', 'Cruks opzeggen: zo werkt het, en lees dit eerst'),
             ('/nl/blog/zelfuitsluiting-gokken-werkt-het', 'Tools', 'Werkt zelfuitsluiting bij gokken?'),
             ('/nl/blog/gokschuld-aflossen', 'Geld', 'Gokschuld aflossen'),
             ('/nl/blog/hoe-vul-ik-mijn-tijd-zonder-gokken', 'Gewoonten', 'Hoe vul ik mijn tijd zonder gokken')]),
      '<div class="crisis-footer"><p>Zit je nu in crisis? Bel <strong>OpenOverGokken: 0800-2400022</strong>. Gratis, anoniem, 24 uur per dag. Denk je aan zelfmoord? Bel <strong>113</strong> (0800-0113).</p></div>',
      HREF, '2026-10-11', faq_ld)
