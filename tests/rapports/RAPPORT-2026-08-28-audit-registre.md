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

---

## Suite donnée — T13 rejoué jusqu'à l'emploi effectif des sources (1er septembre 2026)

Le rapport concluait que « lever une réserve ne suffit pas à faire utiliser la
source ». Il a fallu **trois tentatives** pour comprendre pourquoi, et la
troisième seule a fonctionné.

| Passage | Correction tentée | Résultat |
|---|---|---|
| 2ᵉ | — (état v0.9.4) | Sources absentes |
| 3ᵉ | En-tête de la branche réécrit, sources en vigueur en tête | **Sources absentes** — le répondant travaille depuis le corps, pas depuis l'en-tête |
| 4ᵉ | Sources nommées dans le passage opératoire | **Citées sans emploi** — rien à en tirer |
| 5ᵉ | **Charte réellement dépouillée**, son contenu versé au corps | **Sources mobilisées** |

**Le diagnostic manquait aux deux premières tentatives.** Une source qu'on
n'a pas lue ne peut être que nommée : pointer plus fort ne remplace pas le
dépouillement. Les deux premières corrections déplaçaient une étiquette ; la
troisième a apporté de la matière.

Ce que le juge du 5ᵉ passage constate : périmètre des emplois publiés restitué
presque mot pour mot depuis la charte, exclusion des liens de parenté érigée en
contrôle avant transmission, site DPI santé exploité jusqu'à la répartition des
responsabilités avec l'opérateur national, actualisation annuelle transformée
en règle d'information répétée.

**Une lacune trouvée en chemin, et qui comptait.** La branche était muette sur
la **durée de publication**. Un répondant a comblé le vide à contresens, en
affirmant qu'une fiche encore en ligne après la sortie du périmètre n'avait
plus de base légale. L'**article R. 1451-3 du code de la santé publique**
prévoit la publication pendant la durée des fonctions **et les cinq années
suivant leur fin**. La règle est désormais écrite avec ses deux erreurs
symétriques — retirer trop tôt, publier sans limite — et le 5ᵉ passage
l'énonce exactement.

**Nuance sur le dispositif de février 2026** : la branche portait déjà son
contenu (arrêtés de 2017, amende de 30 000 €, déclaration de moins d'un an,
mécanique de séance) mais ne l'attribuait à rien. Le manque était
d'**attribution**, pas d'extraction. Corrigé.

## Lacune structurelle relevée par un répondant

Le référentiel **ne comporte aucune branche ni aucune source RGPD ou CNIL**.
Sur une question de protection des données, le répondant doit chercher
au-dehors — ce qu'il a fait, en signalant correctement sa trouvaille comme
repère doctrinal antérieur au RGPD. C'est cohérent avec le périmètre du skill,
qui renvoie ces questions au DPO de l'agence, mais cela signifie que le **bloc E
de la batterie repose entièrement sur ce que le répondant va chercher
ailleurs**. À trancher : documenter un socle RGPD minimal, ou assumer le renvoi
et l'écrire.

## Suite du 1er septembre 2026 — la lacune RGPD refermée par coactivation

