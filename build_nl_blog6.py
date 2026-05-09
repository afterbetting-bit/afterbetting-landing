import json
CSS = open("nl/blog/stoppen-met-gokken.html").read().split("<style>")[1].split("</style>")[0]
GA = '<script async src="https://www.googletagmanager.com/gtag/js?id=G-BC3QG79LQ0"></script><script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag("js",new Date());gtag("config","G-BC3QG79LQ0");</script>'
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,wght@0,300;0,400;1,300&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">'
NAV = '<nav><a href="/nl/" class="logo">after<span>betting</span></a><div class="nav-links"><a href="/nl/#how">Hoe het werkt</a><a href="/nl/#features">Functies</a><a href="/nl/#pricing">Prijzen</a><a href="/nl/blog">Blog</a><a href="https://app.afterbetting.com/login">Inloggen</a></div><a href="https://app.afterbetting.com/onboarding" class="btn">Begin gratis</a></nav>'
CRISIS = '<div class="crisis-footer"><p>Zit je nu in crisis? Bel de <strong>Nationale Hulplijn Gokken: 0800-1995</strong>. Gratis. Anoniem. 24 uur per dag.</p></div>'
FOOTER = '<footer><p>&copy; 2026 Afterbetting &middot; <a href="/nl/">Home</a> <a href="/nl/blog">Blog</a> <a href="/nl/about">Over ons</a> <a href="https://app.afterbetting.com/privacy">Privacy</a> <a href="https://app.afterbetting.com/terms">Voorwaarden</a> <a href="mailto:info@afterbetting.com">Contact</a></p><p style="margin-top:.5rem">Geen medische dienst. Neem contact op met een erkend professional voor klinische ondersteuning.</p></footer>'

slug = "salaris-vergokt-wat-nu"
url = f"https://afterbetting.com/nl/blog/{slug}"
title = "Salaris vergokt wat nu. Concrete stappen voor de eerste 24 uur"
desc = "Salaris vergokt en geen idee wat te doen? Eerst ademhalen. Dan dit lezen. Geen oordeel. Wel concrete stappen voor de komende 24 uur."

sa = json.dumps({"@context":"https://schema.org","@type":"Article","headline":"Net je salaris vergokt. Wat nu.","author":{"@type":"Organization","name":"Afterbetting"},"publisher":{"@type":"Organization","name":"Afterbetting","url":"https://afterbetting.com"},"datePublished":"2026-05-09","dateModified":"2026-05-09","inLanguage":"nl","url":url})
sb = json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://afterbetting.com/nl/"},{"@type":"ListItem","position":2,"name":"Blog","item":"https://afterbetting.com/nl/blog"},{"@type":"ListItem","position":3,"name":"Salaris vergokt wat nu","item":url}]})

hero = '<section class="hero"><div class="hero-inner"><div class="bc"><a href="/nl/">Home</a> &rarr; <a href="/nl/blog">Blog</a> &rarr; Crisis</div><div class="tag">Crisis</div><h1>Net je salaris vergokt. Wat nu.</h1><p style="font-size:1.1rem;color:var(--mid);font-weight:300;line-height:1.7;margin-top:1rem">Je salaris is weg. Of een groot deel ervan. En je zit nu te lezen omdat je niet weet wat je moet doen. Lees verder. Eerst dit. Dan een plan.</p><div class="meta">Door Afterbetting &middot; 9 mei 2026 &middot; 8 min lezen</div></div></section>'

