from student import Student
from teacher import Teacher
from classroom import Classroom

david = Teacher("David", "Puippe", "01/01/2001", "david@gmail.com")

one = Classroom(10, david)

nico = Student("Nicolas", "Blanchard", "22/06/1983")
kath = Student("Kathleen", "Vlamynck", "22/06/1983")

one.ajout_student(nico)
one.ajout_student(kath)
one.ajout_student(Student("Pierre", "Dupont", "01/01/2000"))
one.ajout_student(Student("Marie", "Lenoire", "01/01/2000"))
one.commencer_cours("Math")
one.ajout_student(Student("Zack", "Trump", "01/01/2000"))
one.commencer_cours("Math")

print("Liste de cours de Math : ")
print(one.liste_etudiants)
print()

nico.aller_en_cours("Math")
kath.seche()

david.donne_cours("Anglais")

one.ajout_student('string')