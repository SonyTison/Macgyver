#coding:utf-8
import pygame as pg
pg.init()

# window parameter

sprite_side_number = 15
SPRITE_SIDE_NUMBER = 15
sprite_size = 40
SPRITE_SIZE = 40
window_side = sprite_side_number * sprite_size
WINDOW_SIDE = SPRITE_SIDE_NUMBER * SPRITE_SIZE

pg.display.set_caption("Mac Giver") # modify the title of the window

window_surface = pg.display.set_mode((window_side, window_side)) # is an object - display a "board"


# Sprites

FLOOR_CHART = pg.image.load("C:/Users/Mod Python Dev/Desktop/Openclassroom/Parcours_DA_Python/Projet_3/MacGiver_Game/resources/floor.png").convert()
WALL_CHART = pg.image.load("C:/Users/Mod Python Dev/Desktop/Openclassroom/Parcours_DA_Python/Projet_3/MacGiver_Game/resources/wall.png").convert()
START_CHART = pg.image.load("C:/Users/Mod Python Dev/Desktop/Openclassroom/Parcours_DA_Python/Projet_3/MacGiver_Game/resources/start_finished.png").convert()
GOAL_CHART = pg.image.load("C:/Users/Mod Python Dev/Desktop/Openclassroom/Parcours_DA_Python/Projet_3/MacGiver_Game/resources/start_finished.png").convert()
MACGYVER_CHART = pg.image.load("C:/Users/Mod Python Dev/Desktop/Openclassroom/Parcours_DA_Python/Projet_3/MacGiver_Game/resources/macgyver.png").convert_alpha()
GARDIAN_CHART = pg.image.load("C:/Users/Mod Python Dev/Desktop/Openclassroom/Parcours_DA_Python/Projet_3/MacGiver_Game/resources/gardian.png").convert_alpha()
SYRINGE_NEEDLE_CHART = pg.image.load("C:/Users/Mod Python Dev/Desktop/Openclassroom/Parcours_DA_Python/Projet_3/MacGiver_Game/resources/syringe_needle.png").convert()
ETHER_CHART = pg.image.load("C:/Users/Mod Python Dev/Desktop/Openclassroom/Parcours_DA_Python/Projet_3/MacGiver_Game/resources/ether.png").convert_alpha()
SYRINGE_CHART = pg.image.load("C:/Users/Mod Python Dev/Desktop/Openclassroom/Parcours_DA_Python/Projet_3/MacGiver_Game/resources/syringe.png").convert()
PLASTIC_TUBE_CHART = pg.image.load("C:/Users/Mod Python Dev/Desktop/Openclassroom/Parcours_DA_Python/Projet_3/MacGiver_Game/resources/plastic_tube.png").convert()

# Map structure

START_CHAR = 'S'
GOAL_CHAR = 'G'
PATH_CHAR = '.'
WALL_CHAR = '#'

# Start position characters

X_START_POS_MCGIVER =
Y_START_POS_MC