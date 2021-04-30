from personne import Personne

class Employe(Personne):

    def __init__(self, nom, prenom, cadre):
        super().__init__(nom, prenom)
        self.__sup = cadre

    @property
    def sup(self):
        return self.__sup

    def realiser_encodage(self):
        print(f"{self} réalise un encodage")

    def reunion_sup(self):
        print("{0} est en réunion avec {1}".format(self, self.sup))



    
