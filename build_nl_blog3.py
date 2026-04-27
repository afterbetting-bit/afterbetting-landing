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

# ── ARTIKEL 8: gokken-aan-je-familie-vertellen ───────────────────────────────

slug8 = "gokken-aan-je-familie-vertellen"
url8  = f"https://afterbetting.com/nl/blog/{slug8}"

schema8_article = json.dumps({"@context":"https://schema.org","@type":"Article","headline":"Gokken aan je familie vertellen. Zo begin je dat gesprek.","author":{"@type":"Organization","name":"Afterbetting"},"publisher":{"@type":"Organization","name":"Afterbetting","url":"https://afterbetting.com"},"datePublished":"2026-04-26","dateModified":"2026-04-26","inLanguage":"nl","url":url8})
schema8_bc = json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://afterbetting.com/nl/"},{"@type":"ListItem","position":2,"name":"Blog","item":"https://afterbetting.com/nl/blog"},{"@type":"ListItem","position":3,"name":"Gokken aan je familie vertellen","item":url8}]})

hero8 = '''<section class="hero"><div class="hero-inner">
<div class="bc"><a href="/nl/">Home</a> &rarr; <a href="/nl/blog">Blog</a> &rarr; Relaties</div>
<div class="tag">Relaties</div>
<h1>Gokken aan je familie vertellen. Zo begin je dat gesprek.</h1>
<p style="font-size:1.1rem;color:var(--mid);font-weight:300;line-height:1.7;margin-top:1rem">Gokken aan je familie vertellen is een van de zwaarste gesprekken. Hoe begin je, wat zeg je, en wat doe je met de reactie.</p>
<div class="meta">Door Afterbetting &middot; 26 april 2026 &middot; 8 min lezen</div>
</div></section>'''

