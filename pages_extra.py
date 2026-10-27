"""Secondary pages, deliberately rendered as real static HTML routes."""
from html import escape


def hero(kicker, title, description):
    return f'''<section class="page-hero container"><nav class="breadcrumb" aria-label="Fil d’Ariane"><a href="/">Accueil</a><span aria-hidden="true">/</span><span>{kicker}</span></nav><p class="eyebrow">{kicker}</p><h1>{title}</h1><p class="lead">{description}</p></section>'''


def cta(title="On commence par votre quotidien ?", text="Un échange gratuit de 30 minutes avec Florian pour comprendre votre besoin et choisir la suite.", besoin=""):
    return f'''<section class="container section"><div class="cta-panel"><div><p class="eyebrow">La prochaine escale</p><h2>{title}</h2><p>{text}</p></div><a class="button" href="/contact/{('?besoin=' + besoin) if besoin else ''}">Parlons de votre projet <span aria-hidden="true">↗</span></a></div></section>'''


def check(items):
    return '<ul class="check-list">' + ''.join(f'<li>{x}</li>' for x in items) + '</ul>'


def faq(items):
    return '<div class="faq-list">' + ''.join(f'<details><summary>{q}<span aria-hidden="true">+</span></summary><div class="faq-answer"><p>{a}</p></div></details>' for q,a in items) + '</div>'


# Shared course content; the catalogue itself is rendered by training.formations_page.
training = [
    dict(
        id="responsable", num="01", tag="Pour démarrer sereinement", title="IA responsable",
        desc="Une formation de sensibilisation pour découvrir les usages de l’IA, comprendre les risques et adopter les bons réflexes : données personnelles, confidentialité et vérification des réponses.",
        duration="À partir de 2 heures", price="Dès 300 € HT",
        price_detail="Durée et format adaptés à votre équipe.",
        items=[
            "Comprendre les usages, les limites et les erreurs possibles des IA génératives.",
            "Adopter les bons réflexes face aux données confidentielles, aux biais et aux contenus trompeurs.",
            "Situer les enjeux du RGPD, de l’AI Act et des droits d’auteur.",
            "Pratiquer vos premiers prompts et vérifier les réponses.",
        ],
        deliverable="Support de sensibilisation, fiche « 10 bons usages », quiz de validation et attestation de participation EDS.",
        note="Cette sensibilisation contribue à une démarche de maîtrise de l’IA. Elle ne constitue ni une certification officielle AI Act, ni un audit juridique.",
    ),
    dict(
        id="metier", num="02", tag="Pour les équipes opérationnelles", title="IA métier",
        desc="Emails, comptes rendus, documents et mise en place de petites automatisations simples : pratiquez l’IA sur les tâches du quotidien de votre équipe.",
        duration="8 heures · 1 journée ou 2 demi-journées de 4 h", price="600 € HT / personne",
        price_detail="Tarif dégressif à partir de 2 participants.",
        items=[
            "Choisir et configurer les outils adaptés à votre activité.",
            "Structurer une demande : contexte, objectif, sources et critères de qualité.",
            "Travailler sur vos documents préparés et anonymisés si nécessaire.",
            "Créer des prompts métier et des assistants pour vos tâches récurrentes.",
            "Mettre en place de petites automatisations simples, avec une vérification humaine.",
            "Vérifier les résultats et intégrer une routine de travail fiable.",
        ],
        deliverable="Votre bibliothèque de prompts métier et 30 jours de suivi après la formation.",
        note="RH, administratif, commercial, management, industrie ou collectivités : le programme est ajusté à vos usages.",
    ),
    dict(
        id="communication", num="03", tag="Pour donner vie à vos idées", title="IA communication",
        desc="Découvrez et utilisez les meilleurs outils IA pour votre domaine : images, vidéos, audio et textes. Passez de l’idée au contenu, avec des exercices concrets et une méthode fidèle à votre marque.",
        duration="8 heures · 1 journée ou 2 demi-journées de 4 h", price="600 € HT / personne",
        price_detail="Tarif dégressif à partir de 2 participants.",
        items=[
            "Repérer les outils IA les plus pertinents pour votre domaine, vos objectifs et vos moyens.",
            "Créer et retoucher des images : visuels de publication, illustrations et supports de présentation.",
            "Préparer une vidéo courte : scénario, séquences, montage et adaptation au bon format.",
            "Explorer l’audio : voix, narration et habillage sonore pour vos contenus.",
            "Rédiger des textes et décliner une idée en plusieurs formats, en gardant votre ton.",
            "Vérifier la qualité, les droits d’usage et le respect des personnes avant de publier.",
        ],
        deliverable="Vos exercices et une bibliothèque de prompts créatifs pour reproduire les étapes, avec 30 jours de suivi.",
        note="Nous sélectionnons les outils selon votre secteur, les formats à travailler et les abonnements disponibles. Les éventuels coûts sont précisés avant la formation.",
    ),
    dict(
        id="vibe-coding", num="04", tag="Pour apprendre à créer vos propres outils", title="Vibe coding",
        desc="Cet outil dont vous avez besoin depuis longtemps : apprenez comment le créer avec l’IA. Du cadrage à la mise en ligne, découvrez les bons outils et une méthode rapide, structurée et réutilisable.",
        duration="7 heures · 1 journée ou 2 séances de 3 h 30", price="990 €",
        price_detail="En individuel, pour 1 participant. À deux : 1 490 € au total, soit 745 € par personne.",
        pricing=[
            dict(label="En individuel", total="990 €", participants="1 participant", per_person=None),
            dict(label="À deux", total="1 490 €", participants="Au total pour 2", per_person="745 € par personne"),
        ],
        tax_note="Prix nets · TVA non applicable, article 293 B du CGI.",
        prerequisites="Être à l’aise sur ordinateur et avoir déjà utilisé un assistant IA. Aucune expérience en programmation nécessaire.",
        tools=["Codex", "Claude Code", "GitHub", "Hostinger"],
        included=[
            "Des exercices guidés, à votre rythme",
            "Un guide PDF pour refaire les étapes",
            "30 minutes de suivi dans les 30 jours après la formation",
        ],
        items=[
            "Comprendre les fondamentaux du Vibe coding : les possibilités, les limites et votre rôle dans les décisions.",
            "Cadrer un besoin : objectif, utilisateurs, fonctionnalités essentielles et critères de réussite.",
            "Découvrir Codex et Claude Code, puis apprendre à guider l’IA avec des consignes structurées.",
            "Avancer par petites étapes : créer une première version, tester, corriger et documenter.",
            "Utiliser GitHub pour garder des versions et suivre les modifications.",
            "Comprendre les étapes de mise en ligne avec Hostinger et les vérifications avant publication.",
        ],
        deliverable="Des exercices guidés, un guide PDF pour refaire les étapes et 30 minutes de suivi dans les 30 jours après la formation.",
        note="Vous prenez la main sur votre ordinateur. Je montre les étapes, vous pratiquez et nous reprenons ensemble ce qui bloque. L’objectif : acquérir la méthode pour créer vos outils en autonomie.",
    ),
]

