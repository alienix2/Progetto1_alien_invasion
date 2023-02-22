import pygame

from pygame.sprite import Sprite

class Settings:
    """Class that stores settings for the game"""
    
    def __init__(self):
        """Inizializza le impostazioni del gioco"""
        self.screen_width = 800
        self.screen_height = 800
        self.bg_color = (200, 255, 100)
        self.caption = "Gioco alien invasion"
        
        #Impostazioni della navicella
        self.ship_speed = 0.5
        
        #Impostazioni del proiettile
        self.bullets_limit = 5
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 0, 0)
        
        #Impostazioni degli alieni
        self.fleet_speed = 0.5
        self.fleet_drop_speed = 10
        self.fleet_direction = 1 #1 destra, -1 sinistra