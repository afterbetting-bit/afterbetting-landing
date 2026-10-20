# FAQ-uitbreidingen (20 okt 2026) op basis van autocomplete-zoekvragen. Alleen FAQ, geen nieuwe founder-ervaring.
import json, re

def add_faq(path, items, before, heading=None):
    s = open(path, encoding='utf-8').read()
    if items[0][0] in s:
        print('al gedaan:', path); return
    html = (f'<h2>{heading}</h2>\n' if heading else '') + ''.join(f'<h3>{q}</h3>\n<p>{a}</p>\n' for q, a in items)
    assert s.count(before) == 1, (path, before)
    s = s.replace(before, html + before, 1)
    m = re.search(r'<script type="application/ld\+json">(\{[^<]*"FAQPage"[^<]*\})</script>', s)
    new = [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub(r'<[^>]+>', '', a)}} for q, a in items]
    if m:
        d = json.loads(m.group(1)); d['mainEntity'] += new
        s = s.replace(m.group(1), json.dumps(d, ensure_ascii=False), 1)
    else:
        ld = '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": new}, ensure_ascii=False) + '</script>\n'
        s = s.replace('</head>', ld + '</head>', 1)
    s = re.sub(r'"dateModified": ?"[^"]+"', '"dateModified": "2026-10-20"', s)
    open(path, 'w', encoding='utf-8').write(s)
    print('bijgewerkt:', path, len(items), 'vragen')

add_faq('nl/blog/cruks-opzeggen.html', [
 ('Geldt Cruks ook in België of in het buitenland?',
  'Nee. Cruks is een Nederlands register en geldt alleen voor aanbieders met een Nederlandse vergunning. België heeft een eigen systeem, EPIS. Ga je over de grens naar een casino, dan beschermt je Nederlandse gokstop je daar niet.'),
 ('Vallen loterijen en krasloten onder Cruks?',
  'Nee. Cruks geldt voor online gokken bij aanbieders met een Nederlandse vergunning, speelhallen en Holland Casino. Loten en krasloten uit de winkel vallen er niet onder. Was dat jouw manier van spelen, maak dan ook afspraken over je geld, bijvoorbeeld met een gokblokkade bij je bank.'),
 ('Mijn gokstop is afgelopen maar ik wil hem terug. Kan dat?',
  'Ja. Je kunt je op elk moment opnieuw inschrijven via cruksregister.nl met je DigiD, of met een papieren formulier. Kies dan meteen een langere periode en zet een herinnering in je agenda voor de nieuwe einddatum.'),
], '<h2>Bronnen</h2>')

add_faq('blog/my-partner-has-a-gambling-problem.html', [
 ('My husband is gambling behind my back. What do I do?',
  'Start with facts, not an interrogation. Write down what you have seen: transactions, missing money, the times it happens. Then choose a calm moment and say what you saw and how it affects you. Expect denial at first. Lying is part of how a gambling problem keeps going, not proof that he does not care.'),
 ('Should I leave my husband because of his gambling?',
  'That is your decision and nobody else can make it for you. Do not make it on the day you found out. Protect yourself and any children first, financially and emotionally, and talk to a helpline for family members. Some couples come through this. Some do not. Both outcomes are allowed.'),
 ('Will my partner ever stop gambling?',
  'Many people do stop, often after more than one attempt. What you cannot do is make him stop. What helps most is when he takes the decision himself and puts structure around it: blocks, help from outside and one person he is honest with.'),
 ('Am I responsible for my partner\'s gambling debts?',
  'In the UK you are usually not responsible for debts in his name only. Joint loans, joint accounts and debts you guaranteed are different. A joint account can also link your credit files. If you are unsure, ask a free debt advice service such as StepChange or National Debtline.'),
 ('How do I protect my money from a partner who gambles?',
  'Keep your income in an account in your own name. Use one shared account only for fixed bills. Do not lend money or co-sign anything while he is still gambling. Ask him to turn on a gambling block on his own cards.'),
], '<div class="cta"><h3>They need a system', 'Frequently asked questions')

s = open('blog/my-partner-has-a-gambling-problem.html', encoding='utf-8').read()
dup = '<a href="https://afterbetting.com/blog/how-to-tell-family-about-gambling-problem" class="rel-card"><div class="t">Relationships</div><h4>How to tell someone they have a gambling problem</h4></a>'
if dup in s:
    s = s.replace(dup, '<a href="https://afterbetting.com/blog/partner-found-out-about-my-gambling" class="rel-card"><div class="t">Relationships</div><h4>My partner found out about my gambling</h4></a>')
    open('blog/my-partner-has-a-gambling-problem.html', 'w', encoding='utf-8').write(s)

add_faq('nl/blog/hoe-vul-ik-mijn-tijd-zonder-gokken.html', [
 ('Ik gok uit verveling. Wat helpt?',
  'Verveling is vaak het moment waarop de drang binnenkomt, juist omdat er niets anders is. Wacht niet tot je je verveelt. Plan de lege uren vooraf, het liefst met een ander mens. Houd een korte noodlijst bij de hand voor als het toch stil wordt.'),
 ('Is het normaal dat alles saai voelt na stoppen met gokken?',
  'Ja, dat zeggen veel mensen die gestopt zijn. Gokken gaf spanning op afroep. Gewone dingen voelen daarna een tijd vlak. Dat wordt meestal minder naarmate je langer gestopt bent en je dagen weer een vaste vorm krijgen.'),
], '\n<div class="cta-block"><h3>Een plan voor vanavond</h3>')
