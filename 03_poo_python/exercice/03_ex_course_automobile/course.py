from voiture import Voiture
from circuit import Circuit

class Course:
    #INITIALISATION
    def __init__(self, circuit, nb_tour_total):
        self._nb_tour_total = nb_tour_total
        self._tab_voitures = []
        self._tab_temps_v = []
        self._circuit = circuit

    #GETTER / SETTER
    @property
    def nb_tour_total(self):
        return self._nb_tour_total

    @nb_tour_total.setter
    def nb_tour_total(self, nb_tour_total):
        self._nb_tour_total = nb_tour_total

    #METHODE
    def ajout_voiture(self, voiture):
        self._tab_voitures.append(voiture)
        self._tab_temps_v.append(0)

    def start(self):
        print("LA COURSE DEMARRE!")
        for j in range(self.nb_tour_total):
            for i in range(len(self._tab_voitures)):
                tmp = round(self._circuit.distance / self._tab_voitures[i].v_moy())
                print("TOUR {} : La voiture {} à fait un temps de : {}".format(j, self._tab_voitures[i], tmp))
                self._tab_temps_v[i] += tmp

        max_value = max(self._tab_temps_v)
        max_index = self._tab_temps_v.index(max_value)

        print("LE VAINQUEUR EST LA VOITURE {} AVEC UN TEMPS TOTAL DE {}".format(self._tab_voitures[max_index], max_value))