# Bouwt drie NL/EN-paren (20 okt 2026): Cruks voor iemand anders, gokschuld en hypotheek, gokken en alcohol.
import json
from blogbuild import build, hero, cards
from opknap_en import md, faq as en_faq, src as en_src
exec(open('blog_tekst_okt20.py', encoding='utf-8').read())
N = 'https://afterbetting.com/nl/blog/'; B = 'https://afterbetting.com/blog/'
ONCLICK = 'onclick="if(window.gtag)gtag(\'event\',\'cta_click\',{cta_location:\'article_cta\',page_path:location.pathname})"'
NL_CRISIS = '<div class="crisis-footer"><p>Zit je nu in crisis? Bel <strong>OpenOverGokken: 0800-2400022</strong>. Gratis, anoniem, 24 uur per dag. Denk je aan zelfmoord? Bel <strong>113</strong> (0800-0113).</p></div>'
EN_CRISIS = ('<div class="crisis-footer"><p>In crisis right now? In the UK, call the <strong>National Gambling Helpline (GamCare) on 0808 8020 133</strong>, free, 24/7. '
             'In the Netherlands: <strong>OpenOverGokken 0800-2400022</strong>. Thinking about suicide? Call <strong>Samaritans on 116 123</strong>.</p></div>')

def nl_faq(items):
    html = '<h2>Veelgestelde vragen</h2>\n' + ''.join(f'<h3>{q}</h3>\n<p>{a}</p>\n' for q, a in items)
    ld = '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}, ensure_ascii=False) + '</script>\n'
    return html, ld

def nl_src(items):
    return '<h2>Bronnen</h2>\n<ul>' + ''.join(f'<li><a href="{u}" rel="noopener">{t}</a></li>' for t, u in items) + '</ul>\n'

def pair(nl_slug, en_slug, nl, en):
    href = (f'<link rel="alternate" hreflang="nl" href="{N}{nl_slug}"/>\n<link rel="alternate" hreflang="en" href="{B}{en_slug}"/>\n'
            f'<link rel="alternate" hreflang="x-default" href="{B}{en_slug}"/>')
    title, desc, h1, crumb, cat, lead, mins, body, faqs, sources, cta, rel = nl
    fh, fld = nl_faq(faqs)
    build('nl/blog/goksites-blokkeren.html', f'nl/blog/{nl_slug}.html', 'nl', N + nl_slug, title, desc, h1, crumb,
          'https://afterbetting.com/nl/', 'https://afterbetting.com/nl/blog',
          hero('/nl/', '/nl/blog', 'Home', cat, h1, lead, f'Door Afterbetting &middot; 20 oktober 2026 &middot; {mins} min lezen'),
          md(body) + fh + nl_src(sources),
          f'<div class="cta-block"><h3>{cta[0]}</h3><p>{cta[1]}</p><a href="https://app.afterbetting.com/onboarding" {ONCLICK}>Begin gratis</a></div>',
          cards(['Meer lezen'] + rel), NL_CRISIS, href, '2026-10-20', fld)
    title, desc, h1, crumb, cat, lead, mins, body, faqs, sources, cta, rel = en
    fh, fld = en_faq(faqs)
    build('blog/block-gambling-sites-and-payments.html', f'blog/{en_slug}.html', 'en', B + en_slug, title, desc, h1, crumb,
          'https://afterbetting.com', 'https://afterbetting.com/blog',
          hero('https://afterbetting.com', 'https://afterbetting.com/blog', 'Home', cat, h1, lead, f'By Afterbetting &middot; 20 October 2026 &middot; {mins} min read'),
          md(body) + fh + en_src(sources),
          f'<div class="cta"><h3>{cta[0]}</h3><p>{cta[1]}</p><a href="https://app.afterbetting.com/onboarding" {ONCLICK}>Start free</a></div>',
          cards(['Continue reading'] + rel), EN_CRISIS, href, '2026-10-20', fld)

