# Projet Entrepôt de Données

Travail réalisé par Josselin ENET, Kévin ROY, Thomas TABAZZA et Tristan LENORMAND --- M1ALMA

## Introduction

Ce projet consiste en la création d'un entrepôt de données à partir d'un dataset. Nous avons choisi de nous intéresser aux projets Kickstarter, qui est un site de financement participatif. Le dataset utilisé est le suivant : https://www.kaggle.com/kemical/kickstarter-projects. Il est partagé par Mickaël Mouillé sous licence CC BY-NC-SA 4.0.

Nous avons ensuite rédigé un script Python afin de générer les différents fichiers SQL de création de tables et d'insertion de valeurs à partir du dataset.

Enfin, nous avons créé un entrepôt sur notre machine en utilisant l'outil MySql. Il suffit pour cela de lui fournir les fichiers SQL générés plus tôt.

## Utilisation

Ce projet nécessite Python avec la librairie pandas, ainsi que MySQL.

Tout d'abord, clonez le projet sur votre machine : 

`git clone https://github.com/joss-enet/Le-milan-royal`

Ensuite, rendez-vous dans la racine du projet : 

`cd Le-milan-royal`

Pour générer les fichiers SQL, lancez le script Python de votre choix :

`python csv_split.py` pour insérer toutes les valeurs contenues dans le dataset.

`python csv_split_light.py N` pour insérer un échantillon de N valeurs contenues dans le dataset. Si N est supérieur ou égal à la taille du dataset, le dataset entier sera considéré.

Ensuite, connectez-vous à MySql et créez un nouvelle base de données (ici nommée kickstarter) :

`sudo mysql`

`CREATE DATABASE kickstarter;`

`USE kickstarter;`

Pour créer et remplir les tables, récupérez le chemin absolu du répertoire du projet (absPath) et exécutez :

`source <absPath>/sql_scripts/dbScript.sql;` si vous avez utilisé le script csv_split.py.

`source <absPath>/sql_scripts_light/dbScript.sql;` si vous avez utilisé le script csv_split_light.py.
