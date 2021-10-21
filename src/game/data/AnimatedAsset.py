from .Asset import *
import pygame
from ...settings import Settings


class AnimatedAsset(Asset):
	def __init__(self, position, sprite, rotation, rect_center_offset, velocity, animation_frames, animation_frames_len):
		super().__init__(position, sprite, rotation, rect_center_offset, velocity)

		"""Data needed to animate a sprite"""
		self.animation_dt = pygame.time.Clock().tick(Settings().FPS) / 1000
		self.animation_frames = animation_frames
		self.animation_frames_len = animation_frames_len
		self.animation_time = 0.1
		self.current_time = 0
		self.current_frame = 0

	def animate(self):
		self.update_asset_position()
		self.update_animation_frame()

	def update_animation_frame(self):
		self.current_time += self.animation_dt
		if self.current_time >= self.animation_time:
			self.current_time = 0
			self.current_frame += 1
			if self.current_frame >= self.animation_frames_len:
				self.current_frame = 0
