# 17 okt 2026: losse vertrouwensstrip onderaan vervangen door een blok van 4 punten direct na de prijzen. Alle 5 homepages.
import re
ICONS = [
    '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg>',
    '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M5.6 5.6l12.8 12.8"/></svg>',
    '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12.5l5 5L20 6.5"/></svg>',
    '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 12a8 8 0 1 1-2.3-5.6"/><path d="M20 4v4h-4"/></svg>',
]
T = {
 'en': ('Your recovery stays yours', [
   ('Private by default', 'Only you see your journal and numbers. Encrypted in transit and at rest, in a database in the EU. GDPR compliant.'),
   ('No ads, no selling', 'We never show you ads and never sell your data.'),
   ('Free stays free', 'Day counter, Recovery kit and Help now stay free. No credit card needed.'),
   ('Cancel any time', 'Plus is monthly or yearly. You stop it yourself in a few clicks.')]),
 'nl': ('Jouw herstel blijft van jou', [
   ('Alleen voor jou', 'Alleen jij ziet je dagboek en cijfers. Versleuteld verzonden en opgeslagen, in een database in de EU. Volgens de AVG.'),
   ('Geen reclame, geen verkoop', 'We tonen nooit advertenties en verkopen je gegevens niet.'),
   ('Gratis blijft gratis', 'Dagenteller, Herstelkit en Nu hulp blijven gratis. Zonder creditcard.'),
   ('Altijd opzegbaar', 'Plus per maand of per jaar. Opzeggen doe je zelf in een paar klikken.')]),
 'de': ('Deine Genesung gehört dir', [
   ('Privat von Anfang an', 'Nur du siehst dein Tagebuch und deine Zahlen. Verschlüsselt übertragen und gespeichert, in einer Datenbank in der EU. DSGVO-konform.'),
   ('Keine Werbung, kein Verkauf', 'Wir zeigen dir nie Werbung und verkaufen deine Daten nicht.'),
   ('Kostenlos bleibt kostenlos', 'Tageszähler und Hilfe-Kit bleiben kostenlos. Ohne Kreditkarte.'),
   ('Jederzeit kündbar', 'Plus monatlich oder jährlich. Du kündigst selbst mit wenigen Klicks.')]),
 'fr': ('Ton rétablissement t’appartient', [
   ('Privé par défaut', 'Toi seul vois ton journal et tes chiffres. Chiffré en transit et au repos, dans une base de données dans l’UE. Conforme au RGPD.'),
   ('Pas de pub, pas de vente', 'Nous ne te montrons jamais de publicité et ne vendons jamais tes données.'),
   ('Le gratuit reste gratuit', 'Le compteur de jours et le kit de secours restent gratuits. Sans carte bancaire.'),
   ('Résiliable à tout moment', 'Plus au mois ou à l’année. Tu arrêtes toi-même en quelques clics.')]),
 'es': ('Tu recuperación es tuya', [
   ('Privado por defecto', 'Solo tú ves tu diario y tus cifras. Cifrado en tránsito y en reposo, en una base de datos en la UE. Cumple el RGPD.'),
   ('Sin anuncios, sin vender datos', 'Nunca te mostramos anuncios y nunca vendemos tus datos.'),
   ('Lo gratis sigue gratis', 'El contador de días y el kit de ayuda siguen gratis. Sin tarjeta.'),
   ('Cancela cuando quieras', 'Plus mensual o anual. Lo cancelas tú mismo en unos clics.')]),
}
FILES = {'en': 'index.html', 'nl': 'nl/index.html', 'de': 'de/index.html', 'fr': 'fr/index.html', 'es': 'es/index.html'}
CSS = '''
/* Vertrouwensblok na de prijzen (17 okt 2026) */
.assure{padding:3rem 1.5rem;background:var(--cream);border-top:1px solid var(--border)}
.assure-inner{max-width:1100px;margin:0 auto}
.assure h2{font-size:1.35rem;font-weight:700;letter-spacing:-0.02em;text-align:center;margin:0 0 1.75rem;color:var(--dark)}
.assure-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:1rem}
.assure-item{background:#fff;border:1px solid var(--border);border-radius:16px;padding:1.25rem 1.2rem}
.assure-item svg{width:22px;height:22px;fill:none;stroke:var(--green);stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round;margin-bottom:.6rem}
.assure-item strong{display:block;font-size:.98rem;font-weight:600;color:var(--dark);margin-bottom:.3rem}
.assure-item span{display:block;font-size:.86rem;line-height:1.55;color:var(--muted)}
@media(max-width:900px){.assure-grid{grid-template-columns:1fr 1fr}}
@media(max-width:520px){.assure-grid{grid-template-columns:1fr}.assure{padding:2.25rem 1rem}}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]) .assure-item{background:var(--surface,#172524)}}
'''

def block(lang):
    h, items = T[lang]
    cards = ''.join(f'<div class="assure-item">{ICONS[i]}<strong>{t}</strong><span>{d}</span></div>' for i, (t, d) in enumerate(items))
    return f'\n<section class="assure" aria-label="{h}"><div class="assure-inner"><h2>{h}</h2><div class="assure-grid">{cards}</div></div></section>\n'

for lang, f in FILES.items():
    s = open(f, encoding='utf-8').read()
    if 'class="assure"' in s:
        s = re.sub(r'\n<section class="assure"[\s\S]*?</section>\n', '\n', s, count=1)
    old = re.search(r'<section class="trust">[\s\S]*?</section>\n?', s)
    assert old, f
    s = s.replace(old.group(0), '', 1)
    a = s.index('id="pricing"'); b = s.index('</section>', a) + len('</section>')
    s = s[:b] + block(lang) + s[b:]
    assert '—' not in s
    open(f, 'w', encoding='utf-8').write(s)
    print('ok', f)

th = open('theme.css', encoding='utf-8').read()
if '.assure{' not in th:
    open('theme.css', 'a', encoding='utf-8').write(CSS)
    print('css toegevoegd')
