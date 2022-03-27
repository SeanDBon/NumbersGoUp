from .GameMenu import *
import sys
import pygame
from ..settings import Settings


class InGameOptionsMenu(GameMenu):
    def __init__(self, screen):
        super().__init__(screen)

        pygame.font.init()
        self.font = pygame.font.Font("resources/fonts/PixelFont.otf", 40)

        self.music_up_button = Button('woop_button.png', (1000, 487), 0, (24, 24), 400, 400, .12,
                                          self.music_up_callback)
        self.music_down_button = Button('minus_button.png', (900, 487), 0, (24, 24), 400, 400, .12,
                                        self.music_down_callback)
        self.effect_up_button = Button('woop_button.png', (1000, 587), 0, (24, 24), 400, 400, .12,
                                      self.effect_up_callback)
        self.effect_down_button = Button('minus_button.png', (900, 587), 0, (24, 24), 400, 400, .12,
                                        self.effect_down_callback)

    def render_menu(self):
        self.render_game_menu()

        music_value_text = self.font.render(str(abs(round(Settings.music_volume * 10))), False, (0, 0, 0))
        effect_value_text = self.font.render(str(abs(round(Settings.sound_effect_volume * 10))), False, (0, 0, 0))
        music_label_text = self.font.render('Music', False, (0, 0, 0))
        effect_label_text = self.font.render('Effect', False, (0, 0, 0))
        options_header_text = self.font.render('Options', False, (0, 0, 0))

        self.screen.blit(music_value_text, (966, 494))
        self.screen.blit(effect_value_text, (969, 594))
        self.screen.blit(music_label_text, (716, 494))
        self.screen.blit(effect_label_text, (716, 594))
        self.screen.blit(options_header_text, (900, 394))

        self.screen.blit(self.music_up_button.sprite, (1000, 487))
        self.screen.blit(self.music_down_button.sprite, (900, 487))
        self.screen.blit(self.effect_up_button.sprite, (1000, 587))
        self.screen.blit(self.effect_down_button.sprite, (900, 587))

        self.music_up_button.check_for_click()
        self.music_down_button.check_for_click()
        self.effect_up_button.check_for_click()
        self.effect_down_button.check_for_click()

    @staticmethod
    def music_up_callback():
        if round(Settings.music_volume, 2) < 1:
            Settings.music_volume += .1


    @staticmethod
    def music_down_callback():
        if round(Settings.music_volume, 2) > 0.00:
            Settings.music_volume -= .1

    @staticmethod
    def effect_up_callback():
        if round(Settings.sound_effect_volume, 2) < 1:
            Settings.sound_effect_volume += .1

    @staticmethod
    def effect_down_callback():
        if round(Settings.sound_effect_volume, 2) > 0.00:
            Settings.sound_effect_volume -= .1

