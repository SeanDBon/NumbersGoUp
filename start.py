import sys
import pygame as pg

from src.menu import MainMenu


if __name__ == '__main__':
    leaf_game = MainMenu.MainMenu()
    while leaf_game.running:
        leaf_game.curr_menu.display_menu()
        leaf_game.game_loop()

    pg.quit()
    sys.exit()
