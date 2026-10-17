# Bouwt 2 NL/EN-paren (17 okt 2026): verlies terugwinnen / chasing losses en afkickverschijnselen / gambling withdrawal.
import json
from blogbuild import build, hero, cards
from opknap_en import md, faq as en_faq, src as en_src
ONCLICK = 'onclick="if(window.gtag)gtag(\'event\',\'cta_click\',{cta_location:\'article_cta\',page_path:location.pathname})"'
NL_CRISIS = '<div class="crisis-footer"><p>Zit je nu in crisis? Bel <strong>OpenOverGokken: 0800-2400022</strong>. Gratis, anoniem, 24 uur per dag. Denk je aan zelfmoord? Bel <strong>113</strong> (0800-0113).</p></div>'
EN_CRISIS = ('<div class="crisis-footer"><p>In crisis right now? In the UK, call the <strong>National Gambling Helpline (GamCare) on 0808 8020 133</strong>, free, 24/7. '
             'In the Netherlands: <strong>OpenOverGokken 0800-2400022</strong>. Thinking about suicide? Call <strong>Samaritans on 116 123</strong>.</p></div>')

def nl_faq(items):
    html = '<h2>Veelgestelde vragen</h2>\n' + ''.join(f'<h3>{q}</h3>\n<p>{a}</p>\n' for q, a in items)
    ld = '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}, ensure_ascii=False) + '</script>\n'
    return html, ld

def pair(textfile, nl_slug, en_slug, nl, en):
    g = {}; exec(open(textfile, encoding='utf-8').read(), g)
    nu = f'https://afterbetting.com/nl/blog/{nl_slug}'; eu = f'https://afterbetting.com/blog/{en_slug}'
    href = (f'<link rel="alternate" hreflang="nl" href="{nu}"/>\n<link rel="alternate" hreflang="en" href="{eu}"/>\n'
            f'<link rel="alternate" hreflang="x-default" href="{eu}"/>')
    fh, fld = nl_faq(g['NL_FAQ'])
    nsrc = '<h2>Bronnen</h2>\n<ul>' + ''.join(f'<li><a href="{u}" rel="noopener">{t}</a></li>' for t, u in g['NL_SOURCES']) + '</ul>\n'
    build('nl/blog/goksites-blokkeren.html', f'nl/blog/{nl_slug}.html', 'nl', nu, nl['title'], nl['desc'], nl['h1'], nl['crumb'],
          'https://afterbetting.com/nl/', 'https://afterbetting.com/nl/blog',
          hero('/nl/', '/nl/blog', 'Home', nl['cat'], nl['h1'], nl['lead'], f"Door de oprichter van Afterbetting &middot; 17 oktober 2026 &middot; {nl['mins']} min lezen"),
          md(g['NL']) + fh + nsrc,
          f'<div class="cta-block"><h3>{nl["cta"][0]}</h3><p>{nl["cta"][1]}</p><a href="https://app.afterbetting.com/onboarding" {ONCLICK}>Begin gratis</a></div>',
          cards(['Meer lezen'] + nl['rel']), NL_CRISIS, href, '2026-10-17', fld)
    efh, efld = en_faq(g['EN_FAQ'])
    build('blog/block-gambling-sites-and-payments.html', f'blog/{en_slug}.html', 'en', eu, en['title'], en['desc'], en['h1'], en['crumb'],
          'https://afterbetting.com', 'https://afterbetting.com/blog',
          hero('https://afterbetting.com', 'https://afterbetting.com/blog', 'Home', en['cat'], en['h1'], en['lead'], f"By the founder of Afterbetting &middot; 17 October 2026 &middot; {en['mins']} min read"),
          md(g['EN']) + efh + en_src(g['EN_SOURCES']),
          f'<div class="cta"><h3>{en["cta"][0]}</h3><p>{en["cta"][1]}</p><a href="https://app.afterbetting.com/onboarding" {ONCLICK}>Start free</a></div>',
          cards(['Continue reading'] + en['rel']), EN_CRISIS, href, '2026-10-17', efld)

