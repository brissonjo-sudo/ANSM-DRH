# Audit du skill drh-ansm

> **Addendum v0.6.0 — 25 août 2026.** Une revue de publication a relevé
> une arborescence incohérente (renvois `references/` et `assets/` non
> matérialisés), l'absence de contrôle automatisé et deux corrections
> juridiques nécessaires. Les correctifs sont appliqués : registre de
> sources primaires, tests de structure, évaluations de régression et
> CI. Le constat « aucun de droit » ci-dessous est donc un constat
> historique de la revue v0.5.1, non le verdict de la version courante.

## 0. Correctifs v0.6.0

- Les élections FPE 2026 intègrent le décret n° 2025-1430 ; aucun délai
  FPT de six mois n'est désormais présenté comme applicable à l'ANSM.
- L'article 432-12 est distingué de l'article 432-13 : les restrictions
  d'un candidat entrant sont des mesures internes à confirmer, non un
  délai légal automatique de trois ans.
- La structure réelle, les liens officiels, le validateur et les cas de
  régression rendent la prochaine revue vérifiable.

**Date** : 24 août 2026 · **Version auditée** : v0.5.0 · **Version
corrigée livrée** : v0.5.1

**Méthode** : passe automatique (versions, toponymie, numérotation des
sections, renvois croisés) puis revue de contenu (frontmatter,
cohérence inter-branches, qualité du sourçage, structure des livrables).
Audit conduit comme si le skill avait été écrit par un tiers.

---

## 1. Synthèse

| Verdict | Détail |
|---------|--------|
| **Fond juridique** | Sain. Aucune erreur de droit détectée dans les branches ✅ ; les quatre erreurs de fond commises en cours de construction avaient toutes été détectées et corrigées par le processus lui-même (journalisées). |
| **Défauts trouvés par l'audit** | **5 majeurs, 5 mineurs** — tous de cohérence ou de structure, aucun de droit. **Tous corrigés en v0.5.1**, sauf deux nuances de sourçage traitées par mention explicite. |
| **Constat le plus important** | Les corrections de fond faites dans le corps du skill **n'avaient pas été répercutées dans le frontmatter YAML** — précisément la partie que Claude lit en premier pour décider d'activer le skill. |

---

## 2. Constats majeurs (tous corrigés)

### M1 — Le frontmatter contenait « délai de viduité »
L'erreur corrigée dès la v0.2.0 (les trois ans ne sont **pas** un délai
interdisant l'embauche, mais des réserves sur les dossiers de l'ancien
employeur) **subsistait dans la description de déclenchement**. Un
Claude activant le skill lisait donc d'abord l'erreur, puis sa
correction. → Description réécrite : « réserves de trois ans sur les
dossiers de l'ancien employeur ».

### M2 — Le frontmatter disait « masse salariale sur subvention d'État »
L'erreur corrigée en v0.5.0 (le financement actuel est une **dotation de
l'Assurance Maladie**, la subvention d'État étant le régime 2012-2019)
subsistait elle aussi dans la description. → Corrigé.

### M3 — Métadonnée `statut` périmée
Elle décrivait l'état v0.4.0 (« quatre branches fiabilisées, trois
partiellement ») alors que le routeur en comptait cinq. → Réécrite,
avec renvoi au présent audit.

### M4 — README resté en v0.4.0
Le tableau de maturité du README présentait la branche budget en 🟢
alors qu'elle était passée ✅. → README réaligné en v0.5.1.

### M5 — Rupture de structure dans la branche recrutement
Le §5.11 (filtrage déontologique) était placé **après** le §7
(déclencheurs de vérification), en violation de l'ordre canonique du
gabarit — conséquence d'une édition par insertion mal positionnée.
→ Bloc replacé à sa position logique, à la suite du §5.10.

---

## 3. Constats mineurs

### m1 — Toponymie incohérente (corrigé)
La correction « le troisième site est à **Vendargues (34)**, pas à
Montpellier » (v0.5.0) n'avait été portée que dans la branche QVT.
**Douze occurrences** de « Montpellier » subsistaient — dont le
frontmatter, le socle, la branche instances (pourtant ✅) et un asset.
→ Harmonisé partout ; la seule mention conservée est la citation
historique du diagnostic RPS de 2014, reformulée en « site de
l'Hérault ».

