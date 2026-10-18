# Bouwt 2 NL/EN-paren (18 okt 2026): rekenhulp "hoeveel heb ik vergokt" en "waarom liegen gokkers". Teksten in content/*.md (founder akkoord).
import json, re, html as H
from blogbuild import build, hero, cards
from opknap_en import md, inline

src = open('build_blog_test.py', encoding='utf-8').read()
exec(src[src.index('ONCLICK ='):src.index('def nl_faq')])   # ONCLICK, NL_CRISIS, EN_CRISIS
B = 'https://afterbetting.com/blog/'; N = 'https://afterbetting.com/nl/blog/'

def parse(path):
    t = open(path, encoding='utf-8').read()
    title = re.search(r'^Title \(\d+\): (.+)$', t, re.M).group(1).strip()
    desc = re.search(r'^Meta \(\d+\): (.+)$', t, re.M).group(1).strip()
    h1 = re.search(r'^# (.+)$', t, re.M).group(1).strip()
    body = t[t.index('\n', t.index('\n# ')) + 1:]
    m = re.search(r'^## (Veelgestelde vragen|Frequently asked questions)\s*$', body, re.M)
    faq_txt = body[m.end():]; body = body[:m.start()]
    faq_txt = faq_txt[:faq_txt.index('\n[')] if '\n[' in faq_txt else faq_txt
    items = re.findall(r'\*\*(.+?)\*\*\n(.+?)(?=\n\n|\Z)', faq_txt.strip(), re.S)
    return title, desc, h1, body.strip(), m.group(1), [(q.strip(), a.strip()) for q, a in items]

def faq_block(head, items):
    vis = f'<h2>{head}</h2>\n' + ''.join(f'<h3>{q}</h3>\n<p>{inline(a)}</p>\n' for q, a in items)
    plain = lambda a: re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', a)
    ld = '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": plain(a)}} for q, a in items]}, ensure_ascii=False) + '</script>\n'
    return vis, ld

# ---------- rekenhulp ----------
CALC = {
 'nl': dict(l1='Hoeveel verloor je gemiddeld per week?', l2='Hoeveel jaar gok je al?', go='Reken uit', note='Wat je invult blijft op je apparaat. We slaan niets op.',
            tot='In totaal ongeveer vergokt', pm='Dat is per maand', yr='Wat je het komende jaar houdt als je nu stopt', y5='En in vijf jaar',
            miss='Vul een bedrag per week en een aantal jaren in.', cta='Zie elke dag wat je niet meer vergokt', loc='nl-NL',
            sub='Een schatting is genoeg. Vul je verlies in, niet je inzet.'),
 'en': dict(l1='How much did you lose per week, on average?', l2='How many years have you been gambling?', go='Work it out', note='What you enter stays on your device. We store nothing.',
            tot='Roughly lost in total', pm='That is per month', yr='What you keep in the next year if you stop now', y5='And in five years',
            miss='Enter an amount per week and a number of years.', cta='See every day what you no longer lose', loc='en-GB',
            sub='An estimate is fine. Enter what you lost, not what you staked.'),
}
def calc(lang):
    u = CALC[lang]
    data = json.dumps({k: u[k] for k in ('tot', 'pm', 'yr', 'y5', 'miss', 'cta', 'loc')}, ensure_ascii=False)
    cur = "'€'" if lang == 'nl' else "(function(){try{var z=Intl.DateTimeFormat().resolvedOptions().timeZone||'';if(z==='Europe/London')return '£';if(/^(America|US)\\//.test(z))return '$';}catch(e){}return '€';})()"
    js = ('(function(){var T=' + data + ',C=' + cur + ',f=document.getElementById("abc-form"),r=document.getElementById("abc-result");'
          'document.querySelectorAll(".abc-cur").forEach(function(e){e.textContent=C;});'
          'function m(n){return C+" "+Math.round(n).toLocaleString(T.loc);}'
          'f.addEventListener("submit",function(e){e.preventDefault();var w=parseFloat((f.w.value||"").replace(",",".")),y=parseFloat((f.y.value||"").replace(",","."));'
          'r.hidden=false;if(!(w>0)||!(y>0)){r.className="abc-result abc-miss";r.textContent=T.miss;return;}'
          'var tot=w*52*y;r.className="abc-result";'
          'r.innerHTML="<p class=\\"abc-k\\">"+T.tot+"</p><p class=\\"abc-big\\">"+m(tot)+"</p><div class=\\"abc-row\\"><div><span>"+T.pm+"</span><strong>"+m(w*52/12)+"</strong></div>"'
          '+"<div><span>"+T.yr+"</span><strong>"+m(w*52)+"</strong></div><div><span>"+T.y5+"</span><strong>"+m(w*260)+"</strong></div></div>"'
          '+"<a class=\\"abc-cta\\" href=\\"https://app.afterbetting.com/onboarding\\">"+T.cta+"</a>";'
          'r.querySelector(".abc-cta").addEventListener("click",function(){if(window.gtag)gtag("event","cta_click",{cta_location:"calc_result",page_path:location.pathname});});'
          'if(window.gtag)gtag("event","calc_complete",{page_path:location.pathname});});})();')
    return (f'<div class="abc" id="rekenhulp"><form id="abc-form" novalidate><p class="abc-sub">{u["sub"]}</p>'
            f'<label class="abc-f"><span>{u["l1"]}</span><span class="abc-in"><b class="abc-cur">€</b><input name="w" inputmode="decimal" autocomplete="off" placeholder="75"></span></label>'
            f'<label class="abc-f"><span>{u["l2"]}</span><span class="abc-in"><input name="y" inputmode="decimal" autocomplete="off" placeholder="5"></span></label>'
            f'<button type="submit" class="abc-go">{u["go"]}</button><p class="abc-note">{u["note"]}</p></form>'
            f'<div id="abc-result" class="abc-result" hidden aria-live="polite"></div></div>\n<script>{js}</script>\n')

