from .constructor_knights import Knight
from settings import Settings

from random import *


class AnimateKnight:
	def __init__(self, screen, level):
		# Set up animation variables
		self.settings = Settings()
		self.screen = screen
		self.level = level
		self.num_knights = 0
		self.animation_time = 0.1
		self.current_time = 0
		self.animation_frames = 3
		self.current_frame = 0
		self.knight = Knight(self.level, randint(0, 3), (randint(0, Settings().screen_width - 128), randint(0, Settings().screen_height - 128)))

		# Movement config
		self.step_increment = 20
		self.distance_traveled = 0
		self.min_travel_distance = 12

	def update_animation_frame(self, animation_dt, level):
		self.current_time += animation_dt
		self.level = level
		if self.current_time >= self.animation_time:
			self.current_time = 0
			self.current_frame += 1
			self.update_direction()
			self.update_position()
			self.update_level()
			if self.current_frame >= self.animation_frames:
				self.current_frame = 0
		self.knight.current_frame = self.current_frame
		self.render_knights()

	def update_level(self):
		if self.level != self.knight.level:
			self.knight.level = self.level
			self.knight.create_knight_animations()

	def update_position(self):
		x = self.knight.position[0]
		y = self.knight.position[1]

		# 0 is facing south/ forward
		if self.knight.direction == 0:
			y += self.step_increment

		# 1 is facing east/ right
		elif self.knight.direction == 1:
			x += self.step_increment

		# 2 is facing west/ left
		elif self.knight.direction == 2:
			x -= self.step_increment

		# 3 is facing north/ back
		elif self.knight.direction == 3:
			y -= self.step_increment

		self.distance_traveled += 1
		self.knight.position = (x, y)

	def update_direction(self):
		x = self.knight.position[0]
		y = self.knight.position[1]
		# Check bound boxes
		if x + self.step_increment >= self.settings.screen_width - 64:
			self.distance_traveled = 0
			self.knight.direction = 2
		elif x - self.step_increment <= 64:
			self.distance_traveled = 0
			self.knight.direction = 1

		elif y + self.step_increment >= self.settings.screen_height - 64:
			self.distance_traveled = 0
			self.knight.direction = 3
		elif y - self.step_increment <= 0:
			self.distance_traveled = 0
			self.knight.direction = 0

		# Weighted random direction change
		if self.distance_traveled >= self.min_travel_distance:
			rand = randint(0, 12) + self.distance_traveled
			if rand > self.step_increment / 1.5:
				self.distance_traveled = 0
				self.knight.direction = \
					randint(0, 3)

	def render_knights(self):
		self.screen.blit(self.knight.get_sprite(), self.knight.position)
