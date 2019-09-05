""" This module manages the creation of the guardian and his position on the map """

#coding:utf-8
import pygame as pg
from maze import *
from settings import *

pg.init()

class Guardian:
    """ Definition and initialization of the guardian on the map """
    def __init__(self, x, y, my_map):
        self.x = x
        self.y = y
        self.case_x = x * SPRITE_SIZE
        self.case_y = y * SPRITE_SIZE
        self.my_map = my_map

    '''def print_guardian(self):
        """ Print guardian at goal position on the map. """
        window_surface.blit(GUARDIAN_CHART, [self.case_x, self.case_y])
        pg.display.flip()'''