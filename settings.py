import math
import pygame
# /// Settings for the Game ///

#game title
TITLE = "Leaf Blowah"
#load the game window icon
APP_ICON = pygame.image.load("img/Fall_Leaf.png")

#screen variables
RES = WIDTH, HEIGHT = 1600, 900
FPS = 0

PLAYER_POS = 1.5, 5
PLAYER_SPEED = 0.00004
GRAVITY = .0000098
LAUNCH_SPEED = 0.001
LAUNCH_HEIGHT = 0.0005

BASELINE = HEIGHT * 7 / 8 / 100
PLAYERLINE = WIDTH / 8

# practice change