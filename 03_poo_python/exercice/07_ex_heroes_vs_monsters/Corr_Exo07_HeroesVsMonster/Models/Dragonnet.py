from Models.Monstre import Monstre
from Interfaces.ICuir import ICuir
from Interfaces.IOr import IOr


class Dragonnet(Monstre, ICuir, IOr):

    def __init__(self):
        super().__init__()
        self.__cuir = self.d4.lancer()
        self.__piece_or = self.d6.lancer()

    @property
    def endurance(self):
        return super(Dragonnet, self).endurance + 1

    @property
    def piece_or(self):
        return self.__piece_or

    @property
    def cuir(self):
        return self.__cuir

