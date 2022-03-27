import pygame
import pygame.mixer
import sys
from src.settings import Settings
from ..game.SoundEngine import SoundEngine


class Menu:
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offsetx = - 250
        self.offsety = 13

    def draw_cursor(self):
        self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()


class StartScreen(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 70
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 140
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 210
        self.quitx, self.quity = self.mid_w, self.mid_h + 280
        self.cursor_rect.midtop = (self.startx + self.offsetx, self.starty + self.offsety)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('xX_Numbers_Go_Up_Xx', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
            self.game.draw_text("Start Game", 20, self.startx, self.starty)
            self.game.draw_text("Options", 20, self.optionsx, self.optionsy)
            self.game.draw_text("Credits", 20, self.creditsx, self.creditsy)
            self.game.draw_text("Quit to Desktop", 20, self.quitx, self.quity)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.optionsx + self.offsetx, self.optionsy + self.offsety)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.creditsx + self.offsetx, self.creditsy + self.offsety)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.quitx + self.offsetx, self.quity + self.offsety)
                self.state = 'Quit to Desktop'
            elif self.state == 'Quit to Desktop':
                self.cursor_rect.midtop = (self.startx + self.offsetx, self.starty + self.offsety)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.quitx + self.offsetx, self.quity + self.offsety)
                self.state = 'Quit to Desktop'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.startx + self.offsetx, self.starty + self.offsety)
                self.state = 'Start'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.optionsx + self.offsetx, self.optionsy + self.offsety)
                self.state = 'Options'
            elif self.state == 'Quit to Desktop':
                self.cursor_rect.midtop = (self.creditsx + self.offsetx, self.creditsy + self.offsety)
                self.state = 'Credits'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Options':
                self.game.curr_menu = self.game.options
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            elif self.state == 'Quit to Desktop':
                pygame.quit()
                sys.exit()
            self.run_display = False


class OptionsMenu(StartScreen):
    def __init__(self, game):
        super().__init__(game)
        self.state = 'Volume'
        self.volx, self.voly = self.mid_w, self.mid_h + 70
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 140
        self.cursor_rect.midtop = (self.volx + self.offsetx, self.voly + self.offsety)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Options', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
            self.game.draw_text("Volume", 15, self.volx, self.voly)
            self.game.draw_text("Controls", 15, self.controlsx, self.controlsy)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Volume':
                self.state = 'Controls'
                self.cursor_rect.midtop = (self.controlsx + self.offsetx, self.controlsy + self.offsety)
            elif self.state == 'Controls':
                self.state = 'Volume'
                self.cursor_rect.midtop = (self.volx + self.offsetx, self.voly + self.offsety)
        elif self.game.START_KEY:
            if self.state == 'Volume':
                self.game.curr_menu = self.game.volume
                self.run_display = False



class VolumeMenu(StartScreen):
    def __init__(self, game):
        super().__init__(game)
        self.state = 'Music'
        self.volx, self.voly = self.mid_w, self.mid_h + 70
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 140
        self.cursor_rect.midtop = (self.volx + self.offsetx, self.voly + self.offsety)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((100, 0, 0))
            self.game.draw_text('Volume Slider', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
            self.game.draw_text("Music Volume:    " + str(abs(round(Settings.music_volume * 100))), 15,  self.volx, self.voly)
            self.game.draw_text("Effect Volume:   " + str(abs(round(Settings.sound_effect_volume, 2))), 30,  self.controlsx, self.controlsy)
            self.draw_cursor()
            self.blit_screen()

    def draw_cursor(self):
        self.game.draw_text('*', 15, self.cursor_rect.x - 175, self.cursor_rect.y)

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.options
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Effect':
                self.state = 'Music'
                self.cursor_rect.midtop = (self.volx + self.offsetx, self.voly + self.offsety)
            else:
                self.state = 'Effect'
                self.cursor_rect.midtop = (self.controlsx + self.offsetx, self.controlsy + self.offsety)
        elif self.game.RIGHT_KEY:
            if self.state == 'Music':
                if round(Settings.music_volume, 2) < .10:
                    Settings.music_volume += .01
            else:
                if round(Settings.sound_effect_volume, 2) < 10:
                    Settings.sound_effect_volume += 1
        elif self.game.LEFT_KEY:
            if self.state == 'Music':
                if round(Settings.music_volume, 2) > 0.00:
                    Settings.music_volume -= .01
            else:
                if round(Settings.sound_effect_volume, 2) > 0:
                    Settings.sound_effect_volume -= 1


class CreditsMenu(StartScreen):
    def __init__(self, game):
        super().__init__(game)
        self.sound_engine = SoundEngine()
        self.state = "Nick"
        self.nickx, self.nicky = self.mid_w, self.mid_h + 70
        self.seanx, self.seany = self.mid_w, self.mid_h + 140
        self.josephx, self.josephy = self.mid_w, self.mid_h + 210
        self.cursor_rect.midtop = (self.nickx + self.offsetx, self.nicky + self.offsety)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            if self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Credits', 50, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
            self.game.draw_text('Nick Bonorden', 35, self.nickx, self.nicky)
            self.game.draw_text('Sean Bonorden', 35, self.seanx, self.seany)
            self.game.draw_text('Joseph Nevienski', 35, self.josephx, self.josephy)
            self.move_cursor()
            self.draw_cursor()
            self.blit_screen()

    def draw_cursor(self):
        self.game.draw_text('*', 15, self.cursor_rect.x - 50, self.cursor_rect.y)

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Nick':
                self.cursor_rect.midtop = (self.seanx + self.offsetx, self.seany + self.offsety)
                self.state = 'Sean'
            elif self.state == 'Sean':
                self.cursor_rect.midtop = (self.josephx + self.offsetx, self.josephy + self.offsety)
                self.state = 'Joseph'
            elif self.state == 'Joseph':
                self.cursor_rect.midtop = (self.nickx + self.offsetx, self.nicky + self.offsety)
                self.state = 'Nick'
        elif self.game.UP_KEY:
            if self.state == 'Nick':
                self.cursor_rect.midtop = (self.josephx + self.offsetx, self.josephy + self.offsety)
                self.state = 'Joseph'
            elif self.state == 'Sean':
                self.cursor_rect.midtop = (self.nickx + self.offsetx, self.nicky + self.offsety)
                self.state = 'Nick'
            elif self.state == 'Joseph':
                self.cursor_rect.midtop = (self.seanx + self.offsetx, self.seany + self.offsety)
                self.state = 'Sean'

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.START_KEY:
            if self.state == 'Nick':
                self.sound_engine.play_sound_effect('nick_sound')
            elif self.state == 'Sean':
                self.sound_engine.play_sound_effect('sean_sound')
            elif self.state == 'Joseph':
                self.sound_engine.play_sound_effect('jose_sound')
