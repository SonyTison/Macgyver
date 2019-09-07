#coding:utf-8

"""
Macgyver Labyrinth Game
Macgyver has to find the exit of the maze by collecting all the objects needed to win the Game.

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
    game.start()

if __name__ == "__main__":
    main()