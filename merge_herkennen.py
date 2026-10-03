import re, json, os
NB = '/nl/blog/'
HK, SY, HUB = NB + 'gokverslaving-herkennen', NB + 'gokverslaving-symptomen-en-kenmerken', NB + 'omgaan-met-gokverslaafde-naaste'
TODAY = '2026-10-03'
def rd(f): return open(f, encoding='utf-8').read()
def rep(s, a, b, n=1):
    assert s.count(a) == n, f'{a[:60]!r}: {s.count(a)}x, verwacht {n}'
    return s.replace(a, b)
CARD = lambda href, t, h: f'<a href="{href}" class="rel-card"><div class="t">{t}</div><h4>{h}</h4></a>'
SYCARD = CARD(SY, 'Herkenning', 'Gokverslaving symptomen en kenmerken')
HUBCARD = CARD(HUB, 'Naasten', 'Omgaan met een gokverslaafde naaste')
RC = re.compile(r'<a href="' + HK + r'" class="rel-card">.*?</a>', re.S)
out = {}
s = rd('nl/blog/gokverslaving-symptomen-en-kenmerken.html')
S1 = ('<h2>Wat is een gokverslaving eigenlijk?</h2>\n'
 '<p>Voordat we naar de symptomen gaan, even iets duidelijk maken.</p>\n'
 '<p>Gokverslaving heet officieel "gokstoornis". Het staat in het diagnoseboek voor psychiaters (de DSM-5) als een verslavingsziekte. Geen karakterfout. Geen kwestie van wilskracht. Een ziekte. Zoals alcoholisme een ziekte is.</p>\n'
 '<p>Dat betekent niet dat je hulpeloos bent. Dat betekent dat het te behandelen is. Net als andere verslavingen.</p>\n\n')
S2 = ('<h2>Wat als het over iemand anders gaat?</h2>\n'
 '<p>Misschien lees je dit niet voor jezelf. Misschien herken je je partner, kind, broer, ouder.</p>\n'
 '<p>Dan zijn de signalen vaak nog moeilijker te zien. Want jij ziet niet alles. Maar je voelt het wel.</p>\n'
 '<p>Voorzichtige tip: confronteer niet vanuit boosheid. Zelfs als boosheid terecht is. Verslaving en schaamte zijn een vergrendeld koppel. Aanvallen versterkt de schaamte, en daarmee de verslaving.</p>\n'
 '<p>Wat wel werkt: zorg voor jezelf eerst. Bel OpenOverGokken voor advies hoe je het gesprek kunt voeren. En weet: je kunt niet stoppen voor iemand anders. Alleen zij zelf kunnen dat. Jij kunt wel kaders stellen, eerlijk zijn over de impact, en de deur openhouden voor het gesprek.</p>\n'
 f'<p>Hoe je dat gesprek aangaat en je eigen grenzen bewaakt, lees je in <a href="{HUB}">omgaan met een gokverslaafde naaste</a>.</p>\n\n')
s = rep(s, '<h2>Het verschil tussen symptomen en kenmerken</h2>', S1 + '<h2>Het verschil tussen symptomen en kenmerken</h2>')
s = rep(s, '<h2>Wat als je niet zeker bent</h2>', S2 + '<h2>Wat als je niet zeker bent</h2>')
s = rep(s, f'<p>Lees ook: <a href="{HK}">Gokverslaving herkennen, ook bij jezelf</a>.</p>\n', '')
s, n = RC.subn(HUBCARD, s); assert n == 1
s = rep(s, '"dateModified": "2026-05-16"', f'"dateModified": "{TODAY}"')
assert HK not in s
out['nl/blog/gokverslaving-symptomen-en-kenmerken.html'] = s
s = rd('nl/blog/omgaan-met-gokverslaafde-naaste.html')
P = ['Over partners en kinderen wordt veel geschreven. Over broers, zussen en ouders bijna niets. Terwijl daar vaak het langst wordt gezwegen.',
 'Een broer of zus ken je langer dan wie dan ook. Dat is je kracht en je valkuil. Je ziet het eerder dan anderen. Maar je wordt ook sneller weggezet. "Doe niet zo dramatisch." "Bemoei je met je eigen leven." Ga niet in discussie over vroeger, over wie altijd gelijk had. Blijf bij nu. Wat je ziet. Dat je je zorgen maakt. Dat je er bent.',
 'En leen geen geld. Ook niet even voor de huur. Ook niet omdat het familie is. Juist niet omdat het familie is. Familiegeld voelt veilig om te vragen, en dat maakt het zo makkelijk om er een gat mee te dichten.',
 'Bij een moeder of vader draaien de rollen om. Je bent opgevoed door iemand die nu zelf vastloopt. Erover beginnen voelt ongemakkelijk. Soms zelfs als verraad. Toch is het geen gebrek aan respect om te zeggen wat je ziet. Het is zorg.',
 "Mijn ouders probeerden mij te bereiken in de jaren dat ik gokte. Ik weet hoe dat van de andere kant voelt. Maak het daarom klein. Geen familieberaad aan tafel. Een rustig gesprek, met z'n tweeën.",
 'Zie je dat rekeningen niet meer betaald worden, dat er aanmaningen liggen, of dat een ouder geld leent bij anderen in de familie? Trek dan niet alleen aan de bel. Betrek één ander familielid dat je vertrouwt, en bel OpenOverGokken (0800-2400022) voor advies over hoe je het aanpakt. Gratis en anoniem.']
