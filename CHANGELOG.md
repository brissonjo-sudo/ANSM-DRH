# Changelog — drh-ansm

## v0.9.3 — 2026-08-28

**Réancrage des instances sur le code général de la fonction publique.**
La v0.9.2 avait corrigé le seul point exposé — le visa d'un acte — en
laissant les autres mentions du décret n° 2020-1427, abrogé au
1er février 2025. Elles sont toutes reprises ici.

`instances-dialogue-social.md` : l'implantation du CSA est rattachée à
l'**article R. 251-20 du CGFP** (CSA d'établissement public créé par
arrêté des ministres de tutelle, placé auprès du directeur général), la
formation spécialisée SSCT à l'**article R. 251-28**, les consultations
obligatoires à l'**article R. 253-1**. Le bandeau de sources désigne
désormais le titre V de la partie réglementaire du code.

**Correction de fond au passage** : le seuil de la formation spécialisée
SSCT était présenté comme celui « au-delà duquel » l'obligation joue.
L'article R. 251-28 vise un effectif « au moins égal à deux cents
agents » : l'obligation joue **dès** 200. Corrigé dans les deux branches
qui l'énonçaient (instances et QVT).

**Deux misattributions résiduelles** de l'article 110 du décret
n° 2020-1427, identiques à celle corrigée en v0.9.1 mais restées dans
`socle-sources-verification.md` et
`recrutement-classification-contractuels.md`, sont rectifiées : c'est
l'article 109 qui modifie les articles 3 et 33 du décret n° 2003-224,
l'article 110 n'en fixant que la date d'effet.

Le registre des sources distingue maintenant `CSA-ETAT` (le code, en
vigueur) de `CSA-ETAT-ANCIEN` (le décret abrogé, réservé à la lecture de
l'état du droit antérieur, à ne jamais viser dans un acte postérieur au
1er février 2025).

`tests/test_validation.py` : la date de référence des tests suivait la
dernière campagne de vérification et bloquait toute vérification
ultérieure ; elle est portée au 28 août 2026, et le cas « date de
contrôle dans le futur » se calcule désormais à partir d'elle au lieu
d'une date écrite en dur.

## v0.9.2 — 2026-08-28

**Séparation de la réponse et de la tuyauterie.** La campagne de test du
28 août et son rejeu ont relevé le même défaut de forme dans presque
toutes les réponses : chemins de fichiers, noms de branches, bandeaux de
maturité, codes du registre de sources, mentions du « skill » et
check-list de contrôle apparaissaient dans le texte remis. Aucun test n'en
échouait, mais les sorties n'étaient pas transférables telles quelles à un
destinataire qui ignore le dispositif.

La cause était dans le contrat de sortie lui-même : son §2 demandait la
« branche principale et les renvois inter-branches », son §5 de pointer
vers un gabarit `assets/`, et sa check-list §6 ne se disait nulle part
interne. `references/contrat-sortie.md` porte désormais une règle de
séparation en tête, un §2 formulé en langage métier, un §5 qui produit le
livrable sans citer son chemin, une check-list explicitement interne et un
§7 énumérant ce qui ne figure jamais dans une réponse — assorti d'un test
de relecture : la réponse serait-elle transférable telle quelle ?

`SKILL.md` précise en §4 que le niveau de confiance se dit en français
dans le fil de la réponse, rappelle en §7 que la maturité pilote la
prudence sans s'afficher, et ajoute un treizième point d'auto-vérification
sur la transférabilité.

**Rééquilibrage après sur-correction.** Le premier rejeu a montré qu'une
interdiction en liste face à une obligation en prose produit une réponse
appauvrie : le répondant avait retiré, avec la tuyauterie, presque toutes
les sources officielles nommées et les valeurs vérifiées. Le contrat de
sortie porte désormais un **§8 de même rang que le §7** — obligation de
citer chaque texte par son intitulé, son numéro et sa date, et de
conserver les valeurs vérifiées, leur identifiant *interne* de registre
restant seul masqué — et un §9 dont le test de relecture compte deux
moitiés : ni référence qui ne parle pas au lecteur, ni fondement qu'il
doive redemander.

