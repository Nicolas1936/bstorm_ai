from employe import Employe
from chef import Chef
from directeur import Directeur

liste = [   
            Employe("NOM1", "PRENOM1", "03/04/1991", 1001),
            Employe("NOM2", "PRENOM2", "03/04/1992", 1002),
            Employe("NOM3", "PRENOM3", "03/04/1993", 1003),
            Employe("NOM4", "PRENOM4", "03/04/1994", 1004),
            Employe("NOM5", "PRENOM5", "03/04/1995", 1005),
            Chef("NOM6", "PRENOM6", "03/04/1996", 1006, "Informatique"),
            Chef("NOM7", "PRENOM7", "03/04/1997", 1007, "Comptabilité"),
            Directeur("NOM8", "PRENOM8", "03/04/1998", 1008, "Informatique","Microsoft")
]


for i in liste:
    print("*************************************")
    i.affiche()