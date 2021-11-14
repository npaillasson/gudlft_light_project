
***
[Watch below for the English version](#Güdlft_light-en) 
***

# Projet Güdlft_light (fr)

***

Ce projet est entièrement codé en python 3.

Il est réalisé dans le cadre d'une formation sur le site [OpenClassrooms](https://openclassrooms.com/fr/).
Ce projet est une interface web qui permet à des secretaire de clubs sportifs de reserver des places pour leurs athlètes dans des compétition en échange de points.
## Table des matières
1. [Informations génerales](#informations-generales)
2. [Installation/usage](#installation-usage)

***

## Informations Generales

Ce projet utilise le framework de developpement web[flask](https://flask.palletsprojects.com/en/2.0.x/). Pour la réalisation des tests, le projet utilise le framework de test python [pytest](https://docs.pytest.org/en/6.2.x/). Pour la réalisation des tests de performance, le projet utilise [locust](https://locust.io/).


## Installation Usage

Tout d'abord il faut cloner le projet depuis github grâce à la commande suivante :

```
$ git clone https://github.com/npaillasson/gudlft_light_project.git
```

Rendez-vous ensuite à la racine du projet. Il est ensuite recommandé de créer un environement virtuel avec venv afin d'installer tous les packages et dépendances nécéssaires au fonctionnement du projet :

```
$ python3 -m venv env
```

Utilisez ensuite la commande suivante pour activer l'environnement :
```
$ source env/bin/activate
```

ou sous Windows:
```
> env\Scripts\activate
```

Vous pouvez ensuite installer les packages nécéssaire grace à pip et au fichier requirements.txt :
```
$ pip install -r requirements.txt
```

Avant de lancer le server, flask nécéssite que vous configuriez des variables environnementales:
sous les système UNIX (macos/linux):
```
export FLASK_APP=server.py
```

sous Windows:
```
$set FLASK_APP = server.py
```

Pour lancer le serveur exécuter la commande suivante :
```
$ flask run
```

Vous pouvez ensuite aller sur le [site](http://127.0.0.1:5000/) (http://127.0.0.1:5000/)

Pour désactiver l'environnement virtuel, utilisez la commande suivante :
```
$ deactivate
```

Ou sous Windows:
```
> env\Scripts\deactivate
```

Pour lancer les tests du projet

```
$ pytest
```

Pour lancer analyser la couverture de tests du projet
```
$ pytest --cov=.
```

Pour créer un rapport de la couverture de tests au format html
```
$ pytest --cov=. --cov-report html
```

Pour réalisé un test de performance avec locust, lancer le serveur, puis:
```
$ locust -f tests/performance_tests/locustfile.py
```

Puis rendez-vous sur l'interface de [tests](http://0.0.0.0:8089), selectionnez le nombre d'utilisateurs à simuler, et entrez l'adresse du serveur (http://127.0.0.1:5000/) puis cliquez sur "strat swarming" pour lancer les tests. 

***
# güdlft_light (en)
***


This project is entirely coded in python 3.

It is realized within the framework of a training on the site [OpenClassrooms](https://openclassrooms.com/fr/).
This project is a web interface that allows sports clubs to reserve places for their athletes in competitions in exchange for points.


## Table of contents
1. [General information](#general-information)
2. [Installation/usage](#installation)

***

## General Information

This project uses the [flask](https://flask.palletsprojects.com/en/2.0.x/) framework to create the backend. For the realization of the tests, the project uses the python test framework [pytest](https://docs.pytest.org/en/6.2.x/). For the performance tests, the project uses [locust](https://locust.io/).


## Installation

To clone the project locally use the following command :

```
$ git clone https://github.com/npaillasson/gudlft_light_project.git
```

Then go to the root of the project, it is recommended to create a virtual environment with venv :

```
$ python3 -m venv env
```

To activate the virtual environment use :
```
$ source env/bin/activate
```

If you are on Windows use:
```
> env\Scripts\activate
```

To install the necessary packages use pip and the file requierements.txt :
```
$ pip install -r requirements.txt
```

Before starting the server, flask requires you to configure environmental variables:
On UNIX (macos/linux):
```
export FLASK_APP=server.py
```

On Windows:
```
$set FLASK_APP = server.py
```

To start the server run the following command :
```
$ flask run
```

Now you can access the [website](http://127.0.0.1:5000/) (http://127.0.0.1:5000/)

To deactivate the virtual environement use :
```
$ deactivate
```

If you are on Windows use:
```
> env\Scripts\deactivate
```

To launch tests

```
$ pytest
```

To analyze the test coverage of the project
```
$ pytest --cov=.
```

To create a test coverage report in html format
```
$ pytest --cov=. --cov-report html
```

To launch a performance test with locust, start the server, then:
```
$ locust -f tests/performance_tests/locustfile.py
```

Then go to the [tests interface](http://0.0.0.0:8089), select the number of users to simulate, and enter the server address (http://127.0.0.1:5000/) then click on "strat swarming" to launch tests. 


****