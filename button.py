import pygame

class Button:
    """Classe che descrive un bottone"""
    
    def __init__(self, game, msg):
        """Inizializza il bottone"""
        
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        
        #Proprietà del bottone
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        
        #Rettangolo del bottone
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        #Preparo il messaggio del bottone
        self.prep_message(msg)
    
    def prep_message(self, msg):
        """Trasforma il testo in un'immagine e la stampa sul bottone"""
        
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self):
        """Disegna il bottone e lo rimepie con la scritta"""
        
        self.screen.fill(self.button_color, self.msg_image_rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)    