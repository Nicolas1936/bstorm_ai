import random


class Voiture:

    def __init__(self, marque, model, vit_min, vit_max):
        self.__marque = marque
        self.__model = model
        self.__vit_min = vit_min
        self.__vit_max = vit_max

    @property
    def marque(self):
        return self.__marque

    @property
    def model(self):
        return self.__model

    @property
    def vit_min(self):
        return self.__vit_min

    @vit_min.setter
    def vit_min(self, value):
        self.__vit_min = value

    @property
    def vit_max(self):
        return self.__vit_max

    @vit_max.setter
    def vit_max(self, value):
        self.__vit_max = value

    def obtenir_vitesse(self):
        return random.randint(self.vit_min, self.vit_max)

    def se_decrire(self):
        return "{0} {1}".format(self.marque, self.model)