SEC = '<h2>Als het je broer, zus, moeder of vader is</h2>\n' + ''.join(f'<p>{p}</p>\n' for p in P) + '\n'
s = rep(s, '<h2>Grenzen stellen zonder de relatie op te blazen</h2>', SEC + '<h2>Grenzen stellen zonder de relatie op te blazen</h2>')
s, n = RC.subn(SYCARD, s); assert n == 1
s = rep(s, f'<a href="{HK}">gokverslaving herkennen</a>', f'<a href="{SY}">gokverslaving symptomen en kenmerken</a>')
s, n = re.subn(r'"dateModified": "[0-9-]+"', f'"dateModified": "{TODAY}"', s); assert n <= 1
out['nl/blog/omgaan-met-gokverslaafde-naaste.html'] = s
f = 'nl/blog/mijn-partner-is-gokverslaafd-wat-doe-ik.html'
s = rd(f); s, n = RC.subn(HUBCARD, s); assert n == 1
s = rep(s, f'href="{HK}"', f'href="{SY}"'); out[f] = s
for f in ['eerste-week-stoppen-met-gokken', 'stoppen-met-gokken', 'sportgokken-verslaving', 'mijn-vriend-is-gokverslaafd', 'mijn-kind-is-gokverslaafd', 'wat-doet-gokken-met-je-hersenen']:
    f = f'nl/blog/{f}.html'; s = rd(f)
    s, n = RC.subn(SYCARD, s); assert n == 1, f'{f}: kaart {n}'
    s = s.replace(f'<a href="{HK}">Gokverslaving herkennen: 12 signalen die je niet langer kunt negeren</a>', f'<a href="{SY}">Gokverslaving symptomen en kenmerken</a>')
    s = s.replace(f'href="{HK}"', f'href="{SY}"')
    assert s.count(f'href="{SY}" class="rel-card"') == 1, f'{f}: dubbele kaart'
    out[f] = s
s = rd('nl/blog/index.html')
s, n = re.subn(r'<a href="' + HK + r'" class="blog-card">.*?</a>', '', s, flags=re.S); assert n == 1
out['nl/blog/index.html'] = s
s = rd('nl/index.html')
s = rep(s, f'<a href="{HK}"', f'<a href="{SY}"')
s, n = re.subn(r'(<a href="' + SY + r'"[^>]*><div class="feature"[^>]*><div class="f-title">)[^<]*(</div><p class="f-desc">)[^<]*', r'\1Gokverslaving symptomen en kenmerken\2De eerlijke checklist. Wat je voelt, wat je doet, wat je voor jezelf verbergt.', s); assert n == 1
out['nl/index.html'] = s
for f, s in out.items():
    assert HK + '"' not in s, f'{f}: nog link naar herkennen'
    open(f, 'w', encoding='utf-8').write(s)
sm = rd('sitemap.xml')
sm, n = re.subn(r'  <url>\n    <loc>https://afterbetting.com' + HK + r'</loc>.*?</url>\n\n?', '', sm, flags=re.S); assert n == 1
open('sitemap.xml', 'w', encoding='utf-8').write(sm)
v = json.load(open('vercel.json'))
assert not any(r['source'] == HK for r in v['redirects'])
v['redirects'].insert(1, {'source': HK, 'destination': SY, 'permanent': True})
open('vercel.json', 'w').write(json.dumps(v, indent=2, ensure_ascii=False) + '\n')
os.remove('nl/blog/gokverslaving-herkennen.html')
print('aangepast:', len(out), 'html + sitemap + vercel.json, herkennen verwijderd')
