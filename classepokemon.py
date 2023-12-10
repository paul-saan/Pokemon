import random
from classejoueur import Joueur

class pokemon:
    def __init__(self,id , nom, type, pv, pvmax, exp, evolution, attaque1, degat1, attaque2, degat2,equipe, categorie):
        self.id = id
        self.nom = str(nom)
        self.type = str(type)
        self.pv  = pv
        self.pvmax = pvmax
        self.exp = exp
        self.evolution = evolution
        self.attaque1 = attaque1
        self.attaque2 = attaque2
        self.degat1 = degat1
        self.degat2 = degat2
        self.equipe = equipe
        self.categorie = categorie
        
    def rappelCaracteres(self):
        """
        renvoie le NOM, le TYPE, les PVMAX, son EVOLUTION si il y en a une
        """
        print("______________________________")
        print("|Nom :", self.nom,)
        print("|Type :", self.type)
        print("|Point de vie maximum :", self.pvmax)
        if self.evolution == None:
            print("|",self.nom,"n'a pas d'évolution !")
        else:
            print("|Evolution :", self.evolution.nom)
        print("|Attaque principale", self.attaque1, "fait",self.degat1, "de dégats")
        print("|Attaque secondaire", self.attaque2, "fait",self.degat2, "de dégats")
        print("______________________________")

        
    def pointdeVie(self):
        """
        renvoie les PV sur PVMAX
        """
        print("Point de vie de ", self.nom, self.pv, " / ", self.pvmax)
    
    def degatsInfliges(self, pokéAttaquant, pokéDefence, attaqueEffectue):
        if attaqueEffectue == pokéAttaquant.attaque1:
            self.pv = self.pv - pokéAttaquant.degat1
            print("______________________________")
            print("|",attaqueEffectue, "de", pokéAttaquant.nom, "enlève à", self.nom, pokéAttaquant.degat1, "points de vie.")
            print("______________________________")
        if attaqueEffectue == pokéAttaquant.attaque2:
            self.pv = self.pv - pokéAttaquant.degat2
            print("______________________________")
            print("|",attaqueEffectue, "de", pokéAttaquant.nom, "enlève à", self.nom, pokéAttaquant.degat2, "points de vie.")
            print("______________________________")

    
    def defAttaqueIA(self):
        attaqueEffectueIA = random.randint(0,1)
        if attaqueEffectueIA == 0:
            return self.attaque1
        else :
            return self.attaque2

    def choisirAttaqueJoueur(self):
        print("______________________________")
        print("| Tapez 1 pour",self.attaque1,"ou 2 pour", self.attaque2)
        attaqueEffectueJoueur = input()
        if attaqueEffectueJoueur ==1:
            return self.attaque1
        else:
            return self.attaque2
        print("______________________________")
    
    def soinTotal(self):
        self.pv = self.pvmax
                
    def ajoutexp(self, expAjoute):
        self.exp = self.exp + expAjoute
    
    def expActuel(self):
        print(self.exp, "xp")
        
    def evolutionPokemon(self):
        if self.evolution != None:
            if self.exp == 10000 or self.exp == 25000 or self.exp == 50000:
                print(self.nom,"deviens un",self.evolution.nom)
                self.id = self.evolution.id
                self.nom = self.evolution.nom
                self.type = self.evolution.type
                self.pv = self.evolution.pv
                self.pvmax = self.evolution.pvmax
                self.evolution = self.evolution.evolution
                self.degat1 = self.degat1 + 30
                self.degat2 = self.degat2 + 30
                self.categorie = self.evolution.categorie
                
    def enVie(self):
        if self.pv > 0:
            return True
        else:
            return False
