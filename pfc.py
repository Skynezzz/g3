from random import randint

def pcf():
    jeu = ["pierre","feuille", "ciseaux"] 
    cpu = jeu[randint(0,2)]
    tour = 0
    log = open("log.txt", "r").read()
    mouvJourParTour = []
    for i in range(10):
        lst = []
        for y in range(3):
            lst.append(int(log.split(" ")[i].split(",")[y]))
        mouvJourParTour.append(lst)
    scoreCpu = 0
    scoreJoueur = 0
    continuer = True


    while continuer == True:
        nbCpu = randint(0, sum(mouvJourParTour[tour])-1)
        if nbCpu <= mouvJourParTour[tour][0]:
            cpu = "feuille"
        elif nbCpu <= mouvJourParTour[tour][0] + mouvJourParTour[tour][1]:
            cpu = "ciseaux"
        else:
            cpu = "pierre"
        while not(joueur in ["pierre", "feuille", "ciseaux"]):
            joueur = input("pierre, feuille ou ciseaux? \n>")
        if joueur == "pierre":
            mouvJourParTour[tour][0] += 1
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

        elif joueur == "feuille":
            mouvJourParTour[tour][1] += 1
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

        else:
            mouvJourParTour[tour][2] += 1
            if cpu == "pierre":
                scoreCpu += 1
                print("cpu winner")
                print("Joueur : " + str(scoreJoueur) +"\n"+ "CPU : " + str(scoreCpu))
            elif cpu == "feuille":
                scoreJoueur += 1
                print("You win GG") 
                print("Joueur : " + str(scoreJoueur) +"\n"+ "CPU : " + str(scoreCpu))
            else:
                print("it's a draw, retry")
                print("Joueur : " + str(scoreJoueur) +"\n"+ "CPU : " + str(scoreCpu))


        if scoreJoueur == 3:
            print("GG jeune padawan, tu a gagner contre ce maudit bot")
            print("Joueur : " + str(scoreJoueur) +"\n"+ "CPU : " + str(scoreCpu))
            break
        elif scoreCpu == 3:
            print("Passe le bonjour depuis la tombe de la honte, un bot restera un bot ")
            print("Joueur : " + str(scoreJoueur) +"\n"+ "CPU : " + str(scoreCpu))
            break
        if tour < 9:
            tour += 1

    write = ""
    for i in range(10):
        for y in range(3):
            write += str(mouvJourParTour[i][y]) + ","
        write = write[:-1] + " "
    log = open("log.txt", "w")
    log.write(write[:-1])
pcf()