body8 = """<p>Je hebt het al maanden in je hoofd. Misschien jaren.</p>
<p>"Ik moet het ze vertellen."</p>
<p>En elke keer dat je het wil zeggen, draait je maag zich om en zoek je een nieuwe reden om het uit te stellen. Niet vanavond, ze zijn moe. Niet dit weekend, het is een verjaardag. Niet deze week, te druk.</p>
<p>De waarheid: er is geen goed moment.</p>
<p>Er is alleen het moment dat jij erover ophoudt jezelf voor te liegen dat er een goed moment komt. Dat moment is meestal vandaag.</p>
<p>Dit artikel gaat over hoe je het gesprek voert. Niet hoe je het wint. Hoe je het voert. Eerlijk, kwetsbaar, zonder dat het uitloopt op verwijten of paniek.</p>

<h2>Waarom je het ze moet vertellen</h2>
<p>Eerst even de wortel.</p>
<p>Je vraagt jezelf misschien af: moet dit echt? Kan ik het niet alleen oplossen?</p>
<p>Eerlijk antwoord: nee.</p>
<p>Niet omdat je zwak bent. Omdat verslaving in het geheim leeft. Geheimhouding is wat het in stand houdt. Elke leugen die je nog vertelt, is een steen onder het fundament dat je probeert af te breken.</p>
<p>Je hoeft niet aan iedereen te vertellen wat er aan de hand is. Maar één of twee mensen die het weten, veranderen alles. Want dan ben je niet meer alleen.</p>
<p>Tweede reden: ze weten het waarschijnlijk al voor een deel.</p>
<p>Misschien niet de cijfers. Niet de details. Maar dat er iets is, dat voelen mensen die met je leven. Je partner ziet je niet meer. Je ouders horen je stem op een andere manier. Je broer voelt dat je gesprekken vermijdt.</p>
<p>Wat ze niet weten, is wat het is. Dat invullen ze met hun eigen verhaal. Soms een verhaal dat erger is dan de waarheid.</p>

<h2>Bereid je voor. Eén pagina.</h2>
<p>Voordat je het gesprek voert, schrijf je het op.</p>
<p>Niet als script. Wel als kompas. Eén pagina:</p>
<p><strong>Wat je gaat zeggen.</strong> In drie zinnen. Geen lange aanloop. Mensen denken dat ze hun verhaal moeten opbouwen. Niet doen. Direct beginnen.</p>
<p>Voorbeeld: "Ik heb iets te vertellen waar ik me al lang voor schaam. Ik heb een gokverslaving. Het speelt al een tijd en ik wil hulp."</p>
<p>Drie zinnen. Klaar.</p>
<p><strong>Wat je niet gaat zeggen.</strong> Geen vergoeilijkingen. Geen "het kwam door werk", "het is niet zo erg", "ik had het bijna onder controle". Geen disclaimers. Verslaving heeft geen excuses nodig.</p>
<p><strong>Wat je vraagt.</strong> Niet dat ze het oplossen. Wel: dat ze luisteren. Dat ze er zijn. Misschien dat ze meekijken naar de cijfers. Misschien dat ze meegaan naar een eerste afspraak.</p>
<p><strong>Wat je verwacht.</strong> Reken op alles. Boosheid, verdriet, ongeloof, opluchting, zwijgen. Misschien allemaal in één gesprek. Dat is normaal.</p>

<h2>Met wie begin je?</h2>
<p>Niet iedereen tegelijk.</p>
<p>Begin met één persoon. De persoon die het het eerst moet weten. Meestal is dat:</p>
<ul>
<li>Je partner, als je samenwoont of een gezamenlijke financiële situatie hebt</li>
<li>Een ouder of broer/zus die je vertrouwt</li>
<li>Een goede vriend of vriendin</li>
</ul>
<p>Kies iemand die jou kent. Iemand die je niet meteen veroordeelt. Iemand die luistert voordat hij oplossingen aandraagt.</p>
<p>Niet de meest dramatische persoon in je leven. Niet degene die het meteen zal doorvertellen. Niet degene die zelf te kwetsbaar is om dit te dragen.</p>
<p>Kies één. Dan, als dat goed gaat, een tweede. Daarna eventueel meer.</p>

<h2>Hoe je het gesprek opent</h2>
<p>Hier komt het ding.</p>
<p>De zwaarste woorden eruit krijgen, dat is het werk. Niet de uitleg erna.</p>
<p>Een paar voorbeelden van openers:</p>
<p><strong>Direct:</strong> "Ik moet je iets vertellen. Ik gok. Al jaren. En het is uit de hand gelopen. Ik wil ervan af, en ik heb hulp nodig."</p>
<p><strong>Via een verzoek:</strong> "Mag ik even met je praten over iets serieus? Ik heb iets gedaan waar ik me schaam, en ik kan het niet langer alleen dragen."</p>
<p><strong>Via een gevoel:</strong> "Ik moet eerlijk zijn met je. Iets in mijn leven is niet goed, en ik heb het al lang voor me gehouden. Ik wil het nu vertellen."</p>
<p>Welke past, weet jij. Maar wat ze gemeen hebben: kort. Direct. Geen omweg.</p>
<p>Een lange aanloop maakt het zwaarder voor allebei. De ander voelt dat er iets aankomt en raakt onrustig. Jij raakt verlamd. Eerste zin meteen kern.</p>

<h2>De reactie. Wat je waarschijnlijk krijgt.</h2>
<p>Reken op één of meer van deze reacties. Allemaal normaal.</p>
<p><strong>Stilte.</strong> Soms zegt iemand minutenlang niets. Niet omdat ze niet luisteren. Omdat ze proberen te verwerken. Geef de stilte ruimte. Vul hem niet op met meer woorden.</p>
<p><strong>Boosheid.</strong> Vooral als er financiële schade is. Of als het in een liefdesrelatie zit. Boosheid is een uiting van pijn, niet alleen van afkeuring. Probeer er niet defensief in te gaan. Luister.</p>
<p><strong>Verdriet.</strong> Ze huilen. Of jij huilt. Of allebei. Dat mag. Dat is geen falen. Dat is verbinding.</p>
<p><strong>"Hoeveel?"</strong> De vraag over geld komt bijna altijd. Wees voorbereid. Heb een eerlijk getal in je hoofd. Niet liegen om de pijn te verminderen.</p>
<p><strong>"Waarom heb je dit niet eerder gezegd?"</strong> Een eerlijk antwoord: omdat ik me schaamde. Omdat ik dacht dat ik het kon oplossen. Omdat ik bang was wat je zou zeggen.</p>
<p><strong>"Wat heb je nodig van mij?"</strong> Soms krijg je dit. Het is goud. Wees eerlijk: je weet het misschien zelf niet helemaal. Vraag om luisteren. Vraag om geduld.</p>

<h2>Wat je waarschijnlijk niet krijgt</h2>
<p><strong>Een kant en klare oplossing.</strong> Verwacht het niet. Mensen hebben tijd nodig om te begrijpen wat verslaving is en wat ze ermee kunnen. Geef ze die tijd.</p>
<p><strong>Onmiddellijk vergeven worden.</strong> Vooral bij partners. Vergeven duurt. Soms maanden. Soms langer. Dat is hun proces. Jij kunt het niet versnellen.</p>
<p><strong>Volledig begrip in één gesprek.</strong> Mensen die nooit gegokt hebben, snappen niet meteen waarom je niet gewoon kon stoppen. Dat is niet hun fout. Het is een leerproces voor hen ook.</p>

<h2>Drie dingen die het gesprek beter maken</h2>
<p><strong>Eén: een concreet plan, klaar in je hoofd.</strong></p>
<p>Niet "ik ga zoeken naar hulp". Wel: "Ik heb me al aangemeld bij Cruks, ik bel maandag de huisarts, ik wil naar Jellinek of Tactus voor een intake."</p>
<p>Een plan laat zien dat je dit serieus neemt. Het verlicht hun zorg dat dit nog tien jaar gaat duren.</p>
<p><strong>Twee: niets verzwijgen wat ze later zelf gaan ontdekken.</strong></p>
<p>Schulden? Vertellen. Een tweede rekening? Vertellen. Geld dat van iemand was? Vertellen.</p>
<p>Wat ze nu horen is zwaar. Wat ze later zelf ontdekken, breekt vertrouwen op een manier die nog moeilijker te repareren is.</p>
<p><strong>Drie: de Nationale Hulplijn Gokken noemen.</strong></p>
<p>Niet voor jou alleen. Voor hen. Familieleden van mensen met een gokverslaving kunnen ook bellen naar <strong>0800-1995</strong> (gratis, anoniem, 24/7). Of bij Anonieme Gokkers naar de Gam-Anon groepen voor familie.</p>
<p>Geef ze die optie. Hun pijn is ook reëel. Ook zij hebben hulp nodig.</p>

<h2>Wat je niet doet, ook niet als het zwaar wordt</h2>
<p><strong>Niet bagatelliseren als ze schrikken.</strong> "Het valt wel mee" is een leugen. Je vertelt ze niet dat het meevalt om hen gerust te stellen. Want als blijkt dat het niet meeviel, is het tweede gesprek nog erger.</p>
<p><strong>Niet beloven dat het over is.</strong> Verslaving werkt niet zo. Je kunt beloven dat je werkt aan herstel. Dat je open bent. Dat je hulp zoekt. Niet dat je nooit meer een gedachte aan gokken zult hebben.</p>
<p><strong>Niet vragen om geheimhouding.</strong> Vraag wel om respect. Niet om geheimhouding. Een partner moet kunnen praten met haar zus, met een goede vriend, met een therapeut. Anders dragen ze het alleen, en dat breekt mensen.</p>

<h2>En daarna?</h2>
<p>Het gesprek is eindig. Het werk niet.</p>
<p>Wat je doet na dat eerste gesprek bepaalt of je woorden waarde hebben.</p>
<ul>
<li>Maak deze week een afspraak met de huisarts of een verslavingszorgaanbieder</li>
<li>Sluit jezelf aan via Cruks (cruks.nl) als je dat nog niet gedaan hebt</li>
<li>Bel je bank voor een gokblokkade</li>
<li>Vraag of degene die je het verteld heeft, mee wil naar het eerste gesprek bij de hulpverlener</li>
</ul>
<p>Lees ook: <a href="/nl/blog/stoppen-met-gokken">Stoppen met gokken: een eerlijke gids</a></p>
<p>Praten was de eerste stap. De tweede is doen wat je hebt gezegd dat je gaat doen.</p>

<h2>Eén ding tot slot</h2>
<p>Het gesprek dat je vannacht niet kunt voeren, voer je liever vandaag dan over een jaar.</p>
<p>Want elke maand dat je wacht, wordt het bedrag groter. De schaamte dieper. Het verhaal ingewikkelder.</p>
<p>Vandaag is het gesprek zwaar. Maar het is doenlijk.</p>
<p>Adem in. Bel ze. Vraag of ze tijd hebben.</p>
<p>Begin.</p>"""

