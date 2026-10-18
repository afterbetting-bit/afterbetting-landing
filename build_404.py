# 18 okt 2026: eigen 404-pagina (EN en NL; /nl/... krijgt de Nederlandse tekst). Bouwt op het sjabloon van een blogpagina.
import re
s = open('blog/gambling-addiction-test.html', encoding='utf-8').read()
a = s.index('<title>'); b = s.index('<script>window.addEventListener("load",function(){setTimeout(function(){var s=document.createElement("script");')
head = ('<title>Page not found | Afterbetting</title>\n<meta name="description" content="This page does not exist. Find what you were looking for on Afterbetting."/>\n'
        '<meta name="robots" content="noindex,follow"/>\n')
s = s[:a] + head + s[b:]
s = re.sub(r'<script type="application/ld\+json">[\s\S]*?</script>\n?', '', s)

def block(lang, h1, lead, links, btn, btn_url, help_):
    li = ''.join(f'<li><a href="{u}">{t}</a></li>' for t, u in links)
    return (f'<div class="nf" data-lang="{lang}"><h1>{h1}</h1><p class="nf-lead">{lead}</p><ul class="nf-links">{li}</ul>'
            f'<a class="nf-btn" href="{btn_url}">{btn}</a><p class="nf-help">{help_}</p></div>')

EN = block('en', 'This page does not exist', 'The link may be old, or the address has a typo. Here is where most people find what they need:',
           [('Gambling addiction test: 9 questions', '/blog/gambling-addiction-test'), ('Do gambling urges go away?', '/blog/do-gambling-urges-go-away'),
            ('Where to get help for gambling addiction', '/blog/where-to-get-help-gambling-addiction'), ('All articles', '/blog'), ('Home', '/')],
           'Start free', 'https://app.afterbetting.com/onboarding',
           'In crisis right now? UK: <strong>0808 8020 133</strong>. US: call or text <strong>1-800-MY-RESET</strong>. Thinking about suicide? US and Canada: <strong>988</strong>, UK: <strong>116 123</strong>.')
NL = block('nl', 'Deze pagina bestaat niet', 'De link is misschien oud, of er zit een typfout in het adres. Hier vinden de meeste mensen wat ze zoeken:',
           [('Gokverslaving test: 9 vragen', '/nl/blog/gokverslaving-test'), ('Drang om te gokken: wat je nu doet', '/nl/blog/drang-om-te-gokken'),
            ('Hulp bij gokverslaving: waar je terechtkunt', '/nl/blog/gokverslaving-hulp-zoeken'), ('Alle artikelen', '/nl/blog'), ('Home', '/nl/')],
           'Begin gratis', 'https://app.afterbetting.com/onboarding',
           'Zit je nu in crisis? Bel <strong>OpenOverGokken 0800-2400022</strong>, gratis en anoniem, 24 uur per dag. Denk je aan zelfmoord? Bel <strong>113</strong> (0800-0113).')
CSS = ('<style>.nf-wrap{max-width:640px;margin:0 auto;padding:4rem 1.5rem 5rem}.nf h1{font-size:2.2rem;margin-bottom:.75rem}'
       '.nf-lead{color:var(--mid);line-height:1.7;margin-bottom:1.25rem}.nf-links{list-style:none;margin:0 0 1.75rem;padding:0;border-top:1px solid var(--border)}'
       '.nf-links li{border-bottom:1px solid var(--border)}.nf-links a{display:block;padding:.85rem 0;color:var(--ink);text-decoration:none;font-weight:500}'
       '.nf-links a:hover{color:#22403A}.nf-btn{display:inline-block;background:var(--ink);color:#fff;text-decoration:none;font-weight:600;padding:.8rem 1.4rem;border-radius:12px}'
       '.nf-help{font-size:.88rem;color:var(--mid);margin-top:2rem;line-height:1.6}.nf[data-lang="nl"]{display:none}'
       'html.nf-nl .nf[data-lang="nl"]{display:block}html.nf-nl .nf[data-lang="en"]{display:none}</style>')
JS = '<script>if(/^\\/nl(\\/|$)/.test(location.pathname)){document.documentElement.classList.add("nf-nl");document.documentElement.lang="nl";document.title="Pagina niet gevonden | Afterbetting";}</script>'
a = s.index('<section class="hero">'); b = s.index('<div class="crisis-footer">')
s = s[:a] + CSS + JS + f'<main class="nf-wrap">{EN}{NL}</main>\n' + s[b:]
s = re.sub(r'<div class="crisis-footer">[\s\S]*?</div>', '', s, count=1)
s = re.sub(r'<div class="ab-sticky"[\s\S]*?</div>\s*</div>\s*</div>', '', s, count=1)
assert '—' not in s and s.count('<h1>') == 2
open('404.html', 'w', encoding='utf-8').write(s)
print('404.html', len(s))
