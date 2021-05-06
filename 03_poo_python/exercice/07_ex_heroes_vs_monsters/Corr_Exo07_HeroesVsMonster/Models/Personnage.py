from Models.De import De
from Tools.Generateur import Generateur


class Personnage:

    def __init__(self):
        self.__endurance = Generateur.getCarac()
        self.__force = Generateur.getCarac()
        self.__pdv = self.pdv_max
        self.__d4 = De(4)
        self.__d6 = De(6)

    # Props
    @property
    def endurance(self):
        return self.__endurance

    @property
    def force(self):
        return self.__force

    @property
    def pdv(self):
        return self.__pdv

    @pdv.setter
    def pdv(self, value):
        if value < self.pdv_max:
            self.__pdv = value
        else:
            self.__pdv = self.pdv_max

    @property
    def pdv_max(self):
        return self.__endurance + Generateur.getModificateur(self.__endurance)

    @property
    def d4(self):
        return self.__d4

    @property
    def d6(self):
        return self.__d6

    @property
    def race(self):
        return self.__class__.__name__

    # Methodes
    def estMort(self):
        return self.pdv <= 0

    def frappe(self, p):
        if not isinstance(p, Personnage):
            raise NameError("Le parametre p doit etre un personnage")

        degat = self.d4.lancer() + Generateur.getModificateur(self.force)
        p.__pdv = p.__pdv - degat
