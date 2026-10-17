# Opknapronde 4 (17 okt 2026): verzonnen founder-verhalen eruit, claims zonder bron eruit, NL partnerpagina genderneutraal.
# Founder bevestigde 17 okt: wel ooit hele salaris op een avond vergokt; niet: partner ontdekte het 3x, ex-citaat, tandarts, depressie na half jaar + POH-GGZ.
import re
DATE = '2026-10-17'

def edit(path, ops):
    s = open(path, encoding='utf-8').read()
    a = s.index('<article class="body">'); b = s.index('</article>', a)
    lines = s[a:b].split('\n')
    for key, new in ops:
        hits = [i for i, l in enumerate(lines) if key in l]
        assert len(hits) == 1, (path, key, len(hits))
        i = hits[0]
        if new is None: lines.pop(i)
        elif isinstance(new, tuple): lines[i] = lines[i].replace(*new)  # (oud, nieuw) binnen de regel
        else: lines[i] = new
    s = s[:a] + '\n'.join(lines) + s[b:]
    s = re.sub(r'"dateModified": ?"[^"]+"', f'"dateModified": "{DATE}"', s, count=1)
    assert '—' not in s
    open(path, 'w', encoding='utf-8').write(s)
    print('ok', path)

P = lambda t: f'<p>{t}</p>'

# ---------- Partner heeft mijn gokken ontdekt (NL) ----------
edit('nl/blog/partner-heeft-mijn-gokken-ontdekt.html', [
    ('Ik zat zelf in die woonkamer', P('Dit is een van de zwaarste avonden die je kunt hebben. Wat je de komende uren en weken doet, bepaalt meer dan wat je vanavond precies zegt.')),
    ('omdat ze die beloftes al eerder heeft gehoord', P('Niet omdat je het niet meent. Maar omdat je partner die beloftes misschien al eerder heeft gehoord, of het gevoel heeft dat dat zo is. Beloftes nu zijn lucht. En lucht maakt het erger.')),
    ('Laat haar zien dat je het doet', ('Laat haar zien dat je het doet', 'Laat zien dat je het doet')),
    ('Op haar tafel, voor haar ogen', P('<strong>Verwijder elke gok-app.</strong> Waar je partner bij is. Alle gok-apps en sites, browsergeschiedenis weg, e-mails van aanbieders uitschrijven.')),
    ('Apps op haar telefoon waarmee ze meekijkt', ('Apps op haar telefoon waarmee ze meekijkt', 'Laat je partner meekijken als die dat wil')),
    ('Met haar als getuige is liegen moeilijker', P('Dat is geen straf. Dat is structuur. Liegen gaat makkelijker als niemand meekijkt. Met iemand die meekijkt, is liegen moeilijker.')),
    ('<h2>Wat je niet moet verwachten van haar</h2>', '<h2>Wat je niet moet verwachten van je partner</h2>'),
    ('Een ding waar mannen vaak fout gaan', P('Een ding waar het na zo\'n avond vaak misgaat.')),
    ('Wat ze nu voelt is een mix', ('Wat ze nu voelt', 'Wat je partner nu voelt')),
    ('Geef haar ruimte om dat te voelen', P('Geef je partner ruimte om dat te voelen. Lang. Maanden lang. Wees er als je partner je nodig heeft. Wees er ook als dat niet zo is.')),
    ('Drie patronen die ik vaak zie', P('Drie patronen die het vaak erger maken.')),
    ('ze is al boos genoeg', ('Je denkt: ze is al boos genoeg', 'Je denkt: die is al boos genoeg')),
    ('Vertel haar als je een drang voelt', P('Vertel het als je een drang voelt. Vertel het als je een gokreclame hebt gezien die iets in je hoofd opende. Vertel het als je naar een wedstrijd kijkt en je oude denken even terugkomt. Niet om je partner te belasten. Om eerlijk te zijn over een proces.')),
    ('want ik heb haar pijn gedaan', ('want ik heb haar pijn gedaan', 'want ik heb mijn partner pijn gedaan')),
    ('niet hare. Maar je moet het wel doen', P('Je hebt zelf ook hulp nodig. Verslaving kwam ergens vandaan. Stress, eenzaamheid, een leeg gevoel, oude pijn, het kan allemaal meespelen. Dat onderzoeken is jouw werk, niet dat van je partner. Maar je moet het wel doen.')),
    ('wat haar uiteindelijk laat zien', ('wat haar uiteindelijk laat zien', 'wat je partner uiteindelijk laat zien')),
    ('Over wat dit met haar heeft gedaan', ('Over wat dit met haar heeft gedaan, en met wie ze nu is', 'Over wat dit met je partner heeft gedaan')),
    ('Wees niet verrast als zij nog vele maanden later', P('Wees niet verrast als je partner nog vele maanden later in tranen uitbarst over iets wat al lang besproken was. Het is geen ruzie zoeken. Het is verwerking die in een eigen tempo komt, niet in het jouwe.')),
    ('Ik heb mensen gekend wiens relatie', P('Niet elke relatie houdt het. Wat wel waar is:')),
    ('en vooral voor haar.', ('en vooral voor haar.', 'en vooral voor je partner.')),
    ('Als ze nu zegt dat ze weg wil', P('Als je partner nu zegt weg te willen, betekent dat niet dat het definitief is. Het betekent dat er ruimte nodig is. Ruimte geven is wat je doet. Niet smeken. Niet onder druk zetten. Niet beloften stapelen.')),
    ('Want als zij weggaat', ('Want als zij weggaat', 'Want als je partner weggaat')),
    ('Voor haar, voor jou, voor de kinderen', ('Voor haar, voor jou', 'Voor je partner, voor jou')),
])

