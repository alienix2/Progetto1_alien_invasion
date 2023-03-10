import pygame
from pygame.sprite import Sprite

import settings

class Alien(Sprite):
    """Classe che definisce un alieno"""

    def __init__(self, game):
        """Inizializza l'alieno"""
        
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        
        #Carico la foto dell'alieno nel rettangolo 
        self.image = pygame.image.load(".\\progetto1_alien_invasion\\images\\alien.bmp")
        self.image.set_colorkey((230,230,230))  #Rimuovo lo sfondo grigio
        self.rect = self.image.get_rect()
        
        #Posizione iniziale dell'alieno
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        #Posizioni precise con decimali
        self.x_position = float(self.rect.x)
        self.y_position = float(self.rect.y)
    
    def check_edges(self):
        """Ritorna True se l'alieno ha sbattuto ad un bordo"""
        screen_rect = self.screen.get_rect()
        return self.rect.right >= screen_rect.right or self.rect.left <= 0
    
    def update(self):
        """Aggiorna la posizione degli alieni secondo il giusto pattern"""
        
        self.x_position += (self.settings.fleet_speed * self.settings.fleet_direction)
        self.rect.x = self.x_position
        #self.rect.y = self.y_position