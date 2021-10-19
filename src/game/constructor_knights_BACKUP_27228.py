import pygame
from . import spritesheet
from random import *
from settings import Settings


class Knight:
	def __init__(self, level, position=(100, 100)):
		# Each knight can have 4 directions, 0 -3
		self.sprites = {
			0: [],
			1: [],
			2: [],
			3: []
		}
		self.name = ''
		self.level = level

		self.position = position
		self.current_frame = 0
		self.direction = 0

		sprite_sheet_image = pygame.image.load('resources/assets/knights_sprite.png').convert_alpha()
		self.sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)
<<<<<<< HEAD:src/game/constructor_knights.py

		self.create_knight_animations()
=======
		self.level = int(round((level-1) / 3)*3)
>>>>>>> master:src/game/draw_knights.py

	def create_knight_animations(self):
		self.sprites = {
			0: [],
			1: [],
			2: [],
			3: []
		}
		for direction in range(4):
			for frame in range(3):
				self.sprites[direction].append(self.construct_knight_sprite(frame+int(round((self.level - 1) / 3) * 3), direction))

	def construct_knight_sprite(self, frame, direction):
		scale = 1
		dim_x = 75.8
		dim_y = 103.5
		color_key = (0, 0, 0)

		knight_image = self.sprite_sheet.get_image(frame, direction, dim_x, dim_y, scale, color_key)
		return knight_image

	def get_sprite(self):
		sprite = self.sprites[self.direction][self.current_frame]
		return sprite
