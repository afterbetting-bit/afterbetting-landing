# Bouwt de zelftest (18 okt 2026): nl/blog/gokverslaving-test + blog/gambling-addiction-test. PGSI, 9 vragen, alles in de browser.
import json, re
from blogbuild import build, hero, cards
from opknap_en import md, faq as en_faq, src as en_src
ONCLICK = 'onclick="if(window.gtag)gtag(\'event\',\'cta_click\',{cta_location:\'article_cta\',page_path:location.pathname})"'
NL_CRISIS = '<div class="crisis-footer"><p>Zit je nu in crisis? Bel <strong>OpenOverGokken: 0800-2400022</strong>. Gratis, anoniem, 24 uur per dag. Denk je aan zelfmoord? Bel <strong>113</strong> (0800-0113).</p></div>'
EN_CRISIS = ('<div class="crisis-footer"><p>In crisis right now? UK: <strong>National Gambling Helpline 0808 8020 133</strong> (free, 24/7). '
        'US: <strong>1-800-MY-RESET (1-800-697-3738)</strong>, call or text, 24/7. '
        'Canada: your <a href="https://gamblingguidelines.ca/getting-help/" rel="noopener">provincial gambling helpline</a>. '
        'Thinking about suicide? UK: <strong>Samaritans 116 123</strong>. US and Canada: call or text <strong>988</strong>. '
        'Netherlands: <strong>OpenOverGokken 0800-2400022</strong>. Elsewhere, or in danger: your local emergency number.</p></div>')

def nl_faq(items):
    html = '<h2>Veelgestelde vragen</h2>\n' + ''.join(f'<h3>{q}</h3>\n<p>{a}</p>\n' for q, a in items)
    ld = '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}, ensure_ascii=False) + '</script>\n'
    return html, ld


g = {}; exec(open('blog_tekst_test.py', encoding='utf-8').read(), g)
B = 'https://afterbetting.com/blog/'
NU = 'https://afterbetting.com/nl/blog/gokverslaving-test'; EU = 'https://afterbetting.com/blog/gambling-addiction-test'
HREF = (f'<link rel="alternate" hreflang="nl" href="{NU}"/>\n<link rel="alternate" hreflang="en" href="{EU}"/>\n'
        f'<link rel="alternate" hreflang="x-default" href="{EU}"/>')

Q = {
 'nl': ['Heb je meer ingezet dan je je eigenlijk kon veroorloven te verliezen?',
        'Moest je met steeds grotere bedragen gokken om dezelfde spanning te voelen?',
        'Ging je na het gokken een andere dag terug om je verlies terug te winnen?',
        'Heb je geld geleend of iets verkocht om te kunnen gokken?',
        'Had je het gevoel dat je misschien een probleem met gokken hebt?',
        'Heeft gokken je gezondheidsklachten gegeven, zoals stress of angst?',
        'Hebben mensen kritiek gehad op je gokken of gezegd dat je een gokprobleem hebt, ook als je dat zelf niet vond?',
        'Heeft je gokken geldproblemen veroorzaakt voor jou of je huishouden?',
        'Voelde je je schuldig over hoe je gokt of over wat er gebeurt als je gokt?'],
 'en': ['Have you bet more than you could really afford to lose?',
        'Have you needed to gamble with larger amounts of money to get the same feeling of excitement?',
        'When you gambled, did you go back another day to try to win back the money you lost?',
        'Have you borrowed money or sold anything to get money to gamble?',
        'Have you felt that you might have a problem with gambling?',
        'Has gambling caused you any health problems, including stress or anxiety?',
        'Have people criticised your betting or told you that you had a gambling problem, whether or not you thought it was true?',
        'Has your gambling caused any financial problems for you or your household?',
        'Have you felt guilty about the way you gamble or what happens when you gamble?'],
}
UI = {
 'nl': dict(intro='Denk aan de afgelopen 12 maanden.', opts=['Nooit', 'Soms', 'Meestal', 'Bijna altijd'], go='Bekijk mijn uitslag',
            note='Je antwoorden blijven op je apparaat. We slaan niets op.', missing='Beantwoord alle 9 vragen om je uitslag te zien.',
            score='Je score: {s} van 27', again='Opnieuw doen', cta='Begin gratis met Afterbetting',
            help='Wil je praten? Bel OpenOverGokken op <strong>0800-2400022</strong>, gratis en anoniem, 24 uur per dag.',
            disc='Dit is geen diagnose. Twijfel je, praat er dan over met een hulpverlener of je huisarts.',
            bands=[('Geen problemen met gokken', 'Je gokken heeft je de afgelopen 12 maanden niets gekost. Blijf letten op de signalen, want gokproblemen beginnen bijna altijd klein.'),
                   ('Laag risico', 'Er zijn een paar signalen, nog weinig gevolgen. Dit is het moment waarop stoppen of minderen het makkelijkst is. Kijk welke vraag je punten gaf.'),
                   ('Gemiddeld risico', 'Gokken heeft al gevolgen voor je geld, je gevoel of de mensen om je heen. Wacht hier niet mee. Praten met iemand helpt nu, en het kan anoniem.'),
                   ('Probleemgokken', 'Je gokken veroorzaakt duidelijke problemen. Dat zegt niets over wie je bent. Het zegt wel dat het tijd is om hulp te zoeken. Je hoeft het niet alleen te doen.')]),
 'en': dict(intro='Think about the last 12 months.', opts=['Never', 'Sometimes', 'Most of the time', 'Almost always'], go='See my result',
            note='Your answers stay on your device. We store nothing.', missing='Answer all 9 questions to see your result.',
            score='Your score: {s} out of 27', again='Take it again', cta='Start free with Afterbetting',
            help='Want to talk? UK: <strong>0808 8020 133</strong>. US: call or text <strong>1-800-MY-RESET</strong>. Free and confidential, 24/7.',
            disc='This is not a diagnosis. If you are unsure, talk to a professional or your doctor.',
            bands=[('No problems with gambling', 'Gambling has not cost you anything in the last 12 months. Keep an eye on the signs, because gambling problems almost always start small.'),
                   ('Low risk', 'There are a few signs, but few consequences so far. This is when cutting back or stopping is easiest. Look at which question gave you points.'),
                   ('Moderate risk', 'Gambling is already affecting your money, your mood or the people around you. Do not wait this out. Talking to someone helps now, and it can be anonymous.'),
                   ('Problem gambling', 'Your gambling is causing clear problems. That says nothing about who you are. It does say it is time to get help. You do not have to do it alone.')]),
}

