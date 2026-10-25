# Bouwt het NL/EN-paar van 25 okt 2026: mijn vader of moeder is gokverslaafd / my parent has a gambling problem.
# Daarna: interne links vanaf bestaande pagina's. Volledig objectief, geen founder-ervaring, geen juridisch advies.
import re, json
from blogbuild import build, hero, cards
from opknap_en import md, faq as en_faq, src as en_src
src20 = open('build_blog_okt20.py', encoding='utf-8').read()
exec(src20[src20.index("N = 'https"):src20.index('def pair(')])  # N, B, ONCLICK, crisis, nl_faq, nl_src
exec(open('blog_tekst_okt25.py', encoding='utf-8').read())
DATE, NL_DATE, EN_DATE = '2026-10-25', '25 oktober 2026', '25 October 2026'

def pair(nl_slug, en_slug, nl, en):
    href = (f'<link rel="alternate" hreflang="nl" href="{N}{nl_slug}"/>\n<link rel="alternate" hreflang="en" href="{B}{en_slug}"/>\n'
            f'<link rel="alternate" hreflang="x-default" href="{B}{en_slug}"/>')
    title, desc, h1, crumb, cat, lead, mins, body, faqs, sources, cta, rel = nl
    fh, fld = nl_faq(faqs)
    build('nl/blog/goksites-blokkeren.html', f'nl/blog/{nl_slug}.html', 'nl', N + nl_slug, title, desc, h1, crumb,
          'https://afterbetting.com/nl/', 'https://afterbetting.com/nl/blog',
          hero('/nl/', '/nl/blog', 'Home', cat, h1, lead, f'Door Afterbetting &middot; {NL_DATE} &middot; {mins} min lezen'),
          md(body) + fh + nl_src(sources),
          f'<div class="cta-block"><h3>{cta[0]}</h3><p>{cta[1]}</p><a href="https://app.afterbetting.com/onboarding" {ONCLICK}>Begin gratis</a></div>',
          cards(['Meer lezen'] + rel), NL_CRISIS, href, DATE, fld)
    title, desc, h1, crumb, cat, lead, mins, body, faqs, sources, cta, rel = en
    fh, fld = en_faq(faqs)
    build('blog/block-gambling-sites-and-payments.html', f'blog/{en_slug}.html', 'en', B + en_slug, title, desc, h1, crumb,
          'https://afterbetting.com', 'https://afterbetting.com/blog',
          hero('https://afterbetting.com', 'https://afterbetting.com/blog', 'Home', cat, h1, lead, f'By Afterbetting &middot; {EN_DATE} &middot; {mins} min read'),
          md(body) + fh + en_src(sources),
          f'<div class="cta"><h3>{cta[0]}</h3><p>{cta[1]}</p><a href="https://app.afterbetting.com/onboarding" {ONCLICK}>Start free</a></div>',
          cards(['Continue reading'] + rel), EN_CRISIS, href, DATE, fld)

pair('mijn-vader-of-moeder-is-gokverslaafd', 'my-parent-has-a-gambling-problem',
     ('Mijn vader of moeder is gokverslaafd: wat kun je doen?',
      'Je vader of moeder gokt en je weet niet wat je moet doen. Wat je wel en niet kunt doen, hoe je het gesprek begint en waar je hulp vindt.',
      'Mijn vader of moeder is gokverslaafd: wat kun je doen?', 'Vader of moeder gokverslaafd', 'Naasten',
      'Of je nog thuis woont of al jaren op jezelf: wat je wel kunt doen, wat niet, en waar je terecht kunt.', 9, NL_OUDER, NL_OUDER_FAQ,
      [('Gokhulp, informatie voor kinderen van overmatige gokkers', 'https://gokhulp.be/omgeving-kinderen'),
       ('Richtlijnen Jeugdhulp, KOPP/KOV: ingrijpende gevolgen', 'https://www.richtlijnenjeugdhulp.nl/koppkov/3-oorzaken-en-factoren/ingrijpende-gevolgen'),
       ('Rijksoverheid, waar vind ik hulp bij gokproblemen?', 'https://www.rijksoverheid.nl/vraag-en-antwoord/kansspelen/waar-vind-ik-hulp-bij-gokproblemen'),
       ('Rijksoverheid, wat moet ik doen bij huiselijk geweld?', 'https://www.rijksoverheid.nl/vraag-en-antwoord/huiselijk-geweld/wat-moet-ik-doen-bij-huiselijk-geweld'),
       ('NJi, hulp voor jongeren (De Kindertelefoon)', 'https://www.nji.nl/kennis/jeugdcriminaliteit/hulp-voor-jongeren'),
       ('Kansspelautoriteit, beleidsregels onvrijwillige inschrijving Cruks', 'https://kansspelautoriteit.nl/beleidsregels-onvrijwillige-inschrijving-cruks')],
      ('Voor je vader of moeder', 'Afterbetting geeft iemand die stopt met gokken elke dag houvast: een dagenteller, Nu hulp bij drang en een overzicht van het geld. Gratis.'),
      [('/nl/blog/omgaan-met-gokverslaafde-naaste', 'Naasten', 'Omgaan met een gokverslaafde naaste'),
       ('/nl/blog/mijn-partner-is-gokverslaafd-wat-doe-ik', 'Naasten', 'Mijn partner is gokverslaafd. Wat doe ik?'),
       ('/nl/blog/cruks-iemand-anders-inschrijven', 'Naasten', 'Cruks voor iemand anders aanvragen: zo werkt het'),
       ('/nl/blog/waarom-liegen-gokkers', 'Naasten', 'Waarom liegen gokkers?')]),
     ('My dad or mum has a gambling problem: what can I do?',
      "Your dad or mum gambles and you don't know what to do. What you can and can't change, how to start the conversation and where to find support.",
      'My dad or mum has a gambling problem: what can I do?', 'Parent with a gambling problem', 'Family',
      "Whether you still live at home or moved out years ago: what you can do, what you can't, and where to get support.", 9, EN_PARENT, EN_PARENT_FAQ,
      [('Childline, My mum is gambling', 'https://www.childline.org.uk/get-support/ask-sam/home-and-families-asksam/my-mum-is-gambling/'),
       ('National Domestic Abuse Helpline', 'https://nationaldahelpline.org.uk'),
       ('GamCare, National Gambling Helpline', 'https://www.gamcare.org.uk/get-support/talk-to-us-now/'),
       ('GamStop, Support a loved one who gambles', 'https://about.gamstop.co.uk/support-loved-one'),
       ('Richtlijnen Jeugdhulp (Dutch youth care guidelines), KOPP/KOV', 'https://www.richtlijnenjeugdhulp.nl/koppkov/3-oorzaken-en-factoren/ingrijpende-gevolgen')],
      ('For your dad or mum', 'Afterbetting gives someone who is quitting gambling daily structure: a day counter, help with urges and a money overview. Start free.'),
      [(B + 'my-partner-has-a-gambling-problem', 'Family', 'My partner has a gambling problem'),
       (B + 'exclude-someone-else-from-gambling', 'Family', 'Can you exclude someone else from gambling?'),
       (B + 'gambling-addict-lying', 'Family', 'Gambling addict lying: why it happens and how to help'),
       (B + 'gambling-addiction-symptoms-and-signs', 'Signs', 'Gambling addiction symptoms and signs')]))
