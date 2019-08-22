#coding:utf-8
import pygame as pg
from maze import *
import random
from settings import *

pg.init()

class Object:

    """ Definition of an Object to pick up in the game. """
  
    
    def __init__(self, my_map): 
        self.x = 0
        self.y = 0
        self.case_x = 0
        self.case_y = 0
        self.my_map = my_map
	self.number_of_object_collected = 0
        self.object_position_list = []

      
        
    def set_objet_position(self):
        
        """ Define a valid position for an object on the map. """
        
        launched = True
        while launched:
            self.x = random.randint(0, SPRITE_SIDE_NUMBER-1)
            self.y = random.randint(0, SPRITE_SIDE_NUMBER-1)
            
            if (self.my_map[self.y][self.x] != WALL_CHAR) and (self.my_map[self.y][self.x] != START_CHAR) and (self.my_map[self.y][self.x] != GOAL_CHAR):
                if self.my_map[self.y][self.x] not in self.object_position_list:
                    self.case_y = self.y * SPRITE_SIZE
                    self.case_x = self.x * SPRITE_SIZE
                    launched = False
	self.object_position_list.append([self.y, self.x])

                

    def pick_up_object(self):
        
        """ Pick up object 1 by moving it out of the maze."""
        
        self.case_y = 0
        self.case_x = number_of_object * SPRITE_SIZE
        self.number_of_object_collected += 1