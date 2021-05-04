class Dresseur:

    limite_creature = 3

    def __init__(self, nom):
        self.__nom = nom
        self.__creatures = list()
        self.__creature_active = None

    @property
    def nom(self):
        return self.__nom

    @property
    def creatures(self):
        return tuple(self.__creatures)

    @property
    def creature_active(self):
        return self.__creature_active

    @property
    def nb_creature(self):
        return len(self.__creatures)

    @property
    def est_vaincu(self):

        vaincu = True
        i = 0
        while vaincu == True and i < len(self.__creatures):
            if not self.__creatures[i].est_ko:
                vaincu = False
            i +=1
        return vaincu

    def ordonner_attaque(self, creature):
        self.__creature_active.attaquer(creature)

    def ordonner_esquive(self):
        self.creature_active.preparer_esquive()

    def ordonner_defense(self):
        self.__creature_active.se_proteger()
        
    def changer_creature(self, position):

        if not self.__creatures[position].est_ko:
            self.__creature_active = self.creatures[position]
            return True
        
        return False

    def ajouter_creature(self, creature):
        if len(self.__creatures) < self.limite_creature:
            self.__creatures.append(creature)

    def debuter_match(self):
        en_cours = True
        i = 0

        while en_cours : 
            if not self.__creatures[i].est_ko:
                self.__creature_active = self.__creatures[i]
                en_cours = False
            i += 1

    def terminer_match(self):
        self.__creature_active = None

    def __str__(self):
        compteur = 0
        for creature in self.__creatures:
            if not creature.est_ko:
                compteur +=1
        
        return f"{self.nom} possède {len(self.__creatures)} dont {compteur} est/sont encore en vie."


