# Revue ciblée des sources de l'issue #19

Date de référence : **24 octobre 2026 (Europe/Paris)**.
Base examinée : `d886d5c6281be1b4075b30c7fa34060c93b700e9`.
Périmètre : trois affirmations du registre, sans audit global du skill.

## Décisions de renouvellement

| Affirmation | Résultat | Date conservée / nouvelle | Échéance |
|---|---|---|---|
| `elections-2026` | Dates et cadre général corroborés officiellement ; précision d'entrée en vigueur corrigée | 2026-10-24 | 2026-11-23 |
| `dotation-2026` | Montant légal relu directement ; limite budgétaire maintenue | 2026-10-24 | 2026-11-23 |
| `distinction-entree-pendant-sortie` | Renouvellement incomplet ; aucune nouvelle validation globale | 2026-09-24, inchangée | 2026-10-24 |

## Élections : preuves et limites

- Le [portail DGAFP](https://www.fonction-publique.gouv.fr/dialogue-social-et-representation/les-elections-professionnelles-2026), actualisé le 15 octobre, confirme les dates déjà inscrites en septembre et le vote électronique de principe en FPE.
- L'[article 2 de l'arrêté du 2 juillet 2025](https://www.legifrance.gouv.fr/jorf/article_jo/JORFARTI000051844349) est lisible séparément. Le texte intégral de l'arrêté reste bloqué ; la date générale est corroborée par la DGAFP.
- L'[article 32 du décret de codification](https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000050525120), version depuis le 20 novembre 2024, réserve les règles codifiées au renouvellement général ; les anciens décrets demeurent applicables aux scrutins antérieurs.
- L'[article 47 du décret 2025-1430](https://www.legifrance.gouv.fr/loda/id/JORFTEXT000053229755/) a été relu sur une page affichée au 14 septembre 2026. L'accès à la version demandée au 24 octobre a échoué. La [fiche DGAFP](https://www.fonction-publique.gouv.fr/dialogue-social-et-representation/les-elections-professionnelles-2026/des-mesures-de-simplification-et-dharmonisation-pour-les-elections-professionnelles-2026-et-les-instances-de-dialogue-social-dans) confirme le régime différé du chapitre Ier et le chapitre II applicable depuis le **1er janvier 2026** : correction de la date erronée du 31 décembre 2025 dans le registre.
- Aucun changement de date ou de ce cadre général depuis septembre n'a été identifié. La revue ne prouve pas l'absence de toute modification d'un article électoral ; composition, décisions et calendrier local ANSM restent à obtenir.

## Dotation : preuve directe et divergence documentaire

L'[article 107 de la LFSS](https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000053265460), version en vigueur depuis le 31 décembre 2025, a été lu intégralement. Le IV confirme **143,69 M€** ; le XIII autorise des compléments par arrêté. Aucun acte complémentaire propre à l'ANSM n'a été établi par la recherche ciblée. La réserve d'accès de septembre est levée pour la lecture de cet article, pas pour le budget entier.

Sources ANSM publiques retrouvées et lues :

- [BI 2026, délibération 2025-25 du 27 novembre 2025](https://ansm.sante.fr/uploads/2026/01/08/20251127-conseil-administration-deliberation-2025-25-budget-initial-2026.pdf), p. 1-2 ; page 1 contrôlée visuellement.
- [BR1 2026, délibération 2026-02 du 11 mars 2026](https://ansm.sante.fr/uploads/2026/05/04/20260311-ca-delib-2026-02-br1-2026.pdf), p. 1-2 ; page 1 contrôlée visuellement.
- [Retour d'information du 11 mars 2026](https://ansm.sante.fr/uploads/2026/05/04/20260311-ca-retour-information-ca-11-03-2026.pdf), p. 1 pour le contexte du BR1 et le vote du CSA.

La branche distingue désormais montant légal, prévisions des actes datés et exécution. L'écart de **4,36 M€** entre loi et dotation inscrite au BI/BR1 reste inexpliqué. La notification, les rapprochements, les éventuels rectificatifs ultérieurs et l'exécution ne sont pas établis. Le SI RH reste non documenté ; maturité `partial` conservée.

Les CP d'intervention du BI ont été corrigés. Les anciennes variations et conclusions sociales sans preuve dans les passages lus ont été retirées. La mention « loi de finances » est corrigée en « loi de financement de la sécurité sociale ».

## Déontologie : abstention de renouvellement

Des lectures historiques officielles des articles [L. 124-4](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044427774/2026-07-20), [L. 124-7](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044427766/2026-07-26) et [L. 124-8](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044427764/2026-07-20) corroborent la distinction des contrôles avant nomination et après cessation, avec des champs et circuits différents.

Les versions courantes du CGFP et la lecture intégrale exploitable des articles pénaux 432-12 et 432-13 n'ont pas toutes été obtenues. Les recherches et extraits ne remplacent pas leur lecture ; les pages historiques ne prouvent pas l'absence de modification depuis septembre. Pas de `checked_on` renouvelé. Les limites sont inscrites dans la branche et dans `known_limits`. Reprendre la vérification des versions courantes et des renvois avant de fermer ce contrôle.

## Validations

- Avant modification, `validate_skill.py --today 2026-10-24` échoue sur les deux contrôles expirés : anomalie reproduite.
- Après modification, `python scripts/validate_skill.py --today 2026-10-24` : succès.
- `python scripts/behavior_eval.py` : structure des **20 scénarios** valide ; le cas budgétaire existant exige désormais de signaler la divergence, sans en inventer la cause. Aucune campagne de réponses LLM/juges n'a été exécutée.
- `python scripts/internal_sources.py` : **10 besoins** suivis, sans contenu confidentiel ; besoin budgétaire recentré sur le rapprochement et les données courantes.
- `python -m unittest discover -s tests -v` : **51 tests réussis**. La date de référence de la suite suit cette campagne ; les durées maximales et les règles de fraîcheur sont inchangées.
- `python scripts/freshness_report.py --today 2026-10-24 --warning-days 7` : une alerte subsiste, déontologie, échéance le jour même. Elle devient expirée le 25 octobre si la vérification reste incomplète.
- Le contrôle HTTP est distinct de la lecture juridique : le script existant compte les 403 Légifrance comme protections anti-robot, sans prouver le contenu.
- `python scripts/check_source_urls.py` : code 0, **31 URL** comptabilisées (10 HTTP 200, 21 HTTP 403 Légifrance). Aucune URL réputée morte par ce script ; les 403 ne valident pas les textes.
- `git diff --check` : succès.

## Conclusion de portée

Deux renouvellements documentés ; une tentative incomplète explicitement maintenue. Les corrections recensées sont des corrections du corpus et des documents retrouvés, sans réforme nouvelle depuis septembre établie par cette revue. L'issue #19 doit rester ouverte pour la déontologie ; les réserves budgétaires restent suivies séparément dans la branche et le registre.
