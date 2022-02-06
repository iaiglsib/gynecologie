
import random
from string import ascii_uppercase
from string import digits




class Maladie:
    """ on a initialiser une lise des maladies """
    listeNomMaladie = {
        1:"Condylomes",
        2:"KysteOvarien",
        3:"FibromeUterien",
        4:"KysteVaginal",
        5:"Endometriose",
        6:"Salpingite",
        7:"Vulvovaginite",
        8:"Vaginite",
        9:"cancer"
    }
    """ constaté par le patient """
    nom:str
    symptomes:list
    id:str
    carateristiques:str
    """ on cherche a initialiser un maladie commune ou un cancer (qui a des parametre aditionel)"""
    def __init__(self,*arg):
        """ *arg comptient l'essemble des argument passé  """
        self.generateID()
        if(len(arg)==3):
            self.nom =  self.listeNomMaladie[arg[0]] 
            self.symptomes = arg[1]
            self.carateristiques = arg[2]
        if(len(arg)==6):
            if(arg[0]==9):
                self.__init__(arg[0],arg[1],arg[2])
                return print("ce n'est pas un cancer ")
            self.generateID()
            self.nom = self.listeNomMaladie[arg[0]]
            self.symptomes = arg[1]
            self.carateristiques = arg[2]
            self.causes = arg[3]
            self.risques = arg[4]
            self.stades = arg[5]

    

    def generateID(self,size= 10,chars= ascii_uppercase + digits):
        chaine = ''.join(random.choice(chars) for _ in range(size))
        chaine = random.sample(chaine,len(chaine))
        chaine = ''.join([str(item) for item in chaine ])
        self.id = chaine

    


        


    def rtrnObj(self):
        if(self.nom and self.nom!="cancer"):
           return {
                "id":self.id,
                "nom":self.nom,
                "symptomes":self.symptomes,
                "caracteristique":self.carateristiques
            } 
        else:
            return {
                "id":self.id,
                "nom":self.nom,
                "symptomes":self.symptomes,
                "caracteristique":self.carateristiques,
                "causes": self.causes,
                "risques": self.risques,
                "stades": self.stades
            }      