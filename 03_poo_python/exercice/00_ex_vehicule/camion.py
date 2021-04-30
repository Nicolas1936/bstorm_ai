from vehicule import Vehicule

class Camion(Vehicule):

    def __init__(self, annee, modele, prix):
        super().__init__(annee, modele, prix)

    def __str__(self):
        output = "Camion : {} | {} | {} | {}".format(self._matricule, self._annee, self._modele, self._prix)
        return output

    def demarrer(self):
        print("Le camion demarre.")

    def accelerer(self):
        print("le camion accélère")