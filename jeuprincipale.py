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

    fenetre.blit(floor,(0,0))
    niveau.afficher_labyrinthe(fenetre)
    fenetre.blit(mcg.image,(mcg.x,mcg.y))
    fenetre.blit(seringue1.image,(seringue1.x,seringue1.y))
    fenetre.blit(seringue2.image,(seringue2.x,seringue2.y))
    fenetre.blit(seringue3.image,(seringue3.x,seringue3.y))
    pygame.display.flip()

    if niveau.structure[mcg.case_y][mcg.case_x] == 'O':
        stopper = 0
#    elif niveau.structure[mcg.case_y][mcg.case_x] == niveau.structure[seringue1.y][seringue1.x]:
#        fenetre.blit(floor,(0,0))
#        niveau.afficher_labyrinthe(fenetre)
#        fenetre.blit(mcg.image,(mcg.x,mcg.y))
#        fenetre.blit(seringue2.image,(longueur_sprite*11,longueur_sprite*12))
#        fenetre.blit(seringue3.image,(longueur_sprite*5,longueur_sprite*7))
#        pygame.display.flip()
