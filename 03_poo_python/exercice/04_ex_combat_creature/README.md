# Combat de créature

## class Creature

ATTRIBUT : 
- force : 
    - Permet de définir la puissance des coups.
    - Entre 1 - 10
- armure :
    - Réduit les dégât.
    - Entre 0 - 10
- vitesse :
    - Prit en compte pour l'esquive de la créature (max: 20%)
    - Entre 15 - 30

UNE CREATURE VALIDE A MAXIMUM UN TOTAL DE 42 POINTS DE STATISTIQUES

## class Dresseur

ATTRIBUT :
- attaque :
    - Infliger des dégats
    - Il y a 5% de chance d'infliger un coup critique (2X dégâts)
- se_proteger :
    - Permet de restaurer son armure.
    - Réduit les dégats de moitié durant le tour
- esquiver :
    - Donne 50% de bonus pour esquiver l'attaque durant le tour
- change_creature :
    - Permet au dresseur de changer de créature durant le combat


Les combats se déroulent en tour par tour, les actions sont résolues dans l’ordre suivant
1) Changer de créature
2) Préparer une esquive
3) Se protéger
4) Effectuer l’attaque
- En cas d’attaque des 2 créatures, la vitesse permet de définir l'initiative.