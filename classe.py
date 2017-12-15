import pygame
from constante import *
from pygame.locals import *



class Niveau:

    def __init__(self,lab):
        self.lab = lab
        self.struture = 0

    def charger_le_labyrinthe(self):
        with open(self.lab,"r") as lab:
            structure_niveau = []
            for ligne in lab:
                ligne_niveau = []
                for sprite in ligne:
                    if sprite != "\n":
                        ligne_niveau.append(sprite)
                structure_niveau.append(ligne_niveau)
            self.structure = structure_niveau



    def afficher_labyrinthe(self,fenetre):
        mur = pygame.image.load("mur.jpg").convert()
        gardien = pygame.image.load("gardien.jpg").convert()

        compteur_ligne = 0
        for ligne in self.structure:
            num_case = 0
            for sprite in ligne:
                x = num_case * longueur_sprite
                y = compteur_ligne * longueur_sprite
                if sprite == '+':
                    fenetre.blit(mur, (x,y))
                elif sprite == 'O':
                    fenetre.blit(gardien, (x,y))
                num_case += 1
            compteur_ligne += 1





class Perso:

    def __init__(self,ima,niveau):
        self.image = pygame.image.load(ima).convert()
        self.x = 0
        self.y = 0
        self.case_x = 0
        self.case_y = 0
        self.niveau = niveau

    def deplacer(self,direction):
        if direction == 'droite':
            if self.case_x < nb_de_case - 1:
                if self.niveau.structure[self.case_y][self.case_x+1] != "+":
                    self.case_x += 1
                    self.x = self.case_x * longueur_sprite


        if direction == 'gauche':
            if self.case_x > 0:
                if self.niveau.structure[self.case_y][self.case_x-1] != "+":
                    self.case_x -= 1
                    self.x = self.case_x * longueur_sprite


        if direction == 'bas':
            if self.case_y < nb_de_case - 1:
                if self.niveau.structure[self.case_y+1][self.case_x] != "+":
                    self.case_y += 1
                    self.y = self.case_y * longueur_sprite


        if direction == 'haut':
            if self.case_y > 0:
                if self.niveau.structure[self.case_y-1][self.case_x] != "+":
                    self.case_y -= 1
                    self.y = self.case_y * longueur_sprite




class Tresor:

    def __init__(self,image,niveau,x,y):
        self.image = pygame.image.load(image).convert_alpha()
        self.niveau = niveau
        self.x = x
        self.y = y
        self.case_x = 0
        self.case_y = 0
