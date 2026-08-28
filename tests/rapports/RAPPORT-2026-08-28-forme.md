# Rejeu de forme — séparation de la réponse et de la tuyauterie

**Date** : 28 août 2026
**Version testée** : `drh-ansm` v0.9.2
**Portée** : T05, T09, T15 — trois tests déjà réussis sur le fond, choisis
parce que les juges y avaient relevé les résidus de mécanique interne les plus
lourds, et parce qu'ils couvrent trois formats de sortie différents
(abstention, note de cadrage, acte).
**Rapports précédents** : `RAPPORT-2026-08-28.md`, `RAPPORT-2026-08-28-rejeu.md`

---

## Le défaut visé

Les juges de la campagne et de son premier rejeu avaient relevé le même défaut
de forme dans presque toutes les réponses : chemins de fichiers, noms de
branches, bandeaux de maturité (✅ 🟢 🟡), codes du registre de sources,
mentions du « skill » et check-list de contrôles apparaissaient dans le texte
remis. Aucun test n'en avait échoué — mais aucune réponse n'était transférable
telle quelle à un agent de la DRH qui ignore le dispositif.

**La cause n'était pas dans le comportement du modèle, elle était dans
l'instruction.** Le contrat de sortie demandait lui-même, en §2, la « branche
principale et les éventuels renvois inter-branches » ; en §5, de « pointer vers
le gabarit approprié dans `assets/` » ; et sa check-list §6 ne se disait nulle
part interne. Le modèle appliquait ce qu'on lui demandait.

## Ce qui a été corrigé, et en deux temps

### Temps 1 — la règle de séparation

`references/contrat-sortie.md` : règle de séparation en tête, §2 reformulé en
langage métier, §5 qui produit le livrable sans citer son chemin, check-list §6
explicitement interne, §7 énumérant ce qui ne figure jamais dans une réponse.
`SKILL.md` : le niveau de confiance se dit en français (§4), la maturité pilote
sans s'afficher (§7), 13ᵉ point d'auto-vérification (§10).

### Temps 2 — le rééquilibrage, imposé par le rejeu

Le rejeu de T09 a fait apparaître une **sur-correction** : forme conforme, mais
fond retombé en PARTIEL. Le répondant avait retiré, avec la tuyauterie,
**presque toutes les sources officielles nommées** (arrêté du 2 juillet 2025,
décrets n° 2020-1427, 2024-1038, 2025-1430, 2003-224) et les valeurs vérifiées
(5,51 M€, 143,69 M€, résultat du vote au CSA, seuil de 200 agents, part de
contractuels).

L'enseignement est net : **une interdiction en liste face à une obligation en
prose ne fait pas jeu égal.** Le §7 énumérait douze interdits en puces ; le
maintien des sources tenait en une phrase de paragraphe. Le modèle a suivi la
liste.

D'où un **§8 de même rang que le §7** — obligation de citer chaque texte par
son intitulé, son numéro et sa date, et de conserver les valeurs vérifiées,
seul l'identifiant *interne* du registre restant masqué — et un §9 dont le test
de relecture compte deux moitiés : ni référence qui ne parle pas au lecteur, ni
fondement qu'il doive redemander.

La ligne de partage tient en une phrase, désormais écrite dans le contrat :
**masquer ce qui décrit comment la réponse a été fabriquée, conserver ce qui
permet de la contrôler.** Un chemin de fichier ne se vérifie pas ; un numéro de
décret, si.

## Résultats

| Test | Fond avant | Fond après | Sources | Forme |
|------|-----------|-----------|---------|-------|
| T05 — abstention chiffrée | RÉUSSI | **RÉUSSI** | — | **CONFORME** |
| T09 — réflexe calendaire | RÉUSSI | **RÉUSSI** | **SUFFISANTES** | RÉSIDUS MINEURS |
| T15 — livrable décision DG | RÉUSSI | **RÉUSSI** | — | RÉSIDUS MINEURS |

