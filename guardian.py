# coding: utf-8

""" This module manages the creation of the guardian and his position on the map """

from settings import *

class Guardian:
    """ Definition and initialization of the guardian on the map """
    def __init__(self, x, y, my_map):
        self.x = x
        self.y = y
        self.case_x = x * SPRITE_SIZE
        self.case_y = y * SPRITE_SIZE
        self.my_map = my_map