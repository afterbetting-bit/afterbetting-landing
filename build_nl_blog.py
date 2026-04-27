import os

os.makedirs("nl/blog", exist_ok=True)

CSS = """*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}:root{--clay:#C4785A;--clay-light:#E8C4B2;--clay-bg:#FBF3EE;--dark:#2C2420;--mid:#5C4A42;--muted:#9E8E86;--cream:#FFFCFA;--warm:#F7F0EA;--border:#E8DDD6;--green:#7A9E8E;--green-bg:#EEF5F2;--green-border:#C2D8D0}html{scroll-behavior:smooth}body{font-family:"DM Sans",sans-serif;background:var(--cream);color:var(--dark);line-height:1.6;-webkit-font-smoothing:antialiased}nav{position:sticky;top:0;z-index:100;background:#fff;border-bottom:1px solid var(--border);padding:1.25rem 2rem;display:flex;align-items:center;justify-content:space-between}.logo{font-family:"Fraunces",serif;font-size:1.4rem;font-weight:300;color:var(--dark);text-decoration:none}.logo span{color:var(--clay)}.nav-links{display:flex;gap:1.5rem;align-items:center}.nav-links a{font-size:.875rem;color:var(--mid);text-decoration:none}.btn{background:var(--clay);color:#fff;padding:.6rem 1.4rem;border-radius:100px;font-size:.875rem;font-weight:500;text-decoration:none;font-family:"DM Sans",sans-serif;display:inline-block}.hero{background:var(--warm);border-bottom:1px solid var(--border);padding:4rem 2rem}.hero-inner{max-width:760px;margin:0 auto}.bc{font-size:.78rem;color:var(--muted);margin-bottom:1.5rem}.bc a{color:var(--clay);text-decoration:none}.tag{display:inline-block;background:var(--green-bg);color:var(--green);font-size:.75rem;font-weight:500;padding:.25rem .75rem;border-radius:100px;border:1px solid var(--green-border);margin-bottom:1rem}h1{font-family:"Fraunces",serif;font-size:2.8rem;line-height:1.15;font-weight:300;color:var(--dark);margin-bottom:1rem;letter-spacing:-.02em}.meta{font-size:.82rem;color:var(--muted);margin-top:1rem}.body{max-width:760px;margin:0 auto;padding:3rem 2rem}.body h2{font-family:"Fraunces",serif;font-size:1.7rem;font-weight:300;color:var(--dark);margin:2.5rem 0 1rem;line-height:1.2}.body p{font-size:1rem;color:var(--mid);line-height:1.8;margin-bottom:1.25rem;font-weight:300}.body ul,.body ol{margin:1rem 0 1.5rem 1.5rem}.body li{font-size:1rem;color:var(--mid);line-height:1.8;margin-bottom:.5rem;font-weight:300}.body strong{color:var(--dark);font-weight:500}.body a{color:var(--clay);text-decoration:underline;text-underline-offset:3px}.callout{background:var(--clay-bg);border:1px solid var(--clay-light);border-radius:14px;padding:1.5rem;margin:2rem 0}.callout p{margin:0;color:var(--mid)}.cta-block{background:var(--dark);border-radius:16px;padding:2.5rem;margin:3rem 0;text-align:center}.cta-block h3{font-family:"Fraunces",serif;font-size:1.5rem;font-weight:300;color:#fff;margin-bottom:.5rem}.cta-block p{color:rgba(255,255,255,.6);font-size:.9rem;margin-bottom:1.5rem}.cta-block a{background:var(--clay);color:#fff;padding:.75rem 2rem;border-radius:100px;text-decoration:none;font-weight:500;font-size:.9rem;display:inline-block}.related{background:var(--warm);border-top:1px solid var(--border);padding:3rem 2rem}.rel-inner{max-width:760px;margin:0 auto}.related h3{font-family:"Fraunces",serif;font-size:1.3rem;font-weight:300;color:var(--dark);margin-bottom:1.5rem}.rel-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:1rem}.rel-card{background:#fff;border:1px solid var(--border);border-radius:12px;padding:1.25rem;text-decoration:none;display:block}.rel-card:hover{border-color:var(--clay)}.rel-card .t{font-size:.72rem;color:var(--green);font-weight:500;text-transform:uppercase;letter-spacing:.06em;margin-bottom:.5rem}.rel-card h4{font-family:"Fraunces",serif;font-size:1rem;font-weight:400;color:var(--dark);line-height:1.3}.crisis-footer{background:var(--clay-bg);border-top:1px solid var(--clay-light);padding:1.25rem 2rem;text-align:center}.crisis-footer p{font-size:.88rem;color:var(--dark);font-weight:400}.crisis-footer strong{color:var(--clay)}footer{background:var(--dark);color:#fff;padding:2rem;text-align:center}footer p{font-size:.8rem;color:rgba(255,255,255,.3)}footer a{color:var(--clay);text-decoration:none;margin:0 .5rem}@media(max-width:768px){nav .nav-links{display:none}h1{font-size:2rem}.hero{padding:2.5rem 1.25rem}.body{padding:2rem 1.25rem}.rel-grid{grid-template-columns:1fr}}"""

GA = '<script async src="https://www.googletagmanager.com/gtag/js?id=G-BC3QG79LQ0"></script><script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag("js",new Date());gtag("config","G-BC3QG79LQ0");</script>'

FONTS = '<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,wght@0,300;0,400;1,300&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">'

NAV = '''<nav><a href="/nl/" class="logo">after<span>betting</span></a><div class="nav-links"><a href="/nl/#how">Hoe het werkt</a><a href="/nl/#features">Functies</a><a href="/nl/#pricing">Prijzen</a><a href="/nl/blog">Blog</a><a href="https://app.afterbetting.com/login">Inloggen</a></div><a href="https://app.afterbetting.com/onboarding" class="btn">Begin gratis</a></nav>'''

CRISIS = '<div class="crisis-footer"><p>Zit je nu in crisis? Bel de <strong>Nationale Hulplijn Gokken: 0800-1995</strong>. Gratis. Anoniem. 24 uur per dag.</p></div>'

FOOTER = '<footer><p>&copy; 2026 Afterbetting &middot; <a href="/nl/">Home</a> <a href="/nl/blog">Blog</a> <a href="/nl/about">Over ons</a> <a href="https://app.afterbetting.com/privacy">Privacy</a> <a href="https://app.afterbetting.com/terms">Voorwaarden</a> <a href="mailto:info@afterbetting.com">Contact</a></p><p style="margin-top:.5rem">Geen medische dienst. Neem contact op met een erkend professional voor klinische ondersteuning.</p></footer>'

