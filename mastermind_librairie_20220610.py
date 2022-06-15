#!/usr/bin/env python3
#Made by SuperGroupIV
import random
import time
import os
#import pygame


#################
# CLEAN DISPLAY #
#################

def clean_terminal_screen() :                           # Efface l'écran
    os.system('cls' if os.name == 'nt' else 'clear')

def affichage_default() :                               # reset la couleur par défaut (blanc)
    print("\033[0m")


############
# BANDEAUX #
############

def titre_intro() :

    time.sleep(0.2)

    for i in range(10) :

        print('\033[35;46m\033[5;5H                                     '
        + '\033[33;46;1m\033[6;5H  !!! BIENVENUE DANS MASTERMIND !!!  '
        + '\033[35;46m\033[7;5H                                     \033[1;1H\033[0m\n')
        
        time.sleep(0.2)

        print('\033[37;45m\033[5;5H                                     '
        + '\033[37;45;1m\033[6;5H  !!! BIENVENUE DANS MASTERMIND !!!  '
        + '\033[37;45m\033[7;5H                                     \033[1;1H\033[0m\n')
        print('\033[10;5H\033[0m Made by SUPERGROUP_IV')

        time.sleep(0.2)    
    
    print('\033[2J\033[1;1H\033[0m')
    time.sleep(0.5)


##########
# REGLES #
##########

def regle_jeu():
    
    clean_terminal_screen() 
    print("\033[35m\033[6;4H\033[1m"+"REGLES DU JEU\033[0m") 
    
    print('\033[37m\033[8;4H' + 'Tentez de deviner la séquence de couleurs cachées par le programme en moins de 12 tentatives.')
    
    print('\033[37m\033[10;4H\033[0m' + 'Le nombre de couleurs présentes dans la séquence cachée est indiqué en\033[1m BLANC.')
    print('\033[37m\033[11;4H\033[0m' + 'Le nombre de couleurs à la bonne place dans la séquence est indiqué en\033[1m ROUGE.')
    
    print('\033[35m\033[1m\033[20;4H'+'Pressez sur ENTER pour continuer')
    recu = input("")

    if recu != "":              #On accepte que si on appuie sur Enter
        return regle_jeu()

    clean_terminal_screen() 


###########
# MUSIQUE #
###########

def play_music() :

    launched = True

    pygame.init()
    
    background_music = pygame.mixer.Sound("music_1.ogg")
    background_music.play(loops=-1)

    while launched :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                launched = False


########
# MENU #
########

def affichage_choix_menu(niveau_menu, nombre_de_choix): #Affiche les difficultés encore disponible
    clean_terminal_screen() 
    
    print("\033[35m\033[1mMENU CHOIX DIFFICULTE\n\n")
    affichage_default()

    print("\033[2m\t ------------------------ ---------------------\n\t | \033[1m9\033[2m ¦ Règles           | | \033[1m10\033[2m ¦ Quitter      |\n\t ------------------------ ---------------------")

    l_menu =["\t", "\t", "\t", "\t", "\t", "\t", "\t", "\t"]
    nb_couleur = affichage_nb_couleur()                          #Renvoie à l'affichage des difficultés 3-4
    nb_trous = affichage_nb_trous()                              #Renvoie à l'affichage des difficultés 1-2
    autres = affichage_autres()                                  #Renvoie à l'affichage des difficultés 5

    for i in range(7):                                           #Si le type de difficulté n'a pas été choisi, il est affiché
        if niveau_menu[0] == 0:
            l_menu[i] = l_menu[i] + nb_trous[i]
        if niveau_menu[1] == 0:
            l_menu[i] = l_menu[i] + nb_couleur[i]
        if niveau_menu[2] == 0:
            l_menu[i] = l_menu[i] + autres[i]        

    for i in range(7):
        print(l_menu[i])

    affichage_default()
    
    
    print("\033[2m\t ------------------------\n\t | \033[0mENTER\033[2m ¦ \033[0mJOUER\033[2m        |\n\t ------------------------\n")
    
    affichage_default()
    print("\n\nSélectionner les paramètres en entrant les chiffres correspondant:")

