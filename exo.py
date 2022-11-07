#DEBUT
"""
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
    if player == "pierre":
        if cpu == "pierre":
            winner = "bot"
        elif cpu == "feuille":
            winner = "Noob"
        elif cpu == "ciseaux":
            winner = "Chad"
    elif player == "feuille":
        if cpu == "pierre":
            winner = "Chad"
        elif cpu == "feuille":
            winner = "bot"
        elif cpu == "ciseaux":
            winner = "Noob"
    elif player == "ciseaux":
        if cpu == "pierre":
            winner = "Noob"
        elif cpu == "feuille":
            winner = "Chad"
        elif cpu == "ciseaux":
            winner = "bot"
    return("Vous: " + player + "\nCpu: " + cpu + "\nt'es un " + winner)
print(pfc(input("Pierre, feuille, ciseaux?")))  
"""
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def modulo(x, y):
    return x % y

def salaireParSeconde(salaireHoraire, heureParJour, jourParAn):
    return (salaireHoraire * heureParJour * heureParJour) / (365.25 * 24 * 60 * 60)

def salaireNet(brut, coef):
    return brut - brut*coef

#FIN