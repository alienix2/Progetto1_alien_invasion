import pygame

from pygame.sprite import Sprite

class Settings:
    """Class that stores settings for the game"""
    
    def __init__(self):
        """Inizializza le impostazioni statiche del gioco"""
        
        self.screen_width = 800
        self.screen_height = 800
        self.bg_color = (200, 255, 100)
        self.caption = "Gioco alien invasion"
        
        #Impostazioni del proiettile
        self.bullets_limit = 5
        self.bullet_width = 1000
        self.bullet_height = 15
        self.bullet_color = (0, 0, 0)
        
        #Impostazioni degli alieni
        self.fleet_drop_speed = 30
        self.fleet_direction = 1 #1 destra, -1 sinistra
        
        #Impostazioni delle statistiche
        self.ships_number_limit = 3
        
        #Impostazione dell'aumento di difficoltà graduale
        self.speedup_scale = 1.1
        self.score_scale = 1.2

        self.inizialize_speed_values()
        self.inizialize_points_values()
        
    def inizialize_speed_values(self):
        self.ship_speed = 0.5
        self.bullet_speed = 1.5
        self.fleet_speed = 0.5
        
    def inizialize_points_values(self):
        self.alien_points = 50    
        
    def increase_speed(self):
        """Aumenta la velocità e i punti proiettile (nota aumenta anche la velocità dei proiettili1)"""
        
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.fleet_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)