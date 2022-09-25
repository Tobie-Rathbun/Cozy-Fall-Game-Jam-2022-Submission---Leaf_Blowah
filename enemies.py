from colors import *
from settings import *
import random
import pygame as pygame
from collections import deque

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

bee_dir = resource_path("img/bee")

class Enemy:
    def __init__(self, game):
        self.game = game
        self.screen_w, self.screen_h = self.game.get_res()
        self.x, self.y = self.screen_w, random.randrange(0, int(self.screen_h/2))
        self.gravity = GRAVITY
        self.speed_x, self.speed_y = -ENEMY_SPEED, 0
        self.bee_list = self.get_art()
        self.anim_timer = 0
        self.in_air = 1
        self.scale_counter = 0

    def movement(self):
        self.speed_y += self.gravity
        self.y += self.speed_y
        self.x += self.speed_x
        
    def get_art(self):
        self.bee_tiles = deque()
        for tile in range(4):
            self.tile = pygame.image.load(os.path.join(bee_dir, "Bee{}.png".format(tile)))
            pygame.transform.scale(self.tile, ((int(self.screen_w/16), int(self.screen_w/16))))
            self.bee_tiles.append(self.tile)

        return self.bee_tiles

    def get_movement(self):
        return(self.speed_x)

    def get_rect(self):
        #make self.bee_rect smaller here using pygame.transform.scale()
        return(self.bee_rect)

    def new_enemy(self):
        self.speed_x, self.speed_y = -ENEMY_SPEED, 0
        self.x, self.y = self.screen_w, random.randrange(0, int(self.screen_h/2))

    def update(self):
        self.screen_w, self.screen_h = self.game.get_res()

        self.movement()

        self.anim_timer += 1
        if self.in_air == 1:
            if self.anim_timer > 10:      #controls animation speed
                self.bee_list.rotate(-1)   #animates next frame of bee
                self.anim_timer = 0

        self.screen_w, self.bee_h = self.game.get_res()
        self.bee_draw = self.bee_list[0]
        self.bee_rect = self.bee_draw.get_rect()
        self.bee_rect.x, self.bee_rect.y = self.x, self.y
        if (self.scale_counter < 1):
            self.bee_rect.width = self.bee_rect.width * .1
            self.bee_rect.height = self.bee_rect.height * .1
            self.scale_counter += 1
        
    def draw(self):
<<<<<<< HEAD
        pygame.draw.rect(self.game.screen, RED, self.bee_rect)
        self.game.screen.blit(self.bee_draw, (self.bee_rect.x, self.bee_rect.y))
        print("Bee box ", self.bee_rect)
        
        #pygame.draw.circle(self.game.screen, ORANGE, (self.x * 100, self.y * 100), 15)
=======
        self.game.screen.blit(self.bee_draw, (self.bee_rect.x, self.bee_rect.y))
>>>>>>> 73a68ca80d0391a2eb36235da3f1aad5bd483f41
