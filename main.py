# imports
import pygame
import sys
from colors import *
from settings import *
from map import *
from player import *
from enemies import *
from boosts import *
from ingame_hud import *



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

        self.prev_highest = 0


    def pre_game(self):         #pre game main menu for starting game and selecting options
        self.game_running = False
        #self.new_game()
        self.basicFont = pygame.font.SysFont(None, 48)
        self.text = self.basicFont.render("WASD to move leaf, space to launch!", True, WHITE)
        self.text2 = self.basicFont.render("Get as far as you can!", True, WHITE)
        self.text3 = self.basicFont.render("Press ENTER to play!", True, WHITE)
        self.text4 = self.basicFont.render("Your highest score was: {}".format(self.prev_highest), True, WHITE)
        self.pregame = True
        while self.pregame:
            self.screen.fill(DARK_RED)
            self.textRect, self.textRect2, self.textRect3, self.textRect4 = self.text.get_rect(), self.text2.get_rect(), self.text3.get_rect(), self.text4.get_rect()
            self.textRect.centerx, self.textRect2.centerx, self.textRect3.centerx, self.textRect4.centerx = self.screen.get_rect().centerx, self.screen.get_rect().centerx, self.screen.get_rect().centerx, self.screen.get_rect().centerx
            self.textRect.centery, self.textRect2.centery, self.textRect3.centery, self.textRect4.centery = self.screen.get_rect().centery / 3, self.screen.get_rect().centery / 2, self.screen.get_rect().centery / 1.5, self.screen.get_rect().centery
            # self.textRect.inflate_ip(200, 50)
            # self.textRect2.inflate_ip(200, 50)
            # self.textRect3.inflate_ip(200, 50)
            # self.textRect4.inflate_ip(200, 50)
            pygame.draw.rect(self.screen, ORANGE, self.textRect)
            pygame.draw.rect(self.screen, ORANGE, self.textRect2)
            pygame.draw.rect(self.screen, FALL_YELLOW, self.textRect3)
            pygame.draw.rect(self.screen, AUBURN_RED, self.textRect4)
            self.screen.blit(self.text,self.textRect)
            self.screen.blit(self.text2,self.textRect2)
            self.screen.blit(self.text3,self.textRect3)
            self.screen.blit(self.text4,self.textRect4)
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
                    self.pregame = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                    self.store_menu()
                    self.pregame = False
            pygame.display.flip()





    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.enemy = Enemy(self)
        self.boost = Boost(self)
        self.ingame_hud = HUD(self)

    def get_res(self):
        self.res = self.screen_w, self.screen_h = (self.screen.get_width(), self.screen.get_height())
        return self.res

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.pre_game()
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
        if self.e_rect.x < self.screen_w and self.e_rect.y > self.screen_h:
            self.enemy.new_enemy()

    def check_boosts(self):
        self.p_rect = self.player.get_rect()
        self.b_rect = self.boost.get_rect()
        if self.p_rect.colliderect(self.b_rect):
            self.player.launch()
            self.boost.new_boost()
        if self.b_rect.x < self.screen_w and self.b_rect.y > self.screen_h:
            self.boost.new_boost()
            

    def update(self):
        self.player.update()
        self.player_speed_x = self.player.get_movement()
        self.enemy.update()
        self.boost.update()
        self.check_collisions()
        self.check_boosts()
        self.ingame_hud.update()
        self.map.update(self.player_speed_x)
        pygame.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pygame.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        self.screen.fill(ORANGE)
        self.map.draw()
        self.player.draw()
        self.enemy.draw()
        self.boost.draw()
        self.ingame_hud.draw()

    def run(self):
        self.game_running = True
        while self.game_running:
            self.check_events()
            self.update()
            self.draw()

    



    def store_menu(self):
        self.store = True
        
        self.text2 = self.basicFont.render("Aerodynamics: 30", True, WHITE)
        self.text3 = self.basicFont.render("Wind Booster: 50", True, WHITE)
        while self.store:
            self.screen.fill(DARK_RED)
            self.text = self.basicFont.render("Your money is: {}".format(str(self.current_currency)), True, WHITE)
            self.textRect, self.textRect2, self.textRect3 = self.text.get_rect(), self.text2.get_rect(), self.text3.get_rect()
            self.textRect.centerx, self.textRect2.centerx, self.textRect3.centerx = self.screen.get_rect().centerx, self.screen.get_rect().centerx, self.screen.get_rect().centerx
            self.textRect.centery, self.textRect2.centery, self.textRect3.centery = self.screen.get_rect().centery / 3, self.screen.get_rect().centery / 2, self.screen.get_rect().centery / 1.5 
            pygame.draw.rect(self.screen, ORANGE, self.textRect)
            pygame.draw.rect(self.screen, FALL_YELLOW, self.textRect2)
            pygame.draw.rect(self.screen, FALL_YELLOW, self.textRect3)
            self.screen.blit(self.text,self.textRect)
            self.screen.blit(self.text2,self.textRect2)
            self.screen.blit(self.text3,self.textRect3)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.pre_game()
                    self.store = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                    self.fullscreen = not self.fullscreen
                    if self.fullscreen:
                        self.screen = pygame.display.set_mode(FS_RES, pygame.FULLSCREEN)
                    else:
                        self.screen = pygame.display.set_mode(RES, pygame.RESIZABLE)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                    self.pre_game()
                    self.store = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.textRect2.collidepoint(event.pos):
                        if self.current_currency > 30:  #cost
                            self.player.upgrade()
                            self.current_currency -= 30
                    if self.textRect3.collidepoint(event.pos):
                        if self.current_currency > 50:
                            self.boost.upgrade()
                            self.current_currency -= 50
                    
            pygame.display.flip()





    def post_game(self, reason):
        self.game_running = False
        self.screen.fill(AUBURN_RED)

        self.current_score = int(self.player.get_score())
        self.scores_this_session = []
        self.scores_this_session.append(self.current_score)

        self.current_currency += self.current_score
        print('currency: ', self.current_currency)
        if self.current_score > self.prev_highest:
            self.prev_highest = self.current_score

        self.text = self.basicFont.render("Your score was {} before {} killed you".format(str(self.current_score), str(reason)), True, WHITE)
        self.text2 = self.basicFont.render("Your money is: {}".format(str(self.current_currency)), True, WHITE)
        self.text3 = self.basicFont.render("Press SPACE to play again or E to Shop!", True, WHITE)
        self.textRect, self.textRect2, self.textRect3 = self.text.get_rect(), self.text2.get_rect(), self.text3.get_rect()
        self.textRect.centerx, self.textRect2.centerx, self.textRect3.centerx = self.screen.get_rect().centerx, self.screen.get_rect().centerx, self.screen.get_rect().centerx
        self.textRect.centery, self.textRect2.centery, self.textRect3.centery = self.screen.get_rect().centery / 3, self.screen.get_rect().centery / 2, self.screen.get_rect().centery / 1.5 
        self.postgame = True
        
        while self.postgame:
            pygame.draw.rect(self.screen, ORANGE, self.textRect)
            pygame.draw.rect(self.screen, ORANGE, self.textRect2)
            pygame.draw.rect(self.screen, FALL_YELLOW, self.textRect3)
            self.screen.blit(self.text,self.textRect)
            self.screen.blit(self.text2,self.textRect2)
            self.screen.blit(self.text3,self.textRect3)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.pre_game()
                    self.post_game = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.new_game()
                    self.run()
                    self.post_game = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                    self.fullscreen = not self.fullscreen
                    if self.fullscreen:
                        self.screen = pygame.display.set_mode(FS_RES, pygame.FULLSCREEN)
                    else:
                        self.screen = pygame.display.set_mode(RES, pygame.RESIZABLE)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                    self.store_menu()
                    self.post_game = False
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
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                        self.fullscreen = not self.fullscreen
                        if self.fullscreen:
                            self.screen = pygame.display.set_mode(FS_RES, pygame.FULLSCREEN)
                        else:
                            self.screen = pygame.display.set_mode(RES, pygame.RESIZABLE)
                pygame.display.flip()
        else:
            self.run()




if __name__ == '__main__':
    game = Game()
    game.pre_game()