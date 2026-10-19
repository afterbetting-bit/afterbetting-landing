# 19 okt 2026: elf oude pagina's (GSC: gecrawld, niet geindexeerd) inhoudelijk verbeterd.
# Zoekterm per pagina in title/description/H1/H2, nieuw blok, FAQ + FAQPage, "Niet X. Niet Y."-ritme herschreven,
# ervaringsclaims vervangen door wat de founder bevestigde, CTA-teksten zonder jargon.
import re, json, html as H
from opknap_en import md, inline
exec(open('seo_r2_okt19.py', encoding='utf-8').read().split('# ---------------- 1. NAASTEN')[0].split("DATE = '2026-10-19'")[1])  # plain, faq_block, edit, meta
N = 'https://afterbetting.com/nl/blog/'; B = 'https://afterbetting.com/blog/'; DATE = '2026-10-19'

def paras(path, items):
    """Vervangt hele alinea's (of een founder-kader) op basis van het begin van de tekst. new: markdown of ('html', ...)."""
    s = open(path, encoding='utf-8').read()
    for prefix, new in items:
        hits = []
        for m in re.finditer(r'<div class="callout"><p>.*?</p></div>|<p>.*?</p>', s, re.S):
            txt = H.unescape(re.sub('<[^>]+>', '', m.group(0))).strip()
            txt = re.sub(r'^From the founder:\s*', '', txt)
            if txt.startswith(prefix): hits.append(m)
        assert len(hits) == 1, (path, prefix[:50], len(hits))
        m = hits[0]
        rep = new[1] if isinstance(new, tuple) else md(new).strip()
        s = s[:m.start()] + rep + s[m.end():]
    open(path, 'w', encoding='utf-8').write(s)

def founder(text):
    return ('html', f'<div class="callout"><p><strong>From the founder:</strong> {inline(text)}</p></div>')

# ======================= NL =======================
p = 'nl/blog/salaris-vergokt-wat-nu.html'
paras(p, [
 ('Niet eerst je app openen', 'Open nog niet je bank-app om te kijken wat er over is. Ga ook nog niet rekenen of je partner bellen. Dat komt zo.'),
 ('Niet van je creditcard', 'Dus ook niet van je creditcard, via een lening of minilening, of van vrienden en familie. Probeer niet snel geld bij elkaar te krijgen om het einde van de maand recht te trekken.'),
 ('Geen brief naar je werkgever', 'Neem vanavond geen grote besluiten. Je zegt je baan of je huur niet op, je verkoopt je auto niet en je zet je relatie niet op het spel.'),
 ('Niet morgen. Niet als je nuchter bent. Nu.', 'Doe het nu, niet morgen.'),
 ('Geen excuses. Geen', 'Laat excuses en beloftes weg. Vertel wat er is gebeurd.'),
 ('Afterbetting helpt je dag voor dag uit het patroon', 'Een dagenteller, een overzicht van je geld en Nu hulp voor als de drang komt. Gratis te beginnen.'),
])
edit(p, meta(p, 'Salaris vergokt, wat nu? Zo kom je de eerste 24 uur door',
             'Je salaris of al je geld vergokt? Wat je nu niet doet, wat je de komende uren wel doet en hoe je huur en rekeningen regelt.',
             'Net je salaris vergokt: wat nu?'),
     before='<h2>Wat je tegen anderen zegt</h2>', markdown=f'''
## Al je geld vergokt, ook je spaargeld?

Soms gaat het om meer dan één salaris. Spaargeld, een lening, geld dat voor iets anders bedoeld was. De stappen blijven hetzelfde, alleen is het gat groter. Dan is hulp van buiten nog belangrijker.

Ga in dat geval meteen naar schuldhulp van je gemeente of bel Geldfit (0800-8115). Zij kijken mee wat eerst moet en kunnen namens jou met schuldeisers praten. Hoe je daarna stap voor stap aflost, staat in [gokschuld aflossen]({N}gokschuld-aflossen). Wil je weten hoeveel het in totaal is geweest? Met de [rekenhulp hoeveel heb ik vergokt]({N}hoeveel-heb-ik-vergokt) reken je het eerlijk uit.
''', faqs=[
 ('Wat moet ik doen als ik mijn salaris heb vergokt?', 'Gok niet om het terug te winnen en leen geen geld. Schrijf je vandaag in bij Cruks, verwijder je gok-apps en zet lage limieten in je bank-app. Zet daarna op een rij wat deze maand echt betaald moet worden, en bel op tijd met je verhuurder of schuldeisers.'),
 ('Kan ik mijn vergokte geld terugkrijgen?', f'Bij een aanbieder met een Nederlandse vergunning meestal niet, tenzij die zijn zorgplicht heeft geschonden. Bij illegale aanbieders van voor 1 oktober 2021 soms wel. Meer in [geld terugvragen van een online casino]({N}geld-terugvragen-online-casino).'),
 ('Waar krijg ik gratis hulp bij geldproblemen door gokken?', 'Bij schuldhulp van je gemeente en bij Geldfit (0800-8115). Voor het gokken zelf kun je gratis en anoniem bellen met OpenOverGokken: 0800-2400022.'),
])