def widget(lang):
    u = UI[lang]
    qs = ''.join(
        f'<fieldset class="abt-q"><legend><span>{i + 1}/9</span>{q}</legend><div class="abt-o">'
        + ''.join(f'<label><input type="radio" name="q{i}" value="{v}"><span>{o}</span></label>' for v, o in enumerate(u['opts']))
        + '</div></fieldset>' for i, q in enumerate(Q[lang]))
    data = json.dumps({k: u[k] for k in ('missing', 'score', 'again', 'cta', 'help', 'disc', 'bands')}, ensure_ascii=False)
    js = ('(function(){var T=' + data + ';var f=document.getElementById("abt-form"),r=document.getElementById("abt-result");'
          'f.addEventListener("submit",function(e){e.preventDefault();var s=0,miss=null;for(var i=0;i<9;i++){var c=f.querySelector("input[name=q"+i+"]:checked");'
          'if(!c){if(miss===null)miss=i;}else{s+=+c.value;}}'
          'if(miss!==null){r.hidden=false;r.className="abt-result abt-miss";r.textContent=T.missing;f.querySelectorAll("fieldset")[miss].scrollIntoView({behavior:"smooth",block:"center"});return;}'
          'var b=s===0?0:s<=2?1:s<=7?2:3;r.className="abt-result abt-b"+b;r.hidden=false;'
          'r.innerHTML="<p class=\\"abt-score\\">"+T.score.replace("{s}",s)+"</p><h3>"+T.bands[b][0]+"</h3><p>"+T.bands[b][1]+"</p>"'
          '+(b>=2?"<p class=\\"abt-help\\">"+T.help+"</p>":"")+"<a class=\\"abt-cta\\" href=\\"https://app.afterbetting.com/onboarding?van=test\\">"+T.cta+"</a>"'
          '+"<p class=\\"abt-disc\\">"+T.disc+"</p><button type=\\"button\\" class=\\"abt-again\\">"+T.again+"</button>";'
          'r.querySelector(".abt-cta").addEventListener("click",function(){if(window.gtag)gtag("event","cta_click",{cta_location:"test_result",page_path:location.pathname});});'
          'r.querySelector(".abt-again").addEventListener("click",function(){f.reset();r.hidden=true;f.scrollIntoView({behavior:"smooth"});});'
          'r.scrollIntoView({behavior:"smooth",block:"start"});if(window.gtag)gtag("event","test_complete",{page_path:location.pathname});});})();')
    return (f'<div class="abt" id="test"><form id="abt-form" novalidate><p class="abt-intro">{u["intro"]}</p>{qs}'
            f'<button type="submit" class="abt-go">{u["go"]}</button><p class="abt-note">{u["note"]}</p></form>'
            f'<div id="abt-result" class="abt-result" hidden aria-live="polite"></div></div>\n<script>{js}</script>\n')

