import os, json

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

# ── ARTIKEL 11: zelfuitsluiting-gokken-werkt-het ─────────────────────────────

slug11 = "zelfuitsluiting-gokken-werkt-het"
url11  = f"https://afterbetting.com/nl/blog/{slug11}"

schema11_article = json.dumps({"@context":"https://schema.org","@type":"Article","headline":"Werkt zelfuitsluiting bij gokken? Een eerlijk antwoord.","author":{"@type":"Organization","name":"Afterbetting"},"publisher":{"@type":"Organization","name":"Afterbetting","url":"https://afterbetting.com"},"datePublished":"2026-04-26","dateModified":"2026-04-26","inLanguage":"nl","url":url11})
schema11_bc = json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://afterbetting.com/nl/"},{"@type":"ListItem","position":2,"name":"Blog","item":"https://afterbetting.com/nl/blog"},{"@type":"ListItem","position":3,"name":"Werkt zelfuitsluiting bij gokken?","item":url11}]})

hero11 = '''<section class="hero"><div class="hero-inner">
<div class="bc"><a href="/nl/">Home</a> &rarr; <a href="/nl/blog">Blog</a> &rarr; Tools</div>
<div class="tag">Tools</div>
<h1>Werkt zelfuitsluiting bij gokken? Een eerlijk antwoord.</h1>
<p style="font-size:1.1rem;color:var(--mid);font-weight:300;line-height:1.7;margin-top:1rem">Wat Cruks wel en niet doet, de gaten in het systeem en hoe je ze dichtmaakt. Feiten, geen marketingpraat.</p>
<div class="meta">Door Afterbetting &middot; 26 april 2026 &middot; 8 min lezen</div>
</div></section>'''

