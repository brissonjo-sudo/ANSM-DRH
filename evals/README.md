# Évaluations de régression

`cases.yaml` regroupe les cas à rejouer après toute modification de fond.
Pour chaque cas, vérifier que la réponse contient les éléments attendus,
n'emploie aucun élément interdit et distingue toujours source primaire,
source interne et hypothèse. Les cas juridiques doivent être rejoués avec
la méthode `recherche-juridique` et des sources consultées à la date du
test.

Le contrôle structurel se lance avec :

```text
python scripts/validate_skill.py
```
