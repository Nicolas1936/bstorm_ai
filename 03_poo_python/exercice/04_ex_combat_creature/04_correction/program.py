from creature import Creature  
from dresseur import Dresseur
import random

def choisir_creature(dresseur):
    terminer = False
    while not terminer : 
        position = random.randrange(0,dresseur.nb_creature)
        terminer = dresseur.changer_creature(position)



d1 = Dresseur("Sacha")
d1.ajouter_creature(Creature("pikachu", 20, 5 ,8 ,4))
d1.ajouter_creature(Creature("salameche", 21, 3 ,7 ,8))
d1.ajouter_creature(Creature("poke1", 26, 6 ,6,2))

d2 = Dresseur("Ondine")
d2.ajouter_creature(Creature("poke2", 20, 5 ,8 ,4))
d2.ajouter_creature(Creature("poke3", 21, 3 ,7 ,8))
d2.ajouter_creature(Creature("poke4", 26, 6 ,6,2))

d1.debuter_match()
d2.debuter_match()

print(f"combat entre {d1.nom} et {d2.nom} :")
print(f"{d1.nom} : {d1.creature_active}")
print(f"{d2.nom} : {d2.creature_active}")
print()

j=0

while not d1.est_vaincu or not d2.est_vaincu:

    #changer = 0, esquiver = 1, proteger = 2, attaquer = 3
    choix1 = random.randrange(0,4)
    choix2 = random.randrange(0,4)

    #changement 0
    if choix1 == 0:
        choisir_creature(d1)
        print(f"{d1.nom} change de creature")
    if choix2 == 0:
        choisir_creature(d2)
        print(f"{d2.nom} change de creature")

    #esquive 1
    if choix1 == 1:
        d1.ordonner_esquive()
        print(f"{d1.nom} ordonne une esquive")
    if choix2 == 1:
        d1.ordonner_esquive()
        print(f"{d2.nom} ordonne une esquive")

    #esquive 2
    if choix1 == 2:
        d1.ordonner_esquive()
        print(f"{d1.nom} ordonne une protection")
    if choix2 == 2:
        d2.ordonner_esquive()
        print(f"{d2.nom} ordonne une protection")

    
    #attaque 3
    if choix1 == 3 and choix2 == 3 :
        print(f"Les deux dresseurs ordonnent d'attaquer")

        if d1.creature_active.vitesse > d2.creature_active.vitesse:
            d_prio = d1
            d_sec = d2

        else : 
            d_prio = d2
            d_sec = d1

        d_prio.ordonner_attaque(d_sec.creature_active)
        if not d_sec.creature_active.est_ko:
            d_sec.ordonner_attaque(d_prio.creature_active)

    elif choix1 == 3:
        print(f"{d1.nom} attaque !")
        d1.ordonner_attaque(d2.creature_active)

    elif choix2 == 3:
        print(f"{d2.nom} attaque !")
        d2.ordonner_attaque(d1.creature_active)

    d1.creature_active.terminer_tour()
    d2.creature_active.terminer_tour()

    if( not d1.est_vaincu and d1.creature_active.est_ko):
        print(f"{d1.creature_active} de {d1.nom} est KO")
        choisir_creature(d1)
        print(f"{d1.creature_active} rentre en jeu")
    
    if( not d2.est_vaincu and d2.creature_active.est_ko):
        print(f"{d2.creature_active} de {d2.nom} est KO")
        choisir_creature(d2)
        print(f"{d2.creature_active} rentre en jeu")

    j+=1
    print(f"-fin de tour {j}-")

d1.terminer_match()
d2.terminer_match()

if d1.est_vaincu:
    print(f"{d2} gagne la partie")

else:
    print(f"{d1} gagne la partie")
