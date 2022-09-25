import pygame
import sys, os
from collections import deque

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

map_dir = resource_path("img/map")


class Map:
    def __init__(self, game):
        self.game = game
        self.res_w, self.res_h = self.res = self.game.get_res()
        self.map_list = self.get_map()
        self.map_pos_x, self.map_pos_y = 0, 0
        self.speed_x = 0
        

    def get_map(self):
        self.map_tiles = deque()
        for tile in range(4):
            self.tile = pygame.image.load(os.path.join(map_dir, "Path0{}.png".format(tile)))
            self.tile = pygame.transform.scale(self.tile, self.res)
            self.map_tiles.append(self.tile)

        #print(self.map_tiles)  #debug
        return self.map_tiles

    def get_map_tiles(self):
        pass

    def move_map(self, speed_x): # , speed_x
        self.speed_x = speed_x
        self.map_pos_x -= int(self.speed_x * 500)
        
        pass


    def update(self, player_x):
        self.move_map(player_x)
        self.res_w, self.res_h = self.res = self.game.get_res()
        if self.map_pos_x < -self.res_w*4: #4 tiles have passed screen
            self.map_pos_x = 0
            print("reset run")
        if self.map_pos_x < -self.res_w: #1 tile has passed screen
            self.piece_A_cor = (self.map_pos_x + self.res_w*4, self.map_pos_y)
            print("tile has been passed")
        else:
            self.piece_A_cor = (self.map_pos_x, self.map_pos_y)
            print("standard")
        
        
        self.piece_B_cor = (self.map_pos_x + self.res_w, self.map_pos_y)
        self.piece_C_cor = (self.map_pos_x + self.res_w*2, self.map_pos_y)
        self.piece_D_cor = (self.map_pos_x + self.res_w*3, self.map_pos_y)
        pass


    def draw(self):
        self.game.screen.blit(self.map_list[0], self.piece_A_cor)
        self.game.screen.blit(self.map_list[1], self.piece_B_cor)
        self.game.screen.blit(self.map_list[2], self.piece_C_cor)
        self.game.screen.blit(self.map_list[3], self.piece_D_cor)

