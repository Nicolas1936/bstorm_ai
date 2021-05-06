from hero import Hero

class Humain(Hero):

    def __init__(self):
        super().__init__()
        self.force += 1
        self.endurance += 1