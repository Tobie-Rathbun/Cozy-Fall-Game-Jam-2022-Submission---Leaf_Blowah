from colors import *
from settings import *
import pygame as pygame
import math

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.speed = PLAYER_SPEED
        self.gravity = GRAVITY
        self.speed_x, self.speed_y = 0, 0
        self.end_game_counter = 0

    def movement(self):
        self.speed_y += self.gravity
        self.x += self.speed_x
        

        if self.y < BASELINE:
            self.y += self.speed_y
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                #move up
                self.speed_y -= PLAYER_SPEED
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
        else:
            self.speed_x = self.speed_x * .99
            self.end_game_counter += 0.1
            if self.end_game_counter > 100:
                self.game.post_game()
        
    def get_movement(self):
        return(self.speed_x)

    def draw(self):
        pygame.draw.circle(self.game.screen, ORANGE, (self.x * 100, self.y * 100), 15)

    def update(self):
        self.movement()
