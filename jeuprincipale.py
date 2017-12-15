import pygame
from pygame.locals import *
from classe import *
from constante import *
from random import *


pygame.init()    #initialiser pygame

fenetre = pygame.display.set_mode((cote_fenetre,cote_fenetre))    #créer un fenetre

pygame.time.Clock().tick(30)
niveau = Niveau("level1.txt")
niveau.charger_le_labyrinthe()
niveau.afficher_labyrinthe(fenetre)
mcg = Perso("mac.jpg",niveau)
floor = pygame.image.load("floor.jpg").convert()
seringue1 = Tresor("tresor.png",niveau,longueur_sprite*2,longueur_sprite*12)
seringue2 = Tresor("tresor.png",niveau,longueur_sprite*11,longueur_sprite*12)
seringue3 = Tresor("tresor.png",niveau,longueur_sprite*5,longueur_sprite*7)
pygame.display.flip()                                   #rafraichir l'ecran

stopper = 1
while stopper:                     #boucle infinie
    for event in pygame.event.get():
        if event.type == QUIT:
            stopper = 0
        elif event.type == KEYDOWN:
            if event.key == K_DOWN:
                mcg.deplacer('bas')
            elif event.key == K_UP:
                mcg.deplacer('haut')
            elif event.key == K_RIGHT:
                mcg.deplacer('droite')
            elif event.key == K_LEFT:
                mcg.deplacer('gauche')

    if mcg.case_x == seringue1.x / longueur_sprite and mcg.case_y == seringue1.y / longueur_sprite :
        se1 = 1
    if mcg.case_x == seringue2.x / longueur_sprite and mcg.case_y == seringue2.y / longueur_sprite :
        se2 = 1
    if mcg.case_x == seringue3.x / longueur_sprite and mcg.case_y == seringue3.y / longueur_sprite :
        se3 = 1

    fenetre.blit(floor,(0,0))
    niveau.afficher_labyrinthe(fenetre)
    fenetre.blit(mcg.image,(mcg.x,mcg.y))
    if se1 == 0:
        fenetre.blit(seringue1.image,(seringue1.x,seringue1.y))
    if se2 == 0:
        fenetre.blit(seringue2.image,(seringue2.x,seringue2.y))
    if se3 == 0:
        fenetre.blit(seringue3.image,(seringue3.x,seringue3.y))
    pygame.display.flip()

    if niveau.structure[mcg.case_y][mcg.case_x] == 'O':
        stopper = 0
        if se1 == 1 and se2 == 1 and se3 == 1:
            print("You win!!!")
        else:
            print("You loose!!!")
