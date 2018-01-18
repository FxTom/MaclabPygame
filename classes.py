"""All classes of my game"""

from random import randrange
import pygame
from pygame import sprite
from pygame.locals import *
from constant import LENGHT_SPRITE, NB_OF_CASE




class Labyrinth:

    """class for creat lab"""

    def __init__(self, lab):
        """Initialized the labyrinth"""
        self.lab = lab
        self.struture = 0

    def load_lab(self):
        """load the labyrinth in file .txt"""
        with open(self.lab, "r") as lab:
            structure_level = []
            for line in lab:
                line_level = []
                for sprites in line:
                    if sprites != "\n":
                        line_level.append(sprite)
                structure_level.append(line_level)
            self.structure = structure_level

    def display_lab(self, window):
        """ display the labyrinth with the guardian
            and display the wall"""
        wall = pygame.image.load("picture/wall.jpg").convert()
        guardian = pygame.image.load("picture/guardian.jpg").convert()

        count_line = 0
        for line in self.structure:
            num_case = 0
            for yolo in line:
                x_in_x = num_case * LENGHT_SPRITE
                y_in_y = count_line * LENGHT_SPRITE
                if yolo == '+':
                    window.blit(wall, (x_in_x, y_in_y))
                elif yolo == 'O':
                    window.blit(guardian, (x_in_x, y_in_y))
                num_case += 1
            count_line += 1

class Perso:

    """Create perso"""

    def __init__(self, picture, level):
        """Initialized the characer"""
        self.picture = pygame.image.load(picture).convert()
        self.x_x = 0
        self.y_y = 0
        self.case_x = 0
        self.case_y = 0
        self.level = level

    def move(self, direction):
        """move the character in the good direction sprite by sprite"""
        if direction == 'right':
            if self.case_x < NB_OF_CASE - 1:
                if self.level.structure[self.case_y][self.case_x+1] != "+":
                    self.case_x += 1
                    self.x_x = self.case_x * LENGHT_SPRITE

        if direction == 'left':
            if self.case_x > 0:
                if self.level.structure[self.case_y][self.case_x-1] != "+":
                    self.case_x -= 1
                    self.x_x = self.case_x * LENGHT_SPRITE

        if direction == 'down':
            if self.case_y < NB_OF_CASE - 1:
                if self.level.structure[self.case_y+1][self.case_x] != "+":
                    self.case_y += 1
                    self.y_y = self.case_y * LENGHT_SPRITE

        if direction == 'up':
            if self.case_y > 0:
                if self.level.structure[self.case_y-1][self.case_x] != "+":
                    self.case_y -= 1
                    self.y_y = self.case_y * LENGHT_SPRITE

class Tresor:

    """Create a tresor"""

    def __init__(self, picture, level):
        """Initialized a part of the seringue"""
        self.picture = pygame.image.load(picture).convert_alpha()
        self.level = level
        self.x_for_x = 0
        self.y_for_y = 0
        self.case_x = 0
        self.case_y = 0

    def display_tresor(self, window):
        """display the tresor somewhere in the labyrinth"""
        i = 0
        limited = (len(self.level.structure)-1)*LENGHT_SPRITE
        self.x_for_x = randrange(0, limited, LENGHT_SPRITE)
        self.y_for_y = randrange(0, limited, LENGHT_SPRITE)
        self.case_x = int(self.x_for_x / LENGHT_SPRITE)
        self.case_y = int(self.y_for_y / LENGHT_SPRITE)
        while i == 0:
            if self.level.structure[self.case_y][self.case_x] != "x":
                self.x_for_x = randrange(0, limited, LENGHT_SPRITE)
                self.y_for_y = randrange(0, limited, LENGHT_SPRITE)
                self.case_x = int(self.x_for_x / LENGHT_SPRITE)
                self.case_y = int(self.y_for_y / LENGHT_SPRITE)
            elif self.level.structure[self.case_y][self.case_x] == "x":
                window.blit(self.picture, (self.x_for_x, self.y_for_y))
                i += 1
