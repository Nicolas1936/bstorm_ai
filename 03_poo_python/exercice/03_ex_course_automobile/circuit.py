class Circuit:
    #INITIALISATION
    def __init__(self, nom, distance):
        self._nom = nom
        self._distance = distance

    #GETTER / SETTER
    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, nom):
        self._nom = nom

    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, distance):
        self._distance = distance

    #METHODE
    def __str__(self):
        return "{} ({}) km".format(self.nom, self.distance)