def page(lang, title, desc, canonical, hreflangs, schema_json, hero, body, related_html, cta_title, cta_desc):
    hl = "\n".join(f'<link rel="alternate" hreflang="{l}" href="{u}"/>' for l,u in hreflangs)
    schemas = "\n".join(f'<script type="application/ld+json">{s}</script>' for s in schema_json)
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8"/>
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title>{title}</title>
<meta name="description" content="{desc}"/>
<meta name="robots" content="index,follow"/>
<link rel="canonical" href="{canonical}"/>
{hl}
<meta property="og:type" content="article"/>
<meta property="og:locale" content="nl_NL"/>
<meta property="og:url" content="{canonical}"/>
<meta property="og:title" content="{title}"/>
<meta property="og:description" content="{desc}"/>
<meta property="og:image" content="https://afterbetting.com/og-image.png"/>
{schemas}
{GA}
{FONTS}
<style>{CSS}</style>
</head>
<body>
{NAV}
{hero}
<article class="body">
{body}
<div class="cta-block"><h3>{cta_title}</h3><p>{cta_desc}</p><a href="https://app.afterbetting.com/onboarding">Begin gratis</a></div>
</article>
<section class="related"><div class="rel-inner"><h3>Meer lezen</h3><div class="rel-grid">{related_html}</div></div></section>
{CRISIS}
{FOOTER}
</body></html>"""

def rel(href, tag, title):
    return f'<a href="{href}" class="rel-card"><div class="t">{tag}</div><h4>{title}</h4></a>'

import json

# ── ARTIKEL 1: stoppen-met-gokken ────────────────────────────────────────────

slug1 = "stoppen-met-gokken"
url1  = f"https://afterbetting.com/nl/blog/{slug1}"

schema1_article = json.dumps({"@context":"https://schema.org","@type":"Article","headline":"Stoppen met gokken: een eerlijke gids voor wie het echt meent","author":{"@type":"Organization","name":"Afterbetting"},"publisher":{"@type":"Organization","name":"Afterbetting","url":"https://afterbetting.com"},"datePublished":"2026-04-26","dateModified":"2026-04-26","inLanguage":"nl","url":url1})
schema1_bc = json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://afterbetting.com/nl/"},{"@type":"ListItem","position":2,"name":"Blog","item":"https://afterbetting.com/nl/blog"},{"@type":"ListItem","position":3,"name":"Stoppen met gokken: een eerlijke gids","item":url1}]})

hero1 = f'''<section class="hero"><div class="hero-inner">
<div class="bc"><a href="/nl/">Home</a> &rarr; <a href="/nl/blog">Blog</a> &rarr; Herstel</div>
<div class="tag">Herstel</div>
<h1>Stoppen met gokken. Een eerlijke gids voor wie het echt meent.</h1>
<p style="font-size:1.1rem;color:var(--mid);font-weight:300;line-height:1.7;margin-top:1rem">Stoppen met gokken is geen kwestie van wilskracht. Hier is wat wel werkt. Eerlijk. Zonder omwegen.</p>
<div class="meta">Door Afterbetting &middot; 26 april 2026 &middot; 8 min lezen</div>
</div></section>'''

body1 = """<p>Je hebt het al honderd keer gedacht. Misschien wel duizend.</p>
<p>"Vanaf morgen stop ik."</p>
<p>En dan komt morgen. En komt er weer een ronde. En weer een leugen tegen je partner. En weer een belofte aan jezelf.</p>
<p>Stoppen met gokken is geen kwestie van wilskracht. Als wilskracht genoeg was, was je allang gestopt. Dat ben je niet. Dus laten we eens stoppen met dat sprookje.</p>
<p>Dit artikel gaat over wat wel werkt. Eerlijk. Zonder marketingpraat. Zonder tien tips die je leven veranderen. Wel met de tools die het verschil maken voor mensen die echt willen stoppen.</p>

<h2>Waarom stoppen met gokken zo lastig is (en het niet aan jou ligt)</h2>
<p>Even iets rechtzetten.</p>
<p>Gokken is geen ondeugd. Geen karakterzwakte. Geen gebrek aan discipline.</p>
<p>Gokken is een gedraging die je hersenen heeft herbedraad. Dat is geen excuus. Wel een feit. Elke keer dat je gokt, krijgt je brein een dopaminepiek. Niet bij het winnen. Bij het wachten op de uitslag. Bij het draaien van de rollen. Bij de seconde voor het doelpunt.</p>
<p>Dat is het systeem dat je verslaaft. Niet de winst. De anticipatie.</p>
<p>Stoppen betekent dus niet "geen geld meer verliezen". Stoppen betekent: je hersenen leren dat ze die kick niet meer krijgen. En dat duurt. Niet één dag. Niet één week. Maanden.</p>
<p>In de tussentijd ga je merken dat je geïrriteerd bent. Slecht slaapt. Gedachten hebt die nergens slaan. Dat is geen falen. Dat is je systeem dat zich herstelt.</p>
<p>Hou dat vol. Het wordt minder.</p>

<h2>Wat werkt wel? Drie dingen.</h2>
<p>Laten we het simpel houden. Dit zijn de drie dingen die het verschil maken voor mensen die stoppen en gestopt blijven.</p>
<p><strong>Eén: maak gokken fysiek onmogelijk.</strong></p>
<p>Geen wilskracht-toetsen. Niet "ik zie wel of ik me kan inhouden". Knip de toegang weg.</p>
<p>Sluit jezelf uit via Cruks (het Centraal Register Uitsluiting Kansspelen). Doe het vandaag, niet morgen. Het kost je tien minuten online en je staat direct op de zwarte lijst van alle Nederlandse online casino's en speelhallen. Geen toegang. Punt.</p>
<p>Daarnaast: betaalblokkades. Je bank kan transacties naar gokwebsites blokkeren. Bel ze. ABN, ING, Rabobank, Bunq, alle grote banken hebben deze optie. Vraag erom. Activeer.</p>
<p>Apps op je telefoon? Verwijder. Nu. Niet straks.</p>
<p><strong>Twee: vervang het uur, niet de gewoonte.</strong></p>
<p>Mensen denken dat ze gokken moeten "afleren". Dat klopt niet. Je moet de tijd opnieuw invullen.</p>
<p>Want wat doe je met die twee, drie, vier uur per dag die je voorheen aan gokken besteedde? Naar het plafond staren? Dat houdt niemand vol.</p>
<p>Vul ze in. Sport. Lopen. Klussen. Lezen. Bellen met iemand. Het maakt niet uit wat. Het maakt uit dat het iets is.</p>
<p><strong>Drie: praat met iemand.</strong></p>
<p>Eén iemand. Dat is genoeg om te beginnen.</p>
<p>Een partner. Een broer. Een goede vriend. Een huisarts. Een hulpverlener bij Jellinek of Tactus. De Nationale Hulplijn Gokken op <strong>0800-1995</strong> (gratis, anoniem, 24/7).</p>
<p>Geheimhouding houdt verslaving in stand. Eén eerlijk gesprek breekt dat open. Je hoeft het niet groots te maken. Eén zin is genoeg: "Ik heb een gokprobleem en ik wil ervan af."</p>
<p>Dat is de moeilijkste zin die je ooit zult zeggen. En de belangrijkste.</p>

<h2>Je eerste 24 uur. Wat doe je?</h2>
<p>Niet alles tegelijk. Dat lukt toch niet.</p>
<p>Begin hiermee:</p>
<p><strong>Uur 0 tot 1.</strong> Sluit jezelf in bij Cruks. cruks.nl. Tien minuten. Klaar.</p>
<p><strong>Uur 1 tot 2.</strong> Bel je bank. Vraag om een gokblokkade op je rekening en creditcard.</p>
<p><strong>Uur 2 tot 3.</strong> Verwijder elke gok-app van je telefoon. Inclusief de bookmaker-pagina's in je browser. Inclusief de e-mails van bookmakers in je inbox. Schoonmaken.</p>
<p><strong>De rest van de dag.</strong> Eet iets fatsoenlijks. Drink water. Ga lopen. Lang. Een uur, twee uur, het maakt niet uit. Beweging vermindert craving.</p>
<p><strong>Voor het slapen.</strong> Schrijf op waarom je dit doet. Niet voor andere mensen. Voor jezelf. Eén pagina. Of drie regels. Eerlijk.</p>
<p>Als de drang komt, en hij komt, dan is dit je verzekering. Dan lees je terug wat je vanavond schreef.</p>
<p>Dit is dag 1. Het is de zwaarste dag in een tijdje. Hou vol.</p>
<p>Lees ook: <a href="/nl/blog/eerste-week-stoppen-met-gokken">Wat te verwachten in je eerste week zonder gokken</a></p>

