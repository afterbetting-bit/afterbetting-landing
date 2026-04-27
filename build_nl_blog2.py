import os, json

os.makedirs("nl/blog", exist_ok=True)

CSS = """*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}:root{--clay:#C4785A;--clay-light:#E8C4B2;--clay-bg:#FBF3EE;--dark:#2C2420;--mid:#5C4A42;--muted:#9E8E86;--cream:#FFFCFA;--warm:#F7F0EA;--border:#E8DDD6;--green:#7A9E8E;--green-bg:#EEF5F2;--green-border:#C2D8D0}html{scroll-behavior:smooth}body{font-family:"DM Sans",sans-serif;background:var(--cream);color:var(--dark);line-height:1.6;-webkit-font-smoothing:antialiased}nav{position:sticky;top:0;z-index:100;background:#fff;border-bottom:1px solid var(--border);padding:1.25rem 2rem;display:flex;align-items:center;justify-content:space-between}.logo{font-family:"Fraunces",serif;font-size:1.4rem;font-weight:300;color:var(--dark);text-decoration:none}.logo span{color:var(--clay)}.nav-links{display:flex;gap:1.5rem;align-items:center}.nav-links a{font-size:.875rem;color:var(--mid);text-decoration:none}.btn{background:var(--clay);color:#fff;padding:.6rem 1.4rem;border-radius:100px;font-size:.875rem;font-weight:500;text-decoration:none;font-family:"DM Sans",sans-serif;display:inline-block}.hero{background:var(--warm);border-bottom:1px solid var(--border);padding:4rem 2rem}.hero-inner{max-width:760px;margin:0 auto}.bc{font-size:.78rem;color:var(--muted);margin-bottom:1.5rem}.bc a{color:var(--clay);text-decoration:none}.tag{display:inline-block;background:var(--green-bg);color:var(--green);font-size:.75rem;font-weight:500;padding:.25rem .75rem;border-radius:100px;border:1px solid var(--green-border);margin-bottom:1rem}h1{font-family:"Fraunces",serif;font-size:2.8rem;line-height:1.15;font-weight:300;color:var(--dark);margin-bottom:1rem;letter-spacing:-.02em}.meta{font-size:.82rem;color:var(--muted);margin-top:1rem}.body{max-width:760px;margin:0 auto;padding:3rem 2rem}.body h2{font-family:"Fraunces",serif;font-size:1.7rem;font-weight:300;color:var(--dark);margin:2.5rem 0 1rem;line-height:1.2}.body p{font-size:1rem;color:var(--mid);line-height:1.8;margin-bottom:1.25rem;font-weight:300}.body ul,.body ol{margin:1rem 0 1.5rem 1.5rem}.body li{font-size:1rem;color:var(--mid);line-height:1.8;margin-bottom:.5rem;font-weight:300}.body strong{color:var(--dark);font-weight:500}.body a{color:var(--clay);text-decoration:underline;text-underline-offset:3px}.body table{width:100%;border-collapse:collapse;margin:1.5rem 0;font-size:.9rem}.body th{background:var(--warm);color:var(--dark);font-weight:500;padding:.6rem 1rem;border:1px solid var(--border);text-align:left}.body td{padding:.6rem 1rem;border:1px solid var(--border);color:var(--mid);font-weight:300}.callout{background:var(--clay-bg);border:1px solid var(--clay-light);border-radius:14px;padding:1.5rem;margin:2rem 0}.callout p{margin:0;color:var(--mid)}.cta-block{background:var(--dark);border-radius:16px;padding:2.5rem;margin:3rem 0;text-align:center}.cta-block h3{font-family:"Fraunces",serif;font-size:1.5rem;font-weight:300;color:#fff;margin-bottom:.5rem}.cta-block p{color:rgba(255,255,255,.6);font-size:.9rem;margin-bottom:1.5rem}.cta-block a{background:var(--clay);color:#fff;padding:.75rem 2rem;border-radius:100px;text-decoration:none;font-weight:500;font-size:.9rem;display:inline-block}.related{background:var(--warm);border-top:1px solid var(--border);padding:3rem 2rem}.rel-inner{max-width:760px;margin:0 auto}.related h3{font-family:"Fraunces",serif;font-size:1.3rem;font-weight:300;color:var(--dark);margin-bottom:1.5rem}.rel-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:1rem}.rel-card{background:#fff;border:1px solid var(--border);border-radius:12px;padding:1.25rem;text-decoration:none;display:block}.rel-card:hover{border-color:var(--clay)}.rel-card .t{font-size:.72rem;color:var(--green);font-weight:500;text-transform:uppercase;letter-spacing:.06em;margin-bottom:.5rem}.rel-card h4{font-family:"Fraunces",serif;font-size:1rem;font-weight:400;color:var(--dark);line-height:1.3}.crisis-footer{background:var(--clay-bg);border-top:1px solid var(--clay-light);padding:1.25rem 2rem;text-align:center}.crisis-footer p{font-size:.88rem;color:var(--dark);font-weight:400}.crisis-footer strong{color:var(--clay)}footer{background:var(--dark);color:#fff;padding:2rem;text-align:center}footer p{font-size:.8rem;color:rgba(255,255,255,.3)}footer a{color:var(--clay);text-decoration:none;margin:0 .5rem}@media(max-width:768px){nav .nav-links{display:none}h1{font-size:2rem}.hero{padding:2.5rem 1.25rem}.body{padding:2rem 1.25rem}.rel-grid{grid-template-columns:1fr}.body table{font-size:.8rem}.body th,.body td{padding:.4rem .6rem}}"""

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