# ---------- Partner found out (EN) ----------
edit('blog/partner-found-out-about-my-gambling.html', [
    ('I have sat in that living room', P('This is one of the hardest evenings you can have. What you do in the next hours and weeks matters more than exactly what you say tonight.')),
    ('Three patterns I see often', P('Three patterns that often make it worse.')),
    ('just how your brain works, all of it', ('just how your brain works, all of it', 'all of it')),
    ('I have known people whose relationship', P('Not every relationship survives this. Here is what is true:')),
    ('An addicted brain lies more easily', ('An addicted brain lies more easily when nobody is watching.', 'Lying is easier when nobody is watching.')),
])

# ---------- Mijn partner is gokverslaafd (NL) ----------
edit('nl/blog/mijn-partner-is-gokverslaafd-wat-doe-ik.html', [
    ('Dit artikel schrijf ik vanuit een andere kant', P('Dit artikel is voor de andere kant. Voor jou, als je partner gokt. Ik heb ruim acht jaar gegokt en weet hoe goed je iets kunt verbergen voor de mensen om je heen.')),
    ('Niet omdat haar gedrag verkeerd was', P('Wie naast iemand staat die gokt, staat vaak in het donker. De informatie die je nodig hebt om het te begrijpen, krijg je niet, omdat er gelogen wordt over alles wat ertoe doet. Dat ligt niet aan jou.')),
    ('Het is wat ik zelf had willen lezen', P('Wat hieronder volgt is geen lijstje tips. Het is wat ik vanuit de andere kant weet over hoe gokken werkt, en wat partners vaak zelf beschrijven.')),
    ('Dit zijn dingen die ik mijn partner zag doen', P('Dit zijn dingen die partners vaak doen. Goed bedoeld. Bijna allemaal averechts.')),
    ('Dit zijn dingen die ik mijn partner achteraf dankbaar', P('Hier wordt het concreter. Dit zijn dingen die vaak wel helpen.')),
    ('Van de oprichter:', None),
])

# ---------- My partner has a gambling problem (EN) ----------
edit('blog/my-partner-has-a-gambling-problem.html', [
    ('I am writing this from a different angle', P('This piece is for the other side. For you, if your partner gambles. I gambled for more than eight years, and I know how well you can hide it from the people closest to you.')),
    ('Not because what she did was wrong', P('If you are next to someone who gambles, you are often standing in the dark. The information you need to understand it is the information that gets hidden, because the lying covers everything that matters. That is not your fault.')),
    ('It is what I would have wanted to read', P('What follows is not a tips list. It is what I know from the other side about how gambling works, and what partners often describe themselves.')),
    ('These are things I saw my partner do', P('These are things partners often do. Well intentioned. Mostly counterproductive.')),
    ('These are things I am grateful in hindsight', P('Here it gets more concrete. These are things that often do help.')),
    ('because their brain is recalibrating', ('because their brain is recalibrating', 'while they adjust')),
    ('From the founder:', None),
])

