from animal import Animal
from datetime import date

class Chien(Animal):
    #INITIALISATION
    def __init__(self, nom, age, ok_chats):
        super().__init__(nom)
        self._ok_chats = ok_chats
        
        today = date.today().year
        super().naissance(today - age)


    #GETTER / SETTER
    @property
    def ok_chats(self):
        return self._ok_chats

    @ok_chats.setter
    def ok_chats(self, value):
        self._ok_chats = value

    #METHODE
    def parler(self):
        print("{} aboie!".format(self.nom))

    def chats(self):
        if self.ok_chats:
            print("{} aime les chats".format(self.nom))
        else:
            print("{} a peur des chats".format(self.nom))

    def __str__(self):
        retour = "CHIEN || nom : {}".format(self.nom)
        if self.age:
            retour += " | age : {}".format(self.age)
        if self.en_vie:
            retour += " | est en vie!"
        elif self.en_vie == None:
            pass
        else:
            retour += " | n'est pas en vie! ;-("
        
        if self.ok_chats:
            retour += " | aime les chats"
        else:
            retour += " | a peur des chats"
        return retour