<h2>De rol van schaamte (en waarom die je zo lang heeft tegengehouden)</h2>
<p>Hier de olifant in de kamer.</p>
<p>Schaamte is wat verslaving voedt. Niet het gokken zelf. De schaamte erover.</p>
<p>Je gokte. Je verloor. Je loog. Je gokte weer om te winnen wat je verloor. Je verloor meer. Je loog meer. Je gokte meer om de leugen recht te trekken.</p>
<p>En tussen die rondes door zat een stemmetje in je hoofd dat zei: "Niemand mag dit weten. Je bent zwak. Je bent stom. Je bent een mislukking."</p>
<p>Dat stemmetje liegt. Hoor je? Liegt.</p>
<p>Je bent niet zwak. Je hebt een verslaving ontwikkeld in een wereld die je elke dag bombardeert met gokreclames, online casino's op je telefoon, en sportgokken vervlochten in elke wedstrijdsamenvatting. Dat is geen zwakte. Dat is statistiek.</p>
<p>Schaamte loslaten doe je niet door positief te denken. Dat doe je door eerlijk te zijn. Tegen één iemand. En te merken dat de wereld niet vergaat.</p>

<h2>Wanneer moet je professionele hulp zoeken?</h2>
<p>Hier zijn de eerlijke vuistregels.</p>
<p>Zoek hulp als:</p>
<ul>
<li>Je al meer dan eens "voor het laatst" hebt gegokt</li>
<li>Je schulden hebt opgebouwd waar je 's nachts wakker van ligt</li>
<li>Je gedachten over zelfbeschadiging of zelfmoord hebt gehad</li>
<li>Je relaties beginnen te breken</li>
<li>Je werk of opleiding eronder lijdt</li>
</ul>
<p>Dat hoeft geen jarenlange therapie te zijn. Eén intake bij Jellinek of Tactus geeft je al richting. Beide hebben gespecialiseerde gokverslaving-programma's. De zorgverzekering vergoedt het meestal volledig.</p>
<p>Geen wachtlijst die je trekt? De Nationale Hulplijn Gokken: <strong>0800-1995</strong>. Gratis. Anoniem. 24 uur per dag. Eén telefoontje en je weet waar je terecht kunt.</p>
<p>Dit is geen falen. Dit is volwassenheid.</p>

<h2>Wat het oplevert (en waarom het de moeite waard is)</h2>
<p>Geen sprookjes. Geen "je leven verandert binnen een week".</p>
<p>Wat wel gebeurt:</p>
<p><strong>Week 1.</strong> Je slaapt slechter. Je bent prikkelbaar. Je voelt een leegte. Dit is normaal. Hou vol.</p>
<p><strong>Week 2 tot 4.</strong> Je merkt dat je rekening niet leeg loopt. Voor het eerst in maanden. Misschien jaren. Dat is een vreemd gevoel. En een goed gevoel.</p>
<p><strong>Maand 2 tot 3.</strong> Je slaap wordt beter. Je hoofd wordt rustiger. De cravings worden minder vaak en minder hevig. Niet weg. Minder.</p>
<p><strong>Maand 6.</strong> Je begint dingen te merken die je was vergeten. Hoe het smaakt om koffie te drinken zonder constant op je telefoon te kijken. Hoe het voelt om naar een wedstrijd te kijken zonder geld erop. Hoe het is om eerlijk te zijn tegen mensen.</p>
<p><strong>Jaar 1.</strong> Je bent iemand anders dan je was. Niet beter dan andere mensen. Beter dan wie je was.</p>
<p>Dat is wat het oplevert.</p>

<h2>Vandaag begint het</h2>
<p>Niet morgen. Vandaag.</p>
<p>Je hoeft het niet perfect te doen. Je hoeft niet meteen te weten hoe het verder gaat. Je hoeft alleen één ding te doen: beginnen.</p>
<p>Cruks aanmelden. Bank bellen. Apps verwijderen. Iemand bellen.</p>
<p>Eén ding. Vandaag. Daarna het volgende.</p>
<p>Dat is het hele plan. Verder hoeft het niet te zijn.</p>"""

related1 = (
    rel("/nl/blog/gokverslaving-herkennen","Bewustwording","Gokverslaving herkennen: 12 signalen die je niet langer kunt negeren") +
    rel("/nl/blog/eerste-week-stoppen-met-gokken","Herstel","Je eerste week stoppen met gokken: dag voor dag") +
    rel("/nl/blog/wat-doet-gokken-met-je-hersenen","Brein","Wat doet gokken met je hersenen?")
)

html1 = page(
    "nl",
    "Stoppen met gokken: een eerlijke gids | Afterbetting",
    "Stoppen met gokken is geen kwestie van wilskracht. Wat echt werkt, waarom je vastzit, hoe je vandaag begint. Geen preek.",
    url1,
    [("nl","https://afterbetting.com/nl/blog/stoppen-met-gokken"),("x-default","https://afterbetting.com/nl/blog/stoppen-met-gokken")],
    [schema1_article, schema1_bc],
    hero1, body1, related1,
    "Klaar om te beginnen?",
    "Streak bijhouden, dagelijkse check-ins, journaal, en een crisisknop voor als het zwaar wordt. Geen wachtlijst. Geen oordeel."
)

with open("nl/blog/stoppen-met-gokken.html","w",encoding="utf-8") as f:
    f.write(html1)
print("OK: stoppen-met-gokken.html")

# ── ARTIKEL 2: gokverslaving-herkennen ───────────────────────────────────────

slug2 = "gokverslaving-herkennen"
url2  = f"https://afterbetting.com/nl/blog/{slug2}"

schema2_article = json.dumps({"@context":"https://schema.org","@type":"Article","headline":"Gokverslaving herkennen: 12 signalen die je niet langer kunt negeren","author":{"@type":"Organization","name":"Afterbetting"},"publisher":{"@type":"Organization","name":"Afterbetting","url":"https://afterbetting.com"},"datePublished":"2026-04-26","dateModified":"2026-04-26","inLanguage":"nl","url":url2})
schema2_bc = json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://afterbetting.com/nl/"},{"@type":"ListItem","position":2,"name":"Blog","item":"https://afterbetting.com/nl/blog"},{"@type":"ListItem","position":3,"name":"Gokverslaving herkennen: 12 signalen","item":url2}]})

hero2 = f'''<section class="hero"><div class="hero-inner">
<div class="bc"><a href="/nl/">Home</a> &rarr; <a href="/nl/blog">Blog</a> &rarr; Bewustwording</div>
<div class="tag">Bewustwording</div>
<h1>Gokverslaving herkennen: 12 signalen die je niet langer kunt negeren.</h1>
<p style="font-size:1.1rem;color:var(--mid);font-weight:300;line-height:1.7;margin-top:1rem">Gokverslaving herkennen begint bij eerlijk kijken. 12 signalen die je serieus moet nemen, ook als het over jezelf gaat.</p>
<div class="meta">Door Afterbetting &middot; 26 april 2026 &middot; 7 min lezen</div>
</div></section>'''

body2 = """<p>Je leest dit artikel om een reden.</p>
<p>Misschien lees je het voor jezelf. Misschien voor je partner. Voor je broer, je zoon, je collega. Misschien lees je het omdat iemand het je heeft gestuurd, en dat doet wat met je.</p>
<p>Wat je reden ook is: je voelt iets niet kloppen.</p>
<p>Gokverslaving herkennen is niet altijd makkelijk. Vooral niet als jij het zelf bent. Want verslaving liegt. Tegen anderen. Maar vooral tegen jezelf.</p>
<p>Dit artikel zet 12 signalen op een rij. Niet om je een diagnose te geven. Wel om je een eerlijke spiegel voor te houden. Lees ze. En wees eerlijk.</p>

