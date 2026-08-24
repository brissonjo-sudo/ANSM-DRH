# drh-ansm

Skill Claude pour l'expertise RH à l'Agence nationale de sécurité du
médicament et des produits de santé (ANSM).

## Origine

Construit sur l'architecture du skill `drh-fpt` (posture hybride, noyau
de vérification juridique, gabarit de branche, boucle d'apprentissage
JOURNAL/CHANGELOG). Le contenu métier est propre à l'ANSM : établissement
public de l'État, personnel majoritairement contractuel (classification
interne CE1-CE4), régime déontologique renforcé (prévention des
conflits d'intérêts avec l'industrie pharmaceutique), instances de la
fonction publique de l'État (CSA, CAP, CCP).

## État

**v0.6.1 — les huit branches sont traitées ; les niveaux de confiance
sont réalignés sur la traçabilité effective des sources (voir `AUDIT.md`).**

| Branche | Maturité |
|---------|----------|
| Déontologie, DPI & conflits d'intérêts | 🟢 partielle (droit vérifié ; documents internes 2026 à obtenir) |
| Recrutement, classification & rémunération (CE1-CE4) | ✅ fiabilisée |
| Instances & dialogue social | ✅ fiabilisée — 🔴 échéance électorale |
| Fonctionnaires & corps spécifiques | ✅ fiabilisée |
| Masse salariale, budget & SI RH | 🟢 partielle (dotation 2026 vérifiée ; détail budgétaire à confirmer) |
| QVT, santé au travail & RPS | 🟢 partielle |
| Formation & développement des compétences | 🟢 partielle |
| Communication interne | 🟡 amorcée |

**Échelle** : ✅ adossée à des sources primaires, utilisable en mode
assertif · 🟢 mécanisme établi, valeurs ou dispositif interne manquants ·
🟡 repères structurels seulement.

## 🔴 À traiter en priorité

Les **élections professionnelles** se tiennent le **10 décembre 2026**
(arrêté du 2 juillet 2025). Le calendrier local, la modalité de vote et
la décision ANSM relative aux formations spécialisées doivent être
vérifiés sans délai à partir des textes FPE en vigueur ; aucun délai FPT
ne doit être transposé. Voir l'encadré en tête de
`references/instances-dialogue-social.md`.

## Réserve transversale

Le décret statutaire fixe l'**architecture** mais renvoie toutes les
**valeurs** (indices, durées d'échelon, emplois-repères, quotas) à des
**délibérations du conseil d'administration non publiées**. Aucune
réponse chiffrée n'est possible sans ce document.

## Structure


```
drh-ansm/
├── SKILL.md                    — routeur et méthodologie
├── CONTRIBUTING.md             — règles de contribution
├── LICENSE / LICENSE-CODE      — licences du contenu et des scripts
├── AUDIT.md, CHANGELOG.md, JOURNAL.md
├── scripts/validate_skill.py   — contrôle de structure
├── evals/                      — cas de régression métier
├── references/
│   ├── _gabarit-branche.md
│   ├── socle-sources-verification.md
│   ├── sources-principales.md  — textes et liens officiels
│   └── [8 branches métier]
├── assets/                     — modèles d'actes et de profils
└── .github/workflows/validate.yml
```

## Prochaine étape

**Trois documents à obtenir en interne** débloquent l'essentiel de ce
qui manque :

1. La **délibération du conseil d'administration portant cadre
   d'emploi** — grilles indiciaires, durées d'échelon, emplois-repères,
   quotas. Débloque toutes les réponses chiffrées.
2. Le **règlement intérieur** de l'agence (articles 11 à 14) — fonde la
   déontologie et le régime disciplinaire.
3. Les **documents budgétaires de l'année** — plafond d'emplois voté,
   dotation de l'Assurance maladie et délibérations du CA.

## Méthode — trois leçons des fiabilisations successives

1. Remonter au **PDF daté le plus récent** publié par l'agence plutôt
   qu'aux pages HTML ou aux documents archivés, qui accusent souvent
   plusieurs années de retard.
2. Sur un établissement à statut propre, chercher **où le texte
   délègue** : un décret d'agence pose rarement les valeurs lui-même, il
   renvoie à l'organe délibérant.
3. Avant de lancer une fiabilisation, se demander **où vit
   l'information**. Si elle ne vit ni dans un texte publié ni dans un
   document institutionnel, mieux vaut formuler les bonnes questions à
   poser en interne que produire du contenu générique.

## Vérifier avant publication

Exécuter `python scripts/validate_skill.py`. Le contrôle vérifie le
frontmatter, les renvois locaux, les sommaires des branches longues et
les garde-fous juridiques introduits en v0.6. Les cas métier à rejouer
sont dans `evals/cases.yaml`.

## Licence

Le contenu est sous [CC BY 4.0](LICENSE) ; les scripts sont sous licence
[MIT](LICENSE-CODE).
