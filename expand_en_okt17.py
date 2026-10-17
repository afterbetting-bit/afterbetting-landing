# 17 okt 2026: vier dunne EN-pagina's (positie 17 tot 32 in GSC) aangevuld, claims zonder bron verzacht.
exec(open('opknap_r4.py', encoding='utf-8').read().split("P = lambda")[0])
from opknap_en import md
P = lambda t: f'<p>{t}</p>'

def add(path, markdown):
    s = open(path, encoding='utf-8').read()
    a = s.index('<article class="body">'); c = s.index('<div class="cta">', a)
    s = s[:c] + md(markdown) + s[c:]
    assert '—' not in s
    open(path, 'w', encoding='utf-8').write(s)
    print('added', path)

B = 'https://afterbetting.com/blog/'

add('blog/does-self-exclusion-work-gambling.html', f'''
## How long self-exclusion lasts, and what happens when it ends

In the UK, GamStop lets you choose six months, one year or five years. In the Netherlands, Cruks has a minimum of six months. The rules on ending it early are strict on purpose, because the moment you want out is usually the moment you most need it.

If you are thinking about cancelling, read [can you cancel GamStop early](https://afterbetting.com/blog/cancel-gamstop-early) first. It explains the rules honestly, and what to do if the urge is strong right now.

## What to do on the day you self-exclude

Self-exclusion works best when you do it as part of a short list on the same day, not as a single action.

- **Sign up for GamStop or Cruks.** It takes a few minutes.
- **Install blocking software on every device.** Phone, laptop, tablet. Exclusion covers licensed sites. Blocking covers much more.
- **Switch on your bank's gambling block.** Many UK banks have one. How it works per bank is in [how to block gambling sites, apps and bank payments]({B}block-gambling-sites-and-payments).
- **Unsubscribe from every gambling email and delete the apps.** Every notification is an invitation.
- **Tell one person.** Not to be watched, but so you are not the only one who knows.
- **Plan your first evening.** The first evening after excluding is often harder than you expect. Decide now what you will do.

## If you have already found a way around it

Many people find a site that is not covered. If that is you, you are not the only one, and it does not mean self-exclusion was pointless. It means you need more layers, not fewer. Read [found a casino not on GamStop?]({B}casino-not-on-gamstop) for what to do tonight and tomorrow.

## What self-exclusion cannot do for you

It cannot fill the hours you used to gamble. It cannot answer the feeling that comes up on a Friday night. It cannot pay off a debt or rebuild trust.

For me, the routine was what carried the weight. Fixed things at fixed times, especially in the evenings and at weekends. The blocks bought me time. The routine is what I did with that time. More on that in [how to stop gambling urges at night and on weekends]({B}how-to-stop-gambling-urges-weekends).
''')

edit('blog/how-to-stop-gambling-urges-weekends.html', [
    ('These routines created deep neural pathways', ('These routines created deep neural pathways. ', 'These routines became habits. ')),
    ('the following approaches have genuine evidence behind them', ('the following approaches have genuine evidence behind them', 'the following approaches help many people')),
    ('Most cravings peak and pass within 15 to 20 minutes', ('Most cravings peak and pass within 15 to 20 minutes if you do not act on them.', 'For many people, an urge peaks and then fades if they do not act on it.')),
])
add('blog/how-to-stop-gambling-urges-weekends.html', f'''
## A Saturday that works

This is not a perfect day. It is a day with no empty hours where the old habit used to be.

- **Morning:** get up at your normal weekday time. Move first: a run, the gym, a long walk.
- **Late morning:** something with other people. Shopping, a coffee, a family visit.
- **Afternoon, when the matches start:** be somewhere else. Out of the house, away from the sofa where you used to bet.
- **Early evening:** cook something that takes time.
- **Evening:** a film, a book, a call. Phone in another room.
- **Night:** a fixed bedtime. Blocks on every device, so the 2am version of you has no easy route.

It sounds boring. That is the point. For me, the boring weekends were the ones that worked.

## If you wake up at night wanting to bet

The night is often the loneliest moment. Nobody is watching, the apps are open, and you are tired.

- Keep your phone out of the bedroom.
- Get up, drink some water, sit somewhere else for ten minutes.
- Write down what you feel. You do not need to solve it.
- Remind yourself that it passes. In the first weeks after I stopped, I woke up wanting to gamble. After a few weeks it got better, and my sleep came back properly.

More on the first weeks in [gambling withdrawal symptoms]({B}gambling-withdrawal-symptoms).

## When the match is on anyway

You do not have to give up sport forever. But in the first months, watching with friends who bet, or with the app one tap away, is asking a lot of yourself. Watch with someone who knows you have stopped. Or skip the big matches for a while and watch the highlights the next day, when the result is already known. A known result has no pull.
''')

