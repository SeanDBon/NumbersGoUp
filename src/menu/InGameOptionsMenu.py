from .GameMenu import *
import sys
import pygame
from ..settings import Settings


class InGameOptionsMenu(GameMenu):
    def __init__(self, screen):
        super().__init__(screen, use_big_background=True)

        pygame.font.init()
        self.font = pygame.font.Font("resources/fonts/PixelFont.otf", 40)

        self.music_up_button = Button('woop_button.png', (1150, 387), 0, (24, 24), 400, 400, .12,
                                          self.music_up_callback)
        self.music_down_button = Button('minus_button.png', (950, 387), 0, (24, 24), 400, 400, .12,
                                        self.music_down_callback)
        self.effect_up_button = Button('woop_button.png', (1150, 487), 0, (24, 24), 400, 400, .12,
                                      self.effect_up_callback)
        self.effect_down_button = Button('minus_button.png', (950, 487), 0, (24, 24), 400, 400, .12,
                                        self.effect_down_callback)
        self.res_up_button = Button('woop_button.png', (1150, 587), 0, (24, 24), 400, 400, .12,
                                      self.res_up_callback)
        self.res_down_button = Button('minus_button.png', (950, 587), 0, (24, 24), 400, 400, .12,
                                        self.res_down_callback)
        self.fps_up_button = Button('woop_button.png', (1150, 687), 0, (24, 24), 400, 400, .12,
                                       self.fps_up_callback)
        self.fps_down_button = Button('minus_button.png', (950, 687), 0, (24, 24), 400, 400, .12,
                                         self.fps_down_callback)

    def render_menu(self):
        self.render_game_menu()

        music_value_text = self.font.render(str(abs(round(Settings.music_volume * 10))), False, (0, 0, 0))
        effect_value_text = self.font.render(str(abs(round(Settings.sound_effect_volume * 10))), False, (0, 0, 0))
        music_label_text = self.font.render('Music', False, (0, 0, 0))
        effect_label_text = self.font.render('Effect', False, (0, 0, 0))
        options_header_text = self.font.render('Options', False, (0, 0, 0))
        res_label_text = self.font.render('Resolution', False, (0, 0, 0))
        fps_label_text = self.font.render('FPS', False, (0, 0, 0))
        res_value_text = self.font.render(str(Settings.screen_height), False, (0, 0, 0))
        fps_value_text = self.font.render(str(Settings.FPS), False, (0, 0, 0))

        self.screen.blit(music_value_text, (1066, 394))
        self.screen.blit(effect_value_text, (1069, 494))
        self.screen.blit(music_label_text, (716, 394))
        self.screen.blit(effect_label_text, (716, 494))
        self.screen.blit(options_header_text, (900, 294))
        self.screen.blit(res_value_text, (1040, 593))
        self.screen.blit(fps_value_text, (1050, 693))
        self.screen.blit(res_label_text, (716, 587))
        self.screen.blit(fps_label_text, (716, 687))

        # Music & Effect Blits
        self.screen.blit(self.music_up_button.sprite, (1150, 387))
        self.screen.blit(self.music_down_button.sprite, (950, 387))
        self.screen.blit(self.effect_up_button.sprite, (1150, 487))
        self.screen.blit(self.effect_down_button.sprite, (950, 487))

        # Res & FPS Blits
        self.screen.blit(self.res_up_button.sprite, (1150, 587))
        self.screen.blit(self.res_down_button.sprite, (950, 587))
        self.screen.blit(self.fps_up_button.sprite, (1150, 687))
        self.screen.blit(self.fps_down_button.sprite, (950, 687))

        # Check for Clicks
        self.music_up_button.check_for_click()
        self.music_down_button.check_for_click()
        self.effect_up_button.check_for_click()
        self.effect_down_button.check_for_click()
        self.res_up_button.check_for_click()
        self.res_down_button.check_for_click()
        self.fps_up_button.check_for_click()
        self.fps_down_button.check_for_click()

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

    @staticmethod
    def res_up_callback():
        resolution_index = Settings.valid_h.index(Settings.screen_height)
        if resolution_index != len(Settings.valid_h) - 1:
            new_resolution_index = resolution_index + 1
            Settings.screen_height = Settings.valid_h[new_resolution_index]
            Settings.screen_width = Settings.valid_w[new_resolution_index]

    @staticmethod
    def res_down_callback():
        resolution_index = Settings.valid_h.index(Settings.screen_height)
        if resolution_index != 0:
            new_resolution_index = resolution_index - 1
            Settings.screen_height = Settings.valid_h[new_resolution_index]
            Settings.screen_width = Settings.valid_w[new_resolution_index]

    @staticmethod
    def fps_up_callback():
        fps_index = Settings.valid_fps.index(Settings.FPS)
        if fps_index != len(Settings.valid_fps) - 1:
            new_fps_index = fps_index + 1
            Settings.FPS = Settings.valid_fps[new_fps_index]

    @staticmethod
    def fps_down_callback():
        fps_index = Settings.valid_fps.index(Settings.FPS)
        if fps_index != 0:
            new_fps_index = fps_index - 1
            Settings.FPS = Settings.valid_fps[new_fps_index]



