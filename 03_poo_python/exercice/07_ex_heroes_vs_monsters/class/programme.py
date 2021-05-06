from humain import Humain
from nain import Nain
from dragonnet import Dragonnet
from orque import Orque
from loup import Loup


# h = Humain('h1')
# d = Dragonnet('d1')

# print("h : ", h)
# print("d : ", d)

# h.frappe(d)

# if not d.en_vie:
#     h.depouille(d)

# print("h : ", h)
# print("d : ", d)

# h.se_regenere()

def definir_personne(personnes):
    for personne in personnes:
        if personne.en_vie:
            return personne
    return False

heros = [
    Humain('Humain'),
    Nain('Nain')
]

monstres = [
    Dragonnet('Dragonnet'),
    Orque('Orque'),
    Loup('Loup')
]

while True:
    hero_actif = definir_personne(heros)
    monstre_actif = definir_personne(monstres)

    if not hero_actif:
        print("Tous les heros sont mort!")
        break

    if not monstre_actif:
        print("Tout les monstres sont mort!")
        print("Vous avez gagné!!!")
        break

    hero_actif.frappe(monstre_actif)
    
    if monstre_actif.en_vie:
        monstre_actif.frappe(hero_actif)
    else:
        hero_actif.depouille(monstre_actif)
        hero_actif.se_regenere()