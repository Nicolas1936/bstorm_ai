from client import Client

class Compte:
    _compteur = 1

    def __init__(self, client):
        self._numero = Compte._compteur
        self._solde = 0
        self._client = client

        Compte._compteur += 1 

    def __str__(self):
        output = ""

        output += "DETAIL DU COMPTE:\n"
        output += "*****************************\n"
        output += "Numéro de Compte : {}\n".format(self._numero)
        output += "Solde du compte  : {}\n".format(self._solde)
        output += "Propriétaire du compte: \n{}".format(self._client)
        output += "*****************************\n"

        return output

    def crediter_mon_compte(self, somme):
        self._solde += somme
        print("La somme fut bien créditée!")

    def crediter(self, somme, compte):
        if compte.solde >= somme:
            compte._solde = compte.solde - somme
            self._solde += somme
            print("La somme fut bien créditée de {} à {}".format(compte.numero, self.numero))
        else:
            print("Désolé, le compte {} a un solde insuffisant!".format(compte.numero))

    def debiter_mon_compte(self, somme):
        if self._solde >= somme:
            self._solde -= somme
            print("la somme fut bien débitée")
        else:
            print("Désolé, le compte a un solde insuffisant!")

    def debiter(self, somme, compte):
        if self._solde >= somme:
            self._solde -= somme
            compte._solde += somme
            print("La somme fut bien débitée de {} à {}".format(compte.numero, self.numero))
        else:
            print("Désolé, le compte a un solde insuffisant!")

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self):
        pass

    @property
    def solde(self):
        return self._solde

    @solde.setter
    def solde(self):
        pass

    @property
    def client(self):
        return self._client

    @solde.setter
    def client(self, client):
        self._client = client

    @staticmethod
    def nombre_compte_total():
        print("Le nombre de compte crées: {}".format(Compte._compteur))