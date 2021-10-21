from .Asset import *
from .SpriteSheet import SpriteSheet


class LootSackAsset(Asset):
	def __init__(self, level, position=(1550, 780)):
		sprite_sheet_image = pygame.image.load('resources/assets/loot_sack.png').convert_alpha()
		self.sprite_sheet = SpriteSheet(sprite_sheet_image)

		self.level = level
		self.sprite = self.construct_loot_sack_image()
		super().__init__(position, self.sprite, 0, (144, 144), (0, 0))

	def construct_loot_sack_image(self):
		scale = 9
		rotation = 0
		dim_x = 32
		dim_y = 32
		color_key = (0, 0, 0)
		return self.sprite_sheet.get_image(0, 0, dim_x, dim_y, scale, color_key, rotation)
