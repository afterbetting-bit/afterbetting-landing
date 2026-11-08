# 8 nov 2026: titels en H1 op zoektermen uit Ubersuggest (domain_keywords openovergokken.nl, gamcare.org.uk, ncpgambling.org).
# gokstop 2.900/mnd (NL), gamblers anonymous 22.200/mnd (VS), gambling addiction hotline 6.600/mnd (VS). Herhaalbaar.
import re
CHANGES = {
 'nl/blog/zelfuitsluiting-gokken-werkt-het.html': ('Gokstop (Cruks): werkt zelfuitsluiting? Een eerlijk antwoord',
     'Werkt een gokstop (Cruks) echt? Een eerlijk antwoord.'),
 'blog/gambling-addiction-support-groups.html': ('Gamblers Anonymous, support groups and forums for gambling',
     'Gamblers Anonymous and other gambling support groups'),
 'blog/where-to-get-help-gambling-addiction.html': ('Gambling addiction hotline: free numbers (US, UK) and help',
     'Gambling addiction hotlines and where to get help'),
}
def esc(s): return s.replace('&', '&amp;').replace('"', '&quot;')
for path, (title, h1) in CHANGES.items():
    assert len(title) <= 60, (path, len(title))
    s = open(path, encoding='utf-8').read()
    old_h1 = re.search(r'<h1>(.*?)</h1>', s).group(1)
    s, k = re.subn(r'<title>[^<]*</title>', f'<title>{title}</title>', s); assert k == 1
    for prop in ('og:title', 'twitter:title'):
        s = re.sub(rf'(<meta (?:property|name)="{prop}" content=")[^"]*(")', lambda m: m.group(1) + esc(title) + m.group(2), s)
    s = s.replace(f'<h1>{old_h1}</h1>', f'<h1>{h1}</h1>', 1)
    s = s.replace(f'"headline": "{old_h1}"', f'"headline": "{h1}"')
    s = re.sub(r'"dateModified": ?"[^"]+"', '"dateModified": "2026-11-08"', s)
    assert '—' not in s
    open(path, 'w', encoding='utf-8').write(s)
    print(path, len(title))
