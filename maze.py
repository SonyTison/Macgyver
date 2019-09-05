""" This module manages the creation, loading and printing of the map for the Game """

#coding:utf-8
import  pygame as pg
from macgyver import *
from settings import *

pg.init() 

class Map:
    """ Definition and initialization of the map """
    def __init__(self, filename):
        self.filename = filename
        self.my_map = []
    

    def load_file(self):
        """ Load map from text """
        with open(self.filename) as file:
            for line in file:
                map_line = []
                for char in line:
                    if char != '\n':
                        map_line.append(char)
                self.my_map.append(map_line)


    def print_map(self): 
        """ Print map with pygame """
        x = 0
        y = 0
        for line in self.my_map:
            x = 0
            for char in line:
                if char == PATH_CHAR:
                    window_surface.blit(FLOOR_CHART, [x, y])
                if char == WALL_CHAR:
                    window_surface.blit(WALL_CHART, [x, y])
                if char == START_CHAR or char == GOAL_CHAR:
                    window_surface.blit(START_CHART, [x, y])
                if x == SPRITE_SIZE * (SPRITE_SIDE_NUMBER -1):
                    y = y + SPRITE_SIZE
                x = x + SPRITE_SIZE