# ── ARTIKEL 5: gokschuld-aflossen ────────────────────────────────────────────

slug5 = "gokschuld-aflossen"
url5  = f"https://afterbetting.com/nl/blog/{slug5}"

schema5_article = json.dumps({"@context":"https://schema.org","@type":"Article","headline":"Gokschuld aflossen. Een eerlijk plan zonder paniek.","author":{"@type":"Organization","name":"Afterbetting"},"publisher":{"@type":"Organization","name":"Afterbetting","url":"https://afterbetting.com"},"datePublished":"2026-04-26","dateModified":"2026-04-26","inLanguage":"nl","url":url5})
schema5_bc = json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://afterbetting.com/nl/"},{"@type":"ListItem","position":2,"name":"Blog","item":"https://afterbetting.com/nl/blog"},{"@type":"ListItem","position":3,"name":"Gokschuld aflossen: een eerlijk plan zonder paniek","item":url5}]})

hero5 = '''<section class="hero"><div class="hero-inner">
<div class="bc"><a href="/nl/">Home</a> &rarr; <a href="/nl/blog">Blog</a> &rarr; Geld &amp; schulden</div>
<div class="tag">Geld &amp; schulden</div>
<h1>Gokschuld aflossen. Een eerlijk plan zonder paniek.</h1>
<p style="font-size:1.1rem;color:var(--mid);font-weight:300;line-height:1.7;margin-top:1rem">Gokschuld aflossen voelt onmogelijk. Het is het niet. Een eerlijk stappenplan voor wie wil beginnen, zonder paniekvoetbal.</p>
<div class="meta">Door Afterbetting &middot; 26 april 2026 &middot; 8 min lezen</div>
</div></section>'''

