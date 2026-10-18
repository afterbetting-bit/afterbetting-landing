# Voegt ?van= toe aan links naar de aanmelding, zodat de app weet waar iemand vandaan komt (18 okt 2026). Na elke nieuwe pagina draaien.
import glob
src = open('add_mid_cta_okt18.py', encoding='utf-8').read(); ns = {}; exec(src[:src.index('T = {')], ns)
def theme(slug):
    for k, keys in ns['THEMES'].items():
        if any(x in slug for x in keys): return k
    if 'vergokt' in slug or 'lost-gambling' in slug: return 'geld'
    if 'liegen' in slug or 'lying' in slug: return 'naaste'
    return 'basis'
n = 0
for f in glob.glob('blog/*.html') + glob.glob('nl/blog/*.html') + ['index.html', 'nl/index.html', 'about.html', 'nl/about.html', '404.html']:
    s = open(f, encoding='utf-8').read()
    if f == '404.html': q = '?van=404'
    elif f in ('index.html', 'nl/index.html'): q = '?van=home'
    elif f.endswith('about.html'): q = '?van=about'
    elif f.endswith('index.html'): q = '?van=blogindex'
    else: q = '?van=blog&t=' + theme(f.split('/')[-1][:-5])
    s2 = s.replace('href="https://app.afterbetting.com/onboarding"', 'href="https://app.afterbetting.com/onboarding' + q + '"')
    if s2 != s: open(f, 'w', encoding='utf-8').write(s2); n += 1
print('bijgewerkt:', n)
