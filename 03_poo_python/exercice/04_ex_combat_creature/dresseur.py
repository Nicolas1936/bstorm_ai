import random
from creature import Creature

class Dresseur:
    #INITIALISATION
    def __init__(self, nom):
        self._nom = nom
        self._nb_creatures = []
        self._num_creature = 0

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, value):
        self._nom = value

    @property
    def nb_creatures(self):
        return self._nb_creatures

    @nb_creatures.setter
    def nb_creatures(self, value):
        self._nb_creatures = value

    @property
    def num_creature(self):
        return self._num_creature

    @num_creature.setter
    def num_creature(self, value):
        self._num_creature = value

    def __str__(self):
        return "NOM : {} || Num creature : {} | liste creature : {}".\
            format(self._nom, self._num_creature, self._nb_creatures)

    def ajout_creatures(self, creature):
        if isinstance(creature, Creature):
            if len(self._nb_creatures) <= 3:
                self._nb_creatures.append(creature)
            else:
                print("Désolé, le nombre de créature est au max (3)")
        
        else:
            print("Erreur : CreatureType incorrecte!")

    def attaque(self):
        pass

    def se_protege(self):
        creature = self.nb_creatures[self.num_creature]
        creature.armure = 

    def fin_se_protege(self):
        pass

    def esquive(self):
        creature = self.nb_creatures[self.num_creature]
        creature.vitesse = round(creature.vitesse * 1.5)

    def fin_esquive(self):
        creature = self.nb_creatures[self.num_creature]
        creature.vitesse = round(creature.vitesse / 1.5)

    def changer_creature(self):
        pass