body5 = """<p>Je weet niet meer hoeveel.</p>
<p>Of je weet het wel, en daarom slaap je slecht.</p>
<p>De brieven liggen in een la die je niet meer opent. De app van je bank meldt je in het rood. Misschien sta je bij vrienden of familie in het krijt. Misschien bij een instantie. Misschien bij allebei.</p>
<p>En het ergste: je weet niet hoe je hieruit komt.</p>
<p>Even iets duidelijks. Je komt hieruit. Niet morgen. Niet binnen drie maanden misschien. Maar wel. Mensen met grotere schulden dan jij hebben dit ook gedaan. Stap voor stap. Zonder magie.</p>
<p>Dit artikel geeft je een plan. Geen sprookje. Een plan.</p>

<h2>Eerst dit. Voordat je begint met aflossen.</h2>
<p>Voordat je ook maar één euro aflost, moet je dit op orde hebben. Anders gaat het mis.</p>
<p><strong>Eén: stop met gokken.</strong></p>
<p>Klinkt logisch. Wordt vaak overgeslagen. Mensen beginnen met aflossen terwijl ze nog gokken. Dan vul je een lekke band met lucht en vraag je je af waarom hij steeds plat staat.</p>
<p>Sluit jezelf in via Cruks (cruks.nl). Bel je bank voor een gokblokkade. Verwijder elke gok-app van je telefoon. Vandaag.</p>
<p>Lees ook: <a href="/nl/blog/stoppen-met-gokken">Stoppen met gokken: een eerlijke gids</a></p>
<p><strong>Twee: krijg overzicht.</strong></p>
<p>Eén pagina. Eén overzicht. Alles erop.</p>
<p>Bij wie heb je schuld. Hoeveel. Welke rente. Welke datum betalen.</p>
<p>Dat overzicht is de moeilijkste pagina die je ooit zult maken. Het kost je twee uur. Misschien een hele avond. En het voelt afschuwelijk.</p>
<p>Maar zonder dat overzicht ben je een dokter zonder diagnose. Doe het.</p>
<p><strong>Drie: praat met iemand.</strong></p>
<p>Een partner. Een ouder. Een vriend met financieel overzicht. Of iemand van het Maatschappelijk Werk in je gemeente. Veel gemeenten hebben gratis schuldhulpverlening (zie nvvk.nl).</p>
<p>Schaamte over schulden is begrijpelijk. En het houdt je vast. Eén eerlijk gesprek geeft lucht. Twee geven richting.</p>

<h2>Hoeveel kun je afbetalen per maand? Wees eerlijk.</h2>
<p>Pak je inkomen.</p>
<p>Trek af: huur, verzekeringen, energie, eten, vervoer. De vaste lasten. Niet meer.</p>
<p>Wat overblijft, is wat je theoretisch kunt aflossen. Maar wees eerlijk: je hebt ook nieuwe kleren nodig op een gegeven moment. Een verjaardag. Een keer een terras. Anders hou je het niet vol.</p>
<p>Vuistregel: tel ongeveer 100 tot 150 euro per maand mee voor onverwachte dingen, en gebruik de rest voor schulden.</p>
<p>Voor wie niet rekent: bij 200 euro per maand los je 2.400 per jaar af. Bij 400 euro per maand 4.800. Het lijkt klein. Het stapelt op.</p>

<h2>Welke schuld eerst? Twee benaderingen.</h2>
<p>Hier komt de strategie. Er zijn grofweg twee manieren.</p>
<p><strong>Methode A: hoogste rente eerst (avalanche)</strong></p>
<p>Wiskundig de slimste. Je betaalt minimaal op alle schulden, en gooit alle extra ruimte op de schuld met de hoogste rente. Pas als die afgelost is, ga je naar de volgende.</p>
<p>Voordeel: je betaalt het minste totale bedrag. Nadeel: je ziet pas resultaat als de eerste schuld weg is. Dat kan lang duren.</p>
<p><strong>Methode B: kleinste schuld eerst (sneeuwbal)</strong></p>
<p>Je begint met de kleinste schuld. Maakt die zo snel mogelijk af. Voelt de overwinning. Pakt de volgende.</p>
<p>Voordeel: motivatie. Je ziet schulden verdwijnen. Nadeel: je betaalt iets meer rente in totaal.</p>
<p>Welke is beter? Voor mensen die uit gokverslaving komen: meestal de sneeuwbalmethode. Omdat je hersenen pieken nodig hebben. Een schuld zien verdwijnen is een legale, gezonde piek.</p>
<p>Lees ook: <a href="/nl/blog/sneeuwbalmethode-gokschulden">Schulden aflossen met de sneeuwbalmethode na gokverslaving</a></p>

<h2>Wat als ik dit echt niet alleen kan?</h2>
<p>Eerlijk antwoord: dan ben je in goed gezelschap.</p>
<p>In Nederland heeft 1 op de 5 huishoudens te maken met problematische schulden. Daar zijn structuren voor. Gratis. Officieel. Geen oplichters.</p>
<p><strong>Schuldhulpverlening via je gemeente.</strong></p>
<p>Elke gemeente moet wettelijk schuldhulpverlening aanbieden. Gratis. Bel je gemeente, vraag naar het sociaal team of de schuldhulpverlening. Ze helpen je een betalingsregeling opzetten met al je schuldeisers, soms met kwijtschelding.</p>
<p><strong>WSNP (Wet schuldsanering natuurlijke personen).</strong></p>
<p>Voor zwaardere gevallen. Drie jaar leven van een minimumbedrag, daarna ben je schuldenvrij. Streng, maar werkt. Je gemeente kan je hierin begeleiden.</p>
<p><strong>Nibud, NVVK, Geldfit.</strong></p>
<p>Praktische hulp en gratis advies online. Geldfit.nl heeft een geldcoach. Niet zweverig. Wel concreet.</p>
<p>Schuldhulp aanvragen voelt als opgeven. Het is het tegenovergestelde. Het is verantwoordelijkheid nemen. Op de meest volwassen manier die er is.</p>

<h2>De fout die bijna iedereen maakt</h2>
<p>Hier komt de val.</p>
<p>Als je een paar maanden goed bezig bent, schulden aflost, en het gaat lekker, krijg je een gedachte: "Eén keer gokken, ik weet hoe het werkt nu, één snelle winst en ik los meteen vijfduizend af."</p>
<p>Dat. Doet. Niemand.</p>
<p>Niet één persoon in de geschiedenis van gokverslavingen heeft ooit "één keer gegokt om snel schulden af te lossen" en het laten lukken. Nul. Niemand.</p>
<p>Wat er gebeurt: je verliest. Je probeert terug te winnen. Je verliest meer. Je staat dieper in de schulden dan toen je begon. En dan moet je opnieuw beginnen, alleen nu met meer schulden en minder vertrouwen in jezelf.</p>
<p>Bouw die deur dicht. Hou hem dicht.</p>

<h2>Wat het oplevert. Niet alleen geld.</h2>
<p>Schulden aflossen is niet alleen wiskunde.</p>
<p>Eerste maand: je voelt opluchting. De brieven worden minder eng. Je opent ze.</p>
<p>Drie maanden: je begint te merken dat je rustiger slaapt. Niet perfect. Wel beter.</p>
<p>Zes maanden: je hebt iets afbetaald. Echt afbetaald. Iemand belt je niet meer. Een rekening is dicht. Dat is een gevoel dat geen casino je ooit kan geven.</p>
<p>Een jaar: je weet weer wat er op je rekening staat. Op de cent. En je kijkt er niet meer van weg.</p>
<p>Twee jaar: misschien ben je grotendeels schuldenvrij, misschien nog niet. Maar je weet nu één ding zeker: je kunt dit. Je doet dit.</p>
<p>Dat is wat het oplevert. Niet alleen een lege schuld. Een nieuwe relatie met geld. En met jezelf.</p>

<h2>Begin vandaag. Eén pagina.</h2>
<p>Niet morgen. Vandaag.</p>
<p>Pak een blanco pagina. Schrijf bovenaan: "Mijn schulden, eerlijk."</p>
<p>Schrijf alles op. Bij wie. Hoeveel. Rente. Datum.</p>
<p>Eén pagina. Eén uur. Daarna weet je waar je staat.</p>
<p>Dat is dag 1 van aflossen. Verder hoeft het niet te zijn.</p>"""

