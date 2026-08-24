# Protection des données dans les demandes RH

## Repérage rapide

- Filtre d'entrée : §1
- Données à retirer : §2
- Situations sensibles : §3
- Restitution et conservation : §§4–5

## 1. Filtre d'entrée

Avant de lire ou reformuler un cas individuel :

1. demander une version pseudonymisée si des identifiants apparaissent ;
2. conserver uniquement les faits nécessaires à la question ;
3. ne pas demander un document complet si un extrait anonymisé suffit ;
4. traiter séparément le fond juridique et l'identité de l'agent.

Le script local `scripts/privacy_scan.py` repère courriels, téléphones,
IBAN, NIR et matricules structurés. Il s'agit d'un filet de sécurité : il
ne détecte pas de façon fiable les noms, adresses libres ou situations
permettant une réidentification indirecte.

## 2. Données à retirer

- nom, prénom, initiales rares ou photographie ;
- coordonnées personnelles ;
- NIR, matricule, IBAN et signature ;
- adresse précise ou date de naissance complète ;
- diagnostic, traitement ou pièce médicale ;
- détail disciplinaire sans lien avec la question ;
- combinaison unique de fonction, site et événement permettant
  d'identifier l'agent.

Employer `[AGENT A]`, `[MANAGER B]`, des dates relatives et des tranches
d'ancienneté lorsque la précision exacte n'est pas utile.

## 3. Santé, discipline, alerte et déontologie

- **Santé** : ne pas diagnostiquer ; orienter vers le canal confidentiel
  compétent et ne reprendre que l'impact professionnel nécessaire.
- **Discipline ou harcèlement** : ne pas conclure sur les faits ;
  distinguer signalement, instruction contradictoire et décision.
- **Alerte** : ne pas exposer l'identité du lanceur d'alerte ou des
  personnes citées dans une réponse générale.
- **Déontologie** : décrire fonctions, dossiers et liens d'intérêts sans
  publier le patrimoine ou les coordonnées de l'agent.

## 4. Règle de sortie

Un livrable de travail doit utiliser des champs neutres. La version
nominative est complétée uniquement dans le système RH autorisé, par la
personne habilitée. Ne jamais placer de données réelles dans un gabarit,
un scénario d'évaluation, le journal du skill ou le dépôt Git.

## 5. Conservation

Le skill ne définit pas de durée de conservation et ne remplace pas la
politique interne de l'ANSM. Si la conservation, le partage ou la base
légale du traitement est en cause, suspendre la diffusion et saisir les
acteurs internes compétents.
