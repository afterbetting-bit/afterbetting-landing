# 19 okt 2026: ronde 2 op de zoektermen van vandaag (Ubersuggest + Google-autocomplete).
# Clusters: naasten, stoppen en hulp, Cruks en GamStop, geld. Alleen title, description, H1, H2, FAQ en interne links.
import re, json, html as H
from opknap_en import md, inline

N = 'https://afterbetting.com/nl/blog/'; B = 'https://afterbetting.com/blog/'
DATE = '2026-10-19'

def plain(t):
    return H.unescape(re.sub('<[^>]+>', '', inline(t)))

def faq_block(s, items, lang):
    """Voegt vragen toe aan de zichtbare FAQ en aan het FAQPage-schema (maakt beide aan als ze ontbreken)."""
    head, body = s.split('<body', 1)
    m = re.search(r'<script type="application/ld\+json">(\{[^<]*"FAQPage"[^<]*)</script>', head)
    new = [{"@type": "Question", "name": plain(q), "acceptedAnswer": {"@type": "Answer", "text": plain(a)}} for q, a in items]
    if m:
        d = json.loads(m.group(1)); d['mainEntity'] = [e for e in d['mainEntity'] if e['name'] not in {n['name'] for n in new}] + new
        head = head.replace(m.group(0), '<script type="application/ld+json">' + json.dumps(d, ensure_ascii=False) + '</script>')
    else:
        d = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": new}
        bc = re.search(r'<script type="application/ld\+json">[^<]*"BreadcrumbList"[^<]*</script>\n?', head)
        tag = '<script type="application/ld+json">' + json.dumps(d, ensure_ascii=False) + '</script>\n'
        head = head.replace(bc.group(0), bc.group(0).rstrip('\n') + '\n' + tag, 1)
    vis = ''.join(f'<h3>{inline(q)}</h3>\n<p>{inline(a)}</p>\n' for q, a in items)
    title = 'Veelgestelde vragen' if lang == 'nl' else 'Frequently asked questions'
    hm = re.search(rf'<h2>({title}|Veelgestelde vragen|Frequently asked questions)</h2>\n', body)
    if hm:
        nxt = body.find('<h2', hm.end()); cands = [i for i in (nxt, body.find('<div class="cta', hm.end()), body.find('<aside class="author-box"', hm.end())) if i > 0]
        at = min(cands); body = body[:at] + vis + body[at:]
    else:
        block = f'<h2>{title}</h2>\n' + vis
        for marker in ('<h2>Bronnen</h2>', '<h2>Sources</h2>'):
            if marker in body: body = body.replace(marker, block + marker, 1); break
        else:
            art = body[:body.index('</article>')]
            at = max(art.rfind('<div class="cta-block">'), art.rfind('<div class="cta">'))
            if at < 0: at = art.rfind('<aside class="author-box"')
            body = body[:at] + block + body[at:]
    return head + '<body' + body

def edit(path, reps=(), before=None, markdown=None, faqs=None, lang='nl'):
    s = open(path, encoding='utf-8').read()
    for a, b in reps:
        assert s.count(a) >= 1, (path, a[:70]); s = s.replace(a, b)
    if before and 'data-r2' not in s:
        assert before in s, (path, before)
        s = s.replace(before, '<div data-r2></div>\n' + md(markdown) + before, 1)
    if faqs: s = faq_block(s, faqs, lang)
    s = re.sub(r'"dateModified": ?"[0-9-]+"', f'"dateModified": "{DATE}"', s)
    t = re.search(r'<title>([^<]*)', s).group(1); d = re.search(r'name="description" content="([^"]*)', s).group(1)
    assert len(t) <= 60 and len(d) <= 155 and '—' not in s, (path, len(t), len(d))
    open(path, 'w', encoding='utf-8').write(s); print('ok', path, len(t), len(d))

