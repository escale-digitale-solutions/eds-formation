"""Focused training catalogue, with optional user-supplied audio summaries."""
from pathlib import Path
from html import escape
from urllib.parse import urlsplit
import json
from pages_extra import training
from news import news_training

ROOT = Path(__file__).parent
COURSE_PATHS = {'responsable':'sensibilisation-ia','metier':'ia-metier','communication':'ia-communication','vibe-coding':'vibe-coding'}
def detail_link(cid):
    return f'<a class="tr-detail-link" href="/formations/{COURSE_PATHS[cid]}/">Voir la fiche complète de la formation <span aria-hidden="true">↗</span></a>'

PRESENTATION = {
    'responsable': {'headline': 'Sensibilisez vos équipes <br>à l’IA.', 'short': 'Une formation de sensibilisation pour découvrir les usages de l’IA, comprendre les risques et adopter les bons réflexes : données personnelles, confidentialité et vérification des réponses.', 'aim': 'Sensibiliser mon équipe', 'tone': 'sage', 'icon': '<path d="M40 12 65 22v19c0 16-25 29-25 29S15 57 15 41V22Z"/><path d="m29 40 8 8 16-18"/>'},
    'metier': {'headline': 'Moins de tâches. <br>Plus de savoir-faire.', 'short': 'Emails, comptes rendus, documents et mise en place de petites automatisations simples : pratiquez l’IA sur les tâches du quotidien de votre équipe.', 'aim': 'Je veux l’utiliser au travail', 'tone': 'amber', 'icon': '<rect x="17" y="12" width="46" height="58" rx="5"/><path d="M30 27h20M30 39h20M30 51h10"/><path d="m45 56 7 7 15-17"/>'},
    'communication': {'headline': 'Vos idées méritent <br>plus qu’un texte.', 'short': 'Images, vidéos, voix, musique : découvrez les meilleurs outils IA pour votre domaine et apprenez à les utiliser pour créer des contenus qui vous ressemblent.', 'aim': 'Créer images, vidéos & audio', 'tone': 'rose', 'icon': '<rect x="14" y="16" width="52" height="46" rx="4"/><circle cx="49" cy="29" r="6"/><path d="m15 53 17-17 22 26M47 52l8-8 11 11"/>'},
    'vibe-coding': {'headline': 'Cet outil que vous imaginez. <br><em>Apprenez à le créer.</em>', 'short': 'Un outil vous manque depuis toujours ? Apprenez à guider l’IA pour le concevoir : du besoin bien cadré aux étapes de la mise en ligne.', 'aim': 'Apprendre à créer mon outil', 'tone': 'ink', 'icon': '<rect x="10" y="15" width="60" height="49" rx="5"/><path d="M10 27h60M30 38l-8 7 8 7m20-14 8 7-8 7m-7-17-6 23"/>'},
}


def audio_summary(course_id, config=None):
    """Render only an existing local file; never expose an empty or fake player."""
    if config is None:
        config = json.loads((ROOT/'content/training-audio.json').read_text()).get('courses', {})
    item = config.get(course_id, {})
    src = item.get('src')
    if not isinstance(src, str) or not src:
        return ''
    url = urlsplit(src)
    if url.scheme or url.netloc or not url.path.startswith('/assets/audio/'):
        return ''
    file = (ROOT/'dist'/url.path.lstrip('/')).resolve()
    base = (ROOT/'dist/assets/audio').resolve()
    if base not in file.parents or not file.is_file():
        return ''
    duration = item.get('duration_seconds')
    duration_label = f' · {int(duration)} secondes' if isinstance(duration, (int, float)) and 0 < duration < 3600 else ''
    title = escape(item.get('title') or 'La formation en quelques mots')
    transcript = item.get('transcript')
    transcript_html = f'<details class="tr-transcript"><summary>Lire la transcription</summary><p>{escape(transcript)}</p></details>' if isinstance(transcript, str) and transcript.strip() else ''
    return f'''<div class="tr-audio"><p id="audio-{course_id}">{title}<span>{duration_label}</span></p><audio controls preload="none" aria-labelledby="audio-{course_id}" src="{escape(src, quote=True)}">Votre navigateur ne permet pas la lecture audio. <a href="{escape(src, quote=True)}">Télécharger le résumé audio</a>.</audio>{transcript_html}</div>'''


