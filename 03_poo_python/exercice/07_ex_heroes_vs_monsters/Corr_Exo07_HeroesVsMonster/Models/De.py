import random


class De:

    def __init__(self, maximum):
        self.__minimum = 1
        self.__maximum = maximum

    # Props en lecteur
    @property
    def minimum(self):
        return self.__minimum

    @property
    def maximum(self):
        return self.__maximum

    # Methode
    def lancer(self):
        return random.randint(self.minimum, self.maximum)


if __name__ == '__main__':
    de = De(6)
    test = de.lancer()
    print(test)
