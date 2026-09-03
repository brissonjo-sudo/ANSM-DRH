# Journal des cas — drh-ansm

> À chaque échange significatif, repérer puis proposer de consigner une
> lacune, une erreur, un cas nouveau ou un livrable récurrent. Aucune
> donnée nominative d'agent ; décrire les cas de façon anonymisée.
>
> Dans un environnement avec accès fichiers (Claude Code, dépôt), écrire
> l'entrée directement ici. Sinon, générer un bloc prêt à coller.

Format d'entrée suggéré :

```
## [date] — [branche concernée]
**Cas** : [description anonymisée de la situation]
**Ce qui a manqué / ce qui était incertain** : [écart constaté]
**Source qui a permis de trancher** (le cas échéant) : [référence]
**Action** : [mise à jour de branche proposée / faite]
```

---

## 2026-09-03 — formation & développement des compétences
**Cas** : chantier laissé ouvert par l'audit du registre — le livre IV du
CGFP parle d'« agent public » sans que la branche sache si cela couvre les
**agents contractuels de droit public**, alors que le personnel de
l'ANSM l'est majoritairement.
**Ce qui a manqué / ce qui était incertain** : la branche traitait la
question comme non documentée, faute de déclinaison ANSM. Elle ne l'était
pas pour autant indécidable : la réponse est dans le **chapitre liminaire**
du code lui-même (art. L1, L2, L7), jamais consulté jusqu'ici.
**Source qui a permis de trancher** : art. L1 (le code est le statut des
fonctionnaires), art. L2 (extension aux contractuels « quand il le
prévoit », donc conditionnelle), art. L7 (« agent public » désigne le
fonctionnaire ET l'agent contractuel) — chapitre liminaire du CGFP,
lu à la source. Vérifié ensuite que L. 421-1 et L. 422-8 emploient bien
« agent public », jamais « fonctionnaire ».
**Action** : nouveau §5.4 bis dans `formation-developpement-competences.md` ;
nouvelle source `CGFP-CHAMP` au registre ; affirmation ajoutée à la
barrière de fiabilisation.
**Leçon** : une extension de champ d'application « quand le code le
prévoit » n'est pas une clause qu'on cherche article par article dans
chaque disposition — elle se lit dans le **choix du mot** que la
disposition emploie, combiné à la définition que le code donne une fois
pour toutes de ce mot. Chercher la clause d'extension au mauvais endroit
(dans l'article métier) plutôt qu'au bon (le chapitre liminaire) aurait
laissé la question ouverte indéfiniment.

## 2026-09-02 — déontologie, DPI & conflits d'intérêts
**Cas** : dépouillement des rapports publics du déontologue **2025**
(31 mars 2026) et **2024** (31 mars 2025), dernier millésime restant après
la charte et le dispositif de février 2026.
**Ce qui a manqué / ce qui était incertain** : la branche décrivait
correctement les *règles* mais ignorait entièrement leur *application*.
Trois trous s'en trouvent comblés, et deux d'entre eux changent la réponse
qu'on donne à un agent :
1. **Aucun avis d'incompatibilité sur trois exercices** (20 départs en
   2023, 23 en 2024, 17 en 2025) : dire à un agent qu'il « risque un
   refus » est démenti par les faits. Ce qui l'attend, c'est une réserve
   opposable, pas un veto.
2. **65 % des candidats au recrutement reçoivent des réserves** (53 % en
   2024, 49 % en 2023) : la clause de réserves relève de la trame de
   promesse d'embauche, non du cas particulier.
3. **L'entretien annuel d'évaluation est le support déclaratif de droit
   commun** : depuis le 2 décembre 2020, seuls les agents dont la DPI est
   publiée télédéclarent sur DPI Santé ; pour tous les autres, la revue
   des liens se fait à l'entretien et se consigne dans son compte rendu.
   Un compte rendu muet laisse un trou dans le dispositif, y compris pour
   un agent sans aucun lien.
**Source qui a permis de trancher** : `ANSM-DEONTO-2025` et
`ANSM-DEONTO-2024`, lus intégralement (20 et 17 pages).
**Action** : §5.11 nouvelle — tableau de volumétrie sur trois exercices,
avec la mise en garde que les volumes d'instances suivent le calendrier
des mandats et ne se lisent pas comme une tendance. Effets répercutés en
§§5.2, 5.3, 5.4, 5.5 et 5.10. Deux points laissés en suspens depuis la
campagne sont tranchés : la double dénomination du service coexiste **à
l'intérieur d'un même rapport** (ce n'était donc pas un décalage entre
fiches et rapport), et le comité de déontologie n'apparaît plus que
rétrospectivement, comme origine du contrôle interne de 2019.
**Leçon** : une branche peut être juste sur la règle et muette sur son
application. Le rapport d'activité d'une autorité est une source de
**droit vécu** — ce qui est effectivement décidé — que le texte ne donne
jamais.

## 2026-09-01 — contrat de sortie (§2, §7, §8)
**Cas** : rejeu du test de coactivation sur le vote électronique des
élections professionnelles de décembre 2026. Fond **RÉUSSI**, onze
références vérifiées une à une sans aucune invention, aucune règle
territoriale rapatriée depuis `dpo-ct`. Trois défauts de forme subsistent.
**Ce qui a manqué / ce qui était incertain** : deux des trois défauts ne
sont pas imputables au répondant. Le §7 interdisait « le skill », « mon
référentiel », « ma base » — trois formules énumérées, que le répondant a
contournées sans le vouloir en en écrivant une quatrième : « le référentiel
utilisé pour préparer cette réponse ». **Une interdiction énumérée se
contourne ; une interdiction de classe, non.** Et le mot « maturité »
désignait deux choses à la fois — l'état d'une branche, qui est de la
tuyauterie, et le niveau de certitude d'un élément, qui est dû au
destinataire et prescrit par le §3. Le juge les a confondues et a signalé
comme défaut un tableau qui était exigé. Un répondant aurait fait la même
lecture et l'aurait supprimé : c'est la sur-correction qui avait déjà
dégradé T09 en v0.9.2, prête à se rejouer.
**Source qui a permis de trancher** : le §3 du contrat de sortie lui-même,
qui prescrit le tableau que le §7 semblait interdire.
**Action** : le §7 vise désormais toute mention du dispositif *sous quelque
formulation que ce soit*, et renvoie à la rédaction de remplacement (dire ce
qui reste à obtenir et auprès de qui, §8.4). Les deux sens de « maturité »
sont nommés séparément, et le §3 est explicitement hors du champ de
l'interdiction. Le §2 demande une date de référence donnée comme une date,
non comme un compte rendu de vérification. Le §8.1 précise qu'un article de
règlement européen se cite par son numéro comme un décret : le répondant
déroulait tout le contenu de l'article 28 du RGPD sans jamais le nommer.

## 2026-08-28 — instances-dialogue-social : imputation article 110 / 109

**Cas** : campagne de test `tests/TESTS.md` (T11). Un répondant à contexte
frais, chargé de vérifier sur Légifrance si la CCP reste consultée sur les
bonifications indiciaires, a contesté une affirmation de la branche.

**Ce qui a manqué / ce qui était incertain** : `references/instances-dialogue-social.md`
§5.5 impute la modification du titre IV du décret n° 2003-224, avec effet au
1er janvier 2023, à l'**article 110** du décret n° 2020-1427. Contre-vérification
sur sources primaires : l'article 110 est une pure disposition d'entrée en
vigueur du décret n° 2020-1427 et ne modifie aucun article du décret de 2003.
La modification est en revanche réelle et vient de l'**article 109** du même
décret, qui a modifié les articles 3 et 33 du décret n° 2003-224 — l'article 33
relevant bien du titre IV. Le répondant avait raison sur l'imputation, mais
tort sur la conclusion : il en déduisait un simple « rafraîchissement de
métadonnées », ce qui aurait introduit une seconde erreur.

**Source qui a permis de trancher** : article 110 du décret n° 2020-1427
(JORFARTI000042546051, texte lu intégralement) ; historique des modificateurs
du décret n° 2003-224 (LEGITEXT000005634089) ; fiche de l'article 33 portant
mention « Modifié par Décret n° 2020-1427 du 20 novembre 2020 - art. 109 » ;
fiche de l'article 109 (LEGIARTI000042547133, depuis abrogé par le décret
n° 2024-1038 art. 29), rubrique « A modifié les dispositions suivantes ».

