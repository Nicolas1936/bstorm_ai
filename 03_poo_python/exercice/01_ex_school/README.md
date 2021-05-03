# Exercice 1
## class student
caractérisé par :
- firstname
- lastname
- matricule -> 3 dernieres lettres du nom avec les trois dernières du prénom
- birthdate
    
actions : 
- secher un cours
- aller en cours -> lorsqu'il va en cours je veux récupérer le nom du cours auquel il va


## class teacher
caractérisé par : 
- firstname
- lastname
- date d'embauche
- email
    
action:
    donner_cours -> récupérer nom du cours

## class classroom
caractérisé par : 
- nbr_places
- liste d'étudiants présents
- prof assigné à la classe
    
actions:
- Ajout etudiants -> dans les limites des places disponibles
- Commencer un cours -> Si nombre d'étudiants minimum dans la classe
    
-> tester dans un programme principal