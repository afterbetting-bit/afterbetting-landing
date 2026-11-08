# 8 nov 2026: chasing-losses-gambling en how-much-have-i-lost-gambling v2 (founder: direct live). Veilig om opnieuw te draaien.
import json, re
DATE = '2026-11-08'
OC = "onclick=\"if(window.gtag)gtag('event','cta_click',{cta_location:'app_card',cta_theme:'drang',page_path:location.pathname})\""
CARD = ('<div class="app-card"><div class="app-card-screen"><span class="app-card-label">Help now, one tap away</span>'
        '<p class="app-card-quote">"You got through this 3 times before. The urge passes. It rises, peaks and fades."</p><div class="app-card-timer">15:00</div>'
        '<p class="app-card-meta">A timer, your own reason to stop, a message to someone you trust and the helpline.</p></div>'
        f'<a class="app-card-btn" href="https://app.afterbetting.com/onboarding?van=blog&t=drang" rel="noopener" {OC}>Try Help now free</a>'
        '<p class="app-card-note">Example. Afterbetting\'s basics are free, no card needed.</p></div>')
P = {
 'blog/chasing-losses-gambling.html': dict(
  edits=[
   ('Just what I went through.</p>\n', 'Just what I went through.</p>\n<div class="answer-box" id="short-answer"><h2>The short answer</h2><p>Chasing losses means gambling again to win back money you have already lost, often with bigger stakes, faster, and with money meant for something else. It almost never works: the longer you play, the more the odds catch up with you, and even when you do win it back, you rarely stop. The way out is to stop with the loss, put the money out of reach and block access. More in <a href="/blog/how-to-stop-gambling">how to stop gambling</a>.</p></div>\n'),
   ('<h2>Why your head says it can work</h2>', '<h2>Chasing losses in sports betting and poker</h2>\n<p>I bet mostly on sport. There, chasing often looks like a bigger bet on the late kick-off to cover the afternoon, an extra accumulator, or live bets on a match you do not even care about. The fixtures never stop, so there is always a next game to get it back on.</p>\n<p>In poker people call it tilt. After a bad beat you play looser, at higher stakes, more hands, to get it back that same night. Different games, same loop: a loss, a rush to undo it, a bigger loss.</p>\n<h2>Why your head says it can work</h2>'),
   ('gambled away your paycheck</a>.</p>\n', 'gambled away your paycheck</a>.</p>\n<p>Right now, with the urge to win it back, give it 15 minutes before you do anything.</p>\n' + CARD + '\n'),
   ('In the UK the National Gambling Helpline is free and open 24/7 on 0808 8020 133.</p>', 'In the UK the National Gambling Helpline is free and open 24/7 on 0808 8020 133. In the US, call or text 1-800-MY-RESET.</p>'),
  ],
  faq_after='<h3>What should I do after losing a lot of money gambling?</h3>',
  faq=[
   ('What does chasing losses mean?', 'Chasing losses means continuing to gamble, often with bigger or faster bets, to win back money you have already lost. It is one of the most common patterns in problem gambling.'),
   ('How do I stop chasing losses?', 'Stop with the loss instead of waiting to get back to even, move your money out of reach, switch on self-exclusion and blocks, and tell someone. A limit rarely works once you are chasing, because it turns into a target. See <a href="/blog/block-gambling-sites-and-payments">how to block gambling sites</a>.'),
   ('Is chasing losses a sign of a gambling problem?', 'It is one of the clearest signs. The Problem Gambling Severity Index (PGSI), a widely used screening questionnaire, asks directly whether you go back another day to win back money you lost. You can take a version of it in our <a href="/blog/gambling-addiction-test">gambling addiction test</a>.'),
  ]),
 'blog/how-much-have-i-lost-gambling.html': dict(
  edits=[
   ('Free and confidential, 24/7.</p>\n', 'Free and confidential, 24/7.</p>\n' + CARD + '\n'),
  ],
  faq_after='<h3>Does this calculator work in pounds or dollars?</h3>',
  faq=[
   ('How much money do people lose gambling?', 'A lot. In Great Britain, gambling companies kept £16.8 billion after paying out winnings between April 2024 and March 2025, according to the <a href="https://www.gamblingcommission.gov.uk/statistics-and-research/publication/industry-statistics-annual-report-financial-year-april-2024-to-march-2025" rel="noopener">Gambling Commission</a>. That is, in effect, what players lost. For one person, the calculator above gives you your own number.'),
   ('How can I stop losing money gambling?', 'Honestly: by not gambling. Systems, limits and strategies do not change the odds. What works is making it hard to deposit: self-exclusion, blocker apps, a gambling block at your bank and your money out of easy reach. Start with <a href="/blog/how-to-stop-gambling">how to stop gambling</a>.'),
  ]),
}
for f, c in P.items():
    s = open(f, encoding='utf-8').read()
    if 'class="app-card"' in s: print('al gedaan', f); continue
    for old, new in c['edits']:
        assert old in s, (f, old[:60]); s = s.replace(old, new, 1)
    i = s.index('</p>', s.index(c['faq_after'], s.index('<article'))) + 4
    s = s[:i] + '\n' + '\n'.join(f'<h3>{q}</h3>\n<p>{a}</p>' for q, a in c['faq']) + s[i:]
    def fix(m):
        j = json.loads(m.group(1))
        if j.get('@type') == 'FAQPage':
            j['mainEntity'] += [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': re.sub('<[^>]+>', '', a)}} for q, a in c['faq']]
            for e in j['mainEntity']:
                if e['name'] == 'What should I do after losing a lot of money gambling?' and 'MY-RESET' not in e['acceptedAnswer']['text']:
                    e['acceptedAnswer']['text'] += ' In the US, call or text 1-800-MY-RESET.'
        elif j.get('@type') == 'Article':
            j['dateModified'] = DATE
        else: return m.group(0)
        return '<script type="application/ld+json">' + json.dumps(j, ensure_ascii=False) + '</script>'
    s = re.sub(r'<script type="application/ld\+json">(.*?)</script>', fix, s, flags=re.S)
    open(f, 'w', encoding='utf-8').write(s); print('klaar', f)
