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
FS_RES = 1920, 1080 #this should probably get updated somehow
FPS = 60

PLAYER_POS = 1.5, 1.5
PLAYER_SPEED = 0.0005
GRAVITY = .01
LAUNCH_SPEED = 0.05
LAUNCH_HEIGHT = 0.5

ENEMY_SPEED = 5
BOOST_SPEED = 5
WIND_RESISTANCE = 0.00004

BASELINE = HEIGHT * 7 / 8
#print(BASELINE)     #debug
PLAYERLINE = WIDTH / 8

IDK = 420