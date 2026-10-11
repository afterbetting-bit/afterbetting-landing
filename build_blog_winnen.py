# Bouwt nl/blog/stoppen-met-gokken-als-je-wint en blog/stop-gambling-when-winning (11 okt 2026), hreflang naar elkaar.
import json
from blogbuild import build, hero, cards
from opknap_en import md, faq as en_faq, src as en_src
exec(open('blog_tekst_winnen.py', encoding='utf-8').read())
NL_URL = 'https://afterbetting.com/nl/blog/stoppen-met-gokken-als-je-wint'
EN_URL = 'https://afterbetting.com/blog/stop-gambling-when-winning'
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
build('nl/blog/goksites-blokkeren.html', 'nl/blog/stoppen-met-gokken-als-je-wint.html', 'nl', NL_URL,
      'Stoppen met gokken als je wint: zo houd je het',
      'Stoppen met gokken als je aan het winnen bent voelt onmogelijk. Waarom dat zo is, en wat je vandaag doet met je winst. Uit eigen ervaring.',
      'Stoppen met gokken als je wint', 'Stoppen als je wint', 'https://afterbetting.com/nl/', 'https://afterbetting.com/nl/blog',
      hero('/nl/', '/nl/blog', 'Home', 'Stoppen', 'Stoppen met gokken als je wint',
           'Het voelt als het slechtste moment om te stoppen. Het is het beste.', 'Door Afterbetting &middot; 11 oktober 2026 &middot; 7 min lezen'),
      md(NL) + fh + nl_src,
      f'<div class="cta-block"><h3>Houd je winst</h3><p>Zet je dagen vrij, je geld en je schulden op één plek. Bij drang heb je met één tik een timer en de hulplijn.</p><a href="https://app.afterbetting.com/onboarding" {ONCLICK}>Begin gratis</a></div>',
      cards(['Meer lezen', ('/nl/blog/goksites-blokkeren', 'Tools', 'Goksites blokkeren: telefoon, laptop en je bank'),
             ('/nl/blog/gokschuld-aflossen', 'Geld', 'Gokschuld aflossen'),
             ('/nl/blog/hoe-stop-ik-met-gokken-met-schulden', 'Geld', 'Hoe stop ik met gokken als ik schulden heb?'),
             ('/nl/blog/sportgokken-verslaving', 'Herkennen', 'Sportgokken verslaving: hoe je hier eerlijk naar kijkt')]),
      '<div class="crisis-footer"><p>Zit je nu in crisis? Bel <strong>OpenOverGokken: 0800-2400022</strong>. Gratis, anoniem, 24 uur per dag. Denk je aan zelfmoord? Bel <strong>113</strong> (0800-0113).</p></div>',
      HREF, '2026-10-11', fld)

efh, efld = en_faq(EN_FAQ)
build('blog/block-gambling-sites-and-payments.html', 'blog/stop-gambling-when-winning.html', 'en', EN_URL,
      'How to stop gambling when you are winning',
      'Stopping when you are winning feels impossible. Why that is, and what to do with your winnings today. From someone who gambled for 8 years.',
      'How to stop gambling when you are winning', 'Stop gambling when winning', 'https://afterbetting.com', 'https://afterbetting.com/blog',
      hero('https://afterbetting.com', 'https://afterbetting.com/blog', 'Home', 'Quitting', 'How to stop gambling when you are winning',
           'It feels like the worst moment to stop. It is the best one.', 'By Afterbetting &middot; 11 October 2026 &middot; 7 min read'),
      md(EN) + efh + en_src(EN_SOURCES),
      f'<div class="cta"><h3>Keep this win</h3><p>Your days free, your money and your debts in one place. Help one tap away when the urge comes.</p><a href="https://app.afterbetting.com/onboarding" {ONCLICK}>Start free</a></div>',
      cards(['Continue reading', ('https://afterbetting.com/blog/block-gambling-sites-and-payments', 'Tools', 'How to block gambling sites, apps and bank payments'),
             ('https://afterbetting.com/blog/rebuild-finances-after-gambling', 'Money', 'How to pay off gambling debt and rebuild your finances'),
             ('https://afterbetting.com/blog/sports-betting-addiction-quit', 'Quitting', 'How to quit sports betting when you cannot stop watching'),
             ('https://afterbetting.com/blog/what-to-do-after-gambling-relapse', 'Relapse', 'What to do right after a gambling relapse')]),
      '<div class="crisis-footer"><p>In crisis right now? In the UK, call the <strong>National Gambling Helpline (GamCare) on 0808 8020 133</strong>, free, 24/7. In the Netherlands: <strong>OpenOverGokken 0800-2400022</strong>. Thinking about suicide? Call <strong>Samaritans on 116 123</strong>.</p></div>',
      HREF, '2026-10-11', efld)
