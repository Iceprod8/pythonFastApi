# Projet pythonFastApi

## Aperçu

Ce projet implémente un serveur FastAPI pour gérer un historique d'achats électroniques à partir d'une base de données CSV pour une boutique en ligne. Le serveur permet des opérations CRUD sur les données via une API RESTful.

## Fonctionnalités

- **GET** : Récupération de données pour des utilisateurs, commandes, produits, catégories et marques spécifiques.
- **POST** : Ajout de nouveaux enregistrements d'achat dans la base de données.
- **PUT** : Mise à jour des enregistrements d'achat existants.
- **DELETE** : Suppression des enregistrements d'achat de la base de données.
- **Authentification** : Sécurisation des routes API à l'aide de OAuth 2.0 (prochainement).

## Prérequis

Avant de commencer, assurez-vous de répondre aux exigences suivantes :
- Python 3.8+
- FastAPI
- Uvicorn
- pandas
- requests (pour les tests)

Vous pouvez installer les dépendances nécessaires avec pip :

```bash
pip install fastapi uvicorn pandas requests
```

## Structure du Projet

Voici à quoi ressemble la structure du répertoire du projet :

```
pythonFastApi/
│
├── main.py         # Module principal avec la définition de l'app FastAPI.
├── test.py         # Script pour tester les fonctionnalités de l'API.
├── Files/kz.csv    # Fichier de base de données CSV.
└── README.md       # Ce fichier.
```

## Lancement du Serveur

Pour démarrer le serveur FastAPI, naviguez jusqu'au répertoire du projet et exécutez la commande suivante :

```bash
uvicorn main:app --reload
```

L'option `--reload` permet de recharger automatiquement le serveur lors de modifications du code.

## Tester l'API

Pour tester l'API, vous pouvez utiliser le script `test.py` fourni. Ce script envoie des requêtes à l'API et affiche les réponses. Exécutez le script de test avec :

```bash
python .\test.py
```