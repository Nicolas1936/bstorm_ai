
class Client:
    
    def __init__(self, cin, nom, prenom, tel):
        self._cin = cin
        self._nom = nom
        self._prenom = prenom
        self._tel = tel

    def __str__(self):
        output = ""

        output += 'CIN      : {}\n'.format(self.cin)
        output += 'NOM      : {}\n'.format(self.nom)
        output += 'Prénom   : {}\n'.format(self.prenom)
        output += 'Tél      : {}\n'.format(self.tel)
        
        return output

    @property
    def cin(self):
        return self._cin
    
    @property
    def nom(self):
        return self._nom

    @property
    def prenom(self):
        return self._prenom

    @property
    def tel(self):
        return self._tel

    @cin.setter
    def cin(self, cin):
        self._cin = cin

    @nom.setter
    def nom(self, nom):
        self._nom = nom

    @prenom.setter
    def prenom(self, prenom):
        self._prenom = prenom

    @tel.setter
    def tel(self, tel):
        self._tel = tel