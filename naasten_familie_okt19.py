# 19 okt 2026: founder-ervaring (moeder, stiefvader, oom) in de naasten-hub. Tekst door founder goedgekeurd.
import re
from opknap_en import md
p = 'nl/blog/omgaan-met-gokverslaafde-naaste.html'
s = open(p, encoding='utf-8').read()
marker = '<h2>Je eigen mentale ruimte bewaken</h2>'
if 'data-familie' not in s:
    block = md('''
## Hoe het bij mijn familie ging

Mijn moeder had er het meest moeite mee. Ze zocht naar hulp voor zichzelf en hoe ze met situaties moest omgaan, maar vond weinig. Bijna alles ging over de gokker, niet over de mensen eromheen.

Mijn stiefvader worstelde vooral in de periode erna. Ook toen ik gestopt was, vond hij het moeilijk om te geloven wat ik zei. Dat begrijp ik. Na jaren van leugens komt vertrouwen niet terug met één gesprek.

Mijn oom was een rots in de branding. Hij oordeelde niet, bleef open en was er gewoon. Dat hielp meer dan elk advies.

Daarom staat op deze pagina ook wat jij voor jezelf kunt doen. Jij hebt net zo goed steun nodig.
''')
    s = s.replace(marker, '<div data-familie></div>\n' + block + marker, 1)
s = re.sub(r'"dateModified": ?"[0-9-]+"', '"dateModified": "2026-10-19"', s)
assert '—' not in s
open(p, 'w', encoding='utf-8').write(s); print('ok')
