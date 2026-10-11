# Meldt URL's aan bij IndexNow (Bing, Yahoo, DuckDuckGo via Bing, Yandex, Seznam). Google doet niet mee.
# Gebruik: python indexnow.py all  -> alle URL's uit sitemap.xml
#          python indexnow.py FILE...  -> alleen de gewijzigde .html bestanden
import json, re, sys, time, urllib.request
KEY = 'c95651dfff2876758e97b95bb44d996f'
HOST = 'afterbetting.com'
def url_for(f):
    if not f.endswith('.html') or f.startswith(('.', 'node_modules')): return None
    p = f[:-5]
    if p.endswith('index'): p = p[:-5]
    return f'https://{HOST}/' + p.rstrip('/') if p else f'https://{HOST}/'
args = sys.argv[1:]
sitemap = set(re.findall(r'<loc>([^<]+)</loc>', open('sitemap.xml', encoding='utf-8').read()))
if args == ['all']:
    urls = sorted(sitemap)
else:
    urls = sorted({(u if u in sitemap else u + '/' if u + '/' in sitemap else u.rstrip('/')) for u in map(url_for, args) if u and {u, u + '/', u.rstrip('/')} & sitemap})
if not urls:
    print('niets te melden'); sys.exit(0)
time.sleep(int(__import__('os').environ.get('WAIT', '0')))
body = json.dumps({'host': HOST, 'key': KEY, 'keyLocation': f'https://{HOST}/{KEY}.txt', 'urlList': urls[:10000]}).encode()
req = urllib.request.Request('https://api.indexnow.org/indexnow', data=body, headers={'Content-Type': 'application/json; charset=utf-8'})
try:
    r = urllib.request.urlopen(req, timeout=30); print('IndexNow', r.status, len(urls), "URL's")
except urllib.error.HTTPError as e:
    print('IndexNow fout', e.code, e.read()[:300]); sys.exit(1)
for u in urls: print(' ', u)