related5 = (
    rel("/nl/blog/sneeuwbalmethode-gokschulden","Geld & schulden","Schulden aflossen met de sneeuwbalmethode na gokverslaving") +
    rel("/nl/blog/hoe-stop-ik-met-gokken-met-schulden","Geld & schulden","Hoe stop ik met gokken als ik in de schulden zit?") +
    rel("/nl/blog/stoppen-met-gokken","Herstel","Stoppen met gokken: een eerlijke gids")
)

html5 = page(
    "nl",
    "Gokschuld aflossen: een eerlijk plan zonder paniek | Afterbetting",
    "Gokschuld aflossen voelt onmogelijk. Het is het niet. Een eerlijk stappenplan voor wie wil beginnen, zonder paniekvoetbal.",
    url5,
    [("nl","https://afterbetting.com/nl/blog/gokschuld-aflossen"),("x-default","https://afterbetting.com/nl/blog/gokschuld-aflossen")],
    [schema5_article, schema5_bc],
    hero5, body5, related5,
    "Wil je je aflossing zichtbaar maken naast je streak?",
    "Het financieel dashboard van Afterbetting laat je zien wat je terugwint, week voor week. Begin gratis."
)

with open("nl/blog/gokschuld-aflossen.html","w",encoding="utf-8") as f:
    f.write(html5)
print("OK: gokschuld-aflossen.html")

# ── ARTIKEL 6: sneeuwbalmethode-gokschulden ──────────────────────────────────

slug6 = "sneeuwbalmethode-gokschulden"
url6  = f"https://afterbetting.com/nl/blog/{slug6}"

schema6_article = json.dumps({"@context":"https://schema.org","@type":"Article","headline":"Schulden aflossen met de sneeuwbalmethode na gokverslaving.","author":{"@type":"Organization","name":"Afterbetting"},"publisher":{"@type":"Organization","name":"Afterbetting","url":"https://afterbetting.com"},"datePublished":"2026-04-26","dateModified":"2026-04-26","inLanguage":"nl","url":url6})
schema6_bc = json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://afterbetting.com/nl/"},{"@type":"ListItem","position":2,"name":"Blog","item":"https://afterbetting.com/nl/blog"},{"@type":"ListItem","position":3,"name":"Sneeuwbalmethode bij gokschulden","item":url6}]})

hero6 = '''<section class="hero"><div class="hero-inner">
<div class="bc"><a href="/nl/">Home</a> &rarr; <a href="/nl/blog">Blog</a> &rarr; Geld &amp; schulden</div>
<div class="tag">Geld &amp; schulden</div>
<h1>Schulden aflossen met de sneeuwbalmethode na gokverslaving.</h1>
<p style="font-size:1.1rem;color:var(--mid);font-weight:300;line-height:1.7;margin-top:1rem">Waarom kleine schulden eerst werkt, met rekenvoorbeeld en valkuilen. Speciaal voor wie uit gokverslaving komt.</p>
<div class="meta">Door Afterbetting &middot; 26 april 2026 &middot; 7 min lezen</div>
</div></section>'''

