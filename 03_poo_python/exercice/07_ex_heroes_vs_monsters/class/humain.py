from hero import Hero

class Humain(Hero):

    def __init__(self, nom):
        super().__init__(nom)
        self.force += 1
        self.endurance += 1