CSS = '''
/* Zelftest PGSI (18 okt 2026) */
.abt{background:#fff;border:1px solid var(--border);border-radius:18px;padding:1.5rem;margin:2rem 0}
.abt-intro{font-weight:600;color:var(--ink);margin:0 0 1rem}
.abt-q{border:0;border-top:1px solid var(--border);margin:0;padding:1rem 0}
.abt-q legend{display:flex;gap:.6rem;font-size:1rem;font-weight:600;color:var(--ink);line-height:1.45;padding:0;margin-bottom:.7rem;float:left;width:100%}
.abt-q legend span{flex:0 0 auto;font-size:.8rem;color:var(--muted);font-weight:500;padding-top:.15rem}
.abt-o{clear:both;display:grid;grid-template-columns:repeat(4,1fr);gap:.5rem}
.abt-o label{cursor:pointer}
.abt-o input{position:absolute;opacity:0;pointer-events:none}
.abt-o span{display:block;text-align:center;font-size:.86rem;padding:.6rem .4rem;border:1px solid var(--border);border-radius:10px;color:var(--mid);background:var(--cream)}
.abt-o input:checked+span{background:var(--ink);border-color:var(--ink);color:#fff;font-weight:600}
.abt-o input:focus-visible+span{outline:2px solid var(--apricot);outline-offset:2px}
.abt-go{width:100%;margin-top:1rem;background:var(--ink);color:#fff;border:0;border-radius:12px;padding:.9rem;font-size:1rem;font-weight:600;cursor:pointer}
.abt-note{font-size:.82rem;color:var(--muted);text-align:center;margin:.6rem 0 0}
.abt-result{margin-top:1.25rem;border-radius:14px;padding:1.25rem;background:var(--clay-bg);border-left:4px solid var(--apricot)}
.abt-result h3{margin:.2rem 0 .5rem}
.abt-miss{background:#FFF4E5;font-weight:600}
.abt-b0,.abt-b1{border-left-color:var(--green);background:var(--green-bg)}
.abt-score{font-size:.9rem;font-weight:600;color:var(--muted);margin:0}
.abt-help{font-size:.92rem}
.abt a.abt-cta{display:inline-block;background:var(--ink);color:#fff !important;text-decoration:none !important;font-weight:600;padding:.75rem 1.1rem;border-radius:12px;margin:.4rem 0 .6rem}
.abt-disc{font-size:.8rem;color:var(--muted);margin:.2rem 0}
.abt-again{background:none;border:0;color:var(--mid);text-decoration:underline;cursor:pointer;padding:0;font-size:.86rem}
@media(max-width:600px){.abt{padding:1.1rem}.abt-o{grid-template-columns:1fr 1fr}}
'''

NL_FAQ = [
 ('Is deze gokverslaving test betrouwbaar?', 'De vragen komen uit de PGSI, een vragenlijst die al ruim twintig jaar wereldwijd wordt gebruikt. Het is een goede eerste check. Het is geen diagnose. Twijfel je over je uitslag, praat er dan over met een hulpverlener of je huisarts.'),
 ('Wordt mijn uitslag opgeslagen?', 'Nee. De test werkt alleen in je eigen browser. Wij zien je antwoorden niet en bewaren niets.'),
 ('Ik heb een hoge score, ben ik nu gokverslaafd?', 'De test zegt dat je gokken duidelijke problemen veroorzaakt. Of er sprake is van een gokstoornis, kan alleen een hulpverlener vaststellen. Het belangrijkste is niet het woord, maar wat je nu doet.'),
 ('Ik gok alleen op sport. Telt dat ook?', 'Ja. De vragen gaan over alle vormen van gokken: sportweddenschappen, online casino, loterijen en krasloten. Ik was zelf 8 jaar sportwedder.'),
]
EN_FAQ = [
 ('Is this gambling addiction test reliable?', 'The questions come from the PGSI, a questionnaire that has been used around the world for more than twenty years. It is a good first check. It is not a diagnosis. If you are unsure about your result, talk to a professional or your doctor.'),
 ('Is my result stored?', 'No. The test runs only in your own browser. We do not see your answers and we store nothing.'),
 ('I have a high score. Does that mean I am addicted?', 'The test says your gambling is causing clear problems. Only a qualified professional can tell you whether you have a gambling disorder. What matters most is not the word, but what you do next.'),
 ('I only bet on sports. Does that count?', 'Yes. The questions cover every kind of gambling: sports betting, online casino, lotteries and scratch cards. I was a sports bettor for 8 years myself.'),
]
SRC_NL = [('Gambling Commission: Problem Gambling Severity Index, definities en scores', 'https://www.gamblingcommission.gov.uk/manual/exploring-the-relationship-between-gambling-activities-and-problem-gambling/pgsi-report-definitions')]
SRC_EN = [('Gambling Commission: Problem Gambling Severity Index, definitions and scoring', SRC_NL[0][1])]
NOTE_NL = '<p style="font-size:.85rem;color:var(--muted)">Vragenlijst: Ferris, J. en Wynne, H. (2001). The Canadian Problem Gambling Index: Final Report. Canadian Centre on Substance Abuse. Nederlandse vertaling door Afterbetting.</p>\n'
NOTE_EN = '<p style="font-size:.85rem;color:var(--muted)">Questionnaire: Ferris, J. and Wynne, H. (2001). The Canadian Problem Gambling Index: Final Report. Canadian Centre on Substance Abuse.</p>\n'

