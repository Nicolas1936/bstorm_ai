# La classe Compte

## Objectif

* Définir les propriétés et méthodes d’une classe
* Définir des constructeurs
* Créer une instance de classe
* Accéder par les accesseurs aux propriétés en lecture et écriture d’un objet
* Appliquer des méthodes
* Définir des attributs et méthodes statiques

## Travail à faire:
1. Définir une classe Client avec les attributs suivants : CIN, Nom, Prénom, Tél.
2. Définir à l’aide des propriétés les méthodes d’accès aux différents attributs de la classe.
3. Définir un constructeur permettant d’initialiser tous les attributs.
4. Définir un constructeur permettant d’initialiser le CIN, le nom et le prénom.
5. Définir la méthode Afficher ( ) permettant d’afficher les informations du Client en cours.
6. Créer Une classe Compte caractérisée par son solde et un code qui est incrémenté lors de sa création ainsi que son propriétaire qui représente un client.
7. Définir à l’aide des propriétés les méthodes d’accès aux différents attributs de la classe (le numéro de compte et le solde sont en lecture seule)
8. Définir un constructeur permettant de créer un compte en indiquant son propriétaire.
9. Ajouter à la classe Compte les méthodes suivantes :
    * Une méthode permettant de Crediter() le compte, prenant une somme en paramètre.
    * Une méthode permettant de Crediter() le compte, prenant une somme et un compte en paramètres, créditant le compte et débitant le compte passé en paramètres.
    * Une méthode permettant de Debiter() le compte, prenant une somme en paramètre
    * Une méthode permettant de Débiter() le compte, prenant une somme et un compte bancaire en paramètres, débitant le compte et créditant le compte passé en paramètres
    * Une méthode qui permet d’afficher le résumé d’un compte.
    * Une méthode qui permet d’afficher le nombre des comptes crées.
10. Créer un programme de test pour la classe Compte.