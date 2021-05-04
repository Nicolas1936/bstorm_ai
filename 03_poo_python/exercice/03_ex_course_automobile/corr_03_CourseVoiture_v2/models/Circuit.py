class Circuit:

    def __init__(self, nom, distance, max_place):
        self.__nom = nom
        self.__distance = distance  # en metre
        self.__max_place = max_place

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, value):
        self.__nom = value

    @property
    def distance(self):
        return self.__distance

    @distance.setter
    def distance(self, value):
        self.__distance = value

    @property
    def max_place(self):
        return self.__max_place

    def __str__(self):
        km = self.distance / 1000
        return "{0} - {1}km".format(self.nom, km)