body6 = """<p>Je hebt schulden. Meer dan één. Verspreid over creditcards, BKR, vrienden, familie, misschien een instantie of twee.</p>
<p>Je weet niet waar te beginnen.</p>
<p>Je hebt online gezocht en bent twee dingen tegengekomen: de avalanche-methode en de sneeuwbalmethode. Wiskundigen zeggen avalanche. Mensen die er doorheen zijn gekomen, zeggen meestal sneeuwbal.</p>
<p>Voor iemand die uit gokverslaving komt: dit artikel legt uit waarom de sneeuwbalmethode bijna altijd beter werkt dan de wiskundig optimale variant. En hoe je hem opzet.</p>

<h2>Wat is de sneeuwbalmethode?</h2>
<p>Simpel principe.</p>
<p>Je zet al je schulden op een rij van klein naar groot.</p>
<p>Op alle schulden betaal je het minimum. Behalve op de kleinste. Die gooi je dicht zo snel je kunt.</p>
<p>Zodra de kleinste weg is, neem je het bedrag dat je aan die kleinste betaalde, en voeg je het toe aan wat je op de volgende kleinste betaalt. Die schuld smelt nu sneller.</p>
<p>Als die ook weg is, voeg je beide bedragen toe aan de derde. Enzovoorts.</p>
<p>Het bedrag dat je aflost wordt elke keer groter. Als een sneeuwbal die naar beneden rolt. Vandaar de naam.</p>

<h2>Een rekenvoorbeeld. Concreet.</h2>
<p>Stel je hebt de volgende schulden:</p>
<table>
<tr><th>Schuld</th><th>Bedrag</th><th>Rente</th><th>Min. betaling</th></tr>
<tr><td>Vriendenlening</td><td>&euro;800</td><td>0%</td><td>&euro;50</td></tr>
<tr><td>Creditcard</td><td>&euro;1.500</td><td>14%</td><td>&euro;75</td></tr>
<tr><td>BKR consumptief</td><td>&euro;4.200</td><td>9%</td><td>&euro;120</td></tr>
<tr><td>Persoonlijke lening</td><td>&euro;6.000</td><td>6%</td><td>&euro;110</td></tr>
</table>
<p>Totaal: 12.500 euro schuld. Je hebt 500 euro per maand om af te lossen.</p>
<p>Bij minimum betalingen ben je 355 euro kwijt. Je hebt dus 145 euro extra te besteden.</p>
<p><strong>Sneeuwbal-aanpak:</strong></p>
<p>Maand 1 tot 5: 50 minimum plus 145 extra op vriendenlening = 195 per maand. Schuld vrienden weg in maand 5.</p>
<p>Maand 5 verder: nu heb je 195 vrij. Je gooit dat boven op de creditcard. Daar betaalde je 75. Nu 270. Schuld weg rond maand 11.</p>
<p>Maand 11 verder: nu heb je 270 plus 75 = 345 vrij. Bovenop BKR. Daar betaalde je 120. Nu 465. Schuld weg rond maand 21.</p>
<p>Maand 21 verder: alles vrij voor persoonlijke lening. 465 plus 120 = 585 per maand. Schuld weg rond maand 30.</p>
<p>In ongeveer 30 maanden, tweeënhalf jaar, ben je schuldenvrij. Met 500 euro per maand. Dat is doenlijk.</p>

<h2>Waarom dit werkt voor wie uit gokken komt</h2>
<p>Hier is het belangrijke deel.</p>
<p>Een gokker is iemand die ervaring heeft met dopaminepieken. Kortetermijnbeloningen. Variabele schokjes van geluk.</p>
<p>Wat gokken in je hersenen heeft achtergelaten, verdwijnt niet zomaar. Je systeem zoekt nog steeds pieken. Niet omdat je zwak bent. Omdat dat is hoe je brein werkt.</p>
<p>De sneeuwbalmethode geeft je legale, gezonde pieken. Elke keer dat een schuld dicht gaat, is dat een echte overwinning. Een schouderklop voor je hersenen. Een dopamineshot die niets kost en alles oplevert.</p>
<p>De avalanche-methode (hoogste rente eerst) bespaart je een paar honderd euro op tweeënhalf jaar. Maar het kan zijn dat je je grootste schuld eerst aanpakt. Dan duurt het twee jaar voordat je je eerste overwinning ziet.</p>
<p>Vraag jezelf: kun je twee jaar elke maand 500 euro afdragen zonder enig zichtbaar resultaat?</p>
<p>Eerlijk antwoord van bijna iedereen: nee.</p>
<p>De sneeuwbalmethode kost een paar honderd euro extra. Levert je een veel betere kans om hem ook af te maken. Dat is een goede ruil.</p>

<h2>Vier valkuilen om te vermijden</h2>
<p><strong>Valkuil 1: nieuwe schuld bovenop oude.</strong></p>
<p>Dit is de grootste. Mensen lossen af met de ene hand en lenen met de andere. Of ze missen een betaling en tellen de boete niet mee.</p>
<p>Niet doen. Eén keer per maand check je elke rekening. Geen verrassingen.</p>
<p><strong>Valkuil 2: alle spaargeld naar schulden.</strong></p>
<p>Klinkt slim. Werkt zelden.</p>
<p>Hou een buffer. 500 tot 1.000 euro op een aparte rekening. Voor pech. Auto kapot. Tand kapot. Wasmachine kapot.</p>
<p>Zonder buffer leen je bij de eerste tegenslag. Met buffer betaal je het en gaat de aflossing door.</p>
<p><strong>Valkuil 3: te streng zijn.</strong></p>
<p>Je hebt jaren gegokt. Je hebt mensen pijn gedaan. Je hebt jezelf pijn gedaan.</p>
<p>Nu wil je het goedmaken door alle wakkere uren strak te budgetteren en jezelf elk uitje te ontzeggen.</p>
<p>Dat houdt niemand vol. Je explodeert binnen twee maanden.</p>
<p>Plan kleine uitjes. Een terrasje. Een film. Een kerst zonder paniek. Vraag tien procent van je beschikbare budget terug voor menselijke dingen.</p>
<p><strong>Valkuil 4: vergelijken met anderen.</strong></p>
<p>Je vriend kocht een huis. Je broer reed een nieuwe auto. Jij bent 32 en lost schulden af.</p>
<p>Niet vergelijken. Iedereen heeft zijn eigen tempo en zijn eigen verhaal. Jouw verhaal is dit nu. En over vijf jaar ziet jouw verhaal er anders uit.</p>

<h2>Begin met je sneeuwbal vandaag</h2>
<p>Pak een pagina.</p>
<p>Schrijf erop:</p>
<ol>
<li>Al je schulden, klein naar groot</li>
<li>Rente per stuk</li>
<li>Minimum betaling per stuk</li>
<li>Hoeveel je per maand kunt missen</li>
</ol>
<p>Reken uit hoeveel extra je hebt na de minima.</p>
<p>Gooi dat extra bedrag op de kleinste schuld. Vandaag, of bij de eerstvolgende loonbetaling.</p>
<p>Een sneeuwbal begint klein. En rolt door.</p>"""

