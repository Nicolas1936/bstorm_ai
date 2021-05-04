class Course:

    def __init__(self, nom, circuit, nb_tour, prix):
        self.__nom = nom
        self.__circuit = circuit
        self.__nb_tour = nb_tour
        self.__prix = prix
        self.__concurrents = list()

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, value):
        self.__nom = value

    @property
    def nb_tour(self):
        return self.__nb_tour

    @nb_tour.setter
    def nb_tour(self, value):
        self.__nb_tour = value

    @property
    def prix(self):
        return self.__prix

    # Possibilité de l'augementer uniquement
    @prix.setter
    def prix(self, value):
        if value < self.__prix:
            raise ValueError()

        self.__prix = value

    @property
    def circuit(self):
        return self.__circuit

    @property
    def concurrents(self):
        # Tuple => Non modifiable
        # Créer une copie de la collection
        return tuple(self.__concurrents)


    def ajouter_participant(self, concurrent):
        if(concurrent == None):
            return

        self.__concurrents.append(concurrent)


    def demarrer_course(self):

        for i in range(self.nb_tour):

            for concurrent in self.__concurrents:

                concurrent.realiser_tour(self.circuit)


    def obtenir_vainqueur(self):

        winner = self.__concurrents[0]
        for concurrent in self.__concurrents:

            if concurrent.temps_total < winner.temps_total:
                winner = concurrent

        return winner