**Fondement de la consultation du CSA réancré sur le code.** Un juge de
rejeu a établi que le **décret n° 2020-1427 est abrogé depuis le
1er février 2025** (art. 29 du décret n° 2024-1038 du 6 novembre 2024),
ses dispositions étant codifiées dans la partie réglementaire du CGFP. Le
fondement à viser est donc l'**article R. 253-1, 1° du code général de la
fonction publique**, et non l'article 48 du décret de 2020 introduit en
v0.9.1. `instances-dialogue-social.md` §5.1 et
`assets/decision-dg-modele.md` sont corrigés, avec un avertissement sur le
véhicule. Les autres mentions du décret de 2020 dans cette branche
décrivent l'état du droit antérieur et restent à réancrer.

## v0.9.1 — 2026-08-28

**Corrections issues de la première campagne de test complète.** La
batterie `tests/TESTS.md` a été jouée intégralement pour la première
fois (15 tests, sous-agents à contexte frais, juge indépendant) et a
révélé deux défauts de fond, corrigés ici.

`instances-dialogue-social.md` §5.5 imputait à l'**article 110** du
décret n° 2020-1427 la modification du titre IV du décret n° 2003-224 au
1er janvier 2023. L'article 110 est une pure disposition d'entrée en
vigueur : la modification vient de l'**article 109** (articles 3 et 33
du décret de 2003), lui-même abrogé depuis par l'article 29 du décret
n° 2024-1038. L'article 36 reste inchangé — la CCP demeure consultée sur
les bonifications indiciaires.

`instances-dialogue-social.md` §5.1 énonçait les attributions du CSA
sans numéro d'article, lacune qui a conduit un livrable de test à viser
un « article 34 » inexistant en la matière dans le corps d'une décision
DG. Le fondement exact — **article 48, 1° du décret n° 2020-1427** — est
désormais écrit dans la branche et rappelé dans
`assets/decision-dg-modele.md`, assorti d'une règle de visa : jamais de
numéro d'article non lu en source.

Ajout du §3.0 de `SKILL.md` — critère explicite de passage de main à
`recherche-juridique` (état de vigueur, version consolidée, historique
des modificateurs, jurisprudence, mention de Légifrance) — et d'un
douzième point d'auto-vérification sur les numéros d'article.

## v0.9.0 — 2026-08-25

**Évaluation métier, confidentialité et maintenance préventive.** Ajout
de vingt scénarios réalistes couvrant les huit branches, d'une grille de
revue sémantique et d'un signalement lexical des affirmations critiques.

Ajout d'un filtre local pour les identifiants RH, d'un formulaire de
demande anonymisée, d'un contrat de sortie et de nouveaux gabarits de
tableau comparatif et FAQ interne.

Une tâche quotidienne ouvre une issue sept jours avant expiration des
sources. Les documents internes manquants sont désormais suivis par
métadonnées seulement, avec un plan de fiabilisation des cinq branches
incomplètes.

## v0.8.0 — 2026-08-25

**Fraîcheur, tests et protection de branche.** Chaque affirmation
vérifiée porte désormais `checked_on` et `max_age_days` : 30 jours pour
les élections, le budget et la déontologie ; 90 jours pour les autres
règles. Une source expirée bloque la validation.

Ajout de huit tests automatiques couvrant le projet valide, la source
absente, le domaine non officiel, la date incohérente, l'incertitude sur
une branche ✅, la branche absente, l'expiration et la date future.

La configuration reproductible de protection de `main` impose PR, CI à
jour, historique linéaire et interdit suppression et force-push.

## v0.7.0 — 2026-08-25

