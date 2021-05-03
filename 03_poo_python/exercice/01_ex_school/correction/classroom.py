from student import Student
from teacher import Teacher
import random

class Classroom :
    
    def __init__(self, prof, nb_place, students = []):
        self.__nb_place = nb_place
        self.__prof = prof
        self.__students = []

    #prof
    @property
    def prof(self):
        return self.__prof

    @prof.setter
    def prof(self, value):
        if isinstance(value, Teacher) :
            self.__prof = value
        
    #nb_place
    @property
    def nb_place(self):
        return self.__nb_place

    @nb_place.setter
    def nb_place(self, value):
        self.__nb_place = value

    #studens
    @property
    def students(self):
        return self.__students

    @students.setter
    def students(self, value):
        self.__students = value

    #methodes

    def ajout_etudiant(self, new_student):

        if isinstance(new_student, Student):
            if self.nb_place > len(self.students):
                self.students.append(new_student)
            else:
                print("pas ajouté")
                pass

    def debut_cours(self, cours):
        
        if len(self.students) > (self.nb_place / 2):
            #1. prof donner cours
            self.prof.donner_cours(cours)

            #2. Etudiants vont (ou pas) en cours
            for student in self.students:
                if random.randint(0,10)>2:
                    student.aller_en_cours(cours)
                else :
                    student.secher()

                
        


    