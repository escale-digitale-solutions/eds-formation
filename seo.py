"""Metadata derived from the same visible content, with stable entity identifiers."""
import json
from html import escape
from html.parser import HTMLParser
from pages_extra import training
from course_pages import COURSES, course_path
from guide import GUIDE_DATE

MAIL = 'escale.digitale.solutions@gmail.com'
LINKEDIN = 'https://www.linkedin.com/in/escaledigitalesolutions/'


def page_url(origin, slug):
    return origin + ('/404.html' if slug=='404' else '/' + (slug+'/' if slug else ''))


class VisibleFAQ(HTMLParser):
    """Only mark up actual question/answer accordions, never program summaries."""
    def __init__(self):
        super().__init__(); self.items=[]; self.question=None; self.answer=None; self.part=None
    def handle_starttag(self, tag, attrs):
        if tag=='details': self.question=[]; self.answer=[]
        if self.question is not None and tag=='summary': self.part=self.question
        if self.question is not None and tag=='div' and 'faq-answer' in dict(attrs).get('class','').split(): self.part=self.answer
    def handle_data(self, data):
        if self.part is not None: self.part.append(data)
    def handle_endtag(self, tag):
        if tag in ('summary','div'): self.part=None
        if tag=='details' and self.question is not None:
            q=' '.join(''.join(self.question).split()).rstrip('+').strip()
            a=' '.join(''.join(self.answer).split())
            if q and a: self.items.append((q,a))
            self.question=self.answer=self.part=None