related8 = (
    rel("/nl/blog/gokverslaving-en-identiteit","Emotie","Gokverslaving en identiteit: wie ben je zonder de inzet?") +
    rel("/nl/blog/terugval-na-gokverslaving","Herstel","Terugval na gokverslaving. Wat nu?") +
    rel("/nl/blog/stoppen-met-gokken","Herstel","Stoppen met gokken: een eerlijke gids")
)

html8 = page(
    "nl",
    "Gokken aan je familie vertellen: zo begin je het gesprek | Afterbetting",
    "Gokken aan je familie vertellen is een van de zwaarste gesprekken. Hoe begin je, wat zeg je, en wat doe je met de reactie.",
    url8,
    [("nl","https://afterbetting.com/nl/blog/gokken-aan-je-familie-vertellen"),("x-default","https://afterbetting.com/nl/blog/gokken-aan-je-familie-vertellen")],
    [schema8_article, schema8_bc],
    hero8, body8, related8,
    "Het gesprek voeren is moeilijk. Het volhouden ook.",
    "Begin gratis op Afterbetting voor dagelijkse structuur, journaalprompts en een crisisknop voor de momenten dat het zwaar wordt."
)

with open("nl/blog/gokken-aan-je-familie-vertellen.html","w",encoding="utf-8") as f:
    f.write(html8)
print("OK: gokken-aan-je-familie-vertellen.html")

# ── ARTIKEL 9: gokverslaving-en-identiteit ───────────────────────────────────

slug9 = "gokverslaving-en-identiteit"
url9  = f"https://afterbetting.com/nl/blog/{slug9}"

