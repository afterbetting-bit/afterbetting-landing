# 18 okt 2026: vier dunne pagina's aangevuld (audit 18 okt, punt 9). Alleen founder-ervaring die bevestigd is.
import re
from opknap_en import md

def add(path, markdown):
    s = open(path, encoding='utf-8').read()
    if 'data-okt18' in s:
        print('al gedaan', path); return
    a = s.index('<article class="body">')
    m = re.search(r'<div class="(cta|cta-block)">', s[a:])
    c = a + m.start()
    s = s[:c] + '<div data-okt18></div>\n' + md(markdown) + s[c:]
    s = re.sub(r'"dateModified": ?"[0-9-]+"', '"dateModified": "2026-10-18"', s)
    assert '—' not in s
    open(path, 'w', encoding='utf-8').write(s)
    print('aangevuld', path)

B = 'https://afterbetting.com/blog/'
N = 'https://afterbetting.com/nl/blog/'

add('blog/daily-habits-that-replace-gambling.html', f'''
## The habits that carried me

I gambled mostly in the evenings and at weekends, when there was no work to give my day a shape. So those were the hours I had to fill. What helped me was not one big change. It was a few ordinary things, done at the same time every day.

- **Routine.** Fixed things at fixed times. Getting up at the same time, eating at the same time, going to bed at the same time. It sounds dull. It was the core of my recovery.
- **Sport.** Something physical most days. It tired me out in a good way and gave the evenings a different focus.
- **Reading.** Mostly about self-development. It gave my head something to work on that was not betting.
- **Thinking more positively.** Not pretending everything was fine, but catching the thought that one bet would fix it, and letting it go.

## Start with three, not ten

The mistake is to start with a long list. You will not keep it, and then it feels like another thing you failed at.

Pick three habits. One for the body, one for the head, one for the hours you used to gamble. Write down when you do each one. Keep it that small for two weeks before you add anything.

## Put the habits where the gambling was

A habit at 7am does not help much if your urges come at 9pm on a Friday. Look at when you used to gamble and put a habit right there.

- **Weekday evenings:** a walk after dinner, a call with someone, the gym.
- **Weekend afternoons, when the matches are on:** be out of the house, with people.
- **Late at night:** phone in another room, a book, a fixed bedtime.

More on the hardest hours in [how to stop gambling urges at night and on weekends]({B}how-to-stop-gambling-urges-weekends).

## When you miss a day

You will miss days. That is not the end of the habit. Just do it again the next day. A habit is not a streak you can lose. It is something you keep coming back to.

If you are looking for more ideas for what to do with the time, read [what to do instead of gambling]({B}what-to-do-instead-of-gambling).
''')

add('blog/first-30-days-without-gambling.html', f'''
## What I noticed in my own first weeks

The first weeks after I stopped were not calm. I had expected the decision to be the hardest part. It was not.

There was an emptiness, especially in the evenings and at weekends, the hours I used to gamble. There were triggers I did not see coming. And some nights I woke up with one thought: gambling.

After a few weeks it got better. Slowly at first, then clearly. My sleep came back properly, and that changed a lot. If you are in the middle of it now, it does not stay this heavy. More on this in [gambling withdrawal symptoms]({B}gambling-withdrawal-symptoms) and [sleep after stopping gambling]({B}sleep-after-stopping-gambling).

## A simple plan for your first 30 days

- **Day 1:** block gambling sites and apps on every device, switch on your bank's gambling block, and self-exclude. How that works is in [how to block gambling sites, apps and bank payments]({B}block-gambling-sites-and-payments).
- **First week:** tell one person. Plan every evening in advance, even if the plan is small.
- **Week two:** write down honestly how much you lost and what you owe. It is heavy, but it is where control starts.
- **Weeks three and four:** add a fixed routine. The same times for getting up, eating, moving and going to bed. For me, routine was the core of everything.

## When to get extra help

If the urges feel unmanageable, if you are not sleeping at all, or if you have dark thoughts, do not wait for the 30 days to pass. Call a helpline. In the UK, the National Gambling Helpline is 0808 8020 133. In the US, call or text 1-800-MY-RESET (1-800-697-3738). If you are thinking about suicide, call Samaritans on 116 123 in the UK, or call or text 988 in the US and Canada.

Not sure where you stand? The [gambling addiction test]({B}gambling-addiction-test) takes two minutes.
''')

