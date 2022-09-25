from colors import *
from settings import *
import pygame as pygame
from collections import deque

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

leaf_dir = resource_path("img/leaf")

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.speed = PLAYER_SPEED
        self.gravity = GRAVITY
        self.speed_x, self.speed_y = 0, 0
        self.end_game_counter = 0
        self.leaf_list = self.get_art()
        self.anim_timer = 0
        self.in_air = 1

    def movement(self):
        self.speed_y += self.gravity
        self.x += self.speed_x
        

        if self.y < BASELINE:       #if touching ground
            self.y += self.speed_y
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                #move up
                self.speed_y -= PLAYER_SPEED/4
            if keys[pygame.K_s]:
                #move down
                self.speed_y += PLAYER_SPEED
            if keys[pygame.K_a]:
                #move left
                self.speed_x -= PLAYER_SPEED
            if keys[pygame.K_d]:
                #move right
                self.speed_x += PLAYER_SPEED
            if keys[pygame.K_SPACE]:
                #launch / boost
                self.speed_x += LAUNCH_SPEED
                self.speed_y -= LAUNCH_HEIGHT
            if keys[pygame.K_5]:
                print("I pressed K5")
            if keys[pygame.K_4]:
                #presses 4 mutes audio
                pass

        else:
            self.speed_x = self.speed_x * .99
            self.end_game_counter += 1
            self.in_air = 0
            if self.end_game_counter > 10:
                self.game.post_game()
        
    def get_art(self):
        self.leaf_tiles = deque()
        for tile in range(4):
            self.tile = pygame.image.load(os.path.join(leaf_dir, "Leaf0{}.png".format(tile)))
            pygame.transform.scale(self.tile, (self.game.screen.get_width(), self.game.screen.get_height()))
            self.leaf_tiles.append(self.tile)

        return self.leaf_tiles

    def get_movement(self):
        return(self.speed_x)

    def draw(self):
        self.screen_w, self.leaf_h = self.game.get_res()
        self.leaf_draw = pygame.transform.scale(self.leaf_list[0], (int(self.screen_w/16), int(self.screen_w/16)))
        self.game.screen.blit(self.leaf_draw, (PLAYERLINE, self.y * 100))
        #pygame.draw.circle(self.game.screen, ORANGE, (self.x * 100, self.y * 100), 15)

    def get_score(self):
        return(self.x)

    def update(self):
        self.movement()
        self.anim_timer += 1
        if self.in_air == 1:
            if self.anim_timer > 10:      #controls animation speed
                self.leaf_list.rotate(-1)   #animates next frame of leaf
                self.anim_timer = 0
        