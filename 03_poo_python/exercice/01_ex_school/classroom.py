from student import Student

class Classroom:

    #INITIALISATION
    def __init__(self, nbr_place, teacher):
        self.__nbr_place = nbr_place
        self.__liste_etudiants = []
        self.__teacher = teacher

    #GETTER / SETTER
    @property
    def nbr_place(self):
        return self.__nbr_place

    @nbr_place.setter
    def nbr_place(self, nbr_place):
        self.__nbr_place = nbr_place

    @property
    def liste_etudiants(self):
        return self.__liste_etudiants

    @liste_etudiants.setter
    def liste_etudiants(self, liste_etudiants):
        self.__liste_etudiants = liste_etudiants

    #METHODES
    def ajout_student(self, student):
        test_etudiant = isinstance(student, Student)
        if test_etudiant:
            self.liste_etudiants.append(student)
            print("l'étudiant {} {} à bien été ajouté".format(student.prenom, student.nom))
        else:
            print("Erreur : Veuillez passez un étudiant en parametre...")

    def commencer_cours(self, cours):
        if len(self.liste_etudiants) > 4:
            print("le cours {} débute :\n".format(cours))
            print("PROF : {} {}".format(self.__teacher.prenom, self.__teacher.nom))
            print("STUDENTS")
            for k, v in enumerate(self.__liste_etudiants):
                print("{}| {} {}".format(k+1, v.prenom, v.nom))

        else:
            print("Désolé, le cours ne peux se faire, il n'y a pas assez d'élève")
            print("Nbres d'élèves : ", len(self.liste_etudiants))