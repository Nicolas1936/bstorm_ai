from monstre import Monstre

class Orque(Monstre):

    #***********************************************
    # INITIALISATION
    #***********************************************

    def __init__(self, nom):
        super().__init__(nom)

        self._cuir = 0

    #***********************************************
    # METHODE
    #***********************************************