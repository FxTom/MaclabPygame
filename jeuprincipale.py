import pygame
from pygame.locals import *
from classe import *
from constante import *



pygame.init()

fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))

pygame.time.Clock().tick(30)
niveau = Niveau("level1.txt")
niveau.charger_le_labyrinthe()
niveau.afficher_labyrinthe(fenetre)
lose = pygame.image.load("youlose.png").convert_alpha()
win = pygame.image.load("youwin.png").convert_alpha()
mcg = Perso("mac.jpg", niveau)
floor = pygame.image.load("floor.jpg").convert()
seringue1 = Tresor("tresor.png", niveau)
seringue1.afficher(fenetre)
seringue2 = Tresor("tresor.png", niveau)
seringue2.afficher(fenetre)
seringue3 = Tresor("tresor.png", niveau)
seringue3.afficher(fenetre)
pygame.display.flip()
compteur_objet = 0

stopper = 1
while stopper:
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

    if mcg.case_x == seringue1.x / longueur_sprite \
    and mcg.case_y == seringue1.y / longueur_sprite:
        se1 = 1
    elif mcg.case_x == seringue2.x / longueur_sprite \
    and mcg.case_y == seringue2.y / longueur_sprite:
        se2 = 1
    elif mcg.case_x == seringue3.x / longueur_sprite \
    and mcg.case_y == seringue3.y / longueur_sprite:
        se3 = 1

    fenetre.blit(floor, (0, 0))
    niveau.afficher_labyrinthe(fenetre)
    fenetre.blit(mcg.image, (mcg.x, mcg.y))
    if se1 == 0:
        fenetre.blit(seringue1.image, (seringue1.x, seringue1.y))
        compteur_objet += 1
    if se2 == 0:
        fenetre.blit(seringue2.image, (seringue2.x, seringue2.y))
        compteur_objet += 1
    if se3 == 0:
        fenetre.blit(seringue3.image, (seringue3.x, seringue3.y))
        compteur_objet += 1
    pygame.display.flip()

    if niveau.structure[mcg.case_y][mcg.case_x] == 'O':
        if se1 == 1 and se2 == 1 and se3 == 1:
            fenetre.blit(win, (0, 0))
            pygame.display.flip()
        else:
            fenetre.blit(lose, (0, 0))
            pygame.display.flip()
        stopper = 0
