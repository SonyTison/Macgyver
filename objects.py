#coding:utf-8
import pygame as pg
from maze import *
import random
from settings import *

pg.init()

class Object:
    
    def __init__(self, my_map): 
        self.x = 0
        self.y = 0
        self.case_x = 0
        self.case_y = 0
        self.my_map = my_map
        self.object_1_collected = False
        self.object_2_collected = False
        self.object_3_collected = False
        
     

    def set_objet_position(self):
        """ Set up  a valid position of an object on th map """
        launched = True
        while launched :
            self.x = random.randint(0, SPRITE_SIDE_NUMBER-1)
            self.y = random.randint(0, SPRITE_SIDE_NUMBER-1)
            
            if (self.my_map[self.y][self.x] != WALL_CHAR) and (self.my_map[self.y][self.x] != START_CHAR) and (self.my_map[self.y][self.x] != GOAL_CHAR):
                self.case_y = self.y * SPRITE_SIZE
                self.case_x = self.x * SPRITE_SIZE
                launched = False

    def pick_up_object_1(self):
        """ Pick up object number 1 by placing it out the maze """
        self.case_y = 0
        self.case_x = 0
        self.object_1_collected = True

    def pick_up_object_2(self):
        """ Pick uo object number 2 by placing it out the maze """
        self.case_y = 0 
        self.case_x = 1 * SPRITE_SIZE
        self.object_2_collected = True

    def pick_up_object_3(self):      
        """ Pick up object number 3 by placing it out the maze """
        self.case_y = 0
        self.case_x = 2 * SPRITE_SIZE
        self.object_3_collected = True