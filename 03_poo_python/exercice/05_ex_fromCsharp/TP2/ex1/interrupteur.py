class Interrupteur:

    def __init__(self):
        self.ouvert = True

    def switch(self, lampe):
        self.ouvert = not lampe.ChangerEtat()
    
    def __str__(self):
        return f"Interrupteur : {self.ouvert}"