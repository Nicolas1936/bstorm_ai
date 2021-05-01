from employe import Employe

class Chef(Employe):

    def __init__(self, nom, prenom, date_naissance, salaire, service):
        super().__init__(nom, prenom, date_naissance, salaire)
        self._service = service

    def affiche(self):
        super().affiche()
        print("Service              : ", self._service)


if __name__ == "__main__":
    c = Chef("Blanchard", "Nicolas", "22/06/1983", 1000, "Informatique")
    c.affiche()