from student import Student
from teacher import Teacher
from classroom import Classroom

if __name__ == '__main__':

    manu = Student("Manu", "Vicca", "30-05-93")
    aurelien = Student("Aurelien", "Spitaels", "01-01-1995")

    piu = Teacher("Piu", "Li", "01-01-2010", "pi.li@bstorm.be")

    c = Classroom(piu, 3)

    c.ajout_etudiant(manu)
    c.ajout_etudiant(aurelien)

    c.debut_cours("Biologie")