accompagnement = '''<section class="page-hero container support-hero"><nav class="breadcrumb" aria-label="Fil d’Ariane"><a href="/">Accueil</a><span aria-hidden="true">/</span><span>Accompagnement</span></nav><div class="support-hero-grid"><div><p class="eyebrow">Accompagnement IA &amp; automatisation</p><h1>Moins de manipulations.<br>Plus de temps pour votre métier.</h1><p class="lead">Des documents à reprendre, des informations à recopier, des outils qui ne se parlent pas. Je vous aide à simplifier ces tâches avec des assistants IA et des automatisations adaptés à votre activité.</p><a class="button" href="/contact/?besoin=automatisation">Parlons de votre besoin <span aria-hidden="true">↗</span></a><p class="support-hero-meta">Premier échange gratuit · Accompagnement sur devis</p></div><aside class="support-start"><span aria-hidden="true">↗</span><p class="support-small-label">Le bon point de départ</p><h2>Une tâche.<br>Un besoin précis.</h2><p>Montrez-moi ce qui vous prend du temps. Nous examinons ce qui peut être simplifié, avec vos outils et vos contraintes.</p><a class="text-link" href="#exemples">Voir les possibilités <span aria-hidden="true">↓</span></a></aside></div></section>
<section class="container support-section" id="exemples" aria-labelledby="support-examples-title"><div class="support-heading"><div><p class="eyebrow">Dans votre quotidien</p><h2 id="support-examples-title">Qu’aimeriez-vous<br>arrêter de refaire ?</h2></div><p>Trois points de départ possibles.<br>Nous choisissons le vôtre ensemble.</p></div><div class="support-examples"><article><span class="support-index">01</span><div><h3>Recopier les mêmes informations</h3><p>Faire circuler une demande entre un formulaire, un tableau de suivi et une notification, sans ressaisir chaque information.</p></div><span class="support-result">Relier les étapes<br>entre vos outils.</span></article><article><span class="support-index">02</span><div><h3>Repartir d’une page blanche</h3><p>Préparer un compte rendu, une synthèse ou un projet de réponse à partir de vos documents et de consignes réutilisables.</p></div><span class="support-result">Un assistant prépare.<br>Vous vérifiez.</span></article><article><span class="support-index">03</span><div><h3>Réinventer la méthode à chaque fois</h3><p>Structurer vos prompts, vos modèles et vos règles d’usage pour que l’équipe sache quand utiliser l’IA et comment contrôler le résultat.</p></div><span class="support-result">Des pratiques claires,<br>faciles à retrouver.</span></article></div><p class="support-caption">Exemples illustratifs. La faisabilité dépend de vos outils, des accès disponibles et des données concernées.</p></section>
<section class="support-process"><div class="container support-section"><div class="support-heading"><div><p class="eyebrow">Comment nous avançons</p><h2>Une solution utile.<br>Et une équipe qui sait s’en servir.</h2></div><p>Du premier besoin à la prise en main, vous gardez de la visibilité sur ce qui est construit.</p></div><ol class="support-steps"><li><span>01</span><h3>Cadrer avant de construire</h3><p>Nous regardons votre fonctionnement actuel, les utilisateurs et le résultat attendu. Le périmètre, les étapes et le tarif sont fixés au devis.</p></li><li><span>02</span><h3>Tester sur un cas concret</h3><p>Une première version permet de vérifier le fonctionnement, les erreurs possibles et les validations à conserver. Nous ajustons à partir de vos retours.</p></li><li><span>03</span><h3>Vous transmettre la prise en main</h3><p>Vous apprenez à utiliser la solution, à vérifier les résultats et à repérer les situations qui demandent votre intervention.</p></li></ol><div class="support-handoff"><div><p class="support-small-label">Ce qui est défini dans votre proposition</p><h3>Un cadre clair,<br>jusqu’à la suite.</h3></div><ul><li>Les assistants ou automatisations à mettre en place.</li><li>Les tests, les consignes d’utilisation et la prise en main.</li><li>Les licences nécessaires, le suivi et la maintenance éventuelle.</li></ul></div></div></section>
<section class="container support-section support-decisions" aria-labelledby="support-decisions-title"><div><p class="eyebrow">Simple, mais maîtrisé</p><h2 id="support-decisions-title">Les outils travaillent.<br>Vous gardez les décisions.</h2><p>Nous précisons quelles données peuvent être utilisées, qui accède à quoi et à quel moment une personne doit valider. Une automatisation utile doit aussi rester compréhensible.</p><div class="support-tool-line"><span>Selon le besoin</span><strong>n8n</strong><strong>Make</strong><strong>Google Workspace</strong><strong>Assistants IA</strong></div></div><div class="support-mini-flow" aria-label="Exemple d’automatisation avec validation humaine"><p class="support-small-label">Exemple de fonctionnement</p><ol><li><span aria-hidden="true">01</span><div><strong>Une demande arrive</strong><span>Formulaire ou email</span></div></li><li><span aria-hidden="true">02</span><div><strong>Les informations sont préparées</strong><span>Classement, synthèse ou brouillon</span></div></li><li class="support-human-step"><span aria-hidden="true">✓</span><div><strong>Vous vérifiez et validez</strong><span>Avant l’action prévue</span></div></li></ol></div></section>
<section class="container support-section support-faq" aria-labelledby="support-faq-title"><div><p class="eyebrow">Avant de vous lancer</p><h2 id="support-faq-title">Quelques réponses<br>pour décider.</h2></div><div>''' + faq([
    ("Peut-on commencer par une seule tâche ?", "Oui. Un besoin précis permet de définir un périmètre, d’essayer une première solution et de décider ensuite si d’autres étapes méritent d’être traitées."),
    ("Faut-il changer tous nos outils ?", "Nous partons de ceux que vous utilisez déjà et vérifions les possibilités de connexion. Si un autre outil est nécessaire, son rôle et son coût sont précisés avant de commencer."),
    ("Comment sont définis le prix et le suivi ?", "L’accompagnement est sur devis, selon le périmètre du projet. Les livrables, les éventuels abonnements, la prise en main, le suivi et la maintenance sont précisés dans la proposition."),
    ("Formation ou accompagnement : que choisir ?", "La formation vous apprend à faire et à reproduire les étapes. L’accompagnement porte sur la mise en place d’une solution définie ensemble. Le premier échange permet de choisir la formule adaptée à votre besoin."),
]) + '''</div></section>
<section class="container support-next" data-contact-section><div><h2>Quelle tâche aimeriez-vous simplifier ?</h2><p>30 minutes avec Florian pour regarder votre besoin. Gratuit, sans engagement.</p></div><a class="button" href="/contact/?besoin=automatisation">En parler avec Florian <span aria-hidden="true">↗</span></a></section>'''

