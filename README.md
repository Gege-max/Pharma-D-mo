# Pharmacie API - version Démo

Une petite API FastAPI pour gérer l'état de la pharmacie et des medicament disponible.

## Fonctionnalités

- Consulter l'état d'une pharmacie ('ouvert' ou 'ferméé')
- Consulter la disponbilité d'un medicament ('disponible' ou 'rupture_de_stock)

# Endpoints
### Pharmacie

GET /pharmacie/{etat}

*Parametre :*

- 'etat' : '"ouvert"' ou '"fermée"'

### Medicament

GET /medicament/{acces}

*Parametre :*

- 'acces' : '"disponible'" ou '"rupture_de_stock"'

### Lancer L'API localement 

1 - Installer FastAPI et uvicorn 

pip install fastapi uvicorn 

2- Lnacer le serveur

uvicorn main:app --reload

3 - Acceder a L'API

. Swagger UI : http://127.0.0.1:8000/docs
. Redoc : http://127.0.0.1:8000/redoc

### NOTE

Ce projet est une version demo pour apprendre FastAPI et la gestion des Enum.
Il est conseillé de l'utiliser pour s'entrainer avant de l'integrer dans un projet plus complet
