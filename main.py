from fastapi import FastAPI  # Importation FastAPI pour la creation de L'API
from enum import Enum  # On importe Enum pour definir des ensembles de valeurs constantes

class Pharmacies(str, Enum): # On definit une enumeration (Enum) appelée Pharmacies
        OUVERT = "ouvert"
        FERME = "fermée"

class Medicament(str, Enum):  # On definit une enumeration (Enum)  appelée Medicament
        DISPONIBLE = "disponible"
        RUPTURE_DE_STOCK = "rupture_de_stock"

app = FastAPI()  # Creation de l'instance de l'application FastAPI.

@app.get("/pharmacie/{etat}")  # Creation de route get accessible via l'URL /pharmacie/{etat}
async def lire_pharmacie(etat: Pharmacies):
        if etat == Pharmacies.OUVERT:
                return {"etat": etat, "message": "La pharmacie Dafe est ouvert"}
        elif etat == Pharmacies.FERME:
                return {"etat": etat, "message": "La pharmacie est fermée"}
             
@app.get("/medicament/{acces}")  # get accessible via L'URL acces
async def lire_medicament(acces: Medicament):
        if acces == Medicament.DISPONIBLE:
                return {"acces": acces, "message": "Le medicament est disponible"}
        elif acces == Medicament.RUPTURE_DE_STOCK:
                return {"acces": acces, "message": "Le medicament est en rupture de stock"}