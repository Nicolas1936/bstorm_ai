from helper.rng_helper import RngHelper
from models.animal import Animal
import random


class Chat(Animal):

    def __init__(self, nom, poids, taille, sexe, date_naissance, poils_long, caractere):
        super().__init__(nom, poids, taille, sexe, date_naissance, 0.5)
        self.__poils_long = poils_long
        self.__caractere = caractere
        self.__taille_griffe = 0
        self.__taille_griffe_max = 10

    @property
    def caractere(self):
        return self.__caractere

    @property
    def poil_long(self):
        return self.__poils_long

    @property
    def griffes_longues(self):
        return self.__taille_griffe >= self.__taille_griffe_max

    @property
    def age_humain(self):
        return self.age * 5

    def crier(self):
        print(self.nom, "miaule")

    def seduire_personne(self, nom):
        if RngHelper.proba(50):
            print(self.nom, "griffe", nom)
            return False

        return super().seduire_personne(nom)

    def passer_journee(self):
        self.__taille_griffe += random.randrange(0, 3)

    def couper_griffes(self):
        self.__taille_griffe = 0

    def __str__(self):
        poils = "longs" if self.poil_long else "courts"

        return "{0} (Chat à poils {1})".format(super().__str__(), poils)