# ---------- Salaris vergokt (NL) en paycheck (EN) ----------
edit('nl/blog/salaris-vergokt-wat-nu.html', [
    ('Ik heb het meerdere keren meegemaakt', P('Ik weet hoe het voelt. Ik heb ooit mijn hele salaris op een avond vergokt.')),
    ('Je hersenen staan in paniekmodus', ('Je hersenen staan in paniekmodus.', 'Je zit in paniek.')),
    ('Je hersenen zeggen nu: nog een keer', ('Je hersenen zeggen nu', 'Je hoofd zegt nu')),
])
edit('blog/gambled-away-paycheck-what-now.html', [
    ('I have lived it more than once', P('I know how it feels. I once gambled away my whole paycheck in a single evening.')),
    ('Your brain is in panic mode', ('Your brain is in panic mode.', 'You are in panic mode.')),
    ('Your brain is saying right now', ('Your brain is saying right now', 'Your head is saying right now')),
])

# ---------- Gokken, depressie en angst (NL) ----------
edit('nl/blog/gokken-depressie-en-angst.html', [
    ('Dus eerst dit: ik ben geen psycholoog', P('Dus eerst dit: ik ben geen psycholoog en geen psychiater. Wat hier staat is wat veel mensen in herstel beschrijven, aangevuld met wat ik zelf merkte na het stoppen. Het is geen diagnose. Het is geen behandeling. Als je in een donkere periode zit, ga naar je huisarts. Dat is de eerste stap, niet de laatste.')),
    ('<h3>Wat ik dacht versus wat het was</h3>', '<h3>Wat komt eerst: het gokken of de somberheid?</h3>'),
    ('Jarenlang dacht ik dat gokken mij depressief maakte', P('Veel mensen denken dat gokken hen somber maakt. Logisch. Je gokt, je verliest, je voelt je rot, dus het gokken veroorzaakt het rotgevoel.')),
    ('Toen ik een half jaar clean was', P('Maar sommige mensen merken na het stoppen dat de somberheid niet weggaat. Geen gokken, geen verliezen, en toch dezelfde leegte. Dat kan een schok zijn.')),
    ('Het bleek dat de depressie er altijd al was', P('Bij hen was het gokken misschien niet de oorzaak, maar een manier om iets anders niet te voelen. Als het gokken stopt, komt naar boven wat eronder zat.')),
    ('Voor mij was het deze volgorde', P('Bij de een komt het gokken eerst, bij de ander de somberheid. Allebei komt voor. Een huisarts kan helpen uitzoeken wat bij jou speelt.')),
    ('Gokken levert dopamine', P('Op dit moment zoek je een snelle manier om de dofheid te doorbreken. Gokken geeft spanning. En spanning voelt even als een oplossing.')),
    ('Want je dopamine-systeem heeft net', P('Maar daarna voelt het nog dieper. Na de spanning komt de terugval. Plus: je hebt geld verloren, of je hebt een belofte aan jezelf gebroken door weer te gokken.')),
    ('Daar staat het neurologische mechanisme', None),
    ('Je dopamine-systeem zit in onbalans', P('De eerste weken zonder gokken zijn zwaar. Ik merkte vooral leegte, triggers en dat ik \'s nachts wakker werd met de zin om te gokken. Veel mensen beschrijven ook slecht slapen, een wisselende stemming en prikkelbaarheid. Lees <a href="/nl/blog/afkickverschijnselen-gokken">afkickverschijnselen bij stoppen met gokken</a> voor wat je kunt verwachten.')),
    ('Het betekent dat je brein zich aanpast', P('Wat in deze fase belangrijk is: neem niet aan dat je slechter voelen betekent dat stoppen niet werkt. Bij mij werd het na een aantal weken stap voor stap beter. Dat is mijn ervaring, geen belofte.')),
    ('Bij de meeste mensen verbetert de stemming', None),
    ('Bij anderen, en daar hoorde ik bij', P('Bij anderen blijft er iets. Een grondtoon van zwaarte, ook zonder het gokken. Dat kan een somberheid of angst zijn die er al was, en die nu zichtbaar wordt omdat het gokken er niet meer overheen ligt.')),
    ('kon geen therapie of medicatie echt aanslaan', P('Maar het is ook het moment waarop je er echt iets aan kunt doen. Zolang je gokte, zat het gokken overal tussen.')),
    ('<h2>Wat hielp bij mij</h2>', '<h2>Wat kan helpen</h2>'),
    ('Dit is wat bij mij heeft geholpen, naast het stoppen', P('Dit is geen lijstje wat voor iedereen werkt. Het zijn stappen die veel mensen helpen, naast het stoppen met gokken zelf.')),
    ('Dit was de stap waar ik het meest tegenop zag', P('Voor veel mensen is dit de stap waar ze het meest tegenop zien. Het idee dat je het zelf moet kunnen, houdt lang tegen.')),
    ('Ik kreeg een verwijzing naar de POH-GGZ', P('De huisarts is geen rechter. Geen instantie waar je punten verdient of verliest. Het is iemand met medische kennis die met je meedenkt, en die je zo nodig kan doorverwijzen, bijvoorbeeld naar de praktijkondersteuner GGZ of de verslavingszorg.')),
    ('omdat je lichaam beweging nodig heeft om hormonen', P('Niet sporten om af te vallen. Niet hardlopen voor een tijd. Bewegen omdat het helpt. Mij hielp sporten in de eerste weken na het stoppen, samen met regelmaat en lezen over zelfontwikkeling.')),
    ('doet meer dan elke welness-tip', P('Een half uur buiten lopen per dag, zonder telefoon, is een goed begin.')),
    ('Wat ik onderschatte was hoe lang', P('Herstel duurt vaak langer dan je hoopt. Dat is geen slecht nieuws. Het is informatie. Het scheelt teleurstelling als het na drie maanden nog niet "klaar" is.')),
    ('Mensen die ik ken die jaren clean zijn', None),
    ('Ik weet hoe overtuigend die stem is', P('Dat klopt niet. Die stem kan heel overtuigend zijn. Ik ben nu ruim twee jaar gestopt en sta op een plek waar ik vroeger niet in geloofde. Niet omdat ik bijzonder ben. Stoppen en eerlijke hulp zoeken werkt, ook als het op het moment niet zo voelt.')),
])

