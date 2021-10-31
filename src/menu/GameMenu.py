from ..settings import *
from .Button import *


class GameMenu:
    def __init__(self, scores):
        self.background = SpriteSheet('scroll_menu.png').get_image(width=2175, height=1165, scale=.4,
                                                                   color=(255, 255, 47))
        self.scores = scores
        self.is_game_menu_showing = False

        # buttons
        self.x_button = Button('x_button.png', (1211, 362), 0, (24, 24), 400, 400, .12, self.x_button_callback)
        self.knight_level_button = Button('upgrade_button.png', (690, 400), 0, (88.75, 21.25), 355, 85, .5, self.knight_upgrade_level_callback)
        self.knight_num_button = Button('upgrade_button.png', (690, 500), 0, (88.75, 21.25), 355, 85, .5, self.knight_upgrade_num_callback)

        # text
        pygame.font.init()
        self.font = pygame.font.Font("resources/fonts/PixelFont.otf", 20)
        self.knight_level_text = self.font.render(str(self.scores.knight_level), False, (0, 0, 0))
        self.knight_level_label_text = self.font.render("Knight lvl:", False, (0, 0, 0))
        self.knight_level_upgrade_cost_text = self.font.render(str(self.scores.knight_level_upgrade_cost), False, (0, 0, 0))
        self.knight_num_upgrade_cost_text = self.font.render(str(self.scores.knight_num_upgrade_cost), False, (0, 0, 0))
        self.knight_num_text = self.font.render(str(self.scores.num_knights), False, (0, 0, 0))
        self.knight_num_label_text = self.font.render("Num of Knights:", False, (0, 0, 0))

    def render_menu(self, screen):
        pos_x = (Settings.screen_width / 2) - (self.background.get_width() / 2)
        pos_y = (Settings.screen_height / 2) - (self.background.get_height() / 2)
        screen.blit(self.background, (pos_x, pos_y))

        # button rendering
        screen.blit(self.x_button.sprite, (1211, 362))
        screen.blit(self.knight_level_button.sprite, (690, 400))
        screen.blit(self.knight_num_button.sprite, (690, 500))

        # text rendering
        self.knight_level_text = self.font.render(str(int(self.scores.knight_level / 3)), False, (0, 0, 0))
        self.knight_level_upgrade_cost_text = self.font.render(str(int(self.scores.knight_level_upgrade_cost)), False, (0, 0, 0))
        screen.blit(self.knight_level_upgrade_cost_text, (925, 412))
        screen.blit(self.knight_level_label_text, (1030, 412))
        screen.blit(self.knight_level_text, (1142, 413))

        self.knight_num_text = self.font.render(str(self.scores.num_knights), False, (0, 0, 0))
        self.knight_num_upgrade_cost_text = self.font.render(str(int(self.scores.knight_num_upgrade_cost)), False, (0, 0, 0))
        screen.blit(self.knight_num_upgrade_cost_text, (925, 512))
        screen.blit(self.knight_num_label_text, (1030, 512))
        screen.blit(self.knight_num_text, (1210, 513))

        # button clicks
        self.x_button.check_for_click()
        self.knight_level_button.check_for_click()
        self.knight_num_button.check_for_click()

    def x_button_callback(self):
        self.is_game_menu_showing = not self.is_game_menu_showing

    def knight_upgrade_level_callback(self):
        if self.scores.knight_level + 3 < 12:
            if self.scores.total_points >= self.scores.knight_level_upgrade_cost:
                self.scores.total_points -= self.scores.knight_level_upgrade_cost
                self.scores.knight_level_upgrade_cost *= 1.1
                self.scores.knight_level += 3

    def knight_upgrade_num_callback(self):
        if self.scores.total_points >= self.scores.knight_num_upgrade_cost:
            self.scores.total_points -= self.scores.knight_num_upgrade_cost
            self.scores.knight_num_upgrade_cost *= 1.1
            self.scores.num_knights += 1