body11 = """<p>Je hebt erover gehoord. Cruks. Zelfuitsluiting. Een knop op een website waar je jezelf voor minimaal zes maanden buiten kan zetten.</p>
<p>Klinkt makkelijk. Klinkt definitief. Klinkt alsof het probleem zo opgelost is.</p>
<p>En toch heb je twijfels. Want je weet zelf hoe creatief je hersenen kunnen zijn als ze willen gokken. Een uitsluiting omzeilen, dat lukt toch wel?</p>
<p>Dit artikel geeft het eerlijke antwoord. Wat zelfuitsluiting wél doet. Wat het niet doet. Welke gaten er in het systeem zitten. En wat je daarnaast moet regelen om het ook echt te laten werken.</p>

<h2>Wat is Cruks precies?</h2>
<p>Cruks staat voor Centraal Register Uitsluiting Kansspelen.</p>
<p>Het is een Nederlands register, beheerd door de Kansspelautoriteit. Als jij je daar inschrijft, mogen alle Nederlandse legale aanbieders van risicovolle kansspelen je niet meer binnenlaten.</p>
<p>Wat valt onder Cruks:</p>
<ul>
<li>Online casino's met Nederlandse vergunning</li>
<li>Sportgokken-aanbieders met Nederlandse vergunning</li>
<li>Speelautomatenhallen</li>
<li>Holland Casino</li>
</ul>
<p>Hoelang? Minimaal zes maanden. Maximaal levenslang. Je kiest zelf, met een minimum van een half jaar.</p>
<p>Hoe meld je je aan? Via cruks.nl. Je hebt DigiD nodig. Het kost je tien minuten. Vanaf het moment dat je bevestigt, ben je geregistreerd.</p>
<p>Belangrijk: het is gratis. Het kost niets. Geen abonnement, geen verlenging, geen verborgen voorwaarden.</p>

<h2>Wat zelfuitsluiting wel doet</h2>
<p>Het werkt beter dan je denkt. Voor wat het is.</p>
<p><strong>Eén: het haalt de directe toegang weg.</strong></p>
<p>Geen "even snel inloggen op die ene site". Je probeert in te loggen, je krijgt een melding dat je geblokkeerd bent. Spel afgelopen.</p>
<p><strong>Twee: het voegt wrijving toe.</strong></p>
<p>Wrijving is een onderschat woord in herstel. Hoe meer stappen tussen jou en het gokken, hoe groter de kans dat je een van die stappen niet zet. Cruks voegt veel wrijving toe.</p>
<p><strong>Drie: het is moeilijk omkeerbaar.</strong></p>
<p>Je kunt je niet één avond uitschrijven om snel iets te gokken. De minimale termijn is zes maanden. Als je je inschrijft voor langer, is dat ook bindend. Dat is geen beperking. Dat is een gunst aan je toekomstige zelf.</p>
<p><strong>Vier: het werkt psychologisch.</strong></p>
<p>Je weet dat je geregistreerd bent. Je weet dat de optie er niet meer is. Dat verandert je gedachten. Niet alle dwangmatige gedachten verdwijnen, maar de "even snel"-impulsen worden zwakker omdat hun uitvoering onmogelijk is.</p>

<h2>Waar zelfuitsluiting tekort schiet</h2>
<p>Eerlijk verhaal: Cruks heeft gaten.</p>
<p><strong>Gat 1: illegale buitenlandse sites.</strong></p>
<p>Cruks geldt alleen voor aanbieders met een Nederlandse vergunning. Buitenlandse sites zonder Nederlandse vergunning vallen er niet onder. Die zijn officieel illegaal in Nederland, maar bestaan online. Iemand die zoekt, vindt ze.</p>
<p><strong>Gat 2: krasloten en loterij.</strong></p>
<p>De Nederlandse Loterij, Postcode Loterij en sommige loterijproducten vallen niet of beperkt onder Cruks. Krasloten in supermarkten kun je gewoon kopen. Voor sommige verslavingen is dat genoeg om te triggeren.</p>
<p><strong>Gat 3: cryptogokken.</strong></p>
<p>Sites die met crypto werken vallen vaak buiten elke Nederlandse regelgeving. Technisch illegaal, in de praktijk vindbaar.</p>
<p><strong>Gat 4: sociaal gokken.</strong></p>
<p>Pokerspel met vrienden voor geld. Wedjes thuis. Privépools voor sportwedstrijden. Niets daarvan valt onder Cruks.</p>
<p><strong>Gat 5: creatieve omwegen.</strong></p>
<p>Een familielid laten inloggen. Een buitenlandse VPN. Het kan. Het is allemaal af te raden, en het zegt iets over hoe diep de verslaving zit als je hieraan denkt. Dat is informatie. Geen schaamte.</p>

<h2>Cruks alleen is niet genoeg. Maak het systeem dicht.</h2>
<p>Wil je dat zelfuitsluiting echt werkt, dan combineer je het met een paar andere blokkades. Samen vormen ze een netwerk dat veel moeilijker te omzeilen is.</p>
<p><strong>Cruks aanmelding (basislaag).</strong></p>
<p>Doe dit eerst. Tien minuten op cruks.nl. Kies minimaal één jaar. Kies langer als je dat aankunt. Levenslang is een optie.</p>
<p><strong>Bankblokkade (financiële laag).</strong></p>
<p>Bel je bank. Vraag om gokblokkade op je rekening en eventuele creditcards. ABN, ING, Rabobank, Bunq, ASN, Triodos: ze hebben allemaal een vorm hiervan. Soms heet het Stop Gokken, soms een aparte instelling in de app.</p>
<p>Wat dit doet: het blokkeert betalingen naar gokwebsites op het niveau van de bank. Ook als je een site weet te bereiken die niet onder Cruks valt, gaat de betaling niet door.</p>
<p><strong>Telefoonschoonmaak (digitale laag).</strong></p>
<p>Verwijder elke gok-app van je telefoon. Verwijder bookmarks. Schrijf je uit voor reclamemails. Stel schermtijdbeperkingen in waarmee je gok-apps niet meer kunt installeren zonder een code die iemand anders heeft.</p>
<p><strong>Software-blokkades (technische laag).</strong></p>
<p>Op je computer en telefoon kun je software installeren die gokwebsites blokkeert. Voorbeelden: Gamban, BetBlocker, Net Nanny. Sommige zijn gratis, andere betaald. Deze tools werken op DNS-niveau en blokkeren ook veel buitenlandse sites.</p>
<p><strong>Sociale laag.</strong></p>
<p>Vertel iemand dat je je hebt aangemeld. Vraag of die persoon meekijkt. Wrijving plus accountability is sterker dan wrijving alleen.</p>
<p>Lees ook: <a href="/nl/blog/gokken-aan-je-familie-vertellen">Gokken aan je familie vertellen: zo begin je het gesprek</a></p>

<h2>Wanneer schrijf je je in voor langer?</h2>
<p>Veel mensen schrijven zich in voor zes maanden. De minimale termijn. Met de gedachte "ik kijk wel of ik dan zover ben".</p>
<p>Eerlijk advies: schrijf je in voor minimaal een jaar. Liever twee. Sommige mensen kiezen levenslang.</p>
<p>Waarom? Zes maanden is precies lang genoeg om door de zwaarste fysieke ontwenning heen te komen. Het is te kort om je hersenen tijd te geven om volledig opnieuw bedraad te raken. Op maand zes weet je dat je geblokkeerd bent. Op maand zeven kun je weer in. En je hersenen weten dat. Ze tellen af.</p>
<p>Een jaar of langer haalt die telling weg. Het wordt geen tijdelijke maatregel, het wordt een nieuwe normaal.</p>
<p>Levenslang lijkt drastisch. Voor sommigen is het het meest bevrijdende dat ze ooit hebben gedaan. De optie is weg. Niet onderhandelbaar.</p>

<h2>Hoeveel mensen zijn ingeschreven?</h2>
<p>Meer dan honderdduizend Nederlanders zijn aangemeld bij Cruks. Je bent niet alleen.</p>
<p>Dat zijn niet allemaal mensen met een verslaving. Een deel zijn mensen die het preventief doen. Of die voelen dat ze richting een probleem gaan. Of die familieleden zijn die zich op verzoek hebben ingeschreven.</p>
<p>Wat het laat zien: dit is een gewone, geaccepteerde stap. Geen schande. Geen extreme actie. Iets wat steeds meer mensen doen om grip te krijgen.</p>

<h2>Wat doe je als je toch een drang voelt?</h2>
<p>Cruks geeft je een muur. De drang kruipt soms toch over de muur.</p>
<p><strong>Wacht 30 minuten.</strong> Cravings duren tussen 5 en 30 minuten. Verander van omgeving. Loop. Bel iemand. De golf zakt.</p>
<p><strong>Bel de Nationale Hulplijn Gokken: 0800-1995.</strong> Gratis, anoniem, 24/7. Eén keer praten en de impuls neemt af.</p>
<p><strong>Open je app of journaal.</strong> Schrijf op wat je voelt. Vijf regels. Niet om het op te lossen. Om het uit je hoofd te halen.</p>
<p><strong>Onthoud waarom je dit doet.</strong> Lees terug wat je op dag 1 schreef. Je hebt al een muur gebouwd. De muur staat. Je hoeft alleen niet te proberen erover te klimmen.</p>

<h2>Doe het vandaag</h2>
<p>Niet morgen. Vandaag.</p>
<p>Cruks aanmelding: cruks.nl, tien minuten, DigiD bij de hand.</p>
<p>Bel je bank: vandaag of maandag.</p>
<p>Verwijder gok-apps: nu.</p>
<p>Vertel iemand dat je het gedaan hebt: deze week.</p>
<p>Eén actie tegelijk. Maar wel beginnen.</p>"""

