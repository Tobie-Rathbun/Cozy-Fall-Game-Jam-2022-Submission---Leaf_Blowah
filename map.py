import pygame
import sys, os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

img_dir = resource_path("img")


class Map:
    def __init__(self, game):
        self.game = game
        self.map_list = self.get_map()
        self.map_pos = 0, 0

    def get_map(self):
        self.map_tiles = []
        for tile in range(4):
            self.tile = pygame.image.load(os.path.join(img_dir, "Path0{}.png".format(tile)))
            self.map_tiles.append(self.tile)

        #print(self.map_tiles)  #debug
        return self.map_tiles

    def move_map(self): # , speed_x
        pass


    def update(self):
        self.move_map()
        pass



