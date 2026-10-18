# 18 okt 2026: bestaande pagina's verbeterd met de Ubersuggest-zoektermen van vandaag (NL en VS).
import re
from opknap_en import md

def edit(path, reps=(), before=None, markdown=None):
    s = open(path, encoding='utf-8').read()
    for a, b in reps:
        assert a in s, (path, a[:60]); s = s.replace(a, b)
    if before:
        assert before in s, (path, before)
        if 'data-ub18' not in s:
            s = s.replace(before, '<div data-ub18></div>\n' + md(markdown) + before, 1)
    s = re.sub(r'"dateModified": ?"[0-9-]+"', '"dateModified": "2026-10-18"', s)
    t = re.search(r'<title>([^<]*)', s).group(1); d = re.search(r'name="description" content="([^"]*)', s).group(1)
    assert len(t) <= 60 and len(d) <= 155 and '—' not in s, (path, len(t), len(d))
    open(path, 'w', encoding='utf-8').write(s); print('ok', path, len(t), len(d))

def meta(old_t, new_t, old_d=None, new_d=None):
    r = [(old_t, new_t)]
    if old_d: r.append((old_d, new_d))
    return r

N = 'https://afterbetting.com/nl/blog/'; B = 'https://afterbetting.com/blog/'

# NL: hulp zoeken -> "gokverslaving behandeling", "kliniek gokverslaving", "hulp bij gokverslaving"
edit('nl/blog/gokverslaving-hulp-zoeken.html',
     meta('Hulp bij gokverslaving: waar je terechtkunt', 'Hulp bij gokverslaving: behandeling, hulplijn en kliniek',
          'Hulp zoeken bij gokverslaving: OpenOverGokken, huisarts, verslavingszorg, zelfhulp en schuldhulp. Wat er is, wat het kost en wat je kunt verwachten.',
          'Hulp bij gokverslaving: OpenOverGokken, huisarts, behandeling in de verslavingszorg, kliniek, zelfhulp en schuldhulp. Wat het kost en wat je verwacht.')
     + [('<h2>3. Verslavingszorg</h2>', '<h2>3. Behandeling bij de verslavingszorg</h2>')],
     before='<h2>4. Zelfhulpgroepen</h2>', markdown=f'''
### Een kliniek of opname?

De meeste behandelingen voor gokverslaving zijn ambulant. Je woont thuis en gaat naar gesprekken of een groep, soms online. Een opname in een kliniek is voor mensen bij wie dat niet genoeg is, bijvoorbeeld als er ook andere verslavingen of zware psychische klachten spelen.

Er zijn ook privéklinieken. Die worden niet altijd vergoed. Vraag het vooraf na bij je zorgverzekeraar, en vraag de kliniek of ze een contract hebben met je verzekeraar.
''')

# NL: symptomen -> "wat is een gokverslaving", "pathologisch gokken"
edit('nl/blog/gokverslaving-symptomen-en-kenmerken.html', [
 ('<p>Gokverslaving heet officieel "gokstoornis". Het staat in het diagnoseboek voor psychiaters (de DSM-5) als een verslavingsziekte. Geen karakterfout. Geen kwestie van wilskracht. Een ziekte. Zoals alcoholisme een ziekte is.</p>\n<p>Dat betekent niet dat je hulpeloos bent. Dat betekent dat het te behandelen is. Net als andere verslavingen.</p>',
  '<p>Gokverslaving heet officieel gokstoornis. Vroeger heette het pathologisch gokken. Het staat in de DSM-5, het handboek dat psychiaters gebruiken, bij de verslavingen. Het is dus geen karakterfout en ook geen kwestie van te weinig wilskracht.</p>\n<p>Dat betekent niet dat je hulpeloos bent. Het betekent dat het te behandelen is, net als andere verslavingen. Wil je weten waar je staat? Doe de <a href="' + N + 'gokverslaving-test">gokverslaving test</a>.</p>')])