related11 = (
    rel("/nl/blog/stoppen-met-gokken","Herstel","Stoppen met gokken: een eerlijke gids") +
    rel("/nl/blog/eerste-week-stoppen-met-gokken","Herstel","Je eerste week stoppen met gokken: dag voor dag") +
    rel("/nl/blog/terugval-na-gokverslaving","Herstel","Terugval na gokverslaving. Wat nu?")
)

html11 = page(
    "nl",
    "Werkt zelfuitsluiting bij gokken? Eerlijk antwoord | Afterbetting",
    "Werkt zelfuitsluiting bij gokken echt? Wat Cruks wel en niet doet, de gaten in het systeem en hoe je ze dichtmaakt.",
    url11,
    [("nl","https://afterbetting.com/nl/blog/zelfuitsluiting-gokken-werkt-het"),("x-default","https://afterbetting.com/nl/blog/zelfuitsluiting-gokken-werkt-het")],
    [schema11_article, schema11_bc],
    hero11, body11, related11,
    "Cruks dichtgezet?",
    "Maak nu ook een gratis account aan op Afterbetting voor dagelijkse structuur, journaal en een crisisknop voor de momenten dat het zwaar wordt."
)

with open("nl/blog/zelfuitsluiting-gokken-werkt-het.html","w",encoding="utf-8") as f:
    f.write(html11)
print("OK: zelfuitsluiting-gokken-werkt-het.html")

# ── ARTIKEL 12: slaapproblemen-stoppen-met-gokken ────────────────────────────

slug12 = "slaapproblemen-stoppen-met-gokken"
url12  = f"https://afterbetting.com/nl/blog/{slug12}"

schema12_article = json.dumps({"@context":"https://schema.org","@type":"Article","headline":"Slaapproblemen na stoppen met gokken. Wat helpt echt.","author":{"@type":"Organization","name":"Afterbetting"},"publisher":{"@type":"Organization","name":"Afterbetting","url":"https://afterbetting.com"},"datePublished":"2026-04-26","dateModified":"2026-04-26","inLanguage":"nl","url":url12})
schema12_bc = json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://afterbetting.com/nl/"},{"@type":"ListItem","position":2,"name":"Blog","item":"https://afterbetting.com/nl/blog"},{"@type":"ListItem","position":3,"name":"Slaapproblemen na stoppen met gokken","item":url12}]})

