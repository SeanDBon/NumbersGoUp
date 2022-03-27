from .Menu import Menu
import sys
import pygame
from ..settings import Settings


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
                Settings.isPlaying = True
            elif self.state == 'Options':
                print("asdfasdfasdf")
                self.game.curr_menu = self.game.options
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            elif self.state == 'Quit to Desktop':
                pygame.quit()
                sys.exit()
            self.run_display = False
