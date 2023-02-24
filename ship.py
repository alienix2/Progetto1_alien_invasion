import pygame
from pygame.sprite import Sprite

import settings

class Ship(Sprite):
    """Classe che definisce una navetta"""
    
    def __init__(self, game):
        """Inizializza la navetta"""
        
        super().__init__()
        
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings
        
        #Carico la foto nel rettangolo della navetta
        self.image = pygame.image.load(".\progetto1_alien_invasion\images\ship.bmp")
        self.image.set_colorkey((230,230,230))  #Rimuovo lo sfondo grigio
        self.rect = self.image.get_rect()
        
        #Metto la navicella in fondo allo schermo in centro
        self.rect.midbottom = self.screen_rect.midbottom
        
        #Posizione navicella
        self.x_position = float(self.rect.x)
        
        #Parametri per spostamento
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """Aggiorna la posizione della nave"""
        
        if self.moving_right == True:
            self.x_position = (self.x_position + self.settings.ship_speed)%800
        
        if self.moving_left == True:
            self.x_position = (self.x_position - self.settings.ship_speed)%800
        
        self.rect.x = self.x_position
    
    def center_ship(self):
        """Riporta la navicella in centro"""
        
        self.rect.midbottom = self.screen_rect.midbottom
        self.x_position = float(self.rect.x)
    
    def blitme(self):
        """Disegna la navetta"""
        self.screen.blit(self.image, self.rect)