# 8 nov 2026: afkickverschijnselen-gokken / gambling-withdrawal-symptoms v2 (founder: direct live zetten).
# Kort antwoord, "afkicken van gokken" in title/H2/FAQ, alcohol + lege uren (bevestigd), app-kaart, FAQ, US-hulplijnen.
import json, re
DATE = '2026-11-08'
OC = "onclick=\"if(window.gtag)gtag('event','cta_click',{cta_location:'app_card',cta_theme:'drang',page_path:location.pathname})\""
URL = 'https://app.afterbetting.com/onboarding?van=blog&t=drang'
def card(label, quote, meta, btn, note):
    return (f'<div class="app-card"><div class="app-card-screen"><span class="app-card-label">{label}</span>'
            f'<p class="app-card-quote">{quote}</p><div class="app-card-timer">15:00</div><p class="app-card-meta">{meta}</p></div>'
            f'<a class="app-card-btn" href="{URL}" rel="noopener" {OC}>{btn}</a><p class="app-card-note">{note}</p></div>')

P = {
 'nl/blog/afkickverschijnselen-gokken.html': dict(
  title='Afkickverschijnselen bij gokken: zo verloopt het afkicken',
  desc='Afkicken van gokken: leegte, onrust, slecht slapen en triggers. Wat ik merkte na het stoppen, hoe lang het duurde en wat hielp. Van een ex-gokker.',
  edits=[
   ('terechtkunt.</p>\n', 'terechtkunt.</p>\n<div class="answer-box" id="kort-antwoord"><h2>Het korte antwoord</h2><p>Afkicken van gokken gaat voor veel mensen gepaard met onrust, leegte, slecht slapen, prikkelbaarheid en steeds terugkerende gedachten aan gokken. Meestal zijn de eerste weken het zwaarst. Daarna wordt het stap voor stap minder. Wat helpt: je avonden en weekenden vooraf invullen, alles blokkeren wat je kunt, één persoon inlichten en een vast ritme. Gaat het slecht met je, bel dan je huisarts of OpenOverGokken (0800-2400022, gratis, dag en nacht).</p></div>\n'),
   ('Het ene moment was er niets, het volgende moment dacht ik aan een weddenschap.</p>\n', 'Het ene moment was er niets, het volgende moment dacht ik aan een weddenschap.</p>\n<p>Twee dingen maakten het bij mij duidelijk erger: alcohol en lege uren. Na een paar drankjes waren mijn voornemens minder sterk. En een dag zonder invulling was een gevaarlijke dag. Meer daarover in <a href="/nl/blog/gokken-en-alcohol">gokken en alcohol</a>.</p>\n'),
   ('<h2>Hoe lang duurt het?</h2>', '<h2>Hoe lang duurt afkicken van gokken?</h2>'),
   ('drang om te gokken, wat je nu doet</a>.</p>\n', 'drang om te gokken, wat je nu doet</a>.</p>\n'
    + card('Nu hulp, met één tik', '"Je hebt dit 3 keer eerder doorstaan. De drang zakt. Hij komt op, piekt en zakt."',
           'Een timer, je eigen reden om te stoppen, een bericht aan je vertrouwenspersoon en de hulplijn.',
           'Probeer Nu hulp gratis', 'Voorbeeld. De basis van Afterbetting is gratis, zonder betaalgegevens.') + '\n'),
  ],
  faq_after='<h3>Wanneer moet ik hulp zoeken?</h3>',
  faq=[
   ('Wat is afkicken van gokken?', 'Afkicken is de periode na het stoppen waarin je went aan een leven zonder gokken. Je mist de spanning en het ritme dat gokken gaf, en dat merk je als onrust, leegte en drang. Meer over stoppen in <a href="/nl/blog/stoppen-met-gokken">stoppen met gokken: hoe stop je echt?</a>'),
   ('Kun je lichamelijke klachten krijgen als je stopt met gokken?', 'Sommige mensen beschrijven ook lichamelijke onrust, zoals gespannen spieren, hoofdpijn of slecht slapen. Dat verschilt sterk per persoon. Heb je lichamelijke klachten, bespreek ze dan met je huisarts.'),
   ('Kun je in één keer stoppen met gokken?', 'Ja. Bij gokken werkt in één keer stoppen (cold turkey) meestal beter dan minderen, omdat elke kleine inzet de drang levend houdt. Reken wel op een paar zware weken en zorg dat je die van tevoren invult.'),
  ]),
 'blog/gambling-withdrawal-symptoms.html': dict(
  title='Gambling withdrawal symptoms: what to expect and how long',
  desc='What gambling withdrawal feels like: emptiness, restlessness, poor sleep, triggers. What I noticed after stopping, how long it lasted and what helped.',
  edits=[
   ('where else to go.</p>\n', 'where else to go.</p>\n<div class="answer-box" id="short-answer"><h2>The short answer</h2><p>Gambling withdrawal is what many people go through in the first weeks after stopping: restlessness, emptiness, poor sleep, irritability and thoughts of gambling that keep coming back. The first weeks are usually the hardest, and then it eases step by step. What helps: plan your evenings and weekends in advance, block everything you can, tell one person and keep a steady routine. If you are struggling, talk to your doctor or call a free helpline (UK 0808 8020 133, US 1-800-MY-RESET).</p></div>\n'),
   ('One minute there was nothing, the next I was thinking about a bet.</p>\n', 'One minute there was nothing, the next I was thinking about a bet.</p>\n<p>Two things made it clearly worse for me: alcohol and empty hours. A few drinks and my plans got weaker. And a day with nothing in it was a dangerous day. More on that in <a href="/blog/gambling-and-alcohol">gambling and alcohol</a>.</p>\n'),
   ('do gambling urges go away</a>.</p>\n', 'do gambling urges go away</a>.</p>\n'
    + card('Help now, one tap away', '"You got through this 3 times before. The urge passes. It rises, peaks and fades."',
           'A timer, your own reason to stop, a message to someone you trust and the helpline.',
           'Try Help now free', "Example. Afterbetting's basics are free, no card needed.") + '\n'),
   ('call Samaritans on 116 123, or 999 in an emergency.</p>', 'call Samaritans on 116 123, or 999 in an emergency. In the US, call or text 1-800-MY-RESET for gambling help, or call or text 988 if you are thinking about suicide.</p>'),
  ],
  faq_after='<h3>When should I get help?</h3>',
  faq=[
   ('What is gambling withdrawal?', 'It is the period after you stop gambling when you get used to life without it. You miss the excitement and the rhythm gambling gave you, and that shows up as restlessness, emptiness and urges. More on stopping in <a href="/blog/how-to-stop-gambling">how to stop gambling</a>.'),
   ('Can gambling withdrawal cause physical symptoms?', 'Some people describe physical restlessness too, such as tense muscles, headaches or poor sleep. It differs a lot from person to person. If you have physical symptoms, talk to your doctor.'),
   ('Should I quit gambling cold turkey?', 'For gambling, stopping completely usually works better than cutting down, because every small bet keeps the urge alive. Expect a few hard weeks and plan them in advance.'),
  ]),
}

