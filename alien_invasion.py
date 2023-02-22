import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Classe base per gestire assets e comportamento"""
    
    def __init__(self):
        #Inizializza il gioco
        pygame.init()
        
        #background color
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((self.settings.screen_height, self.settings.screen_width))
        pygame.display.set_caption(self.settings.caption)
        
        #Disegno la navetta
        self.ship = Ship(self)
        
    def check_keydown_events(self, event):
        """Risponde se un pulsante è premuto"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
            
    def check_keyup_events(self, event):
        """Risponde se un pulsante è rilasciato"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        
    def check_events(self):
        """"Controlla se sono avvenuti eventi e si comporta di conseguenza"""
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self.check_keyup_events(event)
                
                
    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        
        #Mostro il display aggiornato
        pygame.display.flip()
    
    def run_game(self):
        """Avvia il main loop del gioco"""
        
        while True:
            #Controllo se ci sono eventi di mouse o tastiera
            self.check_events()
            
            #Cambia la posizione della nave in base alla situazione dei tasti
            self.ship.update_position()
            
            #Aggiorno lo schermo
            self.update_screen()
    
if __name__ == "__main__":
    """Crea un'istanza ed avvia il gioco"""
    game = AlienInvasion()
    game.run_game()