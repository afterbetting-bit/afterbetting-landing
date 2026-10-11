# Zet een voorbeeld van de app op de homepages (EN en NL): een telefoon in de hero en een sectie met drie schermen.
# Voorbeeldgegevens zijn verzonnen ("Sam"), geen echte gebruiker. Veilig om opnieuw te draaien.
import re

def strip(n=40, h=30):
    out = []
    for i in range(n):
        if i == n - 1:
            out.append('<i class="t"></i>')
        else:
            hh = 12 + ((i * 7) % 5) * 3
            op = 0.3 + i / (n - 1) * 0.5
            out.append(f'<i style="height:{hh}px;opacity:{op:.2f}"></i>')
    return '<div class="p-strip" aria-hidden="true">' + ''.join(out) + '</div>'

def wave():
    import math
    out = []
    for i in range(24):
        hh = max(5, round(38 * math.exp(-i / 9) * (0.75 + 0.25 * abs(math.sin(i * 1.3)))))
        out.append(f'<i class="{"d" if i < 7 else ""}" style="height:{hh}px"></i>')
    return '<div class="p-wave" aria-hidden="true">' + ''.join(out) + '</div>'

T = {
 'en': dict(date='Sunday 12 October', big='47 days free', sub='13 more to 60, Sam.', today='Today', of='1 of 4', moods=['Heavy','Low','Okay','Good','Strong'],
            r1=('Habits', '2 of 6'), r2=('Log a spend', '€ 62 a day left'), r3=('Evening question', 'a few lines'),
            s1=('€ 180', 'not gambled this week'), s2=('3 times', 'got through an urge'),
            nav=['Today', 'Habits', 'Help', 'Money', 'Journal'],
            h_top='You got through this 3 times before', h_big='The urge passes. Usually within 20 minutes.', h_btn1='I got through it', h_btn2='15 more minutes',
            h_line='Call the National Gambling Helpline', h_line2='0808 8020 133, free, 24/7',
            m_title='Money', m_tabs=['Overview','Spending','Debts'], m_left='Free to spend in October', m_amt='€ 1.240', m_day='€ 62 a day',
            m_in=('Income', '€ 2.650', 'in on 25 Oct'), m_fix=('Fixed costs', '€ 1.050', '40% of income'),
            aria_hero='Example of the Afterbetting app: the Today screen',
            sec_h='This is what you get', sec_lead='One app for the first hard weeks and for everything after: the urges, the habits and your money. Dark by default, because hard moments often come at night.',
            caps=[('Today', 'Your days free, your next milestone and four small things to do.'),
                  ('Help when the urge hits', 'A timer, a message to your person and the helpline, one tap away.'),
                  ('Your money back in view', 'What is left this month, your fixed costs and your debts going down.')],
            cta='Try Progress free for 7 days', cta_sub='No card needed. After 7 days you choose: free plan or Progress.', note='Example data. Not a real user.'),
 'nl': dict(date='Zondag 12 oktober', big='47 dagen vrij', sub='Nog 13 dagen tot 60, Sam.', today='Vandaag', of='1 van 4', moods=['Zwaar','Matig','Oké','Goed','Sterk'],
            r1=('Gewoonten', '2 van 6'), r2=('Uitgave loggen', '€ 62 per dag vrij'), r3=('Avondvraag', 'een paar regels'),
            s1=('€ 180', 'niet vergokt deze week'), s2=('3 keer', 'drang doorstaan'),
            nav=['Vandaag', 'Gewoonten', 'Hulp', 'Geld', 'Dagboek'],
            h_top='Je hebt dit 3 keer eerder doorstaan', h_big='De drang zakt. Meestal binnen 20 minuten.', h_btn1='Ik ben er doorheen', h_btn2='Nog 15 minuten',
            h_line='Bel OpenOverGokken', h_line2='0800-2400022, gratis en anoniem, dag en nacht',
            m_title='Geld', m_tabs=['Overzicht','Uitgaven','Schulden'], m_left='Vrij te besteden in oktober', m_amt='€ 1.240', m_day='€ 62 per dag',
            m_in=('Inkomen', '€ 2.650', 'binnen op 25 okt'), m_fix=('Vaste lasten', '€ 1.050', '40% van je inkomen'),
            aria_hero='Voorbeeld van de Afterbetting-app: het scherm Vandaag',
            sec_h='Zo ziet de app eruit', sec_lead='Eén app voor de eerste zware weken en alles daarna: de drang, je gewoonten en je geld. Standaard donker, want de zware momenten komen vaak \'s avonds.',
            caps=[('Vandaag', 'Je dagen vrij, je volgende mijlpaal en vier kleine dingen om te doen.'),
                  ('Hulp bij drang', 'Een timer, een bericht aan je vertrouwenspersoon en de hulplijn, met één tik.'),
                  ('Je geld weer in beeld', 'Wat er deze maand over is, je vaste lasten en je schulden die dalen.')],
            cta='Probeer Progress 7 dagen gratis', cta_sub='Geen betaalgegevens nodig. Na 7 dagen kies je zelf: gratis of Progress.', note='Voorbeeldgegevens. Geen echte gebruiker.'),
}

def nav(t, on):
    items = []
    for i, n in enumerate(t['nav']):
        if i == 2:
            items.append(f'<b>{n}</b>')
        else:
            items.append(f'<span class="{"on" if i == on else ""}">{n}</span>')
    return '<div class="p-nav" aria-hidden="true">' + ''.join(items) + '</div>'