# NL: stoppen -> "gokverslaving stoppen", "stop met gokken"
edit('nl/blog/stoppen-met-gokken.html', before='<h2>Wanneer moet je professionele hulp zoeken?</h2>', markdown=f'''
## Kun je zelf stoppen met gokken, zonder hulp?

Sommige mensen stoppen op eigen kracht. Maar zelf stoppen betekent niet alleen. Ook wie geen behandeling volgt, heeft iets nodig om op te leunen: blokkades, één persoon die het weet, en een vast ritme voor de uren waarin je vroeger gokte.

Bij mij was ritme de kern. Vaste dingen op vaste tijden, vooral 's avonds en in het weekend. Sport, lezen, en de gedachte dat één inzet alles zou oplossen leren loslaten.

Merk je dat het je alleen niet lukt, of komt de drang steeds terug? Dan is dat geen falen. Dan is het tijd om er iemand bij te halen. Waar je terechtkunt, staat in [hulp bij gokverslaving]({N}gokverslaving-hulp-zoeken).
''')

# NL: blokkeren -> "gokken blokkeren", "blokkade online gokken"
edit('nl/blog/goksites-blokkeren.html', meta('Goksites blokkeren: telefoon, laptop en je bank', 'Goksites en gokken blokkeren: telefoon, laptop en bank',
     'Goksites blokkeren op je iPhone, Android, laptop en via je bank. Wat Rabobank, ING en ABN AMRO wel en niet kunnen, en wat echt werkt.',
     'Gokken blokkeren op je iPhone, Android, laptop en via je bank. Wat Rabobank, ING en ABN AMRO wel en niet kunnen, en welke blokkade echt werkt.'))

# NL: cruks omzeilen -> "cruks en toch gokken"
edit('nl/blog/cruks-omzeilen-wat-nu.html', [('<h2>De buitenlandse sites en illegale platforms</h2>', '<h2>Cruks en toch gokken: buitenlandse en illegale sites</h2>')])

# EN: where to get help -> "gambling addiction hotline" (VS 8.100), "treatment for gambling addiction" (3.600)
edit('blog/where-to-get-help-gambling-addiction.html',
     meta('Where to get help for gambling addiction in the UK', 'Gambling Addiction Help: Hotlines and Treatment (UK, US)',
          'Where to get help for gambling addiction: the National Gambling Helpline, NHS clinics, your GP, support groups and free debt advice. What to expect.',
          'Gambling addiction help in the UK and US: hotlines, NHS clinics and treatment, your GP, support groups and free debt advice. What to expect.')
     + [('<li><strong>In immediate danger?</strong> Call 999.</li>',
         '<li><strong>In the US:</strong> call or text the National Problem Gambling Helpline on 1-800-MY-RESET (1-800-697-3738), free, 24/7.</li>'
         '<li><strong>In Canada:</strong> call your <a href="https://gamblingguidelines.ca/getting-help/" rel="noopener">provincial gambling helpline</a>, for example ConnexOntario on 1-866-531-2600.</li>'
         '<li><strong>Thinking about suicide in the US or Canada?</strong> Call or text 988.</li>'
         '<li><strong>In immediate danger?</strong> Call 999 in the UK, 911 in the US and Canada.</li>'),
        ('<h2>2. NHS gambling clinics</h2>', '<h2>2. Treatment for gambling addiction: NHS gambling clinics</h2>')],
     before='<h2>3. Your GP</h2>', markdown='''
### Treatment in the US

In the US, many states fund free or low-cost treatment for problem gambling. The National Problem Gambling Helpline (1-800-MY-RESET) can connect you with counselling and treatment in your state. Many therapists who treat addiction also work with gambling. Check with your health insurance what is covered.
''')

# EN: symptoms -> "how do I know if I have a gambling addiction", "how does gambling addiction start"
edit('blog/gambling-addiction-symptoms-and-signs.html', before='<h2>What if you are still not sure</h2>', markdown=f'''
## How do I know if I have a gambling addiction?

There is no single moment when gambling turns into an addiction. But a few questions say a lot. Do you gamble to win back what you lost? Do you bet more than you can afford? Do you hide how much you gamble? Have you tried to stop and found you could not?

If you answer yes to more than one, take it seriously. The [gambling addiction test]({B}gambling-addiction-test) uses nine questions from a questionnaire used around the world, and takes two minutes. Nobody sees your answers.

## How does a gambling addiction start?

Usually slowly. I started gambling at 16. It did not feel like a problem for a long time. Every step felt small enough to ignore: a slightly bigger bet, an extra evening, a loss I wanted to win back.

That is what makes it hard to see. There is rarely one big moment. There is a slow slide, and by the time you notice it, it has already shaped a lot of your life. I knew something was wrong long before I was willing to admit it.
''')