schema9_article = json.dumps({"@context":"https://schema.org","@type":"Article","headline":"Gokverslaving en identiteit. Wie ben je zonder de inzet?","author":{"@type":"Organization","name":"Afterbetting"},"publisher":{"@type":"Organization","name":"Afterbetting","url":"https://afterbetting.com"},"datePublished":"2026-04-26","dateModified":"2026-04-26","inLanguage":"nl","url":url9})
schema9_bc = json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://afterbetting.com/nl/"},{"@type":"ListItem","position":2,"name":"Blog","item":"https://afterbetting.com/nl/blog"},{"@type":"ListItem","position":3,"name":"Gokverslaving en identiteit","item":url9}]})

hero9 = '''<section class="hero"><div class="hero-inner">
<div class="bc"><a href="/nl/">Home</a> &rarr; <a href="/nl/blog">Blog</a> &rarr; Emotie</div>
<div class="tag">Emotie</div>
<h1>Gokverslaving en identiteit. Wie ben je zonder de inzet?</h1>
<p style="font-size:1.1rem;color:var(--mid);font-weight:300;line-height:1.7;margin-top:1rem">Gokverslaving en identiteit zijn vaak verstrengeld. Wie ben je als je niet meer gokt? Een eerlijk verhaal over wat overblijft.</p>
<div class="meta">Door Afterbetting &middot; 26 april 2026 &middot; 9 min lezen</div>
</div></section>'''

