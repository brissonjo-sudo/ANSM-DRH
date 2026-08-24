# Gabarit décisionnel des branches

> Méta-document (instructions de conception, pas de contenu métier). Toute
> branche de `references/` suit **exactement** cette structure, dans cet ordre.
> Objectif : une écriture interprétable par le modèle, orientée **décision**
> plutôt que description. Repris à l'identique de `drh-fpt` — la méthode ne
> dépend pas du type d'employeur public.

## Structure imposée d'une branche

1. **Bandeau de maturité** — trois niveaux possibles :
   - ✅ **fiabilisée** — adossée à des sources primaires directement
     consultées ; utilisable en mode assertif. Lister les sources en
     tête, et ce qui reste à obtenir en interne.
   - 🟢 **partiellement fiabilisée** — le **mécanisme** est établi sur
     source primaire, mais les **valeurs** ou le **dispositif interne**
     manquent. Séparer explicitement « ce qui est solide » et « ce qui
     manque ».
   - 🟡 **amorcée** — repères structurels seulement. Dire pourquoi, et
     quelles questions poser pour la faire progresser.

   Ne jamais surévaluer une branche : une branche annoncée fiabilisée
   qui ne l'est pas est plus dangereuse qu'une branche honnêtement
   marquée 🟡.
2. **Périmètre** — ce que couvre la branche, en deux phrases.
3. **Questions couvertes** — les familles de questions typiques (liste courte).
4. **Arbre de traitement** — le réflexe de raisonnement :
   `question → variables à lever → décision → vérification → livrable`.
5. **Variables à lever** — catégorie de personnel, pôle, site, exposition
   déontologique : paramètres propres à la branche, à clarifier avant de
   trancher.
6. **Règles métier** — le fond, par sous-domaine. Distinguer toujours :
   fonctionnaire / contractuel / expert externe ; national / interne à
   l'agence ; obligation / faculté.
7. **Calculs** (si la branche en comporte) — méthode imposée :
   - annoncer les **hypothèses** ;
   - **demander** les données manquantes ;
   - séparer **données connues** et **estimées** ;
   - signaler les **valeurs volatiles** à vérifier.
8. **Déclencheurs de vérification** — les points qui imposent le noyau de
   vérification (matrice §2.2 du SKILL.md).
9. **Pièges & confusions fréquentes** — en particulier les réflexes hérités
   d'une autre fonction publique (FPT, FPH) à ne pas transposer tels quels.
10. **Données volatiles à vérifier** — valeurs à ne jamais donner de mémoire.
11. **Livrables** — classés par niveau (décision / organisation / pilotage /
    communication), au format ANSM (décision DG, pas arrêté/délibération).
12. **Niveau de confiance** — repères stable / à vérifier / débattu pour la
    branche.
13. **Checklist de branche** — contrôles spécifiques avant sortie.

## Règles d'écriture

- Impératif, phrases courtes, une idée par point.
- Distinguer systématiquement **texte publié** (Légifrance, code de la
  santé publique) et **texte interne à l'ANSM** (règlement intérieur,
  procédures, décisions DG non codifiées) — voir socle §1.
- Citer les **références structurelles stables** (codes, numéros de
  décrets fondateurs) en rappelant la vérification de version.
- Pas d'instruction de méta-conception dans le corps métier : elle reste
  ici.