related6 = (
    rel("/nl/blog/gokschuld-aflossen","Geld & schulden","Gokschuld aflossen: een eerlijk plan zonder paniek") +
    rel("/nl/blog/hoe-stop-ik-met-gokken-met-schulden","Geld & schulden","Hoe stop ik met gokken als ik in de schulden zit?") +
    rel("/nl/blog/stoppen-met-gokken","Herstel","Stoppen met gokken: een eerlijke gids")
)

html6 = page(
    "nl",
    "Sneeuwbalmethode bij gokschulden: zo werkt het | Afterbetting",
    "Schulden aflossen met de sneeuwbalmethode na gokken. Waarom kleine schulden eerst werkt, met rekenvoorbeeld en valkuilen.",
    url6,
    [("nl","https://afterbetting.com/nl/blog/sneeuwbalmethode-gokschulden"),("x-default","https://afterbetting.com/nl/blog/sneeuwbalmethode-gokschulden")],
    [schema6_article, schema6_bc],
    hero6, body6, related6,
    "Wil je elke afgeloste schuld zien naast je streak?",
    "Op Afterbetting volg je je financiële voortgang en je dagen-zonder-gokken in één dashboard. Twee soorten winst, één plek."
)

with open("nl/blog/sneeuwbalmethode-gokschulden.html","w",encoding="utf-8") as f:
    f.write(html6)
print("OK: sneeuwbalmethode-gokschulden.html")

# ── ARTIKEL 7: hoe-stop-ik-met-gokken-met-schulden ───────────────────────────

slug7 = "hoe-stop-ik-met-gokken-met-schulden"
url7  = f"https://afterbetting.com/nl/blog/{slug7}"

schema7_article = json.dumps({"@context":"https://schema.org","@type":"Article","headline":"Hoe stop ik met gokken als ik in de schulden zit?","author":{"@type":"Organization","name":"Afterbetting"},"publisher":{"@type":"Organization","name":"Afterbetting","url":"https://afterbetting.com"},"datePublished":"2026-04-26","dateModified":"2026-04-26","inLanguage":"nl","url":url7})
schema7_bc = json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://afterbetting.com/nl/"},{"@type":"ListItem","position":2,"name":"Blog","item":"https://afterbetting.com/nl/blog"},{"@type":"ListItem","position":3,"name":"Hoe stop ik met gokken als ik in de schulden zit?","item":url7}]})

hero7 = '''<section class="hero"><div class="hero-inner">
<div class="bc"><a href="/nl/">Home</a> &rarr; <a href="/nl/blog">Blog</a> &rarr; Geld &amp; schulden</div>
<div class="tag">Geld &amp; schulden</div>
<h1>Hoe stop ik met gokken als ik in de schulden zit?</h1>
<p style="font-size:1.1rem;color:var(--mid);font-weight:300;line-height:1.7;margin-top:1rem">Het paradoxale antwoord, en wat wel werkt. Geen tien tips, wel echt advies voor wie vastloopt.</p>
<div class="meta">Door Afterbetting &middot; 26 april 2026 &middot; 8 min lezen</div>
</div></section>'''

