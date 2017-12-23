from constante import *
from pygame.locals import *
from random import randrange
from pygame import *
import pygame

class Labyrinth:

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
                for sprite in line:
                    if sprite != "\n":
                        line_level.append(sprite)
                structure_level.append(line_level)
            self.structure = structure_level

    def display_lab(self, window):
        """ display the labyrinth with the guardian
            and display the wall"""
        wall = pygame.image.load("wall.jpg").convert()
        guardian = pygame.image.load("guardian.jpg").convert()

        count_line = 0
        for ligne in self.structure:
            num_case = 0
            for sprite in ligne:
                x = num_case * lenght_sprite
                y = count_line * lenght_sprite
                if sprite == '+':
                    window.blit(wall, (x, y))
                elif sprite == 'O':
                    window.blit(guardian, (x, y))
                num_case += 1
            count_line += 1

class Perso:

    def __init__(self, picture, level):
        """Initialized the characer"""
        self.picture = pygame.image.load(picture).convert()
        self.x = 0
        self.y = 0
        self.case_x = 0
        self.case_y = 0
        self.level = level

    def move(self, direction):
        """move the character in the good direction sprite by sprite"""
        if direction == 'right':
            if self.case_x < nb_of_case - 1:
                if self.level.structure[self.case_y][self.case_x+1] != "+":
                    self.case_x += 1
                    self.x = self.case_x * lenght_sprite

        if direction == 'left':
            if self.case_x > 0:
                if self.level.structure[self.case_y][self.case_x-1] != "+":
                    self.case_x -= 1
                    self.x = self.case_x * lenght_sprite

        if direction == 'down':
            if self.case_y < nb_of_case - 1:
                if self.level.structure[self.case_y+1][self.case_x] != "+":
                    self.case_y += 1
                    self.y = self.case_y * lenght_sprite

        if direction == 'up':
            if self.case_y > 0:
                if self.level.structure[self.case_y-1][self.case_x] != "+":
                    self.case_y -= 1
                    self.y = self.case_y * lenght_sprite

class Tresor:

    def __init__(self, picture, level):
        """Initialized a part of the seringue"""
        self.picture = pygame.image.load(picture).convert_alpha()
        self.level = level
        self.x = 0
        self.y = 0
        self.case_x = 0
        self.case_y = 0

    def display_tresor(self,window):
            """display the tresor somewhere in the labyrinth"""
            i = 0
            limited = (len(self.level.structure)-1)*lenght_sprite
            self.x = randrange(0,limited,lenght_sprite)
            self.y = randrange(0,limited,lenght_sprite)
            self.case_x = int(self.x / lenght_sprite)
            self.case_y = int(self.y / lenght_sprite)
            while i == 0:
                if self.level.structure[self.case_y][self.case_x] != "x":
                    self.x = randrange(0,limited,lenght_sprite)
                    self.y = randrange(0,limited,lenght_sprite)
                    self.case_x = int(self.x / lenght_sprite)
                    self.case_y = int(self.y / lenght_sprite)
                elif self.level.structure[self.case_y][self.case_x] == "x":
                        window.blit(self.picture, (self.x,self.y))
                        i += 1
