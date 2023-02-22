import pygame
from pygame.sprite import Sprite

import settings

class Alien(Sprite):
    """Classe che definisce un alieno"""
    
    def __init__(self, game):
        """Inizializza l'alieno"""
        
        super().__init__()
        self.screen = game.screen
        
        #Carico la foto dell'alieno nel rettangolo 
        self.image = pygame.image.load(".\\progetto1_alien_invasion\\images\\alien.bmp")
        self.image.set_colorkey((230,230,230))  #Rimuovo lo sfondo grigio
        self.rect = self.image.get_rect()
        
        #Posizione iniziale dell'alieno
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        #Posizione orizzontale precisa con decimali
        self.x_position = float(self.rect.x)