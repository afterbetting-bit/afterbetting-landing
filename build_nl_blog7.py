import json
CSS = open("nl/blog/stoppen-met-gokken.html").read().split("<style>")[1].split("</style>")[0]
GA = '<script async src="https://www.googletagmanager.com/gtag/js?id=G-BC3QG79LQ0"></script><script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag("js",new Date());gtag("config","G-BC3QG79LQ0");</script>'
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,wght@0,300;0,400;1,300&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">'
NAV = '<nav><a href="/nl/" class="logo">after<span>betting</span></a><div class="nav-links"><a href="/nl/#how">Hoe het werkt</a><a href="/nl/#features">Functies</a><a href="/nl/#pricing">Prijzen</a><a href="/nl/blog">Blog</a><a href="https://app.afterbetting.com/login">Inloggen</a></div><a href="https://app.afterbetting.com/onboarding" class="btn">Begin gratis</a></nav>'
CRISIS = '<div class="crisis-footer"><p>Zit je nu in crisis? Bel de <strong>Nationale Hulplijn Gokken: 0800-1995</strong>. Gratis. Anoniem. 24 uur per dag.</p></div>'
FOOTER = '<footer><p>&copy; 2026 Afterbetting &middot; <a href="/nl/">Home</a> <a href="/nl/blog">Blog</a> <a href="/nl/about">Over ons</a> <a href="https://app.afterbetting.com/privacy">Privacy</a> <a href="https://app.afterbetting.com/terms">Voorwaarden</a> <a href="mailto:info@afterbetting.com">Contact</a></p><p style="margin-top:.5rem">Geen medische dienst. Neem contact op met een erkend professional voor klinische ondersteuning.</p></footer>'

slug = "partner-heeft-mijn-gokken-ontdekt"
url = f"https://afterbetting.com/nl/blog/{slug}"
title = "Partner heeft mijn gokken ontdekt. Wat nu."
desc = "Partner heeft je gokken ontdekt? Wat je nu zegt en doet bepaalt of de relatie overleeft. Geen scripts. Wel eerlijke stappen."

sa = json.dumps({"@context":"https://schema.org","@type":"Article","headline":"Mijn partner heeft ontdekt dat ik gok. Wat nu.","author":{"@type":"Organization","name":"Afterbetting"},"publisher":{"@type":"Organization","name":"Afterbetting","url":"https://afterbetting.com"},"datePublished":"2026-05-09","dateModified":"2026-05-09","inLanguage":"nl","url":url})
sb = json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://afterbetting.com/nl/"},{"@type":"ListItem","position":2,"name":"Blog","item":"https://afterbetting.com/nl/blog"},{"@type":"ListItem","position":3,"name":"Partner heeft mijn gokken ontdekt","item":url}]})

hero = '<section class="hero"><div class="hero-inner"><div class="bc"><a href="/nl/">Home</a> &rarr; <a href="/nl/blog">Blog</a> &rarr; Relatie</div><div class="tag">Relatie</div><h1>Mijn partner heeft ontdekt dat ik gok. Wat nu.</h1><p style="font-size:1.1rem;color:var(--mid);font-weight:300;line-height:1.7;margin-top:1rem">Het is uit. Ze weet het. Of hij. Wat nu komt is moeilijker dan stoppen met gokken zelf. En tegelijk de enige manier waarop dit goed kan komen.</p><div class="meta">Door Afterbetting &middot; 9 mei 2026 &middot; 9 min lezen</div></div></section>'

