import json
CSS = open("nl/blog/stoppen-met-gokken.html").read().split("<style>")[1].split("</style>")[0]
GA = '<script async src="https://www.googletagmanager.com/gtag/js?id=G-BC3QG79LQ0"></script><script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag("js",new Date());gtag("config","G-BC3QG79LQ0");</script>'
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,wght@0,300;0,400;1,300&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">'
NAV = '<nav><a href="/nl/" class="logo">after<span>betting</span></a><div class="nav-links"><a href="/nl/#how">Hoe het werkt</a><a href="/nl/#features">Functies</a><a href="/nl/#pricing">Prijzen</a><a href="/nl/blog">Blog</a><a href="https://app.afterbetting.com/login">Inloggen</a></div><a href="https://app.afterbetting.com/onboarding" class="btn">Begin gratis</a></nav>'
CRISIS = '<div class="crisis-footer"><p>Zit je nu in crisis? Bel de <strong>Nationale Hulplijn Gokken: 0800-1995</strong>. Gratis. Anoniem. 24 uur per dag.</p></div>'
FOOTER = '<footer><p>&copy; 2026 Afterbetting &middot; <a href="/nl/">Home</a> <a href="/nl/blog">Blog</a> <a href="/nl/about">Over ons</a> <a href="https://app.afterbetting.com/privacy">Privacy</a> <a href="https://app.afterbetting.com/terms">Voorwaarden</a> <a href="mailto:info@afterbetting.com">Contact</a></p><p style="margin-top:.5rem">Geen medische dienst. Neem contact op met een erkend professional voor klinische ondersteuning.</p></footer>'

slug = "geld-terugvragen-online-casino"
url = f"https://afterbetting.com/nl/blog/{slug}"
title = "Geld terugvragen van een online casino. Wat kan en wat niet"
desc = "Geld terugvragen van een online casino in Nederland. Wat juridisch kan, wat niet, en hoe je het concreet aanpakt. Geen valse hoop, wel duidelijkheid."

sa = json.dumps({"@context":"https://schema.org","@type":"Article","headline":"Geld terugvragen van een online casino. Wat kan en wat niet.","author":{"@type":"Organization","name":"Afterbetting"},"publisher":{"@type":"Organization","name":"Afterbetting","url":"https://afterbetting.com"},"datePublished":"2026-05-09","dateModified":"2026-05-09","inLanguage":"nl","url":url})
sb = json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://afterbetting.com/nl/"},{"@type":"ListItem","position":2,"name":"Blog","item":"https://afterbetting.com/nl/blog"},{"@type":"ListItem","position":3,"name":"Geld terugvragen online casino","item":url}]})

hero = '<section class="hero"><div class="hero-inner"><div class="bc"><a href="/nl/">Home</a> &rarr; <a href="/nl/blog">Blog</a> &rarr; Financieel</div><div class="tag">Financieel</div><h1>Geld terugvragen van een online casino. Wat kan en wat niet.</h1><p style="font-size:1.1rem;color:var(--mid);font-weight:300;line-height:1.7;margin-top:1rem">Vergokt geld terugkrijgen kan soms wel, soms niet. Hangt af van waar je gokte, wanneer, en of je gegokt hebt bij een legale of illegale aanbieder.</p><div class="meta">Door Afterbetting &middot; 9 mei 2026 &middot; 9 min lezen</div></div></section>'