hero12 = '''<section class="hero"><div class="hero-inner">
<div class="bc"><a href="/nl/">Home</a> &rarr; <a href="/nl/blog">Blog</a> &rarr; Tools</div>
<div class="tag">Tools</div>
<h1>Slaapproblemen na stoppen met gokken. Wat helpt echt.</h1>
<p style="font-size:1.1rem;color:var(--mid);font-weight:300;line-height:1.7;margin-top:1rem">Slaapproblemen na stoppen met gokken zijn normaal. Waarom je niet slaapt, hoe lang het duurt en wat echt helpt. Eerlijk advies.</p>
<div class="meta">Door Afterbetting &middot; 26 april 2026 &middot; 8 min lezen</div>
</div></section>'''

body12 = """<p>Je bent gestopt. Goed bezig.</p>
<p>En je slaapt voor geen meter.</p>
<p>Drie uur 's nachts en je staart naar het plafond. Je hartslag te hoog. Je hoofd vol gedachten die nergens heen gaan. Je telefoon op het nachtkastje die fluistert: "Even checken kan toch geen kwaad."</p>
<p>Dit gaat al dagen zo. Misschien weken.</p>
<p>Eerst dit: het is normaal. Vervelend, slopend, maar normaal. Je lichaam doet wat het moet doen. En je hoeft niet eeuwig zo wakker te liggen.</p>
<p>Dit artikel legt uit waarom je slecht slaapt na stoppen met gokken, hoe lang het duurt, en wat wel en niet helpt. Geen wonderpoeders. Wel concrete dingen die werken.</p>

<h2>Waarom je niet slaapt</h2>
<p>Even uitleggen wat er in je systeem gebeurt.</p>
<p>Maandenlang of jarenlang heb je je hersenen overprikkeld met dopaminepieken. Slotmachines, sportwedstrijden, online roulette: allemaal gemaakt om je arousal-niveau hoog te houden. Je sympathisch zenuwstelsel, het gas van je systeem, was constant aan.</p>
<p>Daarboven kwamen waarschijnlijk: laat opblijven om te gokken, schermen tot diep in de nacht, koffie of energy drinks om wakker te blijven, stress over verliezen en geheimen.</p>
<p>Je biologische klok was ontregeld. Je stresshormoonniveau verhoogd. Je dopamine baseline verschoven.</p>
<p>Nu stop je. Je hersenen krijgen niet meer wat ze gewend waren. Maar je systeem is nog niet gekalibreerd op rust.</p>
<p>Wat er fysiek gebeurt:</p>
<ul>
<li>Cortisol (stresshormoon) blijft hoog</li>
<li>Dopamine afgevlakt, waardoor je je vlak en rusteloos voelt tegelijk</li>
<li>Slaap-waakritme ontregeld</li>
<li>Hersenactiviteit 's avonds nog hoog</li>
<li>Spierspanning hoog, ademhaling oppervlakkig</li>
</ul>
<p>Het resultaat: in slaap vallen lukt niet, of je wordt midden in de nacht wakker en kunt niet meer terug.</p>

<h2>Hoe lang duurt het?</h2>
<p>Eerlijk antwoord: het verschilt.</p>
<p><strong>Eerste week.</strong> Vaak het slechtst. Drie tot vier uur slaap is normaal in deze fase. Plus levendige, soms onaangename dromen als je wel slaapt.</p>
<p><strong>Week 2 tot 4.</strong> Langzame verbetering. Je valt iets makkelijker in slaap, maar je wordt nog vroeg wakker. Vijf tot zes uur.</p>
<p><strong>Maand 2 tot 3.</strong> De meeste mensen merken hier echte verbetering. Zes tot zeven uur. Niet altijd diep, maar wel meer.</p>
<p><strong>Maand 3 tot 6.</strong> Slaap normaliseert grotendeels. Niet voor iedereen. Bij sommige mensen duurt het langer, vooral als er andere problemen meespelen.</p>
<p><strong>Na zes maanden.</strong> Wat overblijft aan slaapproblemen heeft meestal een andere oorzaak dan gokken. Tijd om dat te onderzoeken met een huisarts.</p>
<div class="callout"><p><strong>Belangrijk:</strong> slaap herstelt niet altijd lineair. Je hebt goede weken en slechte weken. Een nacht slecht slapen op maand drie is niet een terugslag. Het is gewoon een nacht.</p></div>

<h2>Wat helpt echt? Negen dingen.</h2>
<p>Niet alles tegelijk. Pak er drie of vier uit en doe ze consequent. Twee weken volhouden, dan evalueren.</p>
<p><strong>1. Vaste opstaantijd.</strong></p>
<p>Belangrijker dan vaste bedtijd. Sta elke dag op hetzelfde tijdstip op. Ook in het weekend. Ook als je slecht hebt geslapen.</p>
<p>Waarom? Je biologische klok kalibreert op opstaan, niet op naar bed gaan. Vast opstaan zorgt op den duur dat in slaap vallen ook regelmatiger gaat.</p>
<p><strong>2. Daglicht in de eerste 30 minuten.</strong></p>
<p>Naar buiten. Geen jas zoeken, geen koffie eerst. Gewoon naar buiten of voor het raam staan, vijftien minuten.</p>
<p>Daglicht in je ogen geeft je hersenen het signaal dat de dag begint. Dat zet een keten in gang die ervoor zorgt dat je 14 tot 16 uur later moe wordt. Werkt zelfs bij bewolkt weer.</p>
<p><strong>3. Beweging, dagelijks.</strong></p>
<p>Een uur lopen per dag is geen luxe. Het is medicijn. Beweging verlaagt cortisol, verhoogt natuurlijke moeheid, verbetert diepteslaap. Niet vlak voor het slapengaan intensief sporten. Lichte beweging in de avond mag wel.</p>
<p><strong>4. Geen schermen in het laatste uur.</strong></p>
<p>Je telefoon, je laptop, je tv: allemaal blauw licht en allemaal stimulerend. Eén uur voor bedtijd: schermen weg. Als dat te veel is, begin met dertig minuten.</p>
<p><strong>5. Geen koffie na 14:00.</strong></p>
<p>Cafeïne heeft een halfwaardetijd van vijf tot zes uur. Een koffie om 16:00 betekent dat de helft nog actief is om 22:00. Voor wie net stopt met gokken en al onrustig is: koffie laat op de dag is een directe slaapsabotage.</p>
<p><strong>6. Schrijven voor het slapen.</strong></p>
<p>Pak een schrift. Schrijf vijf minuten op wat in je hoofd zit. Wat zwaar was. Wat je morgen wil doen. Wat je dwarszit.</p>
<p>Dit haalt gedachten uit je hoofd en op papier. Je hersenen krijgen toestemming om los te laten.</p>
<p><strong>7. Koel en donker slapen.</strong></p>
<p>Slaapkamer rond de 18 graden. Verduistering optimaal (gordijnen, slaapmasker). Geen lampjes (laders, klokken). Je hersenen slapen beter in een grot dan in een woonkamer.</p>
<p><strong>8. Beperk middagslaapjes.</strong></p>
<p>Een dutje van 20 minuten kan helpen. Een dutje van anderhalf uur saboteert je nachtrust. Liever helemaal niet als je 's nachts slecht slaapt. Doorbijten tot avond.</p>
<p><strong>9. Geen alcohol als slaapmiddel.</strong></p>
<p>Alcohol helpt je in slaap vallen. Maar het verstoort de tweede helft van je nacht enorm. Plus: voor wie uit verslaving komt, is alcohol als troost een gevaarlijke gewoonte. Verslavingen ruilen werkt niet.</p>

<h2>Wanneer naar de huisarts?</h2>
<p>Slecht slapen door stoppen met gokken hoort er even bij. Maar er zijn momenten waarop je niet alleen verder moet.</p>
<p>Bel een huisarts als:</p>
<ul>
<li>Je na drie maanden nog structureel minder dan vijf uur slaapt</li>
<li>Je overdag zo moe bent dat je niet kunt functioneren</li>
<li>Je sterke angstklachten of depressieve gevoelens hebt naast de slaapproblemen</li>
<li>Je gedachten hebt aan zelfbeschadiging of zelfmoord</li>
<li>Je in dezelfde nacht meerdere keren wakker schrikt met paniek</li>
</ul>
<p>Geen schaamte voor hulp vragen. Slaap is geen luxe, het is een fundament. Zonder slaap stort de rest in.</p>

<h2>Wat je niet doet</h2>
<p><strong>Geen slaaptabletten zonder begeleiding.</strong> Slaapmedicatie heeft vaak afhankelijkheid als bijwerking. Voor iemand die uit verslaving komt is dat dubbel risicovol. Alleen onder controle van een arts, en kortdurend.</p>
<p><strong>Geen melatonine in willekeurige doses.</strong> Melatonine kan helpen bij ritmeproblemen, maar werkt anders dan veel mensen denken. Te veel of op verkeerde tijden werkt averechts. Vraag een huisarts of apotheker.</p>
<p><strong>Niet eindeloos in bed liggen als je niet slaapt.</strong> Twintig minuten wakker liggen? Sta op. Ga naar een andere kamer. Lees iets saais bij gedimd licht. Ga terug als je weer moe bent. In bed liggen tobben leert je hersenen dat het bed een tobplek is. Dat wil je niet.</p>

<h2>Het komt terug</h2>
<p>Eén ding tot slot.</p>
<p>De slaap die je had voor gokken, komt terug. Soms dieper, vrediger, dan je je herinnert.</p>
<p>Maar er is geen sneltrein. Het is een proces van weken tot maanden. Je systeem is bezig zich opnieuw te kalibreren. Geef het tijd.</p>
<p>Vannacht slaap je misschien weer slecht. Morgenochtend sta je op vaste tijd op. Je gaat naar buiten. Je beweegt. Je drinkt geen koffie na 14:00. Je legt je telefoon weg om 22:00.</p>
<p>Eén dag tegelijk. Eén nacht tegelijk.</p>
<p>Het komt.</p>"""

