# Bouwt blog/casino-not-on-gamstop (11 okt 2026) als EN-pair van nl/blog/cruks-omzeilen-wat-nu en zet hreflang op de NL-pagina.
import json
from blogbuild import build, hero, cards
exec(open('blog_tekst_not_on_gamstop.py', encoding='utf-8').read())
NL_URL = 'https://afterbetting.com/nl/blog/cruks-omzeilen-wat-nu'
URL = 'https://afterbetting.com/blog/casino-not-on-gamstop'
HREF = (f'<link rel="alternate" hreflang="nl" href="{NL_URL}"/>\n<link rel="alternate" hreflang="en" href="{URL}"/>\n'
        f'<link rel="alternate" hreflang="x-default" href="{URL}"/>')

faq_html = '<h2>Frequently asked questions</h2>\n' + ''.join(f'<h3>{q}</h3>\n<p>{a}</p>\n' for q, a in EN_FAQ)
faq_ld = '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
    {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in EN_FAQ]}, ensure_ascii=False) + '</script>\n'
src_html = '<h2>Sources</h2>\n<ul>' + ''.join(f'<li><a href="{u}" rel="noopener">{t}</a></li>' for t, u in EN_SOURCES) + '</ul>'

build('blog/does-self-exclusion-work-gambling.html', 'blog/casino-not-on-gamstop.html', 'en', URL,
      'Found a casino not on GamStop? Read this first',
      'Found a casino not on GamStop and already played? What that means, why one lock was not enough, and what to do tonight and tomorrow.',
      'Found a casino not on GamStop? Read this first', 'Casino not on GamStop', 'https://afterbetting.com', 'https://afterbetting.com/blog',
      hero('https://afterbetting.com', 'https://afterbetting.com/blog', 'Home', 'Crisis', 'Found a casino not on GamStop? Read this first',
           'What it means that you found a way around your own exclusion. And what to do tonight and tomorrow.',
           'By Afterbetting &middot; 11 October 2026 &middot; 8 min read'),
      EN_BODY + faq_html + src_html,
      '<div class="cta"><h3>Help with an urge, one tap away</h3><p>The recovery kit in the app is free: a 15-minute delay timer, a message to your person and the helpline.</p><a href="https://app.afterbetting.com/onboarding" onclick="if(window.gtag)gtag(\'event\',\'cta_click\',{cta_location:\'article_cta\',page_path:location.pathname})">Start free</a></div>',
      cards(['Continue reading', ('https://afterbetting.com/blog/block-gambling-sites-and-payments', 'Tools', 'How to block gambling sites, apps and bank payments'),
             ('https://afterbetting.com/blog/cancel-gamstop-early', 'Crisis', 'Can you cancel GamStop early? Read this first'),
             ('https://afterbetting.com/blog/what-to-do-after-gambling-relapse', 'Relapse', 'What to do immediately after a gambling relapse'),
             ('https://afterbetting.com/blog/how-to-tell-someone-gambling-problem', 'Support', 'How to tell someone you have a gambling problem')]),
      '<div class="crisis-footer"><p>In crisis right now? In the UK, call the <strong>National Gambling Helpline (GamCare) on 0808 8020 133</strong>, free, 24/7. In the Netherlands: <strong>OpenOverGokken 0800-2400022</strong>. Thinking about suicide? Call <strong>Samaritans on 116 123</strong>.</p></div>',
      HREF, '2026-10-11', faq_ld)

# NL-pagina: hreflang naar de nieuwe EN-pagina, x-default naar EN (zoals de rest van de site)
p = 'nl/blog/cruks-omzeilen-wat-nu.html'
s = open(p, encoding='utf-8').read()
old = (f'<link rel="alternate" hreflang="nl" href="{NL_URL}"/>\n<link rel="alternate" hreflang="x-default" href="{NL_URL}"/>')
if old in s:
    s = s.replace(old, HREF)
assert s.count('hreflang="en"') == 1 and s.count('hreflang="x-default"') == 1
open(p, 'w', encoding='utf-8').write(s)
print(p, 'hreflang bijgewerkt')
