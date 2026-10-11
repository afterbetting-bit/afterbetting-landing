# Tekstcorrecties homepages, 11 okt 2026: minder marketingtaal, geen claims die niet kloppen.
def rep(path, old, new):
    # Vervangt overal (ook in de FAQ-schema's). Al gedaan? Dan niets.
    s = open(path, encoding='utf-8').read()
    if old not in s:
        assert new in s, (path, old[:60], 'niet gevonden')
        return
    open(path, 'w', encoding='utf-8').write(s.replace(old, new))

EN = 'index.html'
rep(EN, '>Gambling Recovery App. Free to Start<', '>Free to start<')
rep(EN, 'The free plan is a genuine gambling recovery tool, not a watered-down teaser.', 'The free plan stays free. Upgrade only if you want more.')
rep(EN, 'in one warm, private platform.', 'in one private app.')
rep(EN, 'Absolutely. Afterbetting works well alongside therapy, Gamblers Anonymous, or any other support. Many users combine it with professional help as their daily accountability tool.',
         'Yes. Afterbetting works next to therapy, Gamblers Anonymous or any other support. Use it for the hours in between: the evenings, the weekends, the moments you are on your own.')
rep(EN, '100+ guided journal prompts rooted in psychology. Personalised to your age, gender, and recovery stage.', 'Guided questions for the evening, matched to where you are in recovery. A few lines is enough.')
rep(EN, '"Daily journal with 100+ guided prompts"', '"Daily journal with guided questions"')
rep(EN, 'something that helps thousands of others', 'something that helps others')
rep(EN, 'A warm, structured recovery platform for people ready to leave gambling behind.', 'An app for life after gambling.')

NL = 'nl/index.html'
rep(NL, 'journaal met meer dan 100 prompts', 'dagboek met 80 schrijfvragen')
rep(NL, '"Journaal met 100+ prompts"', '"Dagboek met 80 schrijfvragen"')
rep(NL, '>Journaal met 100+ prompts<', '>Dagboek met 80 schrijfvragen<')
rep(NL, 'Volledige journaalbibliotheek (100+ prompts)', 'Alle 80 schrijfvragen')
rep(NL, 'Ademhalingsoefeningen, grondingstechnieken en hulplijnen op één plek.', 'Ademhaling, uitstellen met timer en hulplijnen op één plek.')
rep(NL, 'Belgische hulplijnen voegen we binnenkort toe.', 'De Belgische hulplijnen staan ook in de app.')
rep(NL, '"Support Circle"', '"Steunkring"')
print('klaar')
rep(NL, 'Support Circle (nodig je eigen mensen uit)', 'Steunkring (nodig je eigen mensen uit)')
rep(NL, '>Support Circle <span', '>Steunkring <span')
