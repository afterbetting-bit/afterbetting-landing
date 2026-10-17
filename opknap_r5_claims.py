# Opknapronde 5 (17 okt 2026): hersenclaims zonder bron en niet-bevestigde ik-verhalen uit oudere pagina's.
exec(open('opknap_r4.py', encoding='utf-8').read().split("P = lambda")[0])
P = lambda t: f'<p>{t}</p>'

edit('nl/blog/omgaan-met-gokverslaafde-naaste.html', [
    ('In die jaren probeerden mijn partner, mijn ouders', P('Ik schrijf dit vanaf de andere kant. Ik heb meer dan 8 jaar gegokt, meer dan 40.000 euro schuld opgebouwd en ben nu ruim 2 jaar gestopt. Ik weet hoe goed je iets kunt verbergen voor de mensen om je heen. Dit artikel gaat over wat naasten vaak helpt, en wat het erger maakt.')),
    ('Toen mijn naasten mij confronteerden met bewijs', P('Dit is de moeilijkste waarheid om te accepteren. Als je iemand confronteert met bewijs, bankafschriften, leugens, missend geld, is de eerste reactie vaak ontkenning. Niet omdat diegene dom is. Maar omdat toegeven betekent dat er gestopt moet worden. En stoppen lijkt op dat moment onmogelijk.')),
    ('Mijn ouders probeerden mij te bereiken', P('Maak het klein. Geen familieberaad aan tafel. Een rustig gesprek, met z\'n tweeën.')),
])

edit('nl/blog/slaapproblemen-stoppen-met-gokken.html', [
    ('heb je je hersenen overprikkeld met dopaminepieken', P('Maandenlang of jarenlang stond je systeem aan. Slotmachines, sportwedstrijden, online roulette: allemaal gemaakt om je scherp en gespannen te houden. Ook \'s avonds en \'s nachts.')),
    ('Je dopamine baseline verschoven', P('Je ritme was ontregeld. Je sliep op rare tijden, of te kort.')),
    ('Je hersenen krijgen niet meer wat ze gewend waren', P('Nu stop je. De spanning valt weg, maar je lichaam is nog niet gewend aan rust. Bij mij werd de slaap na een aantal weken weer echt goed. Maar die eerste weken waren onrustig.')),
    ('<p>Wat er fysiek gebeurt:</p>', P('Wat veel mensen merken:')),
    ('Cortisol (stresshormoon) blijft hoog', '<li>Je blijft gespannen</li>'),
    ('Dopamine afgevlakt, waardoor', '<li>Je voelt je vlak en rusteloos tegelijk</li>'),
    ("Hersenactiviteit 's avonds nog hoog", "<li>Je hoofd blijft 's avonds druk</li>"),
    ('Daglicht in je ogen geeft je hersenen het signaal', P('Daglicht in de ochtend helpt veel mensen om hun ritme terug te vinden. Ook bij bewolkt weer.')),
    ('Beweging verlaagt cortisol', P('Een uur lopen per dag is geen luxe. Beweging helpt tegen onrust en maakt je \'s avonds op een natuurlijke manier moe. Mij hielp sporten in die eerste weken. Niet vlak voor het slapengaan intensief sporten. Lichte beweging in de avond mag wel.')),
    ('Je hersenen krijgen toestemming om los te laten', P('Dit haalt gedachten uit je hoofd en op papier. Dan hoef je ze niet meer vast te houden.')),
    ('Je hersenen slapen beter in een grot', ('Je hersenen slapen beter in een grot dan in een woonkamer.', 'Een donkere, koele kamer slaapt voor de meeste mensen beter.')),
    ('leert je hersenen dat het bed een tobplek is', ('In bed liggen tobben leert je hersenen dat het bed een tobplek is.', 'Lang wakker liggen en tobben maakt van je bed een tobplek.')),
])

edit('nl/blog/sneeuwbalmethode-gokschulden.html', [
    ('ervaring heeft met dopaminepieken', P('Als gokker ben je gewend aan snelle beloningen. Inzet, uitslag, gevoel. Binnen een paar seconden.')),
    ('Wat gokken in je hersenen heeft achtergelaten', P('Dat verdwijnt niet zomaar. Je zoekt nog steeds momenten die iets opleveren. Niet omdat je zwak bent.')),
    ('Een dopamineshot die niets kost', P('De sneeuwbalmethode geeft je die momenten op een gezonde manier. Elke keer dat een schuld dicht gaat, is dat een echte overwinning. Een schouderklop die niets kost en alles oplevert.')),
    ('Vraag tien procent van je beschikbare budget', ('Vraag tien procent van je beschikbare budget terug voor menselijke dingen.', 'Houd een klein deel van je budget vrij voor menselijke dingen.')),
])

edit('nl/blog/mijn-kind-is-gokverslaafd.html', [
    ('het beloningssysteem in de hersenen kaapt', ('Het is een verslaving die het beloningssysteem in de hersenen kaapt, en die kan iedereen treffen.', 'Het is een verslaving, en die kan iedereen treffen.')),
])

