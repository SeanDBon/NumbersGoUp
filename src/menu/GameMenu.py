from ..game.data.SpriteSheet import *
from ..settings import *
from .Button import *


class GameMenu:
    def __init__(self, show_game_menu):
        self.show_game_menu = show_game_menu
        self.background = SpriteSheet('scroll_menu.png').get_image(width=2175, height=1165, scale=.4,
                                                                   color=(255, 255, 47))
        self.button1 = Button('x_button.png', (1211, 362), 0, (24, 24), 400, 400, .12, self.button1_callback)

    def render_menu(self, screen):
        pos_x = (Settings.screen_width / 2) - (self.background.get_width() / 2)
        pos_y = (Settings.screen_height / 2) - (self.background.get_height() / 2)
        screen.blit(self.background, (pos_x, pos_y))
        screen.blit(self.button1.sprite, (1211, 362))

        self.button1.check_for_click()

    def button1_callback(self):
        self.show_game_menu["enabled"] = not self.show_game_menu["enabled"]
