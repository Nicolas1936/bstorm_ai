from Models.Hero import Hero


class Nain(Hero):

    def __init__(self, nom):
        super().__init__(nom)

    @property
    def endurance(self):
        return super(Nain, self).endurance + 2
