# Plan de fiabilisation des branches incomplètes

> Objectif : obtenir les preuves manquantes sans déposer de document RH
> confidentiel dans Git. Le dépôt conserve uniquement métadonnées,
> statut de revue et identifiant interne non sensible.

## Priorités

| Ordre | Branche | Documents à obtenir | Critère de passage |
|---:|---|---|---|
| 1 | Déontologie | règlement intérieur à jour ; procédure interne de prévention et gestion des conflits ; charte 2026 | version, autorité d'approbation, date d'effet et circuit opérationnel confirmés |
| 2 | Masse salariale / SI RH | budget initial et rectificatifs 2026 ; plafond d'emplois ; cartographie fonctionnelle SI RH | chiffres rapprochés du CA et périmètre de chaque donnée documenté |
| 3 | QVT / santé | accord ou décision télétravail ; DUERP ; plan QVT/RPS ; organisation de la médecine de prévention | document en vigueur et responsables/canaux internes confirmés |
| 4 | Formation | plan et budget 2026 ; référentiel métiers ; règles CPF et entretien professionnel | période, population et articulation avec les emplois-repères établies |
| 5 | Communication | circuit DIRCOM/DRH/DG ; inventaire des canaux ; règles multi-site ; kit d'accueil | propriétaire, validation, audience et fréquence de mise à jour confirmés |

## Méthode d'intégration

1. Recevoir le document dans l'espace interne autorisé, jamais dans ce
   dépôt.
2. Vérifier titre, version, date d'effet, autorité, périmètre et statut
   d'abrogation.
3. Calculer une empreinte SHA-256 dans l'espace sécurisé si la politique
   interne l'autorise.
4. Reporter uniquement les métadonnées non sensibles dans le registre de
   suivi.
5. Extraire les affirmations utiles dans la branche avec mention
   explicite « source interne ».
6. Ajouter la preuve à `evals/source-gates.json` seulement si une URL
   officielle existe ; sinon conserver la branche 🟢 et documenter la
   limite.
7. Rejouer les scénarios comportementaux concernés.

## Règles de décision

- Une procédure non datée ou sans autorité identifiable ne fiabilise pas
  une branche.
- Une capture d'écran ou un courriel isolé ne vaut pas doctrine interne.
- Une donnée chiffrée doit porter période, unité, périmètre et date
  d'extraction.
- Une branche ne devient ✅ que si ses affirmations importantes sont
  traçables et si aucun point bloquant ne reste non résolu.

Le détail des pièces attendues est suivi dans
`evals/internal-source-requirements.json`.
