#Exo1 - Class Student
class Student:

    def __init__(self, firstname, lastname, birthdate):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__matricule = firstname[-3:] + lastname[-3:]
        self.__birtdate = birthdate

    #getter - setter 
    @property
    def firstname(self):
        return self.__firstname

    @firstname.setter
    def firstname(self, value):
        self.__firstname = value
        self.__matricule = self.__firstname[-3:] + self.__lastname[-3:]
    
    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, value):
        self.__lastname = value
        self.__matricule = self.__firstname[-3:] + self.__lastname[-3:]

    @property
    def birthdate(self):
        return self.__birtdate

    @birthdate.setter
    def birthdate(self, value):
        self.__birthdate = value


    @property
    def matricule(self):
        return self.__matricule

    #methodes
    def secher(self):
        print(f"{self.firstname} {self.lastname} seche les cours.")

    def aller_en_cours(self, course):
        print(f"{self.firstname} {self.lastname} va en cours de {course}")