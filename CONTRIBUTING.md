# Contribuer

1. Pour toute règle juridique, partir d'une source primaire en vigueur et
   enregistrer son lien dans `references/sources-principales.md`.
2. Distinguer les documents internes ANSM des textes publiés ; ne jamais
   inventer une valeur, un délai ou une procédure locale.
3. Mettre à jour la branche, le registre des sources, `CHANGELOG.md` et
   `JOURNAL.md` ensemble lorsqu'une correction de fond est apportée.
4. Ajouter ou ajuster un cas dans `evals/behavior-cases.json` si la modification
   corrige une erreur susceptible de revenir.
5. Ne jamais déposer de document RH interne : renseigner uniquement ses
   métadonnées dans `evals/internal-source-requirements.json`.
6. Exécuter `python scripts/validate_skill.py` et les tests avant de proposer une
   modification.

Les demandes qui portent sur un cas d'agent doivent rester anonymisées ;
utiliser `scripts/privacy_scan.py` comme filet de sécurité local.
