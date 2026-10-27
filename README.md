# Escale Digitale Solutions — site officiel

Site public : https://eds-formation.fr/

Cette branche `main` contient le site statique servi automatiquement par GitHub Pages. Le domaine est conservé dans `CNAME`. `.nojekyll` désactive la transformation Jekyll. Les pages disposent de vrais répertoires ; aucune application serveur n’est nécessaire.

## Mettre à jour

Le générateur Python et ses données publiques sont conservés dans la branche `source/eds-redesign`. Exécuter `python build.py` dans cette branche, puis publier le contenu généré de `dist/` à la racine de `main`. Les modifications de `main` déclenchent le déploiement Pages existant. Ne pas publier les fichiers de travail internes.

Les quatre formations et leur guide sont reliés au catalogue. Les anciens chemins `/partenariat/` et `/parcours/` redirigent vers `/accompagnement/`. GitHub Pages ne propose pas de redirections HTTP 301 arbitraires : ces changements de page utilisent une redirection HTML immédiate et une URL canonique ; les liens restent également utilisables sans JavaScript.

## Sauvegarde

Ancienne version conservée dans `backup/avant-refonte-2026-10-27`, commit `82fd287d1ee978e0fee055fa512ef32ccf854ffe`. Elle permet de restaurer les anciens fichiers dans un nouveau commit sans réécrire l’historique.

## Référencement

Sitemap : https://eds-formation.fr/sitemap.xml

Douze pages indexables ; page 404 et redirections non indexables. Aucun avis, certificat ou résultat client inventé dans les données structurées. Le fichier `llms.txt` est un répertoire complémentaire, pas une garantie de référencement.

Search Console et Bing Webmaster Tools nécessitent un accès du propriétaire pour soumettre le sitemap et contrôler l’indexation réelle. Le code ne prétend pas effectuer cette connexion.