body = """<p>Je staat waarschijnlijk in een keuken. Of op een wc. Of in de auto. Ergens waar niemand je kan zien.</p>
<p>En je zit te trillen.</p>
<p>Ik weet hoe het voelt. Ik heb het meerdere keren meegemaakt. Een keer was het mijn hele salaris in een avond. Een andere keer was het de huur. Een keer het geld dat ik apart had gezet voor de tandarts.</p>
<p>Het voelt alsof je net een misdrijf hebt gepleegd. Tegen jezelf.</p>
<p>Lees nu door. We gaan dit stap voor stap doen.</p>
<h2>Eerst: adem.</h2>
<p>Niet eerst je app openen om te kijken wat er nog over is. Niet eerst rekenen. Niet eerst je partner bellen.</p>
<p>Eerst tien keer diep ademhalen.</p>
<p>Vier seconden in. Zeven seconden vasthouden. Acht seconden uit.</p>
<p>Tien keer.</p>
<p>Doe het nu. Voor je verder leest.</p>
<p>Klaar?</p>
<p>Goed. Je hersenen staan in paniekmodus. In paniek neem je slechte beslissingen. De slechtste beslissing nu is om te proberen het terug te winnen. Daar komen we zo op.</p>
<h2>Wat je nu absoluut niet doet</h2>
<p>Drie dingen niet. Hoe sterk de drang ook is.</p>
<p><strong>Een: je gokt niet om het terug te winnen.</strong></p>
<p>Je hersenen zeggen nu: nog een keer. Net een gok. Als ik die win, is het probleem opgelost. Iedereen weet hoe dat eindigt. Jij ook. Je weet het. Je hebt het al eens geprobeerd. Het werkt niet. Het werkt nooit.</p>
<p>De gedachte komt op. Je hoeft hem niet te volgen.</p>
<p><strong>Twee: je leent geen geld.</strong></p>
<p>Niet van je creditcard. Niet via een lening. Niet via mini-leningen, niet bij een vriend, niet bij familie. Geen geld bij elkaar krabben om te proberen iets recht te trekken voor het einde van de maand.</p>
<p>Geld lenen om te chasen of om te verbergen wat er gebeurd is, is het tweede pad naar grote schulden. Het eerste was gokken zelf. Doe het niet.</p>
<p><strong>Drie: je doet niets onomkeerbaars.</strong></p>
<p>Geen brief naar je werkgever met ontslag. Geen huur opzeggen. Geen auto verkopen vanavond. Geen huwelijk opzeggen.</p>
<p>Wat je nu voelt, is paniek. Paniek vraagt om actie. Grote actie. Maar grote acties uit paniek zijn bijna altijd fout.</p>
<p>Je hebt 24 uur. Niets gaat in die 24 uur instorten. Het ergste is al gebeurd.</p>
<h2>De volgende vier uur</h2>
<p>Hier is wat je wel doet.</p>
<p><strong>Sluit jezelf vandaag nog uit.</strong></p>
<p>Cruks. cruks.nl. Tien minuten op je telefoon. Je staat dan op de zwarte lijst van alle Nederlandse legale online casino's en speelhallen.</p>
<p>Niet morgen. Niet als je nuchter bent. Nu.</p>
<p>Als je het vanavond niet doet, doe je het nooit. Dat weet je.</p>
<p><strong>Verwijder elke gok-app.</strong></p>
<p>Stuk voor stuk. Toto, Bet365, Unibet, Betcity, Holland Casino Online, alles. Apps weg. Bookmark-pagina's uit je browser. E-mails van bookmakers naar prullenbak. Uitschrijven uit nieuwsbrieven.</p>
<p>Verwijder ook de browser-versies. Niet alleen de apps.</p>
<p><strong>Bel maandagochtend je bank.</strong></p>
<p>Vraag om een gokblokkade op je rekening en creditcard. ABN, ING, Rabobank, SNS, Bunq. Allemaal kunnen ze het. Als ze zeggen van niet, vraag de manager. Het bestaat. Het werkt.</p>
<p>Tot maandag: leg je pinpas in een lade. Geef hem aan iemand anders. Geef hem aan je partner. Doe iets waardoor je er vannacht niet aan kunt.</p>
<p><strong>Schrijf op wat er gebeurd is.</strong></p>
<p>Niet voor anderen. Voor jezelf. Pen en papier. Geen telefoon.</p>
<p>Wat heb je vergokt. Hoeveel. Hoe lang duurde het. Wat dacht je tijdens. Wat dacht je erna. Wat voel je nu.</p>
<p>Ga niet uitleggen. Ga niet rechtvaardigen. Schrijf gewoon op wat er is gebeurd.</p>
<p>Stop het ergens waar je het over zes maanden terugvindt. Je gaat het nodig hebben.</p>
<h2>Het geldprobleem</h2>
<p>Nu het concrete.</p>
<p>Je salaris is weg. De huur moet betaald. De boodschappen moeten gekocht. Misschien moet er nog een rekening betaald.</p>
<p>Wat doe je.</p>
<p><strong>Stap een: rekenen.</strong></p>
<p>Pak een vel papier. Schrijf op:</p>
<ul><li>Wat staat er nog op je rekening</li><li>Wat moet er deze maand sowieso betaald (huur, hypotheek, energie, ziektekosten, eten, vervoer)</li><li>Wat kan wachten een maand (kleding, uitjes, abonnementen, niet-essentiele spullen)</li></ul>
<p>Dan zie je waar je staat. Echt staat. Niet wat je denkt.</p>
<p><strong>Stap twee: prioriteren.</strong></p>
<p>Eten en huur zijn belangrijker dan een telefoonrekening. Een telefoonrekening is belangrijker dan Netflix. Netflix is belangrijker dan dat ene abonnement waar je niets meer mee doet.</p>
<p>Zet alles op een rij. Van moet naar kan-wachten.</p>
<p><strong>Stap drie: communiceren.</strong></p>
<p>Als je huur niet kunt betalen, bel de verhuurder. Eerlijk. Niet morgen, deze week. Vraag of je een week of twee uitstel kunt krijgen. De meeste verhuurders zijn coulant als je belt voordat je niet betaalt.</p>
<p>Hetzelfde voor energie, voor incassobureaus, voor wat dan ook. Bellen voordat het mis gaat is altijd beter dan negeren tot het wel mis gaat.</p>
<p>Schaam je niet. Niet over de telefoon. Je hoeft niet te zeggen waarom. Je kunt zeggen dat je een onverwachte uitgave had en dat je een betalingsregeling vraagt.</p>
<p><strong>Stap vier: hulp.</strong></p>
<p>Als de gaten te groot zijn, ga naar de gemeente. Vraag om schuldhulpverlening. Of bel de Nationale Schuldenlijn op 0800-8115. Gratis.</p>
<p>Schaam je niet. Schuldhulp bestaat voor mensen zoals jij. Letterlijk daarom is het opgericht.</p>
<p>Lees ook: <a href="/nl/blog/gokschuld-aflossen">Gokschuld aflossen, een eerlijk plan zonder valse beloftes</a>.</p>
<h2>Wat je tegen anderen zegt</h2>
<p>Eerlijk: dit is het moeilijkste deel.</p>
<p>Je gaat eraan denken om te liegen. Tegen je partner. Tegen je ouders. Tegen iedereen.</p>
<p>Begrijpelijk. Maar liegen lost niets op. Liegen verlengt het probleem en maakt de bom groter als hij over een maand of een jaar alsnog ontploft.</p>
<p><strong>Tegen je partner.</strong></p>
<p>Vertel het zo snel mogelijk. Niet vandaag in paniek. Wel deze week. Liever vandaag of morgen, als je er rustig genoeg voor bent.</p>
<p>Hou het kort. Hou het feitelijk.</p>
<p>"Ik moet je iets vertellen wat moeilijk is. Ik heb een gokprobleem. Vandaag heb ik een groot deel van mijn salaris vergokt. Het spijt me. Ik wil hier hulp voor zoeken."</p>
<p>Geen excuses. Geen "het komt door...". Geen "ik beloof dat...". Gewoon de feiten.</p>
<p>Wat er daarna komt is wat het is. Boosheid. Verdriet. Stilte. Allemaal goed. Geen van dat is erger dan blijven liegen.</p>
<p>Lees ook: <a href="/nl/blog/gokken-aan-je-familie-vertellen">Gokken aan je familie of partner vertellen, hoe doe je dat</a>.</p>
<p><strong>Tegen werk.</strong></p>
<p>Je hoeft niet te vertellen dat je gegokt hebt. Wel dat je deze maand een financieel probleem hebt. Vraag of er een voorschot mogelijk is. Veel werkgevers doen dat zonder vragen.</p>
<p><strong>Tegen vrienden of familie.</strong></p>
<p>Hangt van de relatie af. Een persoon die je vertrouwt is genoeg. Iemand bij wie je kunt zeggen wat er gebeurd is zonder dat je daarvoor wordt veroordeeld.</p>
<p>Een persoon. Vandaag of morgen. Niet alleen blijven met dit.</p>
<h2>Wat je morgen doet</h2>
<p>Je hebt vandaag overleefd. Je hebt jezelf uitgesloten. Je hebt apps verwijderd. Je hebt opgeschreven wat er gebeurd is. Misschien heb je iemand verteld.</p>
<p>Morgen.</p>
<p>Sta op tijd op. Eet ontbijt, ook als je geen honger hebt. Loop een uur. Buiten. Zonder telefoon.</p>
<p>Je hebt een fysiek systeem dat in de stress zit. Beweging is medicijn. Geen metafoor. Letterlijk medicijn. Je adrenaline en cortisol moeten ergens heen.</p>
<p>Daarna: bel de Nationale Hulplijn Gokken. <strong>0800-1995</strong>. Gratis. Anoniem. Je hoeft niet eens je naam te zeggen. Je belt om te praten met iemand die elke dag mensen aan de lijn heeft die dit hebben meegemaakt.</p>
<p>Als bellen te veel is, chat dan via gokken.hulponline.nl.</p>
<p>Een gesprek. Tien minuten. Dat is genoeg om de eerste week door te komen.</p>
<h2>Over een maand</h2>
<p>Hier is iets wat je nu niet gelooft, maar wat waar is.</p>
<p>Wat er vandaag gebeurd is, kan het beste zijn wat je dit jaar overkomt.</p>
<p>Niet omdat het oke is. Het is niet oke.</p>
<p>Maar omdat dit het moment kan zijn waarop je ophoudt jezelf voor te liegen.</p>
<p>Je gokt niet recreatief. Je hebt geen "ongelukkige avond" gehad. Je hebt een verslaving. En verslavingen lossen niet op door wilskracht of door beloftes aan jezelf.</p>
<p>Ze lossen op door structuur. Door uitsluiting. Door geld weg te halen van waar het gevaar is. Door iemand erbij te halen. Door een leven op te bouwen waarin gokken geen plek meer heeft.</p>
<p>Dat is werk van maanden. Niet van vandaag.</p>
<p>Maar het werk begint vandaag.</p>
<p>Lees ook: <a href="/nl/blog/terugval-na-gokverslaving">Wat moet je doen na een gokterugval</a> en <a href="/nl/blog/zelfuitsluiting-gokken-werkt-het">Werkt zelfuitsluiting bij gokken</a>.</p>
<h2>Een laatste ding</h2>
<p>Je bent geen slecht mens.</p>
<p>Je bent geen mislukking.</p>
<p>Je hebt iets verschrikkelijks gedaan, dat klopt. Tegen jezelf. Tegen mensen die van je houden.</p>
<p>Maar het ding wat je nu het hardst nodig hebt is niet meer schaamte. Schaamte heb je genoeg gehad. Schaamte heeft je hier gebracht.</p>
<p>Wat je nodig hebt is iemand die zegt: dit is een ziekte, niet jouw karakter. Hij is te behandelen. Niet morgen klaar. Wel te behandelen.</p>
<p>Sluit je vanavond uit. Verwijder die apps. Schrijf op wat er gebeurd is. Vertel iemand. Bel maandag je bank.</p>
<p>Stap voor stap. Een tegelijk.</p>
<p>Je gaat dit overleven. Andere mensen hebben dit overleefd. Je bent niet de eerste. Je bent niet de laatste.</p>
<p>Maar deze keer doe je het anders.</p>"""