Les juges notaient **fond et forme séparément**, avec consigne explicite :
une réponse qui aurait perdu en rigueur de fond pour gagner en forme est un
échec. C'est cette consigne qui a fait apparaître la sur-correction ; sans
elle, T09 aurait été enregistré comme un succès de forme.

**T05** — zéro occurrence interdite ; la section « Contrôles avant remise » a
disparu ; confiance, pièce à obtenir et source citée par intitulé et date
restent visibles. Le fond y gagne même deux points par rapport au premier
passage.

**T09** — élections du 10 décembre 2026 au rang 1 à quatre points d'entrée ;
sources et chiffres revenus (arrêté du 2 juillet 2025, décrets n° 2024-1038,
2025-1430, 2003-224, 92-1432, 2025-697, 2012-597, 143,69 M€, 957 ETPT, vote du
CSA, seuil de 200 agents), tous recoupés exacts, **sans réapparition de la
tuyauterie**. Le rééquilibrage fonctionne.

**T15** — voir ci-dessous : ce rejeu a produit une découverte de fond qui
dépasse le cadre de la forme.

## Découverte de fond en cours de rejeu — un visa reposant sur un texte abrogé

Le juge du deuxième passage de T15, en contrôlant les visas un par un, a établi
que le **décret n° 2020-1427 du 20 novembre 2020 est abrogé depuis le
1er février 2025** par l'**article 29 du décret n° 2024-1038 du 6 novembre
2024**, qui a codifié ses dispositions dans la **partie réglementaire du code
général de la fonction publique**.

Or c'est ce décret que la v0.9.1 avait inscrit comme fondement de la
consultation du CSA — correction elle-même issue de la campagne. Le fondement
en vigueur est l'**article R. 253-1, 1° du CGFP** : « des projets de texte
législatif ou réglementaire relatifs au fonctionnement et à l'organisation des
services ».

Vérifications refaites indépendamment sur source officielle avant écriture :
abrogation au 1er février 2025, codification par le décret n° 2024-1038, texte
du 1° de l'article R. 253-1. Le juge du troisième passage a confirmé l'article
en vigueur au 15 septembre 2026 (version issue du décret n° 2026-366 du 7 mai
2026, 1° inchangé).

**Ce que cet épisode enseigne** : la correction de la v0.9.1 avait remplacé un
numéro d'article faux par un numéro d'article exact — mais dans un véhicule
abrogé. Vérifier qu'un article existe et dit bien ce qu'on lui fait dire ne
suffit pas : il faut vérifier que **le texte qui le porte est toujours en
vigueur à la date de l'acte**. C'est précisément le contrôle de vigueur que le
skill compagnon `recherche-juridique` apporte, et que le noyau autonome
n'atteint pas.

`instances-dialogue-social.md` §5.1 et `assets/decision-dg-modele.md` sont
corrigés, avec un avertissement sur le véhicule.

## Ce qui reste ouvert

1. **Réancrage complet de la branche instances.** Les autres mentions du décret
   n° 2020-1427 dans `instances-dialogue-social.md` décrivent l'état du droit
   et doivent être relues une à une pour être rattachées au CGFP. Le point le
   plus exposé — le visa d'un acte — est traité ; le reste ne l'est pas. À
   faire avant la v1.0.0.
2. **Résidus de forme mineurs.** T09 fait encore remonter en surface une liste
   de cases à cocher de contrôle sous un intitulé propre ; T15 cite deux
   décrets sans leur intitulé. Le §7 a été précisé sur le premier point —
   **cette dernière précision n'a pas été rejouée** et reste à vérifier au
   prochain passage.
3. **Réserves de sources sur T09** : la LFSS 2026 est citée sans son numéro ni
   sa date, 5,51 M€ est arrondi, la part de contractuels est passée en
   qualitatif. Le §8 vise ce comportement, mais ne l'a pas entièrement corrigé.

## Contrôles automatiques du dépôt

```text
python scripts/validate_skill.py     → OK — structure, renvois et garde-fous vérifiés
python scripts/behavior_eval.py      → OK — 20 scénarios comportementaux valides
python scripts/internal_sources.py   → OK — 10 besoins internes suivis
python -m pytest tests/ -q           → 28 passed
```
