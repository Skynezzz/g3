from random import randint

jeu = ["pierre","feuille", "ciseaux"] 
cpu = jeu[randint(0,2)]
tour = 0
mouvJourParTour = []

joueur = input("Voulez-vous couplimenter avec moi cette evening \n>")
scoreCpu = 0
scoreJoueur = 0

if joueur == "yes":
    continuer = True
elif joueur == "no":
    continuer = False

while True:
    cpu = jeu[randint(0,2)]
    joueur = input("pierre, feuille ou ciseaux \n>")
    if joueur == "ciseaux":
        mouvJourParTour.append("ciseaux")
        if cpu == "pierre":
            scoreCpu += 1
            print("cpu winner")
            print("Joueur : " + str(scoreJoueur) +"\n"+ "CPU : " + str(scoreCpu))
        elif cpu == "feuille":
            scoreJoueur += 1
            print("You win GG") 
            print("Joueur : " + str(scoreJoueur) +"\n"+ "CPU : " + str(scoreCpu))
        else:
            print("it's draw, retry")
            print("Joueur : " + str(scoreJoueur) +"\n"+ "CPU : " + str(scoreCpu))
    elif joueur == "feuille":
        mouvJourParTour.append("feuille")
        if cpu == "pierre":
            scoreJoueur += 1
            print("You win GG")
            print("Joueur : " + str(scoreJoueur) +"\n"+ "CPU : " + str(scoreCpu))
        elif cpu == "feuille":
            print("it's a draw, retry")
            print("Joueur : " + str(scoreJoueur) +"\n"+ "CPU : " + str(scoreCpu))
        else:
            scoreCpu += 1
            print("cpu winner")
            print("Joueur : " + str(scoreJoueur) +"\n"+ "CPU : " + str(scoreCpu))
    elif joueur == "pierre":
        mouvJourParTour.append("pierre")
        if cpu == "pierre":
            print("it's a draw, retry")
            print("Joueur : " + str(scoreJoueur) +"\n"+ "CPU : " + str(scoreCpu))
        elif cpu == "feuille":
            scoreCpu += 1
            print("cpu winner")
            print("Joueur : " + str(scoreJoueur) +"\n"+ "CPU : " + str(scoreCpu))
        else:
            scoreJoueur += 1
            print("You win, GG")
            print("Joueur : " + str(scoreJoueur) +"\n"+ "CPU : " + str(scoreCpu))

    if scoreJoueur == 3:
        print("GG jeune padawan, tu a gagner contre ce maudit bot")
        print("Joueur : " + str(scoreJoueur) +"\n"+ "CPU : " + str(scoreCpu))
        break
    elif scoreCpu == 3:
        print("Passe le bonjour depuis la tombe de la honte, un bot restera un bot ")
        print("Joueur : " + str(scoreJoueur) +"\n"+ "CPU : " + str(scoreCpu))
        break
    tour += 1

print(mouvJourParTour)