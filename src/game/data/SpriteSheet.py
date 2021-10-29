import pygame


class SpriteSheet:
	def __init__(self, image_name):
		self.sheet = pygame.image.load('resources/assets/' + image_name).convert_alpha()

	def get_image(self, frame=0, level=0, width=32, height=32, scale=1, color=(0, 0, 0), rotation=0):
		image = pygame.Surface((width, height)).convert()
		image.blit(self.sheet, (0, 0), ((frame * width), (level * height), width, height))
		image = pygame.transform.scale(image, (width * scale, height * scale))
		image = pygame.transform.rotate(image, rotation)
		image.set_colorkey(color)

		return image
