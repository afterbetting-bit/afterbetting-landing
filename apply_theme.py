# Zet de nieuwe huisstijl op alle pagina's: Schibsted Grotesk en /theme.css na de eigen stijl.
# Veilig om opnieuw te draaien.
import glob, re
OLD_FONT = re.compile(r'<link href="https://fonts\.googleapis\.com/css2\?family=Fraunces[^"]*" rel="stylesheet">')
NEW_FONT = '<link href="https://fonts.googleapis.com/css2?family=Schibsted+Grotesk:wght@400;500;600;700;800&display=swap" rel="stylesheet">'
THEME = '<link rel="stylesheet" href="/theme.css">'
# Losse oude kleuren in pagina's en scripts naar de nieuwe huisstijl.
HEX = {'#FFFCFA': '#F6F8F5', '#FBF3EE': '#F6EDE2', '#F7F0EA': '#ECF0EC', '#2C2420': '#0F1A19', '#1a1612': '#22403A',
       '#C4785A': '#0F1A19', '#E8C4B2': '#F4B97A', '#B8A89E': '#5A6E67', '#E8DDD6': '#DCE3DE', '#5C4A42': '#33443F',
       '#9E8E86': '#5A6E67', '#FFF4F0': '#F6EDE2', '#4A3D36': '#33443F'}
def recolor(t):
    for a, b in HEX.items():
        t = re.sub(re.escape(a) + r'\b', b, t, flags=re.I)
    return t
for js in ['consent.js', 'nav.js']:
    s0 = open(js, encoding='utf-8').read(); s1 = recolor(s0)
    if s1 != s0: open(js, 'w', encoding='utf-8').write(s1)
n = 0
for f in sorted(glob.glob('**/*.html', recursive=True)):
    s = open(f, encoding='utf-8').read()
    t = recolor(OLD_FONT.sub(NEW_FONT, s))
    if THEME not in t:
        if t.count('</head>') == 1:
            t = t.replace('</head>', THEME + '\n</head>')
        else:  # een paar pagina's missen </head>: dan vlak voor <body
            assert t.count('<body') == 1, f
            t = t.replace('<body', THEME + '\n<body', 1)
    if t != s:
        open(f, 'w', encoding='utf-8').write(t); n += 1
print('pagina\'s bijgewerkt:', n)
