
class Concurrent:

    def __init__(self, nom, numero, voiture):
        self.__nom = nom
        self.__numero = numero
        self.__voiture = voiture
        self.__temps = list()   # secondes

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, value):
        self.__nom = value

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, value):
        self.__numero = value

    @property
    def voiture(self):
        return self.__voiture

    @voiture.setter
    def voiture(self, value):
        self.__voiture = value

    @property
    def temps_tour(self):
        return tuple(self.__temps)

    @property
    def temps_total(self):
        return sum(self.__temps)


    def realiser_tour(self, circuit):

        vit = self.voiture.obtenir_vitesse() / 3.6
        distance = circuit.distance

        temps = distance / vit
        self.__temps.append(temps)


    def se_decrire(self):

        desc_voiture = self.voiture.se_decrire()
        return "No {0} - {1} {2}".format(self.numero, self.nom, desc_voiture)