body7 = """<p>Hier is het paradoxale.</p>
<p>Je wil stoppen met gokken. Maar je hebt schulden. Grote schulden. En in je hoofd zit één gedachte vastgeplakt: als ik nu stop, hoe los ik dit ooit af?</p>
<p>Die gedachte heeft je tot nu toe in het systeem gehouden. "Nog één keer winnen, en ik ben er vanaf." Je weet inmiddels hoe dat verhaal afloopt.</p>
<p>Toch is de vraag terecht. Hoe stop je met gokken als de oorzaak van je stopwens, je schulden, juist is wat je heeft doen denken dat je niet kunt stoppen?</p>
<p>Dit artikel geeft het eerlijke antwoord. En het stappenplan dat erbij hoort.</p>

<h2>De paradox uitgelegd</h2>
<p>Eerst rechtzetten wat in je hoofd zit.</p>
<p>Gokken om schulden af te lossen werkt nooit. Niet omdat je pech hebt. Omdat de wiskunde niet meewerkt.</p>
<p>Een gemiddeld online casino heeft een huisvoordeel van 2 tot 15 procent. Sportgokken zit rond de 5 tot 10 procent. Dat betekent: van elke honderd euro die je inzet, krijg je gemiddeld 85 tot 98 euro terug. Op de lange termijn. Wiskundig gegarandeerd.</p>
<p>Hoe meer je gokt, hoe dichter je gemiddelde tegen die getallen aankomt. Dit heet de wet van de grote getallen. Hij weet niet wie je bent. Hij heeft geen mening over jou. Hij geldt voor iedereen.</p>
<p>Dus wat is de eerlijke conclusie?</p>
<p>Doorgaan met gokken vergroot je schuld. Stoppen met gokken stopt het bloeden. Stoppen is niet de tegenstander van schuld aflossen. Stoppen is de eerste stap.</p>

<h2>Stap 1. Stop met het lek</h2>
<p>Voordat je iets afbetaalt, dicht je het lek.</p>
<p>Een emmer met een gat erin vullen heeft geen zin. Je dicht eerst het gat.</p>
<p>Vandaag, niet morgen:</p>
<p><strong>Cruks aanmelden</strong> (cruks.nl). Tien minuten online. Je staat dan automatisch op de uitsluitingslijst voor alle Nederlandse legale online casino's en speelhallen. Geen toegang.</p>
<p><strong>Gokblokkade bij je bank.</strong> Bel ze. ABN, ING, Rabobank, Bunq, allemaal. Vraag of ze betalingen naar gokwebsites kunnen blokkeren. De meeste banken kunnen dit.</p>
<p><strong>Apps weg.</strong> Elke gok-app van je telefoon. Elke bookmaker-bookmark uit je browser. Elke reclame-mail van een casino uitschrijven of als spam markeren.</p>
<p><strong>Bewaar je betaalgegevens niet meer online bij gokdiensten.</strong> Niet bij PayPal, niet bij Apple Pay voor sites die gokken faciliteren. Wrijving toevoegen helpt.</p>

<h2>Stap 2. Bel iemand die je kan helpen</h2>
<p>Twee soorten mensen.</p>
<p><strong>Eén voor het gokken.</strong> Een huisarts. De Nationale Hulplijn Gokken (<strong>0800-1995</strong>, gratis, anoniem, 24/7). Of een aanmelding bij Jellinek of Tactus voor verslavingszorg.</p>
<p><strong>Eén voor het geld.</strong> Je gemeente, voor schuldhulpverlening. NVVK.nl voor erkende schuldhulpverleners. Geldfit.nl voor een geldcoach. Soms je werkgever, want veel werkgevers hebben tegenwoordig een vertrouwenspersoon of regeling voor financiële problemen.</p>
<p>Beide gesprekken zijn moeilijk. Beide gesprekken halen je vooruit.</p>
<p>Probeer ze allebei deze week te voeren. Niet allebei vandaag, dat is te zwaar. Wel deze week.</p>

<h2>Stap 3. Krijg overzicht. Twee lijsten.</h2>
<p>Pak twee lege pagina's.</p>
<p><strong>Pagina 1: alles wat je gokt of dreigt te gokken.</strong></p>
<p>Welke triggers? Welke momenten van de week zijn risicovol? Welke gevoelens drijven je naar het gokken? Wie zijn de mensen die je niet meer ziet omdat je liever gokt? Welke smoesjes vertel je jezelf?</p>
<p>Dit is geen oefening voor de mooie show. Dit is de spiegel.</p>
<p><strong>Pagina 2: alles wat je schuldig bent.</strong></p>
<p>Bij wie. Hoeveel. Rente. Datum.</p>
<p>Vergeet de boetes niet. Vergeet de openstaande facturen niet. Vergeet de vriend die je honderd euro leende drie maanden geleden niet.</p>
<p>Twee pagina's. Twee uur werk. Daarna weet je waar je staat. Op beide fronten.</p>
<p>Lees ook: <a href="/nl/blog/gokschuld-aflossen">Gokschuld aflossen: een eerlijk plan zonder paniek</a></p>

<h2>Stap 4. Bouw structuur. Niet wilskracht.</h2>
<p>Hier is iets wat veel mensen verkeerd begrijpen.</p>
<p>Stoppen met gokken is geen wilskracht-test. Wilskracht raakt op. Iedereen heeft slechte dagen. Op een slechte dag wint je verslaving van je wilskracht. Elke keer.</p>
<p>Wat wel werkt: structuur die niet afhankelijk is van wilskracht.</p>
<p><strong>Een dagelijkse routine.</strong> Vaste tijden voor opstaan, eten, sporten, slapen. Saai is goed. Saai is veilig.</p>
<p><strong>Vervangen wat je vroeger met gokken deed.</strong> Het uur na het avondeten dat je voorheen besteedde aan online casino? Vul het in. Wandelen, lezen, sporten, klussen, bellen, koken. Wat dan ook.</p>
<p><strong>Een check-in elke dag.</strong> Eén minuut. Hoe ging vandaag? Wat was zwaar? Wat was goed? Vijf regels schrijven of in een app bijhouden.</p>
<p><strong>Iemand die meeleest.</strong> Een sponsor uit een twaalfstappenprogramma (Anonieme Gokkers heeft groepen in Nederland), een therapeut, een vertrouwd persoon. Geen oordeel, wel oog.</p>

<h2>Stap 5. Tegelijk aflossen, in een tempo dat je volhoudt</h2>
<p>Hier komt de combinatie.</p>
<p>Je gokt niet meer. Goed. Daardoor bespaar je geld. Goed.</p>
<p>Wat doe je met dat bespaarde geld?</p>
<p>Niet alles op de eerste schuld. Hou een kleine buffer. Zet de rest in op je kleinste schuld eerst.</p>
<p>Niet alles in één keer. Maand voor maand. Zoals je nu één dag tegelijk niet gokt, los je één maand tegelijk een beetje af.</p>
<p>Eén jaar verder ben je een aantal duizenden euro's afgekomen, en je hebt 365 dagen niet gegokt. Twee winsten tegelijk.</p>

<h2>Wat als de drang terugkomt? En hij komt terug.</h2>
<p>Dat hij terugkomt, is een gegeven.</p>
<p>Hoe je ermee omgaat, bepaalt het verschil.</p>
<p><strong>Erken hem.</strong> Niet wegduwen. Erkennen. "Ik voel nu een sterke drang om te gokken." Hardop of in je hoofd. Naam geven aan iets neemt de helft van zijn macht weg.</p>
<p><strong>Wacht 30 minuten.</strong> Cravings duren tussen 5 en 30 minuten als je ze niet voedt. Verander van omgeving. Loop. Bel iemand. Drink water. De golf komt op, piekt, en zakt.</p>
<p><strong>Bel als het nodig is.</strong> <strong>0800-1995</strong>, Nationale Hulplijn Gokken. Anoniem. Geen oordeel.</p>
<p><strong>Stuur jezelf niet de afgrond in.</strong> Een terugval is niet het einde. Het is informatie. Wat ging er aan vooraf? Welke trigger was er? Wat had je anders kunnen doen?</p>

<h2>Het gevoel dat je zoekt</h2>
<p>Hier komt het laatste eerlijke punt.</p>
<p>Je dacht jarenlang dat de winst je het gevoel zou geven dat je zocht. Vrijheid. Erkenning. Rust.</p>
<p>Klopt niet. De winst gaf je een korte piek en daarna een nieuw verlangen.</p>
<p>Het gevoel dat je echt zoekt, is iets anders. Het is het gevoel van een mens die zijn leven op orde heeft. Eerlijk tegen zichzelf en anderen. Met overzicht. Met rust.</p>
<p>Dat gevoel komt niet van een grote winst. Het komt van een lange reeks kleine, eerlijke beslissingen. Vandaag niet gokken. Vandaag een aflossing doen. Vandaag een lastig gesprek voeren. Vandaag iemand bellen die op je rekent.</p>
<p>Dat is het echte werk. En het echte werk levert het echte gevoel op.</p>"""

