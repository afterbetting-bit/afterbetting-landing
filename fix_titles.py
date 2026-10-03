import re
NEW = {
 'nl/blog/hoe-lang-duurt-herstel-gokverslaving.html': ("Hoe lang duurt herstel van gokverslaving? De 5 fases",
  "Hoe lang duurt herstel van gokverslaving? De vijf fases die ik doorliep, van de eerste twee weken tot jaar vijf. Wat sneller gaat en wat trager."),
 'blog/how-to-stop-gambling-urges-weekends.html': ("How to Stop Gambling Urges at Night and on Weekends",
  "Friday night and the urge is back. What gets me through evenings, nights and weekends without gambling, from someone 2 years clean."),
 'blog/what-to-do-instead-of-gambling.html': ("What to Do Instead of Gambling: Hobbies That Fill the Gap",
  "Looking for hobbies to replace gambling? What filled my empty evenings in the first year clean, and what to do when nothing feels like enough."),
 'nl/blog/terugval-na-gokverslaving.html': ("Terugval na gokverslaving: wat je vandaag doet",
  "Terugval na gokverslaving voelt als alles kwijt. Het is het niet. Wat je nu niet doet, vijf stappen voor vandaag, en hoe je zonder schaamte verdergaat."),
 'nl/blog/sneeuwbalmethode-gokschulden.html': ("Wat is de sneeuwbalmethode? Gokschulden aflossen",
  "Wat is de sneeuwbalmethode en waarom werkt hij bij gokschulden? Kleinste schuld eerst, met een rekenvoorbeeld en vier valkuilen om te vermijden."),
}
def sub(s, pat, val, need):
    s2, n = re.subn(pat, lambda m: m.group(1) + val + m.group(2), s)
    assert n == need or (need is None and n <= 1), f'{pat}: {n}x'
    return s2
out = {}
for f, (t, d) in NEW.items():
    assert len(t) <= 60 and len(d) <= 155
    s = open(f, encoding='utf-8').read()
    soc = t + (' | Afterbetting' if f.startswith('nl/') else '')
    s = sub(s, r'(<title>)[^<]*(</title>)', t, 1)
    s = sub(s, r'(<meta name="description" content=")[^"]*(")', d, 1)
    s = sub(s, r'(<meta property="og:title" content=")[^"]*(")', soc, None)
    s = sub(s, r'(<meta property="og:description" content=")[^"]*(")', d, None)
    s = sub(s, r'(<meta name="twitter:title" content=")[^"]*(")', soc, None)
    s = sub(s, r'(<meta name="twitter:description" content=")[^"]*(")', d, None)
    out[f] = s
for f, s in out.items():
    open(f, 'w', encoding='utf-8').write(s)
print('titles en meta bijgewerkt:', len(out))
