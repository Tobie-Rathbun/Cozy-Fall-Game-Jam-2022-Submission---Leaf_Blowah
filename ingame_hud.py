import pygame
from settings import *
from colors import *

class HUD:
    def __init__(self, game):
        self.game = game
        self.screen_w, self.screen_h = self.game.get_res()
        self.basicFont = self.game.basicFont
        pass

    def update(self):
        self.display_caption = int(self.game.player.speed_x * 100)
        self.label_text = 'Moving {} Speed'.format(self.display_caption)
        self.label_rect = pygame.Rect(self.screen_w/2, self.screen_h/2, 400, 40)
        self.label_surface = self.basicFont.render(self.label_text, True, FALL_YELLOW)
        self.label_rect.w = self.label_surface.get_width()+10
        
        pass

    def draw(self):
        pygame.draw.rect(self.game.screen, DARK_PURPLE, self.label_rect)
        self.game.screen.blit(self.label_surface, (self.label_rect.x +5, self.label_rect.y +5))
        pass