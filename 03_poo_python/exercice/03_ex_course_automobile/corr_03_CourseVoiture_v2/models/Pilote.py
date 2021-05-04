import datetime


class Pilote:

    def __init__(self, nom, prenom, date_naissance, exp=0):
        self.__nom = nom
        self.__prenom = prenom
        self.__date_naissance = date_naissance
        self.__exp = exp  # 0 - 100

    @property
    def prenom(self):
        return self.__prenom

    @prenom.setter
    def prenom(self, value):
        self.__prenom = value

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, value):
        self.__nom = value

    @property
    def nom_complet(self):
        return "{0} {1}".format(self.prenom, self.nom.upper())

    @property
    def date_naissance(self):
        return self.__date_naissance

    @property
    def age(self):
        return datetime.date.today().year - self.__date_naissance.year

    @property
    def exp(self):
        return self.__exp

    def gagner_exp(self, value):
        if value < 0:
            raise ValueError()

        if self.exp + value <= 100:
            self.__exp += value
        else:
            self.__exp = 100

    def perdre_exp(self, value):
        if value < 0:
            raise ValueError()

        if self.exp - value >= 0:
            self.__exp -= value
        else:
            self.__exp = 0

    def __str__(self):
        return "{0} - {1} ans".format(self.nom_complet, self.age)