related7 = (
    rel("/nl/blog/gokschuld-aflossen","Geld & schulden","Gokschuld aflossen: een eerlijk plan zonder paniek") +
    rel("/nl/blog/sneeuwbalmethode-gokschulden","Geld & schulden","Schulden aflossen met de sneeuwbalmethode") +
    rel("/nl/blog/stoppen-met-gokken","Herstel","Stoppen met gokken: een eerlijke gids")
)

html7 = page(
    "nl",
    "Hoe stop ik met gokken met schulden? Eerlijk antwoord | Afterbetting",
    "Hoe stop ik met gokken als ik diep in de schulden zit? Het paradoxale antwoord, en wat wel werkt. Geen tien tips, wel echt advies.",
    url7,
    [("nl","https://afterbetting.com/nl/blog/hoe-stop-ik-met-gokken-met-schulden"),("x-default","https://afterbetting.com/nl/blog/hoe-stop-ik-met-gokken-met-schulden")],
    [schema7_article, schema7_bc],
    hero7, body7, related7,
    "Wil je je dagen zonder gokken en je financiële voortgang bijhouden?",
    "Streak, journaal, financieel dashboard, crisisknop. Alles op één plek. Begin gratis op Afterbetting."
)

with open("nl/blog/hoe-stop-ik-met-gokken-met-schulden.html","w",encoding="utf-8") as f:
    f.write(html7)
print("OK: hoe-stop-ik-met-gokken-met-schulden.html")
print("Alle batch 2 bestanden gegenereerd.")