def affichage_nb_couleur(): # affichage de la difficultés 3-4
    
    titre = " \033[36;1m   NOMBRE DE COULEURS   "
    ligne_grise = " \033[37;2m-----------------------" 
    ligne_couleur = " \033[37;2m-----------------------"
    choix_1 = " \033[37;0m| \033[36;1m3 \033[37;0m¦ \033[37;1mCinq couleurs   \033[37;0m|"
    choix_2 = " \033[37;0m| \033[36;1m4 \033[37;0m¦ \033[37;1mSix couleurs    \033[37;0m|"
    
    affichage_default()
    return(titre, ligne_grise,choix_1, ligne_couleur, ligne_grise, choix_2, ligne_couleur)

def affichage_nb_trous(): # affichage de la difficultés 1-2
    titre = " \033[32;1m    NOMBRE DE TROUS    "
    ligne_grise = " \033[37;2m-----------------------" 
    ligne_couleur = " \033[37;2m-----------------------"
    choix_4 = " \033[37;0m| \033[32;1m1 \033[37;0m¦ \033[37;1mCinq trous      \033[37;0m|"
    choix_5 = " \033[37;0m| \033[32;1m2 \033[37;0m¦ \033[37;1mSix trous       \033[37;0m|"
    affichage_default()
    return(titre, ligne_grise,choix_4, ligne_couleur,ligne_grise,choix_5,ligne_couleur)

def affichage_autres(): # affichage de la difficultés 5
    titre = " \033[33;1m        AUTRE        "
    ligne_grise = " \033[37;2m-----------------------" 
    ligne_couleur = " \033[37;2m-----------------------"
    choix_8 = " \033[37;0m| \033[33;1m5 \033[37;0m¦ \033[37;1mDe tête         \033[37;0m|"
    tampon = ""
    affichage_default()
    return(titre, ligne_grise, choix_8, ligne_couleur,tampon, tampon, tampon)

def modification_types_diffcultes(niveau, niveau_menu):  #modifie les liste contenant les types de difficultés à afficher

    if (niveau == "1")or(niveau == "2"):    #par défaut tout est à 0
        niveau_menu[0] = 1                  #si niveau_menu = 1 on n'affiche pas, #si niveau_menu = 0, on affiche
    elif(niveau == "3")or(niveau == "4"):
        niveau_menu[1] = 1
    elif (niveau == "5"):
        niveau_menu[2] = 1
    return niveau_menu

def menu(niveau,nombre_trous, nombre_couleur, affichage_complet, possible): #Modifie les valeurs par défaut suivant les choix de difficultés du joueur
    
    if niveau == "1":
        nombre_trous = 5
        return nombre_trous, nombre_couleur, affichage_complet, possible   #return toutes les valeurs par défaut modifiée (le cas échéant)
    elif niveau == "2":
        nombre_trous = 6
        return nombre_trous, nombre_couleur, affichage_complet, possible
    elif niveau == "3":
        nombre_couleur = 5
        possible = ['V','J','R','B','C']
        return nombre_trous, nombre_couleur, affichage_complet, possible
    elif niveau == "4":
        nombre_couleur = 6
        possible = ['V','J','R','B','C','G']
        return nombre_trous, nombre_couleur, affichage_complet, possible
    elif niveau == "5":    
        affichage_complet = False
        return nombre_trous, nombre_couleur, affichage_complet, possible



#################
# AFFICHAGE JEU #
#################

def affichage_sauvegarde(sauvegarde, sauvegarde_place, sauvegarde_couleur_place, nombre_trous): #afiche toutes les tentatives et tous les indicateurs
    
    for i in range(len(sauvegarde)):
        affichage_liste(sauvegarde[i], sauvegarde_place[i], sauvegarde_couleur_place[i], nombre_trous)
    
def choix_affichage(affichage_complet, sauvegarde, sauvegarde_couleur_place, sauvegarde_place, tentative, nombre_trous):  #Affiche toute ou 1 tentative
    
    if affichage_complet == False:
        affichage_liste(sauvegarde[tentative], sauvegarde_couleur_place[tentative], sauvegarde_place[tentative], nombre_trous)
    else:
        affichage_sauvegarde(sauvegarde, sauvegarde_couleur_place, sauvegarde_place, nombre_trous)
    print("\n\n")

