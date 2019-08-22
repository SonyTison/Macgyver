#coding:utf-8

import pygame as pg

pg.init()

""" WINDOW PARAMETER """

SPRITE_SIDE_NUMBER = 15
SPRITE_SIZE = 40
WINDOW_SIDE = SPRITE_SIDE_NUMBER * SPRITE_SIZE

pg.display.set_caption("Mac Giver") 

window_surface = pg.display.set_mode((WINDOW_SIDE, WINDOW_SIDE)) 

""" WINDOW of WINNER """







""" WINDOW of LOOSER """





""" SPRITES """

FLOOR_CHART = pg.image.load("./resources/floor.png").convert()
WALL_CHART = pg.image.load("./resources/wall.png").convert()
START_CHART = pg.image.load("./resources/start_finished.png").convert()
GOAL_CHART = pg.image.load("./resources/start_finished.png").convert()
MACGYVER_CHART = pg.image.load("./resources/macgyver.png").convert_alpha()
GARDIAN_CHART = pg.image.load("./resources/gardian.png").convert_alpha()
SYRINGE_NEEDLE_CHART = pg.image.load("./resources/syringe_needle.png").convert()
ETHER_CHART = pg.image.load("./resources/ether.png").convert_alpha()
SYRINGE_CHART = pg.image.load("./resources/syringe.png").convert()
PLASTIC_TUBE_CHART = pg.image.load("./resources/plastic_tube.png").convert()


""" MAP STRUCTURE """

START_CHAR = 'S'
GOAL_CHAR = 'G'
PATH_CHAR = '.'
WALL_CHAR = '#'