**Barrière automatique de fiabilisation.** Ajout de
`evals/source-gates.json`, qui inventorie les huit branches, leurs
affirmations importantes, leurs sources et leurs incertitudes
bloquantes.

Le validateur refuse désormais une branche ✅ si sa maturité diverge du
manifeste, si sa date manque, si une affirmation n'est pas vérifiée, si
elle n'a pas de source officielle reliée au registre ou si une
incertitude importante demeure. Le registre gagne les sources
contractuels, CSA, personnels ANSM et PHISP nécessaires au contrôle.
La CI vérifie en outre la réponse HTTP de toutes les URL du registre avec
`scripts/check_source_urls.py`, avec traitement explicite de la
protection anti-robot 403 de Légifrance.

## v0.6.1 — 2026-08-25

**Traçabilité renforcée sans surévaluer la maturité.** Les branches
déontologie et budget passent de ✅ à 🟢 tant que les documents ANSM 2026
mentionnés dans la copie de travail ne disposent pas d'un lien officiel
direct ou d'une copie interne contrôlée.

**Corrigé** : champ de l'article L. 124-7 du CGFP limité aux emplois
mentionnés à l'article L. 124-5 ; ajout du rapport public 2023 du
déontologue ANSM ; dotation 2026 de 143,69 M€ reliée à l'article 107 IV de
la LFSS 2026 ; autres chiffres budgétaires explicitement à confirmer.

**Bilan de maturité** : 3 branches ✅, 4 🟢, 1 🟡.

## v0.6.0 — 2026-08-25

**Fiabilisation externe et publication reproductible.** Les fichiers de
branche et les modèles sont désormais rangés dans `references/` et
`assets/`, conformément aux renvois du skill.

**Corrections de fond** :
- élections 2026 : ajout du décret n° 2025-1430 ; suppression de
  l'inférence d'un délai FPT de six mois pour les formations spécialisées
  FPE ;
- déontologie : distinction explicite entre réserves internes ANSM et
  les articles 432-12 (pendant les fonctions) et 432-13 (trois ans après
  les fonctions) du code pénal ;
- création d'un registre de sources primaires traçables, avec liens et
  règle de mise à jour.

**Ajouté** : contrôle `scripts/validate_skill.py`, évaluations de
régression, automatisation GitHub Actions, guide de contribution et
licences du contenu et des scripts.

## v0.5.1 — 2026-08-24

**Version d'audit.** Audit interne complet du skill (voir `AUDIT.md`) :
5 constats majeurs et 5 mineurs, tous de cohérence ou de structure,
aucun de droit. Tous corrigés.

**Corrigé** :
- **Frontmatter YAML** : contenait encore « délai de viduité » (erreur
  corrigée en v0.2.0) et « subvention d'État » (erreur corrigée en
  v0.5.0) ; métadonnée `statut` périmée. Description de déclenchement
  réécrite.
- **README** resté en v0.4.0 : réaligné.
- **Structure** : §5.11 de la branche recrutement replacé dans le §5 ;
  §5.6 bis de la branche QVT réordonné.
- **Toponymie** : « Vendargues » propagé aux 12 occurrences résiduelles
  de « Montpellier » (frontmatter, socle, instances, communication,
  asset).
- **Sourçage** : nature analogique (FPT) du délai de six mois des
  formations spécialisées explicitée ; décret n° 2024-1038 signalé
  comme relayé par sources secondaires, à confirmer au texte.

**Ajouté** : `AUDIT.md` (rapport complet) ; règle de méthode dans le
gabarit implicite — toute correction de fond doit être propagée par
recherche sur l'ensemble du skill, frontmatter et assets compris.

## v0.5.0 — 2026-08-24

**Correction majeure du régime de financement** et fiabilisation de la
branche budget grâce à une source jusque-là sous-exploitée.

