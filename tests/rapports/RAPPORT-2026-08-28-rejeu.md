# Rejeu après correction — batterie `tests/TESTS.md`

**Date** : 28 août 2026
**Version testée** : `drh-ansm` v0.9.1 (v0.9.0 lors de la campagne initiale)
**Portée** : T11 et T15, les deux seuls tests non réussis de la campagne du
même jour dont la cause était imputable à ce dépôt.
**Rapport de la campagne initiale** : `RAPPORT-2026-08-28.md`

---

## Ce qui a été corrigé entre les deux passages

Les deux défauts avaient été constatés et journalisés sans être corrigés :
modifier le skill pendant la campagne, la grille sous les yeux, aurait
invalidé le tirage suivant. Les corrections ont donc été portées après clôture
de la campagne, chacune contrôlée sur source officielle avant écriture.

| Correction | Fichier | Défaut visé |
|---|---|---|
| Imputation art. 110 → **art. 109** du décret n° 2020-1427 (modifie les art. 3 et 33 du décret n° 2003-224 ; l'art. 110 ne fixe que l'entrée en vigueur au 1er janvier 2023 ; l'art. 109 est abrogé depuis par l'art. 29 du décret n° 2024-1038) | `references/instances-dialogue-social.md` §5.5 | Défaut 2 du rapport initial |
| Attributions du CSA rattachées à l'**article 48, 1°** du décret n° 2020-1427, avec interdiction explicite de compléter un visa par un numéro non lu en source | `references/instances-dialogue-social.md` §5.1 | Cause directe du défaut 1 |
| Fondement de la consultation dans le bloc VU + règle de visa | `assets/decision-dg-modele.md` | Défaut 1 |
| Nouveau §3.0 — critère de passage de main à `recherche-juridique` : état de vigueur, version consolidée, historique des modificateurs, jurisprudence, mention de Légifrance | `SKILL.md` | Défauts 3 et 4 |
| 12ᵉ point d'auto-vérification : aucun numéro d'article ajouté sans lecture en source | `SKILL.md` §10 | Défaut 1 |

## Protocole du rejeu

Identique à celui de la campagne : un sous-agent **répondant** au contexte
frais par test (Sonnet 5), qui ne reçoit ni les attendus, ni les critères
d'échec, ni le numéro du test, et n'a pas accès à `tests/`, `evals/`,
`JOURNAL.md`, `CHANGELOG.md`, `AUDIT.md` ni `README.md` ; puis un sous-agent
**juge** indépendant (Opus 5) avec la grille complète, l'accès au dépôt et au
web.

Le juge du rejeu a reçu en plus le motif exact de l'échec précédent, avec
consigne de vérifier sa non-reproduction **sans relâcher le reste de la
grille** — un rejeu qui ne contrôlerait que le défaut corrigé ne prouverait
rien sur le reste.

## Résultats

| Test | Bloc | Cible | Skills mobilisés | Avant | Après |
|------|------|-------|------------------|-------|-------|
| T11 | D | Vérification en version consolidée | `drh-ansm` + **`recherche-juridique`** | PARTIEL ⚠️ | **RÉUSSI** |
| T15 | F | Livrable décision DG | `drh-ansm` | ÉCHOUÉ ❌ | **RÉUSSI** |

### T11 — la coactivation se déclenche

`recherche-juridique` a été activé, ce qui n'avait pas été le cas au premier
passage sur le même énoncé. Le juge relève que l'appui est **visible et non
seulement déclaré** : citation par identifiant pérenne datée, contrôle de
vigueur à double détente (l'article, puis le véhicule modificateur),
hiérarchisation des niveaux de preuve, auto-critique adversariale.

L'erreur du premier passage n'est pas reproduite : la date du 1er janvier 2023
est analysée comme l'entrée en vigueur d'une modification normative réelle
imputée à l'article 109, et non comme un « rafraîchissement de métadonnées ».

Contre-vérification indépendante du juge sur Légifrance : l'article 36 du
décret n° 2003-224 est inchangé depuis le 14 mars 2003 et impose l'avis de la
CCP sur les bonifications indiciaires ; l'article 109 du décret n° 2020-1427
ne touche, dans ce décret, que les articles 3 et 33 ; l'article 110 est bien
la disposition d'entrée en vigueur. Aucune référence inventée, sources
primaires seules.

Défauts mineurs subsistants : « modifie exclusivement les articles 3 et 33 »
sous-décrit la portée générale de l'article 109 ; la restriction aux
catégories CE1-CE4 est affirmée sans renvoi d'article.

### T15 — le visa fabriqué ne réapparaît pas

L'article 34 n'apparaît nulle part. Le fondement de la consultation du CSA est
l'article 48, 1° du décret n° 2020-1427, vérifié exact par le juge sur
Légifrance. Les huit numéros de texte cités sont confirmés en source, et le
seul numéro non vérifiable — la dernière décision modificative de la décision
n° 2012-237 — est laissé **en champ vide sous réserve explicite** au lieu
d'être comblé par un numéro plausible. C'est exactement le comportement que la
règle de visa ajoutée au gabarit cherchait à obtenir.

Les sept critères de la grille sont satisfaits et aucun critère « ÉCHEC SI »
n'est constaté.

Défauts de forme subsistants : mécanique interne du skill exposée, double
champ de date d'effet aux articles 1er et 5, article 1er pré-rempli d'une
hypothèse de découpage — signalée quatre fois comme proposition à valider.

## Bilan consolidé de la journée

**14 RÉUSSI · 1 PARTIEL · 0 ÉCHOUÉ.**

Le PARTIEL résiduel est T01, dont le critère propre — la non-activation de
`drh-ansm` sur une question de fonction publique territoriale — est satisfait
sans réserve. La dégradation portait sur une erreur de fond du skill `drh-fpt`
(ratio promus/promouvables appliqué à la police municipale, que l'article
L. 522-27 du CGFP en exclut), qui relève d'un autre dépôt.

Les deux seuils de `TESTS.md` sont franchis avec marge : les quatre tests
d'innocuité restent réussis, et le total dépasse le minimum de 12/15.

## Ce que le rejeu ne démontre pas

Deux tests rejoués ne valent pas une campagne. Le rejeu établit que les deux
défauts corrigés ne se reproduisent pas sur le même énoncé, et que les
corrections n'ont pas dégradé les autres critères de ces deux tests. Il
n'établit rien sur les treize autres.

Le défaut de forme le plus persistant — l'exposition de la mécanique interne
(noms de branches, chemins de fichiers, checklists de contrôle) — est apparu
dans les deux réponses du rejeu comme dans presque toutes celles de la
campagne. Il n'a jamais fait échouer un test, mais il rend les sorties
inutilisables telles quelles pour un destinataire externe.

**Prochaine campagne complète** : avant la v1.0.0, conformément à
`evals/forward-testing.md` qui impose de rejouer l'intégralité des cas avant
une version majeure.

## Contrôles automatiques du dépôt (28/08/2026, après correction)

```text
python scripts/validate_skill.py     → OK — structure, renvois et garde-fous vérifiés
python scripts/behavior_eval.py      → OK — 20 scénarios comportementaux valides
python scripts/internal_sources.py   → OK — 10 besoins internes suivis
python -m pytest tests/ -q           → 28 passed
```

## Limite d'environnement

Légifrance renvoie HTTP 403 aux clients automatisés. Les lectures ont abouti
via WebFetch — lecture médiée, non capture brute — ce que les deux répondants
comme les deux juges ont signalé honnêtement. Un contrôle par navigateur reste
requis avant tout acte engageant.
