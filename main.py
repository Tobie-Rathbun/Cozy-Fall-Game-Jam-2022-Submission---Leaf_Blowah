# imports
import pygame as pg
import sys
from colors import *
from settings import *
from map import *
from player import *

#game constructor class
class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)

    def update(self):
        self.player.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        self.screen.fill('black')
        self.map.draw()
        self.player.draw()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

    def pre_game(self):
        self.game_running = False
        self.new_game()
        self.basicFont = pg.font.SysFont(None, 48)
        self.screen.fill(BLACK)
        self.text = self.basicFont.render("WSAD to walk, click to shoot!", True, WHITE)
        self.text2 = self.basicFont.render("Get to the mushroom to make it to the next round", True, WHITE)
        self.text3 = self.basicFont.render("Press ENTER to play!", True, WHITE)
        self.textRect, self.textRect2, self.textRect3 = self.text.get_rect(), self.text2.get_rect(), self.text3.get_rect()
        self.textRect.centerx, self.textRect2.centerx, self.textRect3.centerx = self.screen.get_rect().centerx, self.screen.get_rect().centerx, self.screen.get_rect().centerx
        self.textRect.centery, self.textRect2.centery, self.textRect3.centery = self.screen.get_rect().centery / 3, self.screen.get_rect().centery / 2, self.screen.get_rect().centery / 1.5 
        self.pregame = True
        while self.pregame:
            self.screen.blit(self.text,self.textRect)
            self.screen.blit(self.text2,self.textRect2)
            self.screen.blit(self.text3,self.textRect3)
            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    pg.quit()
                    sys.exit()
                elif event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
                    self.run()
            pg.display.flip()

    def post_game(self):
        self.game_running = False
        self.screen.fill(BLACK)
        self.text = self.basicFont.render("You made it to round: ", True, WHITE)
        self.text2 = self.basicFont.render("Number Goes Here", True, WHITE)
        self.text3 = self.basicFont.render("Press SPACE to play!", True, WHITE)
        self.textRect, self.textRect2, self.textRect3 = self.text.get_rect(), self.text2.get_rect(), self.text3.get_rect()
        self.textRect.centerx, self.textRect2.centerx, self.textRect3.centerx = self.screen.get_rect().centerx, self.screen.get_rect().centerx, self.screen.get_rect().centerx
        self.textRect.centery, self.textRect2.centery, self.textRect3.centery = self.screen.get_rect().centery / 3, self.screen.get_rect().centery / 2, self.screen.get_rect().centery / 1.5 
        self.pregame = True
        while self.pregame:
            self.screen.blit(self.text,self.textRect)
            self.screen.blit(self.text2,self.textRect2)
            self.screen.blit(self.text3,self.textRect3)
            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    pg.quit()
                    sys.exit()
                elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    self.pre_game()
            pg.display.flip()

if __name__ == '__main__':
    game = Game()
    game.pre_game()