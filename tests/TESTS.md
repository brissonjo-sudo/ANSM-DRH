# Batterie de tests — skill drh-ansm (v0.9.3)

**Objet** : valider le déclenchement, l'exactitude des branches ✅, la
retenue des branches 🟢/🟡, et les coactivations avec
`recherche-juridique` et `dpo-ct`.

**Méthode** : poser chaque question **telle quelle**, dans une
conversation neuve, sans contexte préalable. Noter chaque test
**RÉUSSI / PARTIEL / ÉCHOUÉ** selon les critères indiqués. Un test est
ÉCHOUÉ dès qu'un critère d'échec est constaté, même si le reste est bon.

**Ordre conseillé** : tel que numéroté (du déclenchement vers les cas
complexes).

---

## Bloc A — Déclenchement (2 tests)

### T01 — Contrôle négatif : question FPT
> « Quelles sont les règles d'avancement de grade d'un brigadier-chef
> principal de police municipale ? »

- **Attendu** : `drh-ansm` **ne s'active pas** (c'est le champ de
  `dpm-fpt`/`drh-fpt`). Aucune référence aux catégories CE1-CE4.
- **Échec si** : le skill s'active ou si des notions ANSM contaminent la
  réponse.

### T02 — Contrôle positif : question ANSM générique
> « Mon amie devient DRH de l'ANSM. Quelles sont les spécificités du
> statut du personnel de cette agence ? »

- **Attendu** : activation ; réponse structurée autour de L. 5323-1 CSP,
  de la prédominance contractuelle (85-90 %) et du décret n° 2003-224 ;
  mention de la réserve « valeurs fixées par délibération du CA non
  publiée ».
- **Échec si** : transposition FPT (catégories A/B/C présentées comme le
  cadre applicable, RIFSEEP, CST...).

---

## Bloc B — Branches fiabilisées : exactitude assertive (5 tests)

### T03 — Le piège fondateur : candidat issu de l'industrie
> « On veut recruter comme évaluatrice une pharmacienne qui sort de
> chez Sanofi. C'est interdit pendant 3 ans, non ? »

- **Attendu** : correction ferme du présupposé — l'embauche est
  **possible** ; les 3 ans (art. 432-12 CP) fondent des **réserves
  d'abstention sur les dossiers de l'ancien employeur**, notifiées via
  la **promesse d'embauche** après analyse DRH → DRD.
- **Échec si** : la réponse valide le « délai de viduité » interdisant
  le recrutement. *(C'est l'erreur que le skill a lui-même commise en
  v0.1.0 — le test vérifie que la correction tient.)*

### T04 — Classement d'un praticien hospitalier détaché
> « Un PH arrive en détachement à l'ANSM. On le classe à quel échelon
> de la classe normale ? »

- **Attendu** : correction du présupposé — classement **direct en
  hors-classe de la CE1** (décret n° 2003-224, art. 32-III), sans
  passage par la classe normale.
- **Échec si** : calcul de reprise d'ancienneté en classe normale.

### T05 — Refus de chiffrer sans la délibération du CA
> « Donne-moi l'indice majoré et le salaire brut d'un CE2 au
> 5e échelon. »

- **Attendu** : **abstention chiffrée explicite** — architecture
  expliquée, mais indices et durées renvoyés à la **délibération du CA
  portant cadre d'emploi, non publiée** ; proposition d'obtenir le
  document (interne ou CRPA).
- **Échec si** : un montant ou un indice est produit, même « estimé ».

### T06 — Périmètre exact de la CCP en discipline
> « On envisage une exclusion temporaire de 2 jours contre un agent
> contractuel. Il faut convoquer la CCP avant, n'est-ce pas ? »

- **Attendu** : non — l'exclusion **≤ 3 jours** est hors consultation
  obligatoire (art. 1-2, décret n° 86-83) ; rappel du reste de la
  procédure disciplinaire (droits de la défense) et du rôle central de
  la CCP à l'ANSM pour les sanctions plus lourdes.
- **Échec si** : consultation CCP présentée comme obligatoire ici, ou
  confusion CAP/CCP.

### T07 — Régime de financement : les trois époques
> « L'ANSM est bien financée par les taxes payées par les laboratoires
> pharmaceutiques ? »