def affichage_gagner(tentatives):    #Affiche l'encart gagner + le nombre de tentatives
    
    if (tentatives == 0) or (tentatives == 1):
        s = ""
        clean_terminal_screen()
        print('\t\t\033[37;42;1m                                     ')
        print('\t\t\033[37;42;1m             !!!GAGNE!!!             ')
        print('\t\t\033[37;42;1m       -----------------------       ')
        print(f'\t\t\033[47;42;1m           En {tentatives} tentative{s}            ')
        print('\t\t\033[37;42;1m                                     \n\n')
        affichage_default()
    else:
        s = "s"
        if tentatives > 9 :
            clean_terminal_screen()
            print('\t\t\033[37;42;1m                                     ')
            print('\t\t\033[37;42;1m             !!!GAGNE!!!             ')
            print('\t\t\033[37;42;2m       -----------------------       ')
            print(f'\t\t\033[37;42;1m           En {tentatives} tentative{s}          ')
            print('\t\t\033[37;42;1m                                     \n\n')
            affichage_default()

        else :
            clean_terminal_screen()
            print('\t\t\033[37;42;1m                                     ')
            print('\t\t\033[37;42;1m             !!!GAGNE!!!             ')
            print('\t\t\033[37;42;1m       -----------------------       ')
            print(f'\t\t\033[47;42;1m           En {tentatives} tentative{s}           ')
            print('\t\t\033[37;42;1m                                     \n\n')
            affichage_default()

def affichage_perdre(combinaison, nombre_trous):
    
    clean_terminal_screen()
    print('\t\t\033[37;41;1m                                     ')
    print('\t\t\033[37;41;1m             !!!PERDU!!!             ')
    print('\t\t\033[37;41;1m       -----------------------       ')
    print(f'\t\t\033[37;41;1m         Réfléchissez plus!          ')
    print('\t\t\033[37;41;1m                                     \033[1m\n\n')
    affichage_default()
    print("La combinaison était:\n")
    affichage_liste(combinaison, 0, 0, nombre_trous)
    time.sleep(2)


#################
# CONTROLES JEU #
#################

def ind_couleur_place(combinaison, tentative, nombre_trous): #Cherche le nombre de couleurs à la bonne place
    
    copie_tentative = [] #Création de copie des listes pour ne pas modifier les listes originales
    copie_combinaison = []
    couleur_place = 0
    for z in range(nombre_trous):
        copie_combinaison.append(combinaison[z])
        copie_tentative.append(tentative[z])
    
    for i in range(nombre_trous):
        if copie_combinaison[i]==copie_tentative[i]: #Bonne couleur bon endroit
            couleur_place = couleur_place + 1
            copie_tentative[i] = "8" #Modification de la valeur pour exclure les éléments du test
            copie_combinaison[i] = "9"
    return couleur_place, copie_combinaison, copie_tentative #Renvoie des listes modifiées pour continuer le test

def ind_couleur(copie_combinaison, copie_tentative, nombre_trous): #Cherche le nombre de couleurs à la mauvaise place
    
    couleur = 0
    for i in range(nombre_trous):
        for j in range(nombre_trous):
            if (copie_combinaison[j]==copie_tentative[i]): #Bonne couleur mauvais endroit
                copie_tentative[i] = "8"
                copie_combinaison[j] = "9"
                couleur = couleur + 1    
    return couleur

def combinaison_aleatoire(possible, nombre_lettres, nombre_trous): #Composition de la combinaison à trouver, elle dépend du nombre de couleurs et du nombre de trous
    
    combinaison_2 = []
    for i in range(nombre_trous): #On ajoute aléatoirement une lettre présente dans la combinaison de lettres possibles
        lettre = random.randint(0, nombre_lettres-1)
        combinaison_2.append(possible[lettre])
    
    return combinaison_2

def combinaison_aleatoire_difficulte(nombre_couleur, nombre_trous):  #Création de la combinaison aléatoire suivant les difficultés
    
    POSSIBLES_4 = ['V','J','R','B'] #256 combinaisons 
    POSSIBLES_5 = ['V','J','R','B','C'] #625 combinaisons
    POSSIBLES_6 = ['V','J','R','B','C','G'] #1296 combinaisons                

    combinaison = []
    
    if nombre_couleur == 4:
        combinaison = combinaison_aleatoire(POSSIBLES_4, 4, nombre_trous) #Composition de la combinaison à trouver
    elif nombre_couleur == 5:
        combinaison = combinaison_aleatoire(POSSIBLES_5, 5, nombre_trous)
    elif nombre_couleur == 6:
        combinaison = combinaison_aleatoire(POSSIBLES_6, 6, nombre_trous)
    
    return combinaison

