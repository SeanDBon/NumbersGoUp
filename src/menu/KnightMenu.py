from .GameMenu import *


class KnightMenu(GameMenu):
    def __init__(self, screen, scores):
        super().__init__(screen)

        self.scores = scores
        self.is_game_menu_showing = False

        # buttons
        self.knight_level_button = Button('upgrade_button.png', (690, 400), 0, (88.75, 21.25), 355, 85, .5, self.knight_upgrade_level_callback)
        self.knight_num_button = Button('upgrade_button.png', (690, 500), 0, (88.75, 21.25), 355, 85, .5, self.knight_upgrade_num_callback)

        # text
        pygame.font.init()
        self.font = pygame.font.Font("resources/fonts/PixelFont.otf", 20)
        self.knight_level_text = self.font.render(str(self.scores.knight_level), False, (0, 0, 0))
        self.knight_level_label_text = self.font.render("Knight lvl:", False, (0, 0, 0))
        self.knight_level_upgrade_cost_text = self.font.render(str(self.scores.knight_level_upgrade_cost), False, (0, 0, 0))
        self.knight_num_text = self.font.render(str(self.scores.num_knights), False, (0, 0, 0))
        self.knight_num_label_text = self.font.render("Num of Knights:", False, (0, 0, 0))
        self.knight_num_upgrade_cost_text = self.font.render(str(self.scores.knight_num_upgrade_cost), False, (0, 0, 0))

    def render_menu(self):
        self.render_game_menu()

        # level text rendering
        self.knight_level_text = self.font.render(str(int(self.scores.knight_level / 3)), False, (0, 0, 0))
        self.knight_level_upgrade_cost_text = self.font.render(str(int(self.scores.knight_level_upgrade_cost)), False, (0, 0, 0))
        self.screen.blit(self.knight_level_upgrade_cost_text, (925, 412))
        self.screen.blit(self.knight_level_label_text, (1030, 412))
        self.screen.blit(self.knight_level_text, (1142, 413))

        # num text rendering
        self.knight_num_text = self.font.render(str(self.scores.num_knights), False, (0, 0, 0))
        self.knight_num_upgrade_cost_text = self.font.render(str(int(self.scores.knight_num_upgrade_cost)), False, (0, 0, 0))
        self.screen.blit(self.knight_num_upgrade_cost_text, (925, 512))
        self.screen.blit(self.knight_num_label_text, (1030, 512))
        self.screen.blit(self.knight_num_text, (1210, 513))

        # button rendering
        self.screen.blit(self.knight_level_button.sprite, (690, 400))
        self.screen.blit(self.knight_num_button.sprite, (690, 500))

        # button clicks
        self.knight_level_button.check_for_click()
        self.knight_num_button.check_for_click()

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
