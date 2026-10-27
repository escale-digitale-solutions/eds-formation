"""GitHub Pages-compatible immediate HTML redirects for retired URLs."""
import json
from html import escape

REDIRECTS = {'partenariat':'/accompagnement/', 'parcours':'/accompagnement/', 'methode':'/accompagnement/', 'accueil':'/'}

def write_redirects(dist, origin):
    for slug,target in REDIRECTS.items():
        url=origin+target
        folder=dist/slug;folder.mkdir(parents=True,exist_ok=True)
        html=f'''<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Cette page a changé d’adresse · EDS</title><meta name="robots" content="noindex,follow"><link rel="canonical" href="{escape(url,quote=True)}"><script>location.replace({json.dumps(target)}+location.search+location.hash);</script><meta http-equiv="refresh" content="0;url={escape(url,quote=True)}"></head><body><h1>Retrouvez EDS à cette adresse.</h1><p><a href="{target}">Continuer vers la page actuelle</a></p></body></html>'''
        (folder/'index.html').write_text(html)