CSS = '''
/* Rekenhulp vergokt (18 okt 2026) */
.abc{background:#fff;border:1px solid var(--border);border-radius:18px;padding:1.5rem;margin:2rem 0}
.abc-sub{font-weight:600;color:var(--ink);margin:0 0 1rem}
.abc-f{display:block;margin-bottom:1rem}.abc-f>span:first-child{display:block;font-size:.95rem;font-weight:600;color:var(--ink);margin-bottom:.45rem}
.abc-in{display:flex;align-items:center;gap:.5rem;border:1px solid var(--border);border-radius:12px;background:var(--cream);padding:0 .9rem}
.abc-in b{color:var(--muted);font-weight:600}.abc-in input{flex:1;border:0;background:transparent;font-size:1.05rem;padding:.8rem 0;font-family:inherit;color:var(--ink);outline:none;min-width:0}
.abc-in:focus-within{outline:2px solid var(--apricot);outline-offset:2px}
.abc-go{width:100%;background:var(--ink);color:#fff;border:0;border-radius:12px;padding:.9rem;font-size:1rem;font-weight:600;cursor:pointer}
.abc-note{font-size:.82rem;color:var(--muted);text-align:center;margin:.6rem 0 0}
.abc-result{margin-top:1.25rem;border-radius:14px;padding:1.25rem;background:var(--clay-bg);border-left:4px solid var(--apricot)}
.abc-miss{background:#FFF4E5;font-weight:600}
.abc p.abc-k{font-size:.9rem;color:var(--muted);margin:0}.abc p.abc-big{line-height:1.1;font-size:2.2rem;font-weight:800;color:var(--ink);letter-spacing:-.03em;margin:.1rem 0 1rem}
.abc-row{display:grid;grid-template-columns:repeat(3,1fr);gap:.6rem;margin-bottom:1rem}
.abc-row div{background:#fff;border-radius:10px;padding:.7rem}.abc-row span{display:block;font-size:.78rem;color:var(--muted);line-height:1.35}.abc-row strong{display:block;font-size:1.1rem;color:var(--ink);margin-top:.2rem}
.abc a.abc-cta{display:inline-block;background:var(--ink);color:#fff !important;text-decoration:none !important;font-weight:600;padding:.75rem 1.1rem;border-radius:12px}
@media(max-width:600px){.abc{padding:1.1rem}.abc-row{grid-template-columns:1fr}}
'''

def pair(base_nl, base_en, nl_slug, en_slug, marker, widget, nl_meta, en_meta):
    nu = N + nl_slug; eu = B + en_slug
    href = (f'<link rel="alternate" hreflang="nl" href="{nu}"/>\n<link rel="alternate" hreflang="en" href="{eu}"/>\n'
            f'<link rel="alternate" hreflang="x-default" href="{eu}"/>')
    for lang, path, url, meta, tmpl, out in (('nl', base_nl, nu, nl_meta, 'nl/blog/goksites-blokkeren.html', f'nl/blog/{nl_slug}.html'),
                                             ('en', base_en, eu, en_meta, 'blog/block-gambling-sites-and-payments.html', f'blog/{en_slug}.html')):
        title, desc, h1, body, fh, items = parse(path)
        assert len(title) <= 60 and len(desc) <= 155, (path, len(title), len(desc))
        bh = md(body)
        if marker:
            mk = marker[lang]; assert bh.count(f'<p>{mk}</p>') == 1, mk
            bh = bh.replace(f'<p>{mk}</p>', widget(lang))
        fvis, fld = faq_block(fh, items)
        if lang == 'nl':
            hr = hero('/nl/', '/nl/blog', 'Home', meta['cat'], h1, meta['lead'], f"Door de oprichter van Afterbetting &middot; 18 oktober 2026 &middot; {meta['mins']}")
            cta = f'<div class="cta-block"><h3>{meta["cta"][0]}</h3><p>{meta["cta"][1]}</p><a href="https://app.afterbetting.com/onboarding" {ONCLICK}>Begin gratis</a></div>'
            build(tmpl, out, 'nl', url, title, desc, h1, meta['crumb'], 'https://afterbetting.com/nl/', 'https://afterbetting.com/nl/blog', hr, bh + fvis, cta,
                  cards(['Meer lezen'] + meta['rel']), NL_CRISIS, href, '2026-10-18', fld)
        else:
            hr = hero('https://afterbetting.com', 'https://afterbetting.com/blog', 'Home', meta['cat'], h1, meta['lead'], f"By the founder of Afterbetting &middot; 18 October 2026 &middot; {meta['mins']}")
            cta = f'<div class="cta"><h3>{meta["cta"][0]}</h3><p>{meta["cta"][1]}</p><a href="https://app.afterbetting.com/onboarding" {ONCLICK}>Start free</a></div>'
            build(tmpl, out, 'en', url, title, desc, h1, meta['crumb'], 'https://afterbetting.com', 'https://afterbetting.com/blog', hr, bh + fvis, cta,
                  cards(['Continue reading'] + meta['rel']), EN_CRISIS, href, '2026-10-18', fld)