apropos = hero("À propos &amp; contact", "Faisons connaissance.", "Je suis Florian Rousseau, fondateur d’Escale Digitale Solutions à Issoudun. J’aide les professionnels à comprendre l’IA, à l’utiliser dans leur métier et à simplifier leur quotidien.").replace('class="page-hero container"', 'class="page-hero container about-intro"')
apropos += '''<section class="container about-note about-contact" aria-label="Florian et les moyens de contact"><figure class="about-snapshot"><div class="snapshot-round"><img src="/assets/florian-portrait.webp" alt="Florian Rousseau, fondateur d’Escale Digitale Solutions" width="512" height="512" loading="lazy"></div><figcaption><strong>Florian Rousseau</strong><span>Fondateur d’Escale Digitale Solutions</span><p>Votre interlocuteur pour la formation et l’accompagnement IA, en Centre-Val de Loire.</p></figcaption></figure><div class="about-contact-panel" id="contact" data-contact-section><p class="eyebrow">Échangeons directement</p><h2>Parlons de <br>votre projet.</h2><div class="contact-routes"><a class="contact-route contact-route-mail" href="mailto:escale.digitale.solutions@gmail.com"><span class="contact-route-icon" aria-hidden="true"><svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="7" width="24" height="18" rx="3"/><path d="m5 9 11 8 11-8"/></svg></span><span class="contact-route-copy"><strong>M’écrire par email</strong><span>escale.digitale.solutions@gmail.com</span></span><span class="contact-route-arrow" aria-hidden="true">↗</span></a><a class="contact-route" href="https://www.linkedin.com/in/escaledigitalesolutions/" target="_blank" rel="noopener noreferrer"><span class="contact-route-icon"><img src="/assets/contact/linkedin.png" alt="" width="635" height="540"></span><span class="contact-route-copy"><strong>Échanger sur LinkedIn</strong><span>Retrouvez mon profil et envoyez-moi un message.</span></span><span class="contact-route-arrow" aria-hidden="true">↗</span></a><a class="contact-route contact-route-booking" href="https://calendly.com/florianrouss92/30min" target="_blank" rel="noopener noreferrer"><span class="contact-route-icon"><img src="/assets/contact/calendly.svg" alt="" width="144" height="144"></span><span class="contact-route-copy"><strong>Prendre rendez-vous</strong><span>Choisissez votre créneau sur Calendly · 30 min.</span></span><span class="contact-route-arrow" aria-hidden="true">↗</span></a></div><p class="about-contact-note">Vous échangez directement avec moi.<br>Le premier rendez-vous est gratuit, sans engagement.</p></div></section>'''


