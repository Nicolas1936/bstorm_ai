from chef import Chef

class Directeur(Chef):

    def __init__(self, nom, prenom, date_naissance, salaire, service, societe):
        super().__init__(nom, prenom, date_naissance, salaire, service)
        self._societe = societe

    def affiche(self):
        super().affiche()
        print("Société              : ", self._societe)


if __name__ == "__main__":
    d = Directeur("Blanchard", "Nicolas", "22/06/1983", 1000, "Informatique", "Microsoft")
    d.affiche()