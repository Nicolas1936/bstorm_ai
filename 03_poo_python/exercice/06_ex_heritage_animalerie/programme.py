from animal import Animal
from chat import Chat
from chien import Chien
from oiseau import Oiseau

def affiche():
    print("***********************************************************")

liste = [
            Chat("Mauli", 4, 30, "Femelle", 6, "02/01/2021", "calin", True, True),
            Chat("Mauli2", 4, 30, "Femelle", 8, "02/01/2021", "farouche", False, False),
            Chien('Luna', 20, 2, "Male", 11, "02/02/2018", "rouge", True, "Berger Allemand"),
            Chien('Luna2', 20, 2, "Male", 15, "02/12/2019", "noir", True, "Berger Français"),
            Chien('Luna3', 20, 2, "Femele", 18, "02/02/2015", "blanc", True, "Berger Belge"),
            Oiseau('PuiPui', 0.5, 0.2, "Masculin", 1, "03/03/2021", "jaune", False)
]

print()
affiche()
for animal in liste:
    print(animal)
    
print()
affiche()

print("NB DE CHAT : {} | NB DE CHIENS : {} | NB D'OISEAUX : {}".\
        format(Chat.NB_CHATS, Chien.NB_CHIENS, Oiseau.NB_OISEAUX))

affiche()

for i in range(3):
    for animal in liste:
        animal.passe_nuit()

    affiche()

print()
affiche()
for animal in liste:
    print(animal)

# a = Animal('Fleur', 10, 1.1, "male", 12, "01/01/2021")
# a.crie()
# print(a)
# a.passe_nuit()

# c = Chat("Mauli", 4, 30, "Femelle", 6, "02/01/2021", "calin", True, True)
# c.crie()
# print(c)
# c.passe_nuit()

# d = Chien('Luna', 20, 2, "Male", 15, "02/02/2018", "rouge", True, "Berger Allemand")
# d.crie()
# print(d)
# d.passe_nuit()

# o = Oiseau('PuiPui', 0.5, 0.2, "Masculin", 1, "03/03/2021", "jaune", False)
# o.crie()
# print(o)
# o.passe_nuit()