<h2>Wat is een gokverslaving eigenlijk?</h2>
<p>Voordat we naar de signalen gaan, even iets duidelijk maken.</p>
<p>Gokverslaving heet officieel "gokstoornis". Het staat in het diagnoseboek voor psychiaters (de DSM-5) als een verslavingsziekte. Geen karakterfout. Geen kwestie van wilskracht. Een ziekte. Zoals alcoholisme een ziekte is.</p>
<p>Dat betekent niet dat je hulpeloos bent. Dat betekent dat het te behandelen is. Net als andere verslavingen.</p>
<p>In Nederland heeft naar schatting 79.000 mensen een gokprobleem, en ruim een half miljoen mensen lopen risico. Met de groei van online gokken en sportgokken stijgt dat aantal jaarlijks. Je bent dus niet de enige. Verre van.</p>

<h2>De 12 signalen</h2>
<p>Hier komen ze. Lees ze rustig.</p>
<p><strong>Signaal 1: Je gokt steeds vaker, of voor steeds hogere bedragen.</strong></p>
<p>Het begon misschien klein. Tien euro op een wedstrijd. Een toeristisch potje roulette. Inmiddels is dat opgeschoven. Niet omdat je het zo besloot. Omdat de oude bedragen geen kick meer geven.</p>
<p><strong>Signaal 2: Je hebt al meerdere keren geprobeerd te stoppen.</strong></p>
<p>En het lukt niet. Niet omdat je niet wil. Omdat iets je terugtrekt zodra de eerste reclame voorbij komt. Of de eerste wedstrijd. Of het eerste vlaagje verveling.</p>
<p><strong>Signaal 3: Je liegt over hoe vaak of hoeveel je gokt.</strong></p>
<p>Tegen je partner. Je ouders. Jezelf. "Het was maar twintig euro." Terwijl het tweehonderd was. Of duizend.</p>
<p><strong>Signaal 4: Je gokt om verloren geld terug te winnen.</strong></p>
<p>Het officiële woord hiervoor is "chasen". Je verloor honderd. Je gokt vijfhonderd om die honderd terug te winnen. Je verliest weer. Nu chase je vijfhonderd. Je weet hoe dit eindigt.</p>
<p><strong>Signaal 5: Gokken neemt steeds meer ruimte in je hoofd.</strong></p>
<p>Je denkt eraan onder de douche. Tijdens vergaderingen. Tijdens het avondeten met je gezin. Je bent fysiek aanwezig en mentaal afwezig.</p>
<p><strong>Signaal 6: Je hebt geld geleend om te gokken.</strong></p>
<p>Of je hebt geld geleend om verliezen af te dekken. Of je hebt geld weggehaald van rekeningen waar het niet voor bedoeld was. Boodschappengeld. Spaargeld. Geld van je partner.</p>
<p><strong>Signaal 7: Je verstopt bewijzen.</strong></p>
<p>Je verwijdert apps voordat je partner thuiskomt. Je leegt browsergeschiedenis. Je opent post in het geheim. Je hebt rekeningen die niemand kent.</p>
<p><strong>Signaal 8: Je voelt je rusteloos of geïrriteerd als je niet kunt gokken.</strong></p>
<p>Een avond zonder gokken voelt niet als een gewone avond. Die voelt als een avond waar iets ontbreekt. Je bent kribbig. Onrustig. Niet aanwezig.</p>
<p><strong>Signaal 9: Je gokt om aan vervelende gevoelens te ontsnappen.</strong></p>
<p>Stress op je werk? Gokken. Ruzie thuis? Gokken. Eenzaamheid? Gokken. Het is geen hobby meer. Het is een uitlaatklep. En een dure.</p>
<p><strong>Signaal 10: Je hebt relaties beschadigd door gokken.</strong></p>
<p>Je partner is teleurgesteld of woedend. Je ouders maken zich zorgen. Je vrienden vermijden bepaalde gesprekken met je. Of je vermijdt hen.</p>
<p><strong>Signaal 11: Je werk of studie lijdt eronder.</strong></p>
<p>Je komt te laat. Je presteert minder. Je belt je ziek omdat je laat hebt zitten gokken. Je denkt aan gokken in plaats van aan deadlines.</p>
<p><strong>Signaal 12: Je hebt gedacht aan dingen die je vroeger nooit zou doen.</strong></p>
<p>Geld lenen van iemand waarvan je weet dat je het niet terugbetaalt. Spullen verkopen die niet van jou zijn. Of donkerder: gedachten over zelfbeschadiging of erger.</p>

<h2>Hoeveel van de 12 zijn raak?</h2>
<p>Drie of meer? Dan is er een probleem dat aandacht nodig heeft. Niet morgen. Nu.</p>
<p>Vijf of meer? Dan zit je vrij stevig in de problemen, en hulp zoeken is geen overdrijven. Dat is gewoon volwassen.</p>
<p>Acht of meer? Dan is de kans groot dat je officieel zou voldoen aan de criteria voor een gokstoornis. Dat is geen oordeel. Dat is informatie waar je iets mee kunt.</p>
<div class="callout"><p><strong>Belangrijk:</strong> het gaat niet om hoeveel je verliest. Iemand kan duizend euro per maand verliezen en geen verslaving hebben. Iemand anders kan vijftig euro per maand verliezen en wel een verslaving hebben. Het gaat om de greep die het op je leven heeft. Op je hoofd.</p></div>

<h2>Wat als je dit herkent? Vier stappen.</h2>
<p>Adem uit. Echt. Doe het even.</p>
<p>Dit is het moment waarop het beter wordt. Niet vanzelf. Maar wel onomkeerbaar, als je nu iets doet.</p>
<p><strong>Stap 1.</strong> Praat met iemand. Eén iemand. Vandaag of morgen. De Nationale Hulplijn Gokken op <strong>0800-1995</strong> is een goede plek als je geen idee hebt waar te beginnen. Anoniem, gratis, 24/7.</p>
<p><strong>Stap 2.</strong> Sluit jezelf uit via Cruks. cruks.nl. Tien minuten. Geen Nederlandse legale gokwebsite kan je dan nog binnenlaten.</p>
<p><strong>Stap 3.</strong> Vraag bij je bank een gokblokkade aan. Bel ze.</p>
<p><strong>Stap 4.</strong> Maak een afspraak bij Jellinek, Tactus of een andere gespecialiseerde verslavingszorg. Of begin met een zelfgeleid platform zoals Afterbetting om je dagelijkse structuur op te bouwen, eventueel naast professionele hulp.</p>
<p>Lees ook: <a href="/nl/blog/stoppen-met-gokken">Stoppen met gokken: een eerlijke gids</a></p>

