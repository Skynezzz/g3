#DEBUT
# admettant qu'il existe une fonction random qui renvoie un chifre aléatoir
# admettant qu'il existe une fonction input qui renvoie l'entrée du joueur
# admettant qu'il existe une fonction split qui sépare une chaine de caractere 
# admettant qu'il existe une fonction input qui renvoie l'entrée du joueur

# definir: pcf
#     assigner à la variable jeu: ["pierre","feuille", "ciseaux"] 
#     assigner à la variable cpu: jeu[d'index: le renvoie de l'execution de la fonction random (0 et 2)]
#     assigner à la variable tour: 0
#     assigner à la variable log: contenu du fichier "log.txt"
#     assigner à la variable mouvJourParTour: []
#     pour i alant de 0 à 10
#         assigner à la variable lst: []
#         pour y alant de 0 à 3
#             ajoute à lst l'élement (log.split(" ")[d'index: i].split(",")[d'index: y]))
#         ajouter à la liste mouvJourParTour: lst
#     assigner à la variable scoreCpu: 0
#     assigner à la variable scoreJoueur: 0
#     assigner à la variable continuer: True


#     tant que continuer est égale à True
#         assigner à la variable nbCpu: le renvoie de l'execution de la fonction random (0, sum(mouvJourParTour[d'index: tour]) - 1)
#         si nbCpu est inferieur ou égale mouvJourParTour[d'index: tour][d'index: 0]
#             ALORS assigner à la variable cpu: "pierre"
#         sinon si nbCpu est inferieur ou égale mouvJourParTour[d'index: tour][d'index: 0] + mouvJourParTour[d'index: tour][d'index: 1]
#             ALORS assigner à la variable cpu: "feuille"
#         sinon
#             ALORS assigner à la variable cpu: "ciseaux"
#         tant que joueur in ["pierre", "feuille", "ciseaux"]:
#             ALORS assigner à la variable joueur: retour de l'execution de la fonction input
#         si la variable joueur est égale à "pierre"
#             ALORS ajouter à la variable mouvJourParTour[d'index: tour][d'index: 0]: 1
#             ALORS si cpu est égale à "pierre"
#                 ALORS afficher le message("it's a draw, retry")
#                 ALORS afficher le message("Joueur : " + str(scoreJoueur) +"\n"+ "CPU : " + str(scoreCpu))
#             ALORS sinon si cpu est égale à "feuille"
#                 ALORS ajouter à la variable scoreCpu: 1
#                 ALORS afficher le message("cpu winner")
#                 ALORS afficher le message("Joueur : " + str(scoreJoueur) +"\n"+ "CPU : " + str(scoreCpu))
#             ALORS sinon
#                 ALORS ajouter à la variable scoreJoueur: 1
#                 ALORS afficher le message("You win, GG")
#                 ALORS afficher le message("Joueur : " + str(scoreJoueur) +"\n"+ "CPU : " + str(scoreCpu))

#         sinon si joueur est égale à "feuille"
#             ALORS ajouter à la variable mouvJourParTour [d'index: tour] [d'index: 1]: 1
#             ALORS si cpu est égale à "pierre"
#                 ALORS ajouter à la variable scoreJoueur: 1
#                 ALORS afficher le message("You win GG")
#                 ALORS afficher le message("Joueur : " + str(scoreJoueur) +"\n"+ "CPU : " + str(scoreCpu))
#             ALORS sinon si cpu est égale à "feuille"
#                 ALORS afficher le message("it's a draw, retry")
#                 ALORS afficher le message("Joueur : " + str(scoreJoueur) +"\n"+ "CPU : " + str(scoreCpu))
#             ALORS sinon
#                 ALORS ajouter à la variable scoreCpu: 1
#                 ALORS afficher le message("cpu winner")
#                 ALORS afficher le message("Joueur : " + str(scoreJoueur) +"\n"+ "CPU : " + str(scoreCpu))

#         sinon si joueur est égale à "ciseaux"
#             ALORS ajouter à la variable mouvJourParTour[d'index: tour][d'index: 2]: 1
#             ALORS si cpu est égale à "pierre"
#                 ALORS ajouter à la variable scoreCpu: 1
#                 ALORS afficher le message("cpu winner")
#                 ALORS afficher le message("Joueur : " + str(scoreJoueur) +"\n"+ "CPU : " + str(scoreCpu))
#             ALORS sinon si cpu est égale à "feuille"
#                 ALORS ajouter à la variable scoreJoueur: 1
#                 ALORS afficher le message("You win GG") 
#                 ALORS afficher le message("Joueur : " + str(scoreJoueur) +"\n"+ "CPU : " + str(scoreCpu))
#             ALORS sinon
#                 ALORS afficher le message("it's a draw, retry")
#                 ALORS afficher le message("Joueur : " + str(scoreJoueur) +"\n"+ "CPU : " + str(scoreCpu))


#         si scoreJoueur est égale à 3
#             ALORS afficher le message("GG jeune padawan, tu a gagner contre ce maudit bot")
#             ALORS afficher le message("Joueur : " + str(scoreJoueur) +"\n"+ "CPU : " + str(scoreCpu))
#             ALORS assigner à la variable continuer: False
#         sinon si scoreCpu est égale à 3
#             ALORS afficher le message("Passe le bonjour depuis la tombe de la honte, un bot restera un bot ")
#             ALORS afficher le message("Joueur : " + str(scoreJoueur) +"\n"+ "CPU : " + str(scoreCpu))
#             ALORS assigner à la variable continuer: False
#         si tour < 9
#             ALORS ajouter à la variable tour: 1

#     assigner à la variable write: ""
#     pour i alant de 0 à 10
#         pour y alant de 0 à 3
#             concaténer à la variable write: mouvJourParTour [d'index: x] [d'index: y] + ","
#         remplacer à la variable write: le dernier caractere par ","
#     assigner à la variable log: ouverture du fichier "log.txt"
#     ecrire dans log: write en suprimant le dernier caractere

# appeler la fonction pcf
#FIN