from .Asset import *
from .SpriteSheet import SpriteSheet


class LootSackAsset(Asset):
	def __init__(self, level, position=(1610, 810)):
		self.sprite_sheet = SpriteSheet('loot_sack.png').get_image(frame=0,
																	level=0,
																	width=32,
																	height=32,
																	scale=9,
																	color=(0, 0, 0))
		super().__init__(self.sprite_sheet, position, 0, (144, 144))
		self.level = level
