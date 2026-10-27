"""Searchable course pages: shared commercial facts, distinct practical guidance."""
from html import escape
from pages_extra import training, faq
from training import audio_summary

CNIL = 'https://www.cnil.fr/fr/intelligence-artificielle/ia-comment-etre-en-conformite-avec-le-rgpd'
AI_ACT = 'https://digital-strategy.ec.europa.eu/en/faqs/ai-literacy-questions-answers'
COURSES = {
    'responsable': {
        'slug': 'sensibilisation-ia', 'name': 'Formation de sensibilisation à l’IA en entreprise',
        'title': 'Sensibilisation IA en entreprise · RGPD & AI Act | EDS',
        'description': 'Sensibilisez vos équipes aux usages et aux risques de l’IA : données, RGPD, AI Act et premiers prompts. Dès 2 h et 300 € HT. EDS à Issoudun.',
        'answer': 'La formation IA responsable d’EDS aide vos équipes à comprendre les possibilités et les limites de l’intelligence artificielle. À partir de 2 heures, elle associe découverte, premiers exercices et repères sur les données personnelles, le RGPD et l’AI Act. Elle s’adresse aussi aux personnes qui n’ont jamais utilisé un assistant IA.',
        'audience': 'Dirigeants, salariés, associations et collectivités qui souhaitent partager des repères communs avant de développer leurs usages de l’IA.',
        'prerequisites': 'Aucune connaissance préalable de l’IA. Le niveau et le format sont précisés avec vous avant la session.',
        'example_title': 'Un email à résumer, des informations à protéger.',
        'example': 'À partir d’un exemple fictif, repérez ce qui peut être transmis à un assistant et ce qui doit être retiré. Rédigez une première consigne, puis comparez la synthèse à l’original. L’exercice permet de distinguer une réponse convaincante d’une réponse exacte.',
        'outcome': 'Savoir identifier un usage pertinent, reconnaître les limites d’une réponse et décider quand une vérification ou un avis spécialisé est nécessaire.',
        'faqs': [
            ('Cette sensibilisation est-elle adaptée aux débutants ?', 'Oui. Elle part des usages concrets et du vocabulaire essentiel. Les premiers prompts et les vérifications sont pratiqués pendant la session.'),
            ('Est-ce une certification de conformité à l’AI Act ?', 'Non. Le programme apporte des repères et contribue à la sensibilisation des équipes. Il ne délivre pas de certification officielle AI Act et ne remplace pas un audit juridique. Une attestation de participation EDS est prévue.'),
            ('Peut-on adapter la durée à notre équipe ?', 'Oui. Le format commence à 2 heures, dès 300 € HT. La durée, le nombre de participants et le périmètre sont précisés dans une proposition avant engagement.'),
        ],
    },
    'metier': {
        'slug': 'ia-metier', 'name': 'Formation IA métier et petites automatisations',
        'title': 'Formation IA métier & automatisations simples | EDS',
        'description': 'Pratiquez l’IA sur vos emails, comptes rendus et documents, avec de petites automatisations simples. 8 h, dès 600 € HT par personne. EDS à Issoudun.',
        'answer': 'La formation IA métier d’EDS apprend à utiliser les assistants IA sur les tâches récurrentes de votre équipe : emails, comptes rendus, documents et petites automatisations simples. Elle dure 8 heures, en une journée ou deux demi-journées de 4 heures, avec des exercices adaptés à votre activité.',
        'audience': 'Professionnels des fonctions administratives, RH, commerciales ou de management, dans les entreprises et les collectivités.',
        'prerequisites': 'Le niveau est précisé lors du premier échange. Préparez un ordinateur et des exemples de tâches ; les documents utilisés sont sélectionnés et anonymisés si nécessaire.',
        'example_title': 'Des notes de réunion à un plan d’action vérifié.',
        'example': 'Donnez à l’assistant des notes préparées, un format de sortie et des critères précis. Vérifiez les décisions, les responsables et les échéances. Vous apprenez ensuite à réutiliser la consigne et à examiner une petite automatisation entre vos outils, en conservant une étape de validation.',
        'outcome': 'Repartir avec des prompts métier réutilisables et savoir contrôler les résultats avant de les intégrer au travail de l’équipe.',
        'faqs': [
            ('Quels assistants IA peut-on apprendre à utiliser ?', 'ChatGPT, Claude ou Gemini peuvent être abordés selon vos besoins et vos accès. Le choix se fait avant la session ; il ne s’agit pas de parcourir tous les outils sans objectif métier.'),
            ('Les petites automatisations sont-elles incluses ?', 'Oui. Le programme comprend la mise en place de petites automatisations simples, avec une vérification humaine. Leur choix dépend de vos outils et des accès disponibles. Un projet plus étendu relève d’un accompagnement sur devis.'),
            ('Quel est le tarif de la formation IA métier ?', 'Le tarif est de 600 € HT par personne pour 8 heures, avec un tarif dégressif à partir de 2 participants. La formation comprend une bibliothèque de prompts métier et 30 jours de suivi.'),
        ],
    },
    'communication': {
        'slug': 'ia-communication', 'name': 'Formation IA pour la communication : image, vidéo et audio',
        'title': 'Formation IA communication · Image, vidéo, audio | EDS',
        'description': 'Découvrez et pratiquez les outils IA pour vos images, vidéos, voix et textes. Formation de 8 h adaptée à votre domaine, 600 € HT par personne.',
        'answer': 'La formation IA communication d’EDS vous fait découvrir et utiliser les outils IA adaptés à votre domaine pour créer des images, des vidéos, de l’audio et des textes. Pendant 8 heures, vous pratiquez sur votre ordinateur et apprenez à choisir les outils et les formats selon votre objectif et votre marque.',
        'audience': 'Professionnels de la communication, indépendants et équipes qui produisent des contenus pour leur activité, sans devoir devenir spécialistes de chaque outil.',
        'prerequisites': 'Le niveau, les comptes disponibles et les formats prioritaires sont précisés avant la session. Préparez un ordinateur et, si vous en disposez, des exemples de votre communication.',
        'example_title': 'Une idée, trois supports pour votre activité.',
        'example': 'À partir d’un brief fictif ou préparé ensemble, formulez une intention visuelle, construisez le scénario d’une vidéo courte et préparez une narration audio. Comparez les propositions de l’IA, corrigez ce qui ne correspond pas à votre marque et vérifiez les droits avant de publier.',
        'outcome': 'Savoir choisir un outil pour un format précis, écrire un brief exploitable et améliorer le contenu obtenu plutôt que publier le premier résultat.',
        'faqs': [
            ('La formation couvre-t-elle la vidéo et l’audio ?', 'Oui. Le programme comprend les images, les vidéos courtes, les voix et l’habillage sonore, ainsi que les textes. Les formats à approfondir sont choisis avec vous selon votre domaine.'),
            ('Quels outils créatifs allons-nous utiliser ?', 'Les outils sont sélectionnés selon les formats, votre secteur et les abonnements disponibles. Les solutions présentées par EDS comprennent notamment Gemini, Suno et ElevenLabs ; leur utilisation en session dépend du programme convenu.'),
            ('Les abonnements aux outils sont-ils inclus ?', 'Les éventuels abonnements nécessaires et leurs coûts sont précisés avant la formation. Le tarif pédagogique est de 600 € HT par personne pour 8 heures, avec un tarif dégressif dès 2 participants et 30 jours de suivi.'),
        ],
    },
    'vibe-coding': {
        'slug': 'vibe-coding', 'name': 'Formation Vibe coding : du cadrage à la mise en ligne',
        'title': 'Formation Vibe coding · Codex, Claude Code & GitHub | EDS',
        'description': 'Apprenez à créer avec l’IA : cadrage, Codex, Claude Code, GitHub et mise en ligne. 7 h, 990 € seul ou 1 490 € à deux. Sans expérience en programmation.',
        'answer': 'La formation Vibe coding d’EDS enseigne une méthode pour concevoir un outil avec une IA qui écrit le code : cadrer le besoin, construire par étapes, tester, garder des versions et comprendre la mise en ligne. Vous pratiquez pendant 7 heures avec Codex, Claude Code, GitHub et Hostinger. Aucune expérience en programmation n’est nécessaire.',
        'audience': 'Professionnels qui souhaitent comprendre comment créer un site ou un petit outil avec l’aide de l’IA, puis reproduire la méthode en autonomie.',
        'prerequisites': 'Être à l’aise sur ordinateur et avoir déjà utilisé un assistant IA. Aucune expérience en programmation nécessaire.',
        'example_title': 'D’une idée vague à une première version testable.',
        'example': 'Sur un exercice guidé, décrivez les utilisateurs, les fonctionnalités essentielles et les critères de réussite. Demandez à l’IA une première étape, testez-la et corrigez les erreurs avant d’ajouter une fonction. Vous découvrez ensuite comment conserver les versions et préparer une publication.',
        'outcome': 'Comprendre un processus de création réutilisable, savoir guider l’IA et identifier les vérifications nécessaires avant de mettre un outil en ligne.',
        'faqs': [
            ('Florian crée-t-il mon outil pendant la formation ?', 'Non. Florian enseigne les outils, les bonnes pratiques et la structuration du travail. Vous pratiquez sur des exercices guidés. La création et la livraison de l’outil personnel de chaque participant ne font pas partie de cette formation.'),
            ('Peut-on apprendre le Vibe coding sans savoir programmer ?', 'Oui, sans expérience préalable en programmation. Il faut toutefois être à l’aise sur ordinateur et avoir déjà utilisé un assistant IA. Vous apprenez à cadrer, tester et corriger ; l’IA ne dispense pas de comprendre et vérifier le résultat.'),
            ('Quel est le prix et peut-on venir à deux ?', 'La formation de 7 heures coûte 990 € en individuel ou 1 490 € au total pour deux participants, soit 745 € par personne. Prix nets, TVA non applicable, article 293 B du CGI. Un guide PDF et 30 minutes de suivi dans les 30 jours sont inclus.'),
            ('Peut-on répartir les 7 heures sur deux séances ?', 'Oui. La formation peut se dérouler en une journée ou en deux séances de 3 h 30. Le rythme et les dates sont définis ensemble avant engagement.'),
        ],
    },
}


