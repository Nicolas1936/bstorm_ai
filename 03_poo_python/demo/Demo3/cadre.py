from personne import Personne

class Cadre(Personne):

    def __init__(self, nom, prenom, prime):
        super().__init__(nom, prenom)
        self.__prime = prime

    #getter
    @property
    def prime(self):
        return self.__prime

    #setter
    @prime.setter
    def prime(self, value):
        self.__prime = value

    def realiser_planning(self, numero_planning):
        print(f"{self} réalise le planning {numero_planning}")

    def __str__ (self):
        text = super().__str__() + "(cadre)"
        return text
