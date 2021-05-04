from chien import Chien

class Chien_Aphone(Chien):
    #INITIALISATION
    def __init__(self, nom, age, ok_chats):
        super().__init__(nom, age, ok_chats)

    #METHODES
    def parler(self):
        print("{} aboie très bizzarement...!".format(self.nom))

    def __str__(self):
        retour = "CHIEN APHONE || nom : {}".format(self.nom)
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