from personne import Personne

class Employe(Personne):
    
    def __init__(self, nom, prenom, date_naissance, salaire):
        super().__init__(nom, prenom, date_naissance)
        self._salaire = salaire

    def affiche(self):
        super().affiche()
        print("Salaire              : ", self._salaire)


if __name__ == '__main__':
    e = Employe("Blanchard", "Nicolas", "22/06/1983", 1000)
    e.affiche()