def program_details(t):
    items = ''.join(f'<li>{escape(i)}</li>' for i in t['items'])
    return f'''<details class="tr-program"><summary><span>Découvrir le programme et les supports</span><span class="tr-plus" aria-hidden="true">+</span></summary><div class="tr-program-content"><div><h3>Ce que vous allez pratiquer</h3><ul>{items}</ul></div><div class="tr-takeaway"><h3>Pour continuer après</h3><p>{escape(t['deliverable'])}</p><p class="tr-course-note">{escape(t['note'])}</p><a class="text-link" href="/contact/?besoin=formation&amp;programme={t['id']}">Parlons de cette formation <span aria-hidden="true">↗</span></a></div></div></details>'''


def creative_studio():
    """A light, decorative HTML composition; no simulated tool controls."""
    wave = ''.join(f'<i style="--h:{h}px"></i>' for h in [12,21,35,18,42,30,14,25,38,20,12,30,18])
    return f'''<div class="tr-studio"><div class="tr-studio-art reveal" aria-hidden="true"><div class="studio-image"><span>01 / IMAGE</span><svg viewBox="0 0 230 140" fill="none"><circle cx="160" cy="47" r="28" fill="#FFB52E"/><path d="M0 140V115L73 40l77 100Z" fill="#6A846B"/><path d="m80 140 75-82 75 82" fill="#B5C9A5"/></svg><b>Donnez forme à votre idée.</b></div><div class="studio-video"><span>02 / VIDÉO</span><svg viewBox="0 0 50 50" fill="none"><circle cx="25" cy="25" r="23" stroke="currentColor"/><path d="m21 16 14 9-14 9Z" fill="currentColor"/></svg></div><div class="studio-audio"><span>03 / AUDIO</span><div>{wave}</div></div></div><div class="tr-studio-copy"><p class="tr-small-label">Votre terrain de création</p><h3>Une idée. <br>Plusieurs façons de la raconter.</h3><p>Vous testez les outils, comparez les résultats et apprenez à choisir le bon format pour votre activité.</p><ul class="tr-format-list"><li>Images &amp; visuels</li><li>Vidéos courtes</li><li>Voix &amp; audio</li><li>Textes &amp; publications</li></ul></div></div>'''


def standard_course(t):
    v = PRESENTATION[t['id']]
    icon = f'<svg viewBox="0 0 80 80" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{v["icon"]}</svg>'
    visual = creative_studio() if t['id'] == 'communication' else ''
    label = 'IA responsable · Sensibilisation' if t['id'] == 'responsable' else t['title']
    regulation = '''<div class="tr-regulations" aria-label="Repères réglementaires abordés"><span class="tr-regulations-label">Repères abordés</span><span class="tr-regulation"><img src="/assets/regulation/europe.svg" alt="" width="36" height="24" loading="lazy"><span><strong>RGPD</strong><span>Données personnelles</span></span></span><span class="tr-regulation"><img src="/assets/regulation/europe.svg" alt="" width="36" height="24" loading="lazy"><span><strong>AI Act</strong><span>Usages de l’IA</span></span></span></div>''' if t['id'] == 'responsable' else ''
    return f'''<article class="tr-course tr-{v['tone']}" id="{t['id']}" aria-labelledby="title-{t['id']}"><div class="tr-course-top"><div class="tr-course-symbol" aria-hidden="true"><span>{t['num']} / 04</span>{icon}</div><div class="tr-course-copy"><p class="tr-course-name">{escape(label)}</p><h2 id="title-{t['id']}">{v['headline']}</h2><p class="tr-course-description">{v['short']}</p>{regulation}{detail_link(t['id'])}</div><div class="tr-course-decision"><p class="tr-format">{escape(t['duration'])}</p><p class="tr-price">{escape(t['price'])}</p><p class="tr-price-detail">{escape(t['price_detail'])}</p><a class="tr-course-contact" href="/contact/?besoin=formation&amp;programme={t['id']}">Parlons de cette formation <span aria-hidden="true">↗</span></a></div></div>{visual}{audio_summary(t['id'])}{program_details(t)}</article>'''


