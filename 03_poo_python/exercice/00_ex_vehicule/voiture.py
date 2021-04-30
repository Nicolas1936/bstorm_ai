from vehicule import Vehicule

class Voiture(Vehicule):

    def __init__(self, annee, modele, prix):
        super().__init__(annee, modele, prix)

    def __str__(self):
        output = "Voiture : {} | {} | {} | {}".format(self._matricule, self._annee, self._modele, self._prix)
        return output

    def demarrer(self):
        print("Le voiture demarre.")

    def accelerer(self):
        print("le voiture accélère")