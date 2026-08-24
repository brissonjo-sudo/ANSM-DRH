# Évaluations de régression

`behavior-cases.json` regroupe vingt cas à rejouer après toute
modification de fond. Chaque cas indique les branches, le contexte à
lever, la sensibilité, les critères sémantiques et les affirmations
critiques interdites. Le contrôle lexical est seulement une barrière :
une revue métier reste obligatoire.

`source-gates.json` suit les affirmations vérifiées et leur expiration.
`internal-source-requirements.json` suit uniquement les métadonnées des
documents internes attendus ; aucun contenu confidentiel ne doit entrer
dans le dépôt.

Le contrôle structurel se lance avec :

```text
python scripts/validate_skill.py
python scripts/behavior_eval.py
python scripts/internal_sources.py
```

Pour préparer la revue d'une réponse enregistrée dans `reponse.txt` :

```text
python scripts/behavior_eval.py --case recrutement-apres-industrie --response reponse.txt
```

Le déroulé complet, les règles d'échec et la traçabilité minimale sont
définis dans `evals/forward-testing.md`.
