class GameStats:
    """Classe che contiene le statistiche del gioco"""
    
    def __init__(self, game):
        """Inizializzo le statistiche"""
        self.game = game
        self.settings = self.game.settings
        self.game_active = True
        
        self.highscore = 0
        self.score = 0
        self.level = 1
        
        self.reset_stats()
        
    def reset_stats(self):
        """Imposta l'highscore e resetta le stats"""
        
        self.ships_left = self.game.settings.ships_number_limit
        self.score = 0
        self.level = 1