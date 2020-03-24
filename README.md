# Projet Entrepôt de Données

Travail réalisé par Josselin ENET, Kévin ROY, Thomas TABAZZA et Tristan LENORMAND --- M1ALMA

## Introduction

Ce projet consiste en la création d'un entrepôt de données à partir d'un dataset. Nous avons choisi de nous intéresser aux projets Kickstarter, qui est un site de financement participatif. Le dataset utilisé est le suivant : https://www.kaggle.com/kemical/kickstarter-projects. Il est partagé par Mickaël Mouillé sous licence CC BY-NC-SA 4.0.

Nous avons ensuite rédigé un script Python afin de générer les différents fichiers SQL de création de tables et d'insertion de valeurs à partir du dataset.

Enfin, nous avons créé un entrepôt sur notre machine en utilisant l'outil MySql. Il suffit pour cela de lui fournir les fichiers SQL générés plus tôt.

## Utilisation

Tout d'abord, clonez le projet sur votre machine : 

`git clone https://github.com/joss-enet/Le-milan-royal`

Ensuite, rendez-vous dans la racine du projet : 

`cd Le-milan-royal`

Pour générer les fichiers SQL, lancez le script Python de votre choix :

`python csv_split.py` pour insérer toutes les valeurs contenues dans le dataset.

`python csv_split_light.py` pour insérer un échantillon de 20000 valeurs contenues dans le dataset.

Pour créer et remplir les tables :