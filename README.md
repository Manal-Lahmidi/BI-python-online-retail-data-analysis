# Analyse des Ventes au Détail – Impact des Campagnes Marketing et Comparaison des Performances

## Description
Ce projet d'**informatique décisionnelle** vise à analyser les données de ventes au détail entre 2009 et 2010 afin d'identifier des tendances clés, d'évaluer les performances des campagnes marketing, et de proposer des stratégies pour optimiser les ventes et la gestion des stocks.

---

## Objectifs
- Étudier les **revenus mensuels** pour identifier les tendances et saisonnalités.
- Identifier les **produits les plus populaires** pour optimiser les stocks.
- Analyser la **répartition géographique des revenus** pour cibler les efforts marketing.
- Évaluer le **panier moyen** pour optimiser les stratégies commerciales.

---

## Données
- **Source** : [Online Retail Dataset](https://www.kaggle.com/datasets/lakshmi25npathi/online-retail-dataset?resource=download)
- **Format** : Fichier Excel (`online_retail_II.xlsx`)
- **Contenu** : Transactions de vente au détail couvrant les années 2009 et 2010.

---

## Outils et Technologies
- **Python** : Extraction, transformation, chargement (ETL), analyse et visualisation des données.
- Bibliothèques utilisées :
  - **Pandas** pour la manipulation des données
  - **Matplotlib** et **Seaborn** pour la visualisation
  - **OpenPyXL** pour le traitement des fichiers Excel

---

## Méthodologie
1. **Extraction des Données** : Importation des données brutes depuis le fichier source.
2. **Transformation des Données** :
   - Nettoyage des données : normalisation des formats de dates, suppression des doublons, gestion des valeurs manquantes.
   - Transformation des données pour faciliter l'analyse.
3. **Chargement des Données** : Export des données nettoyées dans un fichier `Cleaned_RetailData.xlsx`.
4. **Analyse et Visualisation** :
   - **Revenus mensuels** : Identification des tendances saisonnières.
   - **Produits populaires** : Détection des articles les plus vendus.
   - **Répartition géographique** : Analyse des performances par pays.
   - **Panier moyen** : Évaluation des commandes pour optimiser les ventes.

---

## Résultats Clés
- **Tendances saisonnières** : Les revenus augmentent significativement en fin d'année (novembre-décembre).
- **Produits populaires** : Concentration des ventes sur un top 10 de produits, avec le "WHITE HANGING HEART T-LIGHT HOLDER" en tête.
- **Répartition géographique** : Le Royaume-Uni domine les ventes, suivi par l'Irlande et les Pays-Bas.
- **Panier moyen** : Environ 457,93 €, avec des opportunités pour augmenter cette valeur via des promotions ou des stratégies de fidélisation.

---

## Décisions Stratégiques
- Renforcer les campagnes marketing en fin d'année.
- Réapprovisionner les produits populaires pour éviter les ruptures.
- Cibler les marchés rentables comme le Royaume-Uni et explorer les marchés émergents.
- Proposer des promotions ciblées pour augmenter la valeur du panier moyen.

---

## Références
- [Dataset Kaggle](https://www.kaggle.com/datasets/lakshmi25npathi/online-retail-dataset?resource=download)
- [ETL avec Python - Saras Analytics](https://sarasanalytics.com/blog/etl-using-python/)
- [ETL avec Python - Astera](https://www.astera.com/fr/type/blog/etl-using-python/)

---

## Auteurs
- **Manal Lahmidi**

### Encadré par :
- **Mr. Brahim Erraha**

---


