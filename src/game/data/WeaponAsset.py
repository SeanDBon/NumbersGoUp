from .Asset import *
from .SpriteSheet import *
from random import *
from ...settings import Settings


class WeaponAsset(Asset):
	def __init__(self, position, sprite, rotation, rect_center_offset, velocity, name, level):
		super().__init__(position, sprite, rotation, rect_center_offset, velocity)

		self.name = name
		self.level = level
		self.settings = Settings()

	def update_asset_position_in_bounds(self):
		self.update_asset_position()
		self.bounce_off_screen_bounds()

	def bounce_off_screen_bounds(self):
		if 0 < self.position[0] < self.settings.screen_width - 64:
			vector_x_velocity = self.x_velocity
			if vector_x_velocity > 0:
				vector_x_velocity -= .05
			elif vector_x_velocity < 0:
				vector_x_velocity += .05
			self.x_velocity = vector_x_velocity
		else:
			self.x_velocity = self.x_velocity * -1

		if 0 < self.position[1] < self.settings.screen_height - 64:
			vector_y_velocity = self.y_velocity
			if vector_y_velocity > 0:
				vector_y_velocity -= .05
			elif vector_y_velocity < 0:
				vector_y_velocity += .05
			self.y_velocity = vector_y_velocity
		else:
			self.y_velocity = self.y_velocity * -1

		x = self.position[0] + self.x_velocity
		y = self.position[1] + self.y_velocity
		self.position = (x, y)


class WeaponAssetFactory:
	def __init__(self):
		sprite_sheet_image = pygame.image.load('resources/assets/weapons_sprite.png').convert_alpha()
		self.sprite_sheet = SpriteSheet(sprite_sheet_image)
		self.weapon_types = ["Sword", "Halberd", "Staff", "Bow", "Shield", "Special"]
		self.weapon_levels = ["Wood", "Bronze", "Iron", "Steel", "Obsidian", "Gold", "Diamond", "Zamorak", "Emerald", "Ruby",
							"Divine", "Void"]
		self.weapon_frames = []
		self.create_weapon_frames()

	def create(self, level, weapon_type):
		pos = (randint(0, Settings().screen_width-128), randint(0, Settings().screen_height-128))
		rotation = randint(-360, 360)
		velocity = (uniform(-5, 5), uniform(-5, 5))
		name = self.weapon_levels[level] + " " + self.weapon_types[weapon_type]
		rect_center_offset = (16, 16)
		return WeaponAsset(pos,
							self.weapon_frames[level][weapon_type],
							rotation,
							rect_center_offset,
							velocity,
							name,
							level)

	def create_weapon_frames(self):
		for i, weapon_level in enumerate(self.weapon_levels):
			weapon_frames_for_level = []
			for y, weapon_types in enumerate(self.weapon_types):
				weapon_frames_for_level.append(self.construct_weapon_image(y, i))
			self.weapon_frames.append(weapon_frames_for_level)

	def construct_weapon_image(self, frame, level):
		scale = 2
		rotation = 0
		dim_x = 32
		dim_y = 32
		color_key = (0, 0, 0)
		return self.sprite_sheet.get_image(frame, level, dim_x, dim_y, scale, color_key, rotation)
