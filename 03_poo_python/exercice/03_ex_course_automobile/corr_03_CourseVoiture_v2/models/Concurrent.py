
class Concurrent:

    def __init__(self, numero, pilote, voiture):
        self.__nom = pilote.nom_complet
        self.__numero = numero
        self.__pilote = pilote
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
    def pilote(self):
        return self.__pilote

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

        vit_voiture = self.voiture.obtenir_vitesse() / 3.6
        vit_coef = (vit_voiture * (self.pilote.exp / 100)) / 10
        vit = vit_voiture + vit_coef

        distance = circuit.distance

        temps = distance / vit
        self.__temps.append(temps)

        self.pilote.gagner_exp(3)


    def __str__(self):
        return "No {0} - {1} {2}".format(self.numero, self.nom, self.voiture)

