from personne import Personne
from des import Des

class Monstre(Personne):

    #***********************************************
    # INITIALISATION
    #***********************************************

    def __init__(self, nom):
        super().__init__(nom)

        de_or = Des(1, 6)
        de_cuir = Des(1, 4)

        self._or = de_or.lancer_des()
        self._cuir = de_cuir.lancer_des()
        


    #***********************************************
    # METHODE
    #***********************************************

    def est_depouille(self):
        d_or = self._or
        d_cuir = self._cuir

        self._or = 0
        self._cuir = 0
        
        return d_or, d_cuir