def meta(path, t_new=None, d_new=None, h1_new=None):
    s = open(path, encoding='utf-8').read(); r = []
    if t_new:
        t = re.search(r'<title>([^<]*)', s).group(1)
        r += [(f'<title>{t}', f'<title>{t_new}'), (f'"og:title" content="{t}"', f'"og:title" content="{t_new}"'),
              (f'"twitter:title" content="{t}"', f'"twitter:title" content="{t_new}"'), (f'"headline": "{t}"', f'"headline": "{t_new}"')]
    if d_new:
        d = re.search(r'name="description" content="([^"]*)', s).group(1)
        r += [(f'content="{d}"', f'content="{d_new}"')]
    if h1_new:
        h = re.search(r'(<h1[^>]*>)(.*?)(</h1>)', s, re.S)
        r += [(h.group(0), h.group(1) + h1_new + h.group(3))]
    return [x for x in r if x[0] in s]

# ---------------- 1. NAASTEN ----------------
p = 'nl/blog/omgaan-met-gokverslaafde-naaste.html'
edit(p, meta(p, 'Omgaan met een gokverslaafde: wat werkt echt',
             'Leven met een gokverslaafde partner, kind of vriend. Hoe een gokverslaafde zich gedraagt, wat helpt, wat het erger maakt en hoe je jezelf beschermt.')
     + [('<h2>Hoe herken je dat iemand een gokprobleem heeft</h2>', '<h2>Hoe gedraagt een gokverslaafde zich?</h2>')],
     before='<h2>Als het je broer, zus, moeder of vader is</h2>', markdown=f'''
## Per relatie: partner, kind of vriend

Wat je kunt doen, hangt af van wie het is. Een partner deelt vaak je huis en je geld. Een ouder voelt zich verantwoordelijk, ook voor een volwassen kind. Een vriend krijgt vaak de vraag om geld te lenen. Per relatie staat het uitgewerkt:

- [Mijn partner is gokverslaafd]({N}mijn-partner-is-gokverslaafd-wat-doe-ik): je relatie, je geld en jezelf.
- [Mijn kind is gokverslaafd]({N}mijn-kind-is-gokverslaafd): voor ouders van een zoon of dochter die gokt.
- [Mijn vriend of vriendin is gokverslaafd]({N}mijn-vriend-is-gokverslaafd): hoe ver je gaat als vriend.
''', faqs=[
 ('Hoe ga je om met een gokverslaafde?', 'Zeg eerlijk wat je ziet en wat het met je doet, zonder er een verhoor van te maken. Leen geen geld en los geen schulden voor de ander op. Stel grenzen die je kunt volhouden, en zoek ook steun voor jezelf.'),
 ('Kun je iemand dwingen te stoppen met gokken?', 'Nee. Je kunt wel stoppen met het opvangen van de gevolgen, hulp aanbieden en je eigen geld beschermen. De keuze om te stoppen ligt bij de ander.'),
 ('Waar kan ik als naaste terecht?', 'OpenOverGokken (0800-2400022) is er ook voor partners, ouders en vrienden. Gratis en anoniem, dag en nacht. Ook bij de verslavingszorg zijn vaak gesprekken of groepen voor naasten.'),
 ('Is gokverslaving te genezen?', 'Gokverslaving is te behandelen. Veel mensen stoppen en blijven gestopt, vaak met hulp en soms na een of meer terugvallen. Herstel kost tijd, ook voor de mensen eromheen.'),
])

