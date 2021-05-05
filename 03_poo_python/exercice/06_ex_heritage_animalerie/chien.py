from animal import Animal

class Chien(Animal):

    RISK_DECES = 1
    NB_CHIENS = 0

    #***********************************************
    # INITIALISATION
    #***********************************************

    def __init__(self, nom, poids, taille, sexe, age, date_arrivee, couleur_collier, est_dresse, race):
        super().__init__(nom, poids, taille, sexe, age, date_arrivee)
        self._couleur_collier = couleur_collier
        self._est_dresse = est_dresse
        self._race = race

        Chien.NB_CHIENS += 1

    #***********************************************
    # GETTER / SETTER
    #***********************************************

    #COULEUR DU COLLIER
    @property
    def couleur_collier(self):
        return self._couleur_collier

    @couleur_collier.setter
    def couleur_collier(self, value):
        self._couleur_collier = value

    #EST DRESSE
    @property
    def est_dresse(self):
        return self._est_dresse

    @est_dresse.setter
    def est_dresse(self, value):
        self._est_dresse = value

    #RACE
    @property
    def race(self):
        return self._race

    @race.setter
    def race(self, value):
        self._race = value

    #***********************************************
    # METHODE
    #***********************************************

    def crie(self):
        print("CHIEN  || {} aboie!".format(self.nom))

    def __str__(self):
        retour = super().__str__()
        retour = "CHIEN " + retour[6:]
        retour += " | couleur du collier : {} | est dressé : {} | race : {}".\
            format(self.couleur_collier, self.est_dresse, self.race)
        return retour