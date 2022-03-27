from ..settings import *
from .Button import *


class GameMenu:
    def __init__(self, screen):
        self.background = SpriteSheet('scroll_menu.png').get_image(width=2175, height=1165, scale=.4,
                                                                   color=(255, 255, 47))
        self.screen = screen
        self.is_game_menu_showing = False

    # buttons
        self.x_button = Button('x_button.png', (1211, 362), 0, (24, 24), 400, 400, .12, self.x_button_callback)

    # button rendering
        self.screen.blit(self.x_button.sprite, (1211, 362))

    # button clicks
        self.x_button.check_for_click()

    def x_button_callback(self):
        self.is_game_menu_showing = not self.is_game_menu_showing

    def render_game_menu(self):
        pos_x = (Settings.screen_width / 2) - (self.background.get_width() / 2)
        pos_y = (Settings.screen_height / 2) - (self.background.get_height() / 2)
        self.screen.blit(self.background, (pos_x, pos_y))