def course_path(course_id):
    return '/formations/' + COURSES[course_id]['slug'] + '/'


def course_page(t):
    m = COURSES[t['id']]
    program = ''.join(f'<li>{escape(item)}</li>' for item in t['items'])
    related = ''.join(f'<a href="{course_path(cid)}">{escape(x["name"])} <span aria-hidden="true">↗</span></a>' for cid,x in COURSES.items() if cid != t['id'])
    scope = '<p><strong>Une formation pour apprendre à faire.</strong> La création et la livraison de votre outil personnel ne font pas partie de la prestation.</p>' if t['id']=='vibe-coding' else ''
    sources = f'<p class="seo-sources">Pour approfondir : <a href="{CNIL}">les repères IA et RGPD de la CNIL</a> et <a href="{AI_ACT}">les questions-réponses de la Commission européenne sur la maîtrise de l’IA</a>.</p>' if t['id']=='responsable' else ''
    tax = f'<p class="course-small">{escape(t["tax_note"])}</p>' if 'tax_note' in t else ''
    return f'''<section class="container page-hero course-hero"><nav class="breadcrumb" aria-label="Fil d’Ariane"><a href="/">Accueil</a><span aria-hidden="true">/</span><a href="/formations/">Formations</a><span aria-hidden="true">/</span><span>{escape(t['title'])}</span></nav><p class="eyebrow">Formation en présentiel · Issoudun &amp; Centre-Val de Loire</p><h1>{escape(m['name'])}</h1><p class="lead">{escape(m['answer'])}</p><div class="course-facts"><div><span>Le format</span><strong>{escape(t['duration'])}</strong></div><div><span>Le tarif</span><strong>{escape(t['price'])}</strong><p>{escape(t['price_detail'])}</p>{tax}</div></div><a class="button" href="/contact/?besoin=formation&amp;programme={t['id']}">Parlons de cette formation <span aria-hidden="true">↗</span></a></section>
    <section class="container course-section course-split"><div><p class="eyebrow">Est-ce pour vous ?</p><h2>Votre point de départ.</h2><p>{escape(m['audience'])}</p><h3>Les prérequis</h3><p>{escape(m['prerequisites'])}</p></div><div class="course-objective"><p class="eyebrow">L’objectif pédagogique</p><h2>Ce que vous apprenez.</h2><p>{escape(m['outcome'])}</p>{scope}</div></section>
    <section class="container course-section course-split"><div><p class="eyebrow">Le programme</p><h2>Des étapes concrètes.<br>De la pratique.</h2><ol class="course-program">{program}</ol></div><aside class="course-example"><p class="eyebrow">Exemple d’exercice</p><h3>{escape(m['example_title'])}</h3><p>{escape(m['example'])}</p><p class="course-small">Exemple illustratif, adapté lors du cadrage de votre session.</p></aside></section>
    <section class="container course-section course-split"><div><h2>Après la formation.</h2><p>{escape(t['deliverable'])}</p><p>{escape(t['note'])}</p>{sources}{audio_summary(t['id'])}</div><div><h2>Comment l’organiser ?</h2><p>La formation est animée par <a href="/a-propos/">Florian Rousseau, fondateur d’EDS à Issoudun</a>, principalement dans vos locaux en Centre-Val de Loire. Nous précisons votre objectif, le niveau des participants et les outils disponibles avant de fixer le programme.</p><p>Les dates sont convenues ensemble. Les frais de déplacement sont facturés au réel au-delà de 60 km d’Issoudun. Les éventuels abonnements et frais sont précisés avant engagement.</p><p>Un besoin particulier pour participer ? <a href="/contact/">Signalez-le lors de notre échange</a> pour étudier les modalités adaptées.</p></div></section>
    <section class="container course-section course-split"><div><p class="eyebrow">Avant de vous décider</p><h2>Vos questions sur cette formation.</h2></div>{faq(m['faqs'])}</section>
    <section class="container course-section course-related"><h2>Un autre objectif ?</h2><div>{related}</div><a class="text-link" href="/guides/choisir-formation-ia-entreprise/">Comment choisir votre formation IA ? <span aria-hidden="true">↗</span></a></section>
    <section class="container course-next" data-contact-section><div><h2>Précisons votre besoin.</h2><p>30 minutes avec Florian. Gratuit, sans engagement.</p></div><a class="button" href="/contact/?besoin=formation&amp;programme={t['id']}">Préparer ma formation <span aria-hidden="true">↗</span></a></section>'''


def course_pages():
    return {'formations/'+COURSES[t['id']]['slug']: {
        'title': COURSES[t['id']]['title'], 'description': COURSES[t['id']]['description'],
        'active':'formations', 'body':course_page(t), 'course_id':t['id'],
        'label':t['title'], 'faqs':COURSES[t['id']]['faqs'],
    } for t in training}
