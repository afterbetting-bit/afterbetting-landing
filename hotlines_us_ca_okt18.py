# 18 okt 2026: Engelse pagina's krijgen VS- en Canada-hulplijnen. NCPG gebruikt sinds jan 2026 1-800-MY-RESET (1-800-GAMBLER is van CCGNJ).
import re, glob
FOOT = ('<div class="crisis-footer"><p>In crisis right now? UK: <strong>National Gambling Helpline 0808 8020 133</strong> (free, 24/7). '
        'US: <strong>1-800-MY-RESET (1-800-697-3738)</strong>, call or text, 24/7. '
        'Canada: your <a href="https://gamblingguidelines.ca/getting-help/" rel="noopener">provincial gambling helpline</a>. '
        'Thinking about suicide? UK: <strong>Samaritans 116 123</strong>. US and Canada: call or text <strong>988</strong>. '
        'Netherlands: <strong>OpenOverGokken 0800-2400022</strong>. Elsewhere, or in danger: your local emergency number.</p></div>')
n = {'footer': 0, 'inline': 0}
for f in ['index.html'] + sorted(glob.glob('blog/*.html')):
    s = open(f, encoding='utf-8').read(); o = s
    s, k = re.subn(r'<div class="crisis-footer"><p>In crisis right now\?[\s\S]*?</p></div>', FOOT, s); n['footer'] += k
    s = s.replace('<strong>1-800-GAMBLER</strong>', '<strong>1-800-MY-RESET (1-800-697-3738)</strong>')
    s = s.replace('1-800-GAMBLER', '1-800-MY-RESET (1-800-697-3738)')
    s = s.replace('In Canada, the ConnexOntario helpline (1-866-531-2600) operates nationally.',
                  'In Canada, each province has its own gambling helpline, for example ConnexOntario (1-866-531-2600) in Ontario.')
    if s != o:
        n['inline'] += o.count('1-800-GAMBLER')
        assert '—' not in s
        open(f, 'w', encoding='utf-8').write(s)
print(n)