# ---------- Gambling, depression and anxiety (EN) ----------
edit('blog/gambling-depression-and-anxiety.html', [
    ('So first: I am not a clinician', P('So first: I am not a clinician. What is here is what many people in recovery describe, plus what I noticed myself after stopping. It is not a diagnosis. It is not treatment. If you are in a dark period, see your doctor. That is the first step, not the last.')),
    ('<h3>What I thought versus what it was</h3>', '<h3>What comes first: the gambling or the low mood?</h3>'),
    ('For years I thought gambling was making me depressed', P('Many people assume gambling is what makes them feel low. Logical. You gamble, you lose, you feel awful, so the gambling causes the awful feeling.')),
    ('When I was six months clean', P('But some people find that after stopping, the low mood does not lift. No gambling, no losses, and still the same emptiness. That can come as a shock.')),
    ('It turned out the depression had always been there', P('For them, gambling may not have been the cause but a way of not feeling something else. When the gambling stops, what was underneath comes up.')),
    ('For me, that was the order', P('For some people the gambling comes first, for others the low mood. Both happen. A doctor can help you work out what is going on for you.')),
    ('Gambling delivers dopamine', P('In that moment you are looking for a quick way to break the numbness. Gambling gives you excitement. And excitement feels like a solution for a moment.')),
    ('Either way, the brain has to come back to baseline', P('The session ends. You have lost money, or you have won and ended on a high. Either way, the excitement fades. And where you started was already low.')),
    ('Because your dopamine system has just had a large peak', P('But now it feels even lower. After the excitement comes the drop. Plus: you lost money, or you broke a promise to yourself by gambling again.')),
    ('The neurological mechanism is explained there', None),
    ('Your dopamine system is in imbalance', P('The first weeks without gambling are hard. What I noticed most was emptiness, triggers and waking up at night wanting to gamble. Many people also describe poor sleep, mood swings and irritability. Read <a href="https://afterbetting.com/blog/gambling-withdrawal-symptoms">gambling withdrawal symptoms</a> for what to expect.')),
    ('It means your brain is recalibrating', P('What matters in this phase: do not assume that feeling worse means stopping is not working. For me it got better step by step after a few weeks. That is my experience, not a promise.')),
    ('mood improves noticeably over two to six months', None),
    ('For others, and I was in that group', P('For others something remains. A baseline of heaviness, even without the gambling. That can be low mood or anxiety that was already there, and is now visible because gambling is no longer covering it.')),
    ('no therapy', P('But it is also the moment you can actually do something about it. While you were gambling, the gambling got in the way of everything.')),
    ('<h2>What helped me</h2>', '<h2>What can help</h2>'),
    ('This is what helped me, alongside stopping', P('This is not a list of what works for everyone. These are steps that help many people, alongside stopping gambling itself.')),
    ('This was the step I most resisted', P('For many people this is the step they resist most. The idea that you should be able to handle it yourself holds people back for a long time.')),
    ('I got a referral', P('A doctor is not a judge. Not an institution where you earn or lose points. It is someone with medical knowledge who thinks it through with you, and who can refer you on if needed, for example to talking therapy or a gambling clinic.')),
    ('to regulate hormones', P('Not exercise to lose weight. Not running for a time. Moving because it helps. Exercise helped me in the first weeks after stopping, together with routine and reading about self-development.')),
    ('does more than any wellness tip', P('Half an hour outside each day, without your phone, is a good start.')),
    ('What I underestimated was how long', P('Recovery often takes longer than you hope. That is not bad news. That is information. It saves you disappointment when it is not "done" at three months.')),
    ('People I know who are years clean', None),
    ('I know how convincing that voice is', P('That is not true. That voice can be very convincing. I have now been gambling-free for over two years and I am in a place I did not believe in back then. Not because I am special. Stopping and getting honest help works, even when it does not feel like it in the moment.')),
])

