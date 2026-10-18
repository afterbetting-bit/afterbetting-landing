# 18 okt 2026: homepage EN en NL zonder het "Geen X. Geen Y."-ritme. Gewone zinnen in de stem van de founder.
# Elke vervanging moet minstens één keer voorkomen (zichtbare tekst en FAQ-schema hebben dezelfde tekst).
R = {
 'nl/index.html': [
  ('Geen wachtlijst. Geen lange intake. Geen oordeel. Alleen jij, één beslissing, en een platform dat met je meeloopt. Eén dag tegelijk. Eén stap tegelijk. Eén leven terug.',
   'Afterbetting helpt je door de dagen na je laatste gok. Je ziet hoeveel dagen je vrij bent en wat je niet meer vergokt, en je hebt hulp bij de hand als de drang komt. Je kunt vandaag beginnen, zonder wachtlijst.'),
  ('Geen creditcard. Werkt op je telefoon. Altijd opzegbaar.', 'Gratis, zonder creditcard, en het werkt op je telefoon.'),
  ('Je verbergt je telefoon. Je verbergt je rekeningen. Je verbergt jezelf.', 'Je verstopt je telefoon, je bankapp, en eigenlijk ook jezelf.'),
  ('Niet door een welzijns-startup. Niet door een algoritme. Door iemand die zelf wist hoe het was. En die nu meer dan twee jaar clean is.',
   'Ik heb 8 jaar gegokt en ben nu ruim twee jaar gestopt. Afterbetting is wat ik toen zelf miste.'),
  ('Acht jaar lang bepaalde het alles om me heen. Geld. Vertrouwen. Hoe ik mezelf zag. Ik bouwde Afterbetting omdat ik precies weet hoe het voelt om iets als dit nodig te hebben en niets te vinden dat echt helpt. Geen hulplijn. Geen forum. Iets dat elke dag opduikt en je helpt opbouwen, stil, dag na dag. Dit is de tool die ik had willen hebben.',
   'Acht jaar lang bepaalde het mijn geld, het vertrouwen van de mensen om me heen en hoe ik naar mezelf keek. Toen ik stopte, zocht ik iets voor de avonden en weekenden, de uren waarin het het zwaarst was. Een hulplijn bel je niet elke avond, en op een forum lees je vooral het verhaal van een ander. Afterbetting is wat ik toen had willen hebben.'),
  ('Drie stappen. Geen omweg.', 'Zo ziet je eerste week eruit.'),
  ("Zes korte vragen om je startpunt vast te leggen. Geen formulieren van vijftig pagina's. Klaar in vijf minuten.",
   'Een paar korte vragen: wanneer je voor het laatst gokte, wat nu het zwaarst weegt en hoeveel er per week naartoe ging. Klaar in een paar minuten.'),
  ('Streak bijhouden. Dagelijkse check-in. Schrijven als je vastloopt. Geen grote beloftes. Geen perfecte plannen. Gewoon: vandaag opnieuw kiezen voor wie je wil zijn.',
   'Elke dag een korte check-in, een paar kleine gewoontes en een plek om te schrijven als je vastloopt. Je hebt geen groot plan nodig, alleen vandaag.'),
  ('Je dashboard laat het zien. Hoeveel dagen. Hoeveel geld. Hoeveel rust. En als een dag zwaar wordt, is hulp één tik weg.',
   'Je ziet hoeveel dagen je vrij bent en hoeveel geld je niet hebt vergokt. Wordt een dag zwaar, dan is Nu hulp één tik weg.'),
  ('Begin gratis. Zet een stap verder als je er klaar voor bent. Geen lange contracten. Geen verborgen kosten.',
   'Begin gratis. Plus kun je 7 dagen proberen en daarna per maand of per jaar nemen, zonder contract en zonder verborgen kosten.'),
  ('Juist dan. Terugval hoort er voor veel mensen bij. Dat maakt je niet zwak. Dat maakt je menselijk. Afterbetting helpt je opnieuw beginnen zonder jezelf af te branden. Streak op nul. Hoofd weer omhoog. Door.',
   'Juist dan. Een terugval komt bij veel mensen voor en zegt niets over wie je bent. Je zet een nieuwe startdatum, en alles wat je eerder schreef en opbouwde blijft bewaard.'),
  ('Via je profiel. Twee klikken. Geen telefoontje, geen formulier, geen gedoe.', 'Via je profiel, in een paar klikken. Je hoeft niet te bellen of een formulier in te vullen.'),
  ('Je hoeft het niet perfect te doen. Je hoeft niet te weten hoe het verder gaat. Je hoeft alleen vandaag te beginnen.',
   'Je hoeft niet te weten hoe het verder gaat om vandaag te beginnen.'),
  ('Afterbetting. Eén dag tegelijk. Eén leven terug.', 'Afterbetting. Herstel na gokken, gebouwd door iemand die het zelf meemaakte.'),
  ('Herstel je financien', 'Herstel je financiën'), ('financiele schade', 'financiële schade'),
  ('>Financien<', '>Financiën<'), ('>Journaal<', '>Dagboek<'),
 ],
 'index.html': [
  ('No credit card. No time limit. Available worldwide.', 'Free, no credit card, and it works on your phone.'),
  ('You hide your phone. You hide your accounts. You hide yourself.', 'You hide your phone, your bank app, and in the end yourself.'),
  ('Not by a wellness startup. Not by an algorithm. By someone who spent 8 years gambling, lost more than money, and found no tool that actually helped when it mattered most.',
   'I gambled for 8 years and lost more than money. When I stopped, I could not find anything that helped in the hours that mattered. So I built it.'),
  ('I built Afterbetting at 27 because I know exactly what it feels like to need something like this and find nothing that truly helps. Not a hotline. Not a forum. Something that shows up every day and helps you rebuild, quietly, one day at a time. This is the tool I wish had existed.',
   'I built Afterbetting at 27 because I know what it is like to need help on a Friday night and find nothing. A helpline is not something you call every evening, and a forum is mostly other people’s stories. I wanted something that is there every day, for the evenings and the weekends. This is the tool I wish I had had.'),
  ('Small daily actions compound into real change over weeks.', 'A short check-in each day, a few small habits and a place to write when you get stuck.'),
  ('Your finances recover, your mindset shifts, and your streak grows. Afterbetting tracks every day you stay gambling-free and celebrates every milestone with you.',
   'You see how many days you have been gambling-free and how much money you have not lost. When a day gets heavy, Help now is one tap away.'),
  ('No credit card. No pressure. The free plan stays free. Upgrade only if you want more.', 'The free plan stays free and needs no card. Plus is there if you want more.'),
  ('A relapse is not the end of your recovery. It is part of it. ', 'A relapse happens to a lot of people and says nothing about who you are. '),
  ('Start free. No credit card. No time limit. Begin your recovery the moment you click below.', 'Starting is free and takes a few minutes. No credit card.'),
 ],
}
for f, reps in R.items():
    s = open(f, encoding='utf-8').read()
    for a, b in reps:
        n = s.count(a)
        assert n >= 1, (f, a[:60])
        s = s.replace(a, b)
    assert '—' not in s
    open(f, 'w', encoding='utf-8').write(s)
    print('ok', f, len(reps))