**Action** : correction à porter en §5.5 — remplacer « par l'article 110 du
décret n° 2020-1427 » par « par l'article 109 du décret n° 2020-1427, dont
l'entrée en vigueur au 1er janvier 2023 est fixée par l'article 110 du même
décret ». Ne pas supprimer la phrase. Impact nul sur le fond : l'article 36
est inchangé depuis le 14 mars 2003, la CCP reste consultée sur les
bonifications indiciaires. Correction non appliquée pendant la campagne, pour
ne pas invalider le prochain tirage ; T11 à rejouer après.

---

## 2026-08-28 — instances-dialogue-social : fondement de la consultation du CSA

**Cas** : campagne de test `tests/TESTS.md` (T15), seul échec de la campagne.
Le livrable demandé était une décision DG actant une réorganisation de la DRH
après avis du CSA.

**Ce qui a manqué / ce qui était incertain** : le considérant n° 2 de l'acte
produit fonde la consultation du CSA sur « l'article 34 du décret n° 2020-1427 ».
L'article 34 porte en réalité sur l'affichage des candidatures dans les
sections de vote. Le fondement de la consultation du CSA sur les projets
relatifs au fonctionnement et à l'organisation des services est l'**article 48**.
L'erreur est dans le corps de l'acte destiné à la signature, et la checklist de
sortie cochait « source officielle vérifiée pour la règle engageante ».

Cause identifiée : `references/instances-dialogue-social.md` §5.1 énonce
l'attribution du CSA **sans numéro d'article**, et `assets/decision-dg-modele.md`
ne fournit pas de bloc de visas type pour ce cas. Le rédacteur a comblé le
manque par un numéro plausible. Une case cochée à tort a été relevée de la même
façon sur T04 : un contrôle déclaré fait qui ne l'était pas.

**Source qui a permis de trancher** : décret n° 2020-1427 du 20 novembre 2020,
articles 34 et 48, lus sur Légifrance.

**Action** : porter le numéro d'article exact du fondement de consultation du
CSA dans la branche et dans le gabarit de décision DG, pour que le rédacteur
n'ait plus à le reconstituer ; renforcer la règle de sortie interdisant de
cocher un contrôle non effectué. Correction non appliquée pendant la campagne ;
T15 à rejouer après.

---

## 2026-08-28 — campagne de test complète v0.9.0

**Cas** : première exécution intégrale de `tests/TESTS.md`, protocole à
sous-agents (répondant Sonnet 5 / juge indépendant Opus 5, contexte frais par
test, attendus jamais transmis au répondant).

**Résultat** : 12 RÉUSSI, 2 PARTIEL, 1 ÉCHOUÉ. Les quatre tests d'innocuité
(T03, T05, T08, T10) sont réussis, seuil de mise en service atteint. Rapport →
`tests/rapports/RAPPORT-2026-08-28.md`.

**Ce qui a manqué / ce qui était incertain** : trois points transverses.
1. **Coactivation `recherche-juridique` déclenchée une fois sur deux** dans le
   bloc D — non déclenchée en T11 malgré un énoncé contenant « Vérifie sur
   Légifrance » et « depuis la réforme de 2023 », déclenchée en T12 où elle a
   produit le meilleur résultat de la campagne (15 affirmations vérifiées sur
   un texte de moins de treize mois, aucune hallucination). Le libellé de
   dépendance en en-tête ne suffit pas à provoquer l'appel.
2. **Exposition de la mécanique interne** signalée par onze verdicts sur
   quinze : chemins de fichiers, noms de branches, statuts de maturité et
   checklist de contrôles apparaissent dans le livrable remis au lecteur. Le §4
   impose de signaler le niveau de confiance, pas d'exposer la tuyauterie.
3. **`dpo-ct` écarté à bon droit** en T13 et T14 (skill borné aux collectivités
   territoriales), sans transposition indue et sans appauvrir le raisonnement
   RGPD — le comportement prévu par le bloc E. Réserve : la méthode CNIL
   d'AIPD n'est pas déroulée, faute de référence équivalente côté ANSM.

**Action** : rendre l'appel à `recherche-juridique` obligatoire sur déclencheur
explicite plutôt que « recommandé » ; ajouter une règle de sortie séparant le
livrable de la note de production.

---

## 2026-09-01 — v0.9.7 et v0.9.8 : une source qu'on n'a pas lue ne peut être que nommée

**Cas** : l'audit du 28 août avait retrouvé la charte de déontologie de
février 2026, le dispositif mis à jour et le rapport du déontologue 2025,
et les avait versés au registre. Le rejeu de T13 montrait pourtant
qu'aucune n'était citée : la réponse continuait de donner la décision DG
du 6 juillet 2012 comme périmètre actuel.

**Ce qui a manqué / ce qui était incertain** — trois tentatives, dont
deux fondées sur un mauvais diagnostic :

1. **Réécrire l'en-tête** de la branche, sources en vigueur en tête.
   Sans effet : le répondant construit sa réponse depuis le **corps**,
   pas depuis la déclaration d'intention en tête de fichier.
