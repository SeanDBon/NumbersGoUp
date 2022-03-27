from .StartScreen import StartScreen
from ..settings import Settings


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