p = 'nl/blog/mijn-partner-is-gokverslaafd-wat-doe-ik.html'
edit(p, meta(p, 'Mijn partner is gokverslaafd: wat doe ik nu?',
             'Je partner gokt en je weet niet meer wat te doen. Wat helpt in een relatie met een gokverslaafde, wat averechts werkt en hoe je jezelf niet kwijtraakt.')
     + [('<h2>Wat er bij hem omgaat</h2>', '<h2>Wat er in je gokverslaafde partner omgaat</h2>')],
     faqs=[
 ('Mijn vrouw of vriendin is gokverslaafd. Geldt dit ook voor mij?', 'Ja. Op deze pagina staat "hij", maar alles geldt ook als je vrouw of vriendin gokt. De signalen, de schaamte en wat helpt zijn hetzelfde.'),
 ('Moet ik bij mijn gokverslaafde partner weggaan?', 'Dat kan niemand voor je beslissen. Het helpt om te weten waar je grens ligt, bijvoorbeeld: je blijft zolang hij hulp zoekt en open is over geld. Kun je je veiligheid of je bestaan niet meer beschermen, dan mag je jezelf voorop zetten.'),
 ('Ben ik aansprakelijk voor de gokschulden van mijn partner?', 'Dat hangt af van hoe jullie getrouwd zijn of samenwonen, en op wiens naam de schuld staat. Bij een gemeenschap van goederen kunnen schuldeisers soms ook aankloppen voor wat jullie samen bezitten. Vraag het gratis na bij Het Juridisch Loket voordat je iets tekent of betaalt.'),
 ('Hoe weet ik of mijn partner stiekem gokt?', f'Vaak aan geld dat niet klopt, onverklaarde opnames of leningen, geheimzinnigheid rond de telefoon en stemmingen die samenvallen met wedstrijden of late avonden. Meer signalen in [gokverslaving: symptomen en kenmerken]({N}gokverslaving-symptomen-en-kenmerken).'),
])

p = 'nl/blog/mijn-kind-is-gokverslaafd.html'
edit(p, meta(p, 'Mijn zoon of dochter is gokverslaafd: wat doe je als ouder',
             'Hoe ga je om met een gokverslaafde zoon of dochter? Signalen, wat helpt, wat averechts werkt, wat je doet met schulden en hoe je jezelf beschermt.'),
     faqs=[
 ('Hoe ga ik om met mijn gokverslaafde zoon of dochter?', 'Houd contact en zeg eerlijk wat je ziet, zonder verhoor. Betaal geen schulden af en geef geen geld dat naar gokken kan gaan. Bied hulp aan, bijvoorbeeld een gesprek met OpenOverGokken (0800-2400022), en zoek ook steun voor jezelf.'),
 ('Moet ik de gokschulden van mijn kind betalen?', 'Voor de schulden van een volwassen kind ben je niet verantwoordelijk, tenzij je zelf iets hebt getekend, zoals een borgstelling. Schulden overnemen voelt als helpen, maar haalt vaak de druk weg om te stoppen. Gratis schuldhulp via de gemeente is een betere route.'),
 ('Kan ik mijn kind inschrijven in Cruks?', 'Inschrijven doet iemand normaal zelf. Wel kun je als familielid de Kansspelautoriteit vragen om iemand in te schrijven. De Kansspelautoriteit onderzoekt dat verzoek en beslist zelf. Het werkt het best als je kind zich zelf inschrijft.'),
 ('Mijn kind is minderjarig en gokt. Wat nu?', 'Gokken mag in Nederland pas vanaf 18 jaar. Gokt je kind toch, dan gaat dat vaak via het account van iemand anders of via illegale sites. Neem het serieus, ook als het om kleine bedragen gaat, en bel OpenOverGokken voor advies.'),
])

