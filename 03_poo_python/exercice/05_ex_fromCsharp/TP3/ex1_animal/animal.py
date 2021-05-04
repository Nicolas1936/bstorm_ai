from datetime import date

class Animal:
    #INITIALISATION
    def __init__(self, nom):
        self._nom = nom
        self._age = 0
        self._en_vie = None

    #GETTER / SETTER
    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, value):
        self._nom = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @property
    def en_vie(self):
        return self._en_vie

    @en_vie.setter
    def en_vie(self, value):
        self._en_vie = value

    #METHODE
    def naissance(self, annee):
        today = date.today().year
        self.age = today - annee
        #self.respirer()
        print("{} est né en {}, il a donc {} ans".format(self.nom, annee, self.age))

    def respirer(self):
        self.en_vie = True
        print("{} respire".format(self.nom))

    def parler(self):
        print("{} fait un bruit".format(self._nom))

    def vieillir(self, nb_annee=1):
        self.age += nb_annee
        print("{} vieilli de {} année(s), il a donc {}".format(self.nom, nb_annee, self.age))

    def deces(self):
        self.en_vie = False
        print("{} n'est plus en vie... ;-(".format(self.nom))

    def __str__(self):
        retour = "ANIMAL || nom : {}".format(self._nom)
        if self.age:
            retour += " | age : {}".format(self._age)
        if self.en_vie:
            retour += " | est en vie!"
        elif self.en_vie == None:
            pass
        else:
            retour += " | n'est pas en vie! ;-("
        return retour