related12 = (
    rel("/nl/blog/wat-doet-gokken-met-je-hersenen","Brein","Wat doet gokken met je hersenen?") +
    rel("/nl/blog/eerste-week-stoppen-met-gokken","Herstel","Je eerste week stoppen met gokken: dag voor dag") +
    rel("/nl/blog/hoe-vul-ik-mijn-tijd-zonder-gokken","Tools","Hoe vul je je tijd zonder gokken?")
)

html12 = page(
    "nl",
    "Slaapproblemen na stoppen met gokken: wat helpt echt | Afterbetting",
    "Slaapproblemen na stoppen met gokken zijn normaal. Waarom je niet slaapt, hoe lang het duurt en wat echt helpt. Eerlijk advies.",
    url12,
    [("nl","https://afterbetting.com/nl/blog/slaapproblemen-stoppen-met-gokken"),("x-default","https://afterbetting.com/nl/blog/slaapproblemen-stoppen-met-gokken")],
    [schema12_article, schema12_bc],
    hero12, body12, related12,
    "Slecht slapen is zwaar. Een goede dagstructuur helpt.",
    "Op Afterbetting gebruik je dagelijkse check-ins, gewoonten tracker en journaalprompts om je systeem terug te kalibreren. Begin gratis."
)

with open("nl/blog/slaapproblemen-stoppen-met-gokken.html","w",encoding="utf-8") as f:
    f.write(html12)