apropos += '''<section class="container about-approach" aria-labelledby="about-approach-title"><div><p class="eyebrow">Ma façon de travailler</p><h2 id="about-approach-title">Partir de votre métier.<br>Vous aider à avancer.</h2><p>L’outil change. Votre besoin reste le point de départ. Nous travaillons sur des situations concrètes, avec des explications claires et le temps de reprendre ce qui bloque.</p><div class="about-local"><span aria-hidden="true">↗</span><p><strong>À Issoudun, et dans vos locaux.</strong><br>Les modalités et les déplacements sont précisés avant de commencer.</p></div></div><ol><li><span>01</span><div><h3>Écouter votre réalité</h3><p>Vos tâches, vos outils et le niveau de l’équipe, avant de proposer une solution.</p></div></li><li><span>02</span><div><h3>Faire avec vous</h3><p>Des démonstrations, des essais et des ajustements pour comprendre les étapes.</p></div></li><li><span>03</span><div><h3>Vous laisser les repères</h3><p>Des supports et des consignes pour refaire, vérifier et continuer après notre intervention.</p></div></li></ol></section>'''

faq_body = hero("Questions fréquentes", "Les réponses claires.<br>Avant de vous lancer.", "Niveau, formats, tarifs, données : les informations utiles pour préparer votre projet.")
faq_groups = [
    ("Commencer", [
        ("Faut-il déjà connaître l’IA ?", "IA responsable permet de débuter. Pour IA métier et IA communication, le niveau est précisé ensemble avant la session. Pour le Vibe coding, il faut être à l’aise sur ordinateur et avoir déjà utilisé un assistant IA. Aucune expérience en programmation n’est nécessaire."),
        ("Comment choisir la bonne formation ?", "IA responsable pour sensibiliser votre équipe aux usages et aux risques ; IA métier pour les tâches du quotidien et les petites automatisations simples ; IA communication pour créer des images, vidéos, audios et textes ; Vibe coding pour apprendre à concevoir et mettre en ligne ses propres outils avec l’IA. Le premier échange permet de choisir le bon point de départ."),
        ("Vais-je repartir avec mon outil sur mesure terminé ?", "Le Vibe coding est une formation pour apprendre à créer. Vous pratiquez sur des exercices guidés et découvrez la méthode, les outils et les étapes jusqu’à la mise en ligne. Florian transmet les bonnes pratiques ; la création et la livraison de l’outil personnel de chaque participant ne font pas partie de cette formation."),
        ("Est-ce adapté à mon secteur ?", "Le programme est personnalisé selon votre activité, vos outils et vos usages : services, industrie, commerce, ressources humaines, administratif ou collectivités. Les situations particulières et les contraintes de confidentialité sont examinées avant la session.")]),
    ("Organisation & tarifs", [
        ("Où ont lieu les formations ?", "Principalement dans vos locaux, en Centre-Val de Loire. EDS est basé à Issoudun. Au-delà de 60 km, les frais de déplacement sont facturés au réel et précisés dans votre devis. D’autres modalités peuvent être étudiées sur demande."),
        ("Combien de temps faut-il prévoir ?", "IA responsable commence à 2 heures, avec un format adapté au besoin. IA métier et IA communication durent 8 heures, en une journée ou deux demi-journées de 4 heures. Le Vibe coding dure 7 heures, en une journée ou deux séances de 3 h 30. Nous définissons les dates et le rythme ensemble."),
        ("Quels sont les tarifs ?", "IA responsable : à partir de 300 € HT. IA métier et IA communication : 600 € HT par personne pour 8 heures, avec un tarif dégressif dès 2 participants. Vibe coding : 990 € en individuel, ou 1 490 € au total à deux, soit 745 € par personne, pour 7 heures. Pour le Vibe coding, les prix sont nets : TVA non applicable, article 293 B du CGI. L’automatisation et l’accompagnement font l’objet d’un devis. Le montant applicable et les frais éventuels sont confirmés avant engagement."),
        ("Une prise en charge financière est-elle possible ?", "Les possibilités dépendent de votre situation, du dispositif et des conditions applicables au moment de votre demande. Nous examinons ces éléments avant toute inscription. Aucune prise en charge n’est garantie et aucun label de certification n’est revendiqué sur cette version du site."),
        ("Un suivi est-il inclus ?", "IA métier et IA communication comprennent 30 jours de suivi. Le Vibe coding inclut un rendez-vous de suivi de 30 minutes dans les 30 jours après la formation, en individuel comme à deux. Pour IA responsable, les modalités dépendent du format choisi.")]),
    ("Outils & données", [
        ("Travaille-t-on sur nos propres documents ?", "Oui, sur des exemples préparés ensemble. Les données sensibles ou confidentielles doivent être retirées, anonymisées ou traitées dans un environnement approprié avant leur utilisation. Le choix des documents fait partie du cadrage."),
        ("Quels outils allons-nous utiliser ?", "Les outils sont sélectionnés pour votre besoin : ChatGPT, Claude, Gemini et des solutions de création d’images, de vidéos ou d’audio pour la communication. Le Vibe coding aborde Codex, Claude Code, GitHub et Hostinger. Pour l’automatisation, n8n, Make et Google Workspace peuvent être utilisés. Les éventuels abonnements payants sont précisés avant la prestation."),
        ("La formation nous rend-elle automatiquement conformes à l’AI Act ?", "Non. Une formation peut contribuer à la maîtrise de l’IA et à la sensibilisation des équipes. Elle ne remplace pas l’analyse de vos obligations, ni un audit juridique. Les règles dépendent notamment de votre rôle et de vos usages."),
        ("Peut-on garder une validation humaine dans une automatisation ?", "Oui. Le rôle des personnes, les étapes de validation et le traitement des erreurs sont définis lors de la conception. Les actions qui ont un impact important doivent faire l’objet de contrôles adaptés.")]),
]
for title,items in faq_groups:
    faq_body += f'<section class="container section"><div class="split"><div><p class="eyebrow">Vos questions</p><h2>{title}</h2></div><div>{faq(items)}</div></div></section>'
