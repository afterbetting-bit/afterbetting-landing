# 18 okt 2026: interne links naar pagina's die dicht bij pagina 1 staan maar weinig links krijgen (audit 18 okt).
# Per bronpagina één regel "Lees ook" vlak voor de slotknop, alleen als de link er nog niet staat.
import re, os
N = 'https://afterbetting.com/nl/blog/'; B = 'https://afterbetting.com/blog/'
T = {  # doel: (ankertekst, [bronnen])
 N+'cruks-opzeggen': ('Cruks eerder opzeggen: hoe het werkt en wat je eerst leest', ['zelfuitsluiting-gokken-werkt-het','goksites-blokkeren','stoppen-met-gokken','terugval-na-gokverslaving','drang-om-te-gokken','eerste-week-stoppen-met-gokken']),
 N+'cruks-omzeilen-wat-nu': ('Cruks of je gokstop omzeilen: wat nu?', ['zelfuitsluiting-gokken-werkt-het','terugval-na-gokverslaving','salaris-vergokt-wat-nu','hoe-stop-ik-met-gokken-met-schulden']),
 N+'goksites-blokkeren': ('goksites en gokken blokkeren op je telefoon, laptop en bij je bank', ['eerste-week-stoppen-met-gokken','salaris-vergokt-wat-nu','eerste-30-dagen-zonder-gokken']),
 N+'gokken-depressie-en-angst': ('gokken, depressie en angst', ['gokverslaving-hulp-zoeken','afkickverschijnselen-gokken','slaapproblemen-stoppen-met-gokken','terugval-na-gokverslaving','gokverslaving-en-identiteit']),
 N+'afkickverschijnselen-gokken': ('afkickverschijnselen bij stoppen met gokken', ['eerste-week-stoppen-met-gokken','eerste-30-dagen-zonder-gokken','slaapproblemen-stoppen-met-gokken','drang-om-te-gokken']),
 N+'mijn-vriend-is-gokverslaafd': ('mijn vriend of vriendin is gokverslaafd', ['omgaan-met-gokverslaafde-naaste','mijn-partner-is-gokverslaafd-wat-doe-ik','waarom-liegen-gokkers']),
 N+'eerste-30-dagen-zonder-gokken': ('de eerste 30 dagen zonder gokken', ['eerste-week-stoppen-met-gokken','stoppen-met-gokken','hoe-lang-duurt-herstel-gokverslaving']),
 B+'gambling-depression-and-anxiety': ('gambling, depression and anxiety', ['where-to-get-help-gambling-addiction','gambling-withdrawal-symptoms','sleep-after-stopping-gambling','what-to-do-after-gambling-relapse','gambling-addiction-identity-loss']),
 B+'casino-not-on-gamstop': ('found a casino not on GamStop? Read this first', ['block-gambling-sites-and-payments','what-to-do-after-gambling-relapse','do-gambling-urges-go-away']),
 B+'cancel-gamstop-early': ('can you cancel GamStop early?', ['block-gambling-sites-and-payments','what-to-do-after-gambling-relapse','how-to-stop-gambling-urges-weekends']),
 B+'first-week-without-gambling': ('your first week without gambling', ['first-30-days-without-gambling','gambling-withdrawal-symptoms','how-long-gambling-recovery-takes']),
 B+'partner-found-out-about-my-gambling': ('my partner found out about my gambling', ['how-to-tell-family-about-gambling-problem','gambling-addict-lying']),
}
added = 0
for target, (anchor, sources) in T.items():
    nl = '/nl/blog/' in target
    for src in sources:
        f = ('nl/blog/' if nl else 'blog/') + src + '.html'
        if not os.path.exists(f): print('ontbreekt', f); continue
        s = open(f, encoding='utf-8').read()
        if f'href="{target}"' in s or f'href="{target.replace("https://afterbetting.com","")}"' in s: continue
        a = s.index('<article class="body">')
        m = re.search(r'<div class="(cta|cta-block)">', s[a:])
        if not m: print('geen cta', f); continue
        c = a + m.start()
        line = (f'<p><strong>Lees ook:</strong> <a href="{target}">{anchor}</a>.</p>\n' if nl else
                f'<p><strong>Also read:</strong> <a href="{target}">{anchor[0].upper() + anchor[1:]}</a>.</p>\n')
        if nl: line = line.replace(f'>{anchor}<', f'>{anchor[0].upper() + anchor[1:]}<')
        # meerdere "Lees ook" achter elkaar samenvoegen
        prev = re.search(r'<p><strong>(Lees ook|Also read):</strong> (.*?)\.</p>\n$', s[:c])
        if prev:
            s = s[:prev.start()] + f'<p><strong>{prev.group(1)}:</strong> {prev.group(2)} · <a href="{target}">{anchor[0].upper() + anchor[1:]}</a>.</p>\n' + s[c:]
        else:
            s = s[:c] + line + s[c:]
        assert '—' not in s
        open(f, 'w', encoding='utf-8').write(s); added += 1
print('links toegevoegd:', added)
