import pygame
from . import spritesheet
from random import *


class Weapon:
	def __init__(self, level, weapon_type, position=(0, 0), rotation=0):
		# sprite is pygame.surface
		self.sprite = None

		self.name = ''
		self.level = level
		self.weapon_type = weapon_type

		# Default position info
		self.position = position
		self.rotation = rotation

		# Load sprite sheed and parse with our SpriteSheet class
		sprite_sheet_image = pygame.image.load('resources/assets/weapons_sprite.png').convert_alpha()
		self.sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)

		self.create_weapon_class()

	def create_weapon_class(self):
		# Create all weapons types at the specified level
		weapon_types = ["Sword", "Halberd", "Staff", "Bow", "Shield", "Special"]
		weapon_levels = ["Wood", "Bronze", "Iron", "Steel", "Obsidian", "Gold", "Diamond", "Zamorak", "Emerald",
						"Ruby", "Divine", "Void"]

		self.sprite = self.construct_weapon_sprite(self.weapon_type)
		self.name = weapon_levels[self.level] + ' ' + weapon_types[self.weapon_type]

	def get_collision_rect(self):
		weapon_rect = self.sprite.get_rect()
		x = self.position[0] + 16
		y = self.position[1] + 16
		weapon_rect.center = (x, y)
		return weapon_rect

	def construct_weapon_sprite(self, image_loc):
		scale = 2
		rotation = randint(-360, 360)
		dim_x = 32
		dim_y = 32
		color_key = (0, 0, 0)

		weapon_sprite = self.sprite_sheet.get_image(image_loc, self.level, dim_x, dim_y, scale, color_key, rotation)
		return weapon_sprite
