# 31 okt 2026: titels en descriptions voor pagina's in de top 10 met vertoningen maar 0 klikken (GSC 23-29 okt).
# Past <title>, meta description, og: en twitter: aan. H1 en tekst blijven gelijk.
import re
CHANGES = {
 'blog/stop-gambling-when-winning.html': ("How to stop gambling when you're winning (and keep it)",
   "I once won €68,000 and gambled it all back. Why stopping while you're up feels impossible, and what to do with your winnings today."),
 'blog/how-much-have-i-lost-gambling.html': ("How much have I lost gambling? Free, anonymous calculator",
   "Work out what gambling has really cost you, and what you keep in the next year if you stop. Free, anonymous, runs in your browser."),
 'nl/blog/hoe-lang-duurt-herstel-gokverslaving.html': ("Hoe lang duurt herstel van gokverslaving? De tijdlijn",
   "Van de zware eerste weken tot jaar vijf: hoe lang herstel van gokverslaving duurt, wat sneller gaat en wat trager. Van iemand die 2+ jaar gestopt is."),
 'blog/first-30-days-without-gambling.html': ("First 30 days without gambling: what to expect, week by week",
   "What the first 30 days without gambling are really like. What is normal, what gets easier, and a simple plan to get through. From a former gambler."),
 'blog/gambling-addiction-test.html': ("Gambling addiction test: 9 questions, free and anonymous", None),
 'blog/partner-found-out-about-my-gambling.html': ("My partner found out about my gambling: what to say tonight", None),
}
def esc(s): return s.replace('&', '&amp;').replace('"', '&quot;')
for path, (title, desc) in CHANGES.items():
    assert len(title) <= 60, (path, len(title))
    assert desc is None or len(desc) <= 155, (path, len(desc))
    s = open(path, encoding='utf-8').read()
    n0 = s
    s, k = re.subn(r'<title>[^<]*</title>', f'<title>{title}</title>', s); assert k == 1, path
    for prop in ('og:title', 'twitter:title'):
        s = re.sub(rf'(<meta (?:property|name)="{prop}" content=")[^"]*(")', lambda m: m.group(1) + esc(title) + m.group(2), s)
    if desc:
        for attr in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
            s, k = re.subn(rf'(<meta {attr} content=")[^"]*(")', lambda m: m.group(1) + esc(desc) + m.group(2), s)
            assert k <= 1
    assert '—' not in s and s != n0
    open(path, 'w', encoding='utf-8').write(s)
    print('bijgewerkt:', path, len(title), len(desc or ''))
