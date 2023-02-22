import pygame

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