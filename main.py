# imports
import pygame
import sys
from colors import *
from settings import *
from map import *
from player import *

#game constructor class
class Game:
    def __init__(self):         #standard initialization, runs on creation of instance of class
        pygame.init()
        # window info
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(APP_ICON)
        self.screen = pygame.display.set_mode(RES)
        # fonts
        basicFont = pygame.font.SysFont(None, 48)
        largeFont = pygame.font.SysFont(None, 76)
        # 
        self.clock = pygame.time.Clock()
        self.delta_time = 1
        self.new_game()



    def pre_game(self):         #pre game main menu for starting game and selecting options
        self.game_running = False
        #self.new_game()
        self.basicFont = pygame.font.SysFont(None, 48)
        self.screen.fill(DARK_PURPLE)
        self.text = self.basicFont.render("WASD to move leaf, space to launch!", True, WHITE)
        self.text2 = self.basicFont.render("Get as far as you can!", True, WHITE)
        self.text3 = self.basicFont.render("Press ENTER to play!", True, WHITE)
        self.textRect, self.textRect2, self.textRect3 = self.text.get_rect(), self.text2.get_rect(), self.text3.get_rect()
        self.textRect.centerx, self.textRect2.centerx, self.textRect3.centerx = self.screen.get_rect().centerx, self.screen.get_rect().centerx, self.screen.get_rect().centerx
        self.textRect.centery, self.textRect2.centery, self.textRect3.centery = self.screen.get_rect().centery / 3, self.screen.get_rect().centery / 2, self.screen.get_rect().centery / 1.5 
        self.pregame = True
        while self.pregame:
            self.screen.blit(self.text,self.textRect)
            self.screen.blit(self.text2,self.textRect2)
            self.screen.blit(self.text3,self.textRect3)
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    self.run()
            pygame.display.flip()



    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)

    def update(self):
        self.player.update()
        self.map.update()
        pygame.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pygame.display.set_caption(f'{self.clock.get_fps() :.1f}')
        self.player_speed_x = self.player.get_movement()
        self.map.move_map(self.player_speed_x)

    def draw(self):
        self.screen.fill(DARK_GREEN)
        self.map.draw()
        self.player.draw()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

    def run(self):
        self.game_running = True
        while self.game_running:
            self.check_events()
            self.update()
            self.draw()

    

    def post_game(self):
        self.game_running = False
        self.screen.fill(DARK_RED)
        self.text = self.basicFont.render("Your score was:", True, WHITE)
        self.text2 = self.basicFont.render("Number of Score Goes Here", True, WHITE)
        self.text3 = self.basicFont.render("Press SPACE to play again!", True, WHITE)
        self.textRect, self.textRect2, self.textRect3 = self.text.get_rect(), self.text2.get_rect(), self.text3.get_rect()
        self.textRect.centerx, self.textRect2.centerx, self.textRect3.centerx = self.screen.get_rect().centerx, self.screen.get_rect().centerx, self.screen.get_rect().centerx
        self.textRect.centery, self.textRect2.centery, self.textRect3.centery = self.screen.get_rect().centery / 3, self.screen.get_rect().centery / 2, self.screen.get_rect().centery / 1.5 
        self.pregame = True
        while self.pregame:
            self.screen.blit(self.text,self.textRect)
            self.screen.blit(self.text2,self.textRect2)
            self.screen.blit(self.text3,self.textRect3)
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.pre_game()
            pygame.display.flip()



if __name__ == '__main__':
    game = Game()
    game.pre_game()