from animal import Animal
from datetime import date

class Chat(Animal):
    #INITIATION
    def __init__(self, nom, age, ok_proprete):
        super().__init__(nom)
        self._ok_proprete = ok_proprete

        today = date.today().year
        super().naissance(today - age)

    #GETTER / SETTER
    @property
    def ok_proprete(self):
        return self._ok_proprete

    @ok_proprete.setter
    def ok_proprete(self, value):
        self._ok_proprete = value

    #METHODES
    def parler(self):
        print("{} miaule!".format(self.nom))

    def propre(self):
        if self.ok_proprete:
            print("{} est propre".format(self.nom))
        else:
            print("{} n'est pas propre... ;-(".format(self.nom))

    def __str__(self):
        retour = "CHAT || nom : {}".format(self.nom)
        if self.age:
            retour += " | age : {}".format(self.age)
        if self.en_vie:
            retour += " | est en vie!"
        elif self.en_vie == None:
            pass
        else:
            retour += " | n'est pas en vie! ;-("
        
        if self.ok_proprete:
            retour += " | est propre"
        else:
            retour += " | n'est pas propre..."
        return retour