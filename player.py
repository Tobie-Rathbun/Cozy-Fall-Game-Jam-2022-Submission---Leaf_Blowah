from colors import *
from settings import *
import pygame as pg
import math

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.speed = PLAYER_SPEED
        self.gravity = GRAVITY
        self.speed_x, self.speed_y = 0, 0

    def movement(self):
        self.speed_y += self.gravity

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            #move up
            self.speed_y -= PLAYER_SPEED
        if keys[pg.K_s]:
            #move down
            self.speed_y += PLAYER_SPEED
        if keys[pg.K_a]:
            #move left
            self.speed_x -= PLAYER_SPEED
        if keys[pg.K_d]:
            #move right
            self.speed_x += PLAYER_SPEED
        if keys[pg.K_SPACE]:
            #launch / boost
            self.speed_x += LAUNCH_SPEED
            self.speed_y -= LAUNCH_HEIGHT

        self.x += self.speed_x
        

        if self.y < BASELINE:
            self.y += self.speed_y
        else:
            self.speed_x = self.speed_x * .99
        


    def draw(self):
        pg.draw.circle(self.game.screen, ORANGE, (self.x * 100, self.y * 100), 15)

    def update(self):
        self.movement()
