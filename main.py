# imports
import pygame
import sys
from colors import *
from settings import *
from map import *
from player import *
from enemy import *

#game constructor class
class Game:
    def __init__(self):         #standard initialization, runs on creation of instance of class
        pygame.init()
        # window info
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(APP_ICON)
        self.screen = pygame.display.set_mode(RES, pygame.RESIZABLE)
        # fonts
        self.basicFont = pygame.font.SysFont(None, 48)
        self.largeFont = pygame.font.SysFont(None, 76)
        # 
        self.clock = pygame.time.Clock()
        self.delta_time = 1
        self.new_game()
        self.scaled = False
        self.fullscreen = False
        self.current_currency = 0
        self.bee_death = "a bee"
        self.gravity_death = "gravity"


    def pre_game(self):         #pre game main menu for starting game and selecting options
        self.game_running = False
        #self.new_game()
        self.basicFont = pygame.font.SysFont(None, 48)
        self.text = self.basicFont.render("WASD to move leaf, space to launch!", True, WHITE)
        self.text2 = self.basicFont.render("Get as far as you can!", True, WHITE)
        self.text3 = self.basicFont.render("Press ENTER to play!", True, WHITE)
       
        self.pregame = True
        while self.pregame:
            self.screen.fill(DARK_PURPLE)
            self.textRect, self.textRect2, self.textRect3 = self.text.get_rect(), self.text2.get_rect(), self.text3.get_rect()
            self.textRect.centerx, self.textRect2.centerx, self.textRect3.centerx = self.screen.get_rect().centerx, self.screen.get_rect().centerx, self.screen.get_rect().centerx
            self.textRect.centery, self.textRect2.centery, self.textRect3.centery = self.screen.get_rect().centery / 3, self.screen.get_rect().centery / 2, self.screen.get_rect().centery / 1.5 
            self.screen.blit(self.text,self.textRect)
            self.screen.blit(self.text2,self.textRect2)
            self.screen.blit(self.text3,self.textRect3)
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                    self.fullscreen = not self.fullscreen
                    if self.fullscreen:
                        self.screen = pygame.display.set_mode(FS_RES, pygame.FULLSCREEN)
                    else:
                        self.screen = pygame.display.set_mode(RES, pygame.RESIZABLE)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    self.new_game()
                    self.run()
            pygame.display.flip()





    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.enemy = Enemy(self)

    def get_res(self):
        self.res = (self.screen.get_width(), self.screen.get_height())
        return self.res

    def draw(self):
        self.screen.fill(DARK_GREEN)
        self.map.draw()
        self.player.draw()
        self.enemy.draw()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                    self.fullscreen = not self.fullscreen
                    if self.fullscreen:
                        self.screen = pygame.display.set_mode(FS_RES, pygame.FULLSCREEN)
                    else:
                        self.screen = pygame.display.set_mode(RES, pygame.RESIZABLE)
            elif event.type == pygame.KEYDOWN and (event.key == pygame.K_p or event.key == pygame.K_PAUSE):
                self.pause_game()

    def check_collisions(self):
        self.p_rect = self.player.get_rect()
        self.e_rect = self.enemy.get_rect()
        if self.p_rect.colliderect(self.e_rect):
            self.post_game(self.bee_death)

    def update(self):
        self.player.update()
        self.player_speed_x = self.player.get_movement()
        self.enemy.update()
        self.check_collisions()
        self.map.update(self.player_speed_x)
        pygame.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pygame.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def run(self):
        self.game_running = True
        while self.game_running:
            self.check_events()
            self.update()
            self.draw()

    



    def post_game(self, reason):
        self.game_running = False
        self.screen.fill(DARK_RED)

        self.current_score = int(self.player.get_score())
        self.scores_this_session = []
        self.scores_this_session.append(self.current_score)

        self.current_currency += self.current_score
        print('currency: ', self.current_currency)

        self.text = self.basicFont.render("Your score was {} before {} killed you".format(str(self.current_score), str(reason)), True, WHITE)
        self.text2 = self.basicFont.render("Your money is: {}".format(str(self.current_currency)), True, WHITE)
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

    def pause_game(self):
        self.game_running = not self.game_running
        if self.game_running == False:
            self.text = self.basicFont.render("PAUSED", True, WHITE)
            self.text2 = self.basicFont.render("Press P to Unpause", True, WHITE)
            self.textRect, self.textRect2 = self.text.get_rect(), self.text2.get_rect()
            self.textRect.centerx, self.textRect2.centerx = self.screen.get_rect().centerx, self.screen.get_rect().centerx
            self.textRect.centery, self.textRect2.centery = self.screen.get_rect().centery / 3, self.screen.get_rect().centery / 2
            self.pausegame = True
            while self.pausegame:
                self.screen.blit(self.text, self.textRect)
                self.screen.blit(self.text2, self.textRect2)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                        self.pause_game()
                pygame.display.flip()
        else:
            self.run()




if __name__ == '__main__':
    game = Game()
    game.pre_game()