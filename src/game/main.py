import sys

import pygame

from settings import Settings
from .draw_weapons import WeaponsLayer


class LeafGame:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Numbers Go Up")

        self.num_weapons = 300
        self.weapon_level = 0

        # Create initial weapons layer (weapon level, weapon amount)
        self.weapons_to_render = WeaponsLayer(self.weapon_level, self.num_weapons).draw_weapons_layer()

        self.total_points = 0
        self.next_level = 1000

        pygame.font.init()
        self.my_font = pygame.font.SysFont('Comic Sans MS', 30)
        self.text_surface = self.my_font.render(str(self.total_points), False, (100, 0, 0))

    def run_game(self):
        """Start the main loop for the game."""
        clock = pygame.time.Clock()

        while True:
            self.text_surface = self.my_font.render(str(self.total_points), False, (100, 0, 0))
            clock.tick(self.settings.FPS)
            self._check_events()
            self._update_screen()

    @staticmethod
    def _check_events():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

    @staticmethod
    def can_move(weapon, max_dist):
        return (abs(weapon.start_position[0] - weapon.position[0]) < max_dist) and (
                abs(weapon.start_position[0] + weapon.position[0]) > max_dist) and \
                (abs(weapon.start_position[1] - weapon.position[1]) < max_dist) and (
                abs(weapon.start_position[1] + weapon.position[1]) > max_dist)

    def mouse_collision(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                for i, weapon in enumerate(self.weapons_to_render):
                    weapon_rect = weapon.image.get_rect()
                    x = weapon.position[0] + 16
                    y = weapon.position[1] + 16
                    weapon_rect.center = (x, y)
                    if weapon_rect.collidepoint(pygame.mouse.get_pos()):
                        self.total_points += (weapon.level + 1) * 10
                        self.weapons_to_render.pop(i)
                        print(self.total_points)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        if len(self.weapons_to_render) < 250:
            self.weapons_to_render += \
                WeaponsLayer(self.weapon_level, self.num_weapons - len(self.weapons_to_render)).draw_weapons_layer()

        if self.total_points > self.next_level:
            self.weapon_level += 1
            self.next_level = self.next_level * 10

        for weapon in self.weapons_to_render:
            if self.can_move(weapon, 300):
                x = weapon.position[0] + weapon.vector_x
                y = weapon.position[1] + weapon.vector_y
                weapon.position = (x, y)

            self.screen.blit(weapon.image, weapon.position)
            self.mouse_collision()
            self.screen.blit(self.text_surface, (0, 0))

        pygame.display.update()
