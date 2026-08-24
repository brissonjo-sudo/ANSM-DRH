# Protocole de forward-testing

## Objectif

Vérifier une réponse réellement produite, pas seulement la présence de
fichiers ou de mots-clés. L'évaluateur doit être distinct de la passe
ayant généré la réponse lorsque l'enjeu le justifie.

## Échantillon minimal

Après une modification de fond, rejouer :

1. tous les cas de la branche modifiée ;
2. au moins un cas inter-branches ;
3. au moins un cas sensible ;
4. un cas qui exige une abstention ou une pièce interne.

Avant une version majeure, rejouer les vingt cas.

## Procédure

1. Fournir au générateur le skill et le prompt du cas, sans lui révéler
   les critères ni les formulations interdites.
2. Enregistrer la réponse dans un fichier temporaire hors du dépôt si
   elle contient des faits réels.
3. Préparer la grille :

   ```text
   python scripts/behavior_eval.py --case <id> --response <fichier>
   ```

4. Confirmer que les branches réellement mobilisées correspondent à la
   liste du scénario.
5. Évaluer chaque critère sur le sens : `pass`, `fail` ou `not_applicable`,
   avec une justification courte.
6. Échouer le cas si une affirmation interdite est détectée, si un
   critère critique échoue ou si une donnée personnelle inutile apparaît.

## Résultat à consigner

- identifiant du cas et version du skill ;
- date et modèle/générateur utilisé ;
- résultat automatique ;
- résultat de chaque critère critique ;
- branches réellement utilisées ;
- défaut observé et correction décidée.

Ne jamais consigner la réponse brute d'un dossier réel dans Git. Pour un
cas issu de la pratique, créer un scénario synthétique anonymisé qui
reproduit uniquement le mécanisme ayant provoqué l'erreur.

## Limite

Une réussite lexicale ne démontre pas la justesse juridique. Pour une
règle engageante, l'évaluateur doit contrôler la source primaire dans sa
version en vigueur à la date du test.