La question laissée ouverte ci-dessus (« documenter un socle RGPD minimal, ou
assumer le renvoi et l'écrire ») est tranchée dans le **second sens**, mais
d'une manière que la formulation d'origine n'envisageait pas : ni socle
maison, ni renvoi muet vers le DPO. Le dépôt de l'utilisateur porte déjà un
skill `dpo-ct` dont dix des onze références sont de la méthode RGPD générique
— AIPD, violations, droits des personnes, sécurité, sous-traitance, relations
CNIL, registre. Une seule, `secteur-collectivites.md`, est propre au versant
territorial. Dupliquer cette méthode ici aurait créé une seconde source de
vérité à maintenir ; la bonne réponse était de **désigner la frontière**.

C'est l'objet du §3.0 bis de `SKILL.md` (v0.9.9) : le référentiel ne documente
aucun régime RGPD, il nomme les cas qui appellent `dpo-ct` et pose ce qui ne
doit pas franchir la frontière — écarter `secteur-collectivites.md` et toute
règle présupposant une délibération d'un conseil municipal, un DPO mutualisé
ou un centre de gestion. À l'ANSM, le responsable de traitement est l'agence
et le DPO est celui de l'agence.

### Rejeu T14 — la coactivation se déclenche

T14 (« vote électronique de décembre 2026 : que doit prévoir la DRH côté
protection des données ? ») rejoué sur répondant neuf, jugé par un agent
distinct avec accès web. Le répondant lit `SKILL.md`, y trouve le renvoi, va
chercher la méthode chez `dpo-ct` — AIPD, sous-traitance, sécurité, droits des
personnes — et rend une réponse dont le calendrier est le fil directeur
(décompte à trois mois, expertise préalable à boucler en novembre pour une
fenêtre de vote du 3 au 10 décembre). Verdict **RÉUSSI**.

Le contrôle des références est le résultat le plus important : **onze
références vérifiées une à une sur le web, aucune inventée** — arrêté du
2 juillet 2025 (NOR APFF2513659A), décrets n° 2024-1038 et n° 2025-1430,
articles R. 211-503 à R. 211-584 du CGFP dont R. 211-518 à R. 211-521 pour
l'expertise indépendante, délibérations CNIL n° 2019-053 du 25 avril 2019 et
n° 2026-045 du 19 mars 2026, y compris le régime transitoire qui laisse la
recommandation de 2019 régir les scrutins déjà engagés en 2026. Un seul point
reste non vérifiable : l'attribution au portail national des élections d'une
exigence de certification de sécurité — le fond est exact par ailleurs, c'est
la source qui est mal identifiée. **Aucune fuite territoriale** : zéro
occurrence de conseil municipal, DPO mutualisé, centre de gestion ou CNFPT.

### Ce que le rejeu apprend sur le contrat de sortie

Trois défauts de forme relevés, et deux d'entre eux ne sont **pas** des fautes
du répondant :

1. « Cette durée n'est pas fixée par **le référentiel utilisé pour préparer
   cette réponse** » — celui-là est bien une fuite. Le §7 interdisait « le
   skill », « mon référentiel », « ma base » : une liste de trois formules,
   que le répondant a contournée sans le vouloir en en écrivant une
   quatrième. Une interdiction énumérée se contourne ; une interdiction de
   classe, non. Le §7 vise désormais **toute mention du dispositif, sous
   quelque formulation que ce soit**, et indique la rédaction de
   remplacement : dire ce qui reste à obtenir et auprès de qui (§8.4), non
   ce que le dispositif ne contient pas.
2. Le tableau **Stable / À vérifier / Hypothèse** a été relevé comme
   « taxonomie de maturité exposée ». Il est en réalité **prescrit** par le
   §3 du contrat de sortie. Le mot « maturité » désignait deux choses à la
   fois : l'état d'une branche du référentiel, qui est de la tuyauterie, et
   le niveau de certitude d'un élément, qui est dû au destinataire. Un juge
   les a confondues ; un répondant l'aurait fait aussi, et aurait supprimé
   le tableau — exactement la sur-correction qui avait dégradé T09 en
   v0.9.2. Les deux sont désormais nommées séparément.
3. « Date de référence : **vérification effectuée le** 1er septembre 2026 » —
   le champ est légitime, le compte rendu de procédure ne l'est pas. Le §2
   demande maintenant une date donnée **comme une date**.

Le juge relève enfin une lacune de fond sans effet sur le verdict :
l'article 28 du RGPD est déroulé dans son contenu mais **jamais cité par son
numéro**. Le §8.1 n'évoquait que des textes français — décret, arrêté. Il
précise désormais qu'un **article de règlement européen** se cite comme les
autres.

## Ce qui reste ouvert après cette suite

1. ~~Le **contenu des rapports du déontologue 2024 et 2025** n'est pas
   dépouillé~~ — **fait le 2 septembre 2026** (v0.9.11). Les deux millésimes
   sont lus ; la branche porte désormais une section de volumétrie sur trois
   exercices, et deux points laissés en suspens par la campagne sont tranchés
   (double dénomination du service, statut du comité de déontologie).
2. Les **fiches de probité** de février 2026 et les **articles 11 à 14 du
   règlement intérieur** restent à obtenir.
3. Le **registre des traitements (article 30)** et la **procédure de violation
   de données** pendant la fenêtre de vote sont nommés par le §3.0 bis mais
   n'ont pas été mobilisés par le répondant de T14. À surveiller au prochain
   rejeu : le renvoi porte-t-il sur toute la liste, ou seulement sur les cas
   que la question rend évidents ?