### m2 — Ordre des sections QVT (corrigé)
L'insertion par script du §5.6 bis l'avait placé après le §5.7.
→ Réordonné.

### m3 — Référence résiduelle « v0.1.0 » dans le SKILL.md (corrigé)
Le §4 (niveaux de confiance) définissait encore le régime « à
vérifier » par référence à la maquette initiale. → Reformulé par
référence à l'échelle de maturité actuelle.

### m4 — Délai des formations spécialisées : analogie FPT non signalée (traité par mention)
L'échéance « six mois avant le scrutin » citée dans l'encadré d'urgence
provient de l'article R. 251-35 du CGFP, propre à la **FPT**. La
rédaction était prudente (« calendrier type », « vraisemblablement »)
mais ne disait pas que la règle FPE exacte restait à confirmer. → La
nature analogique est désormais explicite.

### m5 — Décret n° 2024-1038 sourcé au second degré (traité par mention)
Sa qualification de « texte de référence des élections 2026 » reposait
sur des sources secondaires (prestataires de vote électronique). → La
branche signale désormais qu'il faut le confirmer au texte avant de
fonder un acte.

---

## 4. Ce que l'audit valide

- **Renvois croisés** : les 16 renvois inter-fichiers pointent tous vers
  des fichiers existants.
- **Cohérence des données transversales** : proportions
  contractuels/fonctionnaires (85-90 % / 10-15 %) identiques dans les
  quatre branches qui les citent ; effectif « de l'ordre d'un millier »
  cohérent avec le plafond 2026 (957 + 77,7 ETPT) ; les quatre erreurs
  de fond corrigées en cours de route (viduité, charte 2020→2026,
  gouvernance déontologique, financement) sont bien corrigées **dans le
  corps** de toutes les branches concernées.
- **Traçabilité** : chaque affirmation sensible est adossée à une source
  datée ; les données de 2014 sont systématiquement marquées comme
  historiques ; les niveaux de maturité par branche correspondent au
  contenu réel (aucune branche surévaluée).
- **Boucle d'apprentissage** : le JOURNAL documente les quatre erreurs
  commises et les leçons de méthode — c'est la partie du skill qui a le
  mieux fonctionné, puisque ce sont ces leçons qui ont permis les
  corrections successives.
- **Assets** : aucun contenu nominatif ; avertissements de vérification
  présents ; le gabarit de décision DG reflète le formalisme réel de
  l'agence (visa de l'avis du CSA).
- **Empaquetage** : validation `skill-creator` passée à chaque version.

---

## 5. Faiblesses résiduelles assumées (hors périmètre de correction)

1. **Trois documents internes manquants** — délibération du CA portant
   cadre d'emploi, règlement intérieur (art. 11-14), volet SI RH. Le
   skill le dit partout où c'est pertinent ; rien de plus n'est possible
   sans apport interne.
2. **Branche communication interne en 🟡** — assumé et documenté
   (§12 de la branche).
3. **Compétence CCP / avancement après la réforme de 2023** — signalée
   « à vérifier » ; le texte consolidé de l'article 36 du décret
   n° 2003-224 postérieur au 1er janvier 2023 n'a pas été contrôlé
   article par article.
4. **Composition du CA (trois représentants du personnel)** — reprise de
   la recherche initiale sur le décret n° 2012-597 ; à recontrôler en
   version consolidée lors du premier usage sur ce sujet.
5. **Risque structurel du skill** : sa valeur décroît avec le temps
   (budget annuel, élections, textes modifiés). Le mécanisme de parade
   existe — dates de vérification en métadonnées, réflexe « retour
   d'information du dernier CA », déclencheurs de vérification — mais il
   suppose d'être appliqué.

---

## 6. Leçon de méthode consignée

Le défaut transversal de cet audit est un **défaut de propagation** :
chaque correction de fond a bien été appliquée là où l'erreur avait été
découverte, mais pas systématiquement dans **tous** les fichiers qui
répétaient l'information (frontmatter, README, branches voisines,
assets). Trois des cinq constats majeurs en découlent.

**Règle ajoutée à la méthode** : toute correction de fond doit être
suivie d'un `grep` de l'information erronée sur **l'ensemble** du skill
— frontmatter et assets compris — avant d'être considérée comme close.
C'est ce que cet audit a fait a posteriori ; c'est ce que les prochaines
corrections feront a priori.
