# 8 nov 2026: blog/block-gambling-sites-and-payments v2 (tekst akkoord founder). Veilig om opnieuw te draaien.
import json, re
F = 'blog/block-gambling-sites-and-payments.html'
DATE = '2026-11-08'
TITLE = 'How to block gambling sites: free blockers and bank blocks'
DESC = 'Block gambling sites, apps and payments on your phone, laptop and bank card. Free blockers compared, bank blocks, and how to make the blocks stick.'
B = 'https://afterbetting.com/blog/'
s = open(F, encoding='utf-8').read()
if 'id="short-answer"' in s:
    print('al gedaan'); raise SystemExit
def rep(old, new, count=1):
    global s
    assert old in s, old[:70]; s = s.replace(old, new, count)

s = re.sub(r'<title>[^<]*</title>', f'<title>{TITLE}</title>', s)
for k in ('og:title', 'twitter:title'):
    s = re.sub(r'(<meta (?:property|name)="%s" content=")[^"]*' % k, lambda m: m.group(1) + TITLE, s)
for k in ('description', 'og:description', 'twitter:description'):
    s = re.sub(r'(<meta (?:property|name)="%s" content=")[^"]*' % k, lambda m: m.group(1) + DESC, s)

# 1. kort antwoord
rep('no single block is watertight.</p>',
    'no single block is watertight.</p>\n<div class="answer-box" id="short-answer"><h2>The short answer</h2><p>To block gambling sites, stack a few locks: self-exclusion (GamStop in Great Britain, your state\'s program in the US), a blocker app on every device (BetBlocker is free), and the gambling block in your banking app. Then let someone else hold the codes. One lock on its own is easy to get around on a bad night. Several together buy you the time for the urge to pass. Blocking is one part of stopping; the <a href="' + B + 'how-to-stop-gambling">full guide to stopping</a> covers the rest.</p></div>')

# 2. tabel blockers
old_ul = s[s.index('<p><strong>A gambling blocker app.</strong>'):s.index('<p><strong>iPhone: Screen Time.</strong>')]
TABLE = ('<p><strong>A gambling blocker app.</strong> These apps block gambling sites and apps across your devices. How the main options compare:</p>\n'
 '<div class="cmp-wrap"><table class="cmp-table"><thead><tr><th>Tool</th><th>Cost</th><th>Works on</th><th>Can you switch it off?</th></tr></thead><tbody>'
 '<tr><td><strong>BetBlocker</strong></td><td>Free, run by a UK charity</td><td>iPhone, Android, Windows, Mac and more</td><td>Blocks of two months or longer stay on until you switch them off, then a one-week cooling-off</td></tr>'
 '<tr><td><strong>Gamban</strong></td><td>Paid, 7-day free trial (free in Wales and for Michigan residents)</td><td>iPhone, Android, Windows, Mac</td><td>Designed to be hard to remove</td></tr>'
 '<tr><td><strong>iPhone Screen Time</strong></td><td>Free, built in</td><td>iPhone and iPad</td><td>Only stops you if someone else picks the passcode</td></tr>'
 '<tr><td><strong>Android</strong></td><td>No built-in gambling filter</td><td></td><td>Use a blocker app</td></tr>'
 '</tbody></table></div>\n'
 '<p>Gamban used to be free across the UK through a funded scheme. That ended in March 2026 in England and Scotland. If cost is a barrier, start with BetBlocker today.</p>\n')
s = s.replace(old_ul, TABLE, 1)

# 3. Android
rep('<p><strong>Delete the gambling apps.</strong>',
    '<p><strong>On Android.</strong> Android has no built-in setting that blocks gambling sites. So the blocker app does the work:</p>\n'
    '<ul><li>Install BetBlocker or Gamban from the Play Store and give it the permissions it asks for. Without them it cannot see gambling apps.</li>'
    '<li>Delete every betting and casino app, and remove saved cards from Chrome.</li>'
    '<li>In Settings, check that your browser is not allowed to install apps from outside the Play Store. That closes the side door that some offshore casino apps use.</li></ul>\n'
    '<p><strong>Delete the gambling apps.</strong>')

# 6. Revolut + VS
rep('Revolut:</strong> Security, Payments, Gambling block. Switching it off can take up to 48 hours.</li>',
    'Revolut:</strong> Profile, Security &amp; privacy, Gambling block. Switching it off takes up to 48 hours. Bank transfers and some payment apps are not blocked.</li>')
i = s.index('</ul>', s.index('Revolut:</strong>')) + len('</ul>')
s = s[:i] + ('\n<p><strong>In the US.</strong> There is no standard gambling switch in most US banking apps. Call your card issuer and ask whether they can block gambling transactions on your cards. Some can. '
             'Also sign up for your state\'s self-exclusion program, and for the self-exclusion inside every sportsbook app you have used. Free help: call or text 1-800-MY-RESET.</p>') + s[i:]