<h2>Wat als het over iemand anders gaat?</h2>
<p>Misschien lees je dit niet voor jezelf. Misschien herken je je partner, kind, broer, ouder.</p>
<p>Dan zijn de signalen vaak nog moeilijker te zien. Want jij ziet niet alles. Maar je voelt het wel.</p>
<p>Voorzichtige tip: confronteer niet vanuit boosheid. Zelfs als boosheid terecht is. Verslaving en schaamte zijn een vergrendeld koppel. Aanvallen versterkt de schaamte, en daarmee de verslaving.</p>
<p>Wat wel werkt: zorg voor jezelf eerst. Bel de Nationale Hulplijn Gokken voor advies hoe je het gesprek kunt voeren. En weet: je kunt niet stoppen voor iemand anders. Alleen zij zelf kunnen dat. Jij kunt wel kaders stellen, eerlijk zijn over de impact, en de deur openhouden voor het gesprek.</p>

<h2>Het belangrijkste</h2>
<p>Eén ding tot slot.</p>
<p>Erkennen dat er iets aan de hand is, is de moeilijkste stap. En de belangrijkste. Alles wat daarna komt, is gewoon werk doen.</p>
<p>Het werk is doenlijk. De erkenning is moedig.</p>"""

related2 = (
    rel("/nl/blog/stoppen-met-gokken","Herstel","Stoppen met gokken: een eerlijke gids") +
    rel("/nl/blog/eerste-week-stoppen-met-gokken","Herstel","Je eerste week stoppen met gokken: dag voor dag") +
    rel("/nl/blog/wat-doet-gokken-met-je-hersenen","Brein","Wat doet gokken met je hersenen?")
)

html2 = page(
    "nl",
    "Gokverslaving herkennen: 12 duidelijke signalen | Afterbetting",
    "Gokverslaving herkennen begint bij eerlijk kijken. 12 signalen die je serieus moet nemen, ook bij jezelf. Plus wat je kunt doen.",
    url2,
    [("nl","https://afterbetting.com/nl/blog/gokverslaving-herkennen"),("x-default","https://afterbetting.com/nl/blog/gokverslaving-herkennen")],
    [schema2_article, schema2_bc],
    hero2, body2, related2,
    "Herken je jezelf in deze signalen?",
    "Begin gratis bij Afterbetting. Geen oordeel, geen wachtlijst, gewoon de tools om vandaag de eerste stap te zetten."
)

with open("nl/blog/gokverslaving-herkennen.html","w",encoding="utf-8") as f:
    f.write(html2)
print("OK: gokverslaving-herkennen.html")

# ── ARTIKEL 3: eerste-week-stoppen-met-gokken ────────────────────────────────

slug3 = "eerste-week-stoppen-met-gokken"
url3  = f"https://afterbetting.com/nl/blog/{slug3}"
url3_en = "https://afterbetting.com/blog/first-30-days-without-gambling"

schema3_article = json.dumps({"@context":"https://schema.org","@type":"Article","headline":"Je eerste week stoppen met gokken: dag voor dag","author":{"@type":"Organization","name":"Afterbetting"},"publisher":{"@type":"Organization","name":"Afterbetting","url":"https://afterbetting.com"},"datePublished":"2026-04-26","dateModified":"2026-04-26","inLanguage":"nl","url":url3})
schema3_bc = json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://afterbetting.com/nl/"},{"@type":"ListItem","position":2,"name":"Blog","item":"https://afterbetting.com/nl/blog"},{"@type":"ListItem","position":3,"name":"Je eerste week stoppen met gokken","item":url3}]})

hero3 = f'''<section class="hero"><div class="hero-inner">
<div class="bc"><a href="/nl/">Home</a> &rarr; <a href="/nl/blog">Blog</a> &rarr; Herstel</div>
<div class="tag">Herstel</div>
<h1>Je eerste week stoppen met gokken: dag voor dag.</h1>
<p style="font-size:1.1rem;color:var(--mid);font-weight:300;line-height:1.7;margin-top:1rem">De eerste week is de zwaarste. Dag voor dag wat je tegenkomt en hoe je doorzet. Eerlijk, geen sprookjes.</p>
<div class="meta">Door Afterbetting &middot; 26 april 2026 &middot; 7 min lezen</div>
</div></section>'''

body3 = """<p>Je hebt besloten te stoppen.</p>
<p>Dag 1 is voorbij of begint nu. En je vraagt je af: wat staat me te wachten?</p>
<p>Eerlijk antwoord: het wordt zwaar. Niet altijd. Wel vaak. Het wordt ook iets anders waar mensen je niet voor waarschuwen, en dat is: lang. Een dag voelt als drie. Een week voelt als een maand.</p>
<p>Dit artikel loopt door de zeven dagen heen. Wat je tegenkomt. Wat normaal is. Wat te doen.</p>
<p>Geen sprookjes. Wel een gids.</p>

<h2>Dag 1. De beslissing zelf.</h2>
<p>De eerste dag is vreemd. Niet omdat je iets bijzonders voelt. Juist omdat je het tegenovergestelde voelt.</p>
<p>Je hebt besloten te stoppen. Klaar. Je verwacht een soort emotionele explosie. Een grote scène. Maar er gebeurt niks dramatisch. Je staat op. Je doet je werk. Je gaat naar bed. En dat is dag 1.</p>
<p>Dat is precies waar het gevaar zit.</p>
<p>Want zonder fysieke blokkades zit dag 1 vol momenten waarop je hand vanzelf naar je telefoon gaat. Vanuit gewoonte. Niet vanuit verlangen. Gewoonte.</p>
<p>Wat te doen op dag 1: sluit jezelf uit via Cruks (cruks.nl). Bel je bank voor een gokblokkade. Verwijder elke gok-app. Maak het mechanisch onmogelijk. Niet "ik probeer het". Onmogelijk.</p>
<p>Schrijf een korte tekst aan jezelf. Drie regels is genoeg. Waarom je dit doet, voor wie, wat je hoopt over een jaar. Bewaar dat ergens. Je gaat het later teruglezen.</p>

<h2>Dag 2 tot 3. De stilte begint te schreeuwen.</h2>
<p>Hier wordt het voelbaar.</p>
<p>Je merkt nu dat je hoofd onrustig is. Niet alleen even. Continu. Je kunt geen tien minuten zitten zonder iets te willen doen. Je telefoon voelt als een kompas dat constant naar de verkeerde kant wijst.</p>
<p>Dit is je dopaminesysteem dat protest aantekent. Je hersenen zijn de afgelopen maanden of jaren gewend geraakt aan dagelijkse pieken. Nu krijgen ze die niet. Ze sturen alarmsignalen.</p>
<p>Wat dat fysiek doet:</p>
<ul>
<li>Slechter slapen</li>
<li>Rusteloze benen</li>
<li>Hoofdpijn</li>
<li>Geïrriteerd reageren op kleine dingen</li>
<li>Zin in suiker, koffie, sigaretten of andere kicks</li>
</ul>
<p>Allemaal normaal. Allemaal tijdelijk.</p>
<p>Wat te doen op dag 2 en 3: beweeg. Veel. Een uur lopen per dag is geen luxe, dat is medicijn. Ga naar de sportschool als je daar al kwam. Begin er anders mee. Beweging zet endorfine vrij, die zachter is dan een dopaminepiek maar wel echte rust geeft.</p>
<p>Eet drie maaltijden. Gewone, zoute maaltijden. Niet alleen koffie en koek. Je systeem heeft brandstof nodig.</p>