**⚠️ Erreur corrigée** : l'ANSM était décrite comme financée par une
**subvention pour charges de service public du programme 204**. C'était
le régime **2012-2019**. Le régime actuel est une **dotation de
l'Assurance Maladie** (143,69 M€ en 2026).

**Source identifiée** : l'agence publie, après **chaque séance de son
conseil d'administration**, un **« Retour d'information »** et ses
**délibérations** — contenant budget, plafond d'emplois, programme de
travail et avis du CSA avec le détail des votes.

**Modifié** :
- `masse-salariale-budget-sirh.md` (🟢 → ✅) — historique du financement
  en trois étapes, budget initial 2026 complet, déficit et prélèvement
  sur fonds de roulement, signal social du CSA.
- `qvt-sante-travail.md` — ajout du **nouveau plan d'actions QVT/RPS en
  cours d'élaboration en 2026** ; précision des implantations
  (Vendargues) ; travaux et déménagement comme facteurs de risque.
- `socle-sources-verification.md` — entrée dédiée aux retours
  d'information du CA, signalée comme source prioritaire.
- `SKILL.md` — version, routeur, bandeau, §9.

**Données 2026 intégrées** : dotation 143,69 M€ ; ressources propres
19,38 M€ ; plafond **957 ETPT sous plafond + 77,7 hors plafond** ;
personnel 97,73 M€ ; **budget en déficit**, prélèvement de 5,51 M€ sur
le fonds de roulement ; CSA du 13 novembre 2025 : **1 voix pour,
7 abstentions**.

**Bilan de maturité** : 5 branches ✅, 2 🟢, 1 🟡.

**Reste introuvable en ligne** : délibération du CA portant cadre
d'emploi, règlement intérieur de l'agence, volet SI RH.

## v0.4.0 — 2026-08-24

**Les huit branches sont désormais traitées.** Couverture complète.

**Bilan de maturité** : 4 branches ✅ fiabilisées, 3 🟢 partielles,
1 🟡 amorcée.

**Réécrit** :
- `instances-dialogue-social.md` (🟡 → ✅) — CSA, formation spécialisée,
  CAP, CCP, représentation au CA. **Encadré d'urgence** sur les
  élections professionnelles.
- `fonctionnaires-corps-specifiques.md` (🟡 → ✅) — L. 5323-1 CSP, PHISP
  (décret n° 92-1432), techniciens sanitaires, praticiens hospitaliers,
  partage des compétences corps / agence.
- `masse-salariale-budget-sirh.md` (🟡 → 🟢) — modèle SCSP, plafond
  d'emplois, GBCP, COP 2024-2028, contrôle interne.
- `qvt-sante-travail.md` (🟡 → 🟢) — formation spécialisée obligatoire,
  décret n° 82-453, axes affichés, facteurs de risque propres à
  l'agence.
- `formation-developpement-competences.md` (🟡 → 🟢) — parcours de
  professionnalisation, GPEC, articulation formation / statut.
- `communication-interne.md` (reste 🟡) — rattachement DIRCOM / DRH,
  intranet KUSURI, contrainte multi-site, avec une note assumant
  pourquoi la branche reste faible.

**🔴 Point le plus actionnable du skill** : les **élections
professionnelles se tiennent le 10 décembre 2026** (arrêté du 2 juillet
2025). Vote électronique obligatoire en FPE, effectifs de référence au
1er janvier 2026, et échéance de juin 2026 sur les formations
spécialisées vraisemblablement dépassée. Encadré d'urgence en tête de
la branche instances.

**Autres apports structurants** :
- Formation spécialisée SSCT **obligatoire** (> 200 agents), et
  possibilité de **formations spécialisées de site** pour les
  laboratoires de Lyon et Montpellier.
- **La CCP prime sur la CAP à l'ANSM** — conséquence directe de la
  prédominance contractuelle.
- **L. 5323-1 CSP** confirme et explique la réserve structurelle sur le
  « règlement » délibéré par le CA.
