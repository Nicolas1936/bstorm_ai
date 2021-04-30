class Personne: 

    #init
    def __init__(self, nom, prenom):
        self.__nom = nom
        self.__prenom = prenom

    #Getter - setter
    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, value):
        self.__nom = value

    @property
    def prenom(self):
        return self.__prenom

    @prenom.setter
    def prenom(self, value):
        self.__prenom = value

    #Methodes
    def faire_pause(self):
        print("{0} est en pause {1}".format(self, '15'))
        print(self," est en pause 15" )

    def __str__(self):
        return f"{self.prenom} {self.nom}"
    