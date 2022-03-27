from .Button import *
from .GameMenu import *


class WeaponMenu(GameMenu):
    def __init__(self, screen, scores):
        super().__init__(screen)

        self.scores = scores
        self.is_game_menu_showing = False

        # buttons
        self.weapon_level_button = Button('upgrade_button.png', (690, 400), 0, (88.75, 21.25), 355, 85, .5, self.weapon_upgrade_level_callback)
        self.weapon_num_button = Button('upgrade_button.png', (690, 500), 0, (88.75, 21.25), 355, 85, .5, self.weapon_upgrade_num_callback)

        # text
        pygame.font.init()
        self.font = pygame.font.Font("resources/fonts/PixelFont.otf", 20)
        self.weapon_level_text = self.font.render(str(self.scores.weapon_level), False, (0, 0, 0))
        self.weapon_level_label_text = self.font.render("Weapon lvl:", False, (0, 0, 0))
        self.weapon_level_upgrade_cost_text = self.font.render(str(self.scores.weapon_level_upgrade_cost), False, (0, 0, 0))
        self.weapon_num_text = self.font.render(str(self.scores.num_weapons), False, (0, 0, 0))
        self.weapon_num_label_text = self.font.render("Num of Weapons:", False, (0, 0, 0))
        self.weapon_num_upgrade_cost_text = self.font.render(str(self.scores.weapon_num_upgrade_cost), False, (0, 0, 0))

    def render_menu(self):
        self.render_game_menu()

        # level text rendering
        self.weapon_level_text = self.font.render(str(int(self.scores.weapon_level)), False, (0, 0, 0))
        self.weapon_level_upgrade_cost_text = self.font.render(str(int(self.scores.weapon_level_upgrade_cost)), False, (0, 0, 0))
        self.screen.blit(self.weapon_level_upgrade_cost_text, (925, 412))
        self.screen.blit(self.weapon_level_label_text, (1030, 412))
        self.screen.blit(self.weapon_level_text, (1147, 413))

        # num text rendering
        self.weapon_num_text = self.font.render(str(self.scores.num_weapons), False, (0, 0, 0))
        self.weapon_num_upgrade_cost_text = self.font.render(str(int(self.scores.weapon_num_upgrade_cost)), False, (0, 0, 0))
        self.screen.blit(self.weapon_num_upgrade_cost_text, (925, 512))
        self.screen.blit(self.weapon_num_label_text, (1030, 512))
        self.screen.blit(self.weapon_num_text, (1213, 513))

        # button rendering
        self.screen.blit(self.weapon_level_button.sprite, (690, 400))
        self.screen.blit(self.weapon_num_button.sprite, (690, 500))

        # button clicks
        self.weapon_level_button.check_for_click()
        self.weapon_num_button.check_for_click()

    def weapon_upgrade_level_callback(self):
        if self.scores.weapon_level < 11:
            if self.scores.total_points >= self.scores.weapon_level_upgrade_cost:
                self.scores.total_points -= self.scores.weapon_level_upgrade_cost
                self.scores.weapon_level_upgrade_cost *= 1.1
                self.scores.weapon_level += 1

    def weapon_upgrade_num_callback(self):
        if self.scores.total_points >= self.scores.weapon_num_upgrade_cost:
            self.scores.total_points -= self.scores.weapon_num_upgrade_cost
            self.scores.weapon_num_upgrade_cost *= 1.1
            self.scores.num_weapons += 20
