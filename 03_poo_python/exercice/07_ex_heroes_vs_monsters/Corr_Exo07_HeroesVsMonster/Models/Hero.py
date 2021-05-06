from Models.Personnage import Personnage
from Interfaces.IOr import IOr
from Interfaces.ICuir import ICuir


class Hero(Personnage, IOr, ICuir):

    def __init__(self, nom):
        super().__init__()
        self.__piece_or = 0
        self.__cuir = 0
        self.__nom = nom

    # Props
    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, nom):
        self.__nom = nom

    @property
    def piece_or(self):
        return self.__piece_or

    @property
    def cuir(self):
        return self.__cuir

    # Methodes
    def loot(self, monstre):
        if isinstance(monstre, IOr):
            self.__piece_or += monstre.piece_or

        if isinstance(monstre, ICuir):
            self.__cuir += monstre.cuir

    def seReposer(self):
        self.pdv = self.pdv_max
