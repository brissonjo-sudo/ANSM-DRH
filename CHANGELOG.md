# Changelog — drh-ansm

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