p = 'nl/blog/mijn-vriend-is-gokverslaafd.html'
edit(p, meta(p, 'Mijn vriend of vriendin is gokverslaafd: wat kun je doen',
             'Je vriend of vriendin gokt en je weet niet hoe ver je moet gaan. Waarom vrienden worden afgestroopt, wat helpt en wanneer je jezelf beschermt.',
             'Mijn vriend of vriendin is gokverslaafd'),
     faqs=[
 ('Moet ik mijn gokverslaafde vriend geld lenen?', 'Liever niet. Ook als het voor de huur is, kan het geld naar gokken gaan of andere gaten vullen. Help op een andere manier: samen een rekening betalen, meegaan naar schuldhulp, of er gewoon blijven zijn.'),
 ('Hoe begin ik het gesprek met een vriend die gokt?', 'Kies een rustig moment, niet vlak na een verlies. Zeg wat je ziet en dat je je zorgen maakt. Verwacht niet dat hij meteen alles toegeeft. Het eerste gesprek is een begin.'),
 ('Moet ik zijn familie of partner inlichten?', 'Als er gevaar is, of als hij anderen financieel meesleept, mag je dat overwegen. Zeg het hem dan eerst zelf. Twijfel je, bel dan OpenOverGokken (0800-2400022) voor advies.'),
 ('Wat als mijn vriendin gokverslaafd is?', 'Alles op deze pagina geldt ook voor een vriendin. Het gaat om wat je ziet, wat je wel en niet doet, en hoe je jezelf beschermt.'),
])

p = 'nl/blog/gokverslaving-symptomen-en-kenmerken.html'
edit(p, [('<h2>Wat als het over iemand anders gaat?</h2>', '<h2>Hoe gedraagt een gokverslaafde zich? Signalen bij een ander</h2>')],
     faqs=[
 ('Wanneer ben je gokverslaafd?', f'Als gokken je leven gaat bepalen en je niet kunt stoppen, ook al wil je dat. Denk aan meer inzetten dan je kunt missen, verlies willen terugwinnen, liegen over gokken en pogingen om te stoppen die niet lukken. De [gokverslaving test]({N}gokverslaving-test) helpt je eerlijk te kijken.'),
 ('Is gokverslaving erfelijk?', 'Erfelijkheid kan meespelen, net als bij andere verslavingen. Het is geen vaststaand lot. Stress, hoe makkelijk je kunt gokken en wat je ermee probeert weg te drukken tellen ook mee.'),
 ('Wat zijn de oorzaken van gokverslaving?', f'Meestal een combinatie: hoe je brein reageert op winst en bijna-winst, gokken dat altijd binnen handbereik is op je telefoon, stress of leegte die gokken even wegneemt, en het najagen van verlies. Meer in [wat doet gokken met je hersenen]({N}wat-doet-gokken-met-je-hersenen).'),
 ('Is gokverslaving te genezen?', 'Het is te behandelen. Veel mensen stoppen en blijven gestopt, met of zonder behandeling. De drang kan nog lang opduiken, maar wordt minder vaak en minder sterk.'),
])

# ---------------- 2. STOPPEN EN HULP ----------------
p = 'nl/blog/stoppen-met-gokken.html'
edit(p, before='<h2>Kun je zelf stoppen met gokken, zonder hulp?</h2>', markdown=f'''
## Cold turkey stoppen met gokken: kan dat?

Cold turkey betekent in één keer stoppen, zonder af te bouwen. Bij gokken werkt dat beter dan minderen. Elke kleine inzet houdt de gedachte levend dat het deze keer anders gaat.

In één keer stoppen is wel zwaar. De eerste weken komen drang, onrust en slecht slapen vaak samen. Bij mij waren het de drang en de leegte, en 's nachts wakker worden met één gedachte. Na een paar weken werd het beter. Wat je in die eerste dagen kunt verwachten, staat in [eerste week stoppen met gokken]({N}eerste-week-stoppen-met-gokken) en [afkickverschijnselen bij stoppen met gokken]({N}afkickverschijnselen-gokken).
''', faqs=[
 ('Wat is de beste manier om te stoppen met gokken?', 'Er is niet één manier. Wat bijna altijd helpt: in één keer stoppen, de toegang dichtzetten met Cruks en blokkades, je geld tijdelijk uit eigen handen geven, één persoon inlichten en de uren vullen waarin je vroeger gokte.'),
 ('Is er een app om te stoppen met gokken?', f'Er zijn apps die goksites blokkeren, zoals Gamban, en apps die je helpen om een nieuw ritme op te bouwen. Afterbetting is zo\'n app: een dagenteller, gewoontes, een dagboek, een overzicht van je geld en Nu hulp voor als de drang komt. De basis is gratis. Blokkeren staat uitgelegd in [goksites blokkeren]({N}goksites-blokkeren).'),
 ('Hoe lang duurt het voordat de drang minder wordt?', f'Voor veel mensen zijn de eerste weken het zwaarst. Daarna komt de drang minder vaak en minder heftig, al kan hij lang opduiken bij een trigger. Meer in [hoe lang duurt herstel van gokverslaving]({N}hoe-lang-duurt-herstel-gokverslaving).'),
 ('Waar praat ik met lotgenoten?', 'Bij AGOG zijn zelfhulpgroepen voor mensen met een gokprobleem. Er zijn ook online forums. Lees die met beleid: niet elk verhaal helpt je verder.'),
])