def vibe_course(t):
    prices = ''.join(f'''<div class="tr-vibe-price"><h4>{escape(p['label'])}</h4><p class="tr-price">{escape(p['total'])}</p><p>{escape(p['participants'])}</p>{f'<strong>{escape(p["per_person"])}</strong>' if p['per_person'] else '<span>Pour avancer à votre rythme.</span>'}</div>''' for p in t['pricing'])
    included = ''.join(f'<li>{escape(x)}</li>' for x in t['included'])
    tools = ''.join(f'<span>{escape(x)}</span>' for x in t['tools'])
    steps = [('01', 'Cadrer', 'Définir le besoin et les étapes.'), ('02', 'Construire', 'Guider l’IA, une étape à la fois.'), ('03', 'Vérifier', 'Tester, corriger et garder des versions.'), ('04', 'Publier', 'Comprendre la mise en ligne.')]
    process = ''.join(f'<li><span>{n}</span><h3>{title}</h3><p>{text}</p></li>' for n,title,text in steps)
    return f'''<article class="tr-course tr-ink" id="vibe-coding" aria-labelledby="title-vibe-coding">
      <div class="tr-vibe-intro"><div class="tr-vibe-copy"><p class="tr-course-name">04 / 04 <span>Formation Vibe coding</span></p><h2 id="title-vibe-coding">{PRESENTATION['vibe-coding']['headline']}</h2><p>{PRESENTATION['vibe-coding']['short']}</p><p class="tr-vibe-definition">Le Vibe coding : créer avec une IA qui écrit le code, pendant que vous donnez la direction et vérifiez le résultat.</p></div>
      <div class="tr-iso-stage reveal" aria-hidden="true"><div class="tr-iso"><div class="tr-plate tr-plate-idea"><span>01 / Le besoin</span><b>Une idée claire.</b><i></i></div><div class="tr-plate tr-plate-code"><span>02 / La méthode</span><div><i></i><i></i><i></i><i></i></div></div><div class="tr-plate tr-plate-web"><span>03 / La pratique</span><div class="tr-mini-browser"><i></i><i></i><i></i></div><div class="tr-mini-layout"><b></b><span></span><span></span></div><strong>À vous de créer ↗</strong></div></div></div></div>
      <ol class="tr-process" aria-label="Les étapes que vous apprenez">{process}</ol>
      <div class="tr-vibe-workshop"><div><p class="tr-small-label">Vous prenez la main</p><h3>7 h pour apprendre <em>en pratiquant.</em></h3><p>Sur votre ordinateur, je vous montre, vous essayez, nous reprenons ensemble ce qui bloque.</p><p class="tr-workshop-format">1 journée ou 2 séances de 3 h 30</p><p class="tr-training-scope">Des exercices guidés pour apprendre les bonnes pratiques et une méthode réutilisable. La réalisation d’un outil sur mesure pour chaque participant ne fait pas partie de la formation.</p></div><div class="tr-vibe-offer"><div class="tr-vibe-prices">{prices}</div><p class="tr-tax">{escape(t['tax_note'])}</p><a class="button amber" href="/contact/?besoin=formation&amp;programme=vibe-coding">Je veux apprendre à créer mon outil <span aria-hidden="true">↗</span></a></div></div>
      <div class="tr-vibe-included"><div><h3>Inclus dans les deux formules</h3><ul>{included}</ul></div><div><h3>Pour commencer</h3><p>{escape(t['prerequisites'])}</p><p class="tr-tools-label">Les outils que vous découvrez</p><div class="tr-vibe-tools">{tools}</div></div></div>
      {audio_summary(t['id'])}{program_details(t)}{detail_link(t['id'])}</article>'''


