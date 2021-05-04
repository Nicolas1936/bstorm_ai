from models.Course import Course
from models.Concurrent import Concurrent
from models.Voiture import Voiture
from models.Pilote import Pilote
from models.Circuit import Circuit
import datetime

if __name__ == "__main__":

    spa = Circuit("Spa", 7004, 20)

    c = Course("TechnoBel", spa, 50, 42)

    v_nico = Voiture("Audi", "R8", 180, 300)
    p_nico = Pilote("Hello", "Nico", datetime.date(1995, 1, 1))
    nico = Concurrent(7, p_nico, v_nico)
    c.ajouter_participant(nico)

    v_mh = Voiture("Tesla", "S", 220, 240)
    p_mh = Pilote("World", "Marc-Henry", datetime.date(1993, 1, 1), 50)
    mh = Concurrent(21, p_mh, v_mh)
    c.ajouter_participant(mh)

    c.ajouter_participant(Concurrent(10, Pilote("F", "Francois", datetime.date(1990, 1, 1), 70), Voiture("Porsche", "911", 220, 230)))

    c.demarrer_course()

    for concurrent in c.concurrents:
        print(concurrent.nom, datetime.timedelta(seconds=concurrent.temps_total))

    winner = c.obtenir_vainqueur()
    print(winner)
