'''
exo27-Réalisez un algorithme nous permettant de déplacer un pion dans un tableau
de 10 éléments. Au début, le pion se trouve dans la première case du tableau. Nous
pouvons ensuite le déplacer par la gauche (g), par la droite (d) ou de stopper
l'algorithme (q) (Indice : l'exo doit être exécuté dans la console Windows). 
'''


import os
# insérer la bibliothèque
import msvcrt as m

val = 0
tab2 = [1] * 10
tab2[val] = 0

os.system('cls')
print(tab2)

for i in range(50):
	
	# récupère le caractère sous la forme de byte
	char = m.getch()
	# convertir de bytes en string
	c = char.decode("ascii")

	if c == "d":
		val += 1
	elif c == "g":
		val -= 1
	elif c == "q":
		break

	val = val % 10
	tab2 = [1] * 10
	tab2[val] = 0

	os.system('cls')
	print(tab2)