print('gebouwd')

# Interne links vanaf bestaande pagina's (voor het CTA-blok, zoals 20 okt).
LINKS = [
 ('nl/blog/mijn-partner-is-gokverslaafd-wat-doe-ik.html', '/nl/blog/mijn-vader-of-moeder-is-gokverslaafd', 'Mijn vader of moeder is gokverslaafd: wat kun je doen?', 'Lees ook'),
 ('nl/blog/cruks-iemand-anders-inschrijven.html', '/nl/blog/mijn-vader-of-moeder-is-gokverslaafd', 'Mijn vader of moeder is gokverslaafd', 'Lees ook'),
 ('nl/blog/mijn-kind-is-gokverslaafd.html', '/nl/blog/mijn-vader-of-moeder-is-gokverslaafd', 'Andersom: mijn vader of moeder is gokverslaafd', 'Lees ook'),
 ('blog/my-partner-has-a-gambling-problem.html', B + 'my-parent-has-a-gambling-problem', 'My dad or mum has a gambling problem: what can I do?', 'Read next'),
 ('blog/exclude-someone-else-from-gambling.html', B + 'my-parent-has-a-gambling-problem', 'My dad or mum has a gambling problem', 'Read next'),
 ('blog/gambling-addict-lying.html', B + 'my-parent-has-a-gambling-problem', 'My dad or mum has a gambling problem: what can I do?', 'Read next'),
]
for p, href, text, label in LINKS:
    s = open(p, encoding='utf-8').read()
    if href.split('/')[-1] + '"' in s: continue
    m = re.search(r'<div class="(cta-block|cta)">', s) or re.search(r'<aside class="author-box">', s)
    s = s[:m.start()] + f'<p><strong>{label}:</strong> <a href="{href}">{text}</a></p>\n' + s[m.start():]
    s = re.sub(r'"dateModified": ?"[^"]+"', f'"dateModified": "{DATE}"', s)
    open(p, 'w', encoding='utf-8').write(s)
    print('link toegevoegd:', p)

# Naasten-hub: in de lijst per relatie en in het stuk over broer, zus, moeder of vader.
p = 'nl/blog/omgaan-met-gokverslaafde-naaste.html'
s = open(p, encoding='utf-8').read()
if 'mijn-vader-of-moeder-is-gokverslaafd' not in s:
    old = '<li><a href="https://afterbetting.com/nl/blog/mijn-vriend-is-gokverslaafd">Mijn vriend of vriendin is gokverslaafd</a>: hoe ver je gaat als vriend.</li></ul>'
    assert s.count(old) == 1
    s = s.replace(old, old[:-5] + '<li><a href="https://afterbetting.com/nl/blog/mijn-vader-of-moeder-is-gokverslaafd">Mijn vader of moeder is gokverslaafd</a>: als je ouder gokt, of je broer of zus.</li></ul>')
    old = '<p>Maak het klein. Geen familieberaad aan tafel. Een rustig gesprek, met z\'n tweeën.</p>'
    assert s.count(old) == 1
    s = s.replace(old, old + '\n<p>Alles over een gokkende ouder, ook als je nog thuis woont, lees je in <a href="https://afterbetting.com/nl/blog/mijn-vader-of-moeder-is-gokverslaafd">mijn vader of moeder is gokverslaafd</a>.</p>')
    s = re.sub(r'"dateModified": ?"[^"]+"', f'"dateModified": "{DATE}"', s)
    open(p, 'w', encoding='utf-8').write(s)
    print('hub bijgewerkt')