KSA = ('Kansspelautoriteit, Beleidsregels onvrijwillige inschrijving Cruks', 'https://kansspelautoriteit.nl/beleidsregels-onvrijwillige-inschrijving-cruks')
pair('cruks-iemand-anders-inschrijven', 'exclude-someone-else-from-gambling',
     ('Cruks voor iemand anders aanvragen: zo werkt het',
      'Kun je iemand anders in Cruks laten inschrijven? Wie het mag aanvragen, wat de KSA vraagt, hoe lang het duurt en wat je eerst kunt proberen.',
      'Cruks voor iemand anders aanvragen: zo werkt het', 'Cruks voor iemand anders', 'Naasten',
      'Wat wel kan, wat niet kan, en wat je eerst probeert.', 8, NL_CRUKS, NL_CRUKS_FAQ,
      [KSA, ('CasinoNieuws.nl, Beleidsregels onvrijwillige registratie Cruks', 'https://www.casinonieuws.nl/politiek/ksa-beleidsregels-onvrijwillige-inschrijving-cruks/'),
       ('Cruksregister', 'https://cruksregister.nl/')],
      ('Laat het zien aan wie je lief is', 'Afterbetting geeft iemand die stopt met gokken elke dag houvast: een dagenteller, Nu hulp bij drang en een overzicht van het geld. Gratis.'),
      [('/nl/blog/mijn-partner-is-gokverslaafd-wat-doe-ik', 'Naasten', 'Mijn partner is gokverslaafd. Wat doe ik?'),
       ('/nl/blog/omgaan-met-gokverslaafde-naaste', 'Naasten', 'Omgaan met een gokverslaafde naaste'),
       ('/nl/blog/cruks-opzeggen', 'Crisis', 'Cruks opzeggen: zo werkt het, en lees dit eerst'),
       ('/nl/blog/waarom-liegen-gokkers', 'Naasten', 'Waarom liegen gokkers?')]),
     ('Can you exclude someone else from gambling?',
      'Can you put someone else on GamStop? The honest answer for the UK, what you can do today to protect yourself, and how to ask them to do it themselves.',
      'Can you exclude someone else from gambling?', 'Exclude someone else', 'Family',
      'What you can do, what you cannot, and what to try first.', 7, EN_EXCL, EN_EXCL_FAQ,
      [('GamStop, Support a loved one who gambles', 'https://about.gamstop.co.uk/support-loved-one'),
       ('GamCare, National Gambling Helpline', 'https://www.gamcare.org.uk/get-support/talk-to-us-now/'), KSA],
      ('Show it to the person you love', 'Afterbetting gives someone who is quitting gambling daily structure: a day counter, help with urges and a money overview. Start free.'),
      [(B + 'my-partner-has-a-gambling-problem', 'Family', 'My partner has a gambling problem'),
       (B + 'gambling-addict-lying', 'Family', 'Gambling addict lying: why it happens and how to help'),
       (B + 'block-gambling-sites-and-payments', 'Tools', 'How to block gambling sites, apps and bank payments'),
       (B + 'where-to-get-help-gambling-addiction', 'Support', 'Where to get help for gambling addiction')]))

pair('gokschuld-bkr-hypotheek', 'will-gambling-affect-my-mortgage',
     ('Gokschuld en BKR: krijg je nog een hypotheek?',
      'Gokschuld afgelost en toch geen hypotheek? Wat er in je BKR staat, hoe lang het blijft, wat je zelf kunt doen en waar je voor oppast.',
      'Gokschuld en BKR: krijg je nog een hypotheek?', 'Gokschuld en BKR', 'Geld',
      'Afgelost is niet hetzelfde als verdwenen. Wat je kunt doen terwijl je wacht.', 8, NL_BKR, NL_BKR_FAQ,
      [('BKR, veelgestelde vragen', 'https://www.mijnkredietregistratie.nl/nl/veelgestelde-vragen'), ('Geldfit', 'https://www.geldfit.nl/')],
      ('Zie je schulden kleiner worden', 'Zet je schulden naast je dagen zonder gokken en zie de lijn maand voor maand dalen. Gratis te beginnen.'),
      [('/nl/blog/gokschuld-aflossen', 'Geld', 'Gokschuld aflossen'),
       ('/nl/blog/van-gokschuld-naar-nul', 'Geld', 'Van 40k gokschuld naar nul'),
       ('/nl/blog/sneeuwbalmethode-gokschulden', 'Geld', 'De sneeuwbalmethode voor gokschulden'),
       ('/nl/blog/hoeveel-heb-ik-vergokt', 'Geld', 'Hoeveel heb ik vergokt?')]),
     ('Will gambling affect my mortgage application?',
      'Will gambling affect your mortgage? What lenders see on your bank statements and credit file, how long defaults last, and what to do now.',
      'Will gambling affect my mortgage application?', 'Gambling and mortgages', 'Money',
      'What lenders see, how long it lasts, and what you can do while you wait.', 8, EN_MORT, EN_MORT_FAQ,
      [('Charcol, Does gambling affect a mortgage application?', 'https://www.charcol.co.uk/blog/does-gambling-affect-a-mortgage-application-in-the-uk/'),
       ('Experian, Dealing with defaults on your credit report', 'https://www.experian.co.uk/consumer/questions/credit-and-debt.html'),
       ('StepChange', 'https://www.stepchange.org/')],
      ('Your debts, going down', 'See your debts next to your days free, and watch the line go down month by month. Start free.'),
      [(B + 'rebuild-finances-after-gambling', 'Money', 'How to pay off gambling debt and rebuild your finances'),
       (B + 'paid-off-gambling-debt', 'Money', 'How I paid off my gambling debt'),
       (B + 'snowball-debt-payoff-gambling', 'Money', 'Snowball or avalanche for gambling debt?'),
       (B + 'how-much-have-i-lost-gambling', 'Money', 'How much have I lost gambling?')]))