print("OK: slaapproblemen-stoppen-met-gokken.html")

# ── ARTIKEL 13: hoe-vul-ik-mijn-tijd-zonder-gokken ───────────────────────────

slug13 = "hoe-vul-ik-mijn-tijd-zonder-gokken"
url13  = f"https://afterbetting.com/nl/blog/{slug13}"

schema13_article = json.dumps({"@context":"https://schema.org","@type":"Article","headline":"Hoe vul je je tijd zonder gokken?","author":{"@type":"Organization","name":"Afterbetting"},"publisher":{"@type":"Organization","name":"Afterbetting","url":"https://afterbetting.com"},"datePublished":"2026-04-26","dateModified":"2026-04-26","inLanguage":"nl","url":url13})
schema13_bc = json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://afterbetting.com/nl/"},{"@type":"ListItem","position":2,"name":"Blog","item":"https://afterbetting.com/nl/blog"},{"@type":"ListItem","position":3,"name":"Hoe vul je je tijd zonder gokken?","item":url13}]})

hero13 = '''<section class="hero"><div class="hero-inner">
<div class="bc"><a href="/nl/">Home</a> &rarr; <a href="/nl/blog">Blog</a> &rarr; Tools</div>
<div class="tag">Tools</div>
<h1>Hoe vul je je tijd zonder gokken?</h1>
<p style="font-size:1.1rem;color:var(--mid);font-weight:300;line-height:1.7;margin-top:1rem">De leegte na stoppen is reëel. Concrete ideeën zonder zweverigheid om je dagen op te bouwen.</p>
<div class="meta">Door Afterbetting &middot; 26 april 2026 &middot; 8 min lezen</div>
</div></section>'''

