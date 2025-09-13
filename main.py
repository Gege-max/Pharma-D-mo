from fastapi import FastAPI  # Importation FastAPI pour la creation de L'API
from enum import Enum  # On importe Enum pour definir des ensembles de valeurs constantes

class Pharmacies(str, Enum): # On definit une enumeration (Enum) appelée Pharmacies
        OUVERT = "ouvert"
        FERME = "fermée"

class Medicament(str, Enum):  # On definit une enumeration (Enum)  appelée Medicament
        DISPONIBLE = "disponible"
        RUPTURE_DE_STOCK = "rupture_de_stock"

app = FastAPI()  # Creation de l'instance de l'application FastAPI.

# Exemple de "base de donnée" en memoire
Pharmacies_db = [
        {"nom": "Dafe", "ville": "Brazzaville", "etat": "ouvert"},
        {"nom": "JAGGER", "ville": "Brazzaville", "etat": "ouvert"},
        ]

Medicament_db = [
        {"nom": "Paracetamol", "disponible": "disponible},
        {"nom": "Efferalgan", "disponibilité": "rupture_de_stock"},
        ]

@app.get("/pharmacie")  # Creation de route get accessible via l'URL /pharmacie
async def lire_pharmacie_query(etat: Pharmacies = None, ville: str = None):   # On difinit les parametres de requete
        result = pharmacies_db
        if etat:
            result = [p for p in result if p["etat"] == etat]
        if ville:
            result = [p for p in result if p["ville"].lower() == ville.lower()]
        return {"pharamacies": result}
             
@app.get("/medicament")  # get accessible via medicament
async def lire_medicament_query(acces: Medicament = None, Disponible: str = None):
        result = Medicament_db
        if acces:
                result = [p for p in result if p["acces"] = acces]
        if Disponible:
                result = [p for p in result if p["Disponible"].lower() == p["Disponible.lower()]
        result {"Medicament": result}
