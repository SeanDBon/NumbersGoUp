from .GameMenu import *
import sys
import pygame


class PauseMenu(GameMenu):
    def __init__(self, screen, bitch):
        super().__init__(screen)
        self.bitch = bitch

        # buttons
        self.main_menu_button = Button('main_menu_button.png', (690, 400), 0, (88.75, 21.25), 355, 85, .5, self.main_menu_callback)
        self.quit_button = Button('quit_button.png', (690, 500), 0, (88.75, 21.25), 355, 85, .5, self.quit_callback)

    def render_menu(self):
        self.render_game_menu()

        # button rendering
        self.screen.blit(self.main_menu_button.sprite, (690, 400))
        self.screen.blit(self.quit_button.sprite, (690, 500))

        # button clicks
        self.main_menu_button.check_for_click()
        self.quit_button.check_for_click()

    def main_menu_callback(self):
        bitch = False

    def quit_callback(self):
        pygame.quit()
        sys.exit()
