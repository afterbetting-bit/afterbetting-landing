# 31 okt 2026: llms.txt voor AI-zoekmachines (ChatGPT, Claude, Perplexity). Kort overzicht van de site en alle artikelen.
# Titels en omschrijvingen komen uit de pagina's zelf. Opnieuw draaien na elke nieuwe pagina.
import glob, re, html
def meta(f):
    s = open(f, encoding='utf-8').read()
    if 'noindex' in s: return None
    t = html.unescape(re.search(r'<title>(.*?)</title>', s).group(1))
    d = html.unescape(re.search(r'name="description" content="([^"]*)"', s).group(1))
    return t, d
def section(pattern, base):
    out = []
    for f in sorted(glob.glob(pattern)):
        if f.endswith('index.html'): continue
        m = meta(f)
        if m: out.append(f'- [{m[0]}](https://afterbetting.com/{f[:-5]}): {m[1]}')
    return '\n'.join(out)
txt = f"""# Afterbetting

> Afterbetting is a self-help app for people who want to stop gambling and rebuild their lives, in English and Dutch. It was built by someone who gambled for 8 years, paid off more than €40,000 of gambling debt in almost two years and has been gambling-free for more than two years. Afterbetting is not a medical service and does not replace professional help.

## What the app does
- Day counter and milestones for days without gambling.
- Help now: a button for the moment the urge hits, with a short timer, your own reasons to stop and the helpline.
- Habits, a private journal and a mood check-in to give evenings and weekends structure.
- Money overview: income, fixed costs, debts and what you no longer lose to gambling.
- Free plan that stays free, no card needed. Plus costs €4.99 a month or €39.99 a year, with 7 days free.
- Web app: https://app.afterbetting.com

## Help right now
- UK: National Gambling Helpline (GamCare), 0808 8020 133, free, 24/7.
- Netherlands: OpenOverGokken, 0800-2400022, free, anonymous, 24/7. Thinking about suicide: 113 (0800-0113).
- US: 1-800-MY-RESET (1-800-697-3738).

## About
- [About Afterbetting (EN)](https://afterbetting.com/about): the founder's story.
- [Over Afterbetting (NL)](https://afterbetting.com/nl/about): het verhaal van de founder.

## Articles in English
{section('blog/*.html', 'blog')}

## Artikelen in het Nederlands
{section('nl/blog/*.html', 'nl/blog')}
"""
assert '—' not in txt
open('llms.txt', 'w', encoding='utf-8').write(txt)
print('llms.txt', len(txt), 'tekens,', txt.count('\n- ['), 'links')