# ---------- Sportgokken verslaving (NL) ----------
SRC_SPORT = ('<h2>Bronnen</h2>\n<ul><li><a href="https://www.trimbos.nl/kennis/digitale-media-gokken/expertisecentrum-gokken/cijfers-gokken/gokverslaving/" rel="noopener">Trimbos-instituut, cijfers over gokverslaving (LADIS)</a></li>'
             '<li><a href="https://nos.nl/l/2576926" rel="noopener">NOS, steeds meer gokkers kiezen voor een gokstop (juli 2025)</a></li></ul>\n')
edit('nl/blog/sportgokken-verslaving.html', [
    ('Dit artikel zet de zaken op een rij', P('Dit artikel zet de zaken op een rij. Eerlijk.') + '\n' + P('Ik was zelf acht jaar sportwedder. Ik dacht dat mijn kennis me hielp. Stoppen betekende toegeven dat die kennis me nooit echt had geholpen, en dat het systeem dat ik had gebouwd een verhaal was dat ik mezelf vertelde.')),
    ('In 2021 ging de Nederlandse online gokmarkt open', P('Op 1 oktober 2021 ging de Nederlandse online gokmarkt open. Sindsdien zie je de reclames en sponsoring overal: op tv, op podcasts, in apps, op sportshirts.')),
    ('luiden inmiddels de noodklok', P('Steeds meer mensen zoeken hulp. In 2025 waren 3.108 mensen in de verslavingszorg in behandeling voor gokken, 13% meer dan in 2024. Van hen is 87% man en de gemiddelde leeftijd is 34 jaar (LADIS, via het Trimbos-instituut).')),
    ('Vooral jonge mannen zitten in de risicogroep', P('Ook bij Cruks zie je het: meer dan 100.000 mensen hebben zichzelf laten uitsluiten, en de helft van hen is jonger dan 32 (NOS, juli 2025).')),
    ('In 2025 voerde de Nederlandse overheid', None),
    ('Als je drie of meer kunt aanstippen', P('Herken je er meerdere? Dan is het tijd om er eerlijk naar te kijken. Dit is geen test en geen diagnose. Wel een spiegel.')),
    ('Als je vijf of meer kunt aanstippen', None),
    ('dopaminebommen als ze raken', ('dopaminebommen als ze raken', 'en een enorme kick als er eentje raakt')),
    ('letterlijk minder dopamine', P('Als je stopt met sportgokken, voelt sport een tijd lang vlak. Een wedstrijd kijken zonder geld erop mist de spanning die je gewend was. Dat went.')),
    ('Met dezelfde dopamine-mechanismen', P('Het is gokken. Met dezelfde verslavende kracht. Dezelfde gevolgen voor je financiën, relaties en hoofd.')),
    ('<div class="cta-block">', ('<div class="cta-block">', SRC_SPORT + '<div class="cta-block">')),
])

