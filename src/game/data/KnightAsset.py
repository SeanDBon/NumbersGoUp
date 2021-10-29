from .AnimatedAsset import *
from .SpriteSheet import *
from random import *
from ...settings import Settings


class KnightAsset(AnimatedAsset):
	def __init__(self, sprite, position, rotation, rect_center_offset, velocity, animation_frames, animation_frames_len,
					direction, name, level):
		super().__init__(sprite, position, rotation, rect_center_offset, velocity, animation_frames, animation_frames_len)

		self.direction = direction
		self.level = level
		self.name = name
		self.step_increment = 3
		self.distance_traveled = 0
		self.min_travel_distance = 50
		self.settings = Settings()

	def animate(self):
		self.sprite = self.animation_frames[self.level][self.direction][self.current_frame]
		self.update_animation_frame()
		self.update_asset_position()
		self.update_position()
		self.update_direction()

	def update_position(self):
		x = self.position[0]
		y = self.position[1]
		# 0 is facing south/ forward
		if self.direction == 0:
			y += self.step_increment
		# 1 is facing east/ right
		elif self.direction == 1:
			x += self.step_increment
		# 2 is facing west/ left
		elif self.direction == 2:
			x -= self.step_increment
		# 3 is facing north/ back
		elif self.direction == 3:
			y -= self.step_increment
		self.position = (x, y)

	def update_direction(self):
		x = self.position[0]
		y = self.position[1]
		# Check bound boxes
		if x + self.step_increment >= self.settings.screen_width - 70:
			self.distance_traveled = 0
			self.direction = 2
		elif x - self.step_increment <= 0:
			self.distance_traveled = 0
			self.direction = 1
		elif y + self.step_increment >= self.settings.screen_height - 103.5:
			self.distance_traveled = 0
			self.direction = 3
		elif y - self.step_increment <= 20:
			self.distance_traveled = 0
			self.direction = 0


class KnightAssetFactory:
	def __init__(self):
		self.sprite_sheet = SpriteSheet('knights_sprite.png')
		self.animation_frames = []
		self.create_knight_animations()

	def create(self, level):
		velocity = (0, 0)
		direction = randint(0, 3)
		position = (randint(0, Settings().screen_width-128), randint(0, Settings().screen_height-128))
		rotation = 0
		rect_center_offset = (0, 5)
		animation_frames_len = len(self.animation_frames[level][0])
		return KnightAsset(self.animation_frames[level][direction][1],
							position,
							rotation,
							rect_center_offset,
							velocity,
							self.animation_frames,
							animation_frames_len,
							direction,
							"Knight",
							level)

	def create_knight_animations(self):
		for i in range(11):
			animation_frames = {
				0: [],
				1: [],
				2: [],
				3: []
			}
			for direction in range(4):
				for frame in range(3):
					image_frame = frame+int(round((i - 1) / 3) * 3)
					animation_frames[direction].append(self.sprite_sheet.get_image(frame=image_frame,
																					level=direction,
																					width=75.8,
																					height=103.5,
																					scale=1))
			self.animation_frames.append(animation_frames)