related = '<a href="/nl/blog/terugval-na-gokverslaving" class="rel-card"><div class="t">Terugval</div><h4>Wat moet je doen na een gokterugval</h4></a><a href="/nl/blog/gokschuld-aflossen" class="rel-card"><div class="t">Schulden</div><h4>Gokschuld aflossen, een eerlijk plan</h4></a><a href="/nl/blog/zelfuitsluiting-gokken-werkt-het" class="rel-card"><div class="t">Tools</div><h4>Werkt zelfuitsluiting bij gokken</h4></a><a href="/nl/blog/stoppen-met-gokken" class="rel-card"><div class="t">Herstel</div><h4>Stoppen met gokken: een eerlijke gids</h4></a>'

html = f'<!DOCTYPE html>\n<html lang="nl">\n<head>\n<meta charset="UTF-8"/>\n<link rel="icon" type="image/svg+xml" href="/favicon.svg">\n<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">\n<meta name="viewport" content="width=device-width,initial-scale=1.0"/>\n<title>{title} | Afterbetting</title>\n<meta name="description" content="{desc}"/>\n<meta name="robots" content="index,follow"/>\n<link rel="canonical" href="{url}"/>\n<link rel="alternate" hreflang="nl" href="{url}"/>\n<link rel="alternate" hreflang="x-default" href="{url}"/>\n<meta property="og:type" content="article"/>\n<meta property="og:locale" content="nl_NL"/>\n<meta property="og:locale:alternate" content="nl_BE"/>\n<meta property="og:url" content="{url}"/>\n<meta property="og:title" content="{title} | Afterbetting"/>\n<meta property="og:description" content="{desc}"/>\n<meta property="og:image" content="https://afterbetting.com/og-image.png"/>\n<meta name="twitter:card" content="summary_large_image"/>\n<meta name="twitter:title" content="{title} | Afterbetting"/>\n<meta name="twitter:description" content="{desc}"/>\n<meta name="twitter:image" content="https://afterbetting.com/og-image.png"/>\n<script type="application/ld+json">{sa}</script>\n<script type="application/ld+json">{sb}</script>\n{GA}\n<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n{FONTS}\n<style>{CSS}</style>\n</head>\n<body>\n{NAV}\n{hero}\n<article class="body">\n{body}\n<div class="cta-block"><h3>Je hoeft dit niet alleen te doen.</h3><p>Afterbetting helpt je dag voor dag uit het patroon te breken. Streak tracker, journal, financiele tools, crisis-knop.</p><a href="https://app.afterbetting.com/onboarding">Begin gratis</a></div>\n</article>\n<section class="related"><div class="rel-inner"><h3>Meer lezen</h3><div class="rel-grid">{related}</div></div></section>\n{CRISIS}\n{FOOTER}\n</body></html>'

with open(f"nl/blog/{slug}.html","w") as f:
    f.write(html)
print(f"Done: nl/blog/{slug}.html ({len(html)} bytes)")
