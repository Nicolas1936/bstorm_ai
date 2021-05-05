class Souris:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def pointe(self, x=0, y=0):
        self.x = x
        self.y = y

    def clique(self, fenetre):
        fenetre.click_action(self)
