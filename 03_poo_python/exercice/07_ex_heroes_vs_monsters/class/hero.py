from personne import Personne

class Hero(Personne):
    
    #***********************************************
    # INITIALISATION
    #***********************************************

    # def __init__(self, nom):
    #     super().__init__(nom)

    #***********************************************
    # METHODE
    #***********************************************

    #FRAPPE
    # def frappe(self, player2):
    #     super().frappe(player2)
    #     if not player2.en_vie:
    #         d_or, d_cuir = player2.depouille()
    #         self._or += d_or
    #         self._cuir += d_cuir

    #DEPOUILLE
    def depouille(self, player2):
        d_or, d_cuir = player2.est_depouille()
        self._or += d_or
        self._cuir += d_cuir
        print("{} a gagné {} or et {} cuir || TOTAL => or : {} | cuir : {}".\
            format(self.nom, d_or, d_cuir, self._or, self._cuir))

    #REGENERATION
    def se_regenere(self):
        self.point_de_vie = self._point_de_vie_max

        print("{} s'est regénéré. Prêt au combat!!!".\
            format(self.nom))

if __name__ == "__main__":

    h = Hero()
    print(h)