B = 'https://afterbetting.com/blog/'
pair('blog_tekst_terugwinnen.py', 'verlies-terugwinnen-gokken', 'chasing-losses-gambling',
     dict(title='Verlies terugwinnen met gokken: waarom het nooit lukt',
          desc='Ik won ooit 68.000 euro en vergokte alles. Daarna joeg ik jaren mijn verlies na. Waarom terugwinnen niet werkt en wat je in plaats daarvan doet.',
          h1='Verlies terugwinnen met gokken: waarom het nooit lukt', crumb='Verlies terugwinnen', cat='Stoppen', mins=8,
          lead='Ik won ooit 68.000 euro. Daarna joeg ik jaren mijn verlies na. Wat ik daarvan leerde.',
          cta=('Stoppen met najagen', 'Je dagen zonder gokken, hulp bij drang en een eerlijk beeld van je geld. Gratis te beginnen.'),
          rel=[('/nl/blog/stoppen-met-gokken-als-je-wint', 'Stoppen', 'Stoppen met gokken als je wint'),
               ('/nl/blog/van-gokschuld-naar-nul', 'Geld', 'Van 40k gokschuld naar nul'),
               ('/nl/blog/drang-om-te-gokken', 'Drang', 'Drang om te gokken: wat je nu doet'),
               ('/nl/blog/salaris-vergokt-wat-nu', 'Crisis', 'Salaris vergokt, wat nu?')]),
     dict(title='Chasing losses in gambling: why it never works',
          desc='I once won €68,000 and gambled it all away. Then I spent years chasing my losses. Why winning it back never works, and what to do instead.',
          h1='Chasing losses in gambling: why it never works', crumb='Chasing losses', cat='Quitting', mins=8,
          lead='I once won €68,000. Then I spent years chasing it. What I learned.',
          cta=('Stop chasing', 'Your days without gambling, help when an urge hits, and an honest view of your money. Start free.'),
          rel=[(B + 'stop-gambling-when-winning', 'Quitting', 'How to stop gambling when you are winning'),
               (B + 'paid-off-gambling-debt', 'Money', 'How I paid off my gambling debt'),
               (B + 'do-gambling-urges-go-away', 'Urges', 'Do gambling urges go away?'),
               (B + 'gambled-away-paycheck-what-now', 'Crisis', 'Gambled away your paycheck? What now')]))

pair('blog_tekst_afkick.py', 'afkickverschijnselen-gokken', 'gambling-withdrawal-symptoms',
     dict(title='Afkickverschijnselen bij stoppen met gokken',
          desc='Leegte, onrust, slecht slapen, triggers. Wat ik merkte in de eerste weken na het stoppen met gokken, hoe lang het duurde en wat hielp.',
          h1='Afkickverschijnselen bij stoppen met gokken: wat je kunt verwachten', crumb='Afkickverschijnselen', cat='Herstel', mins=8,
          lead='Leegte, triggers en wakker liggen. Wat ik merkte in de eerste weken, en wat hielp.',
          cta=('Voor de lastige uren', 'Een vast ritme, oefeningen voor als de drang opkomt en de hulplijn onder één knop. Gratis te beginnen.'),
          rel=[('/nl/blog/eerste-week-stoppen-met-gokken', 'Herstel', 'De eerste week stoppen met gokken'),
               ('/nl/blog/eerste-30-dagen-zonder-gokken', 'Herstel', 'De eerste 30 dagen zonder gokken'),
               ('/nl/blog/slaapproblemen-stoppen-met-gokken', 'Slaap', 'Slaapproblemen na stoppen met gokken'),
               ('/nl/blog/gokverslaving-hulp-zoeken', 'Hulp', 'Hulp bij gokverslaving: waar je terechtkunt')]),
     dict(title='Gambling withdrawal symptoms: what to expect',
          desc='Emptiness, restlessness, poor sleep, triggers. What I noticed in the first weeks after I stopped gambling, how long it lasted and what helped.',
          h1='Gambling withdrawal symptoms: what to expect when you stop', crumb='Gambling withdrawal', cat='Recovery', mins=8,
          lead='Emptiness, triggers and lying awake. What I noticed in the first weeks, and what helped.',
          cta=('For the hard hours', 'A steady routine, exercises for when an urge hits and the helpline one tap away. Start free.'),
          rel=[(B + 'first-week-without-gambling', 'Recovery', 'Your first week without gambling'),
               (B + 'first-30-days-without-gambling', 'Recovery', 'The first 30 days without gambling'),
               (B + 'sleep-after-stopping-gambling', 'Sleep', 'Sleep after stopping gambling'),
               (B + 'where-to-get-help-gambling-addiction', 'Support', 'Where to get help for gambling addiction')]))