<h2>Dag 4. De eerste echte craving.</h2>
<p>Ergens rond dag 4 of 5 komt het. De eerste echte, harde craving.</p>
<p>Niet een gewone "zin in". Een golf. Iets dat door je heen gaat alsof je hele lichaam mee wil. Je hartslag versnelt. Je hand zoekt je telefoon. Je hoofd vindt razendsnel argumenten waarom één keer geen probleem is.</p>
<p>Dit is geen falen. Dit is je verslaving die op het punt staat te verliezen, en die niet stilletjes aftreedt.</p>
<p>Wat doe je?</p>
<p><strong>Niet vechten.</strong> Cravings duren tussen de 5 en 30 minuten als je ze niet voedt. Ja, echt. Cravings zijn als een golf: ze komen op, ze pieken, ze zakken weer. Je hoeft ze niet te overwinnen. Je hoeft ze alleen te overleven.</p>
<p><strong>Verander van omgeving.</strong> Sta op. Loop naar buiten. Andere kamer. Andere bezigheid. Beweeg.</p>
<p><strong>Bel iemand.</strong> De Nationale Hulplijn Gokken: <strong>0800-1995</strong>. Gratis. Anoniem. 24/7. Geen oordeel. Eén keer praten en de craving zakt.</p>
<p><strong>Drink water. Eet iets.</strong> Lichaam reset.</p>
<p>Na 30 minuten ben je er doorheen. En je hebt iets bewezen aan jezelf.</p>

<h2>Dag 5 en 6. De leegte.</h2>
<p>Op dag 5 of 6 verschuift iets.</p>
<p>De fysieke onrust wordt minder. Je slaapt iets beter. De cravings worden minder vaak.</p>
<p>Maar er komt iets anders op. Iets vervelenders, eerlijk gezegd. Een soort leegte. Verveling die geen verveling is. Onbestemdheid.</p>
<p>Veel mensen onderschatten dit moment. Ze denken: het zwaarste is voorbij. En dan, vanuit die leegte, sluipt de gedachte binnen: "Ik kan vast wel weer een keer."</p>
<p>Dat is het gevaarlijkste moment van de week.</p>
<p>Wat doe je?</p>
<p><strong>Vul je tijd actief in.</strong> Niet passief tv-kijken (al mag dat ook). Maar dingen doen die structuur geven. Plan je avonden. Plan je weekend. Maak afspraken met mensen.</p>
<p><strong>Ga journalen.</strong> Schrijf over wat je voelt, ook al voel je niks bijzonders. Dat klinkt soft. Het werkt. Je krijgt grip op gedachten die anders rondspoken.</p>
<p><strong>Onthoud waarom.</strong> Lees terug wat je op dag 1 schreef. Vraag jezelf: wat is er veranderd sinds toen? Wat heb je vandaag al bereikt?</p>

<h2>Dag 7. Eén week.</h2>
<p>Eén week.</p>
<p>Dat klinkt klein. Het is enorm.</p>
<p>Eén week is bewijs dat het kan. Bewijs dat je een week kunt zonder. Bewijs dat de wereld niet vergaat. Bewijs dat je hersenen aanpasbaar zijn.</p>
<p>Het is geen overwinning. Wel een fundering.</p>
<p>Op dag 7:</p>
<ul>
<li>Je slaapt waarschijnlijk nog niet perfect, maar wel beter dan op dag 3</li>
<li>Je hebt minimaal één craving overwonnen zonder eraan toe te geven</li>
<li>Je hebt geld bespaard. Concreet. Tel het.</li>
</ul>
<p>Vier het. Niet groots. Wel echt. Trakteer jezelf op iets goeds. Eet ergens uit. Koop dat boek. Doe iets wat geld kost. Want jij hebt nu geld, en je weet het, en het voelt goed.</p>

<h2>Wat komt erna?</h2>
<p>De eerste week is de zwaarste in fysiek opzicht. De maanden erna zijn een ander soort werk. Je bouwt aan nieuwe gewoonten. Aan nieuwe routines. Aan een leven waarin gokken geen plaats meer heeft.</p>
<p>Op dag 30 begint je hoofd echt rustiger te worden. Op dag 100 ben je iemand met een streak van honderd dagen. Op dag 365 lees je terug wat je op dag 1 aan jezelf schreef en je herkent jezelf bijna niet meer.</p>
<p>Maar dat begint nu. Met deze week. Met vandaag.</p>
<p>Eén dag tegelijk. Eén beslissing tegelijk.</p>
<p>Doorgaan.</p>"""

related3 = (
    rel("/nl/blog/stoppen-met-gokken","Herstel","Stoppen met gokken: een eerlijke gids") +
    rel("/nl/blog/wat-doet-gokken-met-je-hersenen","Brein","Wat doet gokken met je hersenen?") +
    rel("/nl/blog/gokverslaving-herkennen","Bewustwording","Gokverslaving herkennen: 12 signalen")
)

html3 = page(
    "nl",
    "Eerste week stoppen met gokken: wat te verwachten | Afterbetting",
    "Eerste week stoppen met gokken is de zwaarste. Dag voor dag wat je tegenkomt en hoe je doorzet. Eerlijk, geen sprookjes.",
    url3,
    [("nl","https://afterbetting.com/nl/blog/eerste-week-stoppen-met-gokken"),("en",url3_en),("x-default",url3_en)],
    [schema3_article, schema3_bc],
    hero3, body3, related3,
    "Wil je je eerste week structureren?",
    "Dagelijkse check-ins en een streak die meegroeit. Crisisknop ingebouwd, voor de momenten dat je hem nodig hebt."
)

with open("nl/blog/eerste-week-stoppen-met-gokken.html","w",encoding="utf-8") as f:
    f.write(html3)
print("OK: eerste-week-stoppen-met-gokken.html")

# ── ARTIKEL 4: wat-doet-gokken-met-je-hersenen ───────────────────────────────

slug4 = "wat-doet-gokken-met-je-hersenen"
url4  = f"https://afterbetting.com/nl/blog/{slug4}"
url4_en = "https://afterbetting.com/blog/what-happens-to-your-brain-when-you-stop-gambling"

schema4_article = json.dumps({"@context":"https://schema.org","@type":"Article","headline":"Wat doet gokken met je hersenen? Een eerlijk verhaal in gewone taal.","author":{"@type":"Organization","name":"Afterbetting"},"publisher":{"@type":"Organization","name":"Afterbetting","url":"https://afterbetting.com"},"datePublished":"2026-04-26","dateModified":"2026-04-26","inLanguage":"nl","url":url4})
schema4_bc = json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://afterbetting.com/nl/"},{"@type":"ListItem","position":2,"name":"Blog","item":"https://afterbetting.com/nl/blog"},{"@type":"ListItem","position":3,"name":"Wat doet gokken met je hersenen?","item":url4}]})

hero4 = '''<section class="hero"><div class="hero-inner">
<div class="bc"><a href="/nl/">Home</a> &rarr; <a href="/nl/blog">Blog</a> &rarr; Brein</div>
<div class="tag">Brein</div>
<h1>Wat doet gokken met je hersenen? Een eerlijk verhaal in gewone taal.</h1>
<p style="font-size:1.1rem;color:var(--mid);font-weight:300;line-height:1.7;margin-top:1rem">Dopamine, beloning, en waarom je niet zomaar kunt stoppen. In gewone taal uitgelegd, zonder jargon.</p>
<div class="meta">Door Afterbetting &middot; 26 april 2026 &middot; 8 min lezen</div>
</div></section>'''

body4 = """<p>Even iets eerlijks.</p>
<p>Je bent niet zwak omdat je niet kunt stoppen met gokken. Je bent niet stom. Je hebt geen karakterprobleem.</p>
<p>Wat je wel hebt: hersenen die zijn geherbedraad door iets dat is ontworpen om precies die hersenen te kapen. Slotmachines, online casino's, sportgokken-apps. Allemaal ontworpen door teams van psychologen en datawetenschappers met één doel: jouw aandacht zo lang mogelijk vasthouden en jouw geld zo snel mogelijk binnenhalen.</p>
<p>Dat klinkt als complotpraat. Het is geen complot. Het is gewoon hoe deze industrie werkt.</p>
<p>In dit artikel leg ik in gewone taal uit wat gokken met je hersenen doet. Geen jargon. Geen wetenschappelijke afstandelijkheid. Wel feiten waar je iets aan hebt.</p>