body = """<p>Misschien vond ze een afschrift. Misschien zag hij een melding op je telefoon. Misschien heb je het zelf verteld omdat je het niet meer kon dragen.</p>
<p>Hoe het ook is gebeurd, het is gebeurd. En nu zit je in de andere kamer. Of in de auto. Of jullie zitten tegenover elkaar en niemand weet wat te zeggen.</p>
<p>Ik zat zelf in die woonkamer. Niet een keer. Meerdere keren. De eerste keer loog ik me eruit. De tweede keer ook. De derde keer kon het niet meer. De relatie hield het. Niet door wat ik die avond zei. Door wat ik in de maanden daarna deed.</p>
<p>Dit artikel gaat over allebei. Wat je vannacht zegt, en wat je daarna doet.</p>
<h2>Eerst: wat je nu niet doet</h2>
<p>Drie dingen. Belangrijker dan wat je wel doet.</p>
<p><strong>Een: je bagatelliseert het niet.</strong></p>
<p>Niet "het is niet zo erg als je denkt". Niet "het is maar een keer geweest". Niet "ik had het bijna onder controle".</p>
<p>Ze weet beter. Iedereen die langer dan een week met je samenwoont voelt al dat er iets niet klopt. Wat ze nu net heeft gevonden is geen ontdekking. Het is een bevestiging.</p>
<p>Bagatelliseren is wat liegen voortzet onder andere kleren. Doe het niet.</p>
<p><strong>Twee: je belooft niets in deze eerste 24 uur.</strong></p>
<p>Niet "ik stop nu". Niet "ik ga in therapie". Niet "het gebeurt nooit meer".</p>
<p>Niet omdat je het niet meent. Maar omdat ze die beloftes al eerder heeft gehoord, of omdat haar gevoel zegt dat ze ze al eerder gehoord moet hebben. Beloftes nu zijn lucht. En lucht maakt het erger.</p>
<p>Wat je vannacht doet is luisteren en eerlijk zijn. Beloftes komen later, in concrete stappen. Niet in woorden.</p>
<p><strong>Drie: je verdedigt jezelf niet.</strong></p>
<p>Wat je gedaan hebt is niet uit te leggen op een manier waardoor het minder erg wordt. Probeer het niet.</p>
<p>Geen "ik deed het omdat het op werk niet goed ging". Geen "het begon als hobby". Geen "iedereen wedt weleens".</p>
<p>Verdedigen is reflex. Het werkt nu tegen je. Je partner heeft geen behoefte aan jouw verklaring. Ze heeft behoefte aan een eerlijk antwoord.</p>
<h2>Wat je wel zegt</h2>
<p>Hou het kort. Hou het waar.</p>
<p>Iets in de richting van:</p>
<p>"Je hebt gelijk. Ik gok. Ik gok al langer dan ik zeg. Ik weet niet of ik het je vannacht volledig kan uitleggen. Ik wil niet liegen. Vraag wat je wilt vragen, dan zal ik eerlijk antwoord geven."</p>
<p>Dat is genoeg. Dat is meer dan ze van je gewend was.</p>
<p>Daarna: stil zijn. Laten komen wat komt.</p>
<p>Wat er komt is meestal een lawine. Vragen. Hoeveel. Hoe lang. Welk geld. Hoe vaak gelogen. Of er meer is. Of er nog meer is.</p>
<p>Antwoord eerlijk op alles. Ook als de waarheid erger is dan ze dacht. Ook als ze gaat huilen. Ook als ze gaat schreeuwen. Ook als ze niets meer zegt.</p>
<p>Liever twee keer in een avond pijn dan tien keer pijn over tien maanden.</p>
<h2>De vragen die je niet kunt beantwoorden</h2>
<p>Drie vragen die zeker komen, en waarop je geen goed antwoord hebt.</p>
<p><strong>"Waarom?"</strong></p>
<p>Eerlijk: je weet het niet. Niemand kan dat in een zin uitleggen. Het zou genoeg zijn om te zeggen: "Ik weet het niet helemaal. Ik weet dat het iets is in mijn hoofd dat sterker werd dan ikzelf. Daar heb ik hulp bij nodig om te begrijpen."</p>
<p>Dat is geen excuus. Dat is een eerlijke erkenning dat je niet de enige bent die hier antwoorden voor zoekt.</p>
<p><strong>"Hoe kan ik je nu nog vertrouwen?"</strong></p>
<p>Hier ben je voorzichtig.</p>
<p>Niet "vertrouw me, ik beloof het". Wel "ik weet niet of je me nu kunt vertrouwen, en je hoeft dat ook niet te doen op basis van wat ik vannacht zeg. Ik wil het terugverdienen. Dat duurt lang."</p>
<p>Vertrouwen is geen ja-of-nee. Het is een trage opbouw. Ze hoeft je niet morgen te vertrouwen. Ze hoeft alleen te zien dat je vandaag iets anders doet dan gisteren.</p>
<p><strong>"Wat ga je nu doen?"</strong></p>
<p>Dit is de enige vraag waar je vannacht een eerste antwoord op kunt geven. Niet door grote beloftes te doen. Wel door te zeggen wat je morgen concreet als eerste stap zet.</p>
<p>Bijvoorbeeld: "Ik ga me morgen uitsluiten via Cruks. Ik ga maandag mijn bank bellen voor een gokblokkade. Ik ga deze week contact opnemen met de Nationale Hulplijn Gokken. Ik weet dat het meer is dan dat. Maar dit zijn de eerste drie dingen."</p>
<p>Concrete stappen, geen beloftes. Wat je gaat doen, niet wie je gaat zijn.</p>
<h2>De eerste 48 uur na de ontdekking</h2>
<p>Hier is wat er feitelijk moet gebeuren.</p>
<p><strong>Sluit jezelf uit via Cruks.</strong> cruks.nl. Tien minuten. Doe het waar je partner bij is. Laat haar zien dat je het doet. Niet als ritueel, maar omdat het gebeurde.</p>
<p><strong>Verwijder elke gok-app.</strong> Op haar tafel, voor haar ogen. Toto, Bet365, Unibet, Betcity, Holland Casino Online, alles. Browsergeschiedenis weg. E-mails uitschrijven.</p>
<p><strong>Geef toegang tot je financien.</strong> Voor zover dat past in jullie relatie. Volledige openheid van bankrekeningen, creditcards, eventuele aparte accounts. Apps op haar telefoon waarmee ze meekijkt. Niet voor altijd, wel voor nu.</p>
<p>Dat is geen straf. Dat is structuur. Een verslaafd brein liegt makkelijker als niemand meekijkt. Met haar als getuige is liegen moeilijker.</p>
<p><strong>Bel maandag je bank.</strong> Gokblokkade aanvragen op rekening en creditcard. Je partner kan meeluisteren. Doe het op de luidspreker.</p>
<p><strong>Maak een afspraak voor hulp.</strong> Deze week, niet over twee weken. Verslavingszorg via Jellinek, Tactus, of een regionaal centrum. Of begin met een huisarts. Een afspraak. Een persoon erbij.</p>
<p>Lees ook: <a href="/nl/blog/zelfuitsluiting-gokken-werkt-het">Werkt zelfuitsluiting bij gokken</a> en <a href="/nl/blog/stoppen-met-gokken">Stoppen met gokken, een eerlijke gids</a>.</p>
<h2>Wat je niet moet verwachten van haar</h2>
<p>Een ding waar mannen vaak fout gaan na zo'n nacht.</p>
<p>Je verwacht erkenning. Je verwacht dat ze ziet hoe moeilijk je het hebt. Je verwacht dat ze, omdat jij eerlijk bent geweest, jou nu helpt om het draaglijk te maken.</p>
<p>Dat gaat niet gebeuren. Tenminste niet de eerste maanden.</p>
<p>Wat ze nu voelt is een mix die je niet kunt fixen door extra eerlijk te zijn of extra je best te doen. Verraden. Boos. Verdrietig. Bang voor de toekomst. Geld-onzeker. Zichzelf afvragend wat er nog meer niet klopt.</p>
<p>Geef haar ruimte om dat te voelen. Lang. Maanden lang. Wees er als ze je nodig heeft. Wees er ook als ze je niet nodig heeft.</p>
<p>Verwacht geen vergeving op een tijdlijn die jou uitkomt. Vergeving heeft geen tijdlijn. Soms komt het. Soms komt het pas na jaren. Soms komt het niet helemaal.</p>
<p>Wat je kunt doen is consistent zijn. Elke dag. Niet een goede week, dan een mindere maand. Elke dag opnieuw laten zien dat de man die ze trouwde of met wie ze leeft, weer terugkomt.</p>
<p>Lees ook: <a href="/nl/blog/gokverslaving-en-identiteit">Gokverslaving en wie je bent</a>.</p>
<h2>Wat je niet moet doen in de weken erna</h2>
<p>Drie patronen die ik vaak zie. Ze maken het erger.</p>
<p><strong>Patroon een: zwijgen om de vrede te bewaren.</strong></p>
<p>Je denkt: ze is al boos genoeg, ik zeg vandaag maar niets meer. Dat is precies fout. Geheimhouding heeft je hier gebracht. Geheimhouding nu, ook al lijkt het kleine geheimhouding, is hetzelfde mechanisme.</p>
<p>Vertel haar als je een drang voelt. Vertel haar als je een gokreclame hebt gezien die iets in je hoofd opende. Vertel haar als je naar een wedstrijd kijkt en je oude denken even terugkomt. Niet om haar te belasten. Om eerlijk te zijn over een proces.</p>
<p>Een verslaving overleven is publiek werk, niet prive.</p>
<p><strong>Patroon twee: alle eigen pijn opzij zetten.</strong></p>
<p>Je denkt: ik mag nu niets voelen, want ik heb haar pijn gedaan. Klopt deels. Klopt niet helemaal.</p>
<p>Je hebt zelf ook hulp nodig. Verslaving kwam ergens vandaan. Stress, eenzaamheid, een leeg gevoel, oude trauma's, gewoon hoe je hersenen werken, het kan allemaal meespelen. Dat onderzoeken is jouw werk, niet hare. Maar je moet het wel doen.</p>
<p>Hulp zoeken is geen egoisme. Hulp zoeken is wat haar uiteindelijk laat zien dat dit echt is.</p>
<p><strong>Patroon drie: terug naar normaal te snel.</strong></p>
<p>Na drie weken denk je: het gaat weer goed. We hebben weer gelachen. Misschien is het ergste voorbij.</p>
<p>Het is niet voorbij. Drie weken is een rustpauze. Het werk komt nog. Maand twee, maand drie, maand zes. Dan komen de echte gesprekken. Over geld. Over toekomst. Over wat dit met haar heeft gedaan, en met wie ze nu is.</p>
<p>Wees niet verrast als zij nog vele maanden later in een keuken in tranen uitbarst over iets wat al lang besproken was. Het is geen ruzie zoeken. Het is verwerking die op haar tempo komt, niet op het jouwe.</p>
<h2>Wat als ze je verlaat</h2>
<p>Misschien is dit waar je nu het bangst voor bent.</p>
<p>Ik heb mensen gekend wiens relatie het niet hield. Hier is wat ik weet:</p>
<p>Een relatie verliezen door eerlijkheid is pijnlijk. Een relatie verliezen door doorgaan met liegen is pijnlijker, voor jullie allebei en vooral voor haar.</p>
<p>Als ze nu zegt dat ze weg wil, betekent dat niet dat het definitief is. Het betekent dat ze ruimte nodig heeft. Ruimte geven is wat je doet. Niet smeken. Niet onder druk zetten. Niet beloften stapelen.</p>
<p>Zeggen: "Ik begrijp het. Ik ga aan mezelf werken. Als je tijd nodig hebt, neem die. Ik zal er niet voor op de loop gaan, maar ik zal je ook niet onder druk zetten."</p>
<p>Soms komen mensen terug. Soms niet. Wat je in beide gevallen wint is jezelf, als je het werk doet.</p>
<p>Een relatie redden is geen reden om te stoppen met gokken. Een relatie kan ook niet je enige reden zijn. Want als zij weggaat, valt je reden weg en gaat je verslaving terug.</p>
<p>Stop voor jezelf. Dan is wat er met de relatie gebeurt een gevolg, geen voorwaarde.</p>
<p>Lees ook: <a href="/nl/blog/gokken-aan-je-familie-vertellen">Gokken aan je familie of partner vertellen</a>.</p>
<h2>Een laatste ding</h2>
<p>Je hebt vannacht het zwaarste gesprek van je leven gehad. Of je gaat het zo hebben.</p>
<p>Daarna is er een keuze.</p>
<p>Optie een: je hoopt dat dit overwaait. Je belooft het beste. Je doet de minimaal nodige dingen. Je probeert door te gaan zonder echt te veranderen. Dit eindigt slecht. Voor haar, voor jou, voor de kinderen als die er zijn.</p>
<p>Optie twee: je doet wat dit van je vraagt. Uitsluiting, hulp, openheid, lange volhardende verandering. Het is harder dan optie een. Het is ook de enige optie waarin er aan het eind van het verhaal nog iets goeds staat.</p>
<p>Niemand kan deze keuze voor je maken.</p>
<p>Maar je hebt vannacht al iets gedaan wat niet iedereen kan. Je hebt eerlijk geluisterd in plaats van weer te liegen. Dat is iets.</p>
<p>Doe nu de volgende stap. Sluit je uit. Verwijder de apps. Bel maandag je bank. Maak een afspraak voor hulp. Schrijf op wat er gebeurd is en lees het over zes maanden terug.</p>
<p>Stap voor stap. Niet morgen al perfect. Wel morgen anders dan gisteren.</p>"""