- **Attendu** : correction en trois temps — industrie (avant 2012),
  SCSP programme 204 (2012-2019), **dotation de l'Assurance Maladie
  (régime actuel, 143,69 M€ au BI 2026)** ; lien avec l'indépendance.
- **Échec si** : la réponse s'arrête au régime 2012-2019 (l'erreur
  corrigée en v0.5.0).

---

## Bloc C — Sujets sensibles et urgences (3 tests)

### T08 — Sujet non tranché : CE1/CE2 des évaluateurs
> « Les évaluateurs recrutés en CE2 depuis 2017 doivent-ils être
> reclassés en CE1 ? »

- **Attendu** : présentation **équilibrée et non tranchée** — pratique
  DG depuis 2017, question Sénat n° 23753 **caduque sans réponse**,
  arbitrage de politique RH interne via la liste des emplois-repères.
- **Échec si** : la pratique est présentée comme illégale **ou** comme
  validée.

### T09 — Réflexe calendaire : élections professionnelles
> « Quels sont les chantiers RH prioritaires pour une prise de poste à
> l'ANSM en septembre 2026 ? »

- **Attendu** : les **élections du 10 décembre 2026** arrivent en tête
  (vote électronique obligatoire FPE, effectifs au 01/01/2026, échéance
  formations spécialisées vraisemblablement dépassée), avant les
  chantiers de fond.
- **Échec si** : les élections sont absentes ou noyées en fin de liste.

### T10 — Branche 🟢 : conditionnel borné sur le télétravail
> « Combien de jours de télétravail par semaine à l'ANSM ? »

- **Attendu** : pas de chiffre inventé — politique affichée
  (« télétravail étendu ») citée comme déclarative, renvoi au **texte
  interne à obtenir** ; éventuellement cadre FPE général clairement
  distingué de la règle locale.
- **Échec si** : un quota précis est affirmé comme règle ANSM.

---

## Bloc D — Coactivation `recherche-juridique` (2 tests)

### T11 — Point marqué « à vérifier » : CCP et bonifications
> « Vérifie sur Légifrance si la CCP de l'ANSM est toujours consultée
> sur les bonifications indiciaires depuis la réforme de 2023. »

- **Attendu** : coactivation ; consultation de l'**art. 36 du décret
  n° 2003-224 en version consolidée** (effet art. 110 du décret
  n° 2020-1427 au 01/01/2023) ; réponse sourcée avec état de vigueur —
  et mise à jour du raisonnement si l'avis CCP a disparu.
- **Échec si** : réponse de mémoire sans vérification de la version
  consolidée, ou source secondaire seule.

### T12 — Texte récent : décret n° 2025-697 (PHISP)
> « Qu'est-ce que le décret du 25 juillet 2025 change au statut des
> pharmaciens inspecteurs de santé publique ? »

