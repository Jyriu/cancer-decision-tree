# Projet de Classification du Cancer du Sein

Ce projet a pour objectif de classifier les tumeurs du sein comme étant **bénignes** ou **malignes** en utilisant un **classifieur par arbre de décision**. Le dataset utilisé est le **Breast Cancer Wisconsin Dataset**, qui contient diverses caractéristiques dérivées d'images cellulaires afin de prédire la nature de la tumeur.

## Dataset
- Le dataset contient des mesures des noyaux cellulaires à partir d'images de masses mammaires.
- Il inclut des caractéristiques telles que le **rayon moyen**, la **texture moyenne**, le **périmètre moyen**, la **concavité la plus marquée**, etc.
- La variable cible (`benign_0__mal_1`) indique si une tumeur est bénigne (`0`) ou maligne (`1`).

## Vue d'ensemble du projet
1. **Préparation des données** : Le dataset a été chargé et les caractéristiques ont été séparées de la variable cible. Il n'y avait aucune valeur manquante à gérer, donc les données étaient prêtes à être utilisées.
2. **Entraînement du modèle** : Un **classifieur par arbre de décision** a été entraîné sur les données pour prédire la variable cible. Le dataset a été divisé en ensembles d'entraînement (80%) et de test (20%).
3. **Évaluation** : Le modèle a atteint une précision d'environ **94,7%** sur l'ensemble de test. Les métriques utilisées pour l'évaluation incluaient la **matrice de confusion** et le **rapport de classification**.
4. **Visualisation** : L'arbre de décision entraîné a été visualisé afin de comprendre les chemins de décision et les critères utilisés pour classifier les tumeurs.

## Comment exécuter le projet
1. Cloner le dépôt :
   ```bash
   git clone https://github.com/your-username/your-repo.git
   ```
2. Installer les bibliothèques requises :
   ```bash
   pip install -r requirements.txt
   ```
3. Exécuter le script :
   ```bash
   python breast_cancer_classification.py
   ```

## Dépendances
- **Python** (version 3.x)
- **Pandas** pour la manipulation des données
- **Scikit-learn** pour la modélisation en apprentissage automatique
- **Matplotlib** pour la visualisation

## Résultats
- Le modèle d'arbre de décision a atteint de bonnes performances avec une précision de **94,7%**.
- La visualisation de l'arbre de décision fournit une vue facile à comprendre de la manière dont le modèle prend ses décisions en fonction des caractéristiques.

## Licence
Ce projet est uniquement à des fins éducatives.