2. **Nommer les sources dans le passage opératoire**, en qualifiant la
   décision de 2012 d'acte fondateur. La décision de 2012 a cessé d'être
   présentée comme l'état courant — mais les sources restaient
   « citées sans emploi ».
3. **Dépouiller réellement la charte** et verser son contenu au corps.
   Sources enfin **mobilisées** : périmètre restitué presque mot pour
   mot, exclusion des liens de parenté érigée en contrôle avant
   transmission, actualisation annuelle transformée en règle
   d'information.

**Enseignement transposable** : *une source qu'on n'a pas lue ne peut
être que nommée*. Les deux premières corrections déplaçaient une
étiquette ; seule la troisième a apporté de la matière. Pointer plus fort
ne remplace pas le dépouillement — et l'écart entre « source au registre »
et « source utilisable » est exactement le travail de lecture.

**Nuance utile** : pour le dispositif de février 2026, le diagnostic était
inverse. La branche portait déjà son contenu (arrêtés de 2017, amende de
30 000 €, déclaration de moins d'un an, conduite des séances) mais ne
l'attribuait à rien. Il manquait l'**attribution**, pas l'extraction. Les
deux défauts se ressemblent en sortie — une source non citée — et
appellent des corrections opposées.

**Lacune trouvée par un juge, et qui comptait** : la branche était muette
sur la **durée de publication** des déclarations. Un répondant a comblé
le vide à contresens, en affirmant qu'une fiche maintenue en ligne après
la sortie du périmètre n'avait plus de base légale. L'**article R. 1451-3
du code de la santé publique** prévoit la publication pendant la durée
des fonctions **et les cinq années suivant leur fin**. Un silence de la
documentation ne produit pas une abstention : il produit une invention.

**Sources qui ont permis de trancher** : charte de déontologie de l'ANSM,
février 2026 (périmètre des DPI publiées, exclusion des liens de parenté,
site DPI santé, actualisation au moins annuelle même sans modification) ;
dispositif de prévention et de gestion des conflits d'intérêts, mise à
jour février 2026 ; art. R. 1451-3 du code de la santé publique.

**Action** : charte et dispositif extraits et lus ; contenu versé au corps
de la branche avec attribution explicite ; durée de publication écrite
avec ses deux erreurs symétriques ; en-tête rendant compte du
dépouillement fait et de ce qui reste à lire.
**Reste ouvert** : le contenu des rapports du déontologue 2024 et 2025,
non dépouillé — les chiffres de la branche datent encore de 2023 ; et une
lacune structurelle relevée par un répondant, l'absence de toute branche
ou source **RGPD/CNIL** dans le référentiel, qui fait reposer le bloc E de
la batterie sur ce que le répondant va chercher au-dehors.

---

## 2026-09-01 — v0.9.5 puis v0.9.6 : le versant, troisième contrôle

**Cas** : réancrage de la branche formation sur le livre IV du CGFP,
dernier chantier ouvert par l'audit du registre. Le cadre général de la
formation n'était plus à chercher dans un décret antérieur : il est au
code depuis le 1er août 2026.

**Ce qui a manqué / ce qui était incertain** :

1. **Une distinction que la branche ne faisait pas.** Son §5.6 rangeait le
   CPF, l'entretien professionnel et la VAE parmi les points « non
   documentés ». Ambigu : leur **cadre général** est codifié, ce qui
   manque est la **déclinaison ANSM**. Confondre les deux fait s'abstenir
   là où il y a une règle à citer.
2. **Une erreur introduite par la correction elle-même.** Le réancrage
   citait les **art. L. 422-28 et suivants** parmi les blocs applicables.
   Ces articles existent et sont en vigueur — mais en **section propre à
   la fonction publique territoriale** (formations CNFPT, promotion
   interne). Ils ne s'appliquent pas à un établissement public de l'État.
   Le répondant du test de vérification l'a relevé en contrôlant au code
   ce que la branche l'invitait à contrôler.

**Enseignement transposable** : trois corrections successives ont porté
sur trois défauts différents d'une même citation — le **véhicule** (un
décret abrogé), la **vigueur** (un article réécrit), et maintenant le
**versant** (un article d'un autre versant de la fonction publique). Un
article peut être exact, en vigueur, et hors versant. La chaîne de
contrôle est donc **véhicule → vigueur → versant**, et aucun des trois
maillons ne se déduit des deux autres.

Second enseignement, sur le dispositif de test : c'est le **répondant**,
pas le juge, qui a trouvé l'erreur — parce que la branche lui disait
explicitement quoi vérifier. Une réserve bien écrite ne se contente pas
de protéger le skill : elle **oriente le contrôle** de qui l'utilise.

**Sources qui ont permis de trancher** : plan du livre IV du CGFP (titre
II formation, titre III télétravail, titre IV réorganisation de
services) ; sous-section « Formations d'intégration et de
professionnalisation », art. L. 422-28 à L. 422-34-1, située en section 3
« Dispositions particulières à la fonction publique territoriale ».

**Action** : branche formation réancrée au niveau des blocs, avec
distinction cadre général / déclinaison ANSM ; référence territoriale
retirée et avertissement de versant posé ; **quatrième règle du socle**
sur les sections par versant ; registre complété d'une entrée
`CGFP-LIVRE4`. Correction d'outillage au passage : le formateur de dates
écrivait « vérification du 1 septembre », interdisant toute branche
vérifiée un premier du mois — corrigé avec test de non-régression.
**Reste ouvert** : l'article précis de chaque règle générale de formation,
et l'application des dispositifs aux contractuels de droit public, que la
partie législative désigne par « agent public ».

---

## 2026-08-28 — v0.9.4 : l'audit qui transforme deux erreurs en motif

**Cas** : deux abrogations trouvées coup sur coup par des juges de test, sur
deux branches différentes, imputables au même décret de codification. Plutôt
que d'attendre la troisième, audit des 21 entrées du registre par trois
auditeurs indépendants, chaque anomalie revérifiée avant correction.

**Ce qui a manqué / ce qui était incertain** :

1. **Ce n'étaient pas deux accidents mais un programme.** La partie
   réglementaire du CGFP se construit **livre par livre** : livres I et II au
   1er février 2025 (décret n° 2024-1038), livre III — recrutement — au
   1er octobre 2025 (décret n° 2025-695), livre IV — organisation et gestion
   RH, dont la **formation** et le **télétravail** — au 1er août 2026 (décret
   n° 2026-366), livre V annoncé. Le référentiel était ancré sur les
   véhicules d'avant, et la dernière vague avait 27 jours.
2. **Une règle manquait au socle** : un article **survivant** peut avoir été
   **réécrit** par le décret codificateur. Vérifier qu'un article dit bien ce
   qu'on lui fait dire ne suffit donc pas — il faut citer la version.
3. **Le numéro refusé en v0.9.3 n'était pas là où on le cherchait.** La
   composition disciplinaire de la CCP n'est pas dans le code : elle est
   restée à l'**article 44 du décret n° 86-83**, réécrit au 1er février 2025,
   qui renvoie lui-même à l'art. R. 271-1 du CGFP. Le régime est hybride.
   Chercher dans le seul code ne pouvait pas aboutir — et le refus d'écrire
   un numéro plausible a évité d'inscrire une erreur.
4. **Une réserve fausse depuis trois jours.** Le dépôt affirmait qu'aucune
   URL n'avait été retrouvée pour la charte de déontologie de février 2026 et
   le dispositif conflits d'intérêts. Les deux sont publics.

**Enseignement transposable** : une réserve d'abstention **se périme comme
une affirmation**. « Document non retrouvé » est une constatation datée, pas
un état permanent ; elle doit être réinterrogée à chaque revue, au même titre
qu'une règle. Et symétriquement : deux occurrences d'un même motif justifient
d'auditer l'ensemble plutôt que de corriger la troisième quand elle viendra.

**Sources qui ont permis de trancher** : décrets n° 2024-1038, n° 2025-695 et
n° 2026-366 (programme de codification et dates d'effet) ; art. 44 du décret
n° 86-83 en vigueur depuis le 1er février 2025 ; art. R. 431-1 et s. du CGFP
(télétravail) ; charte ANSM de février 2026 et dispositif mis à jour février
2026, millésimes confirmés en page de couverture.

**Action** : programme complet de codification et ses trois règles portés au
socle ; registre corrigé sur sept entrées et enrichi de quatre ; branches
QVT, instances et déontologie réancrées ; branche formation marquée à
réancrer. **Rejeu** : T10 et T13, tous deux RÉUSSI. Détail →
`tests/rapports/RAPPORT-2026-08-28-audit-registre.md`.
**Reste ouvert** : le réancrage de la formation sur le livre IV ; les
nouvelles sources ANSM déclarées citables mais pas encore exploitées par le
corps de la branche déontologie — lever une réserve ne suffit pas à faire
utiliser la source.

---

## 2026-08-28 — v0.9.3 : deux textes abrogés, un garde-fou plutôt que deux rustines

**Cas** : la v0.9.2 avait corrigé un visa reposant sur le décret
n° 2020-1427, abrogé au 1er février 2025, mais seulement là où il
produisait un acte fautif. Les autres mentions restaient. Leur reprise a
fait apparaître que le problème n'était pas isolé.

**Ce qui a manqué / ce qui était incertain** :

1. **Une seconde abrogation, même décret de codification.** L'**article
   1-2 du décret n° 86-83**, qui portait les règles de la CCP, est abrogé
   depuis le 1er février 2025 par l'**article 10 du décret n° 2024-1038**
   — quand le décret n° 2020-1427 l'était par l'article 29 du même texte.
   La règle des trois jours siège désormais à l'**article R. 271-12 du
   CGFP**.
2. **L'abrogation est ciblée, pas générale.** Les autres articles du
   décret n° 86-83, dont les articles 43-2 et 44, restent en vigueur. Se
   tromper dans l'autre sens — traiter tout le décret comme abrogé —
   coûterait aussi cher.
3. **Un seuil décalé d'une unité.** La formation spécialisée SSCT était
   présentée comme obligatoire « au-delà de » 200 agents. L'article
   R. 251-28 vise un effectif « au moins égal à deux cents agents » :
   l'obligation joue **dès** 200.
4. **Une barrière de fraîcheur qui interdisait de rafraîchir.**
   `tests/test_validation.py` figeait sa date de référence au 25 août :
   toute affirmation vérifiée après cette date était rejetée comme
   « située dans le futur ».

**Enseignement transposable** : deux abrogations issues du même décret de
codification, trouvées l'une après l'autre par des juges différents sur
des branches différentes, ce n'est plus une erreur, c'est un motif. La
réponse n'est pas une troisième correction ponctuelle mais un
**avertissement transverse** dans le socle : avant de viser un texte
réglementaire antérieur à 2025 en matière de dialogue social ou
d'instances, contrôler qu'il n'a pas été codifié. Corollaire méthodique
déjà tiré en v0.9.2 et confirmé ici : vérifier qu'un article dit bien ce
qu'on lui fait dire ne dispense pas de vérifier que **le texte qui le
porte est en vigueur à la date de l'acte**.

**Sources qui ont permis de trancher** : art. 10 et 29 du décret
n° 2024-1038 du 6 novembre 2024 ; art. R. 251-20, R. 251-28, R. 253-1,
R. 271-1 et R. 271-12 du code général de la fonction publique ; état de
vigueur des art. 43-2 et 44 du décret n° 86-83.

**Action** : réancrage complet des branches instances et QVT sur le CGFP ;
registre dédoublé (`CSA-ETAT` / `CSA-ETAT-ANCIEN`, ajout de `CCP-ETAT`) ;
avertissement transverse de codification dans le socle ; correction du
seuil de 200 agents ; deux misattributions résiduelles de l'article 110
rectifiées ; date de référence des tests désindexée d'une date écrite en
dur. **Rejeu** : T06, T10 et T15 — fond RÉUSSI pour les trois, T15
décrochant pour la première fois fond et forme. Détail →
`tests/rapports/RAPPORT-2026-08-28-codification.md`.
**Reste ouvert** : la règle de composition disciplinaire de la CCP est
laissée **sans numéro d'article**, faute d'avoir pu le lire en source — et
le reste du registre n'a pas été audité pour cette vague de codification.

---

## 2026-08-28 — v0.9.2 : la tuyauterie hors de la réponse, sans emporter les sources

**Cas** : toutes les campagnes de la journée relevaient le même défaut de
forme — chemins de fichiers, noms de branches, bandeaux de maturité, codes
du registre, mentions du « skill » et check-list de contrôles figuraient
dans le texte remis. Aucun test n'en échouait ; aucune réponse n'était
transférable telle quelle à un agent qui ignore le dispositif.

**Ce qui a manqué / ce qui était incertain** :

1. **La cause était dans l'instruction, pas dans le comportement.** Le
   contrat de sortie demandait lui-même la « branche principale et les
   renvois inter-branches » (§2), de « pointer vers le gabarit dans
   `assets/` » (§5), et sa check-list §6 ne se disait nulle part interne.
   Corriger le comportement sans corriger l'instruction n'aurait rien
   donné.
2. **La première correction a sur-corrigé.** Rejeu de T09 : forme
   conforme, fond retombé en PARTIEL — le répondant avait retiré, avec la
   tuyauterie, presque toutes les sources officielles nommées et les
   valeurs vérifiées. Une **interdiction en liste face à une obligation en
   prose ne fait pas jeu égal** : douze interdits en puces contre une
   phrase de paragraphe, le modèle suit la liste.
3. **Un visa reposant sur un texte abrogé.** En contrôlant les visas un à
   un, un juge a établi que le **décret n° 2020-1427 est abrogé depuis le
   1er février 2025** (art. 29 du décret n° 2024-1038), ses dispositions
   étant codifiées au CGFP. Or c'est ce décret que la v0.9.1 venait
   d'inscrire comme fondement de la consultation du CSA. Remplacer un
   numéro faux par un numéro exact **dans un véhicule abrogé** ne corrige
   qu'à moitié : vérifier qu'un article dit bien ce qu'on lui fait dire ne
   dispense pas de vérifier que le texte qui le porte est en vigueur à la
   date de l'acte.

**Enseignement transposable** : une règle de retrait doit toujours être
écrite avec sa règle de conservation, au même rang et dans le même
format. La ligne de partage retenue : masquer ce qui décrit *comment la
réponse a été fabriquée*, conserver ce qui permet *de la contrôler* — un
chemin de fichier ne se vérifie pas, un numéro de décret si.

**Sources qui ont permis de trancher** : article 29 du décret
n° 2024-1038 du 6 novembre 2024 (abrogation du décret n° 2020-1427 au
1er février 2025) ; article R. 253-1, 1° du code général de la fonction
publique, partie réglementaire (titre V « Comités sociaux »).

**Action** : `contrat-sortie.md` réécrit — règle de séparation, §2 en
langage métier, §5 sans chemin, check-list §6 explicitement interne, §7
des interdits, **§8 des obligations de citation de même rang**, §9 test de
relecture en deux moitiés. `SKILL.md` §4, §7 et §10 alignés.
`instances-dialogue-social.md` §5.1 et `assets/decision-dg-modele.md`
réancrés sur l'article R. 253-1, 1° du CGFP, avec avertissement sur le
véhicule. **Rejeu** : T05, T09 et T15 rejoués — fond RÉUSSI pour les
trois, forme conforme (T05) ou résidus mineurs (T09, T15), sources
suffisantes. Détail → `tests/rapports/RAPPORT-2026-08-28-forme.md`.
**Reste ouvert** : le réancrage des autres mentions du décret de 2020 dans
la branche instances, à faire avant la v1.0.0.

---

## 2026-08-28 — v0.9.1 : correction des deux défauts de campagne et rejeu

**Cas** : la première exécution intégrale de `tests/TESTS.md` (voir l'entrée
du même jour) avait laissé deux défauts constatés mais non corrigés, pour ne
pas invalider le tirage suivant. Ils sont corrigés ici, puis les deux tests
concernés ont été rejoués sur des sous-agents neufs.

**Ce qui a manqué / ce qui était incertain** :

1. **Imputation fausse d'un article modificateur.**
   `instances-dialogue-social.md` §5.5 attribuait à l'**article 110** du
   décret n° 2020-1427 la modification du titre IV du décret n° 2003-224 au
   1er janvier 2023. L'article 110 est une pure disposition d'entrée en
   vigueur. La modification vient de l'**article 109**, qui touche les
   articles 3 et 33 du décret de 2003 (substitution du CSA au comité
   technique) ; l'article 109 a lui-même été abrogé par l'article 29 du
   décret n° 2024-1038 du 6 novembre 2024. L'article 36 — celui qui porte
   l'avis de la CCP sur les bonifications indiciaires — est resté inchangé
   depuis le 14 mars 2003.
2. **Lacune ayant produit un visa fabriqué.** Le §5.1 énonçait les
   attributions du CSA sans numéro d'article. Le rédacteur du livrable T15 a
   comblé la lacune par un « article 34 » plausible mais sans rapport
   (l'article 34 porte sur l'affichage des candidatures aux élections), dans
   le corps d'une décision destinée à signature, et sa checklist de sortie
   certifiait la vérification. Le fondement exact est l'**article 48, 1°**.

**Enseignement** : une branche qui énonce une règle **sans son numéro
d'article** ne produit pas une réponse prudente, elle produit un numéro
inventé. La lacune documentaire est ici plus dangereuse que l'absence de la
règle : le rédacteur, sommé de viser un texte, comble. Et le second
enseignement tient au dispositif de vérification lui-même : c'est l'historique
des modificateurs qui distingue l'article qui **modifie** de celui qui fixe
seulement une **date d'entrée en vigueur** — le noyau autonome du skill ne va
pas jusque-là, `recherche-juridique` si.

**Sources qui ont permis de trancher** : article 48 du décret n° 2020-1427
(JORFARTI000042546151), article 109 (LEGIARTI000042547133, rubrique « A
modifié les dispositions suivantes » : art. 3 et 33 du décret n° 2003-224),
article 110 (JORFARTI000042546051), article 36 du décret n° 2003-224
(LEGIARTI000006564370). Vérifications croisées par le juge de campagne puis
refaites indépendamment avant écriture.

**Action** : correction de `instances-dialogue-social.md` §5.1 et §5.5 ; ajout
du fondement et d'une règle de visa dans `assets/decision-dg-modele.md` ;
nouveau §3.0 de `SKILL.md` fixant le critère de passage de main à
`recherche-juridique` ; douzième point d'auto-vérification sur les numéros
d'article. **Rejeu** : T11 et T15 rejoués sur sous-agents neufs, tous deux
**RÉUSSI** — la coactivation se déclenche, le visa fabriqué ne réapparaît pas,
et le numéro non vérifiable est laissé en champ vide sous réserve plutôt que
comblé. Bilan consolidé : 14 RÉUSSI, 1 PARTIEL, 0 ÉCHOUÉ. Détail →
`tests/rapports/RAPPORT-2026-08-28-rejeu.md`.

---

## 2026-08-25 — v0.9.0 : comportement, données RH et préavis

**Cas** : vérifier la qualité réelle des réponses et anticiper la
maintenance sans exposer de dossiers d'agents.

**Action** : vingt scénarios métier, grille de revue, filtre local des
identifiants, demande structurée anonymisée, préavis automatique à J-7,
modèles de sortie et registre sans contenu confidentiel pour les pièces
internes manquantes.

---

## 2026-08-25 — v0.8.0 : expiration, tests et protection de main

**Cas** : rendre la barrière de fiabilisation durable et impossible à
contourner par un push direct.

**Action** : ajout de délais de fraîcheur par affirmation, de huit tests
de régression, de leur exécution dans la CI et d'une configuration de
protection de branche imposant pull request et statut `validate` réussi.

---

## 2026-08-25 — v0.7.0 : barrière de fiabilisation automatique

**Cas** : empêcher qu'une branche soit classée ✅ sans preuve complète
de ses affirmations importantes.

**Ce qui a manqué / ce qui était incertain** : le validateur contrôlait
quelques garde-fous ponctuels, mais pas la cohérence systématique entre
maturité, date, affirmations, registre et URL officielles.

**Action** : ajout du manifeste `evals/source-gates.json` et d'un
contrôle bloquant sans dépendance externe. Les trois branches ✅ sont
reliées à des identifiants de sources officielles complétés dans le
registre. Un second contrôle réseau, exécuté par la CI, vérifie que ces
URL répondent effectivement.

---

## 2026-08-25 — v0.6.1 : recalage de la maturité sur la preuve disponible

**Cas** : audit externe à partir d'une copie locale synchronisée avec la
version v0.6.0 du dépôt.

**Ce qui a manqué / ce qui était incertain** : les versions ANSM 2026 de
la charte de déontologie et du retour d'information budgétaire étaient
décrites comme directement vérifiées, sans URL officielle retrouvable.
L'article L. 124-7 du CGFP était aussi formulé trop largement.

**Source qui a permis de trancher** : art. L. 124-7 du CGFP ; art. 107 IV
de la LFSS 2026 ; rapport public 2023 du déontologue de l'ANSM.

**Action** : déontologie et budget reclassés 🟢 ; sources ajoutées au
registre ; données non traçables marquées à confirmer ; tests de
régression étendus.

---

## 2026-08-25 — publication v0.6.0 : corrections de traçabilité et de droit

**Cas** : revue de publication du dépôt avant réutilisation du skill.

**Ce qui a manqué / ce qui était incertain** : l'arborescence annoncée
n'existait pas, les sources n'étaient pas reliées à leurs URL officielles,
et deux formulations confondaient une règle FPT avec le régime FPE et
une réserve interne ANSM avec l'article 432-12 du code pénal.

**Source qui a permis de trancher** : registre
`references/sources-principales.md`, notamment décret n° 2025-1430,
arrêté du 2 juillet 2025, articles 432-12 et 432-13 du code pénal.

**Action** : fichiers rangés, registre créé, textes corrigés, validateur,
cas de régression et contrôle CI ajoutés. Toute correction de fond doit
désormais modifier simultanément la branche, le registre, le changelog et
le journal.

---

## 2026-08-24 — audit interne du skill (v0.5.1)

**Cas** : audit complet demandé par l'utilisateur, conduit comme sur le
travail d'un tiers. Rapport détaillé : `AUDIT.md`.

**Résultat** : fond juridique sain ; **10 défauts de cohérence ou de
structure** (5 majeurs, 5 mineurs), tous corrigés.

**Le constat qui compte** : les trois principaux défauts majeurs ont la
même cause — un **défaut de propagation des corrections**. Chaque erreur
de fond avait été corrigée là où elle avait été découverte, mais pas
dans tous les fichiers qui répétaient l'information : le **frontmatter
de déclenchement contenait encore « délai de viduité » et « subvention
d'État »**, deux erreurs pourtant corrigées et journalisées dans le
corps du skill. Autrement dit : la partie du skill lue en premier
véhiculait encore ce que le reste avait appris à ne plus dire.

**Règle de méthode ajoutée** : toute correction de fond est close
uniquement après recherche de l'information erronée sur **l'ensemble**
du skill — frontmatter, README et assets compris.

**Enseignement transposable** : dans un système documentaire versionné,
les erreurs ne meurent pas là où on les corrige ; elles survivent dans
les copies. L'audit final doit toujours inclure une passe mécanique
(recherche de motifs) et pas seulement une relecture.

---

## 2026-08-24 — correction majeure : régime de financement, et une source sous-exploitée

**Déclencheur** : question de l'utilisateur — « les informations
manquantes sont-elles trouvables sur internet ? ». Vérification faite :
**oui, en grande partie. J'avais sous-cherché.**

**La source manquée** : l'ANSM publie, après **chaque séance de son
conseil d'administration**, un document **« Retour d'information »**
ainsi que ses **délibérations**, sur ansm.sante.fr. Ces documents
contiennent le budget initial et les budgets rectificatifs, le plafond
d'emplois, le programme de travail annuel, et **les avis du CSA avec le
détail des votes**. Rien de tout cela n'est confidentiel.

**⚠️ Erreur corrigée — régime de financement.** La branche budget
décrivait l'ANSM comme financée par une **subvention pour charges de
service public du programme 204** du budget de l'État. C'était le régime
**2012-2019**. Le régime actuel est une **dotation de l'Assurance
Maladie**. Trois régimes se sont succédé :

| Période | Financement principal |
|---------|----------------------|
| Avant 2012 (AFSSAPS) | Taxes et redevances de l'industrie (> 80 %) |
| 2012-2019 | SCSP du programme 204, mission Santé (> 90 %) |
| Aujourd'hui | **Dotation de l'Assurance Maladie** |

L'erreur venait d'une source secondaire (rapport parlementaire décrivant
la période 2012-2019) prise pour une description du présent.

**Données 2026 désormais intégrées** (CA du 27 novembre 2025) :
- dotation Assurance Maladie **143,69 M€** (+1,07 M€) ; ressources
  propres **19,38 M€** (activité européenne rémunérée) ;
- plafond d'emplois **957 ETPT sous plafond**, **77,7 ETPT hors
  plafond** ;
- enveloppes : personnel **97,73 M€**, fonctionnement 24,03/25,38 M€,
  intervention 26,62/26,254 M€, investissement 11,99/14,86 M€ ;
- répartition par mission : Surveiller 37 %, Autoriser 26 %, Support
  13 %, Contrôler 12 %, Inspecter 8 %, Informer 4 % ;
- **budget en déficit**, financé par un **prélèvement de 5,51 M€ sur le
  fonds de roulement** ; fonctionnement −5,40 %, investissement −9,83 % ;
  personnel en légère hausse (effectifs + GVT).

**Signal social capté** : le CSA du 13 novembre 2025 s'est prononcé sur
le budget 2026 **et** sur le programme de travail 2026 par **1 voix pour
et 7 abstentions**. Indicateur de climat à connaître avant toute
négociation.

**Autres apports** :
- **Un nouveau plan d'actions QVT/RPS est en cours d'élaboration en
  2026**, inscrit à l'axe 4 du COP et au programme de travail voté.
  Chantier ouvert, attendu par la tutelle — à reprendre, pas à lancer.
- **Automatisation et assistance par IA** des processus inscrites au
  même axe : impact conditions de travail, à articuler avec le plan QVT
  et le dialogue social.
- **Le troisième site est à Vendargues (34)**, pas à Montpellier
  stricto sensu. La direction des contrôles compte **124 agents** sur
  les trois sites. Nouveau site de Lyon en fin de construction ; travaux
  d'étanchéité à Saint-Denis et Vendargues — facteurs de conditions de
  travail à part entière.

**Ce qui reste introuvable en ligne** : la **délibération du CA portant
cadre d'emploi** (grilles indiciaires, emplois-repères), le **règlement
intérieur** de l'agence, et le **volet SI RH**. À noter : l'équivalent
de **Santé publique France**, pris sur le même décret n° 2003-224, est
**intégralement public, grilles indiciaires comprises** — il constitue
un analogue de structure utile, à ne jamais transposer comme source du
droit applicable à l'ANSM.

**Action** : branche budget réécrite et passée en ✅ ; branche QVT
enrichie ; socle complété d'une entrée dédiée aux retours d'information
du CA ; corrections de site répercutées.

**Enseignement transposable — le plus important de tous les cycles.**
Avant de conclure qu'une information est interne, **vérifier ce que
l'organisme publie de sa propre gouvernance**. Les établissements
publics publient leurs délibérations d'organe délibérant : c'est là que
vivent les données budgétaires, les effectifs, les orientations et les
votes des instances. J'avais cherché du côté des documents budgétaires
de l'État (annexes du PLF) alors que la réponse était sur le site de
l'agence. **Chercher d'abord chez l'organisme, ensuite chez sa tutelle.**

---

## 2026-08-24 — six branches restantes (instances, fonctionnaires, budget, QVT, formation, communication)

**Cas** : traitement des six branches non encore fiabilisées, pour
achever la couverture des huit branches du skill.

**Résultat, en toute honnêteté** : deux branches atteignent ✅, trois
plafonnent à 🟢, une reste 🟡. L'écart tient à une cause unique et
prévisible : **une branche n'est fiabilisable que si elle repose sur un
texte publié ou sur un document que l'agence publie elle-même.**

| Branche | Niveau | Facteur limitant |
|---------|--------|------------------|
| instances-dialogue-social | ✅ | — |
| fonctionnaires-corps-spécifiques | ✅ | — |
| masse-salariale-budget-sirh | 🟢 | montants de l'année introuvables ; SI RH non documenté |
| qvt-sante-travail | 🟢 | dispositif interne (télétravail, RPS, DUERP) non publié |
| formation-développement | 🟢 | plan et budget actuels non publiés |
| communication-interne | 🟡 | sujet sans trace publique par nature |

**Découverte à forte valeur opérationnelle — échéance électorale.**
L'arrêté du 2 juillet 2025 fixe les élections professionnelles des trois
versants au **10 décembre 2026**. À la date de cette entrée, il reste
moins de quatre mois. La modalité de vote, les effectifs de référence et
le calendrier local doivent être vérifiés. **Correction v0.6** : ne pas
transposer à la FPE le délai FPT de six mois relatif aux formations
spécialisées ; le dossier reste urgent, sans que cette échéance puisse
être affirmée pour l'ANSM. Un encadré d'urgence a été placé en tête de la
branche instances. C'est le point le plus immédiatement actionnable de
tout le skill.

**Autres apports notables** :
- **Formation spécialisée SSCT obligatoire** à l'ANSM (seuil de 200
  agents, décret n° 2020-1427) — et possibilité de créer jusqu'à deux
  formations spécialisées **de site**, ce qui correspond exactement à la
  situation des laboratoires de Lyon et Montpellier.
- **La CCP est l'instance individuelle structurante de l'ANSM**, à
  rebours de l'intuition : la population contractuelle étant très
  majoritaire, la CCP pèse plus que la CAP. Compétences précisées
  (art. 1-2 du décret n° 86-83), y compris le seuil des sanctions
  (avertissement, blâme et exclusion ≤ 3 jours exclus).
- **L. 5323-1 CSP** : liste limitative des catégories de personnel que
  l'agence peut employer, et fondement du « règlement » délibéré par le
  CA — ce qui **confirme et explique** la réserve structurelle
  identifiée en v0.3.0.
- **PHISP** : corps régi par le décret n° 92-1432, **recruté, nommé et
  géré par le ministre chargé de la santé**. L'ANSM est affectataire,
  pas gestionnaire. Modifié récemment par le décret n° 2025-697 du
  25 juillet 2025, à examiner.
- **Modèle de financement** : SCSP du programme 204 à plus de 90 %
  depuis 2012, en rupture assumée avec le financement par l'industrie de
  l'ex-AFSSAPS. À relier explicitement à la politique déontologique.
- **COP 2024-2028** signé le 18 juillet 2024, quatre axes : c'est le
  document auquel adosser tout projet RH structurant devant la tutelle.
- **Contrôle interne** : le processus « Gérer les ressources humaines »
  figure explicitement dans la cartographie des risques présentée au CA.
  La DRH est dans le périmètre.

**Changement de méthode assumé — introduction d'un troisième niveau de
maturité (🟢).** L'échelle binaire ✅/🟡 forçait un choix trompeur pour
trois branches où le mécanisme juridique est parfaitement établi mais
où les valeurs manquent. Le niveau 🟢 « partiellement fiabilisée » a été
ajouté et documenté dans `_gabarit-branche.md`, avec la consigne
explicite de ne jamais surévaluer une branche.

**Sources principales** : arrêté du 2 juillet 2025 ; décrets n° 2020-1427,
n° 2024-1038, n° 86-83 (art. 1-2), n° 92-1432, n° 2003-224 (art. 32-III),
n° 82-453, n° 2012-1246 ; art. L. 5323-1 à L. 5323-4 CSP ;
art. R. 5322-11 CSP ; organigramme ANSM du 7 janvier 2026 ; COP
2024-2028 ; page « Notre politique RH » de l'ANSM ; bilan social 2014.

**Action** : six branches réécrites. Échelle de maturité à trois niveaux
introduite dans le gabarit et le routeur.

**Enseignement transposable** : avant de lancer la fiabilisation d'une
branche, **se demander où vit l'information**. Si elle ne vit ni dans un
texte publié ni dans un document institutionnel, aucune quantité de
recherche ne la fera apparaître — et le temps est mieux employé à
formuler les bonnes questions à poser en interne qu'à produire du
contenu générique.

---

## 2026-08-24 — recrutement-classification-contractuels

**Cas** : fiabilisation de la branche recrutement/classification à
partir du décret n° 2003-224 du 7 mars 2003, de ses modificatifs, et de
la question écrite Sénat n° 23753 du 15 juillet 2021.

**Ce qui a manqué / ce qui était incertain** :

1. **Texte identifié et confirmé.** La maquette annonçait le décret
   n° 2003-224 comme « probablement » le texte de référence, sans
   certitude. Confirmé : l'ANSM figure bien à l'article 1er de son champ
   d'application, le décret est en vigueur et fonde les catégories
   d'emploi CE1 à CE4.
2. **Découverte structurante — la clé décret / délibération.** Le décret
   fixe l'**architecture** (4 catégories, nombre d'échelons, conditions
   d'accès, mécanismes d'avancement) mais renvoie **toutes les valeurs**
   à des **délibérations du conseil d'administration** : indices
   (art. 7), durées d'échelon (art. 7), liste des emplois-repères
   (art. 9), quotas de hors-classe (art. 39), enveloppe de bonifications
   (art. 36), liste des personnels de direction exclus (art. 6). La
   délibération de l'ANSM n'est pas publiée. **Conséquence : aucune
   réponse chiffrée n'est possible sans ce document.** C'est désormais
   signalé comme le premier document à obtenir de la DRH, et la clé de
   lecture a été ajoutée au socle §6.2.