faq_body += cta("Votre question est plus précise ?", "Parlons de votre situation. Vous échangerez directement avec Florian.")
faq_answers = {question: answer for _, items in faq_groups for question, answer in items}
about_questions = [
    ("Comment se passe le premier échange ?", "Nous prenons 30 minutes pour parler de votre activité, de votre besoin et des personnes concernées. Cet échange est gratuit et sans engagement. Une tâche à simplifier ou une envie d’apprendre suffit pour commencer."),
    ("Formation ou accompagnement : quelle différence ?", "En formation, vous apprenez à utiliser les outils et à refaire les étapes. En accompagnement, nous définissons une solution à mettre en place dans votre organisation. Nous choisissons le bon point de départ ensemble."),
    ("Faut-il déjà connaître l’IA ?", faq_answers["Faut-il déjà connaître l’IA ?"]),
    ("Où ont lieu les formations ?", faq_answers["Où ont lieu les formations ?"]),
    ("Peut-on répartir une formation sur deux demi-journées ?", "Oui. IA métier et IA communication peuvent se dérouler en deux séances de 4 heures ; le Vibe coding en deux séances de 3 h 30. Le rythme de la sensibilisation IA responsable est adapté au besoin."),
    ("Un suivi est-il inclus ?", faq_answers["Un suivi est-il inclus ?"]),
]
apropos += '<section class="container about-faq" id="faq" aria-labelledby="about-faq-title"><div><p class="eyebrow">Vos questions, avant de me contacter</p><h2 id="about-faq-title">Les réponses utiles.</h2><p>Pour préparer notre échange en toute simplicité.</p><a class="text-link" href="/faq/">Toutes les questions fréquentes <span aria-hidden="true">↗</span></a></div><div>' + faq(about_questions) + '</div></section>'