def phone_today(t):
    m = ''.join(f'<span class="{"on" if i == 3 else ""}">{x}</span>' for i, x in enumerate(t['moods']))
    rows = ''.join(f'<div class="p-row"><span>{a}</span><span>{b}</span></div>' for a, b in (t['r1'], t['r2'], t['r3']))
    return (f'<div class="ab-phone">'
            f'<div class="p-date">{t["date"]}</div>'
            f'<div><div class="p-big">{t["big"]}</div><div class="p-sub">{t["sub"]}</div></div>'
            f'{strip()}'
            f'<div class="p-card"><div class="p-h">{t["today"]}<span>{t["of"]}</span></div><div class="p-moods">{m}</div>{rows}</div>'
            f'<div class="p-two"><div class="p-card"><div class="p-num g">{t["s1"][0]}</div><div class="p-small">{t["s1"][1]}</div></div>'
            f'<div class="p-card"><div class="p-num">{t["s2"][0]}</div><div class="p-small">{t["s2"][1]}</div></div></div>'
            f'{nav(t, 0)}</div>')

def phone_help(t):
    return (f'<div class="ab-phone">'
            f'<div class="p-date">{t["h_top"]}</div>'
            f'<div class="p-big" style="font-size:26px;letter-spacing:-.8px;line-height:1.1">{t["h_big"]}</div>'
            f'<div class="p-card" style="display:flex;flex-direction:column;gap:12px"><div class="p-timer">12:48</div>{wave()}'
            f'<div class="p-two"><div class="p-btn">{t["h_btn1"]}</div><div class="p-btn o">{t["h_btn2"]}</div></div></div>'
            f'<div class="p-help" style="margin-top:auto;margin-bottom:16px"><strong>{t["h_line"]}</strong>{t["h_line2"]}</div></div>')

def phone_money(t):
    tabs = ''.join(f'<span class="{"on" if i == 0 else ""}">{x}</span>' for i, x in enumerate(t['m_tabs']))
    chart = ('<svg class="p-chart" viewBox="0 0 260 70" aria-hidden="true"><path d="M0 62 L260 8" stroke="#2A3D3A" stroke-width="2" stroke-dasharray="4 5" fill="none"/>'
             '<path d="M0 62 L30 60 L55 57 L80 54 L100 53 L120 48" stroke="#F4B97A" stroke-width="3" fill="none" stroke-linecap="round"/><circle cx="120" cy="48" r="4" fill="#F4B97A"/></svg>')
    a, b = t['m_in'], t['m_fix']
    return (f'<div class="ab-phone">'
            f'<div class="p-big" style="font-size:26px">{t["m_title"]}</div><div class="p-tabs" aria-hidden="true">{tabs}</div>'
            f'<div class="p-card"><div class="p-small">{t["m_left"]}</div><div style="display:flex;align-items:baseline;gap:8px"><div class="p-big" style="font-size:32px">{t["m_amt"]}</div><span class="p-small" style="color:#8ED1B5">{t["m_day"]}</span></div>{chart}</div>'
            f'<div class="p-two"><div class="p-card"><div class="p-small">{a[0]}</div><div class="p-num">{a[1]}</div><div class="p-small">{a[2]}</div></div>'
            f'<div class="p-card"><div class="p-small">{b[0]}</div><div class="p-num">{b[1]}</div><div class="p-small">{b[2]}</div></div></div>'
            f'{nav(t, 3)}</div>')

def section(t, signup):
    figs = ''.join(f'<figure><div role="img" aria-label="{c[0]}">{ph}</div><figcaption><strong>{c[0]}</strong><span>{c[1]}</span></figcaption></figure>'
                   for ph, c in zip((phone_today(t), phone_help(t), phone_money(t)), t['caps']))
    return (f'<!-- app-preview:start -->\n<section class="app-preview" id="app"><div class="ap-inner">'
            f'<h2>{t["sec_h"]}</h2><p class="ap-lead">{t["sec_lead"]}</p><div class="ap-row">{figs}</div>'
            f'<div class="ap-cta"><a href="{signup}" onclick="if(window.gtag)gtag(\'event\',\'cta_click\',{{cta_location:\'app_preview\'}})">{t["cta"]}</a><p>{t["cta_sub"]}</p></div>'
            f'<p class="ap-note">{t["note"]}</p></div></section>\n<!-- app-preview:end -->\n')

SIGNUP = 'https://app.afterbetting.com/onboarding'
for path, lang in (('index.html', 'en'), ('nl/index.html', 'nl')):
    t = T[lang]
    s = open(path, encoding='utf-8').read()
    hero_new = f'<div class="hero-phone" role="img" aria-label="{t["aria_hero"]}">{phone_today(t)}</div>'
    s, n = re.subn(r'<div class="hero-card"[\s\S]*?</div>\s*</div>\s*</div>(?=\s*</section>)', hero_new, s, count=1)
    if n == 0:
        s, n = re.subn(r'<div class="hero-phone"[\s\S]*?</div></div>(?=\s*</section>)', hero_new, s, count=1)
    assert n == 1, (path, 'hero niet gevonden')
    s = re.sub(r'<!-- app-preview:start -->[\s\S]*?<!-- app-preview:end -->\n', '', s)
    i = s.index('<section class="section') if False else s.index('id="pricing"')
    i = s.rindex('<section', 0, i)
    s = s[:i] + section(t, SIGNUP) + s[i:]
    s = s.replace('<div class="badge">✦ ', '<div class="badge">')
    open(path, 'w', encoding='utf-8').write(s)
    print(path, 'bijgewerkt')