3. **Sujet sensible documenté — classement CE1/CE2 des évaluateurs.**
   Depuis 2017, la DG a modifié la liste des emplois-repères pour
   permettre le recrutement d'évaluateurs en CE2 alors que leur niveau
   ouvrirait CE1, créant un écart salarial à missions identiques sur le
   poste d'attaché scientifique réglementaire. Point vérifié : la
   question sénatoriale est **caduque, jamais répondue** — donc **aucune
   position ministérielle** n'a tranché. Le sujet reste ouvert, ni
   validé ni condamné. À présenter comme tel.
4. **Règle oubliée dans la branche fonctionnaires.** Le décret
   (art. 32-III) classe les **praticiens hospitaliers en détachement
   directement en hors-classe de la CE1**. Règle simple, absente de la
   maquette. Ajoutée à `fonctionnaires-corps-specifiques.md`.

**Autres éléments nouveaux** : accès hors-classe des CE2/CE3/CE4 (8e
échelon + 5 ans de services effectifs, comptés dans **l'ensemble des
établissements du décret**, pas seulement l'ANSM) ; dérogation de
diplôme en CE3 (5 ans d'expérience équivalente) ; accès CE4 sans
condition de diplôme ; mobilité inter-agences avec reclassement à
identité d'échelon ; exclusion des titres IV et V pour les CDD ;
subsidiarité du décret n° 86-83 de 1986 ; modification du titre IV au
1er janvier 2023 par l'article 110 du décret n° 2020-1427.

**Sources qui ont permis de trancher** : décret n° 2003-224 (art. 1, 6,
7, 9, 11, 12, 14, 20, 23, 29, 32, 36, 39) ; décret n° 2005-1162 ;
décret n° 2020-1427 art. 110 ; art. L. 5323-1 à L. 5323-3 CSP ; question
écrite Sénat n° 23753.

**Action** : branche réécrite (412 lignes) et passée en ✅ fiabilisée,
avec réserve structurelle explicite en tête. Corrections répercutées sur
`fonctionnaires-corps-specifiques.md` (point 4) et
`socle-sources-verification.md` (points 1 et 2).

**Enseignement transposable** : sur un établissement public à statut
propre, toujours chercher **où le texte délègue**. Un décret statutaire
d'agence pose rarement les valeurs lui-même ; il renvoie à l'organe
délibérant. Identifier ce renvoi tôt évite de croire qu'on détient la
règle alors qu'on n'en a que le cadre.

---

## 2026-08-24 — deontologie-conflits-interets

**Cas** : fiabilisation complète de la branche déontologie à partir des
sources primaires (charte de déontologie de février 2026, dispositif de
prévention mis à jour février 2026, fiches probité, articles CSP / code
pénal / CGFP).

**Ce qui a manqué / ce qui était incertain** — quatre écarts entre la
maquette v0.1.0 (construite sur pages institutionnelles et documents
archivés) et les sources primaires :

1. **Erreur de fond — « délai de viduité avant embauche ».** La maquette
   présentait les trois ans comme un délai interdisant de recruter un
   candidat issu de l'industrie. Faux : c'est la durée des **réserves
   d'abstention sur les dossiers de l'ancien employeur**, notifiées via
   la promesse d'embauche. **Correction v0.6** : ces réserves sont
   internes et individualisées ; l'art. 432-12 CP ne fonde pas un délai
   de trois ans pour un candidat entrant. L'embauche elle-même reste
   possible. Erreur à fort impact opérationnel : elle aurait conduit à
   écarter à tort des candidats dans une agence en tension de
   recrutement.
2. **Charte périmée.** La maquette citait la version du 29/05/2020. La
   version en vigueur est celle de **février 2026** (mise en ligne le
   24/04/2026), et elle est **annexée au règlement intérieur** — ce qui
   lui donne une portée disciplinaire que la maquette ne mentionnait
   pas.
3. **Gouvernance mal décrite.** La maquette décrivait le référent
   déontologue comme rattaché à la DG avec un rôle de conseil, et citait
   un « comité de déontologie ». En réalité : la **directrice de la DRD
   exerce elle-même la fonction de déontologue de l'ANSM** ; le
   **référent déontologue est nommé séparément** comme appui externe en
   déontologie de la fonction publique. Le comité de déontologie
   n'apparaît **pas** dans la charte de février 2026 (figurait sur des
   pages archivées) — signalé comme à confirmer.
4. **Périmètre DPI imprécis.** La maquette donnait « environ 600 agents
   en 2012 » comme repère daté à réactualiser. La charte de février 2026
   confirme le périmètre en le précisant (dirigeants, direction et
   encadrement, membres des instances de gouvernance, métiers de
   l'évaluation scientifique/technique/réglementaire, inspection,
   contrôle pour le niveau cadre, affaires juridiques) et l'agence
   communique sur « plus de 600 agents ».

**Éléments opérationnels nouveaux, absents de la maquette** : délai de
**6 mois** de cession des actifs financiers après la période d'essai
(note DG du 28/08/2018) ; règle du **produit concurrent** en marché
étroit (≤ 3 produits) ; **dérogation encadrée** permettant d'entendre un
expert en conflit d'intérêts hors délibération et vote ; circuit
**DRH → DRD** au recrutement ; jurisprudence ANSM de la Commission de
déontologie (abandon de l'exception de non-subjectivité en 2017).

**Sources qui ont permis de trancher** : charte de déontologie ANSM
février 2026 ; dispositif de prévention et de gestion des conflits
d'intérêts (mise à jour février 2026) ; fiches 1, 1bis et 3 « Les
atteintes à la probité » ; art. L. 5323-4, L. 1451-1, L. 1454-2 et
L. 1454-4 CSP ; art. 432-12 et 432-13 code pénal.

**Action** : branche réécrite intégralement et passée en ✅ fiabilisée.
Corrections répercutées sur `recrutement-classification-contractuels.md`
(point 1) et sur `socle-sources-verification.md` (points 2 à 4, plus
ajout de la carte complète des sources déontologiques).

**Enseignement transposable aux autres branches** : les pages
institutionnelles HTML et les documents archivés de l'agence sont une
mauvaise base de fiabilisation — ils sont souvent en retard de plusieurs
années sur les PDF datés publiés dans la rubrique déontologie. Toujours
remonter au document PDF daté le plus récent avant de figer une règle.