body = """<p>Eerst eerlijk.</p>
<p>Als je verwacht dat je hier leest dat je gewoon je geld terugkrijgt door een mailtje te sturen, dan moet ik je teleurstellen. Voor de meeste mensen ligt het ingewikkelder. Voor sommigen is er wel degelijk een route. Voor anderen niet.</p>
<p>Wat ik ga doen is je de werkelijke situatie geven. Wat juridisch kan in Nederland. Wat al bij rechters is uitgevochten en gewonnen. Wat een doodlopende weg is. En wat je zelf kunt doen, deze week, om te kijken of jouw situatie kans heeft.</p>
<p>Ik ga geen advocaat spelen, want dat ben ik niet. Voor jouw concrete situatie heb je iemand nodig die jouw papieren kan inzien. Maar ik kan je wel helpen om te weten waar je staat voordat je naar zo iemand toe gaat.</p>
<h2>Twee verschillende vragen</h2>
<p>Eerst dit splitsen, want het wordt vaak door elkaar gehaald.</p>
<p><strong>Vraag een: kan ik het geld terugkrijgen dat ik bij een illegale of niet-vergunde aanbieder heb verloren?</strong></p>
<p>Hier is het antwoord vaak ja. Of in elk geval: dit is juridisch gewonnen door anderen, dus het kan.</p>
<p><strong>Vraag twee: kan ik het geld terugkrijgen dat ik bij een legale, in Nederland vergunde aanbieder heb verloren?</strong></p>
<p>Hier is het antwoord meestal nee. Tenzij er bijzondere omstandigheden zijn, bijvoorbeeld dat de aanbieder zijn zorgplicht heeft geschonden.</p>
<p>Belangrijk verschil. We gaan ze apart bespreken.</p>
<h2>De legale Nederlandse markt: wanneer kreeg een aanbieder een vergunning</h2>
<p>Korte geschiedenis voor context.</p>
<p>De Nederlandse online gokmarkt opende officieel op 1 oktober 2021. Vanaf dat moment konden aanbieders een vergunning krijgen van de Kansspelautoriteit (KSA). Voor 1 oktober 2021 was online gokken in Nederland in feite verboden. Dat hield niemand tegen. Buitenlandse partijen boden gewoon Nederlandstalige sites aan en namen Nederlandse spelers aan.</p>
<p>Op die periode (voor oktober 2021) ligt de juridische opening.</p>
<p>Wat hierna komt is geen advies, het is informatie. Voor je eigen situatie ga je naar een advocaat.</p>
<h2>Geld terug bij illegale aanbieders van voor 1 oktober 2021</h2>
<p>Dit is de route waar de meeste juridische winst zit.</p>
<p>De redenering is als volgt. Wat illegaal werd aangeboden, was juridisch nietig. Dat betekent dat de overeenkomst tussen jou en het casino vanaf het begin geen geldige overeenkomst was. Wat geen geldige overeenkomst was, kun je in principe terugvorderen op grond van onverschuldigde betaling.</p>
<p>Nederlandse rechters hebben in de afgelopen jaren in een groeiend aantal zaken in het voordeel van de speler beslist. In sommige zaken ging het om tienduizenden euro's, in andere om honderdduizenden. Niet alle zaken winnen, en niet altijd het volledige bedrag. Maar de juridische lijn is er.</p>
<p>Aanbieders die bekend zijn uit deze periode en bij wie veel zaken lopen of zijn beslecht: Unibet, Bwin, Bet365, Betsson, Betway, Pokerstars, en diverse anderen. Als je daar gegokt hebt voor 1 oktober 2021, is er ten minste reden om je situatie te laten beoordelen.</p>
<p>Wat ze terugvorderbaar maakt:</p>
<ul><li>Je hebt verloren bij een aanbieder zonder Nederlandse vergunning</li><li>De aanbieder richtte zich actief op de Nederlandse markt (Nederlandse taal, iDEAL, Nederlandse marketing)</li><li>Je verlies vond plaats voor 1 oktober 2021</li><li>Je kunt het verlies aantonen met bankafschriften, transactiehistorie, of speelaccounts</li></ul>
<p>Wat je terugkrijgt is je netto verlies, niet je bruto inzet. Dus alles wat je hebt gestort minus alles wat je hebt opgenomen.</p>
<p>Verjaring: in beginsel verjaart een vordering uit onverschuldigde betaling na vijf jaar. Dat ligt juridisch ingewikkelder, sommige rechters rekenen vanaf het moment van betaling, anderen vanaf het moment dat duidelijk werd dat het illegaal was. Hier is een advocaat onmisbaar voor.</p>
<h2>Geld terug bij legale aanbieders na 1 oktober 2021</h2>
<p>Hier ligt het anders.</p>
<p>Een legale aanbieder met een Nederlandse vergunning heeft, zoals iedereen weet, een wettelijke zorgplicht. Hij moet:</p>
<ul><li>Spelersaccounts checken op signalen van problematisch gokken</li><li>Ingrijpen als signalen worden gezien</li><li>Zelf-uitsluiting via Cruks honoreren</li><li>Limieten respecteren die de speler instelt</li><li>Het geld van de speler veilig bewaren</li></ul>
<p>Als de aanbieder die zorgplicht heeft geschonden, kun je een claim hebben. Voorbeelden:</p>
<ul><li>Je hebt jezelf uitgesloten via Cruks en de aanbieder liet je toch spelen</li><li>Je had een dagelijkse stortlimiet ingesteld en de aanbieder gaf je toch toegang tot meer</li><li>Je liet duidelijke signalen zien (uren per dag, snel oplopende inzetten, herhaaldelijke chasing) en de aanbieder ondernam niets</li><li>Een minderjarige kreeg toegang</li><li>Een zelf-uitgesloten speler werd actief teruggemarketet</li></ul>
<p>In die gevallen is er een opening. Maar de bewijslast ligt bij jou en het is meestal complexer dan een illegale-aanbieder zaak. Hier is gespecialiseerd juridisch advies echt nodig.</p>
<p>In gewone, brede zin: "ik heb veel verloren bij een legale aanbieder en wil mijn geld terug omdat ik te veel verloor", dat werkt juridisch niet. Dan was het binnen het toegestane kader.</p>
<h2>Wat je deze week kunt doen</h2>
<p>Concrete stappen, in volgorde.</p>
<p><strong>Stap 1: verzamel je gegevens.</strong></p>
<p>Pak alles wat je hebt:</p>
<ul><li>Bankafschriften van alle jaren waarin je gokte. Met name de jaren voor 1 oktober 2021 als je toen ook online gokte. Vraag bij je bank een uittreksel op van vijf tot tien jaar terug. ABN, ING, Rabobank, SNS en Bunq leveren deze uittreksels op verzoek</li><li>Schermafbeeldingen van je accounts bij gokaanbieders, voor zover je er nog in kunt</li><li>E-mails van bookmakers en casino's met bevestigingen van stortingen, opnames, bonussen</li><li>Eventuele Cruks-registratie of zelf-uitsluitingen die je in het verleden hebt gedaan</li></ul>
<p>Maak een map. Zet alles erin. Ook als je nog niet weet of je een claim hebt.</p>
<p><strong>Stap 2: bepaal je periode en aanbieders.</strong></p>
<p>Maak een lijstje:</p>
<ul><li>Bij welke aanbieders heb ik gespeeld</li><li>In welke periode (jaartal, maand)</li><li>Wat is mijn ruwe schatting van het netto verlies per aanbieder</li><li>Was de aanbieder destijds vergund in Nederland (kijk op kansspelautoriteit.nl voor de huidige vergunninghouders en hun historische data)</li></ul>
<p><strong>Stap 3: beoordeel of je het zelf doet of via een advocaat.</strong></p>
<p>Bij verliezen onder ongeveer 5.000 euro per aanbieder kun je overwegen het zelf op te pakken via een schriftelijke vordering aan de aanbieder. Daar zit een werkmodel achter dat publiek beschikbaar is via verschillende juridische bronnen.</p>
<p>Bij grotere bedragen, of bij meerdere aanbieders, of bij twijfel: ga naar een gespecialiseerd advocaat. Er zijn in Nederland inmiddels tientallen kantoren die zich op dit type zaken hebben gespecialiseerd. Veel werken op no-cure-no-pay basis, dus je betaalt niets als de zaak verloren gaat.</p>
<p>Belangrijk: zoek een advocaat die specifiek ervaring heeft met online gokken-zaken. Niet een algemene civiele advocaat. De materie is specifiek genoeg dat ervaring telt.</p>
<p><strong>Stap 4: dien een schriftelijke vordering in.</strong></p>
<p>Of via je advocaat, of zelf. Inhoud:</p>
<ul><li>Identiteitsgegevens</li><li>Periode van spelen</li><li>Bewijsmateriaal (afschriften, accountoverzichten)</li><li>Bedrag dat je terugvordert (netto verlies)</li><li>Juridische grond (onverschuldigde betaling op basis van nietige overeenkomst, of zorgplichtschending)</li><li>Termijn waarbinnen je antwoord wenst (meestal 14 dagen)</li></ul>
<p>De aanbieder reageert. Soms ontkennend, soms met een schikkingsvoorstel, soms met stilte. Als er stilte komt, kan je advocaat naar de rechter.</p>
<h2>Andere routes (kort)</h2>
<p>Hierbij ook andere routes die je vaak online tegenkomt, met eerlijke duiding.</p>
<p><strong>Chargeback bij je bank.</strong> Als je met creditcard hebt gestort, kun je in beginsel een chargeback aanvragen bij je bank, op grond dat de transactie aan een ongeautoriseerde of illegale aanbieder ging. In de praktijk werkt dit zelden in Nederland voor stortingen die ouder zijn dan een paar maanden. Voor recente stortingen bij illegale aanbieders soms wel. Gewoon vragen kost niets.</p>
<p><strong>Klacht bij de Kansspelautoriteit.</strong> De KSA neemt klachten aan over vergunde aanbieders die hun zorgplicht hebben geschonden. Een klacht leidt zelden tot directe terugbetaling, maar kan wel druk zetten op een aanbieder en kan onderdeel zijn van een dossier dat je later civielrechtelijk inzet. ksa.nl/klacht.</p>
<p><strong>Klacht bij de aanbieder zelf.</strong> Schriftelijke klacht naar de klantenservice van de aanbieder. Soms bieden ze een schikking. Vaak niet. Geen kwaad om te proberen.</p>
<p><strong>Schuldhulpverlening.</strong> Geen route om geld terug te krijgen, wel een route om met je huidige schuld om te gaan. Gemeente, NVVK-aangesloten schuldhulpverlening, of de Nationale Schuldenlijn op 0800-8115. Lees ook: <a href="/nl/blog/gokschuld-aflossen">Gokschuld aflossen, een eerlijk plan zonder valse beloftes</a>.</p>
<h2>Waarvoor je oppast</h2>
<p>Drie waarschuwingen.</p>
<p><strong>Een: bedrijven die per direct geld beloven voor een fee vooraf.</strong></p>
<p>Er zijn online "claim-bureaus" die je hele zaak overnemen tegen een vooraf-vergoeding. Wees voorzichtig. Echte gespecialiseerde advocaten werken vaak op no-cure-no-pay, of bieden een gratis intake. Vooraf grote bedragen vragen is meestal een teken om weg te lopen.</p>
<p><strong>Twee: forums waarop iemand belooft "100 procent terug te krijgen".</strong></p>
<p>Niemand kan dat beloven. Elke zaak is anders. Iedereen die garanties geeft op online gokken-claims, liegt of weet niet waar hij over praat.</p>
<p><strong>Drie: het idee dat je deze tijd in moet steken nu, terwijl je net gestopt bent.</strong></p>
<p>Eerlijk zijn: een claim-procedure kost tijd, mentale ruimte, en haalt je terug naar de jaren waarin je gokte. Je moet bankafschriften doorspitten van vijf jaar geleden. Je herleeft sessies, verliezen, leugens. Voor sommigen is dat te zwaar in de eerste maanden van herstel.</p>
<p>Als je net gestopt bent en deze stap je destabiliseert, doe het later. Een claim van zes of twaalf maanden later is nog steeds een claim. Eerst je eigen herstel, dan deze administratieve strijd.</p>
<h2>Een laatste ding</h2>
<p>Geld terugkrijgen is geen herstel. Het is administratie.</p>
<p>Sommige mensen die hun verliezen geheel of deels terugkrijgen, hebben daar een goed gevoel bij. Anderen merken dat het terugkrijgen iets oprakelt zonder echte voldoening, omdat het echte verlies, de tijd, de relaties, het zelfvertrouwen, niet via een rekening terugkomt.</p>
<p>Doe deze stap omdat het juridisch redelijk is, niet omdat je verwacht dat het je leven herstelt. Je leven herstel je via andere wegen. Niet via een advocaat.</p>
<p>En soms is de eerlijkste conclusie dat je geen kans hebt op teruggave. Ook dat is een antwoord. Niet een om in te blijven hangen. Vooruit kijken, schuld aflossen, leven opbouwen. Dat werkt altijd.</p>
<p>Lees ook: <a href="/nl/blog/sneeuwbalmethode-gokschulden">De sneeuwbalmethode voor gokschulden</a>.</p>
<p style="font-size:0.9rem;color:var(--muted);font-style:italic;margin-top:2rem">Disclaimer: dit artikel is informatie, geen juridisch advies. Voor jouw concrete situatie is een gespecialiseerd advocaat onmisbaar. Geen claims worden in dit artikel gedaan over de uitkomst van individuele zaken.</p>"""

