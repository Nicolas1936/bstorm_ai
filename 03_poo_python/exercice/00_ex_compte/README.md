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

**Exemple d'exécution**
```
Compte 1:
Donner Le CIN: EE111222
Donner Le Nom: Salim
Donner Le Prénom: Omar
Donner Le numéro de télephone: 0611111
Détails du compte:
************************
Numéro de Compte: 1
Solde de compte: 0
Propriétaire du compte :
CIN: EE111222
NOM: Salim
Prénom: Omar
Tél : 06111111
*************************
Donner le montant à déposer: 5000
Opération bien effectuée
************************
Numéro de Compte: 1
Solde de compte: 5000
Propriétaire du compte :
CIN: EE111222
NOM: Salim
Prénom: Omar
Tél : 06111111
*************************
Donner le montant à retirer: 1000
Opération bien effectuée
************************
Numéro de Compte: 1
Solde de compte: 4000
Propriétaire du compte :
CIN: EE111222
NOM: Salim
Prénom: Omar
Tél : 06111111
*************************


Compte 2:
Donner Le CIN: EE333444
Donner Le Nom: Karimi
Donner Le Prénom: samir
Donner Le numéro de télephone: 0622222
Détails du compte:
************************
Numéro de Compte: 2
Solde de compte: 0
Propriétaire du compte :
CIN: EE333444
NOM: Karimi
Prénom: samir
Tél : 06222222
*************************
Crediter le compte 2 à partir du compt
Donner le montant à déposer: 3000
Opération bien effectuée
Débiter le compte 1 et créditer le com
Donner le montant à retirer: 1000
Opération bien effectuée
************************
Numéro de Compte: 1
Solde de compte: 0
Propriétaire du compte :
CIN: EE111222
NOM: Salim
Prénom: Omar
Tél : 06111111
*************************
************************
Numéro de Compte: 2
Solde de compte: 4000
Propriétaire du compte :
CIN: EE333444
NOM: Karimi
Prénom: samir
Tél : 06222222
*************************


Le nombre de comptes crées: 2
```