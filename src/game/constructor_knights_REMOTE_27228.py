import pygame
from . import spritesheet
from random import *
from settings import Settings


class Knight:
	def __init__(self, position=(0, 0)):
		self.sprites = {
			0: [],
			1: [],
			2: [],
			3: []
		}
		self.name = ''

		self.level = None

		self.position = position
		self.direction = 0

		velocity_max = 4
		velocity_min = -4
		self.vector_x = uniform(velocity_min, velocity_max)
		self.vector_y = uniform(velocity_min, velocity_max)


class KnightLayer:
	def __init__(self, level):
		sprite_sheet_image = pygame.image.load('resources/assets/knights_sprite.png').convert_alpha()
		self.sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)
		self.level = int(round((level-1) / 3)*3)

	def create_knight_animations(self):
		knight = Knight((randint(0, Settings().screen_width - 128), randint(0, Settings().screen_height - 128)))
		knight.level = self.level
		for direction in range(4):
			for frame in range(3):
				knight.sprites[direction].append(self.construct_knight_sprite(frame+self.level, direction))
		return knight
# Lvl 0 frames 0-2
# Lvl 1 frames 3-5
# Lvl 2 frames 6-8
# Lvl 3 frames 9-11

	def construct_knight_sprite(self, frame, direction):
		scale = 1
		dim_x = 75.8
		dim_y = 108
		color_key = (0, 0, 0)

		knight_image = self.sprite_sheet.get_image(frame, direction, dim_x, dim_y, scale, color_key)
		return knight_image