body13 = """<p>Je bent gestopt. Goed bezig.</p>
<p>Maar nu zit je er.</p>
<p>Het is dinsdagavond, half negen. Vroeger zou je nu een wedstrijd opzetten en je telefoon op je schoot leggen. Of de app van het casino openklikken. Of een potje poker. Drie uur tot bedtijd, en gevuld.</p>
<p>Nu zit je op de bank. Met je telefoon in je hand zonder te weten wat je ermee wil. Met een tv aan, maar je kijkt niet echt. Met een rusteloos gevoel dat je niet weet hoe je moet plaatsen.</p>
<p>Dit gaat over die avond. En over alle avonden die nog komen. Over wat je doet met de uren die voorheen door gokken werden ingenomen. Niet zweverig. Concreet.</p>

<h2>Eerst dit. De leegte is normaal.</h2>
<p>Voor we naar oplossingen gaan, even erkennen wat er aan de hand is.</p>
<p>Wat je voelt, heeft een naam: een verveling die geen verveling is. Een soort grijze rusteloosheid. Je hebt tijd, maar niets dat dwingend genoeg voelt om te doen. Niets prikt jouw aandacht zoals gokken dat deed.</p>
<p>Dat is geen karakterprobleem. Dat is je dopaminesysteem dat in de wachtkamer staat.</p>
<p>Maandenlang of jarenlang trainde je je hersenen om alleen reactie te geven op pieken. Nu krijgen ze die pieken niet. Het normale leven, een wandeling, een boek, een gesprek, voelt vlak in vergelijking. Niet omdat het vlak is. Omdat je systeem verschoven is.</p>
<p>Dit duurt weken tot maanden. In die periode bouw je gewoonten op die je systeem opnieuw leren waarderen wat klein en gestaag is.</p>
<p>Je voelt je niet meteen geweldig na een wandeling. Maar je doet het toch. En na twintig wandelingen voel je iets anders dan na de eerste. Dat is hoe het werkt.</p>
<p>Lees ook: <a href="/nl/blog/wat-doet-gokken-met-je-hersenen">Wat doet gokken met je hersenen?</a></p>

<h2>Hoeveel tijd had je eigenlijk?</h2>
<p>Reken eens echt.</p>
<p>Hoeveel uur per week ging er naar gokken? Niet alleen het actieve gokken, maar ook:</p>
<ul>
<li>Apps openen om scores te checken</li>
<li>Sportkanalen kijken voor je weddenschappen</li>
<li>Online onderzoek doen</li>
<li>Wachten op uitslagen</li>
<li>Achteraf piekeren over verlies</li>
<li>Geld zoeken, betalingen regelen</li>
</ul>
<p>Voor veel mensen die uit gokverslaving komen, telt dat op tot tien tot twintig uur per week. Soms meer.</p>
<p>Dat zijn drie volle werkdagen aan tijd die nu vrij zijn. Het is geen wonder dat je niet weet wat ermee te doen.</p>

<h2>De drie soorten tijd om in te vullen</h2>
<p>Maak het concreet door te denken in drie categorieën.</p>
<p><strong>Actieve tijd (energie hoog).</strong></p>
<p>Beweging, sport, klussen, koken, sociale dingen. Dingen waarbij je staat, beweegt, doet.</p>
<p><strong>Rustige tijd (energie laag, maar bewust).</strong></p>
<p>Lezen, schrijven, muziek luisteren, een goed gesprek, mediteren, naar buiten gaan zonder doel. Dingen waarbij je niet productief hoeft te zijn, maar wel aanwezig bent.</p>
<p><strong>Verbonden tijd.</strong></p>
<p>Tijd met andere mensen. Bellen, langsgaan, samen iets doen. Niet via een scherm. In het echt.</p>
<p>De fout die mensen maken: ze proberen alleen actieve tijd in te vullen. Ze gaan sporten, klussen, poetsen het huis in een week. Daarna vallen ze in een gat omdat ze rustige tijd niet hebben leren waarderen.</p>
<p>Je hebt allebei nodig. En verbonden tijd is de derde poot waarop je het opbouwt.</p>

<h2>Concrete ideeën. Lange lijst.</h2>
<p>Geen ranglijst. Pak eruit wat resoneert.</p>
<p><strong>Bewegen:</strong> wandelen een uur per dag, sportschool drie keer per week, hardlopen, fietsen, zwemmen, vechtsport (boksen, jiu-jitsu, kickboksen), yoga of pilates, klimmen.</p>
<p><strong>Maken en doen:</strong> bewust koken, tuinieren, klussen in huis, houtbewerken, schilderen of tekenen, muziek maken (gitaar, piano), schrijven (eigen verhaal, journaal, brieven).</p>
<p><strong>Leren:</strong> een taal (Duolingo, Babbel, of een buurtcursus), een vaardigheid, een vak waar je iets aan hebt, lezen (tien boeken per jaar is doenlijk).</p>
<p><strong>Sociale dingen:</strong> sportclub, vrijwilligerswerk (voedselbank, dierenasiel), buurtactiviteiten, iemand bellen die je al lang niet sprak, eens per week samen eten met mensen.</p>
<p><strong>Rustig en bewust:</strong> wandelen zonder telefoon, mediteren (zelfs vijf minuten per dag werkt), een instrument leren bespelen, boekenclub, vissen, vogels kijken.</p>

<h2>Maak een schema. Saaier dan je denkt.</h2>
<p>Hier komt iets saais: structuur werkt.</p>
<p>Gokken vulde je tijd op een ongestructureerde, reactieve manier. Je telefoon stuurde je dag. Een melding, een wedstrijd, een impuls.</p>
<p>Wat je nu nodig hebt is het tegenovergestelde. Een dag waarin je vooraf weet wat je doet. Niet militaristisch. Wel gepland.</p>
<p>Voorbeeld van een doordeweekse avond:</p>
<ul>
<li>18:00 eten, zonder telefoon</li>
<li>19:00 uur lopen of sporten</li>
<li>20:00 ontspannen, lezen, met iemand bellen, een hobby</li>
<li>21:30 tien minuten journalen, telefoon weg</li>
<li>22:00 in bed, lezen of slapen</li>
</ul>
<p>Saai? Misschien. Werkt? Bijna altijd.</p>
<p>Je systeem heeft voorspelbaarheid nodig in deze fase. Voorspelbaarheid is veiligheid. Voorspelbaarheid is de afwezigheid van pieken en dalen waar je impulsief op reageert.</p>

<h2>Twee valkuilen om te vermijden</h2>
<p><strong>Valkuil 1: een nieuwe verslaving.</strong></p>
<p>Mensen die stoppen met gokken pikken soms iets nieuws op dat dezelfde dopaminehit geeft. Online shoppen. Series binge-watchen. Ander gokachtig gedrag (crypto, daytrading).</p>
<p>Wees alert. Een verslaving ruilen voor een andere is geen herstel.</p>
<p><strong>Valkuil 2: te veel ineens.</strong></p>
<p>Je bent vol motivatie. Je schrijft je in voor sportschool, een taalcursus, een vrijwilligersclub en je begint een YouTubekanaal in dezelfde week.</p>
<p>Twee weken later doe je niets meer.</p>
<p>Beter: één of twee dingen, drie maanden volhouden. Daarna iets toevoegen. Geleidelijk uitbouwen verslaat explosief beginnen.</p>

<h2>Wat doe je met die specifieke avonden?</h2>
<p>Sommige avonden voelen extra zwaar. Vrijdag, weekend, de avonden van wedstrijden, de avonden waarop je vroeger gokte.</p>
<p>Vooraf plannen helpt:</p>
<ul>
<li>Vrijdagavond: sport, daarna iets doen met iemand</li>
<li>Zaterdagavond: kookprojectje, of bezoek aan vrienden</li>
<li>Zondagavond: wandeling, dan vroeg naar bed</li>
<li>Wedstrijdavonden: sportschool tijdens de wedstrijd, of bewust niet kijken</li>
</ul>
<p>Het idee: vul de risico-uren met iets actiefs en sociaals. Geen avonden alleen op de bank starend naar het plafond.</p>

<h2>Eén ding tot slot</h2>
<p>Je dagen voelen vandaag misschien lang.</p>
<p>Over een paar maanden voelen ze normaal. Misschien zelfs te kort, omdat je dingen aan het doen bent waar je tijd voor wil.</p>
<p>Dat punt komt niet door erover na te denken. Dat punt komt door dingen te doen, een voor een, dag na dag, ook als ze nu niet voelen alsof ze veel betekenen.</p>
<p>Vanavond. Half negen. Wat doe je?</p>
<p>Iets anders dan toen.</p>"""

