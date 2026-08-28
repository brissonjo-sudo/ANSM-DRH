# Audit de vigueur du registre des sources

**Date** : 28 août 2026
**Version** : `drh-ansm` v0.9.4
**Portée** : les 21 entrées de `references/sources-principales.md`, contrôlées
une à une sur source officielle.
**Rejeu de vérification** : T10 (télétravail) et T13 (DPI × RGPD).

---

## Pourquoi cet audit

Deux abrogations avaient été trouvées coup sur coup par des juges de test,
sur deux branches différentes, toutes deux imputables au même décret de
codification. Deux occurrences du même motif justifiaient de vérifier
l'ensemble plutôt que d'attendre la troisième.

Méthode : trois auditeurs indépendants, un par section du registre, avec
consigne de ne rien modifier, de n'écrire « en vigueur » qu'après avoir vu la
page du texte, et de distinguer ce qu'ils avaient vérifié de ce qu'ils
supposaient. Chaque anomalie signalée a été **revérifiée** avant d'être portée
au dépôt.

## Le constat principal — un programme, pas des accidents

La partie réglementaire du code général de la fonction publique se construit
**livre par livre**. Chaque livre abroge les décrets thématiques dont il
reprend les dispositions.

| Livre | Matière | Décret codificateur | Entrée en vigueur |
|---|---|---|---|
| I et II | Droits et obligations ; dialogue social | n° 2024-1038 du 6 novembre 2024 | 1er février 2025 |
| III | Recrutement | n° 2025-695 du 24 juillet 2025 | 1er octobre 2025 |
| IV | Organisation et gestion RH — formation professionnelle, télétravail | n° 2026-366 du 7 mai 2026 | **1er août 2026** |
| V | Carrière | annoncé | à surveiller |

Le référentiel était ancré sur les véhicules d'avant. La dernière vague a
**27 jours** à la date de l'audit.

Trois règles en découlent, désormais écrites dans le socle :

1. l'abrogation est **ciblée article par article** — le décret n° 86-83 est
   amputé, pas abrogé ;
2. un article **survivant peut avoir été réécrit** par le décret
   codificateur : citer la version, pas seulement le numéro ;
3. tout texte réglementaire antérieur à 2026 s'ouvre en version consolidée
   avant d'être visé.

La deuxième règle est celle qui manquait : elle explique pourquoi vérifier
qu'un article dit bien ce qu'on lui fait dire ne suffit pas.

## Corrections portées

### Vigueur

| Source | Problème | Correction |
|---|---|---|
| `CONTRACTUELS-ETAT` | Décret n° 86-83 amputé en deux vagues (art. 1-2 et voisins au 1/2/2025 ; bloc « recrutement » au 1/10/2025) | Mention des deux vagues et consigne de contrôle article par article |
| Branche QVT | Décret n° 2016-151 (télétravail) abrogé au 1/8/2026 | Rattachement aux art. R. 431-1 et s. du CGFP |
| Branche formation | Livre IV codifie toute la matière | Avertissement de réancrage — **chantier non fait** |
| `ELECTION-REGLES-2025` | « Applicable depuis janvier 2026 » : faux | Chapitre Ier en vue du renouvellement de décembre 2026, chapitre II depuis le 31/12/2025 |
| `CSA-ETAT`, `CCP-ETAT` | Chaînes de modification absentes | R. 253-1 modifié par le décret n° 2026-366, R. 271-1 par le décret n° 2025-695 |
| `ANSM-PERSONNELS` | L. 5323-1 CSP renvoie à des titres abrogés au 1/3/2022 | Lecture par équivalence signalée |
| `ANSM-STATUT` | Décret purement modificatif | Renvoi au code de la santé publique pour une règle citable |

### Le numéro que la v0.9.3 avait refusé d'écrire

La composition de la CCP en matière disciplinaire avait été laissée **sans
numéro d'article**, faute d'avoir pu le lire en source. Il a été trouvé — et
il n'était pas là où on le cherchait : la règle n'est **pas** dans le code,
elle est restée à l'**article 44 du décret n° 86-83**, réécrit au 1er février
2025, qui renvoie lui-même à l'article R. 271-1 du CGFP.

Le régime est **hybride** : institution et attributions au code, composition
disciplinaire au décret. Chercher dans le seul code ne pouvait pas aboutir —
et le refus d'écrire un numéro plausible a évité d'inscrire une erreur.

### Une réserve levée à l'envers

Le dépôt affirmait qu'aucune URL officielle n'avait été retrouvée pour la
**charte de déontologie de février 2026** et le **dispositif de prévention et
de gestion des conflits d'intérêts**. Les deux sont publics. URL vérifiées,
texte des couvertures extrait pour confirmer les millésimes (« Charte de
déontologie — Février 2026 » ; « Septembre 2018 — Mise à jour février 2026 »).
Ils entrent au registre.

Le rapport du déontologue cité datait de **2023** alors que ceux de 2024 et
2025 sont publiés.

### Déontologie — textes en vigueur

Aucun des quatre textes juridiques de la section déontologie n'est abrogé.
Deux compléments : l'**art. L. 124-8** du CGFP (saisine HATVP des dirigeants
d'établissement public nommés en conseil des ministres, cas potentiel de la
direction générale), et la **loi n° 2025-1249 du 22 décembre 2025** comme
dernière modification de l'art. 432-12 du code pénal.

## Rejeu de vérification

| Test | Cible | Fond | Forme |
|------|-------|------|-------|
| T10 | Télétravail — innocuité | **RÉUSSI** | résidus mineurs |
| T13 | DPI × RGPD — coactivation | **RÉUSSI** | résidus mineurs |

**T10** : le juge confirme que le décret n° 2016-151 est traité comme abrogé,
rattaché au livre IV, sans qu'aucun numéro d'article plausible soit avancé
sans vérification — la réserve du dépôt sur le numéro précis a été reprise
telle quelle par le répondant. Aucun quota attribué à l'ANSM.

**T13** : le critère discriminant — l'exclusion des liens de parenté de la
publication — est traité trois fois. Aucune transposition du droit des
collectivités, aucune référence inventée.

## Ce que l'audit n'a pas réglé

1. **Le réancrage de la branche formation** sur le livre IV. Signalé, non
   fait : c'est un travail de fond sur une matière entièrement recodifiée.
2. **Les nouvelles sources ANSM ne sont pas encore exploitées.** T13 ne cite
   ni la charte de février 2026, ni le dispositif, ni le rapport 2025 — le
   dépôt les déclare citables, mais le corps de la branche déontologie n'y
   renvoie pas encore. Lever une réserve ne suffit pas à faire utiliser la
   source.
3. **Trois points laissés non aboutis par les auditeurs**, consignés plutôt
   que comblés : la liste exhaustive des articles du décret n° 86-83 touchés
   par chaque vague, le corps des articles 72-73 du décret n° 2025-695, et la
   décision du Conseil constitutionnel sur la LFSS 2026.
4. **Le livre V est annoncé.** Le prochain audit ne sera pas le dernier — et
   c'est le garde-fou du socle, pas une campagne, qui doit l'attraper.

## Contrôles automatiques du dépôt

```text
python scripts/validate_skill.py     → OK — structure, renvois et garde-fous vérifiés
python scripts/behavior_eval.py      → OK — 20 scénarios comportementaux valides
python scripts/internal_sources.py   → OK — 10 besoins internes suivis
python scripts/check_source_urls.py  → OK — 25 URL officielles (403 Légifrance tolérés)
python -m pytest tests/ -q           → 28 passed
```