# ---------- Gokverslaving en identiteit (NL) ----------
edit('nl/blog/gokverslaving-en-identiteit.html', [
    ('Stoppen met gokken voelt daarom niet als een gewoonte afleren', P('Stoppen met gokken voelt daarom niet als een gewoonte afleren. Het voelt als afscheid nemen van wie je bent.') + '\n' + P('Ik herken dat. Ik was acht jaar sportwedder. Toen ik stopte, bleef er een leegte over die ik eerst niet kon plaatsen.')),
    ('Wat je voelt is je dopaminesysteem in herstel', P('Wat je voelt, is geen "leven zonder gokken". Het is de ruimte die het gokken achterliet, voordat er iets anders in zit. Bij mij zat die leegte in de avonden en weekenden, de uren waarop ik vroeger speelde. Ze werd kleiner naarmate ik die uren vulde met vaste dingen.')),
    ('Dit duurt. Niet eeuwig. Wel maanden.', P('Dat gaat niet in een week over. Maar het blijft niet zo.')),
    ('Wat doet gokken met je hersenen?</a>', P('Lees ook: <a href="/nl/blog/hoe-vul-ik-mijn-tijd-zonder-gokken">Hoe vul je je tijd zonder gokken?</a>')),
])

# ---------- Gokken aan je familie vertellen (NL) ----------
edit('nl/blog/gokken-aan-je-familie-vertellen.html', [
    ('Soms een verhaal dat erger is dan de waarheid.', ('Soms een verhaal dat erger is dan de waarheid.</p>', 'Soms een verhaal dat erger is dan de waarheid.</p>\n' + P('Uit eigen ervaring: als een naaste het zelf ontdekt, doet het vaak meer pijn dat je het niet met hem of haar kon delen, dan wat er gebeurd is. Vertrouwen is het belangrijkste wat er op het spel staat. Het is eerst eng en beschamend. Maar daarna kun je er samen aan werken.'))),
])

# ---------- Geld terugvragen online casino (NL) ----------
edit('nl/blog/geld-terugvragen-online-casino.html', [
    ('Aanbieders die bekend zijn uit deze periode', P('Heb je voor 1 oktober 2021 gespeeld bij een aanbieder zonder Nederlandse vergunning die zich op Nederland richtte? Dan is er reden om je situatie te laten beoordelen. Noteer bij welke aanbieders en in welke periode je speelde.')),
    ('Bij verliezen onder ongeveer 5.000 euro', P('Laat je eerst informeren voordat je zelf iets indient. Bij <a href="https://www.juridischloket.nl/" rel="noopener">Het Juridisch Loket</a> kun je gratis vragen wat in jouw situatie mogelijk is.')),
    ('Veel werken op no-cure-no-pay', P('Bij grotere bedragen, bij meerdere aanbieders of bij twijfel: zoek een advocaat of bureau met ervaring in online gokzaken. Vraag vooraf altijd hoe ze rekenen, en welk deel van een eventuele opbrengst ze zelf houden.')),
])
