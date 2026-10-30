"""Small, source-backed moving bands. Repeated items are generated client-side."""
from html import escape
from pathlib import Path
import json
BASE=Path(__file__).parent

def read_data(file):
    path=BASE/'content'/file
    return json.loads(path.read_text()) if path.exists() else []

def client_logo(client):
    """Preserve original marks; frame JILAY's public announcement without redrawing it."""
    slug=escape(client['slug'],quote=True)
    alt=escape(client.get('alt',client['name']),quote=True)
    src='/assets/clients/'+escape(client['file'],quote=True)
    if client['slug']=='jilay':
        art=f'<svg viewBox="130 225 570 225" role="img" aria-label="{alt}" xmlns="http://www.w3.org/2000/svg"><image href="{src}" width="800" height="800"/></svg>'
    else:
        art=f'<img src="{src}" alt="{alt}" width="220" height="80" loading="lazy" decoding="async">'
    return f'<span class="client-logo-art" data-logo="{slug}">{art}</span>'

def viewport(id, label, items):
    return f'<div class="reel-window" id="{id}" tabindex="0" role="region" aria-label="{label} — défilement horizontal"><div class="reel-track"><div class="reel-group" role="list">{items}</div></div></div>'

def ai_band():
    brands=read_data('ai-brands.json')
    if not brands:return ''
    lanes=[]
    middle=(len(brands)+1)//2
    for index,(group,direction) in enumerate(((brands[:middle],'right'),(brands[middle:],'left')),1):
        cards=''.join(f'<div class="ai-plinth" data-brand="{escape(b["slug"],quote=True)}" role="listitem"><div class="ai-plinth-face"><img src="/assets/brands/{escape(b["file"],quote=True)}" alt="{escape(b["name"],quote=True)}" width="150" height="60" loading="lazy" decoding="async"></div><span class="ai-plinth-name">{escape(b["name"])}</span></div>' for b in group)
        lanes.append(f'<div class="ai-lane reel" data-reel data-speed="20" data-direction="{direction}">{viewport(f"ai-reel-{index}",f"Les outils IA — ligne {index}",cards)}</div>')
    return f'''<section class="ai-gallery" aria-labelledby="ai-heading"><div class="container reel-heading"><h2 id="ai-heading">Des outils pour votre métier.</h2><div class="reel-heading-side"><p>Une sélection selon vos besoins.</p></div></div><div class="ai-lanes">{''.join(lanes)}</div><div class="container"><p class="reel-footnote">Outils présentés selon vos besoins, sans lien de partenariat avec EDS.</p></div></section>'''

def clients_band():
    data=read_data('social-proof.json')
    clients=data.get('clients',[]) if isinstance(data,dict) else []
    if not clients:return ''
    cards=''.join(f'<div class="client-plaque" data-client="{escape(c.get("slug",""),quote=True)}" role="listitem">{client_logo(c)}<span>{escape(c["name"])}</span></div>' for c in clients)
    return f'''<section class="client-section reel" data-reel data-speed="26" aria-labelledby="clients-heading"><div class="container client-layout"><div class="client-intro"><h2 id="clients-heading">Ils ont fait appel à EDS.</h2></div>{viewport('clients-reel','Les organisations accompagnées par EDS',cards)}</div></section>'''

def testimonials_band():
    data=read_data('social-proof.json')
    reviews=data.get('testimonials',[]) if isinstance(data,dict) else []
    if not reviews:return ''
    cards=[]
    for index,r in enumerate(reviews):
        name=r['name'];company=r['company'];quote=r['quote']
        initials=''.join(w[0] for w in name.replace('.','').split()[:2])
        company_html = escape(company)
        if r.get('source_kind') == 'Avis Google' and r.get('source_url'):
            company_html = f'<a href="{escape(r["source_url"], quote=True)}" target="_blank" rel="noopener noreferrer">{escape(company)} <span aria-hidden="true">↗</span></a>'
        cards.append(f'''<figure class="review-card" role="listitem"><blockquote><p>{escape(quote)}</p></blockquote><figcaption><span class="review-avatar" aria-hidden="true">{escape(initials)}</span><span><strong>{escape(name)}</strong><span class="review-company">{company_html}</span></span></figcaption></figure>''')
    return f'''<section class="review-section reel" id="temoignages" data-reel data-speed="13" aria-labelledby="review-heading"><div class="container reel-heading"><h2 id="review-heading">Après la formation, leurs mots.</h2><div class="reel-heading-side"><p>Les retours des participants.</p></div></div>{viewport('reviews-reel','Les témoignages de participants',''.join(cards))}</section>'''
