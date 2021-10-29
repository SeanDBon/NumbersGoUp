import pygame


class CollisionDetection:
	def __init__(self, scores, sound_engine, weapon_objects, knight_objects):
		self.scores = scores
		self.sound_engine = sound_engine
		self.weapon_objects = weapon_objects
		self.knight_objects = knight_objects

		self.check_weapon_collisions()

	# Check if weapons collide with the cursor or a knight
	def check_weapon_collisions(self):
		for i, weapon in enumerate(self.weapon_objects):
			collided = False
			weapon_rect = weapon.get_collision_rect()
			if weapon_rect.collidepoint(pygame.mouse.get_pos()):
				collided = True
			else:
				for knight in self.knight_objects:
					if weapon_rect.colliderect(knight.get_collision_rect()):
						collided = True
			if collided:
				self.weapons_collided(i)

	def weapons_collided(self, weapon):
		claimed_weapon = self.weapon_objects.pop(weapon)
		self.scores.claim_weapon(claimed_weapon)
		self.sound_engine.play_sound_effect('pickup')

		# self.total_points += ((weapon.level + 1) * self.point_modifiers[self.weapon_level]) * 10
		# print(self.claimed_weapons)
		# if claimed_weapon.weapon.name not in self.claimed_weapons.keys():
		# 	self.claimed_weapons[claimed_weapon.weapon.name] = 0
		# else:
		# 	self.claimed_weapons[claimed_weapon.weapon.name] += 1
