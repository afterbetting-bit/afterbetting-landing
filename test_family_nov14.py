# 14 nov 2026: gambling-addiction-test (quiz in title, FAQ) en how-to-tell-family (sectie ouders). Veilig om opnieuw te draaien.
import json, re
DATE = '2026-11-14'

def meta(s, title, desc):
    s = re.sub(r'<title>[^<]*</title>', f'<title>{title}</title>', s)
    for k in ('og:title', 'twitter:title'):
        s = re.sub(r'(<meta (?:property|name)="%s" content=")[^"]*' % k, lambda m: m.group(1) + title, s)
    if desc:
        for k in ('description', 'og:description', 'twitter:description'):
            s = re.sub(r'(<meta (?:property|name)="%s" content=")[^"]*' % k, lambda m: m.group(1) + desc, s)
    return s

def schema(s, faq=None, desc=None):
    def fix(m):
        j = json.loads(m.group(1))
        if j.get('@type') == 'FAQPage' and faq:
            names = {e['name'] for e in j['mainEntity']}
            j['mainEntity'] += [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': re.sub('<[^>]+>', '', a)}} for q, a in faq if q not in names]
        elif j.get('@type') == 'Article':
            j['dateModified'] = DATE
            if desc: j['description'] = desc
        else: return m.group(0)
        return '<script type="application/ld+json">' + json.dumps(j, ensure_ascii=False) + '</script>'
    return re.sub(r'<script type="application/ld\+json">(.*?)</script>', fix, s, flags=re.S)

# 1. Test
F = 'blog/gambling-addiction-test.html'
s = open(F, encoding='utf-8').read()
if 'Is this the same as a gambling quiz' not in s:
    T = 'Gambling addiction test and quiz: 9 questions, anonymous'
    D = 'Free gambling addiction test and quiz: 9 questions about the last 12 months, based on the PGSI questionnaire. Anonymous, two minutes, honest next steps.'
    s = meta(s, T, D)
    Q = [('Is this the same as a gambling quiz or questionnaire?', 'Yes. People call it a gambling quiz, a gambling questionnaire or a self-assessment. This one uses the nine questions of the Problem Gambling Severity Index (PGSI), a questionnaire that is widely used to screen for gambling problems. It is not a diagnosis.')]
    anchor = 'I was a sports bettor for 8 years myself.</p>\n'
    assert anchor in s
    s = s.replace(anchor, anchor + ''.join(f'<h3>{q}</h3>\n<p>{a}</p>\n' for q, a in Q), 1)
    s = schema(s, Q, D)
    open(F, 'w', encoding='utf-8').write(s); print('test klaar', len(T), len(D))

# 2. Ouders
F = 'blog/how-to-tell-family-about-gambling-problem.html'
s = open(F, encoding='utf-8').read()
if 'id="telling-your-parents"' not in s:
    SEC = ('<h2 id="telling-your-parents">Telling your parents</h2>\n'
     '<p>A lot of people who search for this are in their late teens or early twenties, and the people they dread telling most are their mum or dad. If that is you, a few things help.</p>\n'
     '<ul>\n'
     '<li><strong>Pick a calm moment, not a crisis.</strong> Not right after a big loss, not when they have just found a bank statement. A quiet evening, or a walk, where nobody has to rush off.</li>\n'
     '<li><strong>Lead with the problem, then the numbers.</strong> "I have a gambling problem and I want to stop" first. The amount and any debt second. Know your real number beforehand; the <a href="/blog/how-much-have-i-lost-gambling">gambling loss calculator</a> helps.</li>\n'
     '<li><strong>Bring a first step you have already taken.</strong> You self-excluded, you installed a blocker, you called a helpline. It shows them you are serious and gives them something to hold on to. See <a href="/blog/block-gambling-sites-and-payments">how to block gambling sites</a>.</li>\n'
     '<li><strong>Expect fear to come out as anger.</strong> Parents often react with shouting, questions about money or "how could you". That is usually worry. Let the first reaction pass and give them time; the second conversation is often much better.</li>\n'
     '<li><strong>Ask for one specific thing.</strong> Help keeping your money out of reach for a while, someone to call on a bad night, or company when you see a GP or counsellor. A concrete ask is easier to say yes to than "please help".</li>\n'
     '</ul>\n'
     '<p>If they do not take it well, that does not mean you were wrong to tell them. Talk to a helpline in the meantime: in the UK the National Gambling Helpline on 0808 8020 133, in the US 1-800-MY-RESET. Both are free and confidential.</p>\n')
    anchor = '<h2>What to expect from them</h2>'
    assert s.count(anchor) == 1
    s = s.replace(anchor, SEC + anchor, 1)
    s = schema(s)
    open(F, 'w', encoding='utf-8').write(s); print('ouders klaar')