edit('blog/what-to-do-instead-of-gambling.html', [
    ('Exercise is the single most consistently effective replacement activity', ('Exercise is the single most consistently effective replacement activity in addiction recovery.', 'For many people, exercise is one of the most useful replacement activities.')),
])
add('blog/what-to-do-instead-of-gambling.html', f'''
## Hobbies to replace gambling, by what you miss

It helps to match a replacement to what gambling was giving you. A few ideas, by need:

- **If you miss the excitement:** a competitive sport, climbing, a fast cycling route, a running goal with a date on it.
- **If you miss the thinking:** chess, learning a language, a course, a project at work you can sink your teeth into.
- **If you miss the people:** a five-a-side team, a running club, volunteering, a weekly evening with the same friends.
- **If you used gambling to switch off:** cooking, walking without your phone, building or fixing something with your hands.
- **If you miss the hope of a big change:** a savings goal, paying off a debt, building something slowly.

## What I did with my evenings and weekends

I gambled mostly in the evenings and at weekends, when there was no work. So those were the hours I had to fill. What helped me was routine, exercise, thinking more positively and reading about self-development. Nothing dramatic. Fixed things at fixed times.

## When nothing feels like enough

In the first weeks, almost nothing feels as intense as gambling did. That is normal. It does not mean the replacement is wrong. It means you are comparing ordinary life to something built to be exciting.

Give it time. Do the boring thing anyway. The point is not that a walk feels like a win. The point is that you get to the end of the evening without having bet. That adds up.

If the urge is strong right now, read [do gambling urges go away](https://afterbetting.com/blog/do-gambling-urges-go-away).
''')

edit('blog/sports-betting-addiction-quit.html', [
    ('take longer to seek help and have harder recoveries than people addicted to pure chance games', ('one of the main reasons sports bettors take longer to seek help and have harder recoveries than people addicted to pure chance games', 'one of the reasons sports bettors can take a long time to see that there is a problem')),
    ('long-term profitability is essentially impossible for recreational bettors', ('long-term profitability is essentially impossible for recreational bettors', 'long-term profit is very unlikely for recreational bettors')),
])
add('blog/sports-betting-addiction-quit.html', f'''
## In-play betting and accumulators

Two products deserve a special warning.

**In-play betting** turns a single match into dozens of small bets: the next goal, the next card, the next corner. Every few minutes there is a new outcome to wait for. That constant "it could happen" is what makes it so hard to stop.

**Accumulators** stretch the wait over five or six matches. It stays tense until the last one. And when one leg fails, it feels like "nearly". Nearly is what brings you back.

If you recognise yourself in either, that is not a sign you are weak. It is a sign the product works the way it was designed.

## Signs your sports betting has become a problem

- You watch matches for the bet, not for the sport.
- You bet on leagues you would never otherwise follow.
- You chase losses with bigger stakes or more bets.
- You check scores and odds at work, at dinner, in the middle of the night.
- You lie about how much you bet or how much you lost.
- You feel empty or irritable when there is no money on a match.

More signs in [gambling addiction symptoms and signs]({B}gambling-addiction-symptoms-and-signs).

## Watching sport again

When I stopped, a match without money on it felt flat. I had been a sports bettor for eight years, and sport had become something else.

It does come back, slowly. Start with sport where you know the result: highlights the next day, a match you watch after it has finished. Then live sport with people who do not bet. The pull fades when it is no longer fed.

## What to do with the knowledge

Your knowledge of sport is real. Use it for something that does not cost you. Coach a youth team, play in a five-a-side, write about the game, talk tactics with friends without a stake. The knowledge was never the problem. Betting on it was.
''')
