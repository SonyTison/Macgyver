#coding:utf-8

"""
Macgyver Labyrinth GAME
Macgyver has to find the exit of the maze by collecting all the objects needed to win the GAME.

Script Python
Files: settings.py, main.py, maze.py, macgyver.py, objects.py, guardian.py, game.py, resources
"""

import pygame as pg
from maze import *
from macgyver import *
from guardian import *
from settings import *
from objects import *
from game import *

def main():
    game = Game()
    game.intro()

    launched = True
    while launched:

        map = Map("./resources/map_structure.txt")
        map.load_file()
        macgyver = MacGyver(6, 0, map.my_map)
        guardian = Guardian(7, 14, map.my_map)
        objs = Object(map.my_map)
        objs.set_all_object_position()

        running = True
        while running:
            macgyver.event_management()
            map.print_map()
            window_surface.blit(MACGYVER_CHART, (macgyver.case_x, macgyver.case_y))
            window_surface.blit(GUARDIAN_CHART, (guardian.case_x, guardian.case_y))
            window_surface.blit(ETHER_CHART, (objs.object_position_list[0][0] * SPRITE_SIZE, objs.object_position_list[0][1] * SPRITE_SIZE))
            window_surface.blit(SYRINGE_NEEDLE_CHART, (objs.object_position_list[1][0] * SPRITE_SIZE, objs.object_position_list[1][1] * SPRITE_SIZE))
            window_surface.blit(PLASTIC_TUBE_CHART, (objs.object_position_list[2][0] * SPRITE_SIZE, objs.object_position_list[2][1] * SPRITE_SIZE))
            pg.display.flip()

            if macgyver.quit:
                running = False
                launched = False

            if [macgyver.x, macgyver.y] in objs.object_position_list:
                objs.pick_up_object([macgyver.x, macgyver.y])
            
            if [macgyver.x, macgyver.y] == [guardian.x, guardian.y]:
                if objs.case_x_obj == 3:
                    victory = True
                    while victory:
                        window_surface.blit(WINNER_SCREEN, (0,0))
                        pg.display.flip()
                        for event in pg.event.get():
                            if event.type == QUIT:
                                launched = False
                                victory = False
                            if event.type == KEYDOWN and event.key == K_ESCAPE:
                                launched = False
                                victory = False
                            if event.type == KEYDOWN and event.key == K_RETURN:
                                victory = False                  
                    running = False

                else:
                    victory = True
                    while victory:
                        window_surface.blit(LOSER_SCREEN, (0,0))
                        pg.display.flip()
                        for event in pg.event.get():
                            if event.type == QUIT:
                                launched = False
                                victory = False
                            if event.type == KEYDOWN and event.key == K_ESCAPE:
                                launched = False
                                victory = False
                            if event.type == KEYDOWN and event.key == K_RETURN:
                                victory = False
                    running = False

if __name__ == "__main__":
    main()