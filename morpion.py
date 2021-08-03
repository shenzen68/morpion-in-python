# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *

pygame.init()

def Somme(morpion):
	somme = 0
	for k in range(3):
		somme = 0
		for l in range(3):
			somme += morpion[k][l]
			if somme == 3:
				return 1
			if somme == -3:
				return -1

	for l in range(3):
		somme = 0
		for k in range(3):
			somme += morpion[k][l]
			if somme == 3:
				return 1
			if somme == -3:
				return -1

	somme = morpion[0][0] + morpion[1][1] + morpion[2][2]

	if somme == 3:
		return 1
	if somme == -3:
		return -1

	somme = morpion[0][2] + morpion[1][1] + morpion[2][0]

	if somme == 3:
		return 1
	if somme == -3:
		return -1

	return 0



fenetre = pygame.display.set_mode((300, 400))

#Chargement des images
fond = pygame.image.load("background.jpg").convert()
croix = pygame.image.load("croix.png").convert_alpha()
rond = pygame.image.load("rond.png").convert_alpha()


#Definition de la police de charactère
font = pygame.font.Font(None,90)

menu = 1
continuer = 1
jeu = 0
fin = 0

while continuer:
	for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
		if event.type == QUIT:     #Si un de ces événements est de type QUIT
			continuer = 0     #On arrête la boucle


	#Affichage du menu de debut
	while menu:
		for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
			if event.type == QUIT:     #Si un de ces événements est de type QUIT
				menu = 0     #On arrête la boucle
				continuer = 0
			if event.type == MOUSEBUTTONDOWN and event.button == 1:
				if 100<event.pos[1]<200:
					jeu = 1
					joueurs = 1
					menu = 0
				if 200<event.pos[1]<300:
					jeu = 1
					joueurs = 2
					menu = 0
				if 300<event.pos[1]<400:
					continuer = 0
					menu = 0

		fenetre.blit(fond, (0,0))

		fenetre.blit(font.render("Menu", 1, (255,0,0)), (0,0))
		fenetre.blit(font.render("1 joueur", 1, (255,0,0)), (0,100))
		fenetre.blit(font.render("2 joueurs", 1, (255,0,0)), (0,200))
		fenetre.blit(font.render("Quitter", 1, (255,0,0)), (0,300))

		pygame.display.flip()



	#On initialise les variables du jeu
	morpion = [[0,0,0],[0,0,0],[0,0,0]]
	tour = 0

	#Boucle infinie du jeu
	while jeu:
		for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
			if event.type == QUIT:     #Si un de ces événements est de type QUIT
				jeu = 0      #On arrête la boucle
				continuer = 0

			#Recheche de la cible du clic
			if event.type == MOUSEBUTTONDOWN and event.button == 1:
				#On recherche la collone k
				for k in range(3):
					if k*100 < event.pos[0] < (k+1)*100:
						#On recherche la ligne l
						for l in range(3):
							if l*100 < event.pos[1] < (l+1)*100:
								signe = morpion[k][l]
								#On met la croix ou le rond en fonction du tour
								if signe == 0:
									if tour % 2 == 0:
										morpion[k][l]=1
									else:
										morpion[k][l]=-1
									tour += 1

		somme = Somme(morpion)
		if somme != 0 or tour == 9: # On detecte si le jeu est fini
			fin = 1 # On enclenche le menu de fin
			jeu = 0 # On arrete le jeu

		#Affichage du tableau de jeu de morpion
		fenetre.blit(fond, (0,0))
		for i,col in enumerate(morpion):
			for j,ligne in enumerate(col):
				if ligne == 1:
					fenetre.blit(croix,(i*100,j*100))
				if ligne == -1:
					fenetre.blit(rond,(i*100,j*100) )
		fenetre.blit(font.render("Morpion", 1, (255,0,0)), (0,300))
		pygame.display.flip()

	while fin:
		for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
			if event.type == QUIT:     #Si un de ces événements est de type QUIT
				fin = 0      #On arrête la boucle
				continuer = 0
			if event.type == MOUSEBUTTONDOWN and event.button == 1:
				if 200<event.pos[1]<300:
					jeu = 1
					fin = 0
					menu = 0
				if 300<event.pos[1]<400:
					jeu = 0
					fin = 0
					menu = 1
		fenetre.blit(fond, (0,0))
		if somme == 1:
			fenetre.blit(font.render("Cochon a gagné", 1, (255,0,0)), (0,0))
		if somme == -1:
			fenetre.blit(font.render("Vache a gagné", 1, (255,0,0)), (0,0))
		if tour == 9:
			fenetre.blit(font.render("Egalité", 1, (255,0,0)), (0,0))
		fenetre.blit(font.render("Rejouer", 1, (255,0,0)), (0,200))
		fenetre.blit(font.render("Menu", 1, (255,0,0)), (0,300))
		pygame.display.flip()
