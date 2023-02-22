import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

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
        
        #Definisco il gruppo di sprites per i proiettili
        self.bullets = pygame.sprite.Group()
        
        #Definisco il gruppo di sprites per gli alieni e li creo all'inizio
        self.aliens = pygame.sprite.Group()
        self.create_fleet()
        
    def create_fleet(self):
        """Creates the fleet of aliens"""
        self.aliens.add(Alien(self))
    
    def clear_junk(self):
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
       
    def check_keydown_events(self, event):
        """Risponde se un pulsante è premuto"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            if len(self.bullets) <= self.settings.bullets_limit : self.bullets.add(Bullet(self))
            
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
    
    def update_bullets(self):
        """aggiorna lo stato dei proiettili"""
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.clear_junk
                
    def update_screen(self):
        """Aggiorna lo schermo generale"""
        
        #In questa parte si aggiorna lo sfondo in modo che le cose che disegno sparicano nelle loro "vecchie posizioni"
        self.screen.fill(self.settings.bg_color)
        #Disegno la navetta nella nuova posizione
        self.ship.blitme()
        #Disegno i proiettili nelle nuove posizioni
        self.update_bullets()
        #Disegno la flotta di alieni
        self.aliens.draw(self.screen)
        
        #Mostro il display aggiornato
        pygame.display.flip()
    
    def run_game(self):
        """Avvia il main loop del gioco"""
        
        while True:
            #Controllo se ci sono eventi di mouse o tastiera
            self.check_events()
            
            #Cambia la posizione della nave in base alla situazione dei tasti
            self.ship.update()
            
            #Cambia la posizione dei proiettili in base al tempo
            self.bullets.update()
            
            #Rimuovo i proiettili che escono dallo schermo
            self.clear_junk()
            
            #Aggiorno effettivamente le cose disegnate a schermo
            self.update_screen()
    
if __name__ == "__main__":
    """Crea un'istanza ed avvia il gioco"""
    game = AlienInvasion()
    game.run_game()