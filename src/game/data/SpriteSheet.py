import pygame


class SpriteSheet:
	def __init__(self, image):
		self.sheet = image

	def get_image(self, frame, level, width, height, scale, colour, rotation=0):
		image = pygame.Surface((width, height)).convert()
		image.blit(self.sheet, (0, 0), ((frame * width), (level * height), width, height))
		image = pygame.transform.scale(image, (width * scale, height * scale))
		image = pygame.transform.rotate(image, rotation)
		image.set_colorkey(colour)

		return image
