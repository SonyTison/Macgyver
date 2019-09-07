""" This module manages all the constants used in the Game """

#coding:utf-8
import pygame as pg
pg.init()

""" WINDOW PARAMETERS """

SPRITE_SIDE_NUMBER = 15
SPRITE_SIZE = 40
WINDOW_SIDE = SPRITE_SIDE_NUMBER * SPRITE_SIZE


window_surface = pg.display.set_mode((WINDOW_SIDE, WINDOW_SIDE))
icone = pg.image.load("./resources/icon.png")
pg.display.set_icon(icone)
pg.display.set_caption("MacGyver")


""" WELCOME_SCREEN """

WELCOME_SCREEN = pg.image.load("./resources/welcome_pic.png")


""" WINNER_SCREEN """

WINNER_SCREEN = pg.image.load("./resources/win_pic.png")


""" LOSER_SCREEN """

LOSER_SCREEN = pg.image.load("./resources/lose_pic.png")


""" SPRITES """

FLOOR_CHART = pg.image.load("./resources/floor.png").convert()
WALL_CHART = pg.image.load("./resources/wall.png").convert()
START_CHART = pg.image.load("./resources/start_finished.png").convert()
GOAL_CHART = pg.image.load("./resources/start_finished.png").convert()
MACGYVER_CHART = pg.image.load("./resources/macgyver.png").convert_alpha()
GUARDIAN_CHART = pg.image.load("./resources/guardian.png").convert_alpha()
SYRINGE_NEEDLE_CHART = pg.image.load("./resources/syringe_needle.png").convert()
ETHER_CHART = pg.image.load("./resources/ether.png").convert()
SYRINGE_CHART = pg.image.load("./resources/syringe.png").convert()
PLASTIC_TUBE_CHART = pg.image.load("./resources/plastic_tube.png").convert()


""" MAP STRUCTURE """

START_CHAR = 'S'
GOAL_CHAR = 'G'
PATH_CHAR = '.'
WALL_CHAR = '#'