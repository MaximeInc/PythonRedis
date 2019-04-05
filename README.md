# EPSI I4 - NoSQL - TP 3

## Sujet :
A l'aide du langage de programmation de votre choix et d'un driver Redis, développer une application capable de sauvegarder et de consulter des notes.

L'application devra permettre de :
- Consulter l'ensemble des notes sauvegardées sur le serveur
- Ajouter une note (en renseigner uniquement le contenu de celle-ci)
- Consulter une note à partir de son ID

## Solution :
Utilisation du langage Python avec le framework Flask. L'application permet de recevoir des requêtes HTTP afin d'intéragir avec une base de donnée Redis.

### Prérequis :
Systême d'exploitation : Linux

- **Python3**
    - Commande d'installation : `sudo apt-get install python3`
- **RedisServer**
    - Commande d'installation : `sudo apt-get install redis-server`
- **Flask**
    - Commande d'installation : `sudo apt install python3-flask`
- **Git**
    - Commande d'installation : `sudo apt install git`


### Installation du projet :

Pour télécharger le projet lancer la commande :
```
$ git clone https://github.com/MaximeInc/PythonRedis.git
```

### Lancer le serveur HTTP et le serveur Redis :

Dans un premier temps, il est nécessaire de lancer le serveur Redis afin de pouvoir intéragir avec celui-ci.

- **Lancer le server redis :**
```
$ sudo service redis-server start
```
On peut ensuite lancer notre application.

- **Lancer le server HTTP :**
```
$ python3 redisPython.py
```


### Utilisation de l'application : 

Notre application permet donc de créer, ou consulter des notes ajoutées dans la base Redis. Pour envoyer des requêtes, nous utilisons Curl.

- **Créer une note :**
    - **Curl :** `$ curl -H "Content-Type:text/plain" --data 'penser au pain" http://localhost:8080/notes`
- **Consulter une note via son id :**
    - **Curl :** `$ curl http://localhost:8080/notes/{idnote}` 
- **Consulter toutes les notes disponibles :**
    - **Curl :** `$ curl  http://localhost:8080/notes` 

