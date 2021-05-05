class Voiture:

    def __init__(self, vitesse=0):
        self._vitesse = vitesse

    def plus_v(self, nb_vitesse=1):
        if self._vitesse < 6 :
            self._vitesse += nb_vitesse
            print("vitesse :", self._vitesse)
        else:
            print("Desole, vitesse au maximum")
        return None

    def moins_v(self, nb_vitesse=1):
        if self._vitesse > 0 :
            self._vitesse -= nb_vitesse
            print("vitesse :", self._vitesse)
        else:
            print("Desole, vitesse au minimum")
        return None


if __name__ == '__main__':

    v = Voiture(3)

    v.moins_v()
    v.moins_v(2)
    v.moins_v()
    v.moins_v()