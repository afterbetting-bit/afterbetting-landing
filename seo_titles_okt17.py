# SEO 17 okt 2026: title, description en (soms) H1 afgestemd op zoektermen met vertoningen in GSC (4 tot 17 okt).
import re, json, html
DATE = '2026-10-17'

def meta(path, title=None, desc=None, h1=None):
    s = open(path, encoding='utf-8').read()
    if title:
        assert len(title) <= 60, (path, len(title))
        old = re.search(r'<title>(.*?)</title>', s).group(1)
        s = s.replace(f'<title>{old}</title>', f'<title>{title}</title>', 1)
        s = re.sub(r'(<meta property="og:title" content=")[^"]*(")', lambda m: m.group(1) + title + m.group(2), s, count=1)
        s = re.sub(r'(<meta name="twitter:title" content=")[^"]*(")', lambda m: m.group(1) + title + m.group(2), s, count=1)
    if desc:
        assert len(desc) <= 155, (path, len(desc))
        for pat in [r'(<meta name="description" content=")[^"]*(")', r'(<meta property="og:description" content=")[^"]*(")', r'(<meta name="twitter:description" content=")[^"]*(")']:
            s = re.sub(pat, lambda m: m.group(1) + desc + m.group(2), s, count=1)
    if h1:
        s = re.sub(r'(<h1[^>]*>)[\s\S]*?(</h1>)', lambda m: m.group(1) + h1 + m.group(2), s, count=1)
        s = re.sub(r'("@type": "Article", "headline": ")[^"]*(")', lambda m: m.group(1) + h1 + m.group(2), s, count=1)
    s = re.sub(r'"dateModified": ?"[^"]+"', f'"dateModified": "{DATE}"', s, count=1)
    assert '—' not in s
    open(path, 'w', encoding='utf-8').write(s)
    print('ok', path)

meta('nl/blog/cruks-omzeilen-wat-nu.html',
     'Gokstop of Cruks omzeilen? Lees dit eerst',
     'Je gokstop of Cruks omzeilen lukt vaak. Wat het zegt dat je dit zoekt, en wat je vanavond en morgen kunt doen. Eerlijk en zonder oordeel.',
     'Cruks of je gokstop omzeilen lukt. En toch wil je stoppen.')
meta('nl/blog/cruks-opzeggen.html',
     'Cruks eerder opzeggen: kan dat? Regels en bedenktijd',
     'Kun je Cruks of je gokstop eerder opzeggen? De regels (minimaal 6 maanden, 8 dagen bedenktijd) en wat je doet als de zin om te spelen nu groot is.',
     'Cruks eerder opzeggen: kan dat? Zo werkt het, en lees dit eerst')
meta('nl/blog/stoppen-met-gokken.html',
     'Hoe stop je met gokken? Eerlijke gids van een ex-gokker',
     'Hoe stop je met gokken als wilskracht niet werkt? Wat echt helpt, waarom je vastzit en hoe je vandaag begint. Van iemand die 8 jaar gokte.',
     'Stoppen met gokken: hoe stop je echt? Een eerlijke gids')
meta('nl/blog/gokverslaving-symptomen-en-kenmerken.html',
     'Gokverslaving: symptomen, kenmerken en gedrag herkennen',
     'Wanneer ben je gokverslaafd? Symptomen, kenmerken en gedrag van een gokker eerlijk op een rij. Met checklist en wat je doet als je jezelf herkent.',
     'Gokverslaving symptomen en kenmerken: wanneer ben je gokverslaafd?')
meta('nl/blog/hoe-stop-ik-met-gokken-met-schulden.html',
     'Stoppen met gokken met schulden: gokschulden oplossen',
     'Hoe stop je met gokken als je schulden hebt, en hoe los je gokschulden op? Waarom terugwinnen niet werkt en waar je gratis hulp krijgt.')
meta('nl/blog/goksites-blokkeren.html',
     desc='Goksites blokkeren op je iPhone, Android, laptop en via je bank. Wat Rabobank, ING en ABN AMRO wel en niet kunnen, en wat echt werkt.')
meta('blog/block-gambling-sites-and-payments.html',
     desc='Block gambling on your phone, laptop and bank card. How the gambling block works at Monzo, Starling, Revolut and others, and why turning it off takes time.')
meta('blog/does-self-exclusion-work-gambling.html',
     'Does self-exclusion work for gambling? An honest answer')
meta('blog/how-long-gambling-recovery-takes.html',
     'How long does gambling recovery take? An honest timeline',
     h1='How long does gambling recovery take? An honest timeline')
