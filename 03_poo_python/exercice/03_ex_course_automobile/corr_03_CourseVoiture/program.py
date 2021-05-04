from models.Course import Course
from models.Concurrent import Concurrent
from models.Voiture import Voiture
from models.Circuit import Circuit

if __name__ == "__main__":

    spa = Circuit("Spa", 7004, 20)

    c = Course("TechnoBel", spa, 5, 42)

    v_nico = Voiture("Audi", "R8", 180, 260)
    nico = Concurrent("Nico", 7, v_nico)
    c.ajouter_participant(nico)

    mh = Concurrent("Marc-Henry", 21, Voiture("Tesla", "S", 220, 240))
    c.ajouter_participant(mh)

    c.ajouter_participant(Concurrent("François", 10, Voiture("Porsche", "911", 225, 230 )))


    c.demarrer_course()

    for concurrent in c.concurrents:
        print(concurrent.nom, concurrent.temps_total)


    winner = c.obtenir_vainqueur()
    print(winner.se_decrire())

