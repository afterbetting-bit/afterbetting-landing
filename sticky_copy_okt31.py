# 31 okt 2026: tekst van de vaste balk onderaan (#abSticky) per thema. Was overal "Start free in the app".
# Thema komt uit de t= van de knop in de balk. Veilig om opnieuw te draaien.
import glob, re
COPY = {
 'en': {'basis': ('Free app to stop gambling', 'Day counter, help with urges, your money in view.'),
        'drang': ('Help with the urge, one tap away', 'Free app with a short urge timer and your own reasons.'),
        'blok': ('A block buys you time', 'Free app to fill that time: day counter and habits.'),
        'geld': ("See what you're no longer losing", 'Free app with a day counter and money overview.'),
        'naaste': ('For someone who wants to stop', 'A free app they can start today.')},
 'nl': {'basis': ('Gratis app om te stoppen met gokken', 'Dagenteller, hulp bij drang, je geld in beeld.'),
        'drang': ('Hulp bij drang, één tik weg', 'Gratis app met een korte timer en je eigen redenen.'),
        'blok': ('Een blokkade koopt tijd', 'Gratis app om die tijd te vullen: dagenteller en gewoontes.'),
        'geld': ('Zie wat je niet meer vergokt', 'Gratis app met dagenteller en geldoverzicht.'),
        'naaste': ('Voor wie wil stoppen met gokken', 'Een gratis app die hij of zij vandaag kan starten.')},
}
CSS = ('\n/* Vaste balk onderaan: twee regels (31 okt 2026) */\n'
       '.ab-sticky .ab-sticky-text strong{display:block;font-weight:700;line-height:1.3}\n'
       '.ab-sticky .ab-sticky-text small{display:block;font-size:.8rem;font-weight:400;opacity:.85;line-height:1.35;margin-top:.1rem}\n')
n = 0
for f in glob.glob('blog/*.html') + glob.glob('nl/blog/*.html'):
    s = open(f, encoding='utf-8').read()
    m = re.search(r'<span class="ab-sticky-text">(.*?)</span><a href="[^"]*?[?&]t=([a-z]+)', s)
    if not m: continue
    lang = 'nl' if f.startswith('nl/') else 'en'
    t, sub = COPY[lang].get(m.group(2), COPY[lang]['basis'])
    new = f'<span class="ab-sticky-text"><strong>{t}</strong><small>{sub}</small></span>'
    s2 = s[:m.start()] + new + s[m.start() + len('<span class="ab-sticky-text">') + len(m.group(1)) + len('</span>'):]
    if s2 != s:
        open(f, 'w', encoding='utf-8').write(s2); n += 1
th = open('theme.css', encoding='utf-8').read()
if '.ab-sticky .ab-sticky-text strong' not in th:
    open('theme.css', 'a', encoding='utf-8').write(CSS)
print('balk bijgewerkt op', n, "pagina's")
