import pygame

class Scoreboard:
    """Classe che riporta dei risultati"""
    
    def __init__(self, game):
        """Inizializza gli attributi"""
        
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings
        self.game_stats = game.game_stats
        
        #Font della scoreboard
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        
        #Immagine iniziale dello score
        self.prep_score_image()
        
    def prep_score_image(self):
        """Inizializza l'immagine dello score"""
        score_str = str(self.game_stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        
        #Imposto dove disegnerò la mia scoreboard
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = self.screen_rect.left
        self.score_rect.top = 0
    
    def draw_score(self):
        """Disegno effettivamente il mio score"""
        self.screen.blit(self.score_image, self.score_rect)