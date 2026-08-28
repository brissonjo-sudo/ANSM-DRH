# Rejeu de réancrage — codification du 1er février 2025

**Date** : 28 août 2026
**Version testée** : `drh-ansm` v0.9.3
**Portée** : T06, T10, T15 — les trois tests qui mobilisent les branches
remaniées (instances, QVT) et l'acte.
**Rapports précédents** : `RAPPORT-2026-08-28.md`, `-rejeu.md`, `-forme.md`

---

## Le point de départ

La v0.9.2 avait corrigé un visa fondé sur le décret n° 2020-1427, abrogé
depuis le 1er février 2025 — mais uniquement là où il produisait un acte
fautif. Les dix autres mentions du dépôt restaient en place, consignées au
JOURNAL comme chantier avant la v1.0.0. Ce rejeu couvre leur reprise.

## Ce qui a été réancré

| Règle | Ancien véhicule | Fondement en vigueur |
|---|---|---|
| CSA d'établissement public, créé par arrêté des ministres de tutelle | décret n° 2020-1427 | **art. R. 251-20 CGFP** |
| Formation spécialisée SSCT obligatoire à 200 agents | décret n° 2020-1427 | **art. R. 251-28 CGFP** |
| Consultations obligatoires du CSA | décret n° 2020-1427, art. 48 | **art. R. 253-1 CGFP** |
| Institution et attributions de la CCP | décret n° 86-83, art. 1-2 | **art. R. 271-1 et s. CGFP** |
| CCP consultée au-delà de l'exclusion de 3 jours | décret n° 86-83, art. 1-2 | **art. R. 271-12 CGFP** |

Chaque correspondance a été vérifiée sur source officielle avant écriture,
puis contre-vérifiée par les juges du rejeu.

## Une seconde abrogation, trouvée par le même mécanisme

Le premier rejeu de T06 a fait apparaître que l'**article 1-2 du décret
n° 86-83** est lui aussi abrogé depuis le 1er février 2025 — par
l'**article 10 du décret n° 2024-1038**, quand le décret n° 2020-1427
l'était par son article 29. Même texte, même date, deux véhicules
différents.

**L'abrogation est ciblée, pas générale** : les autres articles du décret
n° 86-83, dont les articles 43-2 et 44 sur la procédure disciplinaire,
restent en vigueur. Le juge du second passage a explicitement contrôlé ce
point — une sur-correction qui aurait traité tout le décret comme abrogé
se serait trompée dans l'autre sens, et aurait coûté aussi cher.

**Ce que cet épisode a changé dans l'approche.** Deux abrogations issues
du même décret de codification, trouvées l'une après l'autre par des juges
différents, sur des branches différentes : ce n'est plus une erreur, c'est
un motif. `socle-sources-verification.md` porte désormais un avertissement
transverse — avant de viser un texte réglementaire antérieur à 2025 en
matière de dialogue social ou d'instances, contrôler qu'il n'a pas été
codifié. Les prochaines occurrences seront attrapées par le garde-fou, pas
par une campagne de test.

## Une correction de fond trouvée au passage

Le seuil de la formation spécialisée SSCT était énoncé comme celui
« au-delà duquel » l'obligation joue. L'article R. 251-28 vise un effectif
« **au moins égal à deux cents agents** » : l'obligation joue **dès** 200,
pas à 201. Sans conséquence pour l'ANSM, qui compte un millier d'agents —
mais une branche est écrite pour être citée, et un seuil décalé d'une
unité est une erreur, pas une approximation.

## Résultats

| Test | Cible | Fond | Forme |
|------|-------|------|-------|
| T06 | Périmètre de la CCP en discipline | **RÉUSSI** | résidus mineurs |
| T10 | Conditionnel borné sur le télétravail | **RÉUSSI** | résidus mineurs |
| T15 | Livrable décision DG | **RÉUSSI** | **CONFORME** |

**T15 décroche pour la première fois fond et forme.** Les cinq visas sont
vérifiés en vigueur au 15 septembre 2026 ; le décret abrogé n'apparaît
nulle part dans l'acte ; la réponse refuse d'attester le découpage en
quatre pôles alors que l'organigramme publié en documente trois, et le
signale.

**T06** a demandé deux passages : le premier a révélé l'abrogation, le
second a confirmé la correction — fondement rattaché à l'article R. 271-12,
article 44 du décret n° 86-83 correctement présenté comme non abrogé.

**T10** tient l'abstention chiffrée sans faille : aucun nombre de jours
cité, ni comme règle ANSM ni ailleurs.

## Ce qui reste ouvert

1. **Deux numéros d'article non lus en source.** La règle de composition
   de la CCP en matière disciplinaire est rappelée sans son numéro, avec
   la mention « à confirmer avant tout visa ». C'est l'application du
   douzième point d'auto-vérification à nous-mêmes : écrire un numéro
   plausible ici reproduirait exactement la faute qu'il interdit.
2. **Le reste du registre n'a pas été audité** pour la vague de
   codification. Deux textes ont été traités parce que deux tests les ont
   heurtés. Un balayage systématique des sources antérieures à 2025 reste
   à faire — le garde-fou du socle limite le risque, il ne le supprime
   pas.
3. **Résidus de forme** : quelques règles restent posées sans texte
   identifié (T06 : motivation et prescription, qui relèvent des articles
   43-1 et 43-2 ; T10 : le cadre FPE mobilisé sans citer le décret
   n° 2016-151), et le niveau de confiance est parfois distribué ligne à
   ligne sans être énoncé globalement.

## Contrôles automatiques du dépôt

```text
python scripts/validate_skill.py     → OK — structure, renvois et garde-fous vérifiés
python scripts/behavior_eval.py      → OK — 20 scénarios comportementaux valides
python scripts/internal_sources.py   → OK — 10 besoins internes suivis
python scripts/check_source_urls.py  → OK — 21 URL officielles (403 Légifrance tolérés)
python -m pytest tests/ -q           → 28 passed
```