body9 = """<p>Hier is een vraag die je misschien nog niet aan jezelf hebt durven stellen.</p>
<p>Wie ben je als je niet gokt?</p>
<p>Niet "wie was je voordat je begon". Wie ben je nu, vandaag, zonder de adrenaline, zonder de inzet, zonder die scherpte die je voelt als de wedstrijd begint of de rollen draaien?</p>
<p>Voor veel mensen die jaren hebben gegokt, is dit een lastige vraag. Niet omdat ze niemand zijn. Maar omdat ze gewend zijn aan een ik dat op gokken loopt. Verwijder het gokken, en het ik dat overblijft voelt vreemd. Soms leeg. Soms onbekend.</p>
<p>Dit artikel gaat over die leegte. En over wat erin komt te zitten als je doorgaat.</p>

<h2>Waarom gokken zo verweven raakt met wie je bent</h2>
<p>Verslaving is niet iets wat naast jou staat. Het kruipt in je.</p>
<p>Begin van een dag: je leest het sportnieuws met een andere blik. Je ziet wedstrijden niet meer als wedstrijden, maar als kansen. Je wandelt langs een speelhal en je hand jeukt. Je telefoon is niet je telefoon, het is je portaal naar het volgende potje.</p>
<p>Op een gegeven moment verschuift iets dieper. Je begint het gokken te zien als een eigenschap. "Ik ben iemand die gokt." "Ik ben de persoon die de slimme weddenschap heeft gemaakt." "Ik ben goed in dit."</p>
<p>En dan, langzaam, vervangt het andere dingen.</p>
<p>Je was de muziekliefhebber? Vervangen door avonden achter slotmachines. Je was de sporter? Vervangen door wedstrijden waarop je geld zet. Je was de vader die meeging naar voetbal van je kind? Vervangen door scrollen op je telefoon tijdens de wedstrijd.</p>
<p>Het gokken is geen onderdeel van je leven meer. Het is je leven. En jij bent iemand die gokt.</p>
<p>Stoppen met gokken voelt daarom niet als een gewoonte afleren. Het voelt als afscheid nemen van wie je bent.</p>

<h2>De leegte in de eerste maanden</h2>
<p>In de eerste maanden zonder gokken kom je iets vreemds tegen.</p>
<p>Niet alleen craving. Niet alleen het missen van de kick.</p>
<p>Iets diepers. Iets stillers. Een soort grijsheid. De wereld voelt minder. Kleuren minder fel. Gesprekken minder belangrijk. Je dagen voelen langer. Avonden eindeloos.</p>
<p>Dit is de leegte waar veel mensen in de val trappen. Ze denken: dit is mijn leven zonder gokken. Het is grijs, het is leeg, het is saai. Beter terug.</p>
<p>Niet juist.</p>
<p>Wat je voelt, is geen "leven zonder gokken". Wat je voelt is je dopaminesysteem in herstel. Je hersenen zijn maandenlang afgevlakt door de pieken van gokken. Nu krijgen ze die pieken niet meer, en alles voelt vlak omdat hun referentiekader is verschoven.</p>
<p>Dit duurt. Niet eeuwig. Wel maanden.</p>
<p>Lees ook: <a href="/nl/blog/wat-doet-gokken-met-je-hersenen">Wat doet gokken met je hersenen?</a></p>
<p>In die maanden is het gevaar dat je conclusies trekt over wie je bent op basis van een tijdelijke staat. Je bent niet leeg. Je bent in herstel.</p>

<h2>De vraag opnieuw, langzamer</h2>
<p>Wie ben je als je niet gokt?</p>
<p>Beantwoord die vraag niet meteen. Stel hem op een rustige manier. Schrijf een paar dingen op:</p>
<ul>
<li>Wat deed je leuk vóór gokken je leven binnenkwam?</li>
<li>Wie waren de mensen die je toen om je heen had?</li>
<li>Welke dingen waren belangrijk voor je, dingen waar je over praatte?</li>
<li>Wat zou je zijn gaan doen als gokken nooit was begonnen?</li>
</ul>
<p>Misschien antwoord je: "Ik weet het niet meer." Dat klopt vaak. Maandenlang of jarenlang heb je die delen van jezelf weggestopt. Ze zitten er nog. Ze zijn alleen stoffig.</p>

<h2>Identiteit bouw je. Hij valt niet uit de hemel.</h2>
<p>Eén belangrijke realisatie.</p>
<p>Mensen denken vaak dat ze ergens diep van binnen "een echte zelf" hebben, en dat ze die alleen hoeven te ontdekken.</p>
<p>Klopt niet. Identiteit is geen schatkist die je vindt. Identiteit is iets wat je bouwt. Met dagelijkse keuzes. Met dingen die je doet. Met mensen waarmee je tijd doorbrengt.</p>
<p>Wie ben je over een jaar? Dat hangt af van wat je in dat jaar doet.</p>
<p>Als je elke dag opstaat, sport, werkt, mensen ziet, je hobby's oppikt, je relaties onderhoudt, dan ben je over een jaar iemand die sport, werkt, mensen ziet, hobby's heeft, relaties onderhoudt.</p>
<p>Als je elke dag op de bank zit en wacht tot het beter wordt, ben je over een jaar iemand die op de bank zit en wacht.</p>
<p>Identiteit is een werkwoord, geen zelfstandig naamwoord.</p>

<h2>Vier ankers om opnieuw te bouwen</h2>
<p>In de maanden na stoppen met gokken bouw je je identiteit terug. Niet door diepzinnig na te denken, maar door dingen te doen. Vier ankers helpen.</p>
<p><strong>Eén: lichaam.</strong></p>
<p>Sport. Wandel. Beweeg. Maakt niet uit wat. Je lichaam is van jou en het is concreet. Het reageert op aandacht. Drie keer per week sporten, en je voelt je over een maand anders dan nu. Niet omdat je dunner bent geworden. Omdat je hebt aangetoond dat je iets kunt volhouden.</p>
<p><strong>Twee: werk of richting.</strong></p>
<p>Iets waar je goed in bent of beter in wil worden. Werk, studie, een ambacht, een vaardigheid. Iets waar je tijd in steekt en iets uit haalt. Niet omdat het rijk maakt, maar omdat het structuur geeft.</p>
<p><strong>Drie: relaties.</strong></p>
<p>Niet duizenden contacten. Drie of vier mensen die je echt kent en die jou kennen. Mensen die je belt als het zwaar is, met wie je koffie drinkt zonder agenda. Eén voor één opbouwen. Het kost tijd. Het is het waard.</p>
<p><strong>Vier: iets wat groter is dan jij.</strong></p>
<p>Een hobby. Een doel. Vrijwilligerswerk. Een passie waar je met anderen samenkomt. Iets wat niet over jou gaat. Mensen die alleen op zichzelf zijn gericht, voelen zich uiteindelijk leeg. Mensen die ergens deel van uitmaken, voelen zich verankerd.</p>

<h2>Schaamte loslaten en de oude versie van jezelf</h2>
<p>Hier komt iets ingewikkelds.</p>
<p>Je voelt waarschijnlijk schaamte over de jaren dat je gokte. Over wat je hebt gedaan. Over wie je bent geworden.</p>
<p>Die schaamte heeft twee kanten. De ene kant is gezond, want hij wijst op verantwoordelijkheid. De andere kant is giftig, want hij houdt je vast aan wie je was.</p>
<p>De persoon die jaren gokte, was jij. Maar het was jij in een staat die niet permanent is. Verslaving veranderde je. Stoppen verandert je terug. En meer.</p>
<p>Je hoeft die oude versie van jezelf niet te haten. Je hoeft hem ook niet te omarmen. Je mag hem zien als iemand die zijn best deed met wat hij toen had, en die nu, vandaag, ergens anders staat.</p>
<p>Verzoening met de oude jij gaat hand in hand met de bouw van de nieuwe jij. Als je de ene wegduwt, lukt de andere niet. Als je de ene vasthoudt, blijf je staan.</p>

<h2>Een nieuw verhaal over jezelf</h2>
<p>Verhalen zijn krachtig.</p>
<p>Het verhaal dat je over jezelf vertelt, vormt wat je doet, wat je gelooft, hoe je beslissingen neemt.</p>
<p>Oud verhaal: "Ik ben een gokker. Ik heb het verpest. Ik kom hier nooit uit."</p>
<p>Nieuw verhaal: "Ik gokte. Het ging mis. Ik werk er nu uit, dag voor dag. Ik ben iemand die zijn leven oppakt."</p>
<p>Allebei zijn waar. Maar je bouwt op het tweede. Niet omdat het mooier klinkt. Omdat het accurater is.</p>
<p>Je bent niet wat je vroeger deed. Je bent wat je vandaag kiest.</p>

<h2>Eén jaar verder</h2>
<p>Stel je een moment voor over één jaar.</p>
<p>Je staat op. Je drinkt koffie. Je gaat sporten of werken. Je belt iemand. Je eet samen met mensen. Je gaat naar bed.</p>
<p>Geen indrukwekkend leven? Misschien niet.</p>
<p>Maar je bent iemand die niet meer gokt. Iemand die zijn schulden afbetaalt. Iemand die eerlijk is met de mensen om hem heen. Iemand die kan slapen.</p>
<p>Dat is geen klein leven. Dat is een echt leven. Dat is wie je wordt.</p>
<p>En het begint met vandaag. Niet met grote vragen over identiteit. Met één kleine keuze, vandaag, om door te gaan.</p>"""