def graph(data, slug, origin):
    url=page_url(origin,slug)
    orgid=origin+'/#organization'; personid=origin+'/a-propos/#florian-rousseau'
    org={'@type':['ProfessionalService','EducationalOrganization'],'@id':orgid,
         'name':'Escale Digitale Solutions','alternateName':'EDS','legalName':'Florian Rousseau EI',
         'url':origin+'/', 'logo':{'@type':'ImageObject','url':origin+'/assets/logo-eds-light.png','width':552,'height':160},
         'description':'Formation professionnelle en intelligence artificielle et accompagnement en automatisation à Issoudun et en Centre-Val de Loire.',
         'email':MAIL,'founder':{'@id':personid},
         'identifier':{'@type':'PropertyValue','propertyID':'SIRET','value':'94940901500011'},
         'areaServed':{'@type':'AdministrativeArea','name':'Centre-Val de Loire'},
         'address':{'@type':'PostalAddress','addressLocality':'Issoudun','postalCode':'36100','addressRegion':'Centre-Val de Loire','addressCountry':'FR'},
         'contactPoint':{'@type':'ContactPoint','contactType':'Renseignements formations et accompagnement','email':MAIL,'availableLanguage':'fr','url':origin+'/a-propos/'}}
    person={'@type':'Person','@id':personid,'name':'Florian Rousseau','url':origin+'/a-propos/',
            'jobTitle':'Formateur et fondateur d’Escale Digitale Solutions','worksFor':{'@id':orgid},
            'image':origin+'/assets/florian-portrait.webp','sameAs':[LINKEDIN]}
    web={'@type':'WebSite','@id':origin+'/#website','url':origin+'/', 'name':'Escale Digitale Solutions — EDS','inLanguage':'fr-FR','publisher':{'@id':orgid}}
    ptype='AboutPage' if slug=='a-propos' else 'ContactPage' if slug=='contact' else 'CollectionPage' if slug=='formations' else 'WebPage'
    page={'@type':ptype,'@id':url+'#webpage','url':url,'name':data['title'],'description':data['description'],'inLanguage':'fr-FR','isPartOf':{'@id':web['@id']},'publisher':{'@id':orgid}}
    nodes=[org,person,web,page]
    if slug and slug not in ('audit','404'):
        crumbs=[{'@type':'ListItem','position':1,'name':'Accueil','item':origin+'/'}]
        if '/' in slug: crumbs.append({'@type':'ListItem','position':2,'name':'Formations','item':origin+'/formations/'})
        label=data.get('label') or {'formations':'Formations','accompagnement':'Accompagnement','a-propos':'À propos & contact','faq':'Questions fréquentes','contact':'Contact','mentions-legales':'Mentions légales & confidentialité'}.get(slug,data['title'])
        crumbs.append({'@type':'ListItem','position':len(crumbs)+1,'name':label,'item':url})
        nodes.append({'@type':'BreadcrumbList','@id':url+'#breadcrumb','itemListElement':crumbs})
        page['breadcrumb']={'@id':url+'#breadcrumb'}
    cid=data.get('course_id')
    if cid:
        t=next(t for t in training if t['id']==cid); m=COURSES[cid]
        course={'@type':'Course','@id':url+'#course','url':url,'name':m['name'],'description':m['answer'],'provider':{'@id':orgid},'inLanguage':'fr-FR','teaches':t['items'],'coursePrerequisites':m['prerequisites'],'audience':{'@type':'EducationalAudience','audienceType':m['audience']},'mainEntityOfPage':{'@id':page['@id']}}
        instance={'@type':'CourseInstance','courseMode':'Présentiel','instructor':{'@id':personid},'description':t['duration']+' ; dates et lieu convenus avant engagement.'}
        if cid!='responsable': instance['courseWorkload']='PT7H' if cid=='vibe-coding' else 'PT8H'
        specs=[('Individuel',990,False),('Duo — total pour 2 participants',1490,False)] if cid=='vibe-coding' else [('Tarif par personne',600,False)] if cid!='responsable' else [('À partir de',300,False)]
        offers=[]
        for label,price,tax in specs:
            desc=t['price_detail'] + (' '+t['tax_note'] if 'tax_note' in t else ' Prix hors taxes ; frais éventuels précisés avant engagement.')
            spec={'@type':'PriceSpecification','priceCurrency':'EUR','valueAddedTaxIncluded':tax}
            if cid=='vibe-coding': spec.pop('valueAddedTaxIncluded')
            spec['minPrice' if cid=='responsable' else 'price']=price
            offer={'@type':'Offer','name':label,'url':url,'description':desc,'priceCurrency':'EUR','priceSpecification':spec}
            if cid!='responsable': offer['price']=price
            offers.append(offer)
        instance['offers']=offers; course['hasCourseInstance']=instance
        nodes.append(course); page['mainEntity']={'@id':course['@id']}
    elif slug=='formations':
        catalog={'@type':'ItemList','@id':url+'#catalogue','name':'Les formations IA EDS','numberOfItems':len(COURSES),'itemListElement':[{'@type':'ListItem','position':i,'url':origin+course_path(cid),'name':c['name']} for i,(cid,c) in enumerate(COURSES.items(),1)]}
        nodes.append(catalog); page['mainEntity']={'@id':catalog['@id']}
    elif slug=='accompagnement':
        service={'@type':'Service','@id':url+'#service','name':'Accompagnement IA et automatisation pour les entreprises','serviceType':'Conseil, assistants IA et automatisations','description':data['description'],'provider':{'@id':orgid},'areaServed':org['areaServed'],'url':url}
        nodes.append(service);page['mainEntity']={'@id':service['@id']}
    elif slug=='a-propos': page['mainEntity']={'@id':personid}
    if data.get('article'):
        article={'@type':'Article','@id':url+'#article','headline':'Quelle formation IA choisir pour votre entreprise ?','description':data['description'],'author':{'@id':orgid},'publisher':{'@id':orgid},'datePublished':GUIDE_DATE,'dateModified':GUIDE_DATE,'mainEntityOfPage':{'@id':page['@id']},'inLanguage':'fr-FR','image':origin+'/assets/eds-social.png'}
        nodes.append(article);page['mainEntity']={'@id':article['@id']}
    parser=VisibleFAQ();parser.feed(data['body'])
    if parser.items and slug!='a-propos':
        questions=[{'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':a}} for q,a in parser.items]
        if slug=='faq': page.update({'@type':'FAQPage','mainEntity':questions})
        else: nodes.append({'@type':'FAQPage','@id':url+'#questions','isPartOf':{'@id':page['@id']},'mainEntity':questions})
    return {'@context':'https://schema.org','@graph':nodes}


def head(data,slug,origin):
    robots='noindex,follow' if slug in ('audit','404') else 'index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1'
    schema=json.dumps(graph(data,slug,origin),ensure_ascii=False,separators=(',',':')).replace('<','\\u003c')
    return f'''<meta name="robots" content="{robots}"><meta property="og:site_name" content="Escale Digitale Solutions — EDS"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="EDS — Formation IA et automatisation à Issoudun, Centre-Val de Loire"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{escape(data['title'],quote=True)}"><meta name="twitter:description" content="{escape(data['description'],quote=True)}"><meta name="twitter:image" content="{origin}/assets/eds-social.png"><link rel="preload" href="/assets/fonts/bricolage-grotesque-400-800-latin.woff2" as="font" type="font/woff2" crossorigin><link rel="preload" href="/assets/fonts/hanken-grotesk-400-700-latin.woff2" as="font" type="font/woff2" crossorigin><script type="application/ld+json">{schema}</script>'''
