import re, glob, sys
COND = 'if(/^(www\\.)?afterbetting\\.com$/.test(location.hostname))'
out = {}
cfg = 0
for f in glob.glob('**/*.html', recursive=True):
    s = open(f, encoding='utf-8').read()
    if 'location.hostname))gtag(' in s:
        continue
    n = 0
    for v in ['gtag("config","G-BC3QG79LQ0")', "gtag('config','G-BC3QG79LQ0')"]:
        n += s.count(v)
        s = s.replace(v, COND + v)
    assert n == 1, f'{f}: config {n}x'
    cfg += 1
    out[f] = s
A = re.compile(r'<a rel="noopener noreferrer" href="https://app\.afterbetting\.com/onboarding\?utm_source=landing&utm_content=(\w+)(?:&billing=(\w+))?"')
def a_sub(m):
    q = '?billing=' + m.group(2) if m.group(2) else ''
    return ('<a rel="noopener noreferrer" onclick="gtag(\'event\',\'cta_click\',{cta_location:\'%s\',page_path:location.pathname})" href="https://app.afterbetting.com/onboarding%s"' % (m.group(1), q))
J = re.compile(r'"https://app\.afterbetting\.com/onboarding\?utm_source=landing&utm_content=\w+&billing=(\w+)"')
for f, na, nj in [('index.html', 9, 4), ('nl/index.html', 1, 0)]:
    s = out.get(f) or open(f, encoding='utf-8').read()
    for line in s.splitlines():
        if 'utm_source=landing' in line and 'onclick' in line:
            sys.exit(f'{f}: onclick bestaat al op een UTM-regel, gestopt')
    s, ca = A.subn(a_sub, s)
    s, cj = J.subn(r'"https://app.afterbetting.com/onboarding?billing=\1"', s)
    assert ca == na, f'{f}: links {ca}, verwacht {na}'
    assert cj == nj, f'{f}: js {cj}, verwacht {nj}'
    assert 'utm_source=landing' not in s, f'{f}: nog UTM over'
    out[f] = s
for f, s in out.items():
    open(f, 'w', encoding='utf-8').write(s)
print('config aangepast in', cfg, 'bestanden, totaal geschreven:', len(out))
