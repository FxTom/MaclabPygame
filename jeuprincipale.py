#!/usr/bin/pyhton3
# -*-coding:utf-8 -*
import pygame
from pygame.locals import *
from classe import *
from constante import *



pygame.init()

window = pygame.display.set_mode((lenght_window, lenght_window))

pygame.time.Clock().tick(30)
#load the labyrinth
level = Labyrinth("level1.txt")
level.load_lab()
level.display_lab(window)
#load the picture
lose = pygame.image.load("youlose.png").convert_alpha()
win = pygame.image.load("youwin.png").convert_alpha()
floor = pygame.image.load("floor.jpg").convert()
#create the character and 3 parts of the seringue
mcg = Perso("mac.jpg", level)
first_item = Tresor("tresor.png", level)
first_item.display_tresor(window)
second_item = Tresor("tresor.png", level)
second_item.display_tresor(window)
third_item = Tresor("tresor.png", level)
third_item.display_tresor(window)
pygame.display.flip()

count_item = 0
stop = 1
#Loop of the game
while stop:
    for event in pygame.event.get():
        if event.type == QUIT:
            stop = 0
        elif event.type == KEYDOWN:
            if event.key == K_DOWN:
                mcg.move('down')
            elif event.key == K_UP:
                mcg.move('up')
            elif event.key == K_RIGHT:
                mcg.move('right')
            elif event.key == K_LEFT:
                mcg.move('left')
    #for disappear the tresor when you take this
    if mcg.case_x == first_item.x / lenght_sprite \
    and mcg.case_y == first_item.y / lenght_sprite:
        it1 = 1
    elif mcg.case_x == second_item.x / lenght_sprite \
    and mcg.case_y == second_item.y / lenght_sprite:
        it2 = 1
    elif mcg.case_x == third_item.x / lenght_sprite \
    and mcg.case_y == third_item.y / lenght_sprite:
        it3 = 1

    window.blit(floor, (0, 0))
    level.display_lab(window)
    window.blit(mcg.picture, (mcg.x, mcg.y))

    if it1 == 0:
        window.blit(first_item.picture, (first_item.x, first_item.y))
        count_item += 1
    if it2 == 0:
        window.blit(second_item.picture, (second_item.x, second_item.y))
        count_item += 1
    if it3 == 0:
        window.blit(third_item.picture, (third_item.x, third_item.y))
        count_item += 1

    pygame.display.flip()

    if level.structure[mcg.case_y][mcg.case_x] == 'O':
        if it1 == 1 and it2 == 1 and it3 == 1:
            window.blit(win, (0, 0))
            pygame.display.flip()
        else:
            window.blit(lose, (0, 0))
            pygame.display.flip()
        stop = 0
