# Correcties 11 okt 2026 (YMYL):
# 1. Grote Nederlandse banken hebben geen aparte gokblokkade (eigen sites gecheckt). Wel: online betalen uit, limieten laag.
# 2. cruks.nl is een commerciële site, niet van de Kansspelautoriteit. De officiële is cruksregister.nl.
# Veilig om opnieuw te draaien.
import glob
A = '<a href="/nl/blog/goksites-blokkeren">Goksites blokkeren</a>'
FIX = {
 'nl/blog/stoppen-met-gokken.html': [
  ('Daarnaast: betaalblokkades. Je bank kan transacties naar gokwebsites blokkeren. Bel ze. ABN, ING, Rabobank, Bunq, alle grote banken hebben deze optie. Vraag erom. Activeer.',
   f'Daarnaast: je geld. Zet in je bank-app online betalen met je pas uit, of zet je limieten zo laag als je kunt missen. Een aparte gokblokkade hebben de grote Nederlandse banken niet. Revolut wel. Hoe je het per bank regelt, lees je in {A}.'),
  ('Bel je bank. Vraag om een gokblokkade op je rekening en creditcard.', 'Zet in je bank-app online betalen met je pas uit of je limieten laag.')],
 'nl/blog/cruks-omzeilen-wat-nu.html': [
  ('Bel je bank. Vraag een gokblokkade aan. ABN, ING, Rabobank, SNS, Bunq kunnen het. Verschijnt soms onder verschillende namen, vraag specifiek om "blokkade voor transacties met categorie gokken/wedden".',
   f'Een aparte gokblokkade bieden de grote Nederlandse banken niet. Wat wel kan: online betalen met je pas uitzetten, je limieten verlagen, en bij bunq een winkel blokkeren. Revolut heeft wel een echte gokblokkade. Per bank uitgelegd in {A}.'),
  ('Vraag ook om blokkade van crypto-betaalplatformen (Bitvavo, Coinbase, Binance, Kraken). Sommige banken bieden dit, andere niet. Als jouw bank het niet biedt, sluit dan je crypto-accounts.',
   'Vraag je bank ook of betalingen aan crypto-platforms (Bitvavo, Coinbase, Binance, Kraken) te beperken zijn. Kan dat niet, sluit dan je crypto-accounts.'),
  ('Bel je bank. Vraag de gokblokkade. Vraag specifiek of er ook een mogelijkheid is om transacties naar crypto-platforms te beperken. Bunq, Knab en sommige neobanken hebben hiervoor extra opties.',
   'Zet in je bank-app online betalen met je pas uit of je limieten laag. Vraag je bank of betalingen aan crypto-platforms te beperken zijn.')],
 'nl/blog/zelfuitsluiting-gokken-werkt-het.html': [
  ('Bel je bank. Vraag om gokblokkade op je rekening en eventuele creditcards. ABN, ING, Rabobank, Bunq, ASN, Triodos: ze hebben allemaal een vorm hiervan. Soms heet het Stop Gokken, soms een aparte instelling in de app.',
   'Een aparte gokblokkade hebben de grote Nederlandse banken niet. Wat wel kan: online betalen met je pas uitzetten (Rabobank), je online daglimiet en paslimiet verlagen (ABN AMRO, ING), of bij bunq een winkel blokkeren. Een echte gokblokkade vond ik alleen bij Revolut.'),
  ('Wat dit doet: het blokkeert betalingen naar gokwebsites op het niveau van de bank. Ook als je een site weet te bereiken die niet onder Cruks valt, gaat de betaling niet door.',
   f'Wat dit doet: het maakt betalen aan een goksite lastiger, ook bij sites die niet onder Cruks vallen. Waterdicht is het niet. Per bank uitgelegd in {A}.')],
 'nl/blog/eerste-week-stoppen-met-gokken.html': [('Bel je bank voor een gokblokkade.', 'Zet online betalen in je bank-app uit of je limieten laag.')],
 'nl/blog/gokken-aan-je-familie-vertellen.html': [('<li>Bel je bank voor een gokblokkade</li>', '<li>Zet online betalen in je bank-app uit of je limieten laag</li>')],
 'nl/blog/gokschuld-aflossen.html': [('Bel je bank voor een gokblokkade.', 'Zet online betalen in je bank-app uit of je limieten laag.')],
 'nl/blog/hoe-stop-ik-met-gokken-met-schulden.html': [
  ('<strong>Gokblokkade bij je bank.</strong> Bel ze. ABN, ING, Rabobank, Bunq, allemaal. Vraag of ze betalingen naar gokwebsites kunnen blokkeren. De meeste banken kunnen dit.',
   f'<strong>Je bank.</strong> Zet online betalen met je pas uit of verlaag je limieten. Een aparte gokblokkade hebben de grote Nederlandse banken niet, Revolut wel. Zie {A}.')],
 'nl/blog/mijn-partner-is-gokverslaafd-wat-doe-ik.html': [
  ('<li>Een gokblokkade op zijn rekening en creditcard. Elke Nederlandse bank kan dat regelen</li>',
   '<li>Online betalen met zijn pas uit, of lage limieten in zijn bank-app. Een aparte gokblokkade hebben de grote Nederlandse banken niet</li>')],
 'nl/blog/partner-heeft-mijn-gokken-ontdekt.html': [
  ('Ik ga maandag mijn bank bellen voor een gokblokkade.', 'Ik zet morgen online betalen in mijn bank-app uit.'),
  ('<strong>Bel maandag je bank.</strong> Gokblokkade aanvragen op rekening en creditcard. Je partner kan meeluisteren. Doe het op de luidspreker.',
   '<strong>Zet je bank-app op slot.</strong> Online betalen met je pas uit, limieten laag. Doe het samen aan tafel, je partner kijkt mee.')],
 'nl/blog/salaris-vergokt-wat-nu.html': [
  ('<strong>Bel maandagochtend je bank.</strong>', '<strong>Zet vannacht nog je bank-app op slot.</strong>'),
  ('Vraag om een gokblokkade op je rekening en creditcard. ABN, ING, Rabobank, SNS, Bunq. Allemaal kunnen ze het. Als ze zeggen van niet, vraag de manager. Het bestaat. Het werkt.',
   f'Zet online betalen met je pas uit of je limieten zo laag als het kan. Een aparte gokblokkade hebben de grote Nederlandse banken niet. Lage limieten werken bijna net zo goed. Per bank uitgelegd in {A}.')],
 'nl/blog/sportgokken-verslaving.html': [
  ('<strong>Bel je bank voor een gokblokkade.</strong>', '<strong>Zet je bank-app op slot.</strong>'),
  ('Op betalingen naar bookmakers en betalingsverwerkers.', 'Online betalen met je pas uit, of je limieten laag.')],
 'nl/blog/terugval-na-gokverslaving.html': [('Als je je gokblokkade bij de bank had opgeheven, vraag hem opnieuw aan.', 'Als je je limieten bij de bank had verhoogd, zet ze weer laag.')],
}
for path, pairs in FIX.items():
    s = open(path, encoding='utf-8').read()
    for old, new in pairs:
        if old in s: s = s.replace(old, new)
        else: assert new in s, (path, old[:50])
    open(path, 'w', encoding='utf-8').write(s)
# Officieel Cruks-adres
for path in glob.glob('nl/blog/*.html'):
    s = open(path, encoding='utf-8').read()
    t = s.replace('cruks.nl', 'cruksregister.nl')
    if t != s: open(path, 'w', encoding='utf-8').write(t)
print('klaar')
