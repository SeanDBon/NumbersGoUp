from .constructor_weapons import Weapon
from settings import Settings

from random import *


class AnimateWeapon:
	def __init__(self, screen, level, weapon_type):
		self.settings = Settings()
		self.screen = screen
		self.level = level

		# Velocity config and starts at random vector of movement
		velocity_max = 10
		velocity_min = -10
		self.vector_x = uniform(velocity_min, velocity_max)
		self.vector_y = uniform(velocity_min, velocity_max)

		# Generate a new weapon
		random_position = (randint(0, Settings().screen_width - 128), randint(0, Settings().screen_height - 128))
		self.weapon = Weapon(self.level, weapon_type, random_position)

	# This gets called on every render
	def update_animation_frame(self, level):
		self.level = level
		self.bounce_off_screen_bounds()
		self.update_level()
		self.render_weapon()

	def update_level(self):
		if self.level != self.weapon.level:
			self.weapon.level = self.level
			self.weapon.create_weapon_class()

	def bounce_off_screen_bounds(self):
		if 0 < self.weapon.position[0] < self.settings.screen_width - 64:
			vector_x_velocity = self.vector_x
			if vector_x_velocity > 0:
				vector_x_velocity -= .1
			elif vector_x_velocity < 0:
				vector_x_velocity += .1
			self.vector_x = vector_x_velocity
		else:
			self.vector_x = self.vector_x * -1.2

		if 0 < self.weapon.position[1] < self.settings.screen_height - 64:
			vector_y_velocity = self.vector_y
			if vector_y_velocity > 0:
				vector_y_velocity -= .1
			elif vector_y_velocity < 0:
				vector_y_velocity += .1
			self.vector_y = vector_y_velocity
		else:
			self.vector_y = self.vector_y * -1.2

		x = self.weapon.position[0] + self.vector_x
		y = self.weapon.position[1] + self.vector_y
		self.weapon.position = (x, y)

	def render_weapon(self):
		self.screen.blit(self.weapon.sprite, self.weapon.position)
