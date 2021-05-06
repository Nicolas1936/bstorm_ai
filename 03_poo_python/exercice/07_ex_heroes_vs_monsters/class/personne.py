import random
from des import Des

class Personne:

    #***********************************************
    # INITIALISATION
    #***********************************************

    def __init__(self, nom):
        self._nom = nom
        
        de = Des(1, 6)

        self._force = de.calcul_force_endurance()
        self._endurance = de.calcul_force_endurance()
        self._point_de_vie = self.modificateur(self.endurance)

        self._en_vie = True

        self._or = 0
        self._cuir = 0
        self._point_de_vie_max = self._point_de_vie

    #***********************************************
    # GETTER / SETTER
    #***********************************************

    #FORCE
    @property
    def force(self):
        return self._force

    @force.setter
    def force(self, value):
        self._force = value

    #ENDURANCE
    @property
    def endurance(self):
        return self._endurance

    @endurance.setter
    def endurance(self, value):
        self._endurance = value

    #POINT DE VIE
    @property
    def point_de_vie(self):
        return self._point_de_vie

    @point_de_vie.setter
    def point_de_vie(self, value):
        self._point_de_vie = value

    #EN VIE
    @property
    def en_vie(self):
        return self._en_vie

    @en_vie.setter
    def en_vie(self, value):
        self._en_vie = value

    #NOM
    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, value):
        self._nom = value

    #***********************************************
    # METHODE
    #***********************************************

    #MODIFICATEUR
    def modificateur(self, caracteristique):
        points = 0
        if caracteristique < 5:
            points = caracteristique - 1

        elif caracteristique < 10:
            points = caracteristique

        elif caracteristique < 15:
            points = caracteristique + 1

        else:
            points = caracteristique + 2

        return points

    #FRAPPE
    def frappe(self, player2):
        des = random.randint(1, 4)
        points_degats = des + self.modificateur(self.force)
        print("{} frappe {}".format(self.nom, player2.nom))
        player2.degats(points_degats)

    #DEGATS
    def degats(self, points_degats):
        if self.point_de_vie > points_degats:
            self.point_de_vie -= points_degats
            print("{} perd {} de point de vie. (pdv:{})".\
                format(self.nom, points_degats, self.point_de_vie))
        else:
            self.point_de_vie = 0
            self._en_vie = False
            print("{} est mort!".format(self.nom))

    
    def __str__(self):
        return "NOM : {} || For : {} | End : {} | PV : {} | en vie : {} | OR : {} | CUIR | {}".\
            format(self._nom, self.force, self.endurance, self.point_de_vie, self.en_vie, self._or, self._cuir)


if __name__ == "__main__":
    p = Personne()

    print(p)

    