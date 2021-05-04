class Employe:
    tarif_horaire = 25
    #INITIALISATION
    def __init__(self, nom, heure_hebdo=38):
        if heure_hebdo < 1:
            raise ValueError("Erreur : nombre d'heure de travail hebdomadaire trop petit (>=1)")
        
        if heure_hebdo > 168:
            raise ValueError("Erreur : nombre d'heure de travail hebdomadaire trop grand (<=168)")
        self.nom = nom
        self.heure_hebdo = heure_hebdo

    #METHODES
    def get_salaire(self):
        salaire = self.heure_hebdo * Employe.tarif_horaire
        return "EMPLOYE || nom : {} | heure hebdomadaire : {} | salaire : {}".\
            format(self.nom, self.heure_hebdo, salaire)

    def __str__(self):
        return "{} de classe Employe est de type : {}".format(self.nom, type(self))

if __name__ == "__main__":

    liste = [
                Employe('Freddy'),
                Employe('Anna', 50)
    ]

    for employe in liste:
        print(employe.get_salaire())

    for employe in liste:
        print(employe)