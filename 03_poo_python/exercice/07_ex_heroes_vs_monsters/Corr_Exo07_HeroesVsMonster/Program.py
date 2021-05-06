from Models.Nain import Nain
from Models.Humain import Humain
from Models.Orque import Orque
from Models.Loup import Loup
from Models.Dragonnet import Dragonnet
from Models.De import De


if __name__ == '__main__':
    joueur = input("Quel est nom de Hero : ")

    race = None
    while race == None:
        choix = input("Etes vous un Humain (1) ou un Nain (2) : ")
        if(choix.isdigit()):
            choix_int = int(choix)
            if(choix_int == 1 or choix_int == 2):
                race = choix_int
            else:
                print("Choix incorrect")
        else:
            print("Vous devez choisir soit 1 ou 2...")


    # Ternaire degeux
    hero = Humain(joueur) if race == 1 else Nain(joueur)

    print("Votre", hero.race, "- force :", hero.force, " / endurance :", hero.endurance, " / pdv :", hero.pdv)
    print()

    d2 = De(2)
    d3 = De(3)
    while not hero.estMort():

        choix_monstre = d3.lancer()
        if(choix_monstre == 1):
            creature = Loup()
        elif choix_monstre == 2:
            creature = Orque()
        else:
            creature = Dragonnet()

        print("Votre hero rencontre un", creature.race,"!")

        initiative = d2.lancer() == 1
        while not hero.estMort() and not creature.estMort():
            if initiative:
                hero.frappe(creature)
                print("Le hero attaque !")
            else:
                creature.frappe(hero)
                print("Le", creature.race, "attaque !")

            initiative = not initiative

        if not hero.estMort():
            print(hero.nom,"a vaincu le", creature.race)
            hero.loot(creature)
            hero.seReposer()

        print()

    print("Le hero est mort!")
    print("Butin :", hero.piece_or, " pieces d'or,", hero.cuir, "cuirs");