add('blog/how-to-tell-family-about-gambling-problem.html', f'''
## A few ways to start the conversation

The first sentence is the hardest. It helps to have it ready. You do not need a speech. You need one honest opening, and then you can let them react.

- "I need to tell you something difficult. I have a problem with gambling, and I want to stop."
- "I have been hiding something from you. It is about money and gambling, and it is worse than you think."
- "I am not asking you to fix it. I just do not want to carry this on my own anymore."

Say it, then stop talking for a moment. Give them room.

## If there is debt they do not know about

If there is debt, say it in the same conversation. A second surprise a few weeks later often hurts more than the first. Write down the real number before you talk, so you are not tempted to make it smaller.

I ended up with more than €40,000 in debt. Writing down the real amount was one of the hardest moments, and also the moment things started to change. How I paid it back is in [how I paid off my gambling debt]({B}paid-off-gambling-debt).

## Practical things to agree on afterwards

Once the first conversation is done, it helps to agree on a few concrete things. Not as punishment, but as protection while you are early in recovery.

- **Money:** who has access to which account for now, and whether someone else checks the statements with you.
- **Blocks:** which blocks you will set up, and that you will tell them if you ever want to switch one off.
- **Hard moments:** what you will do when the urge comes, and whether you can call or message them then.
- **A check-in:** a fixed moment each week to talk about how it is going.

If your partner found out before you could tell them, read [my partner found out about my gambling]({B}partner-found-out-about-my-gambling). For the money side, there is [rebuilding your finances after gambling]({B}rebuild-finances-after-gambling).
''')

add('nl/blog/sneeuwbalmethode-gokschulden.html', f'''
## Sneeuwbal of lawine?

Naast de sneeuwbalmethode bestaat de lawinemethode. Daarbij los je eerst de schuld met de hoogste rente af, in plaats van de kleinste. Op papier bespaar je zo meestal iets meer rente.

Toch kiezen veel mensen die uit het gokken komen voor de sneeuwbal. De reden is simpel: je ziet sneller een schuld verdwijnen. Dat eerste kleine succes geeft je iets wat gokken je nooit gaf: een winst die blijft. Kies wat je het langst volhoudt. De beste methode is de methode die je niet halverwege opgeeft.

## Hoe ik mijn schuld afloste

Ik had ruim 40.000 euro schuld. Ik heb er bijna twee jaar over gedaan om alles terug te betalen. Wat werkte, was niet ingewikkeld:

- **Een vast bedrag per maand om van te leven.** Alles daarboven ging naar de schuld.
- **Alles wat extra binnenkwam, ging ook naar de schuld.** Geen uitzonderingen.
- **Volhouden zonder directe beloning.** Dat was het moeilijkste. Je werkt maanden hard en je ziet nog steeds een groot bedrag staan.
- **Niets hoeven laten zien.** Niemand om je heen ziet dat je aflost. Je doet het voor jezelf.

Het hele verhaal staat in [van 40k gokschuld naar nul]({N}van-gokschuld-naar-nul).

## Als je schulden te groot zijn om zelf af te lossen

Lukt het niet om rond te komen en tegelijk af te lossen? Dan hoef je het niet alleen te doen. Je gemeente heeft schuldhulpverlening. Die is gratis en je kunt je zelf aanmelden. Op Geldfit.nl kun je anoniem een eerste test doen en vind je hulp bij jou in de buurt.

Meld bij een schuldhulpverlener eerlijk dat je schulden door gokken komen. Dat is geen schande. Het helpt ze om een plan te maken dat bij je past.

Meer over aflossen en geld na het gokken lees je in [gokschuld aflossen]({N}gokschuld-aflossen) en [hoe stop ik met gokken als ik schulden heb]({N}hoe-stop-ik-met-gokken-met-schulden).
''')
