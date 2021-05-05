class Lampe:

    def __init__(self):
        self.lumiere = False
    
    def ChangerEtat(self):
        self.lumiere = not self.lumiere
        return self.lumiere

    def __str__(self):
        return f"Lampe : {self.lumiere}"

