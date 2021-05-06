import random

class Des:
    
    def __init__(self, min, max):
        self.min = min
        self.max = max

    def lancer_des(self, nb_des=1):
        if nb_des > 0:
            if nb_des == 1:
                return random.randint(self.min, self.max)
            else:
                return [random.randint(self.min, self.max) for i in range(nb_des)]


    def calcul_force_endurance(self):
        liste = self.lancer_des(4)
        liste.sort(reverse=True)
        points = sum(liste[:3])
        return points