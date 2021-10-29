from ..game.data.Asset import *
from ..game.data.SpriteSheet import *


class Button(Asset):
    def __init__(self, image, position, rotation, rect_center_offset, width, height, scale):
        self.sprite_sheet = SpriteSheet(image).get_image(width=width, height=height, scale=scale)
        super().__init__(self.sprite_sheet, position, rotation, rect_center_offset)
        self.clicked = False

    def check_for_click(self):
        if self.get_collision_rect().collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked = True
            else:
                self.clicked = False
        else:
            self.clicked = False
