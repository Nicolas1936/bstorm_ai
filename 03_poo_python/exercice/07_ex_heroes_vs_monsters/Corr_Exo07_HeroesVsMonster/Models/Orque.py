from Models.Monstre import Monstre
from Interfaces.IOr import IOr


class Orque(Monstre, IOr):

    def __init__(self):
        super().__init__()
        self.__piece_or = self.d6.lancer()

    @property
    def force(self):
        return super(Orque, self).force + 1

    @property
    def piece_or(self):
        return self.__piece_or

