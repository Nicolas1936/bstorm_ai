import random

class Animal:

    RISK_DECES = 0

    #***********************************************
    # INITIALISATION
    #***********************************************

    def __init__(self, nom, poids, taille, sexe, age, date_arrivee):
        self._nom = nom
        self._poids = poids
        self._taille = taille
        self._sexe = sexe
        self._age = age
        self._date_arrivee = date_arrivee

        self._age_humain_equi = self._age * 3
        self._en_vie = True

    #***********************************************
    # GETTER / SETTER
    #***********************************************

    #NOM
    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, value):
        self._nom = value

    #POIDS
    @property
    def poids(self):
        return self._poids

    @poids.setter
    def poids(self, value):
        self._poids = value

    #TAILLE
    @property
    def taille(self):
        return self._taille

    @taille.setter
    def taille(self, value):
        self._taille = value

    #SEXE
    @property
    def sexe(self):
        return self._sexe

    @sexe.setter
    def sexe(self, value):
        self._sexe = value

    #AGE
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    #DATE D'ARRIVEE
    @property
    def date_arrivee(self):
        return self._date_arrivee

    @date_arrivee.setter
    def date_arrivee(self, value):
        self._date_arrivee = value

    #AGE HUMAIN EQUIVALENT
    @property
    def age_humain_equi(self):
        return self._age_humain_equi

    #EST EN VIE
    @property
    def en_vie(self):
        return self._en_vie

    @en_vie.setter
    def en_vie(self, value):
        self._en_vie = value

    #***********************************************
    # METHODE
    #***********************************************

    def crie(self):
        print("ANIMAL || {} fait un bruit!".format(self.nom))

    def passe_nuit(self):
        if not self.en_vie:
            print("{} est déjà mort".format(self.nom))
        else:
            chance_vie = round(random.uniform(0.0, 10.0),1)
            #print(chance_vie)
            if chance_vie >= self.RISK_DECES:
                print("{} à passé la nuit".format(self.nom))
            else:
                print("{} est mort pendant la nuit...".format(self.nom))
                self.en_vie = False

    def __str__(self):
        retour = "ANIMAL || nom : {} | poids : {} | taille : {} | sexe : {} | age : {} | age humain : {} | date d'arrivée : {} | en vie : {}".\
            format(self.nom, self.poids, self.taille, self.sexe, self.age, self.age_humain_equi, self.date_arrivee, self.en_vie)
        return retour