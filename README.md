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

**v0.5.1 — les huit branches sont traitées, audit interne passé (voir `AUDIT.md`).**

| Branche | Maturité |
|---------|----------|
| Déontologie, DPI & conflits d'intérêts | ✅ fiabilisée |
| Recrutement, classification & rémunération (CE1-CE4) | ✅ fiabilisée |
| Instances & dialogue social | ✅ fiabilisée — 🔴 échéance électorale |
| Fonctionnaires & corps spécifiques | ✅ fiabilisée |
| Masse salariale, budget & SI RH | ✅ fiabilisée (budget 2026 confirmé) |
| QVT, santé au travail & RPS | 🟢 partielle |
| Formation & développement des compétences | 🟢 partielle |
| Communication interne | 🟡 amorcée |

**Échelle** : ✅ adossée à des sources primaires, utilisable en mode
assertif · 🟢 mécanisme établi, valeurs ou dispositif interne manquants ·
🟡 repères structurels seulement.

## 🔴 À traiter en priorité

Les **élections professionnelles** se tiennent le **10 décembre 2026**
(arrêté du 2 juillet 2025). Vote électronique obligatoire en fonction
publique de l'État, effectifs de référence arrêtés au 1er janvier 2026,
et échéance de juin 2026 sur les formations spécialisées
vraisemblablement dépassée. Voir l'encadré en tête de
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
├── CHANGELOG.md                — historique des versions
├── JOURNAL.md                  — cas rencontrés, à journaliser
├── references/
│   ├── _gabarit-branche.md             — méta-gabarit de branche
│   ├── socle-sources-verification.md   — carte des sources ANSM
│   └── [8 branches métier]
└── assets/
    ├── decision-dg-modele.md   — acte ANSM type (décision DG)
    ├── note-modele.md
    ├── courrier-modele.md
    └── fiche-profil-poste.md
```

## Prochaine étape

**Trois documents à obtenir en interne** débloquent l'essentiel de ce
qui manque :

1. La **délibération du conseil d'administration portant cadre
   d'emploi** — grilles indiciaires, durées d'échelon, emplois-repères,
   quotas. Débloque toutes les réponses chiffrées.
2. Le **règlement intérieur** de l'agence (articles 11 à 14) — fonde la
   déontologie et le régime disciplinaire.
3. Les **documents budgétaires de l'année** — plafond d'emplois voté et
   subvention pour charges de service public.

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
