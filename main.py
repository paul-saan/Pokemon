from classepokemon import pokemon
from classejoueur import Joueur
import random

#duel(joueur1,IA)

dracaufeu = pokemon(3,"Dracaufeu", "Feu", 150, 150, 0, None, "Flammeche", 20, "Lance-Flamme", 25, None,3)
reptincel = pokemon(2,"Reptincel", "Feu", 100, 100, 0, dracaufeu, "Flammeche", 20, "Lance-Flamme", 25, None,2)
salameche = pokemon(1,"Salameche", "Feu", 60, 60, 0, reptincel, "Flammeche", 20, "Lance-Flamme", 25, None,1)
    
clamiral = pokemon(6,"Clamiral", "Eau", 150, 150, 0, None, "Pistolet à O", 20, "Aqua-Jet", 25, None,3)
mateloutre = pokemon(5,"Mateloutre", "Eau", 100, 100, 0, clamiral, "Pistolet à O", 20, "Aqua-Jet", 25, None,2)
moustillon = pokemon(4,"Moustillon", "Eau", 60, 60, 0, mateloutre, "Pistolet à O", 25, "Aqua-Jet", 20, None,1)

florizarre = pokemon(9,"Florizarre", "Feuille", 150, 150, 0, None, "Fouet-liane", 20, "Tranch-Herbe", 25, None,3)
herbizarre = pokemon(8,"Herbizzard", "Feuille", 100, 100, 0, florizarre, "Fouet-liane", 20, "Tranch-Herbe", 25, None,2)
bulbizarre = pokemon(7,"Bulbizarre", "Feuille", 60, 60, 0, herbizarre, "Fouet-liane", 20, "Tranch-Herbe", 25, None,1)

tortank = pokemon(12,"Tortank", "Eau", 150, 150, 0, None, "Hydrocanon", 20, "Ecume", 25, None,3)
carabaffe = pokemon(11,"Carabaffe", "Eau", 100, 100, 0, tortank, "Hydrocanon", 20, "Ecume", 25, None,2)
carapuce = pokemon(10,"Carapuce", "Eau", 60, 60, 0, carabaffe, "Hydrocanon", 20, "Ecume", 25, None,1)
    
roucarnage = pokemon(15,"Roucarnage", "Air", 150, 150, 0, None, "Tornade", 20, "Danse-Plume", 25, None,3)
roucoups = pokemon(14,"Roucoups", "Air", 100, 100, 0, roucarnage, "Tornade", 20, "Danse-Plume", 25, None,2)
roucool = pokemon(13,"Roucool", "Air", 60, 60, 0, roucoups, "Tornade", 20, "Danse-Plume", 25, None,1)

zeblitz = pokemon(17,"Zéblitz", "Electrik", 120, 120, 0, None, "Cage-Eclaire", 20, "Etincelle", 25, None,2)
zebibron = pokemon(16,"Zébibron", "Electrik", 70, 70, 0, zeblitz, "Cage-Eclaire", 20, "Etincelle", 25, None,1)

dracaufeuIA = pokemon(3,"Dracaufeu", "Feu", 150, 150, 0, None, "Flammeche", 20, "Lance-Flamme", 25, None,3)
reptincelIA = pokemon(2,"Reptincel", "Feu", 100, 100, 0, dracaufeu, "Flammeche", 20, "Lance-Flamme", 25, None,2)
salamecheIA = pokemon(1,"Salameche", "Feu", 60, 60, 0, reptincel, "Flammeche", 20, "Lance-Flamme", 25, None,1)
    
clamiralIA = pokemon(6,"Clamiral", "Eau", 150, 150, 0, None, "Pistolet à O", 20, "Aqua-Jet", 25, None,3)
mateloutreIA = pokemon(5,"Mateloutre", "Eau", 100, 100, 0, clamiral, "Pistolet à O", 20, "Aqua-Jet", 25, None,2)
moustillonIA = pokemon(4,"Moustillon", "Eau", 60, 60, 0, mateloutre, "Pistolet à O", 25, "Aqua-Jet", 20, None,1)

