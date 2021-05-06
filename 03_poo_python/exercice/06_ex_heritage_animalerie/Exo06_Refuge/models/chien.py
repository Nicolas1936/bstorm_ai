from helper.rng_helper import RngHelper
from models.animal import Animal
import random
import datetime


class Chien(Animal):

    def __init__(self, nom, poids, taille, sexe, date_naissance, couleur_collier, race, est_dresse):
        super().__init__(nom, poids, taille, sexe, date_naissance, 1)
        self.__couleur_collier = couleur_collier
        self.__race = race
        self.__est_dresse = est_dresse

    # region Propriétés

    @property
    def couleur_collier(self):
        return self.__couleur_collier

    @couleur_collier.setter
    def couleur_collier(self, value):
        self.__couleur_collier = value

    @property
    def race(self):
        return self.__race

    @property
    def est_dresse(self):
        return self.__est_dresse

    @property
    def age_humain(self):
        return self.age * 7

    # endregion

    # region Méthodes

    def crier(self):

        if RngHelper.proba(75):
            print(self.nom, "aboie!")
        else:
            print(self.nom, "hurle à la mort!")

    def passer_journee(self):
        pass

    def courir(self, cible):
        print(self.nom, "court après", cible)
    # endregion

    # region Méthodes specials

    def __str__(self):

        return "{0} ({1})".format(super().__str__(), self.race)

    # endregion



#Zone de test
if __name__ == '__main__':

    c = Chien("Robert", 20, 1, "F", datetime.date(2016, 2, 29), "Vert", "Labrador", False)

    print(c.age)
    print(c.age_humain)