for path, k in [('nl/blog/hoe-lang-duurt-herstel-gokverslaving.html', 'nl'), ('blog/how-long-gambling-recovery-takes.html', 'en')]:
    if k == 'nl':
        edit(path, [
            ('Dit is je dopaminesysteem dat zich aanpast', P('Zo kan het voelen als iets wegvalt dat jarenlang je dagen en je hoofd vulde. De spanning kwam altijd op onvoorspelbare momenten. Nu blijft die uit. Dat moet wennen.')),
            ('omdat beweging cortisol en adrenaline afbouwt', ('omdat beweging cortisol en adrenaline afbouwt', 'omdat beweging helpt tegen de onrust')),
            ('Je hersenen zijn niet meer in volle paniek', ('Je hersenen zijn niet meer in volle paniek, maar ook nog lang niet hersteld.', 'De ergste onrust is voorbij, maar je bent er nog niet.')),
            ('om hersenen herkenningspunten te geven', ('om hersenen herkenningspunten te geven', 'om je dagen herkenningspunten te geven')),
            ('Elke dag clean is een dag waarin je hersenen', ('Elke dag clean is een dag waarin je hersenen iets minder hard werken om de oude rotzooi vast te houden. Onzichtbaar. Cumulatief. Onomkeerbaar als je doorzet.', 'Elke dag zonder gokken maakt de volgende dag een beetje makkelijker. Niet altijd zichtbaar, maar het telt op.')),
        ])
    else:
        edit(path, [
            ('This is your dopamine system adjusting', P('This is what it can feel like when something that filled your days and your head for years falls away. The excitement always came at unpredictable moments. Now it stops. That takes getting used to.')),
            ('because movement burns down cortisol and adrenaline', ('because movement burns down cortisol and adrenaline', 'because moving helps with the restlessness')),
            ('Your brain is no longer in full panic', ('Your brain is no longer in full panic, but also nowhere near recovered.', 'The worst of the restlessness has passed, but you are not through it yet.')),
            ('to give your brain landmarks', ('to give your brain landmarks', 'to give your days landmarks')),
            ('Every clean day is a day your brain works', ('Every clean day is a day your brain works a little less hard to hold on to the old mess. Invisible. Cumulative. Irreversible if you keep going.', 'Every day without gambling makes the next one a little easier. Not always visible, but it adds up.')),
        ])

edit('nl/blog/gokverslaving-symptomen-en-kenmerken.html', [
    ('Hoe je hersenen op dopamine reageren staat in', P('Wat gokken met je hoofd doet, lees je in <a href="/nl/blog/wat-doet-gokken-met-je-hersenen">Wat doet gokken met je hersenen</a>. Het belangrijkste: dat je er moeilijk mee stopt, is geen karakterzwakte.')),
    ('Je hersenen hebben er belang bij dat je niet zeker weet', ('Je hersenen hebben er belang bij dat je niet zeker weet of er een probleem is, want zekerheid leidt tot actie.', 'Zolang je twijfelt, hoef je nog niets te veranderen. Zekerheid vraagt om actie.')),
])
edit('blog/gambling-addiction-symptoms-and-signs.html', [
    ('How the brain responds to dopamine is covered in', P('What gambling does to your head is covered in <a href="https://afterbetting.com/blog/what-happens-to-your-brain-when-you-stop-gambling">What does gambling do to your brain?</a> The key point: finding it hard to stop is not a character flaw.')),
    ('Your brain has an interest in keeping you unsure', ('Your brain has an interest in keeping you unsure that there is a problem, because certainty leads to action.', 'As long as you are unsure, you do not have to change anything. Certainty demands action.')),
])

edit('blog/does-self-exclusion-work-gambling.html', [
    ('prevents a percentage of rela', ('prevents a percentage of relapses that would otherwise happen', 'can be enough to stop a bet that would otherwise have happened')),
    ('Research on self-exclusion programmes shows', P('It is not theatre. When you are excluded and try to log in, you cannot. The barrier is real, even if it is not complete.')),
    ('The research is clear:', '<div class="callout"><p><strong>From the founder:</strong> Self-exclusion works best as one layer of a broader structure. What made the difference for me was a daily routine, especially for the evenings and weekends, the hours I used to gamble.</p></div>'),
])

edit('blog/how-to-stop-gambling-urges-weekends.html', [
    ('Your brain has been trained over years to associate free time', ('Your brain has been trained over years to associate free time with gambling.', 'Over the years, free time and gambling became linked.')),
    ('When you remove the behaviour, the brain still sends the signal', ('When you remove the behaviour, the brain still sends the signal.', 'When you stop, the pull is still there.')),
    ('It is a sign that your brain learned a pattern', ('It is a sign that your brain learned a pattern.', 'It is a sign that you learned a pattern.')),
    ('What helped most was filling Saturday morning', ('What helped most was filling Saturday morning so specifically that by the time the afternoon arrived, I was already tired and satisfied.', 'What helped most was filling those hours with fixed things at fixed times.')),
])

edit('blog/what-to-do-instead-of-gambling.html', [
    ('The dopamine of anticipation, the adrenaline of live events', ('The dopamine of anticipation, the adrenaline of live events.', 'The tension of waiting, the rush of live events.')),
    ("The brain's reward system is recalibrated around", P('Next to the excitement gambling gave you, everything else can feel flat at first. That is normal, and it does not stay that way.')),
    ('long enough for the brain to recalibrate', ('long enough for the brain to recalibrate', 'long enough for it to start feeling normal again')),
])

edit('blog/how-to-tell-family-about-gambling-problem.html', [
    ('From the founder:', None),
])