florizarreIA = pokemon(9,"Florizarre", "Feuille", 150, 150, 0, None, "Fouet-liane", 20, "Tranch-Herbe", 25, None,3)
herbizarreIA = pokemon(8,"Herbizzard", "Feuille", 100, 100, 0, florizarre, "Fouet-liane", 20, "Tranch-Herbe", 25, None,2)
bulbizarreIA = pokemon(7,"Bulbizarre", "Feuille", 60, 60, 0, herbizarre, "Fouet-liane", 20, "Tranch-Herbe", 25, None,1)

tortankIA = pokemon(12,"Tortank", "Eau", 150, 150, 0, None, "Hydrocanon", 20, "Ecume", 25, None,3)
carabaffeIA = pokemon(11,"Carabaffe", "Eau", 100, 100, 0, tortank, "Hydrocanon", 20, "Ecume", 25, None,2)
carapuceIA = pokemon(10,"Carapuce", "Eau", 60, 60, 0, carabaffe, "Hydrocanon", 20, "Ecume", 25, None,1)
    
roucarnageIA = pokemon(15,"Roucarnage", "Air", 150, 150, 0, None, "Tornade", 20, "Danse-Plume", 25, None,3)
roucoupsIA = pokemon(14,"Roucoups", "Air", 100, 100, 0, roucarnage, "Tornade", 20, "Danse-Plume", 25, None,2)
roucoolIA = pokemon(13,"Roucool", "Air", 60, 60, 0, roucoups, "Tornade", 20, "Danse-Plume", 25, None,1)

zeblitzIA = pokemon(17,"Zéblitz", "Electrik", 120, 120, 0, None, "Cage-Eclaire", 20, "Etincelle", 25, None,2)
zebibronIA = pokemon(16,"Zébibron", "Electrik", 70, 70, 0, zeblitz, "Cage-Eclaire", 20, "Etincelle", 25, None,1)


reservePokemonJoueur1 = [dracaufeu,mateloutre,zeblitz,carapuce,bulbizarre,roucarnage]
reserveIA = [salamecheIA,reptincelIA,dracaufeuIA,moustillonIA,mateloutreIA,clamiralIA,bulbizarreIA,herbizarreIA,florizarreIA,carapuceIA,carabaffeIA,tortankIA,roucoolIA,roucoupsIA,roucarnageIA,zebibronIA,zeblitzIA]

joueur1 = Joueur("Paul-san",reservePokemonJoueur1)
IA = Joueur("Dresseur en herbe",reserveIA)

def choixEquipe(joueur):
    if len(joueur.reservePokemon) >= 6:
        for i in range(5):
            print("Saisissez le nom du pokémon")
            x = str(input())
            joueur.equipe.append(joueur.reserve.index(lower(x)))
            

def gagneExp(joueur, pokeElimine):
    if pokeElimine.categorie == 3:
        joueur.exp = joueur.exp +300
        expgagne = 300
    if pokeElimine.categorie == 2:
        joueur.exp = joueur.exp + 200
        expgagne =200
    if pokeElimine.categorie == 1:
        joueur.exp = joueur.exp + 100
        expgagne =100
    print(joueur.nom, "gagne",expgagne,"d'expérience")
    joueur.evolutionPokemon()
        
def healCentrePoke(pokeAheal):
    if pokeAheal.pv != pokeAheal.pvmax:
        pokeAheal.soinTotal()
        print(pokeAheal.nom, "a été soigné !!!")
    else:
        print("Désolé votre pokemon est déja totalement soigné.")
        
def healEquipeCentrePoke(joueur):
    p = 0
    for i in range(len(joueur.equipe)):
        if joueur.equipe[i].pv != joueur.equipe[i].pvmax:
            joueur.equipe[i].soinTotal()
            p = p+1
    if p >=1:
        print("Votre equipe à été soigné !")
    else:
        print("Votre équipe semble en pleine santé")  
        
