from .StartScreen import StartScreen


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
