""" This module manage the creation of the object, their position on the map and their capability to be pick up by Macgiver """

#coding:utf-8
import pygame as pg
from maze import *
import random
from settings import *

pg.init()

class Object:
    """ Definition and initialization of the objects """
    def __init__(self, my_map): 
        self.x = 0
        self.y = 0
        self.case_x = 0
        self.case_y = 0
        self.my_map = my_map
        self.object_position = []
        self.object_position_list = []
        self.object_collected = False
        
     
    def set_objet_position(self):       
        """ Definition of a valid position for an object on the map """
        launched = True
        while launched:
            self.x = random.randint(0, SPRITE_SIDE_NUMBER-1)
            self.y = random.randint(0, SPRITE_SIDE_NUMBER-1)
            self.object_position = [self.x, self.y]

            if (self.my_map[self.y][self.x] != WALL_CHAR) and (self.my_map[self.y][self.x] != START_CHAR) and (self.my_map[self.y][self.x] != GOAL_CHAR):
                if self.object_position not in self.object_position_list:
                    self.case_y = self.y * SPRITE_SIZE
                    self.case_x = self.x * SPRITE_SIZE
                    self.object_position_list.append(self.object_position)
                    launched = False

    def pick_up_object(self):       
        """ Pick up an object by moving it out of the maze """
        self.case_y = 0
        self.case_x = 1 * SPRITE_SIZE
        self.object_collected = True