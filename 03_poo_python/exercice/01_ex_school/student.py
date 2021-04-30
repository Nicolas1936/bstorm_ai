from person import Person

class Student(Person):

    #INITIALISATION
    def __init__(self, prenom, nom, birthdate):
        super().__init__(prenom, nom)
        self.__matricule = (nom[-3:] + prenom[-3:]).upper()
        self.__birthdate = birthdate

    # def __str__(self):
    #     output = "{} {}".format(self.prenom, self.nom)
    #     return output

    #GETTER / SETTER
    @property
    def matricule(self):
        return self.__matricule

    @matricule.setter
    def matricule(self, matricule):
        self.__matricule = matricule

    @property
    def birthdate(self):
        return self.__birthdate

    @birthdate.setter
    def birthdate(self, birthdate):
        self.__birthdate = birthdate

    #METHODE
    def seche(self):
        print("{} {} seche un cours!".format(self.prenom, self.nom))

    def aller_en_cours(self, cours):
        print("{} {} va en cours de {}.".format(self.prenom, self.nom, cours))