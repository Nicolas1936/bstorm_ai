from abc import ABC, abstractmethod
import datetime

from helper.rng_helper import RngHelper


class Animal(ABC):

    def __init__(self, nom, poids, taille, sexe, date_naissance, chance_deces):
        self.__nom = nom
        self.__poids = poids
        self.__taille = taille
        self.__sexe = sexe if sexe is not None else "X"
        self.__date_naissance = date_naissance
        self.__chance_deces = chance_deces
        self.__est_vivant = True
        self.__est_adopte = False
        self.__date_arrive = datetime.date.today()

    #region Propriétés
    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, value):
        self.__nom = value

    @property
    def poids(self):
        return self.__poids

    @poids.setter
    def poids(self, value):
        self.__poids = value

    @property
    def taille(self):
        return self.__taille

    @taille.setter
    def taille(self, value):
        self.__taille = value

    @property
    def date_arrive (self):
        return self.__date_arrive

    @property
    def date_naissance(self):
        return self.__date_naissance

    @property
    def age(self):
        today = datetime.date.today()

        # age = today.year - self.date_naissance.year - int((today.month, today.day) < (self.date_naissance.month, self.date_naissance.day))

        age = today.year - self.date_naissance.year
        if today.month < self.date_naissance.month or (today.month == self.date_naissance.month and today.day < self.date_naissance.day):
            age -= 1

        return age

    @property
    @abstractmethod
    def age_humain(self):
        pass

    @property
    def sexe(self):
        return self.__sexe

    @property
    def est_vivant(self):
        return self.__est_vivant

    @property
    def est_adopte(self):
        return self.__est_adopte

    @property
    def est_dispo(self):
        return self.est_vivant and not self.est_adopte
    # endregion

    # region Méthodes
    @abstractmethod
    def crier(self):
        pass

    def se_faire_adopter(self):
        self.__est_adopte = True
        print(self.nom, "est adopté! ♥")

    def seduire_personne(self, nom):
        print(self.nom, "seduit", nom)
        return True


    @abstractmethod
    def passer_journee(self):
        pass


    def passer_nuit(self):
        # chance_survie = random.random() * 100
        # if chance_survie < self.__chance_deces:

        if RngHelper.proba(self.__chance_deces):
            self.__est_vivant = False
            print("{} est mouru".format(self.nom))
        else:
            print("{} a bien dormi".format(self.nom))
    # endregion

    # region Méthodes spécials

    def __str__(self):
        return "{0} {1} {2} ans".format(self.nom, self.sexe, self.age)

    # endregion