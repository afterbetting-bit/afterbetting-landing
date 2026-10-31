# Bouwt de drie NL/EN-paren van 31 okt 2026: waarom kan ik niet stoppen, stoppen en sparen, lotgenoten/support groups.
# Daarna interne links vanaf bestaande pagina's. Teksten goedgekeurd door de founder (31 okt).
import re, json, html
from blogbuild import build, hero, cards
from opknap_en import md, faq as en_faq, src as en_src
src20 = open('build_blog_okt20.py', encoding='utf-8').read()
exec(src20[src20.index("N = 'https"):src20.index('def pair(')])  # N, B, ONCLICK, crisis, nl_faq, nl_src
exec(open('blog_tekst_okt31.py', encoding='utf-8').read())
DATE, NL_DATE, EN_DATE = '2026-10-31', '31 oktober 2026', '31 October 2026'

def h1(path):  # kaarttekst uit de bestaande pagina
    return html.unescape(re.search(r'<h1>(.*?)</h1>', open(path, encoding='utf-8').read()).group(1))
def rel(items, lang):
    return [((N if lang == 'nl' else B) + slug if lang == 'en' else '/nl/blog/' + slug, cat, h1(('nl/blog/' if lang == 'nl' else 'blog/') + slug + '.html')) for slug, cat in items]
def mins(t): return max(5, round(len(t.split()) / 200))

def pair(nl_slug, en_slug, nl, en):
    href = (f'<link rel="alternate" hreflang="nl" href="{N}{nl_slug}"/>\n<link rel="alternate" hreflang="en" href="{B}{en_slug}"/>\n'
            f'<link rel="alternate" hreflang="x-default" href="{B}{en_slug}"/>')
    title, desc, head, crumb, cat, lead, body, faqs, sources, cta, related = nl
    fh, fld = nl_faq(faqs)
    build('nl/blog/goksites-blokkeren.html', f'nl/blog/{nl_slug}.html', 'nl', N + nl_slug, title, desc, head, crumb,
          'https://afterbetting.com/nl/', 'https://afterbetting.com/nl/blog',
          hero('/nl/', '/nl/blog', 'Home', cat, head, lead, f'Door Afterbetting &middot; {NL_DATE} &middot; {mins(body)} min lezen'),
          md(body) + fh + nl_src(sources),
          f'<div class="cta-block"><h3>{cta[0]}</h3><p>{cta[1]}</p><a href="https://app.afterbetting.com/onboarding" {ONCLICK}>Begin gratis</a></div>',
          cards(['Meer lezen'] + rel(related, 'nl')), NL_CRISIS, href, DATE, fld)
    title, desc, head, crumb, cat, lead, body, faqs, sources, cta, related = en
    fh, fld = en_faq(faqs)
    build('blog/block-gambling-sites-and-payments.html', f'blog/{en_slug}.html', 'en', B + en_slug, title, desc, head, crumb,
          'https://afterbetting.com', 'https://afterbetting.com/blog',
          hero('https://afterbetting.com', 'https://afterbetting.com/blog', 'Home', cat, head, lead, f'By Afterbetting &middot; {EN_DATE} &middot; {mins(body)} min read'),
          md(body) + fh + en_src(sources),
          f'<div class="cta"><h3>{cta[0]}</h3><p>{cta[1]}</p><a href="https://app.afterbetting.com/onboarding" {ONCLICK}>Start free</a></div>',
          cards(['Continue reading'] + rel(related, 'en')), EN_CRISIS, href, DATE, fld)

OOG = ('Rijksoverheid, waar vind ik hulp bij gokproblemen?', 'https://www.rijksoverheid.nl/vraag-en-antwoord/kansspelen/waar-vind-ik-hulp-bij-gokproblemen')
GAMCARE = ('GamCare, what support do we provide', 'https://www.gamcare.org.uk/about-us/what-support-do-we-provide')
GA_WIKI = ('Wikipedia, Gamblers Anonymous', 'https://en.wikipedia.org/wiki/Gamblers_Anonymous')

