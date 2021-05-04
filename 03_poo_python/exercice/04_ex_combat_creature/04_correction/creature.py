import random

class Creature :

    def __init__(self, nom, pdv, force, vitesse, armure):
        if (pdv + force + vitesse + armure) > 42 :
            raise ValueError()

        #if (pdv > 30 or pdv < 15):
        #   raise ValueError()

        self.__nom = nom
        self.__pdv = pdv
        self.__force = force
        self.__vitesse = vitesse
        self.__armure = armure
        self.__armure_max = armure
        self.__mode_esquive = False
        self.__mode_protection = False

    #Getter - Setter

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, value):
        self.__nom = value

    @property
    def pdv(self):
        return self.__pdv

    @property
    def force(self):
        return self.__force

    @property
    def vitesse(self):
        return self.__vitesse

    @property
    def armure(self):
        return self.__armure

    @property
    def taux_esquive(self):

        esquive = 2*self.vitesse

        if self.__mode_esquive:
            esquive += 50

        return esquive

    @property
    def est_ko(self):
        return self.__pdv <= 0

    #Methodes
    def attaquer (self, cible):
    
        degats = self.force

        if random.randint(1,100) <=5  :
            degats *= 2

        cible.subir_attaque(degats)

    def se_proteger(self):
        self.__armure = self.__armure_max
        self.__mode_protection = True

    def preparer_esquive(self):
        self.__mode_esquive = True

    def subir_attaque(self, degats):
        if random.randint(1,100) > self.taux_esquive:
            self.subir_degat(degats)

    def subir_degat(self, degats):
        if self.__mode_protection == True :
            degats /= 2

        if self.armure >= degats:
            self.__armure -= degats
        else:
            self.__pdv -= degats - self.__armure
            self.__armure = 0

    def terminer_tour(self):
        self.__mode_esquive = False
        self.__mode_protection = False

    def __str__(self):
        return f"{self.nom} (pdv : {self.pdv})"
