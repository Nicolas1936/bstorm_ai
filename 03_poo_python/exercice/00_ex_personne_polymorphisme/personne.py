class Personne:
    #INITIALISATION
    def __init__(self, nom, prenom, date_naissance):
        self._nom = nom
        self._prenom = prenom
        self._date_naissance = date_naissance

    def affiche(self):
        print("Nom                  : ", self._nom)
        print("Prenom               : ", self._prenom)
        print("Date de naissance    : ", self._date_naissance)


if __name__ == '__main__':
    p = Personne("Blanchard", "Nicolas", "22/06/1983")
    p.affiche()