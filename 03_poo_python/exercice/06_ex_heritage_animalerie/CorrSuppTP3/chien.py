from animal import Animal

class Chien(Animal):

    def __init__(self, ok_chat, nom, age):
        super().__init__(nom)
        self.ok_chat = ok_chat
        self.age = age
        #super().age = age -> erreur

    def Parler(self):
        print(f"{self.nom} : Wouaf !")

    def __str__(self):
        return f"{super().__str__()} \nChats ok : {self.ok_chat}"
    



