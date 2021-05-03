#Exo1 - Class Teacher
class Teacher:

    def __init__(self, firstname, lastname, embauche, email):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__embauche = embauche
        self.__email = email

    #Getter - Setter

    ##firstname
    @property
    def firstname(self):
        return self.__firstname

    @firstname.setter
    def firstname(self, value):
        self.__firstname = value
    #lastname
    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, value):
        self.__lastname = value 

    #embauche
    @property
    def embauche(self):
        return self.__embauche

    @embauche.setter
    def embauche(self, value):
        self.__embauche = value 

    #email
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    # ------------------------------------------ #

    #methodes
    def donner_cours(self, course):
        print(f"{self.firstname} {self.lastname} donne le cours de {course}")
