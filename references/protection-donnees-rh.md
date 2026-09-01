# Protection des données dans les demandes RH

> **Portée de ce fichier** : l'**hygiène** des données personnelles dans
> les échanges — ce qu'on retire d'une demande avant de la traiter. Ce
> n'est **pas** une branche de conformité RGPD : ce référentiel n'en a
> pas.
>
> Pour une question de **conformité** — AIPD, registre des traitements,
> violation et notification CNIL à 72 heures, sous-traitance (art. 28),
> droits des personnes, sécurité (art. 32), doctrine CNIL — **activer le
> skill `dpo-ct`** et lui emprunter sa méthode. Écarter sa référence
> `secteur-collectivites.md` et toute règle propre aux collectivités
> (délibération d'un conseil municipal, DPO mutualisé, centre de
> gestion) : à l'ANSM, le responsable de traitement est **l'agence**,
> établissement public de l'État, et le **DPO est celui de l'agence** —
> l'associer systématiquement. Voir `SKILL.md` §3.0 bis.

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

Le script renvoie le code `1` lorsqu'un identifiant direct est détecté
et `2` pour un risque élevé ; un simple contexte sensible non identifié
reste un avertissement de code `0`.

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
