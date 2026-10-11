# Bouwt nl/blog/goksites-blokkeren en blog/block-gambling-sites-and-payments (11 okt 2026), hreflang naar elkaar.
import json
from blogbuild import build, hero, cards
exec(open('blog_tekst_goksites.py', encoding='utf-8').read())
exec(open('blog_tekst_block_gambling_en.py', encoding='utf-8').read())
URL = 'https://afterbetting.com/nl/blog/goksites-blokkeren'
EN_URL = 'https://afterbetting.com/blog/block-gambling-sites-and-payments'
HREF = (f'<link rel="alternate" hreflang="nl" href="{URL}"/>\n<link rel="alternate" hreflang="en" href="{EN_URL}"/>\n'
        f'<link rel="alternate" hreflang="x-default" href="{EN_URL}"/>')
def faq_parts(faq, title):
    html = f'<h2>{title}</h2>\n' + ''.join(f'<h3>{q}</h3>\n<p>{a.replace("&", "&amp;")}</p>\n' for q, a in faq)
    ld = '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}, ensure_ascii=False) + '</script>\n'
    return html, ld
def src_parts(sources, title):
    return f'<h2>{title}</h2>\n<ul>' + ''.join(f'<li><a href="{u}" rel="noopener">{t}</a></li>' for t, u in sources) + '</ul>'
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

en_faq_html, en_faq_ld = faq_parts(EN_FAQ, 'Frequently asked questions')
build('blog/does-self-exclusion-work-gambling.html', 'blog/block-gambling-sites-and-payments.html', 'en', EN_URL,
      'How to block gambling sites, apps and bank payments',
      'Block gambling on your phone, laptop and bank card. Which UK banks have a gambling block, how long it takes to turn off, and how to hand over the key.',
      'How to block gambling sites, apps and bank payments', 'Block gambling sites and payments', 'https://afterbetting.com', 'https://afterbetting.com/blog',
      hero('https://afterbetting.com', 'https://afterbetting.com/blog', 'Home', 'Tools', 'How to block gambling sites, apps and bank payments',
           'What works on your phone, your laptop and your bank card. And where the gaps are.',
           'By Afterbetting &middot; 11 October 2026 &middot; 9 min read'),
      EN_BODY + en_faq_html + src_parts(EN_SOURCES, 'Sources'),
      '<div class="cta"><h3>Blocking is step one</h3><p>The app helps with the rest: your days, your money back in order and help one tap away when the urge comes.</p><a href="https://app.afterbetting.com/onboarding" onclick="if(window.gtag)gtag(\'event\',\'cta_click\',{cta_location:\'article_cta\',page_path:location.pathname})">Start free</a></div>',
      cards(['Continue reading', ('https://afterbetting.com/blog/cancel-gamstop-early', 'Crisis', 'Can you cancel GamStop early? Read this first'),
             ('https://afterbetting.com/blog/does-self-exclusion-work-gambling', 'Tools', 'Does self-exclusion actually work for gambling addiction?'),
             ('https://afterbetting.com/blog/rebuild-finances-after-gambling', 'Money', 'Rebuilding your finances after gambling'),
             ('https://afterbetting.com/blog/what-to-do-instead-of-gambling', 'Habits', 'What to do instead of gambling')]),
      '<div class="crisis-footer"><p>In crisis right now? In the UK, call the <strong>National Gambling Helpline (GamCare) on 0808 8020 133</strong>, free, 24/7. In the Netherlands: <strong>OpenOverGokken 0800-2400022</strong>. Thinking about suicide? Call <strong>Samaritans on 116 123</strong>.</p></div>',
      HREF, '2026-10-11', en_faq_ld)