related9 = (
    rel("/nl/blog/wat-doet-gokken-met-je-hersenen","Brein","Wat doet gokken met je hersenen?") +
    rel("/nl/blog/gokken-aan-je-familie-vertellen","Relaties","Gokken aan je familie vertellen") +
    rel("/nl/blog/terugval-na-gokverslaving","Herstel","Terugval na gokverslaving. Wat nu?")
)

html9 = page(
    "nl",
    "Gokverslaving en identiteit: wie ben je zonder de inzet | Afterbetting",
    "Gokverslaving en identiteit zijn vaak verstrengeld. Wie ben je als je niet meer gokt? Een eerlijk verhaal over wat overblijft.",
    url9,
    [("nl","https://afterbetting.com/nl/blog/gokverslaving-en-identiteit"),("x-default","https://afterbetting.com/nl/blog/gokverslaving-en-identiteit")],
    [schema9_article, schema9_bc],
    hero9, body9, related9,
    "Wil je je nieuwe identiteit dag voor dag opbouwen?",
    "Streak, journaal, gewoonten tracker en de brief aan jezelf op dag 365: het zit allemaal in Afterbetting. Begin gratis."
)

with open("nl/blog/gokverslaving-en-identiteit.html","w",encoding="utf-8") as f:
    f.write(html9)
print("OK: gokverslaving-en-identiteit.html")

# ── ARTIKEL 10: terugval-na-gokverslaving ────────────────────────────────────

slug10 = "terugval-na-gokverslaving"
url10  = f"https://afterbetting.com/nl/blog/{slug10}"

schema10_article = json.dumps({"@context":"https://schema.org","@type":"Article","headline":"Terugval na gokverslaving. Wat nu?","author":{"@type":"Organization","name":"Afterbetting"},"publisher":{"@type":"Organization","name":"Afterbetting","url":"https://afterbetting.com"},"datePublished":"2026-04-26","dateModified":"2026-04-26","inLanguage":"nl","url":url10})
schema10_bc = json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://afterbetting.com/nl/"},{"@type":"ListItem","position":2,"name":"Blog","item":"https://afterbetting.com/nl/blog"},{"@type":"ListItem","position":3,"name":"Terugval na gokverslaving. Wat nu?","item":url10}]})

hero10 = '''<section class="hero"><div class="hero-inner">
<div class="bc"><a href="/nl/">Home</a> &rarr; <a href="/nl/blog">Blog</a> &rarr; Herstel</div>
<div class="tag">Herstel</div>
<h1>Terugval na gokverslaving. Wat nu?</h1>
<p style="font-size:1.1rem;color:var(--mid);font-weight:300;line-height:1.7;margin-top:1rem">Terugval na gokverslaving voelt als alles kwijt. Het is het niet. Eerlijk advies over wat te doen, vandaag, zonder schaamte.</p>
<div class="meta">Door Afterbetting &middot; 26 april 2026 &middot; 8 min lezen</div>
</div></section>'''

