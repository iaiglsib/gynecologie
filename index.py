
from datetime import datetime
from classe.personne import personne 
from classe.Maladie import Maladie
"""les parametres de maladie sont :
nom,symptomes,caracteristiques,causes,risques,stades"""
maladie = Maladie(2,["diarrhee","saignement"],["diarrhee","cool"])

""" pour declarer un objet personne on met le sexe,l'age,nom,prenom,profession,poids,tension,billan_sanguin, date_dernier_frotis,date_derniere_regle"""

firstPersone = personne("M","18","alba","koffi","pompier",80,17,"sool",datetime.now(),datetime.now())

""" fonction qui permet d'afficher les information d'une personne """
firstPersone.affiche_personne()

firstPersone.addMaladie(maladie) 
firstPersone.addMaladie(maladie) 

firstPersone.save()