pair('waarom-kan-ik-niet-stoppen-met-gokken', 'why-cant-i-stop-gambling',
     ('Waarom kan ik niet stoppen met gokken? 8 eerlijke redenen',
      'Je wilt stoppen, je belooft het, en toch ga je terug. Acht redenen waarom stoppen zo moeilijk is, en wat wel werkt. Van iemand die 8 jaar gokte.',
      'Waarom kan ik niet stoppen met gokken?', 'Waarom kan ik niet stoppen', 'Stoppen',
      'Het ligt niet aan je karakter. Acht redenen waarom stoppen zo moeilijk is, en wat wel werkt.', NL_A, NL_A_FAQ, [OOG],
      ('Stoppen gaat dag voor dag', 'Afterbetting geeft je elke dag houvast: een dagenteller, gewoontes voor je risico-uren en Nu hulp bij drang. Gratis.'),
      [('stoppen-met-gokken', 'Stoppen'), ('verlies-terugwinnen-gokken', 'Stoppen'), ('hoe-vul-ik-mijn-tijd-zonder-gokken', 'Gewoonten'), ('terugval-na-gokverslaving', 'Terugval')]),
     ("Why can't I stop gambling? 8 honest reasons",
      'You want to stop, you promise yourself, and you still go back. Eight reasons why quitting is so hard, and what actually works. From a former gambler.',
      "Why can't I stop gambling?", "Why can't I stop", 'Quitting',
      "It isn't a flaw in your character. Eight reasons quitting is so hard, and what actually works.", EN_A, EN_A_FAQ,
      [('NHS, Help for problems with gambling', 'https://www.nhs.uk/live-well/addiction-support/gambling-addiction/'), GAMCARE],
      ('Stopping happens one day at a time', 'Afterbetting gives you something to hold on to every day: a day counter, habits for your risky hours and Help now for urges. Free.'),
      [('how-to-stop-gambling', 'Quitting'), ('chasing-losses-gambling', 'Quitting'), ('daily-habits-that-replace-gambling', 'Habits'), ('what-to-do-after-gambling-relapse', 'Relapse')]))

pair('stoppen-met-gokken-en-sparen', 'how-to-stop-gambling-and-save-money',
     ('Stoppen met gokken en sparen: zo bouw je weer iets op',
      'Stoppen met gokken en eindelijk geld overhouden. Hoe je van aflossen naar sparen gaat, wat je per week terugkrijgt en waarom je jezelf mag belonen.',
      'Stoppen met gokken en sparen: zo bouw je weer iets op', 'Stoppen en sparen', 'Geld',
      'Van verliezen, naar aflossen, naar opbouwen. Wat ik deed, en waarom je jezelf onderweg iets mag gunnen.', NL_B, NL_B_FAQ,
      [('BKR, veelgestelde vragen', 'https://www.mijnkredietregistratie.nl/nl/veelgestelde-vragen'), ('Geldfit', 'https://www.geldfit.nl/')],
      ('Zie wat je niet meer vergokt', 'Afterbetting rekent elke dag uit hoeveel je niet hebt vergokt en zet je schulden en vaste lasten op een rij. Gratis.'),
      [('hoeveel-heb-ik-vergokt', 'Geld'), ('van-gokschuld-naar-nul', 'Geld'), ('gokschuld-aflossen', 'Geld'), ('gokschuld-bkr-hypotheek', 'Geld')]),
     ('How to stop gambling and save money: start rebuilding',
      'Quit gambling and finally keep your money. How to go from paying off debt to saving, what you get back each week, and why you can reward yourself.',
      'How to stop gambling and save money', 'Stop gambling and save', 'Money',
      "From losing, to paying off, to building. What I did, and why you're allowed to treat yourself along the way.", EN_B, EN_B_FAQ,
      [('StepChange, free debt advice', 'https://www.stepchange.org/'),
       ('Experian, Dealing with defaults on your credit report', 'https://www.experian.co.uk/consumer/questions/credit-and-debt.html')],
      ("See what you're no longer losing", 'Afterbetting shows every day how much you have not gambled and puts your debts and fixed costs in one place. Free.'),
      [('how-much-have-i-lost-gambling', 'Money'), ('paid-off-gambling-debt', 'Money'), ('rebuild-finances-after-gambling', 'Money'), ('will-gambling-affect-my-mortgage', 'Money')]))

pair('gokverslaving-forum-en-lotgenoten', 'gambling-addiction-support-groups',
     ('Gokverslaving forum en lotgenoten: waar praat je erover?',
      'Praten met mensen die het ook meemaakten. Lotgenotengroepen, forums en chat bij gokverslaving: wat er is, wat het kost en waar je op let.',
      'Gokverslaving forum en lotgenoten: waar praat je erover?', 'Forum en lotgenoten', 'Hulp',
      'Lotgenotengroepen, forums en chat: wat er is, wat het kost en waar je op let.', NL_C, NL_C_FAQ,
      [('AGOG, gokverslaafd? AGOG helpt', 'https://www.agog.nl/gokverslaafd-agog-helpt-ook-jou-met-stoppen/'), OOG, GAMCARE, GA_WIKI],
      ('Voor de avonden tussen de bijeenkomsten', 'Afterbetting is er voor de uren tussen gesprekken in: een dagenteller, Nu hulp bij drang en een privé dagboek. Gratis.'),
      [('gokverslaving-hulp-zoeken', 'Hulp'), ('omgaan-met-gokverslaafde-naaste', 'Naasten'), ('gokken-aan-je-familie-vertellen', 'Naasten'), ('drang-om-te-gokken', 'Drang')]),
     ('Gambling addiction support groups, forums and meetings',
      'Talking to people who have been there. Support groups, forums and chatrooms for gambling addiction: what exists, what it costs and what to watch for.',
      'Gambling addiction support groups, forums and meetings', 'Support groups', 'Support',
      'Gamblers Anonymous, GamCare forums and chatrooms: what exists, what it costs and what to watch for.', EN_C, EN_C_FAQ,
      [('Gamblers Anonymous UK', 'https://gamblersanonymous.org.uk/'), GAMCARE, GA_WIKI],
      ('For the evenings between meetings', 'Afterbetting is for the hours in between: a day counter, Help now for urges and a private journal. Free.'),
      [('where-to-get-help-gambling-addiction', 'Support'), ('my-partner-has-a-gambling-problem', 'Family'), ('how-to-tell-family-about-gambling-problem', 'Family'), ('do-gambling-urges-go-away', 'Urges')]))
