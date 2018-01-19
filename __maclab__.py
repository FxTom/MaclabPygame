#! /usr/bin/env python3
# -*-coding:utf-8 -*

"""
This my project 3 of the Python web developer courses of Openclassrooms.
Macgyver must escape the labyrinth.
"""

import pygame
from pygame.locals import *
from classes import Labyrinth, Perso, Tresor
from constant import LENGHT_SPRITE, LENGHT_WINDOW, LEVELS, IT1, IT2, IT3

pygame.init()

WINDOW = pygame.display.set_mode((LENGHT_WINDOW, LENGHT_WINDOW))
pygame.display.set_caption("Game FX")

pygame.time.Clock().tick(30)
#load the labyrinth
LEVEL = Labyrinth(LEVELS)
LEVEL.load_lab()
LEVEL.display_lab(WINDOW)
#load the picture
LOSE = pygame.image.load("picture/youlose.png").convert_alpha()
WIN = pygame.image.load("picture/youwin.png").convert_alpha()
FLOOR = pygame.image.load("picture/floor.jpg").convert()
#create the character and 3 parts of the seringue
MCG = Perso("picture/mac.jpg", LEVEL)
FIRST_ITEM = Tresor("picture/tresor.png", LEVEL)
FIRST_ITEM.display_tresor(WINDOW)
SECOND_ITEM = Tresor("picture/tresor.png", LEVEL)
SECOND_ITEM.display_tresor(WINDOW)
THIRD_ITEM = Tresor("picture/tresor.png", LEVEL)
THIRD_ITEM.display_tresor(WINDOW)
pygame.display.flip()

STOP = 1
#main loop
while STOP:
    for event in pygame.event.get():
        if event.type == QUIT:
            STOP = 0
        elif event.type == KEYDOWN:
            if event.key == K_DOWN:
                MCG.move('down')
            elif event.key == K_UP:
                MCG.move('up')
            elif event.key == K_RIGHT:
                MCG.move('right')
            elif event.key == K_LEFT:
                MCG.move('left')
    #for disappear the tresor when you take this
    if MCG.case_x == FIRST_ITEM.x_for_x / LENGHT_SPRITE \
    and MCG.case_y == FIRST_ITEM.y_for_y / LENGHT_SPRITE:
        IT1 = 1
    elif MCG.case_x == SECOND_ITEM.x_for_x / LENGHT_SPRITE \
    and MCG.case_y == SECOND_ITEM.y_for_y / LENGHT_SPRITE:
        IT2 = 1
    elif MCG.case_x == THIRD_ITEM.x_for_x / LENGHT_SPRITE \
    and MCG.case_y == THIRD_ITEM.y_for_y / LENGHT_SPRITE:
        IT3 = 1

    WINDOW.blit(FLOOR, (0, 0))
    LEVEL.display_lab(WINDOW)
    WINDOW.blit(MCG.picture, (MCG.x_x, MCG.y_y))

    if IT1 == 0:
        WINDOW.blit(FIRST_ITEM.picture, (FIRST_ITEM.x_for_x, FIRST_ITEM.y_for_y))
    if IT2 == 0:
        WINDOW.blit(SECOND_ITEM.picture, (SECOND_ITEM.x_for_x, SECOND_ITEM.y_for_y))
    if IT3 == 0:
        WINDOW.blit(THIRD_ITEM.picture, (THIRD_ITEM.x_for_x, THIRD_ITEM.y_for_y))

    pygame.display.flip()

    if LEVEL.structure[MCG.case_y][MCG.case_x] == 'O':
        if IT1 == 1 and IT2 == 1 and IT3 == 1:
            WINDOW.blit(WIN, (0, 0))
            pygame.display.flip()
            STOP = 0
        else:
            WINDOW.blit(LOSE, (0, 0))
            pygame.display.flip()
            STOP = 0
