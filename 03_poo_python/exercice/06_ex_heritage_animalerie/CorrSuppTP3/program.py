from animal import Animal
from chien import Chien
from chat import Chat
from chienAphone import ChienAphone

animaux = []

animaux.append(Animal("kiki"))
animaux.append(Chien(True, "Medor", 5))
animaux.append(Chat(False, "poupouss", 2))
animaux.append(ChienAphone(False, "kwtech", 15))

for animal in animaux:
    print(animal)
    animal.Parler()
    print("=========================================")