p = 'nl/blog/gokken-aan-je-familie-vertellen.html'
paras(p, [
 ('Uit eigen ervaring:', 'Bij mij kwam het nooit uit. Niemand betrapte me, ik heb zelf open kaart gespeeld. Dat was eerst eng en beschamend. Maar zo bepaalde ik zelf hoe het gesprek begon, en daarna konden we er samen aan werken. Als iemand het zelf ontdekt, doet het vaak meer pijn dat je het niet kon delen dan wat er gebeurd is.'),
 ('Wat je niet gaat zeggen.', 'Wat je niet gaat zeggen. Laat vergoelijkingen weg, zoals "het kwam door werk", "het is niet zo erg" of "ik had het bijna onder controle". Je hoeft het niet te verpakken.'),
 ('Niet de meest dramatische persoon', 'Kies liever niet iemand die snel in paniek raakt, die het meteen doorvertelt of die zelf te kwetsbaar is om dit te dragen.'),
 ('Niet voor jou alleen.', 'Dat nummer is er ook voor hen. Familieleden van mensen met een gokprobleem kunnen ook bellen met 0800-2400022, gratis en anoniem, dag en nacht.'),
 ('Begin gratis op Afterbetting', 'Een dagenteller, een dagboek en Nu hulp voor de momenten dat het zwaar wordt. Gratis te beginnen.'),
])
edit(p, meta(p, None, 'Hoe vertel je je familie of partner dat je gokverslaafd bent? Hoe je begint, wat je zegt, wat je vraagt en wat je doet met hun reactie.',
             'Gokken aan je familie vertellen: zo begin je dat gesprek'),
     before='<h2>Wat je waarschijnlijk niet krijgt</h2>', markdown=f'''
## Hoe het bij mijn familie ging

Iedereen reageerde anders. Mijn moeder had er het meest moeite mee en vond weinig hulp voor zichzelf. Mijn stiefvader vond het in de periode erna moeilijk om te geloven wat ik zei. Mijn oom was een rots in de branding: hij oordeelde niet en was er gewoon.

Reken er dus niet op dat iedereen hetzelfde reageert. En wijs je familie op wat er voor hen is. Meer daarover in [omgaan met een gokverslaafde naaste]({N}omgaan-met-gokverslaafde-naaste).
''', faqs=[
 ('Hoe vertel ik dat ik gokverslaafd ben?', 'Kort en direct. Bijvoorbeeld: "Ik moet je iets vertellen waar ik me voor schaam. Ik heb een gokprobleem en ik wil hulp." Vertel het eerst aan één persoon, noem een eerlijk bedrag en zeg wat je al hebt gedaan, zoals inschrijven bij Cruks.'),
 ('Aan wie vertel ik het eerst?', 'Aan één persoon die je vertrouwt en die luistert voordat hij oordeelt. Vaak is dat je partner, zeker als jullie geld delen. Daarna kun je het stap voor stap aan anderen vertellen.'),
 ('Moet ik vertellen hoeveel ik heb vergokt?', f'Ja. Een tweede verrassing een paar weken later doet vaak meer pijn dan de eerste. Wil je het bedrag eerst zelf op een rij hebben, gebruik dan de [rekenhulp]({N}hoeveel-heb-ik-vergokt).'),
 ('Waar kan mijn familie terecht?', 'Bij OpenOverGokken (0800-2400022), gratis en anoniem, dag en nacht. Dat nummer is ook voor naasten.'),
])