def remplacePoke(joueur,pokeAjoute,pokeEnlever):
    """
    ajoute un pokemon à votre équipe (mettre None pour pokeEnlever)
    ou remplace un pokemon par un autre dans l'équipe 
    """
    if len(joueur.equipe) == 6:
         indicePokeEnlever = joueur.equipe.index(pokeEnlever)
         joueur.equipe[indicePokeEnlever] = pokeAjoute
         print(pokeAjoute.nom,"a remplacé",pokeEnlever.nom,"dans votre équipe.")
    else:
        joueur.equipe.append(pokeAjoute)
        print(pokeAjoute.nom,"à été ajouté à votre équipe")

def capturePoke(joueur1,pokeCible):
    print("Entrer 1 si vous voulez capturer le pokemon")
    p = int(input())
    if p == 1:
        print("Vous lancé une pokéball.")
        x = random.random()
        if x<= 0.50:
            x = 0
            if len(joueur1.equipe)<=6:
                joueur1.equipe.append(pokeCible)
                reservePokemonJoueur1.append(pokeCible)
                print("Vous avez capturé",pokeCible.nom,"sauvage.")
                return True
            else:
                joueur1.reservePokemonJoueur1.append(pokeCible)
                print("            ______________________________")
                print("            |Vous avez capturé",pokeCible.nom,"sauvage. \nVotre équipe étant déja au complet, le pokemon a été placé dans votre réserve")
                print("            |______________________________")
                return True
        if x > 0.50:
            print("            ______________________________")
            print("            |Le", pokeCible.nom,"s'échappe de sa pokéball.")
            print("            |______________________________")
            x = 1
            return False
    else:
        x = 1
        return False


def duel(joueur1, IA):
    """
    foncion d'un duel d'une IA contre un joueur
    input: choix des attaques
    """
    joueur1.choixEquipe()
    IA.defEquipeIA(2)
    IA.rappelEquipeIA()
    indicePokemonJoueur1 = 0
    indicePokemonIA = 0
    while joueur1.equipeElimine() == False and IA.equipeElimine() == False:  #tant que les deux équipes ont encore des pokemon avec pv > 0
        for i in range(max(len(IA.equipe),len(joueur1.equipe))):
            if joueur1.equipeElimine() == False and IA.equipeElimine() == False:
                if indicePokemonJoueur1 <= len(joueur1.equipe) and indicePokemonIA <= len(IA.equipe):
                    while joueur1.equipe[indicePokemonJoueur1].enVie() == True and IA.equipe[indicePokemonIA].enVie() == True:
                        x = random.randint(1,2)
                        if x == 1:
                            IA.equipe[indicePokemonIA].degatsInfliges(joueur1.equipe[indicePokemonJoueur1],IA.equipe[indicePokemonIA],joueur1.equipe[indicePokemonJoueur1].choisirAttaqueJoueur())
                            joueur1.equipe[indicePokemonJoueur1].degatsInfliges(IA.equipe[indicePokemonIA],joueur1.equipe[indicePokemonJoueur1], IA.equipe[indicePokemonIA].defAttaqueIA())
                        else:
                            joueur1.equipe[indicePokemonJoueur1].degatsInfliges(IA.equipe[indicePokemonIA],joueur1.equipe[indicePokemonJoueur1], IA.equipe[indicePokemonIA].defAttaqueIA())
                            IA.equipe[indicePokemonIA].degatsInfliges(joueur1.equipe[indicePokemonJoueur1],IA.equipe[indicePokemonIA],joueur1.equipe[indicePokemonJoueur1].choisirAttaqueJoueur())
                        print("            ______________________________")
                        print("            |Il reste à",joueur1.equipe[indicePokemonJoueur1].nom,"de",joueur1.nom, joueur1.equipe[indicePokemonJoueur1].pv,"/",joueur1.equipe[indicePokemonJoueur1].pvmax)
                        print("            |Il reste à",IA.equipe[indicePokemonIA].nom,"de",IA.nom, IA.equipe[indicePokemonIA].pv,"/",IA.equipe[indicePokemonIA].pvmax)
                        print("            |______________________________")
                        if IA.equipe[indicePokemonIA].enVie == False:
                            gagneExp(joueur1.equipe[indicePokemonJoueur1],IA.equipe[indicePokemonIA])
                        if joueur1.equipe[indicePokemonJoueur1].enVie() == False:
                            indicePokemonJoueur1 = indicePokemonJoueur1 + 1
                        if IA.equipe[indicePokemonIA].enVie() == False:
                            indicePokemonIA = indicePokemonIA + 1
                        if joueur1.equipeElimine() == True or IA.equipeElimine() == True:
                            break
    if joueur1.equipeElimine() == True:
        print("\nLe duel est gagné par", IA.nom)
    if IA.equipeElimine() == True:
        print("Le duel est gagné par", joueur1.nom)