- Les **PHISP sont gérés par le ministère**, pas par l'agence.
- Le **modèle de financement par SCSP** est un choix d'indépendance, à
  relier à la déontologie.

**Changement de méthode** : introduction d'un **troisième niveau de
maturité 🟢 « partiellement fiabilisée »**, documenté dans
`_gabarit-branche.md`, pour les branches dont le mécanisme est établi
mais dont les valeurs manquent. L'échelle binaire forçait une
surévaluation.

**Prochaine étape (0.5.0)** — trois documents à obtenir en interne :
1. la **délibération du CA portant cadre d'emploi** ;
2. le **règlement intérieur** de l'agence (articles 11 à 14) ;
3. les **documents budgétaires de l'année** (plafond d'emplois, SCSP).

## v0.3.0 — 2026-08-24

**Branche recrutement-classification fiabilisée** (🟡 → ✅), sur le
décret n° 2003-224 du 7 mars 2003 et ses modificatifs.

**Modifié** :
- `references/recrutement-classification-contractuels.md` — réécriture
  intégrale (412 lignes). Architecture des quatre catégories d'emploi,
  conditions de diplôme et dérogations, classement à l'échelon,
  avancement, hors-classe, mobilité inter-agences, CDD/CDI.
- `references/fonctionnaires-corps-specifiques.md` — ajout de la règle
  de classement des praticiens hospitaliers détachés (hors-classe CE1
  directe) et du fondement L. 5323-1 CSP.
- `references/socle-sources-verification.md` — décret n° 2003-224
  confirmé et détaillé ; ajout du décret n° 86-83 (subsidiaire) et des
  art. L. 5323-1 à L. 5323-3 CSP ; **clé de lecture décret /
  délibération** ajoutée au §6.2.
- `SKILL.md` — version, statut, bandeau de maturité, routeur, §9, §11.

**Découverte structurante** : le décret fixe l'**architecture** mais
renvoie **toutes les valeurs** (indices, durées d'échelon, liste des
emplois-repères, quotas de hors-classe, enveloppes de bonifications) à
des **délibérations du conseil d'administration non publiées**. Aucune
réponse chiffrée n'est donc possible sans ce document, désormais
identifié comme la **priorité n° 1 à obtenir auprès de la DRH**.

**Point sensible documenté** : le classement CE1 vs CE2 des évaluateurs
(pratique modifiée en 2017 par la DG). La question écrite Sénat
n° 23753 est **restée sans réponse** — aucune position ministérielle
n'a tranché. Le sujet est présenté comme ouvert.

**Correction répercutée** : les praticiens hospitaliers en détachement
sont classés **directement en hors-classe de la CE1** (art. 32-III),
règle absente de la maquette.