edit('nl/blog/gokverslaving-hulp-zoeken.html', faqs=[
 ('Is hulp bij gokverslaving gratis?', 'Een gesprek met OpenOverGokken is gratis. Behandeling bij de verslavingszorg valt onder de basisverzekering, maar meestal gaat je eigen risico eraf. Schuldhulp via de gemeente is gratis.'),
 ('Heb ik een verwijzing nodig voor de verslavingszorg?', 'Voor behandeling meestal wel, van je huisarts. Sommige instellingen bieden ook online zelfhulp of een eerste gesprek zonder verwijzing. Vraag het na bij de instelling bij jou in de buurt.'),
 ('Wat is het verschil tussen een kliniek en ambulante behandeling?', 'Bij ambulante behandeling woon je thuis en ga je naar gesprekken of een groep, soms online. In een kliniek verblijf je een periode. De meeste mensen met een gokverslaving worden ambulant behandeld.'),
])

# ---------------- 3. CRUKS EN GAMSTOP ----------------
edit('nl/blog/cruks-opzeggen.html', faqs=[
 ('Hoe zeg ik Cruks op?', 'Na de eerste 6 maanden kun je opzeggen via Mijn Cruks op cruksregister.nl, met je DigiD, of met een papieren formulier. Daarna geldt een bedenktijd van 8 dagen. Pas daarna is je gokstop opgeheven.'),
 ('Kan ik Cruks opzeggen na 6 maanden?', 'Ja. Na 6 maanden mag je opzeggen, ook als je voor een langere periode had gekozen. Daarna volgt de bedenktijd van 8 dagen.'),
 ('Hoe weet ik of ik in Cruks sta?', 'Log in bij Mijn Cruks op cruksregister.nl met je DigiD. Daar zie je of je ingeschreven staat en tot wanneer.'),
 ('Wat gebeurt er als mijn gokstop afloopt?', 'Dan stopt hij vanzelf. Je krijgt geen bericht en Cruks verwijdert je gegevens. Wil je beschermd blijven, verleng dan op tijd. Verlengen kan altijd.'),
 ('Kan iemand anders mij inschrijven in Cruks?', 'Familie of hulpverleners kunnen de Kansspelautoriteit vragen om iemand in te schrijven. De Kansspelautoriteit onderzoekt zo\'n verzoek en beslist zelf.'),
])

edit('nl/blog/cruks-omzeilen-wat-nu.html', faqs=[
 ('Kun je Cruks omzeilen?', 'Bij aanbieders met een Nederlandse vergunning niet: zij moeten iedereen controleren. Bij illegale en buitenlandse sites lukt het wel. Daar heb je geen bescherming, geen zorgplicht en geen zekerheid dat winst wordt uitbetaald.'),
 ('Ik sta in Cruks en gok toch. Wat nu?', f'Dan ben je niet de enige, en het betekent niet dat stoppen mislukt is. Het laat zien dat Cruks alleen niet genoeg is. Zet blokkades op je telefoon en bij je bank, zie [goksites blokkeren]({N}goksites-blokkeren), en vertel het één persoon.'),
 ('Mag een casino mij laten spelen als ik in Cruks sta?', f'Een aanbieder met een Nederlandse vergunning mag dat niet. Gebeurt het toch, bewaar dan je gegevens, want dat kan een schending van de zorgplicht zijn. Meer in [geld terugvragen van een online casino]({N}geld-terugvragen-online-casino).'),
])

