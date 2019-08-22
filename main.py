#coding:utf-8

"""
Macgiver Labyrinthe GAME
MacGiver have to found the exit of the maze by collecting all the necessary objects to win the GAME.

Script Python
Files: settings.py, main.py, maze.py, macgiver.py, objects.py, gardian.py, game.py, resources
"""


import  pygame as pg
from maze import *
from macgiver import *
from gardian import *
from settings import *
from objects import *

def main():

    map = Map("./resources/map_structure.txt")
    map.load_file()
    macgiver = MacGiver(6, 0, map.my_map)
    gardian = Gardian(7, 14, map.my_map)
    
    """" Objet creation and position definition on the map"""

    syringe_needle = Object(map.my_map)
    plastic_tube = Object(map.my_map)
    ether = Object(map.my_map)
    #syringe = Object(map.my_map)

    syringe_needle.set_objet_position()
    plastic_tube.set_objet_position()
    ether.set_objet_position()
    

    # creation d'une liste vide pour stoker les positions des objects
    object_position_list = []
    position_ether = [ether.x, ether.y]
    object_position_list.append(position_ether)
    position_plastic_tube = [plastic_tube.x, plastic_tube.y]

    # verification de non superposition des object
    # stockage de la position ether dans une liste
    while position_plastic_tube == position_ether:
        plastic_tube.set_objet_position()
    object_position_list.append(position_plastic_tube)
    
    # vérification de trois positions differentes pour les 3 objets
    position_syringe_needle = [syringe_needle.x, syringe_needle.y]
    while (position_syringe_needle == position_plastic_tube) or (position_syringe_needle == position_ether):
        syringe_needle.set_objet_position()
    object_position_list.append(position_syringe_needle)

    # boucle principale du jeu
    launched = True
    while launched:
        macgiver.event_management()
        map.print_map()
        window_surface.blit(MACGYVER_CHART, (macgiver.case_x, macgiver.case_y))
        window_surface.blit(GARDIAN_CHART, (gardian.case_x, gardian.case_y))
        window_surface.blit(ETHER_CHART, (ether.case_x, ether.case_y))
        window_surface.blit(SYRINGE_NEEDLE_CHART, (syringe_needle.case_x, syringe_needle.case_y))
        window_surface.blit(PLASTIC_TUBE_CHART, (plastic_tube.case_x, plastic_tube.case_y))
        pg.display.flip()

        if macgiver.quit:
            launched = False

        if [ether.x, ether.y] == [macgiver.x, macgiver.y]:
            ether.pick_up_object_1()

        if [plastic_tube.x, plastic_tube.y] == [macgiver.x, macgiver.y]:
            plastic_tube.pick_up_object_2()

        if [syringe_needle.x, syringe_needle.y] == [macgiver.x, macgiver.y]:
            syringe_needle.pick_up_object_3()
        
        if [macgiver.x, macgiver.y] == [gardian.x, gardian.y] :
            if ether.object_1_collected and plastic_tube.object_2_collected and syringe_needle.object_3_collected:
                print("Bravo!!!!!!!!!")
                print("Voulez-vous rejouer ? Si OUI taper la touche Entrée. Sinon faites Echape")
                

                launched = False
            else :
                print("U LOSE!!!!!")
                launched = False

if __name__ == "__main__":
    main()