related = '<a href="/nl/blog/gokken-aan-je-familie-vertellen" class="rel-card"><div class="t">Relatie</div><h4>Gokken aan je familie vertellen</h4></a><a href="/nl/blog/gokverslaving-en-identiteit" class="rel-card"><div class="t">Identiteit</div><h4>Gokverslaving en wie je bent</h4></a><a href="/nl/blog/stoppen-met-gokken" class="rel-card"><div class="t">Herstel</div><h4>Stoppen met gokken: een eerlijke gids</h4></a><a href="/nl/blog/zelfuitsluiting-gokken-werkt-het" class="rel-card"><div class="t">Tools</div><h4>Werkt zelfuitsluiting bij gokken</h4></a>'

html = f'<!DOCTYPE html>\n<html lang="nl">\n<head>\n<meta charset="UTF-8"/>\n<link rel="icon" type="image/svg+xml" href="/favicon.svg">\n<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">\n<meta name="viewport" content="width=device-width,initial-scale=1.0"/>\n<title>{title} | Afterbetting</title>\n<meta name="description" content="{desc}"/>\n<meta name="robots" content="index,follow"/>\n<link rel="canonical" href="{url}"/>\n<link rel="alternate" hreflang="nl" href="{url}"/>\n<link rel="alternate" hreflang="x-default" href="{url}"/>\n<meta property="og:type" content="article"/>\n<meta property="og:locale" content="nl_NL"/>\n<meta property="og:locale:alternate" content="nl_BE"/>\n<meta property="og:url" content="{url}"/>\n<meta property="og:title" content="{title} | Afterbetting"/>\n<meta property="og:description" content="{desc}"/>\n<meta property="og:image" content="https://afterbetting.com/og-image.png"/>\n<meta name="twitter:card" content="summary_large_image"/>\n<meta name="twitter:title" content="{title} | Afterbetting"/>\n<meta name="twitter:description" content="{desc}"/>\n<meta name="twitter:image" content="https://afterbetting.com/og-image.png"/>\n<script type="application/ld+json">{sa}</script>\n<script type="application/ld+json">{sb}</script>\n{GA}\n<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n{FONTS}\n<style>{CSS}</style>\n</head>\n<body>\n{NAV}\n{hero}\n<article class="body">\n{body}\n<div class="cta-block"><h3>Eerlijkheid is het begin. Structuur is wat het draagt.</h3><p>Afterbetting helpt je dag voor dag het verschil te maken. Streak tracker, journal, financiele tools, crisis-knop.</p><a href="https://app.afterbetting.com/onboarding">Begin gratis</a></div>\n</article>\n<section class="related"><div class="rel-inner"><h3>Meer lezen</h3><div class="rel-grid">{related}</div></div></section>\n{CRISIS}\n{FOOTER}\n</body></html>'

with open(f"nl/blog/{slug}.html","w") as f:
    f.write(html)
print(f"Done: nl/blog/{slug}.html ({len(html)} bytes)")
