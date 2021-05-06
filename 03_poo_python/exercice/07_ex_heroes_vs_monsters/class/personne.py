import random
from des import Des

class Personne:

    def __init__(self):
        de = Des(1, 6)

        self.force = de.calcul_force_endurance()
        self.endurance = de.calcul_force_endurance()
        self.point_de_vie = self.modificateur(self.endurance)

    def modificateur(self, caracteristique):
        points = 0
        if caracteristique < 5:
            points = caracteristique - 1

        elif caracteristique < 10:
            points = caracteristique

        elif caracteristique < 15:
            points = caracteristique + 1

        else:
            points = caracteristique + 2

        return points

    def frappe(self, player2):
        des = random.randint(1, 4)
        points_degats = des + modificateur(self.force)
        player2.degats(points_degats)

    def degats(self, points_degats):
        self.point_de_vie -= points_degats

    
    def __str__(self):
        return "For : {} | End : {} | PV : {}".\
            format(self.force, self.endurance, self.point_de_vie)


if __name__ == "__main__":
    p = Personne()

    print(p)

    