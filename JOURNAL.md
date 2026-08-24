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

## 2026-08-25 — v0.7.0 : barrière de fiabilisation automatique

**Cas** : empêcher qu'une branche soit classée ✅ sans preuve complète
de ses affirmations importantes.

**Ce qui a manqué / ce qui était incertain** : le validateur contrôlait
quelques garde-fous ponctuels, mais pas la cohérence systématique entre
maturité, date, affirmations, registre et URL officielles.

**Action** : ajout du manifeste `evals/source-gates.json` et d'un
contrôle bloquant sans dépendance externe. Les trois branches ✅ sont
reliées à des identifiants de sources officielles complétés dans le
registre.

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
