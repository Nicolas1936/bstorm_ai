# import Models.De as De
from Models.De import De


class Generateur:

    @staticmethod
    def getCarac():
        de = De(6)
        stats = []
        nb_de = 4

        i = 0
        while i < nb_de:
            stats.append(de.lancer())
            i += 1

        if __name__ == '__main__':
            print(stats)

        stats.sort()
        stats.remove(stats[0])

        if __name__ == '__main__':
            print(stats)

        total = 0
        for item in stats:
            total += item

        return total

    @staticmethod
    def getModificateur(valeur):
        if valeur < 5:
            modif = -1
        elif valeur < 10:
            modif = 0
        elif valeur < 15:
            modif = 1
        else:
            modif = 2

        return modif


if __name__ == '__main__':
    stats = Generateur.getCarac()
    print('Stats', stats)
    modif = Generateur.getModificateur(stats)
    print('Modif', modif)