p = 'nl/blog/partner-heeft-mijn-gokken-ontdekt.html'
paras(p, [
 ('Niet "het is niet zo erg', 'Zeg dus niet dat het meevalt, dat het maar één keer was of dat je het bijna onder controle had.'),
 ('Niet "ik stop nu"', 'Zeg vannacht niet dat je nu stopt, dat je in therapie gaat of dat het nooit meer gebeurt.'),
 ('Geen "ik deed het omdat', 'Leg het niet uit met werkstress, met hoe het ooit als hobby begon of met dat iedereen weleens wedt.'),
 ('Als je partner nu zegt weg te willen', 'Als je partner nu zegt weg te willen, betekent dat niet dat het definitief is. Het betekent dat er ruimte nodig is. Geef die ruimte, zonder te smeken, druk te zetten of beloftes te stapelen.'),
 ('Wat je kunt doen is consistent zijn', 'Wat je kunt doen is consistent zijn, elke dag. Geen goede week gevolgd door een mindere maand, maar dag na dag laten zien dat je verandert.'),
 ('Een verslaving overleven is publiek werk', 'Herstel doe je niet in het geheim.'),
 ('Afterbetting helpt je dag voor dag het verschil', 'Een dagenteller, een overzicht van je geld en Nu hulp. In Plus zit een steunkring: je partner krijgt elke week een korte update van wat jij wilt delen. Gratis te beginnen.'),
])
edit(p, meta(p, 'Partner heeft mijn gokken ontdekt: wat nu?',
             'Je partner heeft je gokken ontdekt. Wat je vanavond zegt, wat je de eerste 48 uur doet en hoe je het vertrouwen in je relatie herstelt.',
             'Mijn partner heeft ontdekt dat ik gok: wat nu?'),
     before='<h2>Wat als ze je verlaat</h2>', markdown=f'''
## Hoe herstel je vertrouwen na gokken?

Vertrouwen komt niet terug met één goed gesprek. Het komt terug met kleine dingen die kloppen, keer op keer. Doen wat je zegt. Vertellen voordat je partner ernaar vraagt. Je geld laten zien zonder dat het een ruzie wordt.

Ik ken dit van de andere kant. Mijn stiefvader vond het in de periode nadat ik gestopt was moeilijk om te geloven wat ik zei. Dat begreep ik. Na jaren van leugens komt vertrouwen niet terug met één gesprek.

Waarom liegen zo diep in een gokprobleem zit, staat in [waarom liegen gokkers]({N}waarom-liegen-gokkers).
''', faqs=[
 ('Mijn partner heeft mijn gokken ontdekt. Wat zeg ik?', 'Kort en eerlijk: dat het klopt, dat het langer speelt dan je zei en dat je alle vragen eerlijk beantwoordt. Bagatelliseer het niet en doe vannacht geen grote beloftes.'),
 ('Hoe herstel ik het vertrouwen van mijn partner?', 'Met gedrag dat klopt, keer op keer. Wees open over geld, vertel het als je drang voelt en doe wat je zegt. Dat kost maanden, soms langer.'),
 ('Moet mijn partner meekijken naar mijn geld?', 'Voor een tijd kan dat helpen, als jullie dat allebei willen. Het is geen straf maar structuur. Liegen gaat moeilijker als iemand meekijkt.'),
 ('Wat als mijn partner bij me weggaat?', 'Dat kan gebeuren. Geef ruimte, zonder te smeken of druk te zetten. Stop voor jezelf, zodat je herstel niet afhangt van hoe het met de relatie gaat.'),
])