**Prochaine étape (0.4.0)** : obtenir la délibération du CA portant
cadre d'emploi, puis fiabiliser `instances-dialogue-social` — qui s'y
articule directement (la CCP est consultée sur les bonifications
indiciaires, le CA délibère sur le cadre d'emploi).

## v0.2.0 — 2026-08-24

**Branche déontologie fiabilisée** (🟡 → ✅), sur sources primaires
directement consultées.

**Modifié** :
- `references/deontologie-conflits-interets.md` — réécriture intégrale
  (487 lignes). Couvre désormais les trois populations (agents, membres
  d'instances, experts ponctuels) et les trois temps (avant / pendant /
  après les fonctions), avec circuits, délais, sanctions et
  jurisprudence ANSM sourcés.
- `references/socle-sources-verification.md` — carte des sources
  restructurée en 5 strates : textes fondateurs publiés, textes de
  déontologie sanitaire publiés, publications de l'agence, sources
  internes non publiées, doctrine.
- `references/recrutement-classification-contractuels.md` — correction
  du circuit de filtrage déontologique au recrutement.
- `SKILL.md` — version, statut, bandeau de maturité à deux régimes,
  routeur, §9 et §11.

**Quatre corrections de fond** par rapport à la v0.1.0 — détail et
sources dans `JOURNAL.md` :
1. Les **trois ans ne sont pas un délai interdisant l'embauche** d'un
   candidat issu de l'industrie, mais la durée des réserves
   d'abstention sur les dossiers de son ancien employeur.
2. Charte de déontologie en vigueur = **février 2026** (et non mai
   2020), **annexée au règlement intérieur** donc à portée
   disciplinaire.
3. Gouvernance corrigée : la **directrice de la DRD est le déontologue
   de l'ANSM** ; le **référent déontologue est nommé séparément** comme
   appui externe. Le « comité de déontologie » ne figure plus dans la
   charte 2026.
4. Périmètre des DPI publiques précisé et actualisé.

**Ajouts opérationnels** : délai de 6 mois de cession des actifs
financiers ; règle du produit concurrent (marché ≤ 3 produits) ;
dérogation permettant d'entendre un expert en conflit hors délibération
et vote ; circuit DRH → DRD au recrutement ; jurisprudence de la
Commission de déontologie propre à l'ANSM.

**Prochaine étape (0.3.0)** : fiabiliser
`recrutement-classification-contractuels` — point dur = consolidation du
décret n° 2003-224 du 7 mars 2003 (classification CE1-CE4) et grille de
rémunération associée, probablement non accessibles publiquement et à
obtenir auprès de la DRH.

## v0.1.0 — 2026-08-24

Création de la maquette initiale.

**Contexte** : construit à la demande de l'utilisateur pour une DRH
prenant ses fonctions à l'ANSM, à partir de l'architecture du skill
`drh-fpt` (même méthodologie : posture hybride, noyau de vérification,
gabarit de branche, boucle d'apprentissage). Le contenu métier est
entièrement nouveau — le droit de la fonction publique territoriale ne
s'applique pas à un établissement public de l'État.

**Créé** :
- `SKILL.md` — routeur et 12 sections adaptées de `drh-fpt`.
- `references/_gabarit-branche.md` — repris à l'identique (méthode
  indépendante du type d'employeur).
- `references/socle-sources-verification.md` — carte des sources
  propres à l'ANSM (textes publiés vs textes internes à l'agence).
- 8 branches amorcées (🟡) : recrutement-classification-contractuels,
  fonctionnaires-corps-specifiques, deontologie-conflits-interets
  (branche prioritaire), instances-dialogue-social, qvt-sante-travail,
  formation-developpement-competences, masse-salariale-budget-sirh,
  communication-interne.
- `assets/` : decision-dg-modele, note-modele, courrier-modele,
  fiche-profil-poste.

**Méthode de construction** : recherche documentaire multi-sources
(légifrance, site institutionnel ansm.sante.fr, questions parlementaires,
rapports Sénat/IGAS, organigramme officiel daté du 7 janvier 2026,
bilan social 2014-2015 — seule source chiffrée détaillée publique
identifiée). Pas encore d'itération d'usage réel ni de confirmation
directe par la DRH de l'agence.

**Connu comme non fiabilisé, à traiter en priorité pour v0.2.0** :
- Contenu consolidé du décret n° 2003-224 du 7 mars 2003 (classification
  CE1-CE4).
- Grille de rémunération actuelle par catégorie d'emploi.
- Périmètre exact et à jour des postes soumis à DPI publique.
- Contenu précis du règlement intérieur de l'ANSM (texte interne non
  publié sur Légifrance).
- Toute donnée chiffrée actuelle (effectifs par statut, budget, masse
  salariale, absentéisme) : les seuls chiffres détaillés trouvés datent
  de 2014-2015 ou de repères ponctuels 2018/2026.

**Prochaine étape suggérée** : confirmer la branche déontologie et la
branche recrutement-classification auprès de la DRH réelle de l'agence,
puis journaliser les écarts constatés dans `JOURNAL.md`.