def body(text, lang):
    h = md(text)
    assert h.count('<p>[TEST]</p>') == 1
    return h.replace('<p>[TEST]</p>', widget(lang))

fh, fld = nl_faq(NL_FAQ)
nsrc = '<h2>Bronnen</h2>\n<ul>' + ''.join(f'<li><a href="{u}" rel="noopener">{t}</a></li>' for t, u in SRC_NL) + '</ul>\n' + NOTE_NL
build('nl/blog/goksites-blokkeren.html', 'nl/blog/gokverslaving-test.html', 'nl', NU,
      'Gokverslaving test: 9 vragen om eerlijk te kijken',
      'Doe de gratis gokverslaving test: 9 vragen over de afgelopen 12 maanden. Anoniem, in 2 minuten, met uitleg over je uitslag en wat je daarna kunt doen.',
      'Gokverslaving test: ben ik gokverslaafd?', 'Gokverslaving test', 'https://afterbetting.com/nl/', 'https://afterbetting.com/nl/blog',
      hero('/nl/', '/nl/blog', 'Home', 'Zelftest', 'Gokverslaving test: ben ik gokverslaafd?',
           '9 vragen over de afgelopen 12 maanden. Anoniem, in twee minuten.',
           'Door de oprichter van Afterbetting &middot; 18 oktober 2026 &middot; 2 min test, 7 min lezen'),
      body(g['NL'], 'nl') + fh + nsrc,
      f'<div class="cta-block"><h3>Na de test</h3><p>Een dagenteller, hulp bij drang en een eerlijk beeld van je geld. Gratis te beginnen.</p><a href="https://app.afterbetting.com/onboarding" {ONCLICK}>Begin gratis</a></div>',
      cards(['Meer lezen', ('/nl/blog/gokverslaving-symptomen-en-kenmerken', 'Signalen', 'Gokverslaving: symptomen en kenmerken'),
             ('/nl/blog/stoppen-met-gokken', 'Stoppen', 'Stoppen met gokken'),
             ('/nl/blog/verlies-terugwinnen-gokken', 'Stoppen', 'Verlies terugwinnen met gokken'),
             ('/nl/blog/gokverslaving-hulp-zoeken', 'Hulp', 'Hulp bij gokverslaving: waar je terechtkunt')]),
      NL_CRISIS, HREF, '2026-10-18', fld)

efh, efld = en_faq(EN_FAQ)
build('blog/block-gambling-sites-and-payments.html', 'blog/gambling-addiction-test.html', 'en', EU,
      'Gambling addiction test: 9 honest questions (PGSI)',
      'Take the free gambling addiction test: 9 questions about the last 12 months. Anonymous, two minutes, with an honest look at your score and next steps.',
      'Gambling addiction test: am I addicted to gambling?', 'Gambling addiction test', 'https://afterbetting.com', 'https://afterbetting.com/blog',
      hero('https://afterbetting.com', 'https://afterbetting.com/blog', 'Home', 'Self-test', 'Gambling addiction test: am I addicted to gambling?',
           'Nine questions about the last 12 months. Anonymous, two minutes.',
           'By the founder of Afterbetting &middot; 18 October 2026 &middot; 2 min test, 7 min read'),
      body(g['EN'], 'en') + efh + en_src(SRC_EN) + NOTE_EN,
      f'<div class="cta"><h3>After the test</h3><p>A day counter, help when an urge hits and an honest view of your money. Start free.</p><a href="https://app.afterbetting.com/onboarding" {ONCLICK}>Start free</a></div>',
      cards(['Continue reading', (B + 'gambling-addiction-symptoms-and-signs', 'Signs', 'Gambling addiction symptoms and signs'),
             (B + 'chasing-losses-gambling', 'Quitting', 'Chasing losses in gambling'),
             (B + 'first-week-without-gambling', 'Recovery', 'Your first week without gambling'),
             (B + 'where-to-get-help-gambling-addiction', 'Support', 'Where to get help for gambling addiction')]),
      EN_CRISIS, HREF, '2026-10-18', efld)

th = open('theme.css', encoding='utf-8').read()
if '.abt{' not in th:
    open('theme.css', 'a', encoding='utf-8').write(CSS)
