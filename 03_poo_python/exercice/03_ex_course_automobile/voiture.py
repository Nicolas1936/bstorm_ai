import random

class Voiture:
    #INITIALISATION
    def __init__(self, nom,  v_min, v_max):
        self._nom = nom
        self._v_min = v_min
        self._v_max = v_max
    
    #GETTER / SETTER
    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, nom):
        self._nom = nom

    @property
    def v_min(self):
        return self._v_min

    @v_min.setter
    def v_min(self, v_min):
        self._v_min = v_min

    @property
    def v_max(self):
        return self._v_max

    @v_max.setter
    def v_max(self, v_max):
        self._v_max = v_max

    #METHODE
    def v_moy(self):
        return random.randint(self.v_min, self.v_max)

    def __str__(self):
        return self.nom