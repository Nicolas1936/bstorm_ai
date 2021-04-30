class Vehicule:
    nombres_vehicule = 1

    def __init__(self, annee, modele, prix):
        self._annee = annee
        self._modele = modele
        self._prix = prix
        self._matricule = Vehicule.nombres_vehicule
        Vehicule.nombres_vehicule += 1

    def __str__(self):
        output = "Vehicule : {} | {} | {} | {}".format(self._matricule, self._annee, self._modele, self._prix)
        return output

    def demarrer(self):
        print("Le vehicule demarre.")

    def accelerer(self):
        print("le vehicule accélère")

    @property
    def annee(self):
        return self._annee

    @annee.setter
    def annee(self, annee):
        self._annee = annee

    @property
    def modele(self):
        return self._modele

    @modele.setter
    def modele(self, modele):
        self._modele = modele

    @property
    def prix(self):
        return self._prix

    @prix.setter
    def prix(self, prix):
        self._prix = prix

    @property
    def matricule(self):
        return self._matricule