def formations_page():
    courses = ''.join(vibe_course(t) if t['id'] == 'vibe-coding' else standard_course(t) for t in training)
    shortcuts = ''.join(f'<a href="#{t["id"]}"><span>{t["num"]}</span><span>{PRESENTATION[t["id"]]["aim"]}</span><span aria-hidden="true">↘</span></a>' for t in training)
    return f'''<section class="container tr-hero"><nav class="breadcrumb" aria-label="Fil d’Ariane"><a href="/">Accueil</a><span aria-hidden="true">/</span><span>Formations</span></nav><div class="tr-hero-grid"><div><p class="eyebrow">Les formations EDS · En présentiel</p><h1>Formations IA. <br><em>Apprendre en faisant.</em></h1><p class="tr-lead">Gagner du temps, créer vos contenus ou apprendre à construire vos outils. Des formations en présentiel à Issoudun et en Centre-Val de Loire, sur votre ordinateur, avec Florian Rousseau.</p><a class="button" href="#programmes">Trouver ma formation <span aria-hidden="true">↓</span></a></div><aside class="tr-hero-aside"><span class="tr-hero-mark" aria-hidden="true">↗</span><p class="tr-aside-title">Vous pratiquez.<br>Je vous guide.</p><p>On essaie. On échange.<br>On reprend ce qui bloque.</p><div class="tr-trainer"><span>Avec Florian Rousseau<br><strong>Dans vos locaux, à vos côtés.</strong></span></div></aside></div></section>
    <section class="tr-catalog container" id="programmes" aria-labelledby="tr-catalog-heading"><div class="tr-catalog-heading"><div><p class="eyebrow">4 formations, un objectif : savoir faire</p><h2 id="tr-catalog-heading">Que voulez-vous <br>faire avec l’IA ?</h2></div><p>Un objectif clair. Un format adapté.<br>Choisissez votre point de départ.</p></div><nav class="tr-shortcuts" aria-label="Choisir une formation">{shortcuts}</nav><div class="tr-course-list">{courses}</div></section>
    <section class="container tr-practical"><div><p class="eyebrow">Simple à organiser</p><h2>On prépare la formation <br>avec vous.</h2></div><div><p>Votre objectif, votre niveau et les cas à travailler : nous précisons l’essentiel avant la session. Les formations à la journée peuvent aussi se répartir en deux demi-journées.</p><p class="seo-guide-link"><a href="/guides/choisir-formation-ia-entreprise/">Notre guide pour choisir une formation IA adaptée à votre entreprise ↗</a></p><details class="tr-logistics"><summary>Suivi, déplacements et outils</summary><div><p><strong>Le suivi :</strong> 30 jours pour IA métier et Communication ; 30 minutes dans les 30 jours pour le Vibe coding. Les modalités d’IA responsable dépendent du format choisi.</p><p><strong>Les déplacements :</strong> principalement en Centre-Val de Loire. Les frais sont facturés au réel au-delà de 60 km d’Issoudun.</p><p><strong>Les outils :</strong> les éventuels abonnements nécessaires sont précisés lors du cadrage. Le programme et le tarif sont définis avant engagement.</p><a class="text-link" href="/faq/">Les questions fréquentes <span aria-hidden="true">↗</span></a></div></details></div></section>
    {news_training()}
    <section class="tr-final" data-contact-section><div class="container tr-final-inner"><div><p class="eyebrow">Pas besoin d’avoir déjà choisi</p><h2>Parlons de ce que <br>vous aimeriez faire.</h2><p>30 minutes pour trouver la formation qui vous convient.<br>Gratuit, sans engagement.</p></div><a class="button amber" href="/contact/?besoin=formation">Échanger avec Florian <span aria-hidden="true">↗</span></a></div></section>'''
