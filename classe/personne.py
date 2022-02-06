import json
from select import select
import string


import random
from string import ascii_uppercase
from string import digits





class personne ():
    id:string
    sexe:string
    age:string
    nom:string
    prenom:string
    profession:string
    

    

    def __init__(self,sexe, age, nom, prenom, profession,poids,tension,bilan_sanguin,dernier_frottis,date_des_dernieres_règles):
         self.generateID()
         self.sexe= sexe 
         self.age=age
         self.nom=nom
         self.prenom=prenom
         self.profession=profession
         self.maladie = []
         self.poids = poids
         self.tension = tension
         self.bilan_sanguin = bilan_sanguin
         self.dernier_frottis = dernier_frottis
         if(sexe=="f"):
            self.date_des_dernieres_règles = date_des_dernieres_règles

         
    
    def generateID(self,size= 10,chars= ascii_uppercase + digits):
        chaine = ''.join(random.choice(chars) for _ in range(size))
        chaine = random.sample(chaine,len(chaine))
        chaine = ''.join([str(item) for item in chaine ])
        self.id = chaine    
    
    def affiche_personne(self):
        print("nom: "+ self.nom +",prenom: "+self.prenom)

    def addMaladie(self,maladie):
        self.maladie.append(maladie.rtrnObj())
        

    
    def save(self):
       if(self.id):
            personne = {
            "id": self.id,
            "nom":self.nom,
            "prenom": self.prenom,
            "profession": self.profession,
            "age": self.age,
            "sexe": self.sexe,
            "maladie":self.maladie,
            "bilan_sanguin": self.bilan_sanguin,
            "dernier_frottis":self.dernier_frottis.strftime("%d-%b-%Y (%H:%M:%S.%f)")

    
            }
            with open('json/personne.json', 'w') as personnefile:
                 
	             json.dump(personne,personnefile,ensure_ascii=True)
                
                
