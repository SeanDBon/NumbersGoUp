from .Menu import *
from ..game import main
import sys
import pygame as pg
from src.settings import Settings


class MainMenu:
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.LEFT_KEY, self.RIGHT_KEY = False, False, False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = Settings.screen_width, Settings.screen_height
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))
        self.font_name = pygame.font.Font("resources/fonts/SquidFont.ttf", 20)
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        self.main_menu = StartScreen(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.volume = VolumeMenu(self)
        self.curr_menu = self.main_menu

    def game_loop(self):
        while self.playing:
            self.check_events()
            leaf_game = main.NumbersGoUp()
            leaf_game.run_game()

            pg.quit()
            sys.exit()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
                if event.key == pygame.K_RIGHT:
                    self.RIGHT_KEY = True
                if event.key == pygame.K_LEFT:
                    self.LEFT_KEY = True

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.LEFT_KEY, self.RIGHT_KEY = False, False, False, False, False, False

    def draw_text(self, text, size, x, y):
        pygame.font.init()
        font = pygame.font.Font("resources/fonts/SquidFont.ttf", 50)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)
