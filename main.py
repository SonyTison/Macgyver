# coding: utf-8
"""
Macgyver Labyrinth Game
Macgyver has to find the exit of the maze by collecting all the objects needed to win the Game.

Script Python
Files: settings.py, main.py, maze.py, macgyver.py, objects.py, guardian.py, game.py, resources
"""
from game import *

def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()