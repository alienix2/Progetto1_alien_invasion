import sys
import pygame
from time import sleep

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

class AlienInvasion:
    """Classe base per gestire assets e comportamento"""
    
    def __init__(self):
        #Inizializza il gioco
        pygame.init()
        
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.caption)
        
        #Disegno la navetta
        self.ship = Ship(self)
                
        #Inizializzo le statistiche per il gioco
        self.game_stats = GameStats(self)
        self.game_stats.game_active = False

        #Disegno il pulsante da premere per iniziare il gioco
        self.start_button = Button(self, "Inizia a giocare")
        
        #Definisco il gruppo di sprites per i proiettili
        self.bullets = pygame.sprite.Group()
        
        #Definisco il gruppo di sprites per gli alieni e li creo all'inizio
        self.aliens = pygame.sprite.Group()
        self.create_fleet()
        
        #Creo la scoreboard
        self.score = Scoreboard(self)
        self.score.draw_score()
       
    def create_alien(self, x_alien_number, y_alien_number):
        new_alien = Alien(self)
        new_alien.x_position = self.alien_width + 1.5 * self.alien_width * x_alien_number
        new_alien.y_position = self.alien_height + 1.5 * self.alien_height *y_alien_number
        new_alien.rect.x = new_alien.x_position
        new_alien.rect.y = new_alien.y_position
        self.aliens.add(new_alien)   
     
    def create_fleet(self):
        """Crea la flotta di alieni"""
        
        new_alien = Alien(self)
        self.aliens.add(new_alien)
        self.alien_width, self.alien_height = new_alien.rect.size

        #Numero di alieni da spawnare
        self.x_aliens_number = (self.settings.screen_width - (2 * self.alien_width)) // (1.5 * self.alien_width)
        self.y_aliens_number = ((self.settings.screen_height) - 2/5 * (self.settings.screen_height)) // (1.5 * self.alien_height)
        
        for y_alien_number in range(int(self.y_aliens_number)):
            for x_alien_number in range(int(self.x_aliens_number)):
                self.create_alien(x_alien_number, y_alien_number)        
    
    def clear_junk(self):
        """Ripulisce la roba che esce dallo schermo"""
        
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
    
    def start_game(self):
        """Resetta i valori del gioco"""
        
        self.game_stats.reset_stats()
        self.score.prep_score_image()
        self.score.prep_level_image()
        self.score.prep_ships()
        self.game_stats.game_active = True
        self.settings.inizialize_speed_values()
        self.settings.inizialize_points_values()
        pygame.mouse.set_visible = False
    
    def check_start_button(self, mouse_position):
        """Controllo se il muose ha premuto il pulsante di start"""
        
        if self.start_button.rect.collidepoint(mouse_position) and not self.game_stats.game_active:
            self.start_game()    
    
    def reset_game(self):
        """Resetta gli sprites a schermo"""
                    
        self.bullets.empty()
        self.aliens.empty()
        self.score.prep_ships()
        
        self.create_fleet()
        self.ship.center_ship()
    
    def ship_hit(self):
        """Comportamento del programma quando la navetta è colpita dagli alieni"""
        
        if self.game_stats.ships_left > 0:
            self.game_stats.ships_left -= 1
            
            #Inserisco una pausa per far capire al giocatore che è stato colpito
            sleep(1)
        else:
            pygame.mouse.set_visible = True
            self.game_stats.game_active = False
        self.reset_game()
            
    def check_keydown_events(self, event):
        """Risponde se un pulsante è premuto"""
        
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_p:
            if not self.game_stats.game_active:
                self.start_game()
        elif event.key == pygame.K_SPACE:
            if len(self.bullets) <= self.settings.bullets_limit : self.bullets.add(Bullet(self))
            
    def check_keyup_events(self, event):
        """Risponde se un pulsante è rilasciato"""
        
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def check_mousedown_events(self, event):
        """Risponde alla pressione del mouse"""
        
        mouse_position = pygame.mouse.get_pos()
        self.check_start_button(mouse_position)
    
    def check_events(self):
        """"Controlla se sono avvenuti eventi e si comporta di conseguenza"""
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self.check_keyup_events(event)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.check_mousedown_events(event)
    
    def reset_bullets_aliens(self):
        """Resetta i proiettili e ricrea la flotta, aumenta la velocità se dinamica"""
        
        self.bullets.empty()
        self.create_fleet()
        
        #Aumento il numero del livello e la velocità del gioco
        self.game_stats.level += 1
        self.score.prep_level_image()
        self.settings.increase_speed()

    
    def detect_bullet_alien_collisions(self):
        """Controlla se ci sono collisioni fra alieni e proiettili"""
        
        #Controllo se un proiettile ha colpito un alieno (fa tutto il framework in pratica)
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        
        #Se non ci sono più alieni resetto i proiettili e creo una nuova flotta
        if not self.aliens:
            self.reset_bullets_aliens()        
        
        if collisions:
            for collisions in collisions.values():
                self.game_stats.score += self.settings.alien_points * len(collisions)
            
            #Aggiona lo score e controlla se l'highscore è stato superato
            self.score.prep_score_image()
            self.score.set_highscore()
        
    def detect_alien_ship_collision(self):
        """Controlla se un alieno ha toccato la navetta"""
        
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self.ship_hit()
    
    def detect_alien_bottom_screen(self):
        """Controlla se un alieno ha raggiunto il fondo dello schermo"""
        
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                #Non è stata colpita ma attuo lo stesso comportamento che se lo fosse
                self.ship_hit()
                break
    
    def update_bullets(self):
        """aggiorna lo stato dei proiettili"""
        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
                    
        #Gestisco le collisioni
        self.detect_bullet_alien_collisions()
        
        #Rimuovo gli sprites che sono fuori dallo schermo
        self.clear_junk()

        
    def update_aliens(self):
        """Aggiorna lo stato della flotta di alieni"""
        
        for alien in self.aliens.sprites():
            if alien.check_edges():
                for alien in self.aliens.sprites():
                    alien.rect.y += self.settings.fleet_drop_speed
                alien.settings.fleet_direction *= -1
                break
        self.aliens.update()
        
        self.detect_alien_ship_collision()
        self.detect_alien_bottom_screen()
                
    def update_screen(self):
        """Aggiorna lo schermo generale"""
        
        #In questa parte si aggiorna lo sfondo in modo che le cose che disegno sparicano nelle loro "vecchie posizioni"
        self.screen.fill(self.settings.bg_color)
        #Disegno la navetta nella nuova posizione
        self.ship.blitme()
        #Disegno i proiettili nelle nuove posizioni
        self.update_bullets()
        #Disegno la flotta di alieni nelle nuove posizioni
        self.aliens.draw(self.screen)
        
        self.score.draw_score()
        
        if not self.game_stats.game_active:
            self.start_button.draw_button()

        #Rimuovo la roba dallo schermo
        self.clear_junk()
        
        #Mostro il display aggiornato
        pygame.display.flip()
    
    def run_game(self):
        """Avvia il main loop del gioco"""
        
        while True:
            #Controllo se ci sono eventi di mouse o tastiera
            self.check_events()
            
            if self.game_stats.game_active:
                #Cambia la posizione della nave in base alla situazione dei tasti
                self.ship.update()
                #Cambia la posizione dei proiettili in base al tempo
                self.bullets.update()
                #Cambia la posizione degli alieni in base al tempo
                self.update_aliens()
                
            #Aggiorno effettivamente le cose disegnate a schermo
            self.update_screen()
    
if __name__ == "__main__":
    """Crea un'istanza ed avvia il gioco"""
    
    game = AlienInvasion()
    game.run_game()