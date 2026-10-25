# 18 okt 2026: korte knop halverwege elk blog (voor de derde h2), tekst per thema. Veilig om opnieuw te draaien.
import re, glob

THEMES = {
 'naaste': ['my-partner-has', 'mijn-partner-is', 'mijn-kind', 'mijn-vriend', 'omgaan-met-gokverslaafde', 'iemand-anders', 'exclude-someone', 'vader-of-moeder', 'my-parent'],
 'geld': ['chasing-losses', 'gambled-away-paycheck', 'paid-off', 'rebuild-finances', 'snowball', 'geld-terugvragen',
          'gokschuld', 'met-schulden', 'mortgage', 'salaris', 'sneeuwbal', 'verlies-terugwinnen'],
 'drang': ['urges', 'withdrawal', 'what-to-do-instead', 'sleep-after', 'drang', 'afkick', 'hoe-vul-ik', 'slaap',
           'daily-habits', 'dagelijkse', 'alcohol'],
 'blok': ['block-gambling', 'gamstop', 'self-exclusion', 'cruks', 'goksites-blokkeren', 'zelfuitsluiting'],
}
T = {
 'nl': {
  'geld': ('Zie wat je niet meer vergokt', 'Afterbetting rekent elke dag uit hoeveel je niet hebt vergokt en geeft je een overzicht van je geld. Gratis, zonder creditcard.'),
  'drang': ('Drang op dit moment?', 'In de app staat Nu hulp: een korte timer, je eigen redenen om te stoppen en de hulplijn, één tik weg. Gratis.'),
  'blok': ('Een blokkade koopt tijd', 'Wat je met die tijd doet, telt. Afterbetting geeft je avonden en weekenden een vast ritme, met een dagenteller, gewoontes en Nu hulp. Gratis.'),
  'naaste': ('Voor de persoon om wie je geeft', 'Afterbetting geeft iemand die stopt met gokken elke dag houvast: een dagenteller, Nu hulp bij drang en een overzicht van het geld. Gratis.'),
  'basis': ('Stoppen gaat dag voor dag', 'Afterbetting geeft je elke dag houvast: een dagenteller, gewoontes, een dagboek en Nu hulp bij drang. Gratis, zonder creditcard.'),
  'btn': 'Begin gratis'},
 'en': {
  'geld': ('See what you are no longer losing', 'Afterbetting shows every day how much you have not gambled and gives you an overview of your money. Free, no credit card.'),
  'drang': ('Feeling the urge right now?', 'The app has Help now: a short timer, your own reasons to stop and the helpline, one tap away. Free.'),
  'blok': ('A block buys you time', 'What you do with that time counts. Afterbetting gives your evenings and weekends a steady rhythm, with a day counter, habits and Help now. Free.'),
  'naaste': ('For the person you care about', 'Afterbetting gives someone who is stopping gambling something to hold on to every day: a day counter, Help now for urges and an overview of their money. Free.'),
  'basis': ('Stopping happens one day at a time', 'Afterbetting gives you something to hold on to every day: a day counter, habits, a journal and Help now for urges. Free, no credit card.'),
  'btn': 'Start free'},
}
CSS = '''
/* Knop halverwege blogs (18 okt 2026) */
.mid-cta{display:flex;gap:1.25rem;align-items:center;justify-content:space-between;background:var(--clay-bg);border-left:4px solid var(--apricot);border-radius:14px;padding:1.1rem 1.25rem;margin:2rem 0}
.mid-cta strong{display:block;font-size:1.02rem;font-weight:700;color:var(--ink);margin-bottom:.2rem}
.mid-cta span{display:block;font-size:.92rem;line-height:1.5;color:var(--mid)}
.mid-cta a{flex:0 0 auto;background:var(--ink);color:#fff !important;text-decoration:none !important;font-weight:600;font-size:.92rem;padding:.7rem 1.1rem;border-radius:12px;white-space:nowrap}
.mid-cta a:hover{background:#22403A}
@media(max-width:600px){.mid-cta{flex-direction:column;align-items:flex-start;gap:.8rem}}
'''

def theme(slug):
    for k, keys in THEMES.items():
        if any(x in slug for x in keys): return k
    return 'basis'

count = {}
for f in sorted(glob.glob('blog/*.html') + glob.glob('nl/blog/*.html')):
    if f.endswith('index.html'): continue
    s = open(f, encoding='utf-8').read()
    if 'class="mid-cta"' in s: continue
    lang = 'nl' if f.startswith('nl/') else 'en'
    slug = f.split('/')[-1][:-5]; k = theme(slug); title, body = T[lang][k]
    a = s.index('<article class="body">'); b = s.index('</article>', a)
    h2 = [m.start() for m in re.finditer(r'<h2[\s>]', s[a:b])]
    assert len(h2) >= 2, f
    pos = a + (h2[2] if len(h2) >= 3 else h2[-1])
    box = (f'<div class="mid-cta"><div><strong>{title}</strong><span>{body}</span></div>'
           f'<a href="https://app.afterbetting.com/onboarding" rel="noopener" '
           f'onclick="if(window.gtag)gtag(\'event\',\'cta_click\',{{cta_location:\'mid_article\',cta_theme:\'{k}\',page_path:window.location.pathname}})">{T[lang]["btn"]}</a></div>\n')
    s = s[:pos] + box + s[pos:]
    assert '—' not in s
    open(f, 'w', encoding='utf-8').write(s)
    count[k] = count.get(k, 0) + 1
print(count)

th = open('theme.css', encoding='utf-8').read()
if '.mid-cta{' not in th:
    open('theme.css', 'a', encoding='utf-8').write(CSS)
