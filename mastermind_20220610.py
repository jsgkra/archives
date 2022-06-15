#!/usr/bin/env python3
#Made by SuperGroupIV
from mastermind_librairie_20220610 import *
import os
import time
from threading import Thread
#import pygame

#Initialisation
choix = True

Thread(target = play_music).start()
clean_terminal_screen()             # Efface l'écran

titre_intro()                       # Affiche le titre
regle_jeu()                         # Affiche les règles

while choix:                        # Boucle principale (menu + jeu)
    
    #Initialisation
    sauvegarde_place = []           # Nombre d'éléments de bonne couleur à la mauvaise place de toutes les tentatives
    sauvegarde_couleur_place = []   # Nombre d'éléments de bonne couleur et à la bonne place de toutes les tentatives
    sauvegarde = []                 # Contient toutes le tentatives
    tentative = []                  # proposition du joueur
    possible = ["R", "V", "B", "J"] # Combinaison à chercher
    i = 1                           # compteur des tentatives
    combinaison = []                # Combinaison à trouver
    nouveau_types_difficultes = ["1", "2", "3", "4","5", "9", "10", "11", ""] # numéro qui peuvent être choisis dans le menu 
    numero = "0"                                                              # numéro sélectioner                                                                    
    types_difficultes = [0, 0, 0, 0]                                          # types de difficulté qui peuvent-être choisies 0 = disponible et 1 = indisponible

    #Difficultés par défaut
    affichage_complet = True        # Affiche toutes les tentatives     
    nb_secondes = 0                 # pas de timer
    nombre_trous = 4                # 4 trous
    nombre_couleur = 4              # 4 couleurs
    nombre_de_choix = 0             # Pas encore de difficultés sélectionées
    

    while nombre_de_choix < 3:                                                   # Boucle menu
        affichage_choix_menu(types_difficultes, nombre_de_choix)                 # Affiche le menu
        input_numero = entre_menu(nouveau_types_difficultes, nombre_de_choix)    # Input du numéro choisi et actualisation de la possibilité des choix dans le menu. Return numéro et types_de_difficultés
        numero = input_numero[0]                                                 # Numéro choisi
        nouveau_types_difficultes = input_numero[1]                              # numero qu'il est possible d'entrée dans le menu
        if numero == "":                                                         # Si on tappe Enter (sauf si on a pas sélectionné au moins une difficulté, voir entre_menu()) on sort du menu
            break
        elif types_difficultes == [1, 1, 1, 1]:                                  # Si on a choisi une difficulté de chaque type, on sort du menu                    
            break                                   
        elif numero == "9":                                                      # Affiche le menu
            regle_jeu()
        elif numero == "10":                                                     # break = quitter menu, ["STOP"] = quitter jeu
            combinaison = "STOP"
            print("Au revoir et à bientôt")
            time.sleep(1)
            clean_terminal_screen()
            sauvegarde_partie()
            break
        else:
            types_difficultés = modification_types_diffcultes(numero, types_difficultes)        # modifie les types de difficultés possiblement sélectionables et affichables
            recu_menu = menu(numero, nombre_trous, nombre_couleur, affichage_complet,possible)  # Modifie les valeurs par défaut suivant les diffiucltés selectionnées
            nombre_trous = recu_menu[0]
            nombre_couleur = recu_menu[1]
            affichage_complet = recu_menu[2]
            possible = recu_menu[3]
            nombre_de_choix = nombre_de_choix +1                                                # Le joueur a choisi une difficulté suplémentaire, il peut en choisir au maximum 4.
    
    clean_terminal_screen()                      # Clean l'écran
    if combinaison == "STOP":                    # Quitter jeu
        break
    else :
        combinaison = combinaison = combinaison_aleatoire_difficulte(nombre_couleur, nombre_trous) # Création de la combinaison à trouver
    
    
    #Jeu
    
    exemple_liste = combinaison_aleatoire(possible, nombre_couleur, nombre_trous)
    exemple = "".join(exemple_liste)
    consigne(nombre_couleur, nombre_trous, possible, exemple)
    
    while combinaison != tentative:                                                       # Boucle di jeu
        
            if i <= 12:                                                                   # Pour gagner, le joueur doit trouver la combinaison en 12 tentatives
                tentative = entre_combinaison(possible, nombre_trous)                     # Controle série 
                sauvegarde.append(tentative)                                              # Retiens les tentatives
                couleur_place = ind_couleur_place(combinaison, tentative, nombre_trous)   # Recherche le nombre d'éléments de bonne couleur et à la bonne place
                place = ind_couleur(couleur_place[1], couleur_place[2], nombre_trous)     # Recherche le nombre d'éléments de bonne couleur et à la mauvaise place
                sauvegarde_place.append(place)                                            # Retiens indicateurs couleurs 
                sauvegarde_couleur_place.append(couleur_place[0])                         # Retiens indicateurs couleurs + places
                clean_terminal_screen()                                                   # Efface l'écran
                if 12-i > 3 :                                                             # print le nombre de tentatives restantes
                    print(f"Il vous reste {12-i} tentatives\n\n")                         
                elif 12-i <=3 :
                    print(f"Il vous reste \033[31m\033[1m{12-i}\033[0m tentatives!\033[0m\n\n")
                elif 12-i > 2 :
                    print(f"Encore \033[31m\033[1m{12-i}\033[0m tentative!\033[0m\n\n")

                choix_affichage(affichage_complet, sauvegarde, sauvegarde_couleur_place, sauvegarde_place, i-1, nombre_trous)     # Affiche les tentatives et les indicateurs
                consigne(nombre_couleur, nombre_trous, possible, exemple)
                i = i+1
                if couleur_place[0] == nombre_trous:                                   # Gagner 
                    affichage_gagner(i-1)                                              # Affiche l'encart "gagner"
                    time.sleep(2)
                    choix_affichage(affichage_complet, sauvegarde, sauvegarde_couleur_place, sauvegarde_place, i-2, nombre_trous) # Affiche les tentatives et les indicateurs
                    choix = continuer_ou_laisser()      # le joueur peut soit retourner au menu soit quitter
                    
                    if choix == False:
                        print(" Goodbye ")
                        time.sleep(2)
                        break
                    else:
                        continue
            else:                                            # Perdre 
                
                affichage_perdre(combinaison, nombre_trous)  # Affiche l'encart "perdre
                time.sleep(2)
                choix = continuer_ou_laisser()               # le joueur peut soit retourner au menu soit quitter
                if choix == False:
                    print(f" Goodbye\n")
                    time.sleep(2)
                    break
                else:
                    tentative = combinaison                  # quitte la boucle while tentative != combinaison

    clean_terminal_screen()