pair('content/vergokt_nl.md', 'content/vergokt_en.md', 'hoeveel-heb-ik-vergokt', 'how-much-have-i-lost-gambling',
     {'nl': '[REKENHULP]', 'en': '[CALCULATOR]'}, calc,
     dict(cat='Geld', crumb='Hoeveel heb ik vergokt', mins='1 min rekenen, 7 min lezen', lead='Reken uit wat je hebt verloren, en wat je vanaf vandaag houdt.',
          cta=('Zie wat je niet meer vergokt', 'Een dagenteller, een overzicht van je geld en hulp als de drang komt. Gratis te beginnen.'),
          rel=[('/nl/blog/van-gokschuld-naar-nul', 'Geld', 'Van 40k gokschuld naar nul'), ('/nl/blog/verlies-terugwinnen-gokken', 'Stoppen', 'Verlies terugwinnen met gokken'),
               ('/nl/blog/gokschuld-aflossen', 'Geld', 'Gokschuld aflossen'), ('/nl/blog/gokverslaving-test', 'Zelftest', 'Gokverslaving test')]),
     dict(cat='Money', crumb='How much have I lost gambling', mins='1 min to calculate, 7 min read', lead='Work out what you have lost, and what you keep from today.',
          cta=('See what you no longer lose', 'A day counter, an overview of your money and help when an urge hits. Start free.'),
          rel=[(B + 'paid-off-gambling-debt', 'Money', 'How I paid off my gambling debt'), (B + 'chasing-losses-gambling', 'Quitting', 'Chasing losses in gambling'),
               (B + 'rebuild-finances-after-gambling', 'Money', 'Rebuilding your finances after gambling'), (B + 'gambling-addiction-test', 'Self-test', 'Gambling addiction test')]))

pair('content/liegen_nl.md', 'content/liegen_en.md', 'waarom-liegen-gokkers', 'gambling-addict-lying', None, None,
     dict(cat='Naasten', crumb='Waarom liegen gokkers', mins='8 min lezen', lead='Hoe kleine leugens groot worden, en hoe je eruit komt. Van iemand die jaren loog.',
          cta=('Vertrouwen in kleine stappen', 'Een dagenteller, hulp bij drang en een steunkring die elke week hoort hoe het gaat. Gratis te beginnen.'),
          rel=[('/nl/blog/omgaan-met-gokverslaafde-naaste', 'Naasten', 'Omgaan met een gokverslaafde naaste'), ('/nl/blog/gokken-aan-je-familie-vertellen', 'Naasten', 'Gokken aan je familie vertellen'),
               ('/nl/blog/partner-heeft-mijn-gokken-ontdekt', 'Relatie', 'Mijn partner heeft mijn gokken ontdekt'), ('/nl/blog/gokverslaving-symptomen-en-kenmerken', 'Signalen', 'Gokverslaving: symptomen en kenmerken')]),
     dict(cat='Family', crumb='Gambling addict lying', mins='8 min read', lead='How small lies grow, and how to help. From someone who lied for years.',
          cta=('Trust in small steps', 'A day counter, help when an urge hits, and a support circle that hears each week how it is going. Start free.'),
          rel=[(B + 'my-partner-has-a-gambling-problem', 'Family', 'How to help your partner'), (B + 'how-to-tell-family-about-gambling-problem', 'Family', 'How to tell your family'),
               (B + 'partner-found-out-about-my-gambling', 'Relationships', 'My partner found out about my gambling'), (B + 'gambling-addiction-symptoms-and-signs', 'Signs', 'Signs of a gambling addiction')]))

th = open('theme.css', encoding='utf-8').read()
if '.abc{' not in th:
    open('theme.css', 'a', encoding='utf-8').write(CSS)
