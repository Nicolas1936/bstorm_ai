from hero import Hero

class Nain(Hero):
    
    def __init__(self, nom):
        super().__init__(nom)
        self.endurance += 2