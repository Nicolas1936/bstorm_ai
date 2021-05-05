from animal import Animal

class Oiseau(Animal):

    RISK_DECES = 3
    NB_OISEAUX = 0

    #***********************************************
    # INITIALISATION
    #***********************************************

    def __init__(self, nom, poids, taille, sexe, age, date_arrivee, couleur, vivre_ds_voliere):
        super().__init__(nom, poids, taille, sexe, age, date_arrivee)
        self._couleur = couleur
        self._vivre_ds_voliere = vivre_ds_voliere

        Oiseau.NB_OISEAUX += 1

    #***********************************************
    # GETTER / SETTER
    #***********************************************

    #COULEUR
    @property
    def couleur(self):
        return self._couleur

    @couleur.setter
    def couleur(self, value):
        self._couleur = value

    #VIVRE DANS UNE VOLIERE (AU CONTRAIRE DE VIVRE DANS UNE CAGE)
    @property
    def vivre_ds_voliere(self):
        return self._vivre_ds_voliere

    @vivre_ds_voliere.setter
    def vivre_ds_voliere(self, value):
        self._vivre_ds_voliere = value

    #***********************************************
    # METHODE
    #***********************************************

    def crie(self):
        print("OISEAU || {} chante!".format(self.nom))

    def __str__(self):
        retour = super().__str__()
        retour = "OISEAU" + retour[6:]
        retour += " | couleur : {} | vie dans une volière : {}".\
            format(self.couleur, self.vivre_ds_voliere)
        return retour