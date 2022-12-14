from colors import *
from settings import *
import random
import pygame as pygame
from collections import deque

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

wind_dir = resource_path("img/wind")

class Boost:
    def __init__(self, game):
        self.game = game
        self.screen_w, self.screen_h = self.game.get_res()
        self.x, self.y = self.screen_w, random.randrange(0, int(self.screen_h/2))
        self.gravity = GRAVITY
        self.boost_speed = BOOST_SPEED
        self.speed_x, self.speed_y = -self.boost_speed, 0
        self.wind_list = self.get_art()
        self.anim_timer = 0
        self.in_air = 1

    def movement(self):
        self.speed_y += self.gravity
        self.y += self.speed_y
        self.x += self.speed_x
        
    def get_art(self):
        self.wind_tiles = deque()
        for tile in range(4):
            self.tile = pygame.image.load(os.path.join(wind_dir, "wind-0{}.png".format(tile)))
            pygame.transform.scale(self.tile, (int(self.screen_w/16), int(self.screen_w/16)))
            self.wind_tiles.append(self.tile)

        return self.wind_tiles

    def get_movement(self):
        return(self.speed_x)

    def get_rect(self):
        return(self.wind_rect)

    def new_boost(self):
        self.speed_x, self.speed_y = -self.boost_speed, 0
        self.x, self.y = self.screen_w, random.randrange(0, int(self.screen_h/2))
        
    def upgrade(self):
        self.boost_speed = int(self.boost_speed * 1.2)
        print("upgraded boosts")

    def update(self):
        self.screen_w, self.screen_h = self.game.get_res()

        self.movement()

        self.anim_timer += 1
        if self.in_air == 1:
            if self.anim_timer > 10:      #controls animation speed
                self.wind_list.rotate(-1)   #animates next frame of wind
                self.anim_timer = 0

        self.screen_w, self.screen_h = self.game.get_res()
        self.wind_draw = self.wind_list[0]
        self.wind_rect = self.wind_draw.get_rect()
        self.wind_rect.x, self.wind_rect.y = self.x, self.y
        
    def draw(self):
        self.game.screen.blit(self.wind_draw, (self.wind_rect.x, self.wind_rect.y))