# 31 okt 2026: interne links naar pagina's op positie 11-25 in GSC (23-29 okt), met de zoekterm als linktekst.
# Alleen als de bronpagina nog niet naar het doel linkt. Zelfde plek als eerdere "Lees ook"-regels. Herhaalbaar.
import re, os
N = '/nl/blog/'; B = 'https://afterbetting.com/blog/'
T = {  # doel: (linktekst, [bronnen])
 N + 'cruks-omzeilen-wat-nu': ('Gokstop omzeilen? Lees dit eerst', ['nl/blog/cruks-opzeggen', 'nl/blog/goksites-blokkeren', 'nl/blog/zelfuitsluiting-gokken-werkt-het']),
 N + 'afkickverschijnselen-gokken': ('Afkickverschijnselen bij stoppen met gokken', ['nl/blog/eerste-week-stoppen-met-gokken', 'nl/blog/stoppen-met-gokken', 'nl/blog/drang-om-te-gokken']),
 N + 'waarom-liegen-gokkers': ('Waarom liegen gokkers?', ['nl/blog/mijn-partner-is-gokverslaafd-wat-doe-ik', 'nl/blog/partner-heeft-mijn-gokken-ontdekt', 'nl/blog/omgaan-met-gokverslaafde-naaste']),
 N + 'hoe-stop-ik-met-gokken-met-schulden': ('Hoe stop ik met gokken als ik schulden heb?', ['nl/blog/gokschuld-aflossen', 'nl/blog/stoppen-met-gokken', 'nl/blog/salaris-vergokt-wat-nu']),
 B + 'how-to-tell-family-about-gambling-problem': ('How to tell your family about your gambling problem', ['blog/partner-found-out-about-my-gambling', 'blog/how-to-stop-gambling']),
 B + 'my-parent-has-a-gambling-problem': ('My dad or mum has a gambling problem', ['blog/where-to-get-help-gambling-addiction']),
 B + 'chasing-losses-gambling': ('Chasing losses: why winning it back never works', ['blog/stop-gambling-when-winning', 'blog/gambled-away-paycheck-what-now']),
 B + 'what-to-do-after-gambling-relapse': ('What to do after a gambling relapse', ['blog/do-gambling-urges-go-away', 'blog/first-30-days-without-gambling']),
 B + 'gambling-addiction-test': ('Gambling addiction test: 9 questions', ['blog/gambling-addiction-symptoms-and-signs', 'blog/how-to-stop-gambling']),
}
DATE = '2026-10-31'; n = 0
for href, (text, sources) in T.items():
    slug = href.rstrip('/').split('/')[-1]
    for src in sources:
        p = src + '.html'
        if not os.path.exists(p): print('ontbreekt:', p); continue
        s = open(p, encoding='utf-8').read()
        if re.search(r'href="[^"]*/' + re.escape(slug) + r'"', s): continue
        label = 'Lees ook' if p.startswith('nl/') else 'Read next'
        m = re.search(r'<div class="(cta-block|cta)">', s) or re.search(r'<aside class="author-box">', s)
        s = s[:m.start()] + f'<p><strong>{label}:</strong> <a href="{href}">{text}</a></p>\n' + s[m.start():]
        s = re.sub(r'"dateModified": ?"[^"]+"', f'"dateModified": "{DATE}"', s)
        open(p, 'w', encoding='utf-8').write(s); n += 1; print(p, '->', slug)
print('links toegevoegd:', n)
