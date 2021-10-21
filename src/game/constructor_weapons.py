import pygame
from . import spritesheet
from random import *
from settings import Settings


class Weapon:

	def __init__(self, position=(0, 0)):
		self.image = None
		self.name = ''

		self.level = None

		self.position = position
		self.rotation = randint(-360, 360)

		velocity_max = 10
		velocity_min = -10
		self.vector_x = uniform(velocity_min, velocity_max)
		self.vector_y = uniform(velocity_min, velocity_max)

	def get_collision_rect(self):
		weapon_rect = self.image.get_rect()
		x = self.position[0] + 16
		y = self.position[1] + 16
		weapon_rect.center = (x, y)
		return weapon_rect


class WeaponsLayer:
	def __init__(self, level, clutter_amount):
		sprite_sheet_image = pygame.image.load('resources/assets/weapons_sprite.png').convert_alpha()
		self.sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)
		self.level = level
		self.clutter_amount = clutter_amount

	def draw_weapons_layer(self):
		weapons_layer = []
		weapon_types = ["Sword", "Halberd", "Staff", "Bow", "Shield", "Special"]
		weapon_levels = ["Wood", "Bronze", "Iron", "Steel", "Obsidian", "Gold", "Diamond", "Zamorak", "Emerald", "Ruby",
						"Divine", "Void"]

		clutter = 0
		while clutter < self.clutter_amount:
			for weapon_num in range(6):
				clutter += 1
				image_loc = weapon_num
				weapon = Weapon((randint(0, Settings().screen_width-128), randint(0, Settings().screen_height-128)))
				weapon.image = self.construct_weapon_image(image_loc)
				weapon.name = weapon_levels[self.level] + ' ' + weapon_types[weapon_num]
				weapon.level = self.level
				weapons_layer.append(weapon)

		return weapons_layer

	def construct_weapon_image(self, image_loc):
		scale = 2
		rotation = randint(-360, 360)
		dim_x = 32
		dim_y = 32
		color_key = (0, 0, 0)

		weapon_image = self.sprite_sheet.get_image(image_loc, self.level, dim_x, dim_y, scale, color_key, rotation)
		return weapon_image
