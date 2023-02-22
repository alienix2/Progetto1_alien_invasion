import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Classe che gestisce i proiettili sparati dalla navicella"""
    
    def __init__(self, game):
        """Crea un proiettile dalla posizione attuale della navicella"""
        
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.bullet_color
        
        #Creo il proiettile in posizione 0,0 e subito lo sposto al centro sopra al rettangolo della vanicella
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = game.ship.rect.midtop
        
        self.y_position = float(self.rect.y)
    
    def update(self):
        """Aggiorna la posizione del proiettile sullo schermo"""
        
        self.y_position -= self.settings.bullet_speed
        self.rect.y = self.y_position
    
    def draw_bullet(self):
        """Disegna il proiettile"""
        
        pygame.draw.rect(self.screen, self.color, self.rect)