body10 = """<p>Het is gebeurd.</p>
<p>Je had het zo lang volgehouden. Misschien dertig dagen. Misschien zes maanden. Misschien meer dan een jaar. En dan was er gisteren of vannacht of een week geleden iets: een moment, een trigger, een drang waar je niet doorheen kwam.</p>
<p>En je gokte.</p>
<p>Misschien klein. Misschien fors. Misschien voor het eerst weer, misschien al een paar dagen op rij.</p>
<p>Nu zit je dit te lezen. Met schaamte die op je drukt als een steen. Met de gedachte dat alles voor niets was. Met angst om iemand onder ogen te komen. Met een hoofd dat al de hele dag tegen je schreeuwt: "Je bent een mislukking. Je kunt het niet."</p>
<p>Stop even.</p>
<p>Adem in. Adem uit.</p>
<p>Wat je nu denkt, is niet de waarheid. Het is de stem van je verslaving die zo hard mogelijk roept om je te laten geloven dat de moeite niet waard was.</p>
<p>Dat is een leugen. En dit artikel is hoe je hem doorbreekt.</p>

<h2>Eerst dit. Een terugval is niet het einde.</h2>
<p>Belangrijke definitie.</p>
<p>Een terugval is wat het is: een terugval. Het is geen mislukking. Het is geen einde. Het is geen bewijs dat je nooit kon stoppen.</p>
<p>Het is een moeilijk moment in een lang proces.</p>
<p>Onderzoek laat zien dat de meeste mensen die uiteindelijk stoppen met gokken, één of meerdere terugvallen hebben gehad voordat het lukte. Niet één van de tien. Niet de helft. De meeste.</p>
<p>Dat is niet om je gerust te stellen dat het allemaal wel meevalt. Dat is om je te laten weten: dit hoort vaak bij het pad. Het diskwalificeert je niet.</p>
<p>Wat het wel doet: informatie geven. Over wat is misgegaan. Over wat je anders had moeten doen. Over wat de volgende keer beter kan.</p>

<h2>Wat je nu niet doet</h2>
<p>Voordat we naar wat te doen, een paar dingen die je vandaag niet doet.</p>
<p><strong>Niet doorgaan met gokken.</strong></p>
<p>Het verleidelijkste idee na een terugval is: "Ik heb het toch al verpest, ik kan net zo goed het weekend doorgaan." Dat is exact hoe een korte terugval een lange ineenstorting wordt.</p>
<p>Stop nu. Vandaag. Eén dag verlies weegt niet op tegen een week verlies, of een maand.</p>
<p><strong>Niet helemaal opgeven.</strong></p>
<p>"Ik heb het geprobeerd, het werkt niet voor mij." Dat is je verslaving die spreekt, niet jij. Hij is bang dat je weer terugkomt op het pad. Hij wil dat je opgeeft.</p>
<p>Geef niet op.</p>
<p><strong>Niet alleen blijven met dit.</strong></p>
<p>Schaamte zegt: vertel het niemand. Doe het stiekem ongedaan. Verzin een verhaal.</p>
<p>Doe het tegenovergestelde. Vertel iemand vandaag.</p>
<p><strong>Niet jezelf afmaken.</strong></p>
<p>Geen interne tirade. Geen lijst maken van waarom je een mislukking bent. Geen vergelijking met andere mensen die het beter doen.</p>
<p>Iemand die in een put valt, klimt eruit. Hij scheldt zichzelf niet eerst een uur uit.</p>

<h2>Wat je vandaag wel doet. Vijf stappen.</h2>
<p><strong>Stap 1: stop het lek opnieuw.</strong></p>
<p>Als je je Cruks-aanmelding ergens hebt omzeild, sluit dan opnieuw. Als je je gokblokkade bij de bank had opgeheven, vraag hem opnieuw aan. Als je apps had teruggezet, verwijder ze.</p>
<p>Direct, vandaag. Niet uitstellen.</p>
<p><strong>Stap 2: vertel het iemand. Eén iemand.</strong></p>
<p>Een partner. Een ouder. Een vriend. Een hulpverlener. De Nationale Hulplijn Gokken op <strong>0800-1995</strong> (gratis, anoniem, 24/7).</p>
<p>Schaamte leeft in stilte. Eén eerlijk gesprek breekt zijn kracht. Niet voor altijd. Wel voor vandaag.</p>
<p><strong>Stap 3: begrijp wat eraan vooraf ging.</strong></p>
<p>Niet om jezelf te kwellen. Om informatie te krijgen.</p>
<p>Pak een pagina. Schrijf op:</p>
<ul>
<li>Wat gebeurde er die dag voor de terugval?</li>
<li>Welke gevoelens had ik?</li>
<li>Welke gedachten kwamen voorbij?</li>
<li>Welke trigger duwde me over de rand?</li>
<li>Wat had ik kunnen doen op dat moment?</li>
</ul>
<p>Misschien was er stress op werk. Misschien een ruzie. Misschien een eenzame avond. Misschien een onverwachte trigger zoals een reclame of een wedstrijd.</p>
<p>Wat het ook was, je weet het nu. En de volgende keer dat dit gebeurt, herken je het.</p>
<p><strong>Stap 4: begin opnieuw met dag 1.</strong></p>
<p>Je streak gaat naar nul. Dat is geen straf. Dat is een feit.</p>
<p>Maar dag 1 is niet hetzelfde als de eerste dag 1. Je weet meer dan toen. Je hebt al maanden bewezen dat je het kunt. Je hebt een terugval gehad en je staat weer op. Dat zegt iets over jou.</p>
<p>Dag 1 is een nieuwe lijn. Niet een verloren begin.</p>
<p><strong>Stap 5: praat met een professional als je dat nog niet doet.</strong></p>
<p>Een terugval is een teken dat je een dimensie mist. Misschien werkte je aanpak voor maanden, maar niet voor wat er nu speelt. Tijd om dat aan te vullen.</p>
<p>Bel de huisarts. Vraag om verwijzing naar verslavingszorg. Jellinek, Tactus, Brijder, Iriszorg: allemaal hebben ze gokverslaving-programma's. De meeste worden vergoed door je zorgverzekering.</p>
<p>Als je al hulp had: ga terug. Vertel je therapeut wat er is gebeurd. Geen oordeel, wel werk.</p>

<h2>Hoe je terugkomt naar je partner of familie</h2>
<p>Als je het ze had verteld en nu een terugval hebt gehad, is dit gesprek extra moeilijk.</p>
<p><strong>Vertel het zelf, wacht niet tot ze het ontdekken.</strong></p>
<p>Niets kapot zoveel vertrouwen als wegdraaien voor de tweede keer. Vertel het binnen 24 uur. Pijnlijk, maar essentieel.</p>
<p><strong>Niet vergoeilijken.</strong></p>
<p>Geen "het was maar één keer". Geen "het was minder dan vroeger". Het is wat het is: een terugval. Erken hem volledig.</p>
<p><strong>Geef ze ruimte voor woede en verdriet.</strong></p>
<p>Ze hebben jou geloofd. Ze hebben hun hoop in je gezet. Hun reactie heeft niets met overdrijving te maken. Het is echte pijn. Laat het er zijn.</p>
<p><strong>Geef geen beloftes die je niet kunt waarmaken.</strong></p>
<p>Niet: "het gebeurt nooit meer". Wel: "ik ga vandaag opnieuw aan de slag, ik bel maandag mijn hulpverlener, ik zorg dat dit niet doorgaat."</p>
<p>Concreet en doenlijk verslaat groots en vaag.</p>
<p><strong>Bied aan dat ze meekijken.</strong></p>
<p>Als ze willen, geef ze inzicht in je rekening. Of in je app waar je je streak bijhoudt. Of in je afspraken bij hulpverlening. Vertrouwen herstel je door transparantie, niet door beloftes.</p>

<h2>Het patroon doorbreken</h2>
<p>Een terugval die alleen blijft, is een ongeluk.</p>
<p>Een terugval die niets verandert, is een waarschuwing.</p>
<p>Vraag jezelf eerlijk: wat moet er anders na deze terugval?</p>
<ul>
<li>Heb je extra hulp nodig die je nog niet had?</li>
<li>Zijn er triggers die te dichtbij staan?</li>
<li>Mist je structuur op bepaalde momenten?</li>
<li>Zijn er emoties die je vermijdt door te gokken?</li>
<li>Loop je met dingen rond die je tegen niemand vertelt?</li>
</ul>
<p>De terugval is informatie. Wat je ermee doet, bepaalt of de volgende komt of niet.</p>

<h2>Je staat weer op. Vandaag.</h2>
<p>Je hebt het al een keer gedaan. Of meer dan een keer.</p>
<p>De afgelopen weken of maanden niet gokken: dat heb je echt gedaan. Dat verdwijnt niet door één terugval.</p>
<p>Wat verdwenen is, is je streak. Niet je vermogen. Niet je richting. Niet wie je geworden bent in de tijd ertussen.</p>
<p>Je staat weer op. Niet omdat het makkelijk is. Omdat de andere optie geen optie is.</p>
<p>Adem in. Verwijder de apps opnieuw. Sluit jezelf opnieuw aan op Cruks. Bel je bank. Bel iemand.</p>
<p>Eén ding tegelijk. Vandaag.</p>
<p>Doorgaan.</p>"""