p = 'nl/blog/gokken-depressie-en-angst.html'
paras(p, [
 ('Mensen die gokken kampen veel vaker', 'Een gokprobleem en depressie of angst gaan vaak samen. Dat is geen toeval. Het werkt twee kanten op.'),
 ('De cyclus herhaalt.', 'De cyclus herhaalt zich. Het zwaardere gevoel vraagt om een grotere onderbreking, dus de volgende keer zet je meer in. De afstand tussen de piek en de val wordt groter, en de somberheid zakt over de maanden dieper weg.'),
 ('Niet sporten om af te vallen.', 'Het gaat er niet om dat je afvalt of een snelle tijd loopt. Bewegen helpt gewoon. Mij hielp sporten in de eerste weken na het stoppen, samen met regelmaat en lezen over zelfontwikkeling.'),
 ('Afterbetting biedt structuur', 'Afterbetting geeft je dagen structuur, met een dagenteller, gewoontes en een dagboek. Voor de mentale kant ga je naar je huisarts. Dat is geen falen, dat is verstandig.'),
])
edit(p, meta(p, 'Gokken, depressie en angst: de cyclus die niemand uitlegt',
             'Gokverslaving en depressie of angst gaan vaak samen. Hoe ze elkaar versterken, wat er gebeurt als je stopt en waar je hulp vindt.',
             'Gokken, depressie en angst: de cyclus die niemand uitlegt'),
     faqs=[
 ('Kan gokken een depressie veroorzaken?', 'Gokken kan somberheid en angst flink verergeren, door geldzorgen, slecht slapen, schaamte en isolement. Het kan ook andersom: wie al somber of angstig is, gebruikt gokken soms om dat even niet te voelen. Een huisarts kan helpen uitzoeken wat bij jou speelt.'),
 ('Gaat de somberheid weg als ik stop met gokken?', 'Bij sommige mensen wel, bij anderen blijft er iets. De eerste weken kunnen juist zwaarder voelen. Blijft de somberheid, ga dan naar je huisarts.'),
 ('Waar kan ik terecht als ik somber ben door gokken?', 'Bij je huisarts, die je zo nodig doorverwijst. Voor het gokken bij OpenOverGokken (0800-2400022). Denk je aan zelfmoord, bel dan 113 of 0800-0113. Gratis en anoniem, dag en nacht.'),
])

p = 'nl/blog/gokverslaving-en-identiteit.html'
paras(p, [
 ('Niet alleen craving.', 'Het is meer dan drang of het missen van de kick.'),
 ('Niet juist.', 'Dat klopt niet.'),
 ('Sport. Wandel. Beweeg.', 'Sport, wandel, beweeg. Het maakt niet uit wat. Je lichaam is van jou en het reageert op aandacht. Sport een paar keer per week en kijk na een maand hoe het voelt. Het gaat niet om dunner worden, maar om merken dat je iets kunt volhouden.'),
 ('Streak, journaal, gewoonten tracker', 'Een dagenteller, gewoontes, een dagboek en de brief aan jezelf op dag 365. Gratis te beginnen.'),
])
edit(p, meta(p, 'Leegte na stoppen met gokken: wie ben je zonder de inzet?',
             'Leeg of verloren nu je gestopt bent met gokken? Waarom gokken deel wordt van wie je bent, en vier ankers om jezelf opnieuw op te bouwen.',
             'Gokverslaving en identiteit: wie ben je zonder de inzet?'),
     before='<h2>De vraag opnieuw, langzamer</h2>', markdown=f'''
## Leegte na het stoppen: hoe lang duurt het?

Daar is geen vaste termijn voor. Bij mij zat de leegte vooral in de eerste weken, samen met de drang. Ze werd kleiner naarmate ik de avonden en weekenden vulde met vaste dingen: sporten, lezen, een ritme.

Zie de leegte niet als bewijs dat je leven zonder gokken saai is. Het is een tussenfase. Wat je in die uren doet, bepaalt hoe snel ze gevuld raken. Ideeën staan in [hoe vul je je tijd zonder gokken]({N}hoe-vul-ik-mijn-tijd-zonder-gokken) en [afkickverschijnselen bij stoppen met gokken]({N}afkickverschijnselen-gokken).
''', faqs=[
 ('Waarom voel ik me leeg nu ik gestopt ben met gokken?', 'Gokken gaf je spanning, iets om naar uit te kijken en soms een groep om bij te horen. Als dat wegvalt, blijft er eerst een gat over. Dat is een tussenfase, geen eindstation.'),
 ('Hoe vind ik mezelf terug na een gokverslaving?', 'Begin klein: pak iets op wat je vroeger leuk vond, bouw één dagelijkse gewoonte, zoek mensen op buiten het gokken en vertel minstens één persoon wat je doormaakt.'),
 ('Gaat de leegte na het stoppen weer weg?', 'Voor veel mensen wordt hij kleiner naarmate de dagen weer gevuld raken. Blijft de somberheid lang hangen, praat er dan over met je huisarts.'),
])