edit('blog/cancel-gamstop-early.html', lang='en', faqs=[
 ('Can you cancel GamStop?', 'Not during your minimum period. Nobody can end it early. After that period, the exclusion stays in place until you ask GamStop to remove it, followed by a 24-hour cooling-off period.'),
 ('How long does GamStop last?', 'You choose six months, one year or five years. When that period is over, the exclusion does not end by itself. If you do nothing, it carries on for another seven years.'),
 ('What happens when GamStop ends?', 'Your minimum period ending does not lift the block. You have to log in and request removal. Then there is a 24-hour cooling-off period, and you can still cancel the removal in that time.'),
 ('How does GamStop work?', f'You sign up once, and online gambling sites and apps licensed in Great Britain have to block you for the period you chose. Sites without a British licence do not check GamStop. More in [does self-exclusion work?]({B}does-self-exclusion-work-gambling)'),
])

# Verborgen FAQ-schema zichtbaar maken (Google wil dat de vragen op de pagina staan), in eigen woorden.
def reset_faq(path):
    s = open(path, encoding='utf-8').read()
    s = re.sub(r'<script type="application/ld\+json">\{[^<]*"FAQPage"[^<]*</script>\n?', '', s)
    open(path, 'w', encoding='utf-8').write(s)

p = 'blog/does-self-exclusion-work-gambling.html'; reset_faq(p)
edit(p, lang='en', faqs=[
 ('Does self-exclusion stop a gambling addiction?', 'Not on its own. It closes the licensed sites and buys you time between the thought and the bet. It works best together with blocking software, someone who knows, and a plan for the hours you used to gamble.'),
 ('What is GamStop and does it work?', 'GamStop is the free UK self-exclusion scheme for online gambling. It blocks sites and apps licensed in Great Britain. It does not cover sites without a British licence, which is where most people who get around it end up.'),
 ('Can you cancel self-exclusion early?', f'With GamStop and the Dutch Cruks register, no. Both have a minimum period that nobody can shorten. Read [can you cancel GamStop early?]({B}cancel-gamstop-early) before you try.'),
])

p = 'blog/how-to-stop-gambling-urges-weekends.html'; reset_faq(p)
edit(p, lang='en', faqs=[
 ('Why are gambling urges stronger at night?', 'You are tired, the day is done and there is nothing planned. If evenings were when you used to bet, your head links those quiet hours with gambling. That is why planning the evening helps more than willpower.'),
 ('How long does a gambling urge last?', 'An urge usually builds, peaks and then fades if you do not act on it. Delaying by fifteen minutes is often enough to get past the peak.'),
 ('What helps with gambling urges at the weekend?', 'Plan the risky hours before they arrive, get out of the house or the room where you used to bet, and have one thing ready to do when the urge hits: a walk, a call, a shower.'),
])

p = 'blog/sports-betting-addiction-quit.html'; reset_faq(p)
edit(p, lang='en', reps=[('<h2>How to quit sports betting specifically</h2>', '<h2>How to stop gambling on sports</h2>')], faqs=[
 ('Is sports betting addiction different from other gambling?', 'In a few ways. Knowing a lot about the sport makes it feel like skill, betting is part of how friends talk about matches, and the apps are always on your phone. That makes it easy to tell yourself it is not a real problem.'),
 ('Can you still watch sport after you stop betting?', 'Yes. At first a match can feel flat without money on it. That passes. Watching with other people and without a betting app on your phone makes it easier.'),
 ('How do I get through live matches without betting?', 'Delete the betting apps and block the sites before the match. Turn off score apps that show odds. Watch with someone, and decide in advance what you do if the urge comes.'),
])

