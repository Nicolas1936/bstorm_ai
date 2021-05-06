from exceptions.refuge_exception import RefugeError
from models.adresse import Adresse
from models.animal import Animal
from models.chat import Chat
from models.chien import Chien
import datetime
from helper.rng_helper import RngHelper


class Refuge:

    def __init__(self, nom, capacite, rue, numero, ville, code_postal):
        self.__nom = nom
        self.__adresse = Adresse(rue, numero, ville, code_postal)
        self.__capacite = capacite
        self.__animaux = list()

    # region

    @property
    def nom(self):
        return self.__nom

    @property
    def adresse(self):
        return self.__adresse

    @property
    def capacite(self):
        return self.__capacite

    @capacite.setter
    def capacite(self, value):
        self.__capacite = value

    @property
    def animaux_dispo(self):
        # dispos = list()

        for animal in self.__animaux:
            if animal.est_dispo:
                # dispos.append(animal)
                yield animal

        # return dispos

    @property
    def nb_chien(self):
        nb = 0
        for animal in self.animaux_dispo:
            if isinstance(animal, Chien):
                nb += 1
        return nb

    @property
    def nb_chat(self):
        nb = 0
        for animal in self.animaux_dispo:
            if isinstance(animal, Chat):
                nb += 1
        return nb

    @property
    def nb_animaux(self):
        nb = 0
        for animal in self.animaux_dispo:
            nb += 1
        return nb

    # endregion

    # region Méthodes

    def resumer(self):
        desc = "Liste des animaux : \n"

        for animal in self.animaux_dispo:
            desc += "\t- {0}\n".format(animal)

        desc += "Nb animaux : {} (Chien : {}, Chat : {})".format(self.nb_animaux, self.nb_chien, self.nb_chat)

        return desc

    def ajouter_animal(self, animal):

        if not isinstance(animal, Animal):
            raise RefugeError("Not an animal!")

        if self.nb_animaux >= self.capacite:
            raise RefugeError("No place!")

        if not animal.est_vivant:
            raise RefugeError("Pas d'animal mort, merci!")

        if animal not in self.__animaux:
            self.__animaux.append(animal)


    def tenter_adoption(self, visiteur, animal):
        # Si l'animal "seduit" le visiteur, celui-ci l'adopte
        # Si la seduction a raté, il a tout de même 1% de chance.

        if animal.seduire_personne(visiteur) or RngHelper.proba(1):
            animal.se_faire_adopter()


    def simuler_journee(self):

        print(self.resumer())
        print()

        print("Evenement de la matinée")
        for animal in self.animaux_dispo:

            if isinstance(animal, Chat) and animal.griffes_longues:
                animal.couper_griffes()
                print("Les griffes de", animal.nom, "sont coupées")

            if isinstance(animal, Chien):
                animal.crier()

            if RngHelper.proba(5):
                self.tenter_adoption("Une personne", animal)
        print()

        print("Evenement de la journée")
        for animal in self.animaux_dispo:
            animal.passer_journee()

            if isinstance(animal, Chien) and RngHelper.proba(33):
                animal.courir("un visiteur")

            if RngHelper.proba(30):
                self.tenter_adoption("Une personne", animal)

            animal.crier()
        print()

        print("Evenement de la nuit")
        for animal in self.animaux_dispo:
            animal.passer_nuit()
        print()
        # endregion