p = 'nl/blog/sportgokken-verslaving.html'
paras(p, [
 ('Eén keer een grote combi raken', 'Eén grote winst kan iemand jarenlang bezighouden. Ik won ooit 68.000 euro. Dat werd het begin van jaren waarin ik dat gevoel najoeg, en later vooral probeerde terug te winnen wat ik kwijt was.'),
 ('Verlies je favoriete club?', 'Verlies van je club, boosheid, stress op je werk: dat zijn precies de momenten waarop mensen een verkeerde gok plaatsen. Alcohol hoort in dat rijtje. Bij mij maakte drinken de triggers erger.'),
 ('Spoiler: bookmakers', 'Bookmakers verdienen geld omdat ze het op grote schaal beter weten dan jij. Anders bestonden ze niet meer.'),
 ('Het verschil zit in de marketing.', 'Het verschil zit in de marketing, niet in wat het met je doet.'),
 ('Op Afterbetting hou je je streak bij', 'Een dagenteller, een dagboek en Nu hulp voor wedstrijdavonden. Gratis te beginnen.'),
])
edit(p, meta(p, 'Sportgokken verslaving: stoppen met sportweddenschappen',
             'Verslaafd aan sportgokken? Waarom het anders voelt dan casino, de signalen, de valkuilen van live wedden en combi\'s, en hoe je stopt.',
             'Sportgokken verslaving: hoe je er eerlijk naar kijkt')
     + [('<h2>Stoppen met sportgokken. Specifieke aanpak.</h2>', '<h2>Stoppen met sportgokken: zo pak je het aan</h2>')],
     faqs=[
 ('Wanneer is sportgokken een verslaving?', f'Als je meer inzet dan je wilde, verlies probeert terug te winnen, wedstrijden alleen nog kijkt voor je inzet, liegt over wat je inzet of niet kunt stoppen terwijl je dat wel wilt. Doe de [gokverslaving test]({N}gokverslaving-test) voor een eerlijk beeld.'),
 ('Hoe stop ik met sportweddenschappen?', 'Schrijf je in bij Cruks, verwijder alle bookmaker-apps en accounts, zet lage limieten in je bank-app en plan wat je doet tijdens wedstrijden. Kijk de eerste tijd liever samen met anderen dan alleen.'),
 ('Kan ik nog voetbal kijken als ik stop met gokken?', 'Ja, al voelt het eerst vlak zonder geld erop. Voor sommige mensen helpt het om een paar maanden minder live te kijken.'),
 ('Is live wedden gevaarlijker?', 'Live wedden geeft snelle, kleine inzetten en directe uitslagen. Daardoor raak je makkelijker in een roes, net als bij een gokkast.'),
])

