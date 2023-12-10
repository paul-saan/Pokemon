import random

class Joueur:
    def __init__(self,nom , reservePokemon):
        self.nom = nom
        self.equipe = []
        self.reservePokemon = reservePokemon
        
    def rappelReserve(self):
        print("Votre réserve de pokémon")
        for i in range(1, len(self.reservePokemon)):
            print(" -", self.reservePokemon[i])
        
    def rappelEquipeJoueur(self):
        print("______________________________\n|Votre équipe:")
        for nombrePokeEquipe in range(len(self.equipe)):
            print("|",self.equipe[nombrePokeEquipe].nom, " ")
        print("|______________________________")
            
    def rappelEquipeIA(self):
        print("______________________________\nL'adveraire a choisi cette équipe:\n")
        for nombrePokeEquipe in range(len(self.equipe)):
            print("|",self.equipe[nombrePokeEquipe].nom," ")
        print("______________________________")
        
    def choixEquipe(self):
        print("De combien pokemon se compose votre équipe ?")
        y = input()
        print("______________________________")
        for indiceReservePokemon in range(0,len(self.reservePokemon)):
            print("|",self.reservePokemon[indiceReservePokemon].nom,"Entré", indiceReservePokemon)
        print("______________________________")
        for i in range(1,int(y)+1):
            pokeChoisi = input()
            self.equipe.append(self.reservePokemon[int(pokeChoisi)])
        
    def defEquipeIA(self, tailleEquipe):
        for i in range(tailleEquipe):
            self.equipe.append(self.reservePokemon[random.randint(0,len(self.reservePokemon)-1)])
            
    def pokeElimine(self):
        for i in range(len(self.equipe)):
            if self.equipe[i].pv == 0:
                print( self.equipe[i].nom, "est éliminé !" )
        
    def equipeElimine(self):
        """
        renvoie True si tout les pokemon d'une équipe ont leurs pv à 0
        """
        n=0
        for i in range(len(self.equipe)):
            if self.equipe[i].pv <= 0:
                n = n+1
        if n ==len(self.equipe) :
            return True
        else:
            return False