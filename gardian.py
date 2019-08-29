""" This module manage the creation of the Gardian and, his position on the map """

#coding:utf-8
import pygame as pg
from maze import *
from settings import *

pg.init()

class Gardian:
    def __init__(self, x, y, my_map):
        self.x = x
        self.y = y
        self.case_x = x * SPRITE_SIZE
        self.case_y = y * SPRITE_SIZE
        self.my_map = my_map

    def print_Gardian(self):
        """ Print Gardian at goal position on the map. """
        window_surface.blit(GARDIAN_CHART, [self.case_x, self.case_y])
        pg.display.flip()