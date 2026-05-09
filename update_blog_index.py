new_cards = [
    ("salaris-vergokt-wat-nu", "Crisis", "Net je salaris vergokt. Wat nu.", "Concrete stappen voor de eerste 24 uur. Wat je niet doet, wat je wel doet.", "9 mei 2026", "8 min lezen"),
    ("partner-heeft-mijn-gokken-ontdekt", "Relatie", "Mijn partner heeft mijn gokken ontdekt. Wat nu.", "Wat je vannacht zegt en wat je daarna doet bepaalt of de relatie het houdt.", "9 mei 2026", "9 min lezen"),
    ("hoe-lang-duurt-herstel-gokverslaving", "Herstel", "Hoe lang duurt herstel van gokverslaving.", "De vijf fases, wat wegtrekt en wanneer, wat blijft. Geen valse beloftes.", "9 mei 2026", "11 min lezen"),
    ("geld-terugvragen-online-casino", "Financieel", "Geld terugvragen van een online casino.", "Wat juridisch kan, wat niet, en hoe je het concreet aanpakt.", "9 mei 2026", "9 min lezen"),
    ("cruks-omzeilen-wat-nu", "Crisis", "Cruks omzeilen lukt me. En toch wil ik stoppen.", "Een hek is niet genoeg. Hoe je het hele systeem opbouwt dat wel werkt.", "9 mei 2026", "9 min lezen"),
]

with open("nl/blog/index.html","r") as f:
    content = f.read()

cards_html = ""
for slug, cat, h2, p, date, mins in new_cards:
    if f'/nl/blog/{slug}"' in content:
        print(f"SKIP: {slug} bestaat al in index")
        continue
    cards_html += f'<a href="/nl/blog/{slug}" class="blog-card">\n<div class="cat">{cat}</div>\n<h2>{h2}</h2>\n<p>{p}</p>\n<div class="meta">{date} &middot; {mins}</div>\n</a>'

# Plaats nieuwe cards direct na <div class="blog-grid">
marker = '<div class="blog-grid">'
content = content.replace(marker, marker + cards_html, 1)

with open("nl/blog/index.html","w") as f:
    f.write(content)

print(f"Blog index updated met {len(new_cards)} cards bovenaan.")
