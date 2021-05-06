import datetime
from models.refuge import Refuge
from models.chat import Chat
from models.chien import Chien

r = Refuge("AnimalBel", 20, "Rue de bruxelles", 42, "Namur", 5000)

le_chat_1 = Chat("LeChat", 5, 0.3, "F", datetime.date(2017, 1, 1), True, "Calin")
le_chat_2 = Chat("Garfield", 10, 0.7, "M", datetime.date(2015, 2, 28), False, "Dormeur")

le_chien_1 = Chien("Didier", 40, 1, None, datetime.date(2012, 2, 3), "Rose", "Labrador", False)

r.ajouter_animal(le_chat_1)
r.ajouter_animal(le_chat_2)
r.ajouter_animal(le_chien_1)


def demande_animal():
    choix = int(input("- Choix animal (1 - Chat, 2 - Chien) :"))
    print()

    nom = input("Nom : ")
    poids = float(input("Poids : "))
    taille = float(input("Taille : "))
    sexe = input("Sexe (M/F) : ")
    date_query = input("Date de naissance (YYYY-MM-DD) : ")
    date_naissance = datetime.date.fromisoformat(date_query)

    if choix == 1:
        caractere = input("Caractere : ")
        type_poils = input("Type de poils (Long/Court)")
        poils_long = type_poils.upper() == "LONG"

        animal = Chat(nom, poids, taille, sexe, date_naissance, poils_long, caractere)
    else:
        collier = input("Couleur collier : ")
        race = input("Race : ")
        dressage = input("Est dressé (Oui/Non): ")
        est_dresse = dressage.upper() == "OUI"

        animal = Chien(nom, poids, taille, sexe, date_naissance,collier, race, est_dresse)
    return  animal


while(r.nb_animaux > 0):
    # Demande nouveau arrivant
    nbr_text = input("Nombre d'arrivant (entrer pour passer): ")
    if nbr_text.isdigit():
        nbr = int(nbr_text)
        while nbr > 0:
            animal = demande_animal()
            r.ajouter_animal(animal)
            nbr -= 1
            print()

    #Simulation
    r.simuler_journee()
    print("**********************************************")


