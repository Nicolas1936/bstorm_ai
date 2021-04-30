from client import Client
from compte import Compte

#Création du compte 1
salim = Client("EE111222", "Salim", "Omar", "0611111")
print(salim)
c_salim = Compte(salim)
print(c_salim)

#Créditer et Débiter le compte 1
c_salim.crediter_mon_compte(5000)
print(c_salim)
c_salim.debiter_mon_compte(1000)
print(c_salim)

print()

#Création du compte 2
print("Compte 2:")
samir = Client("EE3334444", "Karimi", "samir", "0622222")
print(samir)
c_samir = Compte(samir)
print(c_samir)
c_samir.crediter(3000, c_salim)
c_salim.debiter(1000, c_samir)
print(c_salim)
print(c_samir)

print()

#Affiche le nombre de compte total
print(Compte.nombre_compte_total())