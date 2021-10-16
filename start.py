import sys
import pygame as pg

from src.game import main


if __name__ == '__main__':
    leaf_game = main.LeafGame()
    leaf_game.run_game()

    pg.quit()
    sys.exit()
