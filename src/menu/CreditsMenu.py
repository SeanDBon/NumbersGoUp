from .StartScreen import StartScreen
from ..game.SoundEngine import SoundEngine


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