p = 'blog/what-to-do-instead-of-gambling.html'; reset_faq(p)
edit(p, lang='en', faqs=[
 ('What can I do instead of gambling?', 'Look at what gambling gave you and replace that. Exercise for the rush, something that keeps your head busy for the boredom, and people for the company. Filling the evenings and weekends matters most.'),
 ('How do I deal with boredom without gambling?', 'Expect it. Ordinary evenings can feel flat at first. A fixed routine helps more than waiting for motivation: the same things at the same times, especially in the hours you used to bet.'),
 ('How long does the empty feeling last after quitting?', 'For many people the first weeks are the hardest. It usually eases as your days fill up with other things. If the emptiness turns into lasting low mood, talk to your GP.'),
])

# ---------------- 4. GELD ----------------
p = 'nl/blog/geld-terugvragen-online-casino.html'
edit(p, meta(p, 'Geld terugvragen van een online casino: wat kan en wat niet',
             'Gokverlies terugvorderen van een online casino in Nederland. Wanneer het kan (illegale aanbieder, zorgplicht), wanneer niet, en hoe je het aanpakt.'),
     faqs=[
 ('Kan ik mijn gokverlies terugvorderen?', 'Soms. Bij aanbieders zonder Nederlandse vergunning die zich voor 1 oktober 2021 op Nederland richtten, hebben spelers in rechtszaken geld teruggekregen. Bij legale aanbieders kan het meestal alleen als die hun zorgplicht hebben geschonden.'),
 ('Hoeveel krijg je terug?', 'Als het lukt, gaat het om je netto verlies: wat je stortte min wat je opnam. Niet om je totale inzet.'),
 ('Hoe lang kun je geld terugvragen?', 'In beginsel verjaart zo\'n vordering na vijf jaar. Wanneer die termijn begint, beoordelen rechters niet overal hetzelfde. Laat dat nakijken door Het Juridisch Loket of een advocaat met ervaring in gokzaken.'),
])

p = 'nl/blog/gokschuld-aflossen.html'
edit(p, faqs=[
 ('Wat moet ik doen met gokschulden?', f'Eerst stoppen met gokken en de toegang dichtzetten. Daarna alles op een rij en contact met schuldhulp van je gemeente, dat is gratis. Leen niet om te gokken of om andere schulden te dekken. Zie ook [stoppen met gokken met schulden]({N}hoe-stop-ik-met-gokken-met-schulden).'),
 ('Hoe lang duurt het om een gokschuld af te lossen?', f'Dat hangt af van het bedrag en wat je per maand kunt missen. Bij mij ging het om ruim 40.000 euro en duurde het bijna twee jaar, met een vast bedrag om van te leven en de rest naar de schuld. Het verhaal staat in [van 40k gokschuld naar nul]({N}van-gokschuld-naar-nul).'),
 ('Kunnen gokschulden worden kwijtgescholden?', 'Via de wettelijke schuldsanering (Wsnp) kan dat soms, maar bij gokschulden wordt goed gekeken of je te goeder trouw was. Vaak moet je eerst laten zien dat je gestopt bent. Schuldhulp van je gemeente weet hoe dat bij jou zit.'),
])

p = 'blog/rebuild-finances-after-gambling.html'
edit(p, lang='en', faqs=[
 ('How do I get out of gambling debt?', 'Stop the leak first: self-exclude, block gambling on your phone and bank card, and let someone you trust help with your money for a while. Then list every debt, cover the essentials and get free debt advice. In the UK, StepChange and National Debtline are free. In the US, look for a nonprofit credit counselling agency.'),
 ('Should I take a loan to consolidate gambling debt?', 'Be careful. A consolidation loan can lower your interest, but it also clears your cards and overdraft again. While the urge to gamble is still strong, that can make things worse. Talk to a free debt adviser first.'),
])
print('klaar')
