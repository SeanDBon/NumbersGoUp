from .GameMenu import *
import sys
import pygame
from ..settings import Settings
from .InGameOptionsMenu import InGameOptionsMenu


class PauseMenu(GameMenu):
    def __init__(self, screen):
        super().__init__(screen)

        self.show_options_menu = False
        self.igom = InGameOptionsMenu(self.screen)

        # buttons
        self.main_menu_button = Button('main_menu_button.png', (885, 420), 0, (88.75, 21.25), 355, 85, .8, self.main_menu_callback)
        self.options_button = Button('options_button.png', (885, 510), 0, (88.75, 21.25), 355, 85, .8, self.options_callback)
        self.quit_button = Button('quit_button.png', (885, 600), 0, (88.75, 21.25), 355, 85, .8, self.quit_callback)

    def render_menu(self):
        self.render_game_menu()

        # button rendering
        self.screen.blit(self.main_menu_button.sprite, (830, 420))
        self.screen.blit(self.options_button.sprite, (830, 510))
        self.screen.blit(self.quit_button.sprite, (830, 600))

        if self.show_options_menu:
            self.igom.render_menu()
        else:
            self.main_menu_button.check_for_click()
            self.options_button.check_for_click()
            self.quit_button.check_for_click()

    @staticmethod
    def main_menu_callback():
        Settings.isPlaying = False

    def options_callback(self):
        self.show_options_menu = True

    @staticmethod
    def quit_callback():
        pygame.quit()
        sys.exit()
