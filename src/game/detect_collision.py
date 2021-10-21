import pygame


class CollisionDetection:
	def __init__(self, weapon_objects, knight_objects):
		self.weapon_objects = weapon_objects
		self.knight_objects = knight_objects

	# Check if weapons collide with the cursor or a knight
	def check_weapon_collisions(self):
		for i, weapon in enumerate(self.weapon_objects):
			weapon_rect = weapon.weapon.get_collision_rect()
			if weapon_rect.collidepoint(pygame.mouse.get_pos()):
				self.weapon_collided(i)
			for knight in self.knight_objects:
				if weapon_rect.colliderect(knight.knight.get_collision_rect()):
					self.weapon_collided(i)

	def weapon_collided(self, i):
		claimed_weapon = self.weapon_objects.pop(i)

		# self.pickup_sound.play()
		# self.total_points += ((weapon.level + 1) * self.point_modifiers[self.weapon_level]) * 10
		# print(self.claimed_weapons)
		# if claimed_weapon.weapon.name not in self.claimed_weapons.keys():
		# 	self.claimed_weapons[claimed_weapon.weapon.name] = 0
		# else:
		# 	self.claimed_weapons[claimed_weapon.weapon.name] += 1