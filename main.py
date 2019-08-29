#coding:utf-8

"""
Macgyver Labyrinthe GAME
MacGyver have to found the exit of the maze by collecting all the necessary objects to win the GAME.

Script Python
Files: settings.py, main.py, maze.py, macgyver.py, objects.py, gardian.py, game.py, resources
"""

import pygame as pg
from maze import *
from macgyver import *
from gardian import *
from settings import *
from objects import *

def main():

    map = Map("./resources/map_structure.txt")
    map.load_file()
    macgyver = MacGyver(6, 0, map.my_map)
    gardian = Gardian(7, 14, map.my_map)
    
    """" Objet creation and position definition on the map"""

    syringe_needle = Object(map.my_map)
    plastic_tube = Object(map.my_map)
    ether = Object(map.my_map)

    """" Definition of object position on the map """

    syringe_needle.set_objet_position()
    plastic_tube.set_objet_position()
    ether.set_objet_position()

    running = True
    while running:
        macgyver.event_management()
        map.print_map()
        window_surface.blit(MACGYVER_CHART, (macgyver.case_x, macgyver.case_y))
        window_surface.blit(GARDIAN_CHART, (gardian.case_x, gardian.case_y))
        window_surface.blit(ETHER_CHART, (ether.case_x, ether.case_y))
        window_surface.blit(SYRINGE_NEEDLE_CHART, (syringe_needle.case_x, syringe_needle.case_y))
        window_surface.blit(PLASTIC_TUBE_CHART, (plastic_tube.case_x, plastic_tube.case_y))
        pg.display.flip()

        if macgyver.quit:
            launched = False

        if [plastic_tube.x, plastic_tube.y] == [macgyver.x, macgyver.y]:
            plastic_tube.pick_up_object()

        if [ether.x, ether.y] == [macgyver.x, macgyver.y]:
            ether.pick_up_object()

        if [syringe_needle.x, syringe_needle.y] == [macgyver.x, macgyver.y]:
            syringe_needle.pick_up_object()
        
        if [macgyver.x, macgyver.y] == [gardian.x, gardian.y]:
            if plastic_tube.object_collected and ether.object_collected and syringe_needle.object_collected:
                victory = True
                while victory:
                    window_surface.blit(WINNER_SCREEN, (0,0))
                    pg.display.flip()
                    for event in pg.event.get():
                        if event.type == KEYDOWN and event.key == K_RETURN:
                            victory = False
                        if event.type == KEYDOWN and event.key == K_ESCAPE:
                            victory = False                        
                running = False
                
            else:
                victory = True
                while victory:
                    window_surface.blit(LOSER_SCREEN, (0,0))
                    pg.display.flip()
                    for event in pg.event.get():
                        if event.type == KEYDOWN and event.key == K_RETURN:
                            victory = False
                        if event.type == KEYDOWN and event.key == K_ESCAPE:
                            victory = False
                running = False

if __name__ == "__main__":
    main()