for f, c in P.items():
    s = open(f, encoding='utf-8').read()
    if 'answer-box' in s: print('al gedaan', f); continue
    for old, new in c['edits']:
        assert old in s, (f, old[:60]); s = s.replace(old, new, 1)
    s = re.sub(r'<title>[^<]*</title>', f"<title>{c['title']}</title>", s)
    for k in ('og:title', 'twitter:title'):
        s = re.sub(r'(<meta (?:property|name)="%s" content=")[^"]*' % k, lambda m: m.group(1) + c['title'], s)
    for k in ('description', 'og:description', 'twitter:description'):
        s = re.sub(r'(<meta (?:property|name)="%s" content=")[^"]*' % k, lambda m: m.group(1) + c['desc'], s)
    i = s.index('</p>', s.index(c['faq_after'], s.index('<article'))) + 4
    s = s[:i] + '\n' + '\n'.join(f'<h3>{q}</h3>\n<p>{a}</p>' for q, a in c['faq']) + s[i:]
    def fix(m):
        j = json.loads(m.group(1))
        if j.get('@type') == 'FAQPage':
            j['mainEntity'] += [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': re.sub('<[^>]+>', '', a)}} for q, a in c['faq']]
        elif j.get('@type') == 'Article':
            j['dateModified'] = DATE; j['description'] = c['desc']
        else: return m.group(0)
        return '<script type="application/ld+json">' + json.dumps(j, ensure_ascii=False) + '</script>'
    s = re.sub(r'<script type="application/ld\+json">(.*?)</script>', fix, s, flags=re.S)
    open(f, 'w', encoding='utf-8').write(s); print('klaar', f, len(c['title']), len(c['desc']))
