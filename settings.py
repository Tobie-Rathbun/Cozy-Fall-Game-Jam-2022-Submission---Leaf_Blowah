import math
import pygame
import sys, os
# /// Settings for the Game ///

# /// Method to Load Folders ///
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
# Folders are stored in varibales
icon_dir = resource_path("img/icon")

#game title
TITLE = "Leaf Blowah"
#load the game window icon
APP_ICON = pygame.image.load(os.path.join(icon_dir, "Fall_Leaf.png"))  #loads image from folder

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

#example change
#change in map art branch