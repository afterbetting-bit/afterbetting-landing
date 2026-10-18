# 18 okt 2026: twee EN-pagina's gericht op zoektermen uit Ubersuggest (VS): weinig concurrentie, echt volume.
import re
P = {
 'blog/gambling-addiction-symptoms-and-signs.html': [
  ('Gambling Addiction Symptoms and Signs. The Honest Checklist.', 'Signs of a Gambling Addiction: Symptoms and an Honest Checklist'),
  ('Gambling Addiction Symptoms and Signs. The Honest Checklist', 'Signs of a Gambling Addiction: Symptoms and Honest Checklist'),
  ('Gambling addiction symptoms and signs. The honest checklist.', 'Signs of a gambling addiction: symptoms and an honest checklist'),
  ('The real symptoms of gambling addiction. Not the textbook list. What you feel, what you do, what you hide from yourself. Written from the inside.',
   'The signs of a gambling addiction, from the inside: what you feel, what you do, what you hide. An honest checklist and a two-minute test.'),
 ],
 'blog/my-partner-has-a-gambling-problem.html': [
  ('My Partner Has a Gambling Problem. What Do I Do.', 'My Partner Has a Gambling Problem: How to Help Them and Yourself'),
  ('My Partner Has a Gambling Problem. What Do I Do', 'Gambling Addiction: How to Help Your Partner'),
  ('My partner has a gambling problem. What do I do.', 'My partner has a gambling problem: how to help them, and yourself'),
  ('Your partner gambles and you do not know what to do. What helped, what backfired, and how to not lose yourself in their recovery.',
   'How to help someone with a gambling addiction when it is your partner: what backfires, what helps, the money side, and how not to lose yourself.'),
  ('>What does help<', '>How to help someone with a gambling addiction<'),
 ],
}
for f, reps in P.items():
    s = open(f, encoding='utf-8').read()
    for a, b in reps:
        assert a in s, (f, a[:50]); s = s.replace(a, b)
    s = re.sub(r'"dateModified": ?"[0-9-]+"', '"dateModified": "2026-10-18"', s)
    t = re.search(r'<title>([^<]*)', s).group(1); d = re.search(r'name="description" content="([^"]*)', s).group(1)
    assert len(t) <= 60 and len(d) <= 155 and '—' not in s, (f, len(t), len(d))
    open(f, 'w', encoding='utf-8').write(s); print(f, len(t), len(d))
