# Bouwt nl/blog/van-gokschuld-naar-nul en blog/paid-off-gambling-debt (17 okt 2026), hreflang naar elkaar.
import json
from blogbuild import build, hero, cards
from opknap_en import md, faq as en_faq, src as en_src
exec(open('blog_tekst_schuld.py', encoding='utf-8').read())
NL_URL = 'https://afterbetting.com/nl/blog/van-gokschuld-naar-nul'
EN_URL = 'https://afterbetting.com/blog/paid-off-gambling-debt'
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
H1_NL = 'Van 40k gokschuld naar nul: hoe ik mijn gokschulden heb afgelost'
build('nl/blog/goksites-blokkeren.html', 'nl/blog/van-gokschuld-naar-nul.html', 'nl', NL_URL,
      'Van 40k gokschuld naar nul: zo heb ik alles afgelost',
      'Ik gokte 8 jaar en had meer dan 40.000 euro schuld. In bijna 2 jaar heb ik alles afgelost. Hoe ik dat deed, wat het kostte en wat het me opleverde.',
      H1_NL, 'Gokschuld afgelost', 'https://afterbetting.com/nl/', 'https://afterbetting.com/nl/blog',
      hero('/nl/', '/nl/blog', 'Home', 'Geld', H1_NL,
           'Meer dan 8 jaar gokken, meer dan 40.000 euro schuld, bijna 2 jaar aflossen. Wat ik deed en wat ik ervan leerde.',
           'Door de oprichter van Afterbetting &middot; 17 oktober 2026 &middot; 9 min lezen'),
      md(NL) + fh + nl_src,
      f'<div class="cta-block"><h3>Herstel en geld op één plek</h3><p>Je dagen zonder gokken, hulp bij drang en je schuld die kleiner wordt. Gratis te beginnen.</p><a href="https://app.afterbetting.com/onboarding" {ONCLICK}>Begin gratis</a></div>',
      cards(['Meer lezen', ('/nl/blog/gokschuld-aflossen', 'Geld', 'Gokschuld aflossen'),
             ('/nl/blog/sneeuwbalmethode-gokschulden', 'Geld', 'De sneeuwbalmethode voor gokschulden'),
             ('/nl/blog/stoppen-met-gokken-als-je-wint', 'Stoppen', 'Stoppen met gokken als je wint'),
             ('/nl/blog/gokverslaving-hulp-zoeken', 'Hulp', 'Hulp bij gokverslaving: waar je terechtkunt')]),
      '<div class="crisis-footer"><p>Zit je nu in crisis? Bel <strong>OpenOverGokken: 0800-2400022</strong>. Gratis, anoniem, 24 uur per dag. Denk je aan zelfmoord? Bel <strong>113</strong> (0800-0113).</p></div>',
      HREF, '2026-10-17', fld)

efh, efld = en_faq(EN_FAQ)
H1_EN = 'How I paid off my gambling debt: from €40k to zero'
build('blog/block-gambling-sites-and-payments.html', 'blog/paid-off-gambling-debt.html', 'en', EN_URL,
      'How I paid off €40k of gambling debt in two years',
      'I gambled for 8 years and owed more than €40,000. It took me almost two years to pay it all off. How I did it, what was hard and what I learned.',
      H1_EN, 'Paid off gambling debt', 'https://afterbetting.com', 'https://afterbetting.com/blog',
      hero('https://afterbetting.com', 'https://afterbetting.com/blog', 'Home', 'Money', H1_EN,
           'Eight years of gambling, more than €40,000 owed, almost two years of paying it off. What I did and what I learned.',
           'By the founder of Afterbetting &middot; 17 October 2026 &middot; 9 min read'),
      md(EN) + efh + en_src(EN_SOURCES),
      f'<div class="cta"><h3>Recovery and money in one place</h3><p>Your days without gambling, help when an urge hits, and your debt getting smaller. Start free.</p><a href="https://app.afterbetting.com/onboarding" {ONCLICK}>Start free</a></div>',
      cards(['Continue reading', ('https://afterbetting.com/blog/rebuild-finances-after-gambling', 'Money', 'How to pay off gambling debt and rebuild your finances'),
             ('https://afterbetting.com/blog/snowball-debt-payoff-gambling', 'Money', 'Snowball or avalanche: paying off gambling debt'),
             ('https://afterbetting.com/blog/stop-gambling-when-winning', 'Quitting', 'How to stop gambling when you are winning'),
             ('https://afterbetting.com/blog/where-to-get-help-gambling-addiction', 'Support', 'Where to get help for gambling addiction')]),
      '<div class="crisis-footer"><p>In crisis right now? In the UK, call the <strong>National Gambling Helpline (GamCare) on 0808 8020 133</strong>, free, 24/7. In the Netherlands: <strong>OpenOverGokken 0800-2400022</strong>. Thinking about suicide? Call <strong>Samaritans on 116 123</strong>.</p></div>',
      HREF, '2026-10-17', efld)