# ======================= EN =======================
p = 'blog/what-to-do-after-gambling-relapse.html'
paras(p, [
 ('I gambled for more than eight years.', 'I gambled for eight years. I know the morning after, and the feeling of having let everyone down, yourself most of all.'),
 ('The shame after a relapse was the worst part.', founder('After one of my first attempts to stop, I relapsed. A lot of people do. It did not mean I could not do it. I have now been gambling-free for more than two years.')),
 ('Not tomorrow. Not after one more. Now.', 'Stop now, not tomorrow and not after one more.'),
])
edit(p, meta(p, 'Gambling relapse: what to do right after you gamble again',
             'Gambled again after stopping? What to do in the first hour, the first day and the first week, how to tell your family and when to get more help.'),
     lang='en', faqs=[
 ('Is relapse common when you stop gambling?', 'Yes. Many people need more than one attempt before stopping holds. I relapsed after one of my first attempts too. What matters is what you do in the next hours and days.'),
 ('Should I tell my partner I relapsed?', 'Yes, yourself and soon, ideally within a day. Being found out a second time does more damage than telling them. Say what happened and what you have already done to close the gap.'),
])

p = 'blog/gambled-away-paycheck-what-now.html'
paras(p, [
 ('Not from your credit card.', 'That includes credit cards, personal loans, payday lenders, friends and family. Do not try to scrape money together to fix the end of the month.'),
 ('No resignation letter', 'Do not make big decisions tonight. You are not quitting your job, ending your lease, selling the car or ending your relationship.'),
 ('Not tomorrow. Not when you are sober. Now.', 'Do it now, not tomorrow.'),
 ('Call your bank Monday morning.', 'Block gambling at your bank.'),
 ('Ask for a gambling block on your account', 'In the UK, most big banks, including Monzo, Starling, Barclays, HSBC, Lloyds and NatWest, let you switch on a gambling block in the app, often in a minute. In the US and Canada this is less common. Ask your bank or card issuer whether they can block gambling transactions, and lower your limits if they cannot.'),
 ('Until Monday: put your debit card', 'Until the block is on: put your debit card in a drawer. Hand it to someone else. Do something that puts it out of reach tonight.'),
 ('No excuses. No', 'Leave out the excuses and the promises. Just say what happened.'),
 ('Self-exclude tonight. Delete the apps. Write down', 'Self-exclude tonight. Delete the apps. Write down what happened. Tell one person. Switch on your bank\'s gambling block.'),
 ('Afterbetting helps you break the pattern', 'A day counter, a money overview and Help now when the urge hits. Start free.'),
])
edit(p, meta(p, 'Gambled away my paycheck: what to do in the next 24 hours',
             'Just gambled your paycheck or lost all your money gambling? What not to do tonight, what to do in the next 24 hours and how to cover rent and bills.',
             'Just gambled away my paycheck. What now?'),
     lang='en', before='<h2>What you say to other people</h2>', markdown=f'''
## Lost all your money gambling, not just one paycheck?

Sometimes it is more than one paycheck. Savings, a loan, money that was meant for something else. The steps stay the same, the gap is just bigger. That makes outside help more important.

Get free debt advice straight away. In the UK, StepChange and Citizens Advice can look at what has to be paid first and can talk to creditors for you. In the US, look for a nonprofit credit counsellor through the NFCC. How to pay it off step by step is in [how to pay off gambling debt]({B}rebuild-finances-after-gambling). Want to know how much it has been in total? The [gambling loss calculator]({B}how-much-have-i-lost-gambling) helps you work it out honestly.
''', faqs=[
 ('What should I do if I gambled my paycheck?', 'Do not gamble to win it back and do not borrow. Self-exclude tonight, delete the apps and block gambling at your bank. Then list what must be paid this month and call your landlord or creditors before a payment is missed.'),
 ('How do I pay rent after gambling my paycheck?', 'Work out what must be paid first, then call your landlord before the due date and ask for a short extension or a payment plan. If the gap is too big, get free debt advice: StepChange or Citizens Advice in the UK, a nonprofit credit counsellor in the US.'),
 ('Who can I talk to right now?', 'In the UK, the National Gambling Helpline on 0808 8020 133. In the US, call or text 1-800-MY-RESET (1-800-697-3738). Both are free and open 24/7. Thinking about suicide? Call Samaritans on 116 123 in the UK, or call or text 988 in the US and Canada.'),
])

