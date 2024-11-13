# Prédire le cancer du sein

Ce projet vise à classifier des tumeurs du sein en **bénignes** ou **malignes** en utilisant un **arbre de décision**. Le dataset utilisé est le **Breast Cancer Wisconsin Dataset**, qui contient diverses caractéristiques dérivées d'images cellulaires pour aider à prédire la nature de la tumeur.

## Aperçu du Projet

![Arbre de Décision](/decision_tree_visual.png)

L'image ci-dessus montre l'arbre de décision entraîné pour classer les tumeurs en bénignes ou malignes. Les nœuds représentent les différentes décisions prises en fonction des caractéristiques des tumeurs, et les couleurs indiquent la classe prédite. Voici quelques détails pour mieux comprendre l'arbre de décision :

- **Noeuds et décisions** : Chaque nœud représente une décision basée sur une caractéristique de la tumeur. Par exemple, dans la partie supérieure de l'arbre, la décision commence par `mean concave points <= 0.051`, qui sépare les échantillons en fonction de cette caractéristique.
- **Valeur `gini`** : Le coefficient de **Gini** est une mesure d'impureté. Un **gini** proche de 0 signifie que le nœud est principalement composé d'une seule classe (ce qui est idéal). Un **gini** plus élevé signifie qu'il y a un mélange des classes dans le nœud.
- **Échantillons (`samples`)** : Indique le nombre total d'échantillons considérés à ce niveau de l'arbre. Cela aide à comprendre combien d'échantillons sont traités dans chaque nœud.
- **Valeurs (`value`)** : Montre la répartition des classes (`[bénignes, malignes]`) dans ce nœud. Par exemple, `value = [169, 286]` signifie qu'il y a 169 tumeurs bénignes et 286 malignes à ce point précis.
- **Couleurs des nœuds** : Les nœuds en **bleu** représentent une prédiction de tumeur maligne, tandis que les nœuds en **orange** prédisent une tumeur bénigne.
- **Chemins de décision** : Les caractéristiques les plus discriminantes apparaissent dans les niveaux supérieurs de l'arbre. Cela signifie que certaines caractéristiques sont plus importantes pour décider si une tumeur est bénigne ou maligne.

## Dataset
- Mesures des noyaux cellulaires à partir d'images de masses mammaires.
- Caractéristiques : **rayon moyen**, **texture moyenne**, **périmètre moyen**, **concavité**, etc.
- La variable cible (`benign_0__mal_1`) indique si une tumeur est bénigne (`0`) ou maligne (`1`).

## Vue d'ensemble du projet
1. **Préparation des données** : Chargement des données et séparation des caractéristiques de la variable cible.
2. **Entraînement du modèle** : Entraînement d'un **arbre de décision** sur les données divisées en ensembles d'entraînement (80%) et de test (20%).
3. **Évaluation** : Le modèle a obtenu une précision d'environ **94,7%** sur l'ensemble de test.
4. **Visualisation** : Visualisation de l'arbre de décision pour comprendre les critères de classification (cf. l'image ci-dessus).

## Exécution du projet
1. Cloner le dépôt :
   ```bash
   git clone https://github.com/Jyriu/cancer-decision-tree.git
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
- **Scikit-learn** pour la modélisation
- **Matplotlib** pour la visualisation

## Résultats
- Précision du modèle : **94,7%**.
- La visualisation de l'arbre de décision permet de mieux comprendre la prise de décision (voir l'image ci-dessus).

## Licence
Projet à des fins éducatives uniquement.

