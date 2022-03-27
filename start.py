import sys
import pygame as pg
from src.game.SoundEngine import SoundEngine

from src.menu import MainMenu


if __name__ == '__main__':
    sound_engine = SoundEngine()
    sound_engine.play_music("background_1")
    leaf_game = MainMenu.MainMenu()
    while leaf_game.running:
        sound_engine.update_volume()
        leaf_game.curr_menu.display_menu()
        leaf_game.game_loop()

    pg.quit()
    sys.exit()