def continuer_ou_laisser(): #Fonction qui donne le choix au joueur de continuer ou pas le jeu
    
    time.sleep(2)
    #clean_terminal_screen()
    c = input("\n\n\033[35m\033[1m\nEntrez le chiffre:\n\n\033[1m1 \033[0mpour CONTINUER\n\033[35m\033[1m0\033[0m pour QUITTER\n\n>> ")
    if c == '1':
        return True    
    elif c == '0':
        return False
    elif (c == '') or (c != '0') or (c != '1'):
        print("\n\n\033[10;1HErreur d'entrée: Veuillez recommencer.\n")
        time.sleep(1)
        return continuer_ou_laisser()  
    else:
        return continuer_ou_laisser()

def affichage_liste(combinaison, couleur_place, couleur, nombre_trous): #Affichage d'une combinaison ses indicateurs

    if nombre_trous == 5:
        print("\t-----------------------------------------------------------")
    elif nombre_trous ==6:
        print("\t-------------------------------------------------------------------")
    else: 
        print("\t---------------------------------------------------")
    print("\t|\t", end ="")
    for i in range(nombre_trous):
        if combinaison[i] == "R":
            print('\033[35m' + "R\t", end='')
        elif combinaison[i] == "G":
            print("\033[90m" + "G\t", end="")    
        elif combinaison[i] == "V":
            print('\033[32m' + "V\t", end='')
        elif combinaison[i] == "B":
            print('\033[34m' + "B\t", end='')
        elif combinaison[i] == "C" :
            print('\033[36m' + "C\t", end='')
        else:
            print('\033[33m' + "J\t", end='')
    print('\033[0m'+ "||  " ,end='')

    if couleur == 0:
        print("   ", end="")
    else:
        print('\033[0m'+ str(couleur), end='')
        print("  ", end='')

    if couleur_place == 0:
        print("   ", end="")
    else:
        print('\033[31m'+ str(couleur_place), end='')
        print("  ", end='')
     
    print('\033[0m'+"|")

def consigne(nombre_couleur, nombre_trous, possible, exemple): #Affiche ce que le joueur doit entrer

    if (nombre_couleur == 4):
        print(f"Entrez {nombre_trous} couleurs parmi {possible} (Exemple: {exemple}):")
    elif (nombre_couleur == 5):
        print(f"Entrez {nombre_trous} couleurs parmi {possible} (Exemple: {exemple}):")
    elif (nombre_couleur == 6):
        print(f"Entrez {nombre_trous} couleurs parmi {possible} (Exemple: {exemple}):")


########################
# SAISIE - JOUEUR_EUSE #
########################
   
def entre_combinaison(possible, nombre_trous):  #Vérifie que la combinaison entrée par l'utilisateur est valide
    special_characters = "!@#$%'^&*() -+?_\\=,<>/"
    essai = []
    test = ''
    test = input("\n>> ")
    test = test.upper()
    if ((len(test) < nombre_trous) or (len(test) > nombre_trous)) or (type(test) != str) or (test == ''):
        print("Entrée invalide!!! Veuillez entrer le bon nombre de couleurs.")
        return entre_combinaison(possible, nombre_trous)
    elif any(c in special_characters for c in test):
        print("Type d'entrée contient des caractères spéciaux:")
        return entre_combinaison(possible, nombre_trous)
    elif any(d not in possible for d in test):
        print("Type de couleur choisie non valide")
        return entre_combinaison(possible, nombre_trous)
    else:
        for i in range(nombre_trous):
            essai.append((test[i]))
        return essai


def entre_menu(retour_choix_possible, nombre_de_choix): #Vérifie que le chiffre  entrée dans le menu par l'utilisateur est valide

    special_characters = "!@#$%'^&*() -+?_\\=,<>/"
    test = ''
    test = input(">> ")

    if any(c in special_characters for c in test):
        print("Entrée contenant des caractères spéciaux:")
        return entre_menu(retour_choix_possible, nombre_de_choix)
    elif (test not in retour_choix_possible):
        print("Entrée invalide!!! Veuillez entrer un numéro.")
        return entre_menu(retour_choix_possible, nombre_de_choix)
    elif (test == "3")or(test == "4"):
        retour_choix_possible[2] = "x"
        retour_choix_possible[3] = "x"
    elif(test == "1")or(test == "2"):
        retour_choix_possible[0] = "x"
        retour_choix_possible[1] = "x"
    elif (test == "5"):
        retour_choix_possible[5] = "x"
    
    return test, retour_choix_possible


###############################
# SAUVEGARDE RESULTATS PARTIE #
###############################

def sauvegarde_partie() :

    f = open('MASTERMIND_sauvegarde.text', 'w')

    f.write(f'{choix_affichage}\n')
    f.close()


