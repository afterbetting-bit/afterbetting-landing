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
<meta property="og:locale:alternate" content="nl_BE"/>
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

# ── ARTIKEL 14: sportgokken-verslaving ───────────────────────────────────────

slug14 = "sportgokken-verslaving"
url14  = f"https://afterbetting.com/nl/blog/{slug14}"

schema14_article = json.dumps({"@context": "https://schema.org", "@type": "Article", "headline": "Sportgokken verslaving. Hoe je hier eerlijk naar kijkt.", "author": {"@type": "Organization", "name": "Afterbetting"}, "publisher": {"@type": "Organization", "name": "Afterbetting", "url": "https://afterbetting.com"}, "datePublished": "2026-04-26", "dateModified": "2026-04-26", "inLanguage": "nl", "url": url14})
schema14_bc = json.dumps({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://afterbetting.com/nl/"}, {"@type": "ListItem", "position": 2, "name": "Blog", "item": "https://afterbetting.com/nl/blog"}, {"@type": "ListItem", "position": 3, "name": "Sportgokken verslaving", "item": url14}]})

hero14 = '''<section class="hero"><div class="hero-inner">
<div class="bc"><a href="/nl/">Home</a> &rarr; <a href="/nl/blog">Blog</a> &rarr; Specifiek</div>
<div class="tag">Specifiek</div>
<h1>Sportgokken verslaving. Hoe je hier eerlijk naar kijkt.</h1>
<p style="font-size:1.1rem;color:var(--mid);font-weight:300;line-height:1.7;margin-top:1rem">Sportgokken verslaving voelt anders dan casino. Waarom dat een illusie is, hoe het werkt en wat helpt om eruit te komen.</p>
<div class="meta">Door Afterbetting &middot; 26 april 2026 &middot; 9 min lezen</div>
</div></section>'''

body14 = """<p>Even iets uitspreken wat in je hoofd zit.</p>
<p>"Sportgokken is anders. Het is geen echt gokken. Ik ken voetbal. Ik weet wat ik doe. Het is meer een hobby met geld erbij dan een verslaving."</p>
<p>Klinkt bekend?</p>
<p>Het is precies wat de hele industrie wil dat je gelooft. Daarom heten ze ook "sportbookmakers" en niet "casino's", al doen ze in essentie hetzelfde. Daarom staan hun logo's op shirts van clubs die je liefhebt. Daarom is er nu een betting-blok bij elke wedstrijdsamenvatting op tv en achter elke voetbal-podcast.</p>
<p>Sportgokken voelt niet als gokken omdat het zo verweven is met iets wat je leuk vindt. Maar het is wel gokken. En het kan net zo verslavend worden als slotmachines. Soms erger.</p>
<p>Dit artikel zet de zaken op een rij. Eerlijk.</p>

<h2>Waarom sportgokken zo'n addertje is</h2>
<p>Sportgokken is bijzonder gevaarlijk om drie redenen.</p>
<p><strong>Eén: de illusie van controle.</strong></p>
<p>Bij een slotmachine weet iedereen dat het puur kans is. Bij sportgokken denk je dat je iets weet. Je kent de competitie. Je hebt de wedstrijd zien aankomen. Je weet wie er geblesseerd is. Je hebt een mening.</p>
<p>En soms heb je gelijk. Dat versterkt de illusie. "Zie je wel dat ik dit kan."</p>
<p>Wat je niet ziet: de bookmaker heeft betere modellen, betere data en een ingebouwd voordeel. Op de lange termijn verlies je. Niet omdat je dom bent. Omdat de wiskunde niet meewerkt.</p>
<p><strong>Twee: de oneindige toegang.</strong></p>
<p>Een casino moest je ooit voor naar Holland Casino of een speelhal. Sportgokken zit in je broekzak, 24 uur per dag. Live betting. Tussendoor wedden op het volgende doelpunt. In-play markten op tien wedstrijden tegelijk.</p>
<p>Er is letterlijk nooit een moment waarop je niet kunt gokken. Wedstrijden in Australië, in Brazilië, in de Champions League, in de eerste divisie van Roemenië. Altijd loopt er ergens iets.</p>
<p><strong>Drie: de sociale acceptatie.</strong></p>
<p>Praten over een grote winst aan de slots is taboe. Praten over een sportwed die je hebt gewonnen is een gespreksopener bij de borrel. Sportgokken voelt acceptabel.</p>
<p>En dat is wat het verraderlijk maakt. Mensen om je heen zien het niet als een probleem. Jij bent niet "die gokverslaafde". Jij bent gewoon "die gozer die altijd op voetbal wedt". Tot het te ver is.</p>

<h2>De cijfers waar de industrie liever niet over praat</h2>
<p>Sportgokken in Nederland groeit hard.</p>
<p>In 2021 ging de Nederlandse online gokmarkt open. Sindsdien is sportgokken explosief toegenomen. Reclames overal. Op tv, op radio, op podcasts, in apps, op sportshirts.</p>
<p>De Kansspelautoriteit en verslavingszorginstellingen luiden inmiddels de noodklok. Het aantal aanmeldingen voor gokverslavingsbehandeling is sinds 2021 fors gestegen. Een groot deel daarvan zit in sportgokken.</p>
<p>Vooral jonge mannen zitten in de risicogroep. Mannen tussen de 18 en 35, vaak met interesse in voetbal of andere sporten, vaak online actief. De industrie weet dat. Daar wordt op gemarketeerd.</p>
<p>In 2025 voerde de Nederlandse overheid strenger beleid in voor gokreclames vanwege de toename van problematisch gokgedrag, vooral bij jongeren. Dat zegt iets.</p>

<h2>Hoe weet je of jouw sportgokken een probleem is?</h2>
<p>Eerlijke check. Lees mee.</p>
<p>Heb je weleens:</p>
<ul>
<li>Meer ingezet dan je had willen inzetten?</li>
<li>Verloren geld geprobeerd terug te winnen door meer te wedden?</li>
<li>Sportwedstrijden gekeken alleen vanwege je inzet, niet voor de sport zelf?</li>
<li>Geld geleend om te kunnen wedden?</li>
<li>Gelogen over hoeveel je inzet?</li>
<li>Je gefrustreerd of leeg gevoeld na een wedstrijd waar geen geld op stond?</li>
<li>Op meerdere bookmakers tegelijk een account?</li>
<li>Tijdens werk of vergaderingen wedstrijden of odds gecheckt?</li>
<li>Plezier in sport zelf verloren omdat het altijd om geld gaat?</li>
<li>Geprobeerd te stoppen en het niet volgehouden?</li>
</ul>
<p>Als je drie of meer kunt aanstippen: er is iets aan de hand dat aandacht verdient.</p>
<p>Als je vijf of meer kunt aanstippen: je sportgokken is geen hobby meer, het is een probleem.</p>
<p>Lees ook: <a href="/nl/blog/gokverslaving-herkennen">Gokverslaving herkennen: 12 signalen die je niet langer kunt negeren</a></p>

<h2>Specifieke valkuilen bij sportgokken</h2>
<p><strong>Valkuil 1: live betting.</strong></p>
<p>In-play wedden op kleine momenten in een wedstrijd is psychologisch het meest verslavend stuk van sportgokken. Constante kleine inzetten, snelle uitslagen, instant emoties. Net als slotmachines, maar dan vermomd als sportkennis.</p>
<p>Als je sportgokt: live betting is meestal de eerste plek waar het verslavend wordt.</p>
<p><strong>Valkuil 2: combinatieweddenschappen.</strong></p>
<p>Combi's met grote uitbetalingen ("zes wedstrijden goed gokken voor 80 keer je inzet") zijn marketingtechnisch het slimste product van bookmakers. Lage winstkans, hoge ingebouwde marge, dopaminebommen als ze raken.</p>
<p>Eén keer een grote combi raken kan iemand jarenlang bezighouden met chasen.</p>
<p><strong>Valkuil 3: wedden tijdens emotionele momenten.</strong></p>
<p>Verlies je favoriete club? Boos? Stress op je werk? Dat zijn precies de momenten waarop mensen een verkeerde gok plaatsen.</p>
<p><strong>Valkuil 4: de "ik ken het beter dan de markt"-illusie.</strong></p>
<p>Sommige sportgokkers worden goed in hun analyse. Dat is gevaarlijker dan amateurs zijn. Want kleine winstreeksen voeden de overtuiging dat je echt slimmer bent dan de bookmaker.</p>
<p>Spoiler: bookmakers verdienen geld omdat ze, op grote schaal, het altijd beter weten dan jij. Anders waren ze allang failliet.</p>

<h2>Stoppen met sportgokken. Specifieke aanpak.</h2>
<p>De basis-aanpak is hetzelfde als bij elke gokvorm. Maar er zitten een paar specifieke stappen bij.</p>
<p><strong>Sluit je aan bij Cruks (cruks.nl).</strong></p>
<p>Tien minuten online. Daarna geen toegang meer tot Nederlandse legale bookmakers en online casino's.</p>
<p>Lees ook: <a href="/nl/blog/zelfuitsluiting-gokken-werkt-het">Werkt zelfuitsluiting bij gokken? Een eerlijk antwoord</a></p>
<p><strong>Verwijder elke bookmaker-app.</strong></p>
<p>Toto, Bet365, Unibet, Betcity, Holland Casino Sport, Bingoal, alles. Apps weg, websites uit je browsergeschiedenis, e-mails uitschrijven, accounts deactiveren of laten sluiten.</p>
<p><strong>Bel je bank voor een gokblokkade.</strong></p>
<p>Op betalingen naar bookmakers en betalingsverwerkers.</p>
<p><strong>Heroverweeg je sport-consumptie.</strong></p>
<p>Je liefde voor de sport is door gokken besmet. Voor sommige mensen is de oplossing om een tijd lang minder of geen sport te kijken. Vooral live wedstrijden. Niet voor altijd. Wel een paar maanden. Tot je weet dat je een wedstrijd kunt kijken zonder gokken in je hoofd te krijgen.</p>
<p><strong>Vermijd plekken die je naar gokken triggeren.</strong></p>
<p>Bepaalde cafés. Bepaalde vrienden die altijd over gokken praten. Bepaalde WhatsApp-groepen waar tips worden gedeeld.</p>
<p>Verwijder je niet uit hun leven. Wel uit de momenten waarin gokken centraal staat.</p>

<h2>Sport opnieuw leren liefhebben</h2>
<p>Eén ding waar veel mensen niet op zijn voorbereid.</p>
<p>Als je stopt met sportgokken, voelt sport een tijd lang vlak. Een wedstrijd kijken zonder geld erop is letterlijk minder dopamine. Je hersenen merken het.</p>
<p>Dat is een fase. Het gaat over.</p>
<p>Wat helpt:</p>
<ul>
<li>Kijk samen met anderen, niet alleen</li>
<li>Speel zelf weer een sport, in plaats van alleen kijken</li>
<li>Volg een kleinere club of een lager niveau, waar wedden minder zin heeft</li>
<li>Lees over de tactische kant, niet over de odds-kant</li>
</ul>
<p>Je liefde voor de sport komt terug. Vaak zuiverder dan voorheen.</p>
<p>Lees ook: <a href="/nl/blog/wat-doet-gokken-met-je-hersenen">Wat doet gokken met je hersenen?</a></p>

<h2>Wanneer hulp inschakelen?</h2>
<p>Voor sportgokken gelden dezelfde regels als voor andere gokvormen.</p>
<p>Bel de Nationale Hulplijn Gokken: <strong>0800-1995</strong>. Gratis, anoniem, 24/7. Een eerste gesprek geeft je richting.</p>
<p>Of neem contact op met Jellinek, Tactus, Brijder, Iriszorg of een andere verslavingszorgaanbieder. De meeste hebben specifieke programma's voor gokverslaving, en zien sportgokken steeds vaker als hoofdreden voor aanmelding.</p>
<p>Schaamte is hier extra zwaar omdat sportgokken zo "normaal" is gemaakt door de industrie. Doorbreek die schaamte. Je bent niet de eerste die belt. Je bent niet de laatste.</p>

<h2>Eén ding om te onthouden</h2>
<p>Sportgokken is geen kleinere broer van casino-gokken.</p>
<p>Het is gokken. Met dezelfde dopamine-mechanismen. Dezelfde verslavende kracht. Dezelfde gevolgen voor je financiën, relaties en hoofd.</p>
<p>Het verschil zit in de marketing. Niet in de werkelijkheid.</p>
<p>Vandaag stop je. Morgen ook. En dan elke dag opnieuw.</p>"""

related14 = (
    rel("/nl/blog/zelfuitsluiting-gokken-werkt-het","Tools","Werkt zelfuitsluiting bij gokken? Een eerlijk antwoord") +
    rel("/nl/blog/gokverslaving-herkennen","Bewustwording","Gokverslaving herkennen: 12 signalen") +
    rel("/nl/blog/dagelijkse-gewoonten-na-gokverslaving","Gewoonten","Dagelijkse gewoonten na gokverslaving")
)

html14 = page(
    "nl",
    "Sportgokken verslaving: hoe je hier eerlijk naar kijkt | Afterbetting",
    "Sportgokken verslaving voelt anders dan casino. Waarom dat een illusie is, hoe het werkt en wat helpt om eruit te komen.",
    url14,
    [("nl","https://afterbetting.com/nl/blog/sportgokken-verslaving"),("x-default","https://afterbetting.com/nl/blog/sportgokken-verslaving")],
    [schema14_article, schema14_bc],
    hero14, body14, related14,
    "Stoppen met sportgokken vraagt om dagelijkse structuur.",
    "Op Afterbetting hou je je streak bij, schrijf je in een journaal en heb je een crisisknop voor wedstrijdavonden. Begin gratis."
)

with open("nl/blog/sportgokken-verslaving.html","w",encoding="utf-8") as f:
    f.write(html14)
print("OK: sportgokken-verslaving.html")

# ── ARTIKEL 15: dagelijkse-gewoonten-na-gokverslaving ────────────────────────

slug15 = "dagelijkse-gewoonten-na-gokverslaving"
url15  = f"https://afterbetting.com/nl/blog/{slug15}"

schema15_article = json.dumps({"@context": "https://schema.org", "@type": "Article", "headline": "Dagelijkse gewoonten na gokverslaving. Een nieuw normaal opbouwen.", "author": {"@type": "Organization", "name": "Afterbetting"}, "publisher": {"@type": "Organization", "name": "Afterbetting", "url": "https://afterbetting.com"}, "datePublished": "2026-04-26", "dateModified": "2026-04-26", "inLanguage": "nl", "url": url15})
schema15_bc = json.dumps({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://afterbetting.com/nl/"}, {"@type": "ListItem", "position": 2, "name": "Blog", "item": "https://afterbetting.com/nl/blog"}, {"@type": "ListItem", "position": 3, "name": "Dagelijkse gewoonten na gokverslaving", "item": url15}]})

hero15 = '''<section class="hero"><div class="hero-inner">
<div class="bc"><a href="/nl/">Home</a> &rarr; <a href="/nl/blog">Blog</a> &rarr; Gewoonten</div>
<div class="tag">Gewoonten</div>
<h1>Dagelijkse gewoonten na gokverslaving. Een nieuw normaal opbouwen.</h1>
<p style="font-size:1.1rem;color:var(--mid);font-weight:300;line-height:1.7;margin-top:1rem">Dagelijkse gewoonten na gokverslaving zijn de bouwstenen van je nieuwe leven. Concrete routines voor ochtend, dag en avond.</p>
<div class="meta">Door Afterbetting &middot; 26 april 2026 &middot; 9 min lezen</div>
</div></section>'''

body15 = """<p>Hier is een vraag die je over een jaar kan beantwoorden.</p>
<p>Wie ben je over een jaar?</p>
<p>Je weet het antwoord nu nog niet. En dat is goed. Want het antwoord is niet iets wat je vandaag bedenkt. Het antwoord is de optelsom van wat je elke dag doet, vanaf vandaag, voor 365 dagen achter elkaar.</p>
<p>Dagelijkse gewoonten zijn de stille bouwers van je toekomst. Niet de grote beslissingen. Niet de motivationele speeches in je hoofd. De vijftig kleine dingen die je doet zonder erbij na te denken, die bepalen wie je wordt.</p>
<p>Voor iemand die uit gokverslaving komt, is dit extra belangrijk. Gokken vulde je dagen met chaos en pieken. Stoppen vraagt om het tegenovergestelde: rust en herhaling.</p>
<p>Dit artikel laat zien hoe je dat opbouwt. Concreet, niet zweverig.</p>

<h2>Waarom gewoonten zo belangrijk zijn na gokken</h2>
<p>Even uitleggen wat hier speelt.</p>
<p>Wanneer je gokte, draaide je leven op impulsen. Een melding op je telefoon. Een wedstrijd die begon. Een vlaag van verveling. Reactief leven.</p>
<p>Stoppen met gokken haalt die impuls-structuur weg. Wat overblijft is een leeg ritme. Geen automatische dagvulling. Geen pieken om naar uit te kijken. Geen reden om vanzelf in beweging te komen.</p>
<p>Dit is gevaarlijk territorium. Je hersenen houden niet van leegte. Als jij geen structuur biedt, gaan ze vanzelf op zoek naar de oude structuur. Dat is waarom mensen na drie weken zonder gokken plotseling de neiging voelen "alleen maar even te kijken".</p>
<p>Dagelijkse gewoonten vullen de leegte met iets anders. Niet spannend. Wel veilig. En na verloop van tijd: prettig.</p>
<p>Lees ook: <a href="/nl/blog/hoe-vul-ik-mijn-tijd-zonder-gokken">Hoe vul je je tijd zonder gokken?</a></p>

<h2>Het principe. Vijf kleine, niet één grote.</h2>
<p>De fout die bijna iedereen maakt: ze proberen één grote gewoonte tegelijk in te bouwen. Hard sporten elke dag. Een uur lezen elke dag. Mediteren elke dag.</p>
<p>Werkt niet. Wat wel werkt: vijf hele kleine gewoonten tegelijk. Zo klein dat je ze niet kunt overslaan.</p>
<p>Niet "een uur sporten". Wel "tien minuten lopen na het ontbijt".</p>
<p>Niet "elke dag een hoofdstuk lezen". Wel "twee bladzijden voor het slapen".</p>
<p>Niet "elke dag mediteren". Wel "drie diepe ademhalingen voordat ik mijn auto start".</p>
<p>De kleine gewoonten worden vanzelf groter zodra ze automatisch zijn. Maar je begint klein. Anders sneuvel je in week twee.</p>

<h2>De ochtend. Hoe je je dag opent.</h2>
<p>De ochtend zet de toon voor de rest. Hier vier gewoonten die werken.</p>
<p><strong>Vaste opstaantijd, ook in het weekend.</strong></p>
<p>Niet om jezelf te kwellen. Om je biologische klok te kalibreren. Maandagochtend zeven uur en zaterdagochtend twaalf uur is een klok-shock. Je systeem komt nooit in een ritme.</p>
<p>Kies een tijd. Hou hem aan. Zes dagen per week minimaal.</p>
<p><strong>Vijftien minuten naar buiten in het eerste uur.</strong></p>
<p>Daglicht in je ogen geeft je hersenen het signaal dat de dag begint. Zelfs bij bewolkt weer. Combineer eventueel met een korte wandeling, koffie buiten, of de hond uitlaten.</p>
<p><strong>Geen telefoon in het eerste half uur.</strong></p>
<p>Pak je telefoon niet op zodra je wakker wordt. Lees geen mail. Open geen apps. Begin niet met scrollen.</p>
<p>Waarom: je hersenen zijn 's ochtends het meest beïnvloedbaar. Wat je in dat eerste half uur ziet, kleurt de rest van je dag. Pak je telefoon na je douche of na het ontbijt. Niet voor.</p>
<p><strong>Een korte morgenroutine die je niet overslaat.</strong></p>
<p>Vijf minuten. Niet meer. Bijvoorbeeld: glas water drinken, drie diepe ademhalingen, drie dingen opschrijven waar je dankbaar voor bent, bed opmaken.</p>
<p>Klein. Voorspelbaar. Doe je elke ochtend.</p>
<p>Dit is de meest onderschatte gewoonte van allemaal. Niet omdat het magisch is. Omdat het je hersenen leert: ik begin elke dag met iets dat ik kies, niet met iets wat me overkomt.</p>

<h2>Tijdens de dag. Drie ankers.</h2>
<p><strong>Eén: bewegen, elke dag.</strong></p>
<p>Een uur lopen. Een half uur fietsen. Sportschool drie keer per week. Iets.</p>
<p>Beweging is geen luxe in herstel. Beweging verlaagt cortisol, geeft endorfine, verbetert slaap, verlaagt de kans op terugval en verhoogt zelfwaardering.</p>
<p>Eén uur per dag. Niet veel. Niet weinig. Genoeg.</p>
<p><strong>Twee: één maaltijd zonder telefoon.</strong></p>
<p>Eén maaltijd per dag eet je zonder schermen. Zonder tv, zonder telefoon, zonder laptop. Met iemand of alleen, maakt niet uit.</p>
<p>Dit traint je hersenen om tijd te kunnen verdragen zonder constante prikkeling. Voor iemand die uit gokverslaving komt, is dat een vaardigheid die opnieuw geleerd moet worden.</p>
<p><strong>Drie: één moment van aandacht voor iets niet-digitaal.</strong></p>
<p>Vijftien minuten muziek luisteren zonder iets anders. Een hoofdstuk lezen. Een wandeling zonder telefoon. Een gesprek met iemand zonder afgeleid te zijn.</p>
<p>Eén moment. Per dag. Bewust.</p>

<h2>De avond. Hoe je je dag afsluit.</h2>
<p>De avond is voor veel mensen die uit gokverslaving komen het zwaarst. Gokken vond vooral 's avonds plaats.</p>
<p><strong>Schermen weg een uur voor bedtijd.</strong></p>
<p>Begin met dertig minuten als een uur te veel is. Wat doe je dan? Lezen, praten, wandelen, douche. Iets simpels en niet-stimulerend. Je hersenen krijgen de tijd om af te schakelen.</p>
<p><strong>Vijf minuten journalen voor het slapen.</strong></p>
<p>Pak een notitieboek. Vijf minuten. Drie vragen: wat ging vandaag goed? Wat was zwaar? Waar kijk ik morgen naar uit?</p>
<p>Niet je beste schrijfwerk. Wel eerlijk. Dit haalt gedachten uit je hoofd op papier. Je slaapt makkelijker omdat je hersenen zijn bediend.</p>
<p>Lees ook: <a href="/nl/blog/slaapproblemen-stoppen-met-gokken">Slaapproblemen na stoppen met gokken: wat helpt echt</a></p>
<p><strong>Vaste bedtijd waar je redelijk dichtbij blijft.</strong></p>
<p>Niet militaristisch. Wel een richtbedtijd. Bijvoorbeeld 22:30, met een marge van 30 minuten. Je biologische klok beloont voorspelbaarheid.</p>

<h2>De drie gewoonten die specifiek voor herstel werken</h2>
<p>Naast de algemene gewoonten zijn er drie die direct met je herstel te maken hebben.</p>
<p><strong>Gewoonte 1: een dagelijkse check-in.</strong></p>
<p>Eén minuut, één keer per dag. Hoe gaat het? Voel je drang? Wat ging goed? Wat was risico?</p>
<p>Kan in een app (Afterbetting heeft dit), kan op papier, kan in je hoofd terwijl je tanden poetst. Maar doe het. Elke dag.</p>
<p>Het effect: je houdt jezelf in beeld. Je merkt eerder wanneer iets verschuift. Je traint zelfreflectie.</p>
<p><strong>Gewoonte 2: contact met iemand die het weet.</strong></p>
<p>Eén keer per week, minimaal. Een sponsor uit een twaalfstappenprogramma. Een vriend die je het verteld hebt. Een hulpverlener. Wekelijks contact. Niet diep. Niet lang. Wel echt.</p>
<p>Dit voorkomt dat je in de stilte verdwijnt waarin verslaving floreert.</p>
<p><strong>Gewoonte 3: je streak en cijfers checken.</strong></p>
<p>Wekelijks, op een vast moment. Je streak. Je financiële voortgang. Wat heb je bespaard? Welke schulden gaan af?</p>
<p>Concrete vooruitgang voedt je gevoel van competentie. En herinnert je waarom je dit doet.</p>

<h2>Wat je niet doet</h2>
<p><strong>Niet in een keer alle gewoonten ineens invoeren.</strong></p>
<p>Pak er twee. Doe ze drie weken consistent. Voeg dan de volgende toe. In een keer alles veranderen werkt nooit langer dan twee weken.</p>
<p><strong>Niet jezelf afmaken bij een gemiste dag.</strong></p>
<p>Een dag overslaan is geen mislukking. Twee dagen overslaan ook niet. Pak het de derde dag weer op zonder drama. De vraag is niet of je een dag mist. De vraag is of je weer instapt.</p>
<p><strong>Geen perfectie najagen.</strong></p>
<p>80% van de tijd je gewoonten volhouden is genoeg om je leven te veranderen. 100% is niet realistisch en niet nodig.</p>

<h2>Hoe lang voordat ze automatisch worden?</h2>
<p>Eerlijk antwoord: tussen de zes weken en zes maanden, afhankelijk van de gewoonte.</p>
<p>De eerste drie weken voelt het als werk. Je moet erbij nadenken. Je moet jezelf eraan herinneren.</p>
<p>Tussen week 4 en 12 wordt het gemakkelijker. Je doet het niet altijd zonder denken, maar het kost minder energie.</p>
<p>Na drie tot zes maanden zijn de meeste gewoonten geïntegreerd. Je doet ze omdat je ze doet. Niet omdat je je dwingt.</p>
<p>Hoe kleiner de gewoonte, hoe sneller hij automatisch wordt. Daarom begin je klein.</p>

<h2>Begin met twee. Vandaag.</h2>
<p>Niet alles van bovenstaande. Twee.</p>
<p>Twee kleine gewoonten die je vandaag of morgen begint. Drie weken volhouden, dan evalueren.</p>
<p>Voorbeeld: vaste opstaantijd (7:30) en geen telefoon in het eerste half uur.</p>
<p>Of: vijftien minuten lopen na het avondeten en vijf minuten journalen voor het slapen.</p>
<p>Kies twee. Niet drie. Niet vijf. Twee.</p>
<p>Een nieuw normaal bouw je niet door één keer de berg te beklimmen. Je bouwt het door duizend kleine stappen op dezelfde plek te zetten, dag na dag, tot je daar bent zonder dat je merkt hoe je er kwam.</p>
<p>Begin vandaag.</p>"""

related15 = (
    rel("/nl/blog/hoe-vul-ik-mijn-tijd-zonder-gokken","Tools","Hoe vul je je tijd zonder gokken?") +
    rel("/nl/blog/slaapproblemen-stoppen-met-gokken","Tools","Slaapproblemen na stoppen met gokken") +
    rel("/nl/blog/gokverslaving-en-identiteit","Emotie","Gokverslaving en identiteit: wie ben je zonder de inzet?")
)

html15 = page(
    "nl",
    "Dagelijkse gewoonten na gokverslaving: zo bouw je het op | Afterbetting",
    "Dagelijkse gewoonten na gokverslaving zijn de bouwstenen van je nieuwe leven. Concrete routines voor ochtend, dag en avond.",
    url15,
    [("nl","https://afterbetting.com/nl/blog/dagelijkse-gewoonten-na-gokverslaving"),("x-default","https://afterbetting.com/nl/blog/dagelijkse-gewoonten-na-gokverslaving")],
    [schema15_article, schema15_bc],
    hero15, body15, related15,
    "Wil je je dagelijkse gewoonten op één plek bijhouden?",
    "De gewoonten tracker en dagelijkse check-in van Afterbetting helpen je het vol te houden. Gratis te beginnen."
)

with open("nl/blog/dagelijkse-gewoonten-na-gokverslaving.html","w",encoding="utf-8") as f:
    f.write(html15)
print("OK: dagelijkse-gewoonten-na-gokverslaving.html")
print("Alle batch 5 bestanden gegenereerd.")
