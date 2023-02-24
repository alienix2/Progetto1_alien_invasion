import pygame

from pygame.sprite import Group

from ship import Ship

class Scoreboard:
    """Classe che riporta dei risultati"""
    
    def __init__(self, game):
        """Inizializza gli attributi"""
        
        self.game = game
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings
        self.game_stats = game.game_stats
        
        #Font della scoreboard
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        
        #Immagine iniziale dello score
        self.prep_score_image()
        self.prep_level_image()
        self.prep_highscore_image()
        self.prep_ships()
        
    def prep_score_image(self):
        """Inizializza l'immagine dello score"""
        
        score_str = str(self.game_stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        
        #Imposto dove disegnerò la mia scoreboard
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = self.screen_rect.left
        self.score_rect.top = 0
    
    def prep_highscore_image(self):
        """Inizializza l'immagine dello score"""
        
        highscore_str = f"Highscore: {self.game_stats.highscore}"
        self.highscore_image = self.font.render(highscore_str, True, self.text_color, self.settings.bg_color)
        
        #Imposto dove disegnerò la mia highscoreboard
        self.highscore_rect = self.highscore_image.get_rect()
        self.highscore_rect.left = self.screen_rect.left
        self.highscore_rect.top = 30
    
    def prep_level_image(self):
        """Inizializza l'immagine dello score"""
        
        level_str = f"Level: {self.game_stats.level}"
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)
        
        #Imposto dove disegnerò la mia scoreboard
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.screen_rect.left
        self.level_rect.top = 60
    
    def prep_ships(self):
        """Disegna le navicelle rimaste a schermo"""
        
        self.ships = Group()
        for ship_number in range(self.game_stats.ships_left + 1):
            ship = Ship(self.game)
            ship.rect.x = self.screen_rect.right - ship_number * ship.rect.width
            ship.rect.y = 0
            self.ships.add(ship)
    
    def set_highscore(self):
        """Se è stato battuto il record reimposta l'hishscore"""
        
        if self.game_stats.score > self.game_stats.highscore:
            self.game_stats.highscore = self.game_stats.score
            self.prep_highscore_image()
    
    def draw_score(self):
        """Disegno effettivamente tutta la mia scoreboard"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.highscore_image, self.highscore_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)