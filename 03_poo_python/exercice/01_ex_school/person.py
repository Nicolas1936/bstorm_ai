class Person:
    def __init__(self, prenom, nom):
        self.__nom = nom
        self.__prenom = prenom

    def __repr__(self):
        output = "{} {}".format(self.__prenom, self.__nom)
        return output

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, nom):
        self.__nom = nom

    @property
    def prenom(self):
        return self.__prenom

    @prenom.setter
    def prenom(self, prenom):
        self.__prenom = prenom