# 4 + 5. founder-moment en app-kaart in stap 6
rep('<h2>Step 6: hand over the key</h2>\n',
    '<h2>Step 6: hand over the key</h2>\n<p>I used Gamban. And on a bad night I found a way to get rid of it quickly. That is not a flaw in Gamban. It is what addiction does: it gets creative. That is why one block is never enough, and why the codes should not be in your own hands.</p>\n')
URL = 'https://app.afterbetting.com/onboarding?van=blog&t=drang'
OC = "onclick=\"if(window.gtag)gtag('event','cta_click',{cta_location:'app_card',cta_theme:'drang',page_path:location.pathname})\""
CARD = ('<p>Caught yourself looking up how to remove a block? That is the urge talking. Give it 15 minutes first. <a href="' + B + 'do-gambling-urges-go-away">Urges do pass</a>.</p>\n'
 '<div class="app-card"><div class="app-card-screen"><span class="app-card-label">Help now, one tap away</span>'
 '<p class="app-card-quote">"You got through this 3 times before. The urge passes. It rises, peaks and fades."</p><div class="app-card-timer">15:00</div>'
 '<p class="app-card-meta">A timer, your own reason to stop, a message to someone you trust and the helpline.</p></div>'
 f'<a class="app-card-btn" href="{URL}" rel="noopener" {OC}>Try Help now free</a><p class="app-card-note">Example. Afterbetting\'s basics are free, no card needed.</p></div>\n')
rep('So undoing them at least takes time.</p>\n', 'So undoing them at least takes time.</p>\n' + CARD)

# Afterbetting bij onderliggend probleem (verzoek founder)
rep('or the empty evenings gambling leaves behind.</p>\n',
    'or the empty evenings gambling leaves behind.</p>\n'
    '<p>A block takes away the access. It does not touch why you gambled: the urge itself, the evenings with nothing in them, the stress about money. '
    'That is the part I built <a href="https://app.afterbetting.com/onboarding?van=blog&t=drang">Afterbetting</a> for. A day counter, small habits for the hours you used to gamble, a journal, an overview of your money and debt, and Help now for when the urge hits. The basics are free.</p>\n')

# 7. FAQ
FAQ = [
 ("What is the best free gambling blocker?", "BetBlocker. It is free, run by a charity, works on most devices and has no ads. Pick a long block period so you cannot switch it off on impulse."),
 ("How do I block gambling sites on Android?", "Install a blocker app such as BetBlocker or Gamban, allow the permissions it needs, delete your gambling apps and stop your browser from installing apps outside the Play Store."),
 ("How do I block gambling apps?", "Delete them, then install a blocker app that also covers apps. On Android, BetBlocker can spot and stop gambling apps once you allow its permissions. On iPhone, let someone else set a Screen Time passcode and switch off installing apps, so a new betting app cannot come back on a bad night."),
 ("Can I block gambling on Revolut?", "Yes. Go to Profile, Security & privacy and switch on Gambling block. It works straight away. Turning it off takes up to 48 hours. It blocks card payments, not bank transfers."),
]
q = '<h3>Can I turn a block off later?</h3>'
i = s.index('</p>', s.index(q)) + 4
s = s[:i] + '\n' + '\n'.join(f'<h3>{a}</h3>\n<p>{b.replace("&", "&amp;")}</p>' for a, b in FAQ) + s[i:]
def fix(m):
    j = json.loads(m.group(1))
    if j.get('@type') == 'FAQPage':
        j['mainEntity'] += [{'@type': 'Question', 'name': a, 'acceptedAnswer': {'@type': 'Answer', 'text': b}} for a, b in FAQ]
    elif j.get('@type') == 'Article':
        j['dateModified'] = DATE; j['description'] = DESC
    else: return m.group(0)
    return '<script type="application/ld+json">' + json.dumps(j, ensure_ascii=False) + '</script>'
s = re.sub(r'<script type="application/ld\+json">(.*?)</script>', fix, s, flags=re.S)
open(F, 'w', encoding='utf-8').write(s)

CSS = ('\n/* Vergelijkingstabel in artikelen (8 nov 2026) */\n'
       '.cmp-wrap{overflow-x:auto;margin:1rem 0 1.5rem}\n.cmp-table{width:100%;border-collapse:collapse;font-size:.92rem}\n'
       '.cmp-table th,.cmp-table td{border-bottom:1px solid var(--border);padding:.6rem .5rem;text-align:left;vertical-align:top}\n'
       '.cmp-table th{font-weight:600;color:var(--ink)}\n')
th = open('theme.css', encoding='utf-8').read()
if '.cmp-table{' not in th: open('theme.css', 'a', encoding='utf-8').write(CSS)
print('block-gambling v2 klaar')
