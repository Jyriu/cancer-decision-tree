# Projet de Classification du Cancer du Sein

Ce projet vise à classifier des tumeurs du sein en **bénignes** ou **malignes** en utilisant un **arbre de décision**. Le dataset utilisé est le **Breast Cancer Wisconsin Dataset**, qui contient diverses caractéristiques dérivées d'images cellulaires pour aider à prédire la nature de la tumeur.

## Aperçu du Projet

![Arbre de Décision](/decision_tree_visual.png)

L'image ci-dessus montre l'arbre de décision entraîné pour classer les tumeurs en bénignes ou malignes. Les nœuds représentent les différentes décisions prises en fonction des caractéristiques des tumeurs, et les couleurs indiquent la classe prédite. Voici quelques détails pour mieux comprendre l'arbre de décision :

- **Noeuds et décisions** : Chaque nœud représente une question posée sur une caractéristique de la tumeur (par exemple, `mean concave points <= 0.051`). En fonction de la réponse, l'arbre dirige l'échantillon vers la gauche ou vers la droite pour poursuivre le processus de classification.
- **Valeur `gini`** : Le coefficient de **Gini** est une mesure d'impureté qui indique à quel point les échantillons dans un nœud appartiennent à la même classe. Un **gini** de 0 signifie que tous les échantillons sont de la même classe (bénignes ou malignes), tandis qu'une valeur plus élevée indique une diversité des classes.
- **Échantillons (`samples`)** : Indique le nombre total d'échantillons à chaque nœud. Cela permet de voir combien de données sont en jeu à chaque étape de la décision.
- **Valeurs (`value`)** : Affiche la répartition des classes dans chaque nœud (`[bénignes, malignes]`). Par exemple, `value = [169, 286]` signifie qu'il y a 169 tumeurs bénignes et 286 malignes à ce point précis, ce qui montre la prédominance d'une classe sur l'autre.
- **Couleurs des nœuds** : Les nœuds en **bleu** indiquent une prédiction de tumeur maligne, tandis que les nœuds en **orange** indiquent une prédiction de tumeur bénigne. La saturation de la couleur montre la pureté de la prédiction (plus la couleur est saturée, plus le nœud est pur).
- **Chemins de décision** : Les caractéristiques les plus importantes apparaissent en haut de l'arbre. Cela signifie que ces caractéristiques ont un fort pouvoir discriminant. Par exemple, `mean concave points` est souvent la première caractéristique examinée, car elle est très efficace pour séparer les tumeurs bénignes des malignes.

## Dataset
Le **Breast Cancer Wisconsin Dataset** est constitué de mesures des noyaux cellulaires à partir d'images de masses mammaires. Voici quelques détails sur les caractéristiques disponibles :
- **Rayon moyen** (`mean radius`) : la moyenne des distances du centre au périmètre du noyau.
- **Texture moyenne** (`mean texture`) : écart-type des valeurs des niveaux de gris.
- **Périmètre moyen** (`mean perimeter`) : la longueur totale du périmètre.
- **Concavité** (`concavity`) : la sévérité des indentations des contours.
- La variable cible (`benign_0__mal_1`) indique si une tumeur est bénigne (`0`) ou maligne (`1`).

## Vue d'ensemble du projet
1. **Préparation des données** : Chargement du dataset, vérification des valeurs manquantes (aucune dans ce cas), et séparation des caractéristiques de la variable cible.
2. **Entraînement du modèle** : Utilisation de l'**arbre de décision** sur les données, avec une division entre l'ensemble d'entraînement (80%) et l'ensemble de test (20%). L'arbre est entraîné pour identifier les caractéristiques les plus discriminantes afin de séparer les tumeurs bénignes des malignes.
3. **Évaluation du modèle** : Le modèle a atteint une **précision** d'environ **94,7%** sur l'ensemble de test. Cela signifie que 94,7% des prédictions étaient correctes.
4. **Visualisation de l'arbre de décision** : L'arbre de décision a été visualisé pour mieux comprendre les critères de classification. Cette visualisation est essentielle pour interpréter les décisions du modèle et garantir que les critères de séparation sont logiques et compréhensibles.

## Interprétation des résultats
- Le modèle a montré une précision élevée, ce qui signifie qu'il est capable de classer les tumeurs avec un haut niveau de fiabilité.
- Les caractéristiques les plus importantes pour la classification sont celles qui apparaissent en haut de l'arbre de décision. Ces caractéristiques permettent de prendre des décisions très tôt dans l'arbre, réduisant ainsi l'incertitude des classifications suivantes.
- La **matrice de confusion** montre qu'il y a peu d'erreurs de classification, et la majorité des tumeurs malignes et bénignes sont correctement identifiées.

## Exécution du projet
1. **Cloner le dépôt** :
   ```bash
   git clone https://github.com/Jyriu/cancer-decision-tree.git
   ```
2. **Installer les dépendances** : 
- **Python** (version 3 min)
- **Pandas**
- **Scikit-learn**
- **Matplotlib**
- 
3. **Exécuter le script** :
   ```bash
   python breast_cancer_classification.py
   ```

## Résultats
- **Précision du modèle** : **94,7%**. Cela signifie que le modèle est assez fiable pour prédire correctement si une tumeur est bénigne ou maligne.
- **Visualisation de l'arbre de décision** : L'image ci-dessus permet de visualiser les décisions et les caractéristiques importantes qui influencent la classification. Cette visualisation est particulièrement utile pour comprendre le fonctionnement interne du modèle et s'assurer qu'il n'y a pas de biais non désirés.

## Licence
Projet à des fins éducatives uniquement.

## Auteur
Sami YEZZA, @Jyriu.
