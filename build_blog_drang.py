# Bouwt nl/blog/drang-om-te-gokken en blog/do-gambling-urges-go-away (11 okt 2026), hreflang naar elkaar.
import json
from blogbuild import build, hero, cards
from opknap_en import md, faq as en_faq, src as en_src
exec(open('blog_tekst_drang.py', encoding='utf-8').read())
NL_URL = 'https://afterbetting.com/nl/blog/drang-om-te-gokken'
EN_URL = 'https://afterbetting.com/blog/do-gambling-urges-go-away'
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
build('nl/blog/goksites-blokkeren.html', 'nl/blog/drang-om-te-gokken.html', 'nl', NL_URL,
      'Drang om te gokken: wat je nu doet en wat helpt',
      'Drang om te gokken? Wat je nu doet in 15 minuten, waar drang vandaan komt, vijf dingen die helpen en of hij ooit weggaat. Uit eigen ervaring.',
      'Drang om te gokken: wat je nu doet', 'Drang om te gokken', 'https://afterbetting.com/nl/', 'https://afterbetting.com/nl/blog',
      hero('/nl/', '/nl/blog', 'Home', 'Drang', 'Drang om te gokken: wat je nu doet',
           'Drang is een golf. Hij komt op, piekt en zakt. Zo kom je erdoorheen.', 'Door Afterbetting &middot; 11 oktober 2026 &middot; 7 min lezen'),
      md(NL) + fh + nl_src,
      f'<div class="cta-block"><h3>Hulp bij drang, met één tik</h3><p>De Herstelkit in de app is gratis: 15 minuten uitstellen met timer, een bericht aan je vertrouwenspersoon en de hulplijn.</p><a href="https://app.afterbetting.com/onboarding" {ONCLICK}>Begin gratis</a></div>',
      cards(['Meer lezen', ('/nl/blog/hoe-vul-ik-mijn-tijd-zonder-gokken', 'Gewoonten', 'Hoe vul je je tijd zonder gokken?'),
             ('/nl/blog/goksites-blokkeren', 'Tools', 'Goksites blokkeren: telefoon, laptop en je bank'),
             ('/nl/blog/terugval-na-gokverslaving', 'Terugval', 'Terugval na gokverslaving. Wat nu?'),
             ('/nl/blog/stoppen-met-gokken-als-je-wint', 'Stoppen', 'Stoppen met gokken als je wint')]),
      '<div class="crisis-footer"><p>Zit je nu in crisis? Bel <strong>OpenOverGokken: 0800-2400022</strong>. Gratis, anoniem, 24 uur per dag. Denk je aan zelfmoord? Bel <strong>113</strong> (0800-0113).</p></div>',
      HREF, '2026-10-11', fld)

efh, efld = en_faq(EN_FAQ)
build('blog/block-gambling-sites-and-payments.html', 'blog/do-gambling-urges-go-away.html', 'en', EN_URL,
      'Do gambling urges go away? What helps right now',
      'Do gambling urges go away? What to do in the next 15 minutes, where urges come from, five things that help and what changes over time.',
      'Do gambling urges go away? What helps right now', 'Gambling urges', 'https://afterbetting.com', 'https://afterbetting.com/blog',
      hero('https://afterbetting.com', 'https://afterbetting.com/blog', 'Home', 'Urges', 'Do gambling urges go away? What helps right now',
           'An urge is a wave. It rises, peaks and falls. Here is how to get through it.', 'By Afterbetting &middot; 11 October 2026 &middot; 7 min read'),
      md(EN) + efh + en_src(EN_SOURCES),
      f'<div class="cta"><h3>Help with an urge, one tap away</h3><p>The recovery kit in the app is free: a 15-minute delay timer, a message to your person and the helpline.</p><a href="https://app.afterbetting.com/onboarding" {ONCLICK}>Start free</a></div>',
      cards(['Continue reading', ('https://afterbetting.com/blog/how-to-stop-gambling-urges-weekends', 'Urges', 'How to stop gambling urges at the weekend'),
             ('https://afterbetting.com/blog/block-gambling-sites-and-payments', 'Tools', 'How to block gambling sites, apps and bank payments'),
             ('https://afterbetting.com/blog/stop-gambling-when-winning', 'Quitting', 'How to stop gambling when you are winning'),
             ('https://afterbetting.com/blog/what-to-do-after-gambling-relapse', 'Relapse', 'What to do right after a gambling relapse')]),
      '<div class="crisis-footer"><p>In crisis right now? In the UK, call the <strong>National Gambling Helpline (GamCare) on 0808 8020 133</strong>, free, 24/7. In the Netherlands: <strong>OpenOverGokken 0800-2400022</strong>. Thinking about suicide? Call <strong>Samaritans on 116 123</strong>.</p></div>',
      HREF, '2026-10-11', efld)