legal = hero("Mentions légales & confidentialité", "Les informations<br>essentielles.", "Éditeur, hébergement, contacts et traitement des données du site EDS.")
legal += '''<section class="section container legal-content"><article><h2>Éditeur</h2><p>Escale Digitale Solutions — Florian Rousseau, entrepreneur individuel.<br>Responsable de publication : Florian Rousseau.<br>Adresse : 2 rue du Maine, 36100 Issoudun, France.<br>SIRET : 949 409 015 00011.</p><p>Contact : <a href="mailto:escale.digitale.solutions@gmail.com">escale.digitale.solutions@gmail.com</a>.</p><p>Activité : formation professionnelle en intelligence artificielle, conseil et accompagnement.</p><p>Déclaration d’activité enregistrée sous le numéro 24 36 01193 36 auprès du préfet de la région Centre-Val de Loire. Cet enregistrement ne vaut pas agrément de l’État.</p></article><article><h2>Hébergement</h2><p>Le site eds-formation.fr est hébergé par GitHub Pages, un service de GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis.</p><p>Contact de l’hébergeur : <a href="https://support.github.com/contact">support GitHub</a>. Informations sur les traitements techniques et les droits : <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement">déclaration de confidentialité de GitHub</a>.</p></article><article><h2>Vos demandes de contact</h2><p>Le formulaire de contact prépare un email dans votre propre messagerie. Il ne transmet aucun message automatiquement et n’enregistre pas les informations saisies sur un serveur du site. Vous choisissez d’envoyer ou non votre message.</p><p>La prise de rendez-vous s’effectue sur Calendly, un service tiers. Sa politique de confidentialité s’applique lors de l’utilisation de ce service. Les liens LinkedIn ouvrent également un service tiers.</p><p>Les informations que vous transmettez volontairement à EDS sont utilisées pour répondre à votre demande et assurer le suivi de la relation commerciale. Elles ne sont pas revendues. Pour les contacts commerciaux, la durée de conservation annoncée par EDS est de trois ans à compter du dernier contact.</p></article><article><h2>Vos droits</h2><p>Vous pouvez demander l’accès, la rectification ou l’effacement de vos données, ainsi que la limitation du traitement et, selon les conditions applicables, la portabilité ou l’opposition au traitement.</p><p>Pour exercer ces droits, écrivez à <a href="mailto:escale.digitale.solutions@gmail.com">escale.digitale.solutions@gmail.com</a>. Vous pouvez également adresser une réclamation à la <a href="https://www.cnil.fr/fr/plaintes" target="_blank" rel="noopener noreferrer">CNIL</a>.</p></article><article><h2>Cookies et mesure d’audience</h2><p>Ce site n’intègre pas de publicité, de pixel de suivi ou d’outil de mesure d’audience ajouté par EDS. Le service d’hébergement peut utiliser des dispositifs techniques nécessaires à l’accès et au fonctionnement de la publication.</p></article><article><h2>Contenus et marques</h2><p>Le logo EDS et les contenus propres à Escale Digitale Solutions sont protégés. Toute réutilisation nécessite l’autorisation de leur titulaire. Les marques et logos d’outils présentés appartiennent à leurs propriétaires respectifs. Leur présence identifie les outils évoqués et ne constitue pas une annonce de partenariat ou de certification.</p></article><article><h2>Informations sur les prestations</h2><p>Les tarifs portant la mention HT sont indiqués hors taxes. Les tarifs de la formation Vibe coding sont des prix nets : TVA non applicable, article 293 B du CGI. Le montant applicable, les éventuelles taxes, le programme, les modalités et les frais sont précisés dans une proposition avant engagement. Les exemples d’usage sont illustratifs et ne garantissent pas un résultat identique pour chaque organisation.</p><p>Les contenus de sensibilisation aux risques et à la réglementation ne constituent pas un conseil juridique individualisé.</p></article></section>'''

