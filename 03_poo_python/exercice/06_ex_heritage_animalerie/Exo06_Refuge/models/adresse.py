class Adresse:

    def __init__(self, rue, numero, ville, code_postal):
        self.__rue = rue
        self.__numero = numero
        self.__ville = ville
        self.__code_postal = code_postal

    # region Propriétés

    @property
    def rue(self):
        return self.__rue

    @property
    def numero(self):
        return self.__numero

    @property
    def ville(self):
        return self.__ville

    @property
    def code_postal(self):
        return self.__code_postal

    # endregion


    # region Méthodes

    def __str__(self):
        return "{0} {1}, {2} {3}".format(self.rue, self.numero, self.code_postal, self.ville)

    # endregion