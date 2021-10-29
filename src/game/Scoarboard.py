import pygame


class Scores:
	def __init__(self, load_save=None):
		self.level = 0
		self.total_points = 0
		self.claimed_weapons = {}

		# Game balance modifiers
		self.next_level = 1000
		self.next_level_modifier = 10
		self.point_modifiers = {
			0: 1,
			1: 1.5,
			2: 3,
			3: 7.5,
			4: 37.5,
			5: 281,
			6: 2812,
			7: 35156,
			8: 527343,
			9: 9228515,
			10: 1000000,
			11: 1500000}

		# Initialize font and set global default font
		pygame.font.init()
		self.font = pygame.font.SysFont('Futura', 50)

	def load_save(self):
		pass

	def save_game(self):
		pass

	def claim_weapon(self, claimed_weapon):
		if claimed_weapon.name not in self.claimed_weapons.keys():
			self.claimed_weapons[claimed_weapon.name] = 0
		else:
			self.claimed_weapons[claimed_weapon.name] += 1
		self.total_points += ((claimed_weapon.level + 1) * self.point_modifiers[claimed_weapon.level]) * 10

	def level_up(self):
		if self.total_points > self.next_level:
			if self.level < 11:
				self.level += 1
			self.next_level = self.next_level * 10

	def render_scoreboard(self,screen):
		self.level_up()
		# Draw score boards
		point_text = self.font.render("Points: " + str(self.total_points), False, (255, 255, 255))
		level_text = self.font.render("Level: " + str(self.level + 1), False, (255, 255, 255))
		screen.blit(point_text, (0, 0))
		screen.blit(level_text, (720, 0))