related10 = (
    rel("/nl/blog/stoppen-met-gokken","Herstel","Stoppen met gokken: een eerlijke gids") +
    rel("/nl/blog/gokken-aan-je-familie-vertellen","Relaties","Gokken aan je familie vertellen") +
    rel("/nl/blog/gokverslaving-en-identiteit","Emotie","Gokverslaving en identiteit: wie ben je zonder de inzet?")
)

html10 = page(
    "nl",
    "Terugval na gokverslaving. Wat nu? | Afterbetting",
    "Terugval na gokverslaving voelt als alles kwijt. Het is het niet. Eerlijk advies over wat te doen, vandaag, zonder schaamte.",
    url10,
    [("nl","https://afterbetting.com/nl/blog/terugval-na-gokverslaving"),("x-default","https://afterbetting.com/nl/blog/terugval-na-gokverslaving")],
    [schema10_article, schema10_bc],
    hero10, body10, related10,
    "Begin opnieuw zonder schaamte.",
    "Op Afterbetting kun je je streak resetten en doorgaan met dagelijkse check-ins, journaal en de crisisknop. Geen oordeel. Alleen vooruit."
)

with open("nl/blog/terugval-na-gokverslaving.html","w",encoding="utf-8") as f:
    f.write(html10)
print("OK: terugval-na-gokverslaving.html")
print("Alle batch 3 bestanden gegenereerd.")
