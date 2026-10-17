# Bouwt nl/blog/gokverslaving-hulp-zoeken en blog/where-to-get-help-gambling-addiction (11 okt 2026), hreflang naar elkaar.
import json
from blogbuild import build, hero, cards
from opknap_en import md, faq as en_faq, src as en_src
exec(open('blog_tekst_hulp.py', encoding='utf-8').read())
NL_URL = 'https://afterbetting.com/nl/blog/gokverslaving-hulp-zoeken'
EN_URL = 'https://afterbetting.com/blog/where-to-get-help-gambling-addiction'
HREF = (f'<link rel="alternate" hreflang="nl" href="{NL_URL}"/>\n<link rel="alternate" hreflang="en" href="{EN_URL}"/>\n'
        f'<link rel="alternate" hreflang="x-default" href="{EN_URL}"/>')
ONCLICK = 'onclick="if(window.gtag)gtag(\'event\',\'cta_click\',{cta_location:\'article_cta\',page_path:location.pathname})"'

def nl_faq(items):
    html = '<h2>Veelgestelde vragen</h2>\n' + ''.join(f'<h3>{q}</h3>\n<p>{a}</p>\n' for q, a in items)
    ld = '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}, ensure_ascii=False) + '</script>\n'
    return html, ld

fh, fld = nl_faq(NL_FAQ)
nl_src = '<h2>Bronnen</h2>\n<ul>' + ''.join(f'<li><a href="{u}" rel="noopener">{t}</a></li>' for t, u in NL_SOURCES) + '</ul>\n'
build('nl/blog/goksites-blokkeren.html', 'nl/blog/gokverslaving-hulp-zoeken.html', 'nl', NL_URL,
      'Hulp bij gokverslaving: waar je terechtkunt',
      'Hulp zoeken bij gokverslaving: OpenOverGokken, huisarts, verslavingszorg, zelfhulp en schuldhulp. Wat er is, wat het kost en wat je kunt verwachten.',
      'Hulp bij gokverslaving: waar je terechtkunt', 'Hulp zoeken', 'https://afterbetting.com/nl/', 'https://afterbetting.com/nl/blog',
      hero('/nl/', '/nl/blog', 'Home', 'Hulp', 'Hulp bij gokverslaving: waar je terechtkunt',
           'Wat er in Nederland is, wat het kost en wat je kunt verwachten.', 'Door Afterbetting &middot; 11 oktober 2026 &middot; 7 min lezen'),
      md(NL) + fh + nl_src,
      f'<div class="cta-block"><h3>Voor de uren tussendoor</h3><p>Naast hulp: je dagen vrij, je gewoonten en de hulplijn onder één knop. Gratis te beginnen.</p><a href="https://app.afterbetting.com/onboarding" {ONCLICK}>Begin gratis</a></div>',
      cards(['Meer lezen', ('/nl/blog/gokverslaving-symptomen-en-kenmerken', 'Herkennen', 'Gokverslaving symptomen en kenmerken'),
             ('/nl/blog/goksites-blokkeren', 'Tools', 'Goksites blokkeren: telefoon, laptop en je bank'),
             ('/nl/blog/gokken-aan-je-familie-vertellen', 'Praten', 'Gokken aan je familie vertellen'),
             ('/nl/blog/gokschuld-aflossen', 'Geld', 'Gokschuld aflossen')]),
      '<div class="crisis-footer"><p>Zit je nu in crisis? Bel <strong>OpenOverGokken: 0800-2400022</strong>. Gratis, anoniem, 24 uur per dag. Denk je aan zelfmoord? Bel <strong>113</strong> (0800-0113).</p></div>',
      HREF, '2026-10-11', fld)

efh, efld = en_faq(EN_FAQ)
build('blog/block-gambling-sites-and-payments.html', 'blog/where-to-get-help-gambling-addiction.html', 'en', EN_URL,
      'Where to get help for gambling addiction in the UK',
      'Where to get help for gambling addiction: the National Gambling Helpline, NHS clinics, your GP, support groups and free debt advice. What to expect.',
      'Where to get help for gambling addiction', 'Getting help', 'https://afterbetting.com', 'https://afterbetting.com/blog',
      hero('https://afterbetting.com', 'https://afterbetting.com/blog', 'Home', 'Support', 'Where to get help for gambling addiction',
           'What is available in the UK, what it costs and what to expect.', 'By Afterbetting &middot; 11 October 2026 &middot; 7 min read'),
      md(EN) + efh + en_src(EN_SOURCES),
      f'<div class="cta"><h3>For the hours in between</h3><p>Next to support: your days free, your habits and the helpline one tap away. Start free.</p><a href="https://app.afterbetting.com/onboarding" {ONCLICK}>Start free</a></div>',
      cards(['Continue reading', ('https://afterbetting.com/blog/gambling-addiction-symptoms-and-signs', 'Signs', 'Gambling addiction symptoms and signs'),
             ('https://afterbetting.com/blog/block-gambling-sites-and-payments', 'Tools', 'How to block gambling sites, apps and bank payments'),
             ('https://afterbetting.com/blog/how-to-tell-family-about-gambling-problem', 'Support', 'How to tell someone you have a gambling problem'),
             ('https://afterbetting.com/blog/rebuild-finances-after-gambling', 'Money', 'How to pay off gambling debt and rebuild your finances')]),
      '<div class="crisis-footer"><p>In crisis right now? In the UK, call the <strong>National Gambling Helpline (GamCare) on 0808 8020 133</strong>, free, 24/7. In the Netherlands: <strong>OpenOverGokken 0800-2400022</strong>. Thinking about suicide? Call <strong>Samaritans on 116 123</strong>.</p></div>',
      HREF, '2026-10-11', efld)