pair('gokken-en-alcohol', 'gambling-and-alcohol',
     ('Gokken en alcohol: waarom drank de drang groter maakt',
      'Merk je dat je na een paar drankjes sneller gaat gokken? Waarom alcohol en gokken samen zo lastig zijn, en wat je kunt doen. Van een ervaringsdeskundige.',
      'Gokken en alcohol: waarom drank de drang groter maakt', 'Gokken en alcohol', 'Drang',
      'Waarom die twee elkaar versterken, en hoe je je sloten zet voordat je drinkt.', 7, NL_ALC, NL_ALC_FAQ,
      [('Jellinek, verslavingszorg voor gokken en alcohol', 'https://www.jellinek.nl'), ('OpenOverGokken', 'https://www.openovergokken.nl/')],
      ('Drang op dit moment?', 'In de app staat Nu hulp: een korte timer, je eigen redenen om te stoppen en de hulplijn, één tik weg. Gratis.'),
      [('/nl/blog/drang-om-te-gokken', 'Drang', 'Drang om te gokken: wat je nu doet'),
       ('/nl/blog/goksites-blokkeren', 'Tools', 'Goksites blokkeren: telefoon, laptop en je bank'),
       ('/nl/blog/hoe-vul-ik-mijn-tijd-zonder-gokken', 'Gewoonten', 'Hoe vul ik mijn tijd zonder gokken?'),
       ('/nl/blog/terugval-na-gokverslaving', 'Terugval', 'Terugval na gokverslaving. Wat nu?')]),
     ('Gambling and alcohol: why drinking makes urges worse',
      'Do you gamble more after a few drinks? Why alcohol and gambling feed each other, and how to set your locks before you drink. From a former gambler.',
      'Gambling and alcohol: why drinking makes the urge worse', 'Gambling and alcohol', 'Urges',
      'Why the two feed each other, and how to set your locks before you drink.', 7, EN_ALC, EN_ALC_FAQ,
      [('NHS, Help for problems with gambling', 'https://www.nhs.uk/live-well/addiction-support/gambling-addiction/'),
       ('NHS, Alcohol support', 'https://www.nhs.uk/live-well/alcohol-advice/alcohol-support/')],
      ('Help with an urge, one tap away', 'The recovery kit in the app is free: a 15-minute delay timer, a message to your person and the helpline.'),
      [(B + 'do-gambling-urges-go-away', 'Urges', 'Do gambling urges go away?'),
       (B + 'block-gambling-sites-and-payments', 'Tools', 'How to block gambling sites, apps and bank payments'),
       (B + 'what-to-do-after-gambling-relapse', 'Relapse', 'What to do right after a gambling relapse'),
       (B + 'chasing-losses-gambling', 'Quitting', 'Chasing losses in gambling: why it never works')]))
print('gebouwd')

# interne links vanaf bestaande pagina's
LINKS = [
 ('nl/blog/mijn-partner-is-gokverslaafd-wat-doe-ik.html', '/nl/blog/cruks-iemand-anders-inschrijven', 'Cruks voor iemand anders aanvragen: zo werkt het', 'Lees ook'),
 ('nl/blog/cruks-opzeggen.html', '/nl/blog/cruks-iemand-anders-inschrijven', 'Cruks voor iemand anders aanvragen', 'Lees ook'),
 ('nl/blog/gokschuld-aflossen.html', '/nl/blog/gokschuld-bkr-hypotheek', 'Gokschuld en BKR: krijg je nog een hypotheek?', 'Lees ook'),
 ('nl/blog/drang-om-te-gokken.html', '/nl/blog/gokken-en-alcohol', 'Gokken en alcohol: waarom drank de drang groter maakt', 'Lees ook'),
 ('blog/my-partner-has-a-gambling-problem.html', B + 'exclude-someone-else-from-gambling', 'Can you exclude someone else from gambling?', 'Read next'),
 ('blog/rebuild-finances-after-gambling.html', B + 'will-gambling-affect-my-mortgage', 'Will gambling affect my mortgage application?', 'Read next'),
 ('blog/do-gambling-urges-go-away.html', B + 'gambling-and-alcohol', 'Gambling and alcohol: why drinking makes the urge worse', 'Read next'),
]
import re
for p, href, text, label in LINKS:
    s = open(p, encoding='utf-8').read()
    if href.split('/')[-1] in s: continue
    m = re.search(r'<div class="(cta-block|cta)">', s)
    s = s[:m.start()] + f'<p><strong>{label}:</strong> <a href="{href}">{text}</a></p>\n' + s[m.start():]
    s = re.sub(r'"dateModified": ?"[^"]+"', '"dateModified": "2026-10-20"', s)
    open(p, 'w', encoding='utf-8').write(s)
    print('link toegevoegd:', p)
