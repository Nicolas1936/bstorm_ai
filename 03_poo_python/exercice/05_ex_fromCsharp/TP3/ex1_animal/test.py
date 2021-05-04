from animal import Animal
from chien import Chien
from chat import Chat
from chien_aphone import Chien_Aphone

# a = Animal('Tweeky')
# print(a)

# a.naissance(2000)
# print(a)

# a.respirer()
# a.vieillir()
# a.vieillir(5)
# print(a)

# a.vieillir()
# a.deces()
# print(a)

# c = Chien("Luna", 5, True)
# print(c)

# c.parler()
# c.chats()

# d = Chat("Maouli", 2, True)
# print(d)

# d.parler()
# d.propre()

liste = [   Animal('Fox'),
            Chat('Miauli', 15, True),
            Chat('Miauli2', 11, False),
            Chien('Luna', 2, True),
            Chien('Luna2', 4, False),
            Chien_Aphone('Sun', 6, True)
]

# for animal in liste:
#     animal.respirer()
#     animal.parler()
#     animal.vieillir(10)
#     print(animal)
#     animal.deces()

for animal in liste:
    animal.respirer()

for animal in liste:
    animal.parler()

for animal in liste:
    animal.vieillir(5)

for animal in liste:
    print(animal)

for animal in liste:
    animal.deces()

for animal in liste:
    print(animal)

c = liste[3]
c.vieillir(20)
print(c)
print(liste[3])