related13 = (
    rel("/nl/blog/gokverslaving-en-identiteit","Emotie","Gokverslaving en identiteit: wie ben je zonder de inzet?") +
    rel("/nl/blog/slaapproblemen-stoppen-met-gokken","Tools","Slaapproblemen na stoppen met gokken") +
    rel("/nl/blog/eerste-week-stoppen-met-gokken","Herstel","Je eerste week stoppen met gokken: dag voor dag")
)

html13 = page(
    "nl",
    "Hoe vul je je tijd zonder gokken? Concrete ideeën | Afterbetting",
    "Hoe vul je je tijd zonder gokken? De leegte na stoppen is reëel. Concrete ideeën zonder zweverigheid om je dagen op te bouwen.",
    url13,
    [("nl","https://afterbetting.com/nl/blog/hoe-vul-ik-mijn-tijd-zonder-gokken"),("x-default","https://afterbetting.com/nl/blog/hoe-vul-ik-mijn-tijd-zonder-gokken")],
    [schema13_article, schema13_bc],
    hero13, body13, related13,
    "Wil je je nieuwe gewoonten en je streak op één plek bijhouden?",
    "Op Afterbetting gebruik je een dagelijkse check-in, gewoonten tracker en journaal om je dagen vorm te geven. Begin gratis."
)

with open("nl/blog/hoe-vul-ik-mijn-tijd-zonder-gokken.html","w",encoding="utf-8") as f:
    f.write(html13)
print("OK: hoe-vul-ik-mijn-tijd-zonder-gokken.html")
print("Alle batch 4 bestanden gegenereerd.")
