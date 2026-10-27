# Sources du site EDS

Générer avec `python build.py` (Python 3, bibliothèque standard uniquement). Le dossier `dist/` est la sortie à publier dans la branche `main` du même dépôt. `SITE_ORIGIN` vaut par défaut `https://eds-formation.fr`. Les assets utilisés sont conservés dans `dist/assets/` et ne sont pas effacés par la génération.

`pages_extra.py` : offres et pages secondaires ; `training.py` : catalogue ; `course_pages.py` : fiches ; `guide.py` : guide ; `seo.py` : métadonnées et données structurées ; `legacy.py` : anciennes adresses ; `reels.py` et `content/` : références publiques et bandeaux. Les audios ne sont activés que lorsqu’un fichier local valide est renseigné dans `content/training-audio.json`.

Aucune recherche privée, pièce jointe de messagerie ou contenu d’audit interne n’est inclus. Les références commerciales se limitent aux informations publiques affichées sur le site.
