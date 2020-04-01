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

A partir de maintenant, deux approches sont possibles et décrites plus bas.

## Docker

### Dépendances

* [Docker](https://docs.docker.com/install/)

### Utilisation

Tout d'abord, cleaner et convertir les données provenant des dataset CSV vers SQL.

```sh
# CSV to SQL pour toutes les entrées
make sql_all
# 50 000 entrées par défaut
make sql_partial
# Nombre spécifique d'entrées
make COUNT=100 sql_partial
```

Puis lancer les conteneurs docker et exécuter des requêtes.

```sh
# Les commandes docker sont à executer dans le dossier racine
# 1 - Lancement des conteneurs
docker-compose up

# 2 - Ouvrir un nouveau terminal
# 3 - Lancer la console mysql
docker exec -it le-milan-royal_database_1 mysql

# 4 - Éxecuter une requête (dans la console mysql)
source queries/1_popular_projects.sql

# 5 - Ctrl-C pour tout quitter la console mysql
# 5 - Ctrl-C pour quitter les logs docker-compose (1ère commande)
# 6 - (optionnel) On supprime toutes les données
docker-compose down -v
```

### Outils supplémentaires

* [PHPMyAdmin](http://localhost:3300) - Localhost port 3300
  * username: root
  * password: (laisser vide)


### Ajout de requêtes

Pour ajouter une requête, ajouter un fichier sql dans le dossier `queries`. Il sera automatiquement disponible dans le conteneur docker et la requête pourra être utilisée comme dans l'exemple plus haut.

### Reconstruire la base de données

La base de donnée est construire en exécutant tous les fichiers présents dans le dossier `database` lors de la création du volume docker. Pour la reconstuire, il suffit de supprimer le conteneur docker ainsi que le volume associé.

```sh
# On supprime les conteneurs & volumes (dossier racine)
docker-compose down -v
# On relance les conteneurs et la base de donnée sera reconstruite avec tout le contenu de database
docker-compose up
```

## Manuellement

Cette approche nécessite Python avec la librairie pandas, ainsi que MySQL.

Pour générer les fichiers SQL, lancez le script Python de votre choix :

`python tools/csv_split.py` pour insérer toutes les valeurs contenues dans le dataset.

`python tools/csv_split_light.py N` pour insérer un échantillon de N valeurs contenues dans le dataset. Si N est supérieur ou égal à la taille du dataset, le dataset entier sera considéré.

Ensuite, connectez-vous à MySql et créez un nouvelle base de données (ici nommée kickstarter) :

`sudo mysql`

`CREATE DATABASE kickstarter;`

`USE kickstarter;`

Pour créer et remplir les tables, récupérez le chemin absolu du répertoire du projet (absPath) et exécutez :

`source <absPath>/database/<fichier.sql>;` La table Facts doit être créée en dernier.

Pour exécuter les requêtes, lancer la commande suivante :

`source <absPath>/queries/<requete.sql>;`