related = '<a href="/nl/blog/gokschuld-aflossen" class="rel-card"><div class="t">Schulden</div><h4>Gokschuld aflossen, een eerlijk plan</h4></a><a href="/nl/blog/sneeuwbalmethode-gokschulden" class="rel-card"><div class="t">Schulden</div><h4>De sneeuwbalmethode voor gokschulden</h4></a><a href="/nl/blog/hoe-stop-ik-met-gokken-met-schulden" class="rel-card"><div class="t">Schulden</div><h4>Hoe stop ik met gokken met schulden</h4></a><a href="/nl/blog/zelfuitsluiting-gokken-werkt-het" class="rel-card"><div class="t">Tools</div><h4>Werkt zelfuitsluiting bij gokken</h4></a>'

html = f'<!DOCTYPE html>\n<html lang="nl">\n<head>\n<meta charset="UTF-8"/>\n<link rel="icon" type="image/svg+xml" href="/favicon.svg">\n<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">\n<meta name="viewport" content="width=device-width,initial-scale=1.0"/>\n<title>{title} | Afterbetting</title>\n<meta name="description" content="{desc}"/>\n<meta name="robots" content="index,follow"/>\n<link rel="canonical" href="{url}"/>\n<link rel="alternate" hreflang="nl" href="{url}"/>\n<link rel="alternate" hreflang="x-default" href="{url}"/>\n<meta property="og:type" content="article"/>\n<meta property="og:locale" content="nl_NL"/>\n<meta property="og:locale:alternate" content="nl_BE"/>\n<meta property="og:url" content="{url}"/>\n<meta property="og:title" content="{title} | Afterbetting"/>\n<meta property="og:description" content="{desc}"/>\n<meta property="og:image" content="https://afterbetting.com/og-image.png"/>\n<meta name="twitter:card" content="summary_large_image"/>\n<meta name="twitter:title" content="{title} | Afterbetting"/>\n<meta name="twitter:description" content="{desc}"/>\n<meta name="twitter:image" content="https://afterbetting.com/og-image.png"/>\n<script type="application/ld+json">{sa}</script>\n<script type="application/ld+json">{sb}</script>\n{GA}\n<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n{FONTS}\n<style>{CSS}</style>\n</head>\n<body>\n{NAV}\n{hero}\n<article class="body">\n{body}\n<div class="cta-block"><h3>Vooruit kijken werkt altijd. Met of zonder claim.</h3><p>Afterbetting helpt je je financien opnieuw op te bouwen. Schuldtracker, wealth calculator, journal, crisis-knop.</p><a href="https://app.afterbetting.com/onboarding">Begin gratis</a></div>\n</article>\n<section class="related"><div class="rel-inner"><h3>Meer lezen</h3><div class="rel-grid">{related}</div></div></section>\n{CRISIS}\n{FOOTER}\n</body></html>'

with open(f"nl/blog/{slug}.html","w") as f:
    f.write(html)
print(f"Done: nl/blog/{slug}.html ({len(html)} bytes)")
