""" This module manages the creation of the main character, his position on the map and his ability to pick up an object """

#coding:utf-8
from pygame import *
from maze import *
from settings import *
pg.init()

class MacGyver:
    """ Definition and initialization of Macgyver on the map """
    def __init__(self, x, y, my_map): 
        self.x = x
        self.y = y
        self.case_x = x * SPRITE_SIZE
        self.case_y = y * SPRITE_SIZE
        self.my_map = my_map
        self.quit = False
        
    def event_management(self):
        """ Management of Macgyver's position on the map """
        for event in pg.event.get():
            
            if event.type == QUIT:
                self.quit = True

            if event.type == KEYDOWN and event.key == K_DOWN:
                if self.my_map[self.y+1][self.x] and self.my_map[self.y+1][self.x] != WALL_CHAR:
                    self.y = self.y +1
                    self.case_y = self.case_y + SPRITE_SIZE
                    
            if event.type == KEYDOWN and event.key == K_UP:
                if self.my_map[self.y-1][self.x] and self.my_map[self.y-1][self.x] != WALL_CHAR:
                    self.y = self.y -1
                    self.case_y = self.case_y - SPRITE_SIZE
                                   
            if event.type == KEYDOWN and event.key == K_RIGHT:
                if self.my_map[self.y][self.x+1] and self.my_map[self.y][self.x+1] != WALL_CHAR:
                    self.x = self.x +1
                    self.case_x = self.case_x + SPRITE_SIZE
                    
            if event.type == KEYDOWN and event.key == K_LEFT:
                if self.my_map[self.y][self.x-1] and self.my_map[self.y][self.x-1] != WALL_CHAR:
                    self.x = self.x -1
                    self.case_x = self.case_x - SPRITE_SIZE