new_urls = [
    "salaris-vergokt-wat-nu",
    "partner-heeft-mijn-gokken-ontdekt",
    "hoe-lang-duurt-herstel-gokverslaving",
    "geld-terugvragen-online-casino",
    "cruks-omzeilen-wat-nu",
]
date = "2026-05-09"

with open("sitemap.xml","r") as f:
    content = f.read()

block = ""
for slug in new_urls:
    u = f"https://afterbetting.com/nl/blog/{slug}"
    block += f'\n  <url>\n    <loc>{u}</loc>\n    <lastmod>{date}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.7</priority>\n    <xhtml:link rel="alternate" hreflang="nl" href="{u}"/>\n    <xhtml:link rel="alternate" hreflang="x-default" href="{u}"/>\n  </url>'

# Check geen duplicaten
for slug in new_urls:
    if f"/nl/blog/{slug}<" in content:
        print(f"SKIP: {slug} bestaat al in sitemap")
        new_urls.remove(slug)

content = content.replace("</urlset>", block + "\n</urlset>")

with open("sitemap.xml","w") as f:
    f.write(content)

print(f"Sitemap updated. {len(new_urls)} nieuwe URLs toegevoegd.")
