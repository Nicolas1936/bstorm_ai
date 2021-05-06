from animal import Animal

class Chat(Animal):

    def __init__(self, ok_propreté, nom, age):
        super().__init__(nom)
        self.ok_propreté = ok_propreté
        self.age = age


    def Parler(self):
        print(f"{self.nom} : Miawou !")

    def __str__(self):
        return f"{super().__str__()} \nPropre : {self.ok_propreté}"
    

