import random

class Creature:
    #INITIALISATION
    def __init__(self, nom):
        flag = True
        
        while flag:
            self._nom = nom
            self._force = random.randint(1, 10)
            self._armure = random.randint(0, 10)
            self._vitesse = random.randint(1, 10)
            self._point_vie = random.randint(15, 30)

            if self._force + self._armure + self._vitesse + self._point_vie <= 42:
                flag = False

    #GETTER / SETTER
    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, value):
        self._nom = value

    @property
    def force(self):
        return self._force

    @force.setter
    def force(self, value):
        self._force = value

    @property
    def armure(self):
        return self._armure

    @armure.setter
    def armure(self, value):
        self._armure = value

    @property
    def vitesse(self):
        return self._vitesse

    @vitesse.setter
    def vitesse(self, value):
        self._vitesse = value

    @property
    def point_vie(self):
        return self._point_vie

    @point_vie.setter
    def point_vie(self, value):
        self._point_vie = value

    def __str__(self):
        return "NOM : {} || Force : {} | Armure : {} | Vitesse : {} | Point de vie : {}".\
            format(self._nom, self._force, self._armure, self._vitesse, self._point_vie)


    def validation(self, force, armure, vitesse):
        if self._force + self._armure + self._vitesse + self._point_vie <= 42:
            return True
        return False


if __name__ == '__main__':

    c = Creature("Pikachu")
    print(c)