PAGES = {
    "formations": {"title": "Formations IA en entreprise à Issoudun · EDS", "description": "Formations IA responsable, métier, communication et Vibe coding en Centre-Val de Loire. Apprenez en pratiquant : images, vidéos, audio et création d’outils avec l’IA.", "active": "formations", "body": ""},
    "accompagnement": {"title": "Accompagnement IA & automatisation pour PME · EDS", "description": "Simplifiez les tâches répétitives avec des assistants IA et des automatisations adaptés à vos outils. Cadrage, tests et prise en main avec Florian Rousseau. Sur devis.", "active": "accompagnement", "body": accompagnement},
    "a-propos": {"title": "À propos & contact · Florian Rousseau · EDS", "description": "Faites connaissance avec Florian Rousseau et contactez EDS par email, sur LinkedIn ou via Calendly. Premier échange de 30 minutes offert.", "active": "a-propos", "body": apropos},
    "faq": {"title": "Questions fréquentes sur les formations IA · EDS", "description": "Niveau requis, durée, tarifs, déplacements, suivi et protection des données : les réponses pour préparer votre formation ou accompagnement IA.", "active": "", "body": faq_body},
    "mentions-legales": {"title": "Mentions légales & confidentialité · EDS", "description": "Informations sur l’éditeur Escale Digitale Solutions, les contacts, la confidentialité et les services tiers.", "active": "", "body": legal},
}
