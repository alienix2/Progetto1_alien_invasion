class GameStats:
    """Classe che contiene le statistiche del gioco"""
    
    def __init__(self, game):
        """Inizializzo le statistiche"""
        self.game = game
        self.settings = self.game.settings
        self.game_active = True
        
        self.reset_stats()
        
    def reset_stats(self):
        self.ships_left = self.game.settings.ships_number_limit
        self.score = 0