print('gebouwd')

LINKS = [
 ('nl/blog/stoppen-met-gokken.html', '/nl/blog/waarom-kan-ik-niet-stoppen-met-gokken', 'Waarom kan ik niet stoppen met gokken?', 'Lees ook'),
 ('nl/blog/drang-om-te-gokken.html', '/nl/blog/waarom-kan-ik-niet-stoppen-met-gokken', 'Waarom kan ik niet stoppen met gokken?', 'Lees ook'),
 ('nl/blog/verlies-terugwinnen-gokken.html', '/nl/blog/waarom-kan-ik-niet-stoppen-met-gokken', 'Waarom kan ik niet stoppen met gokken?', 'Lees ook'),
 ('blog/how-to-stop-gambling.html', B + 'why-cant-i-stop-gambling', "Why can't I stop gambling? 8 honest reasons", 'Read next'),
 ('blog/chasing-losses-gambling.html', B + 'why-cant-i-stop-gambling', "Why can't I stop gambling?", 'Read next'),
 ('blog/do-gambling-urges-go-away.html', B + 'why-cant-i-stop-gambling', "Why can't I stop gambling?", 'Read next'),
 ('nl/blog/van-gokschuld-naar-nul.html', '/nl/blog/stoppen-met-gokken-en-sparen', 'Stoppen met gokken en sparen: van aflossen naar opbouwen', 'Lees ook'),
 ('nl/blog/hoeveel-heb-ik-vergokt.html', '/nl/blog/stoppen-met-gokken-en-sparen', 'Stoppen met gokken en sparen', 'Lees ook'),
 ('nl/blog/gokschuld-aflossen.html', '/nl/blog/stoppen-met-gokken-en-sparen', 'Stoppen met gokken en sparen', 'Lees ook'),
 ('blog/paid-off-gambling-debt.html', B + 'how-to-stop-gambling-and-save-money', 'How to stop gambling and save money', 'Read next'),
 ('blog/how-much-have-i-lost-gambling.html', B + 'how-to-stop-gambling-and-save-money', 'How to stop gambling and save money', 'Read next'),
 ('blog/rebuild-finances-after-gambling.html', B + 'how-to-stop-gambling-and-save-money', 'How to stop gambling and save money', 'Read next'),
 ('nl/blog/gokverslaving-hulp-zoeken.html', '/nl/blog/gokverslaving-forum-en-lotgenoten', 'Gokverslaving forum en lotgenoten', 'Lees ook'),
 ('nl/blog/omgaan-met-gokverslaafde-naaste.html', '/nl/blog/gokverslaving-forum-en-lotgenoten', 'Lotgenoten bij gokverslaving, ook voor naasten', 'Lees ook'),
 ('blog/where-to-get-help-gambling-addiction.html', B + 'gambling-addiction-support-groups', 'Gambling addiction support groups, forums and meetings', 'Read next'),
 ('blog/my-partner-has-a-gambling-problem.html', B + 'gambling-addiction-support-groups', 'Support groups for gamblers and their families', 'Read next'),
]
for p, href, text, label in LINKS:
    s = open(p, encoding='utf-8').read()
    if href.split('/')[-1] + '"' in s: continue
    m = re.search(r'<div class="(cta-block|cta)">', s) or re.search(r'<aside class="author-box">', s)
    s = s[:m.start()] + f'<p><strong>{label}:</strong> <a href="{href}">{text}</a></p>\n' + s[m.start():]
    s = re.sub(r'"dateModified": ?"[^"]+"', f'"dateModified": "{DATE}"', s)
    open(p, 'w', encoding='utf-8').write(s)
    print('link toegevoegd:', p)
