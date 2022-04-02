from .StartScreen import StartScreen
from ..settings import Settings


class ControlMenu(StartScreen):
    def __init__(self, game):
        super().__init__(game)
        self.state = 'Resolution'
        self.volx, self.voly = self.mid_w, self.mid_h + 70
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 140
        self.cursor_rect.midtop = (self.volx + self.offsetx, self.voly + self.offsety)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 100, 0))
            self.game.draw_text('Display Controls', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
            self.game.draw_text('Resolution:        ' + str(Settings.screen_width), 15, self.volx, self.voly)
            self.game.draw_text('FPS:           ' + str(Settings.FPS), 30,  self.controlsx, self.controlsy)
            self.draw_cursor()
            self.blit_screen()

    def draw_cursor(self):
        self.game.draw_text('*', 15, self.cursor_rect.x - 175, self.cursor_rect.y)

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.options
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Resolution':
                self.state = 'FPS'
                self.cursor_rect.midtop = (self.controlsx + self.offsetx, self.controlsy + self.offsety)
            else:
                self.state = 'Resolution'
                self.cursor_rect.midtop = (self.volx + self.offsetx, self.voly + self.offsety)
        elif self.game.RIGHT_KEY:
            if self.state == 'Resolution':
                resolution_index = Settings.valid_h.index(Settings.screen_height)
                if resolution_index != len(Settings.valid_h) - 1:
                    new_resolution_index = resolution_index + 1
                    Settings.screen_height = Settings.valid_h[new_resolution_index]
                    Settings.screen_width = Settings.valid_w[new_resolution_index]
            else:
                fps_index = Settings.valid_fps.index(Settings.FPS)
                if fps_index != len(Settings.valid_fps) - 1:
                    new_fps_index = fps_index + 1
                    Settings.FPS = Settings.valid_fps[new_fps_index]
        elif self.game.LEFT_KEY:
            if self.state == 'Resolution':
                resolution_index = Settings.valid_h.index(Settings.screen_height)
                if resolution_index != 0:
                    new_resolution_index = resolution_index - 1
                    Settings.screen_height = Settings.valid_h[new_resolution_index]
                    Settings.screen_width = Settings.valid_w[new_resolution_index]
            else:
                fps_index = Settings.valid_fps.index(Settings.FPS)
                if fps_index != 0:
                    new_fps_index = fps_index - 1
                    Settings.FPS = Settings.valid_fps[new_fps_index]
