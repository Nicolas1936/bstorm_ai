from vehicule import Vehicule
from camion import Camion
from voiture import Voiture

class Test():

    def __init__(self):
        self.test_vehicule()
        self.test_camion()
        self.test_voiture()

    def test_vehicule(self):
        bateau = Vehicule(2000, "Leman", 10000)
        print(bateau)
        bateau.annee, bateau.modele, bateau.prix = 1990, "Geneve", 8000
        print(bateau.matricule, bateau.annee, bateau.modele, bateau.prix)

    def test_camion(self):
        camion = Camion(2000, "Leman", 10000)
        print(camion)
        camion.annee, camion.modele, camion.prix = 1990, "Geneve", 8000
        print(camion.matricule, camion.annee, camion.modele, camion.prix)

    def test_voiture(self):
        voiture = Voiture(2000, "Leman", 10000)
        print(voiture)
        voiture.annee, voiture.modele, voiture.prix = 1990, "Geneve", 8000
        print(voiture.matricule, voiture.annee, voiture.modele, voiture.prix)


if __name__ == "__main__":
    Test()