p = 'blog/sleep-after-stopping-gambling.html'
paras(p, [
 ('Sleep was one of the first things that improved', founder('In the first weeks after I stopped, I woke up at night with one thought. The urges and the emptiness were worst in the evenings, the hours I used to bet. After a few weeks it got better, and my sleep came back.')),
])
edit(p, lang='en', faqs=[
 ('How long does bad sleep last after quitting gambling?', 'It differs per person. For me it got better after a few weeks. If you have slept badly for months, or it makes daily life hard, see your GP.'),
])

p = 'blog/partner-found-out-about-my-gambling.html'
paras(p, [
 ('Not "it is not as bad', 'So do not say it is not that bad, that it was only once or that you almost had it under control.'),
 ('Not "I am stopping now"', 'Do not say tonight that you are stopping, that you will go to therapy or that it will never happen again.'),
 ('No "I did it because', 'Do not explain it with stress at work, with how it started as a hobby or with the idea that everyone gambles a bit.'),
 ('If they say tonight that they want to leave', 'If they say tonight that they want to leave, that does not mean it is final. It means they need space. Give it, without begging, pressuring or piling up promises.'),
 ('Surviving an addiction is public work', 'Recovery does not happen in secret.'),
 ('Call your bank Monday. Ask for a gambling block', 'Switch on a gambling block at your bank, together. In the UK most banks let you do it in the app. Elsewhere, call your bank or card issuer and ask what they can block.'),
 ('Now take the next step.', 'Now take the next step. Self-exclude. Delete the apps. Switch on the bank block. Book real help. Write down what happened and read it back in six months.'),
 ('Afterbetting helps you make the difference', 'A day counter, a money overview and Help now. Plus includes a support circle: your partner gets a short weekly update of what you choose to share. Start free.'),
])
edit(p, meta(p, 'My Partner Found Out About My Gambling: What Now?',
             'Your partner just found out you gamble. What to say tonight, what to do in the first 48 hours and how to rebuild trust after gambling.',
             'My partner found out about my gambling. What now?'),
     lang='en', before='<h2>What if they leave</h2>', markdown=f'''
## How to rebuild trust after gambling

Trust does not come back with one good conversation. It comes back through small things that check out, again and again. Doing what you say. Telling them before they ask. Showing your money without it turning into a fight.

I know this from the other side. After I stopped, my stepfather found it hard to believe what I said. I understood that. After years of lies, trust does not come back with one conversation.

Why lying runs so deep in a gambling problem is in [gambling addict lying]({B}gambling-addict-lying).
''', faqs=[
 ('My partner found out I gamble. What do I say?', 'Keep it short and honest: that it is true, that it has been going on longer than you said and that you will answer every question honestly. Do not minimise it and do not make big promises tonight.'),
 ('How do I rebuild trust after gambling?', 'Through behaviour that checks out, again and again. Be open about money, tell them when you feel an urge and do what you say. It takes months, sometimes longer.'),
 ('Should my partner see my bank accounts?', 'For a while it can help, if you both want that. It is not a punishment but structure. Lying is harder when someone can see.'),
 ('What if my partner leaves me?', 'It can happen. Give them space without begging or pressuring. Stop for yourself, so your recovery does not depend on how the relationship goes.'),
])

p = 'blog/gambling-addiction-identity-loss.html'
paras(p, [
 ('I spent 8 years as a sports bettor.', founder('I bet mostly on sports for eight years. When I stopped, the urges and the emptiness were the hardest part of the first weeks. The emptiness sat in the evenings and weekends, the hours I used to bet. It got smaller as I filled those hours with fixed things: exercise, reading, a routine.')),
])
edit(p, meta(p, 'Who Am I Without Gambling? Emptiness After Quitting',
             'Feeling empty after you stopped gambling? Why gambling becomes part of who you are, and four places to start rebuilding. From a former sports bettor.'),
     lang='en', faqs=[
 ('How long does the emptiness last after quitting gambling?', 'There is no fixed time. For me it was strongest in the first weeks and got smaller as my evenings and weekends filled up. If low mood lasts, talk to your GP.'),
])
print('klaar')

# Nagekomen: og/twitter-titels met oude suffix-variant en een laatste ritme-zin (handmatig in dezelfde PR toegepast).
