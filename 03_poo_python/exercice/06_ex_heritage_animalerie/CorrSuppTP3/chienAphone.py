from chien import Chien

class ChienAphone(Chien):

    def __init__(self, ok_chat, nom, age):
        super().__init__(ok_chat, nom, age)

    def Parler(self):
        print(f"{self.nom} : * ")

    def __str__(self):
        return f"{super().__str__()}\nEst aphone : True"

    
    