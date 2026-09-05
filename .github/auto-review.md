# Règles de relecture du dépôt

Ce dépôt est un skill Claude d'expertise RH pour l'ANSM (établissement public
de l'État, fonction publique d'État). Il est construit sur l'architecture de
`drh-fpt` (fonction publique territoriale) : la méthode se transpose, le
contenu métier ne se transpose jamais tel quel.

## À vérifier en priorité, dans cet ordre

- **Aucun contenu de document RH interne dans le dépôt.** La politique du
  registre est `metadata-only-no-confidential-content`
  (`evals/internal-source-requirements.json`) : un document interne obtenu
  ne doit jamais être recopié, résumé avec ses valeurs, ni joint. Seules ses
  métadonnées (référence, statut, date) y ont leur place. Un diff qui ajoute
  un nom d'agent, un matricule, une adresse mail, un numéro de téléphone, un
  IBAN ou un NIR est **grave**, quel que soit le fichier : le contrôle
  `scripts/privacy_scan.py` existe mais n'est pas exécuté par la CI
  (`.github/workflows/validate.yml`), la relecture est donc la seule
  vérification avant fusion.
- **Aucune valeur, délai ou procédure inventés.** Une grille indiciaire, une
  durée d'échelon, un quota, un délai électoral ajoutés sans source primaire
  citée dans `references/sources-principales.md` sont un constat, pas une
  question.
- **Ne pas transposer une règle d'une autre fonction publique.** Un délai,
  une instance ou une procédure propre à la FPT ou à la FPH glissée dans une
  branche ANSM (FPE) sans vérification est le piège documenté dans le README
  du dépôt et dans `references/_gabarit-branche.md` §9.
- **Le bandeau de maturité ne doit jamais être surévalué.** Passer une
  branche de 🟢 ou 🟡 à ✅ dans le diff doit s'accompagner de l'ajout des
  sources primaires correspondantes dans la même branche ; sinon c'est un
  problème, pas un point fort.
- **Toute branche modifiée dans `references/` suit la structure imposée par
  `references/_gabarit-branche.md`**, dans l'ordre : bandeau de maturité,
  périmètre, questions couvertes, arbre de traitement, variables à lever,
  règles métier, déclencheurs de vérification, pièges et confusions,
  données volatiles, livrables, niveau de confiance, checklist.
- **Une correction de fond sur une branche doit mettre à jour ensemble** la
  branche, `references/sources-principales.md`, `CHANGELOG.md` et
  `JOURNAL.md` (règle de `CONTRIBUTING.md`). Un diff qui ne touche que l'un
  de ces fichiers pour une correction de fond mérite une question, pas un
  constat certain.

## À ne pas signaler

- Le style d'écriture des fiches métier.
- Les contrôles déjà mécaniques de la CI (`validate_skill.py`,
  `behavior_eval.py`, `internal_sources.py`, `freshness_report.py`,
  `check_source_urls.py`, les tests) : ils s'exécutent sur chaque PR.
