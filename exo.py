#DEBUT

from random import randint
def pfc(player):
    lst_pfc = ("pierre", "feuille", "ciseaux")
    while not(player in lst_pfc):
        player = input("Pierre, feuille, ciseaux!?")
    cpu = randint(1,3)
    if cpu == 1:
        cpu = "pierre"
    elif cpu == 1:
        cpu = "feuille"
    else:
        cpu = "ciseaux"
    if player == cpu:
        print("Bot")
    elif player == "pierre":
        if cpu == "feuille":
            winner = "Noob"
        elif cpu == "ciseaux":
            winner = "Chad"
    elif player == "feuille":
        if cpu == "pierre":
            winner = "Chad"
        elif cpu == "ciseaux":
            winner = "Noob"
    elif player == "ciseaux":
        if cpu == "pierre":
            winner = "Noob"
        elif cpu == "feuille":
            winner = "Chad"
    return("Vous: " + player + "\nCpu: " + cpu + "\nt'es un " + winner)
if input("You want to play?") in ("oui", "yes", "ye", "y", "oué", "wé", "ouais", "ouaip", "ok", "ez", "yep", "o"):
    print("Let's play!")
    print(pfc(input("Pierre, feuille, ciseaux?")))  

# def add(x, y):
#     return x + y

# def sub(x, y):
#     return x - y

# def multiply(x, y):
#     return x * y

# def divide(x, y):
#     if y == 0:
#         return None
#     return x / y

# def modulo(x, y):
#     return x % y

# def salaireNet(brut, coef):
#     return brut - brut*coef

# def salaireParSeconde(salaireHoraire, heureParJour, jourParAn):
#     return (salaireHoraire * heureParJour * heureParJour) / (365.25 * 24 * 60 * 60)

#definir la fonction miniJeu
def miniJeu(lettre):
    #Regader si la lettre aléatoir est la même que la lettre choisi
    if input("Devine la lettre ou j'te bute!\n>") == lettre:
        #Renvoyer le compteur WowOWoOWWOw
        return 1
    #Ajouter 1 au compteur
    return 1 + miniJeu(lettre)

print(miniJeu('a'))

#FIN








1 + (1 + (1))