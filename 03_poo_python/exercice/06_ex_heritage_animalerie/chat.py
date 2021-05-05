from animal import Animal

class Chat(Animal):

    RISK_DECES = 0.5
    NB_CHATS = 0

    #***********************************************
    # INITIALISATION
    #***********************************************

    def __init__(self, nom, poids, taille, sexe, age, date_arrivee, caractere, griffes_coupees, poil_long):
        super().__init__(nom, poids, taille, sexe, age, date_arrivee)
        self._caractere = caractere
        self._griffes_coupees = griffes_coupees
        self._poil_long = poil_long

        Chat.NB_CHATS += 1

    #***********************************************
    # GETTER / SETTER
    #***********************************************

    #CARACTERE
    @property
    def caractere(self):
        return self._caractere

    @caractere.setter
    def caractere(self, value):
        self._caractere = value

    #GRIFFES COUPEES
    @property
    def griffes_coupees(self):
        return self._griffes_coupees

    @griffes_coupees.setter
    def griffes_coupees(self, value):
        self._griffes_coupees = value

    #POIL LONG
    @property
    def poil_long(self):
        return self._poil_long

    @poil_long.setter
    def poil_long(self, value):
        self._poil_long = value

    #***********************************************
    # METHODE
    #***********************************************

    def crie(self):
        print("CHAT   || {} miaule!".format(self.nom))

    def __str__(self):
        retour = super().__str__()
        retour = "CHAT  " + retour[6:]
        retour += " | caractere : {} | griffes coupees : {} | poil long : {}".\
            format(self.caractere, self.griffes_coupees, self.poil_long)
        return retour