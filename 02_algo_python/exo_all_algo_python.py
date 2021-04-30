# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 14:03:27 2021

@author: Administrator
"""

#%%
'''
exo05-Réaliser un algorithme convertisseur de seconde. Ce dernier reçoit
un nombre de secondes et détermine le nombre de jours, heures, minutes
et secondes auquel elles correspondent.
'''

seconde = int(input('secondes : '))
print('-----------------')

minute = seconde // 60
seconde = seconde % 60

heure = minute // 60
minute = minute % 60

jour = heure // 24
heure = heure % 24

print("jour :", jour)
print("heure :", heure)
print("minute :", minute)
print("seconde :", seconde)

#%%
'''
exo07-Année bissextile (Pseudo-Code + Python)
Réaliser un petit algorithme qui sur base d’une année donnée va déterminer s’il s’agit d’une année
bissextile. Une année est bissextile si elle est divisible par 4, mais non divisible par 100. Ou si elle est
divisible par 400.
'''

annee = 2024

if ((annee % 4) == 0 and (annee % 100) != 0) or (annee % 400 == 0):
    print("L'année {} est bissextile".format(annee))
else:
    print("L'année {} n'est pas bissextile".format(annee))
    
#%%
'''
exo8-Lanceur de balles de tennis (Pseudo-Code + Python)
(Indice : booleen = bool(int(input("Veuillez insérer : 1 = oui / 0 = non"))
Réaliser l’algorithme d’un lanceur de balles de tennis. Ce lanceur possède deux états :
– prêt : permet de savoir si le tennisman est prêt. Il ne faut pas lancer de balles dans le cas contraire
– panier_vide : permet de savoir s’il y a encore des balles disponibles
Le lanceur de balle possède l’opération « lancerBalle » qui, vous l’aurez compris, permet de lancer
une balle.
'''

#booleen = bool(int(input("Etes-vous prêt? : 1 = oui / 0 = non")

pret = bool(int(input("Etes-vous prêt? (0-1) :")))
panier_vide = bool(int(input("Panier vide? (0-1):")))

if pret and not panier_vide:
    print("la balle est lancée!")
else:
    print("La balle n'est pas lancée!")
    
#%%
'''
exo09-Distributeur de boissons (Pseudo-Code + Python)
Réaliser l’algorithme d’un distributeur de boissons. Ce dernier propose plusieurs boissons et
l’utilisateur choisit celle qu’il désire en entrant le numéro correspondant. Ne pas oublier de vérifier
s’il y a encore des boissons en stock.
'''

nb_fanta = 2
nb_coke = 5
nb_spa = 0



choix = int(input("1. Fanta\n2. Coke\n3. Eau\nSelection : "))

if choix == 1:
    if nb_fanta != 0:
        nb_fanta = nb_fanta - 1
        print('Vous prenez un fanta')
    else:
        print("Désolé, il n'y a plus de fanta!")
elif choix == 2:
    if nb_coke != 0:
        nb_coke = nb_coke - 1
        print('Vous prenez un coca')
    else:
        print("Désolé, il n'y a plus de coca!")
else:
    if nb_spa != 0:
        nb_spa = nb_spa - 1
        print('Vous prenez un spa')
    else:
        print("Désolé, il n'y a plus de spa!")

        
#%%
'''
exo10-Calculatrice (Pseudo-Code + Python)
Réaliser l’algorithme d’une calculatrice basique. L’utilisateur
est invité à saisir un nombre, un opérateur, et un deuxième
nombre. La calculatrice affiche ensuite le résultat. (Gérer la
division par 0)
'''

n1 = int(input("n1 : "))
operateur = input("operateur :")
n2 = int(input("n2 : "))

if operateur == '+':
    resultat = n1 + n2
elif operateur == '-':
    resultat = n1 - n2
elif operateur == '*':
    resultat = n1 * n2
elif operateur == '/':
    if n2 != 0:
        resultat = n1 / n2
    else:
        print("Ne peux être divisible par 0!!!")
else:
    print("ERROR!!!")
    
if not (operateur == '/' and n2 == 0):     
    print(f"resultat de {n1} {operateur} {n2} =", resultat)
    
#%%

import platform
import os
 
def Clean():
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux":
        os.system("clear")
 
print("Le texte a effacer")
Clean()
print(platform.system())

#%%
print("\014")

#%%
'''
exo11-Note (Pseudo-Code + Python)
Ecrire un algorithme qui met l'appréciation par rapport à des
notes. Ces notes sont comprises entre 0 et 20.
'''
#print("\014")

compteur = 5
nb = 0

while nb < 5:
    note = int(input("note (0-20) : "))
    
    if note <= 5:
        print("la note est mauvaise")
    elif note > 5 and note < 15:
        print("la note est moyenne")
    elif note >= 15 and note <= 20:
        print("la note est excellente")
    else:
        print("la note est erronnée")
    
    nb = nb + 1

#%%
'''
exo12-Réalisez un algorithme utilisant le convertisseur de
secondes, il reçoit deux durées (jours, heures, minutes et
secondes) et calcule la différence entre ces dernières.
'''
print("\014")


#%%
'''
exo13-À l’aide d’une boucle, afficher la table de multiplication par
2. Ensuite, coder votre algorithme en Python.
'''
#print("\014")

nb = 0

while nb < 10:
    print(f"2 * {nb} :", 2*nb)
    nb = nb + 1
    
#%%
'''
exo14-Reprenez l’algorithme du lanceur de balles de tennis et
faites en sorte qu’il lance une balle tant que le stock n’est pas vide.
Il y a donc 2 variables stock_balles et pret
'''

stock_balles = 5

while stock_balles > 0:
    pret = bool(int(input("Etes-vous prêt? (0-1) :")))
    if pret:
        print("la balle est lancée!")
        stock_balles = stock_balles - 1
    
#%%
'''
exo15-À l’aide de deux boucles, afficher les tables de
multiplication de 1 à 9. Ensuite, coder votre algorithme en Python.
'''
n1 = 1

while n1 < 10:
    n2 = 1
    while n2 < 10:
        print(f"{n1} * {n2} : ", n1 * n2)
        n2 += 1
    n1 += 1

#%%
'''
exo16-Un algorithme reçoit deux nombres de l’utilisateur
(opération Lire) : a et b.
• Il répond : « C’est plus » lorsque b est plus petit que a.
• Et inversement, il répond : « C’est moins » lorsque b est plus
grand que a.
• Si a est égal à b, il répond : « C’est gagné ».
'''


a = int(input("a : "))
c = True
while c:
    
    b = int(input("b : "))
    if  b < a:
        print("C'est plus")
    elif b > a:
        print("C'est moins")
    else:
        print("C'est gagné")
        c = False
        
#%%
'''
exo17-À l’aide d’une boucle TantQue … Faire, améliorez l’algorithme du distributeur
de boissons pour qu’il demande au client s’il désire une autre boisson (Tant qu’il en a
envie).
'''

nb_fanta = 2
nb_coke = 5
nb_spa = 0

c = True
while c:
    
    choix = int(input("1. Fanta\n2. Coke\n3. Eau\nSelection : "))
    
    if choix == 1:
        if nb_fanta != 0:
            nb_fanta = nb_fanta - 1
            print('Vous prenez un fanta')
        else:
            print("Désolé, il n'y a plus de fanta!")
    elif choix == 2:
        if nb_coke != 0:
            nb_coke = nb_coke - 1
            print('Vous prenez un coca')
        else:
            print("Désolé, il n'y a plus de coca!")
    else:
        if nb_spa != 0:
            nb_spa = nb_spa - 1
            print('Vous prenez un spa')
        else:
            print("Désolé, il n'y a plus de spa!")
    
    c = int(input("Veux-tu une autre boisson? (0-1) : "))


#%%
'''
exo18-À l’aide d’une boucle TantQue … Faire, améliorez l’algorithme de la
calculatrice afin qu’elle demande à l’utilisateur s’il veut faire un autre calcul (tant
qu’il le désire).
'''

c = True
while c:
    n1 = int(input("n1 : "))
    operateur = input("operateur :")
    n2 = int(input("n2 : "))
    
    if operateur == '+':
        resultat = n1 + n2
    elif operateur == '-':
        resultat = n1 - n2
    elif operateur == '*':
        resultat = n1 * n2
    elif operateur == '/':
        if n2 != 0:
            resultat = n1 / n2
        else:
            print("Ne peux être divisible par 0!!!")
    else:
        print("ERROR!!!")
        
    if not (operateur == '/' and n2 == 0):     
        print(f"resultat de {n1} {operateur} {n2} =", resultat)
        
    c = int(input("Veux-tu refaire un autre calcul? (0-1) : "))

#%%
'''
exo19-À l’aide de la boucle TantQue … Faire, réalisez un algorithme calculant le
résultat de N10. N étant un nombre saisi par l’utilisateur.
'''

max = 10
i = 0

n = int(input("N : "))
total = 1
while i < max:
    total = total * n
    i = i + 1

print(f"{n}**10 :", total)
#%%
'''
exo20-Reprenez l’exercice précédent et modifiez-le pour que l’utilisateur entre
également l’exposant qu’il désire calculer.
'''


i = 0

n = int(input("N : "))
exp = int(input("exp : "))

total = 1
while i < exp:
    total = total * n
    i = i + 1

print(f"{n}**{exp} :", total)

#%%
'''
exo21-Améliorez le "C'est plus, c'est moins, c'est gagné" pour qu'il tourne en boucle tant que le juste_prix n'a pas été trouvé.
L'ordinateur choisit un nombre aléatoirement entre 1 et 100. L'utilisateur est invité à entrer un nombre et l'algorithme nous
répond "C'est plus" ou "C'est moins". Lorsqu'on a trouvé le bon nombre, l'algorithme affiche le nombre de tentatives
effectuées pour trouver le résultat
'''
import random


print("Bonjour aux juste prix!")
print("Vous avez droit à 10 essai au maximun!")
print()
p = int(input("Choisissez votre niveau (1-Facile <10 | 2-Moyen <100 | 3-Difficile <1000) :"))
if p < 1:
    p = 1
elif p > 3:
    p = 3

a = random.randrange(1, 10**p, 1)
c = False
compteur = 1

while compteur <= 10 and not c:
    
    b = int(input(f"{compteur} | nombre ? : "))
    if  b < a:
        print("C'est plus")
    elif b > a:
        print("C'est moins")
    else:
        print("C'est gagné!")
        print("Le nombre de tentative effectué est de :", compteur)
        print("Le juste prix était donc :", a)
        c = True
    
    compteur += 1
else:
    if not c:
        print("Désolé, vous avez perdu!")
        print("Vous avez depassé votre limite de 10 essai. ;-(")

#%%



# définition de la fonction
def metajour(tab):
 tab[0] = 3
tableau = [0, 1]
#appel de la fonction
metajour(tableau)
print(tableau)

#%%
'''
exo22-BONUS : initialiser un tableau de 10 entiers avec
les valeurs 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024 à
l’aide d’une boucle. Ensuite, à l’aide d’une boucle
afficher la valeur de chaque cellule du tableau avec
l’opération Ecrire().
'''

tab = []

a = 1
compteur = 0

while compteur < 10:
    a = a * 2
    tab.append(a)
    compteur += 1
    
print(tab)

compteur = 0
while compteur < len(tab):
    print(f"tab[{compteur}] : ", tab[compteur])
    compteur += 1

#%%
'''
exo23-Écrire un algorithme demandant à l’utilisateur le nombre de joueurs (max 10
joueurs). Ensuite, l’algorithme doit demander à l’utilisateur le score de chaque
joueur. Une fois ceci fini, il faut afficher la moyenne des scores. Faites de même en
Python
'''

nb_joueurs = 0

while nb_joueurs < 1 or nb_joueurs > 10:
    nb_joueurs = int(input("Nombres de joueurs (max : 10) : "))
    
    if nb_joueurs < 1 or nb_joueurs > 10:
        print("Erreur: Inserez un chiffre entre 0 et 10!")

tab = []

for i in range(1, nb_joueurs+1):
    entree = int(input(f"Score du joueur {i} : "))
    tab.append(entree)
    
total = 0
for i in tab:
    total += i
    
moyenne = total / len(tab)

print("La moyenne des score est de :", moyenne)

#%%
'''
exo24-Inverser un tableau : soit un tableau T. Saisir ce tableau. Changer de place les
éléments de ce tableau de façon à ce que le nouveau tableau soit une sorte de miroir
de l'ancien et afficher le nouveau tableau.
'''

tab = [1, 2, 3, 4, 5]

tab_m = []
for i in range(len(tab)-1, -1, -1):
    tab_m.append(tab[i])
    
print(tab_m)

#%%
'''
exo25-À l’aide des boucles, réalisez un algorithme permettant de trier un tableau
d’entiers dans l’ordre croissant. Mettez-le ensuite en pratique avec le Python.
'''

tab = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

for i in range(len(tab)-1):
    for key, value in enumerate(tab):
        if (key + 1) != len(tab):
            if tab[key] > tab[key+1]:
                var = tab[key]
                tab[key] = tab[key + 1]
                tab[key+1] = var
                
print(tab)

#%%
'''
exo26-En considérant deux tableaux d'entiers (non triés), réalisez un algorithme qui
place tous les éléments des deux tableaux dans un troisième. Ce dernier doit être
trié une fois l'algorithme terminé. Notez que le tri doit être fait en même temps que
la fusion des deux tableaux et pas après. (Indice : tab.reverse())
'''

tab1 = [5, 3, 4]
tab2 = [1, 2]

print("tab1 :", tab1)
print("tab2 :", tab2)

tab = []

tab_min = -1
key_min = -1



tab_len = len(tab1) + len(tab2)

for i in range(tab_len):
    value_min = 999999999
    for key, value in enumerate(tab1):
        if value < value_min:
            value_min = value
            key_min = key
            tab_min = 1
    
    for key, value in enumerate(tab2):
        if value < value_min:
            value_min = value
            key_min = key
            tab_min = 2
            
    if tab_min == 1:
        tab.append(value_min)
        del tab1[key_min]
    else:
        tab.append(value_min)
        del tab2[key_min]

print("tab tot :", tab)
    
#%%
'''
exo27-Réalisez un algorithme nous permettant de déplacer un pion dans un tableau
de 10 éléments. Au début, le pion se trouve dans la première case du tableau. Nous
pouvons ensuite le déplacer par la gauche (g), par la droite (d) ou de stopper
l'algorithme (q) (Indice : l'exo doit être exécuté dans la console Windows). 
'''
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
    

#%%
'''
exo28-Réalisez un algorithme permettant de rechercher une valeur dans un tableau.
Si la valeur se trouve bien dans la tableau, nous affichons sa position. 
'''

tab = [3, 6, 8, 1, 4, 7, 5]

valeur_a_trouve = 3
flag = True

for k, v in enumerate(tab):
    if v == valeur_a_trouve:
        print("Valeur trouvé à la position :", k)
        flag = False
        break

if flag:
    print("Valeur non trouvé!")

#%%
'''
exo29-Refaites l'algorithme qui demande à l’utilisateur de taper 10 entiers et qui
affiche le plus petit de ces entiers mais cette fois-ci à l'aide d'un tableau et sans
retenir le minimum lors de la saisie. 
'''

tab = []

print("Entrez 10 valeurs, je vais trouvé la valeur minimum! ;-)")
for i in range(10):
    entree = int(input(f"val {i+1} :"))
    tab.append(entree)
    
val_min = tab[0]

for value in tab:
    if value < val_min:
        val_min = value


print("La valeur minimum est de :", val_min)

#%%
'''
exo30-En considérant un tableau d'entiers trié dans l'ordre croissant, réaliser un
algorithme étant capable d'insérer une nouvelle valeur dans le tableau de façon à ce
que la tableau reste trié. Le but n'est évidemment pas d'insérer la valeur à la fin et
de trier après mais bien de l'insérer au bon endroit directement. 
'''
#Exo30

#Initialisatino du tableau
tab = [1, 2, 3, 4, 6, 7, 8, 9]
print(tab)

#Valeur à ajouter
value_add = 9
print(value_add)

if value_add >= tab[-1]:
    #Ajout de la valeur à la fin si supérieur
    tab.append(value_add)
else:
    #Ajout de la valeur dans le tableau sinon
    for k, v in enumerate(tab):
        if value_add <= v:
            tab = tab[:k] + [value_add] + tab[k:]
            break
       
print(tab)


#%%
'''
exo31-Réalisez un algorithme dans lequel nous devons rechercher une valeur (entrée
par l'utilisateur) dans un tableau d'entiers. 
'''

tab = [1, 2, 3, 4, 5, 6, 7, 8, 9]

valeur_a_trouve = int(input("Valeur recherchée : "))

flag = True

for k, v in enumerate(tab):
    if v == valeur_a_trouve:
        print("Valeur trouvé à la position :", k)
        flag = False
        break

if flag:
    print("Valeur non trouvé!")
    
#%%
'''
exo32-Réalisez une fonction calculant le carré d’un nombre entier
donné en paramètre.
'''

def carre_de(entier):
    return entier * entier

print(carre_de(5))

#%%
'''
exo33-Réalisez une fonction de recherche dans un tableau. Cette
fonction va recevoir un tableau, la taille du tableau, et la valeur
recherchée en paramètres et renvoyer l’indice de l’élément dans le
tableau. Si l’élément ne s’y trouve pas, la fonction renvoie -1.
'''

def recherche(tab, taille, valeur_a_chercher):
    t = tab.copy()
    
    for key, value in enumerate(t):
        if value == valeur_a_chercher:
            return key   
    return -1

tab = [1, 2, 3, 5]

print(recherche(tab, 4, 2))


#%%
'''
exo34-Réalisez une procédure dont l’objectif est de fusionner deux
tableaux d’entiers.
'''

def fusionner_tab(tab1, tab2):
    tab = []

    tab_min = -1
    key_min = -1
    
    
    
    tab_len = len(tab1) + len(tab2)
    
    for i in range(tab_len):
        value_min = 999999999
        for key, value in enumerate(tab1):
            if value < value_min:
                value_min = value
                key_min = key
                tab_min = 1
        
        for key, value in enumerate(tab2):
            if value < value_min:
                value_min = value
                key_min = key
                tab_min = 2
                
        if tab_min == 1:
            tab.append(value_min)
            del tab1[key_min]
        else:
            tab.append(value_min)
            del tab2[key_min]
            
    return tab


print(fusionner_tab([4, 6, 1],[9, 3]))

#%%
tab = [1, 2, 3]

print(type(tab))

tab.reverse()
print(tab)


t = [2, 4, 6, 10, 20, 30, 7]
t1 = []
tLen = len(t)
k = 1
for j in t:
    t1.append(t[tLen - k])
    k += 1

print(t)
print(t1)



#%%
print("test")
















