def combatDsBuisson(joueur1,IA):
    indicePokemonIA = 0
    indicePokemonJoueur1 = 0
    IA.defEquipeIA(1)
    print("Un",IA.equipe[0].nom,"sauvage apparait !")
    while joueur1.equipeElimine() == False and IA.equipe[0].enVie() == True :
        while joueur1.equipe[indicePokemonJoueur1].enVie() == True and IA.equipe[indicePokemonIA].enVie() == True:
            x = random.randint(1,2)
            if capturePoke(joueur1,IA.equipe[0]) == True:
                y = 0
                break
            else:
                y = 1
            if x == 1:
                IA.equipe[indicePokemonIA].degatsInfliges(joueur1.equipe[indicePokemonJoueur1],IA.equipe[indicePokemonIA],joueur1.equipe[indicePokemonJoueur1].choisirAttaqueJoueur())
                joueur1.equipe[indicePokemonJoueur1].degatsInfliges(IA.equipe[indicePokemonIA],joueur1.equipe[indicePokemonJoueur1], IA.equipe[indicePokemonIA].defAttaqueIA())
            else:
                joueur1.equipe[indicePokemonJoueur1].degatsInfliges(IA.equipe[indicePokemonIA],joueur1.equipe[indicePokemonJoueur1], IA.equipe[indicePokemonIA].defAttaqueIA())
                IA.equipe[indicePokemonIA].degatsInfliges(joueur1.equipe[indicePokemonJoueur1],IA.equipe[indicePokemonIA],joueur1.equipe[indicePokemonJoueur1].choisirAttaqueJoueur())
            print("            ______________________________")
            print("            |Il reste à",joueur1.equipe[indicePokemonJoueur1].nom,"de",joueur1.nom, joueur1.equipe[indicePokemonJoueur1].pv,"/",joueur1.equipe[indicePokemonJoueur1].pvmax)
            print("            |Il reste à",IA.equipe[0].nom,"sauvage",IA.equipe[0].pv,"/",IA.equipe[0].pvmax)
            print("            |______________________________")
            gagneExp(joueur1.equipe[indicePokemonJoueur1],IA.equipe[indicePokemonIA])
            if joueur1.equipe[indicePokemonJoueur1].enVie() == False:
                indicePokemonJoueur1 = indicePokemonJoueur1 + 1
            if IA.equipe[indicePokemonIA].enVie() == False:
                indicePokemonIA = indicePokemonIA + 1
            if joueur1.equipeElimine() == True or IA.equipeElimine() == True:
                break
        if y != 1:
            break
    if joueur1.equipeElimine() == True and y == 1:
        print("\nLe Combat est gagné par", IA.nom)
    if IA.equipeElimine() == True and y == 1:
        print("Le Combat est gagné par", joueur1.nom)