- **Attendu** : coactivation ; lecture du décret n° 2025-697 sur source
  officielle ; rappel que les PHISP restent **gérés par le ministère**
  (l'ANSM est affectataire).
- **Échec si** : contenu du décret inventé ou non sourcé.

---

## Bloc E — Coactivation `dpo-ct` (2 tests)

*(`dpo-ct` est conçu pour les collectivités : le test vérifie aussi
qu'il sait raisonner RGPD hors de ce périmètre sans transposer à tort —
ou qu'il passe la main proprement.)*

### T13 — DPI publiées et données personnelles
> « Les déclarations d'intérêts de plus de 600 agents de l'ANSM sont
> publiées en ligne. Quelles précautions RGPD pour la DRH ? »

- **Attendu** : croisement correct — base légale (obligation légale,
  art. L. 1451-1 CSP), **exclusion des liens de parenté de la
  publication**, occultation vie privée en cas de communication CADA,
  minimisation, information des agents, durées de publication à
  vérifier.
- **Échec si** : la publication est présentée comme illicite, ou le
  RGPD comme y faisant obstacle (l'obligation légale spéciale prime).

### T14 — Vote électronique : traitement à risque
> « Pour les élections professionnelles de décembre 2026 en vote
> électronique, qu'est-ce que la DRH doit prévoir côté protection des
> données ? »

- **Attendu** : qualification en traitement à risque élevé → **AIPD**,
  recommandations CNIL sur le vote électronique, contrat de
  sous-traitance art. 28 avec le prestataire, sécurité/scellement,
  information des électeurs, association du DPO de l'agence — articulé
  avec le calendrier serré du 10/12/2026.
- **Échec si** : aucun réflexe AIPD/CNIL, ou calendrier ignoré.

---

## Bloc F — Livrable de bout en bout (1 test)

### T15 — Décision DG complète
> « Rédige la décision DG actant une réorganisation de la DRH de
> l'ANSM en quatre pôles, après l'avis du CSA rendu le 15 septembre
> 2026. »

- **Attendu** : utilisation du gabarit — visas corrects (CSP livre III,
  décret n° 2012-597, décision d'organisation en vigueur), **visa
  explicite de l'avis du CSA du 15/09/2026**, articles numérotés, date
  d'effet, signature DG ; avertissement de vérification des visas en
  version consolidée.
- **Échec si** : forme d'arrêté territorial, absence du visa CSA, ou
  visas inventés sans réserve.

---

## Grille de synthèse

| Test | Bloc | Cible principale | Résultat |
|------|------|------------------|----------|
| T01 | A | Non-activation FPT | PARTIEL ⚠️ |
| T02 | A | Activation + cadrage EPA | RÉUSSI |
| T03 | B | Piège « viduité » | RÉUSSI |
| T04 | B | PH → hors-classe CE1 | RÉUSSI |
| T05 | B | Abstention chiffrée | RÉUSSI |
| T06 | B | Périmètre CCP | RÉUSSI |
| T07 | B | Financement (3 régimes) | RÉUSSI |
| T08 | C | Neutralité CE1/CE2 | RÉUSSI |
| T09 | C | Urgence électorale | RÉUSSI |
| T10 | C | Conditionnel borné 🟢 | RÉUSSI |
| T11 | D | Vérification consolidée | PARTIEL ⚠️ → **RÉUSSI** (rejeu) |
| T12 | D | Texte récent sourcé | RÉUSSI |
| T13 | E | DPI × RGPD | RÉUSSI |
| T14 | E | AIPD vote électronique | RÉUSSI |
| T15 | F | Livrable décision DG | ÉCHOUÉ ❌ → **RÉUSSI** (rejeu) |

**Campagne du 28 août 2026** (skill v0.9.0) : 12 RÉUSSI, 2 PARTIEL,
1 ÉCHOUÉ. Les quatre tests d'innocuité sont réussis et le total atteint le
seuil. Détail, défauts et corrections à porter →
`tests/rapports/RAPPORT-2026-08-28.md`.

**Rejeu du 28 août 2026 après correction** (skill v0.9.1) : T11 et T15
rejoués sur sous-agents neufs, tous deux **RÉUSSI**. Le compte passe à
**14 RÉUSSI, 1 PARTIEL, 0 ÉCHOUÉ** — le PARTIEL résiduel étant T01, dont
le critère propre (non-activation de `drh-ansm`) est satisfait, la réserve
portant sur `drh-fpt`, hors de ce dépôt. Détail →
`tests/rapports/RAPPORT-2026-08-28-rejeu.md`.

**Rejeu de forme du 28 août 2026** (skill v0.9.2) : T05, T09 et T15 rejoués
après correction du défaut de forme transverse (exposition de la mécanique
interne). Les trois restent **RÉUSSI** sur le fond, la forme passe de
non conforme à conforme ou à résidus mineurs. Le rejeu a mis au jour un
défaut de fond hors grille — un visa reposant sur un décret abrogé —
corrigé depuis. Détail → `tests/rapports/RAPPORT-2026-08-28-forme.md`.

**Rejeu de réancrage du 28 août 2026** (skill v0.9.3) : T06, T10 et T15
rejoués après reprise de toutes les mentions des textes abrogés au
1er février 2025 par la codification au code général de la fonction
publique. Les trois sont **RÉUSSI** sur le fond ; T15 décroche pour la
première fois fond et forme. Détail →
`tests/rapports/RAPPORT-2026-08-28-codification.md`.

**Seuil de mise en service suggéré** : 100 % de réussite sur T03, T05,
T08 et T10 (ce sont les tests d'*innocuité* — une erreur y produit un
acte fautif), et ≥ 12/15 au total. Tout échec s'inscrit au JOURNAL du
skill avec sa correction, conformément à la boucle d'apprentissage.
