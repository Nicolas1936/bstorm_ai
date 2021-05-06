from Models.Hero import Hero


class Humain(Hero):

    def __init__(self, nom):
        super().__init__(nom)

    @property
    def endurance(self):
        return super(Humain, self).endurance + 1