<h2>Het beloningssysteem. De motor onder de motorkap.</h2>
<p>In je hersenen zit een netwerk dat het beloningssysteem heet. Het is een paar miljoen jaar oud. Het is de reden dat je voorouders eten zochten, een partner vonden, en gevaar ontweken.</p>
<p>Het werkt simpel: als je iets doet dat goed is voor overleving of voortplanting, krijg je een dopamineshot. Dat voelt fijn. Dus ga je het opnieuw doen.</p>
<p>Eten dat zoet smaakt? Dopamine. Goedkeuring van anderen? Dopamine. Seks? Dopamine. Het werkt. Het houdt de soort in stand.</p>
<p>Maar het systeem werd niet ontworpen voor 2026. Het werd ontworpen voor de savanne.</p>
<p>In de savanne kreeg je af en toe iets goeds. Een rijpe vrucht. Een succesvolle jacht. Tussendoor was er niks. Het systeem heeft die zeldzaamheid nodig om gezond te functioneren.</p>
<p>En toen kwamen slotmachines.</p>

<h2>Waarom gokken zo verslavend is. Drie woorden.</h2>
<p>Variabele intermitterende beloning.</p>
<p>Klinkt ingewikkeld. Is simpel.</p>
<p><strong>Variabel</strong> betekent: de beloning is niet altijd even groot. Soms win je een tientje. Soms duizend.</p>
<p><strong>Intermitterend</strong> betekent: de beloning komt onvoorspelbaar. Je weet niet wanneer.</p>
<p>Dit is, statistisch en neurologisch, het meest verslavende beloningspatroon dat bestaat. Verslavender dan vaste beloningen. Verslavender dan grote zekere beloningen. Verslavender dan veel drugs.</p>
<p>In experimenten met ratten en duiven werd dit ontdekt: een dier dat soms wel en soms niet voer krijgt na een knop indrukken, blijft die knop drukken tot het doodvalt. Letterlijk. Terwijl een dier dat altijd voer krijgt na de knop, snel stopt zodra het verzadigd is.</p>
<p>Slotmachines, sportgokken, online casino's. Allemaal zijn ze gebaseerd op variabele intermitterende beloning. Niet per ongeluk. Heel bewust.</p>

<h2>De dopaminepiek zit niet waar je denkt.</h2>
<p>Hier is het tweede belangrijke ding.</p>
<p>Je zou denken: ik krijg dopamine als ik win.</p>
<p>Klopt niet.</p>
<p>De grootste dopaminepiek komt niet bij de winst. Die komt bij de anticipatie van mogelijke winst. Het draaien van de rollen. De seconde voor het doelpunt. De kaart die nog niet is gedraaid.</p>
<p>Dat moment van "het kan, het kan, het kan" is waar je hersenen vuur vatten.</p>
<p>Dat is waarom verliezen je niet stopt. Verliezen vermindert de dopamine niet. Het verlangt naar de volgende anticipatie. Dat is waarom je doorgaat. Niet omdat je een idioot bent. Omdat je hersenen je vertellen: "De volgende keer komt eraan, en het kan groot zijn."</p>

<h2>Wat gokken op de lange termijn met je hoofd doet.</h2>
<p>Hier wordt het minder leuk om te lezen, maar je hebt het recht om het te weten.</p>
<p>Langdurig gokken, we hebben het over maanden tot jaren, verandert je hersenen op een paar manieren:</p>
<p><strong>Je beloningsdrempel stijgt.</strong></p>
<p>Je dopaminesysteem raakt afgestompt. Wat vroeger fijn was, voelt nu vlak. Een wandeling. Een goed gesprek. Een mooie maaltijd. Allemaal worden ze minder bevredigend, omdat je systeem alleen nog reageert op de pieken die gokken geeft.</p>
<p>Dit heet hedonische adaptatie. En het is wat veel mensen ervaren als depressie of leegheid bij gokverslaving.</p>
<p><strong>Je impulscontrole neemt af.</strong></p>
<p>Je prefrontale cortex, het deel van je hersenen dat lange termijnbeslissingen neemt, raakt minder actief. Je beloningssysteem wordt overactief. Het ene roept "later, plan, denk na". Het andere roept "nu, nu, nu". Bij gokverslaving wint het tweede.</p>
<p><strong>Je stressrespons raakt ontregeld.</strong></p>
<p>Cortisol, het stresshormoon, gaat schommelen. Je voelt je vaker gespannen, ook zonder duidelijke reden. Je slaapt slechter. Je rust minder uit.</p>
<p><strong>Je geheugen en concentratie nemen af.</strong></p>
<p>Studies laten zien dat mensen met een gokverslaving slechter scoren op concentratie- en werkgeheugentaken. Niet omdat ze dommer zijn. Omdat hun systeem onder constante druk staat.</p>

<h2>Het goede nieuws. Hersenen zijn aanpasbaar.</h2>
<p>Hier is het lichtpunt, en het is een groot lichtpunt.</p>
<p>Je hersenen zijn neuroplastisch. Dat betekent: ze kunnen veranderen. Ook nadat ze door verslaving zijn herbedraad.</p>
<p>Wat er gebeurt als je stopt:</p>
<p><strong>Eerste 1 tot 2 weken.</strong> Je dopaminesysteem zit in een ontwenning. Je voelt je vlak, prikkelbaar, leeg. Dit is de fase waar veel mensen sneuvelen. Hou het vol.</p>
<p><strong>Week 3 tot 6.</strong> Je beloningsdrempel begint te zakken. Kleine dingen beginnen weer te bevredigen. Een goede koffie. Een wandeling. Een gesprek waar je echt aanwezig bent. Geen explosies van geluk. Wel een soort warmte die was verdwenen.</p>
<p><strong>Maand 2 tot 6.</strong> Je prefrontale cortex herstelt. Je impulscontrole verbetert. Je kunt langer doelgericht werken. Je kunt makkelijker beslissingen nemen die je niet meteen iets opleveren.</p>
<p><strong>Na 6 maanden.</strong> Functioneel onderzoek laat zien dat veel hersenfuncties bij voormalige gokkers terug bewegen naar normale waarden. Niet altijd helemaal. Maar genoeg.</p>
<p><strong>Na een jaar of langer.</strong> Je systeem heeft een nieuwe baseline gevonden. Cravings worden zeldzaam. Het leven krijgt weer kleur, maar dan op een rustigere manier dan ooit.</p>

<h2>Wat je hersenen nodig hebben tijdens herstel.</h2>
<p>Geen wondermiddelen. Wel basis.</p>
<p><strong>Slaap.</strong> Je hersenen herstellen tijdens slaap. Slecht slapen vertraagt herstel. Slaap is niet onderhandelbaar.</p>
<p><strong>Beweging.</strong> Beweging zet endorfine vrij en stimuleert de aanmaak van nieuwe verbindingen tussen hersencellen. Een uur lopen per dag is geen luxe, het is bouwsteen.</p>
<p><strong>Eten.</strong> Echt eten. Vis, groente, noten, fruit. Je hersenen hebben omega-3, vitamines en mineralen nodig om te herstellen.</p>
<p><strong>Connectie.</strong> Eenzaamheid vertraagt herstel. Mensen om je heen die het weten. Eén of twee is genoeg.</p>
<p><strong>Geduld.</strong> Je systeem heeft tijd nodig. Probeer het niet te forceren. Probeer het wel vol te houden.</p>

