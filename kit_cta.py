A = '<a href="https://app.afterbetting.com/onboarding" onclick="gtag(\'event\',\'cta_click\',{cta_location:\'kit_inline\',page_path:location.pathname})">'
P = '<p class="kit-cta" style="background:#EEF5F2;border:1px solid #C2D8D0;border-radius:12px;padding:1rem 1.2rem">'
ITEMS = [
 ('blog/how-to-stop-gambling-urges-weekends.html', '<h3>Track how you feel after</h3>',
  P + '<strong>Need something for those minutes right now?</strong> The free Recovery kit in the Afterbetting app has five short exercises built for this moment: surf the urge, a HALT check, play the film to the end, ' + A + 'delay it 15 minutes with a timer</a>, and box breathing. Free, no credit card needed.</p>\n'),
 ('blog/first-30-days-without-gambling.html', '<h2>Days 8 to 14: The fog lifts slightly</h2>',
  P + '<strong>For the hardest moments of week one:</strong> the free Recovery kit in the Afterbetting app has five short exercises for when an urge hits, including a 15-minute delay timer and box breathing. ' + A + 'Open it for free</a>, no credit card needed.</p>\n'),
 ('nl/blog/terugval-na-gokverslaving.html', '<h2>Hoe je terugkomt naar je partner of familie</h2>',
  P + '<strong>Komt de drang vandaag terug?</strong> In de gratis Herstelkit in de app staan vijf korte oefeningen voor precies dat moment, zoals de HALT-check en ' + A + '15 minuten uitstellen met een timer</a>. Gratis, zonder betaalgegevens.</p>\n'),
 ('nl/blog/stoppen-met-gokken.html', '<h2>De rol van schaamte',
  P + '<strong>Wat doe je als de drang in die eerste 24 uur opkomt?</strong> Daarvoor bouwde ik de gratis Herstelkit in de app: vijf korte oefeningen, zoals surfen op de drang, de HALT-check en ' + A + '15 minuten uitstellen met een timer</a>. Gratis, zonder betaalgegevens.</p>\n'),
 ('nl/blog/eerste-week-stoppen-met-gokken.html', '<h2>Dag 5 en 6. De leegte.</h2>',
  P + '<strong>Voor die eerste echte craving:</strong> in de gratis Herstelkit in de app staan vijf korte oefeningen die je er doorheen helpen, zoals box-ademhaling en ' + A + '15 minuten uitstellen met een timer</a>. Gratis, zonder betaalgegevens.</p>\n'),
]
out = {}
for f, anchor, block in ITEMS:
    s = open(f, encoding='utf-8').read()
    assert 'kit_inline' not in s, f'{f}: staat er al'
    assert s.count(anchor) == 1, f'{f}: anker {s.count(anchor)}x'
    out[f] = s.replace(anchor, block + anchor)
for f, s in out.items():
    open(f, 'w', encoding='utf-8').write(s)
print('herstelkit-verwijzing toegevoegd in', len(out), 'artikelen')
