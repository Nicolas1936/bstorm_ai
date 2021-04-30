from person import Person

class Teacher(Person):

    #INITIALISATION
    def __init__(self, prenom, nom, date_embauche, email):
        super().__init__(prenom, nom)
        self.__date_embauche = date_embauche
        self.__email = email

    def __str__(self):
        output = "{} {}".format(self.prenom, self.nom)
        return output

    #GETTER / SETTER
    @property
    def date_embauche(self):
        return self.__date_embauche

    @date_embauche.setter
    def date_embauche(self, date_embauche):
        self.__date_embauche = date_embauche

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    #METHODE
    def donne_cours(self, cours):
        print("{} {} donne le cours de {}.".format(self.prenom, self.nom, cours))