<h2>Het allerbelangrijkste</h2>
<p>Eén ding om te onthouden.</p>
<p>Wat gokken met je hersenen heeft gedaan, is niet permanent. Wat je terugbouwt, is dat ook niet automatisch. Het is werk. Maar het werkt.</p>
<p>Eén dag tegelijk. Eén beslissing tegelijk. Eén nieuwe verbinding in je hoofd tegelijk.</p>
<p>Je hersenen weten al hoe ze het moeten doen. Je hoeft ze alleen de kans te geven.</p>"""

related4 = (
    rel("/nl/blog/stoppen-met-gokken","Herstel","Stoppen met gokken: een eerlijke gids") +
    rel("/nl/blog/eerste-week-stoppen-met-gokken","Herstel","Je eerste week stoppen met gokken: dag voor dag") +
    rel("/nl/blog/gokverslaving-herkennen","Bewustwording","Gokverslaving herkennen: 12 signalen")
)

html4 = page(
    "nl",
    "Wat doet gokken met je hersenen? Helder uitgelegd | Afterbetting",
    "Wat doet gokken met je hersenen? Dopamine, beloning, en waarom je niet zomaar kunt stoppen. In gewone taal uitgelegd.",
    url4,
    [("nl","https://afterbetting.com/nl/blog/wat-doet-gokken-met-je-hersenen"),("en",url4_en),("x-default",url4_en)],
    [schema4_article, schema4_bc],
    hero4, body4, related4,
    "Wil je je herstel ondersteunen?",
    "Dagelijkse check-ins, journaal en streak. Tools die werken met hoe je hersenen werken."
)

with open("nl/blog/wat-doet-gokken-met-je-hersenen.html","w",encoding="utf-8") as f:
    f.write(html4)
print("OK: wat-doet-gokken-met-je-hersenen.html")

# ── BLOG INDEX ────────────────────────────────────────────────────────────────

index_schema_blog = json.dumps({"@context":"https://schema.org","@type":"Blog","name":"Afterbetting Blog","url":"https://afterbetting.com/nl/blog","description":"Eerlijke artikelen over stoppen met gokken, herstel en gokverslaving. In gewone taal, voor mensen die echt willen stoppen.","inLanguage":"nl","publisher":{"@type":"Organization","name":"Afterbetting","url":"https://afterbetting.com"}})
index_schema_bc = json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://afterbetting.com/nl/"},{"@type":"ListItem","position":2,"name":"Blog","item":"https://afterbetting.com/nl/blog"}]})

index_css_extra = """
.blog-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:1.5rem;margin:2rem 0}
.blog-card{background:#fff;border:1px solid var(--border);border-radius:14px;padding:1.5rem;text-decoration:none;display:block;transition:border-color .2s}
.blog-card:hover{border-color:var(--clay)}
.blog-card .cat{font-size:.72rem;color:var(--green);font-weight:500;text-transform:uppercase;letter-spacing:.06em;margin-bottom:.6rem}
.blog-card h2{font-family:"Fraunces",serif;font-size:1.15rem;font-weight:400;color:var(--dark);line-height:1.3;margin-bottom:.6rem}
.blog-card p{font-size:.9rem;color:var(--muted);line-height:1.6;font-weight:300;margin:0 0 .75rem}
.blog-card .meta{font-size:.75rem;color:var(--muted)}
@media(max-width:768px){.blog-grid{grid-template-columns:1fr}}
"""

articles = [
    {
        "href":"/nl/blog/stoppen-met-gokken",
        "cat":"Herstel",
        "title":"Stoppen met gokken: een eerlijke gids voor wie het echt meent",
        "desc":"Stoppen met gokken is geen kwestie van wilskracht. Wat echt werkt, waarom je vastzit, en hoe je vandaag begint.",
        "time":"8 min lezen"
    },
    {
        "href":"/nl/blog/gokverslaving-herkennen",
        "cat":"Bewustwording",
        "title":"Gokverslaving herkennen: 12 signalen die je niet langer kunt negeren",
        "desc":"Verslaving liegt, ook tegen jezelf. Deze 12 signalen laten zien wanneer er meer aan de hand is.",
        "time":"7 min lezen"
    },
    {
        "href":"/nl/blog/eerste-week-stoppen-met-gokken",
        "cat":"Herstel",
        "title":"Je eerste week stoppen met gokken: dag voor dag",
        "desc":"De eerste week is de zwaarste. Dag voor dag wat je tegenkomt en hoe je doorzet.",
        "time":"7 min lezen"
    },
    {
        "href":"/nl/blog/wat-doet-gokken-met-je-hersenen",
        "cat":"Brein",
        "title":"Wat doet gokken met je hersenen? Een eerlijk verhaal in gewone taal.",
        "desc":"Dopamine, anticipatie, en waarom stoppen zo moeilijk is. Uitgelegd zonder jargon.",
        "time":"8 min lezen"
    },
]

cards_html = ""
for a in articles:
    cards_html += f'''<a href="{a["href"]}" class="blog-card">
<div class="cat">{a["cat"]}</div>
<h2>{a["title"]}</h2>
<p>{a["desc"]}</p>
<div class="meta">26 april 2026 &middot; {a["time"]}</div>
</a>'''

index_html = f"""<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="UTF-8"/>
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title>Blog over gokverslaving en herstel | Afterbetting</title>
<meta name="description" content="Eerlijke artikelen over stoppen met gokken, gokverslaving herkennen en herstel. In gewone taal, voor mensen die echt willen stoppen."/>
<meta name="robots" content="index,follow"/>
<link rel="canonical" href="https://afterbetting.com/nl/blog"/>
<link rel="alternate" hreflang="nl" href="https://afterbetting.com/nl/blog"/>
<link rel="alternate" hreflang="en" href="https://afterbetting.com/blog"/>
<link rel="alternate" hreflang="x-default" href="https://afterbetting.com/blog"/>
<meta property="og:type" content="website"/>
<meta property="og:locale" content="nl_NL"/>
<meta property="og:url" content="https://afterbetting.com/nl/blog"/>
<meta property="og:title" content="Blog over gokverslaving en herstel | Afterbetting"/>
<meta property="og:description" content="Eerlijke artikelen over stoppen met gokken en herstel."/>
<meta property="og:image" content="https://afterbetting.com/og-image.png"/>
<script type="application/ld+json">{index_schema_blog}</script>
<script type="application/ld+json">{index_schema_bc}</script>
{GA}
{FONTS}
<style>{CSS}{index_css_extra}</style>
</head>
<body>
{NAV}
<section class="hero"><div class="hero-inner">
<div class="bc"><a href="/nl/">Home</a> &rarr; Blog</div>
<h1>Blog</h1>
<p style="font-size:1.1rem;color:var(--mid);font-weight:300;line-height:1.7;margin-top:1rem">Eerlijke artikelen over stoppen met gokken, gokverslaving herkennen en herstel. Geen preek. Geen sprookjes. Wel wat werkt.</p>
</div></section>
<div style="max-width:820px;margin:0 auto;padding:3rem 2rem">
<div class="blog-grid">{cards_html}</div>
</div>
{CRISIS}
{FOOTER}
</body></html>"""

with open("nl/blog/index.html","w",encoding="utf-8") as f:
    f.write(index_html)
print("OK: nl/blog/index.html")
print("Alle bestanden gegenereerd.")
