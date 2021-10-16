import sys

import pygame
from random import *
from settings import Settings
from .draw_weapons import WeaponsLayer
from .draw_knights import KnightLayer
from pygame import mixer
import pygame.mixer

# Background Sound
pygame.mixer.init()
pygame.mixer.music.load('resources/music/Background.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(.009)

# Sound Effects


class LeafGame:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Numbers Go Up")

        self.num_weapons = 500
        self.weapon_level = 0

        # Create initial weapons layer (weapon level, weapon amount)
        self.weapons_to_render = WeaponsLayer(self.weapon_level, self.num_weapons).draw_weapons_layer()

        self.total_points = 0
        self.next_level = 100
        self.claimed_weapons = {}

        self.point_modifiers = [1, 1.5, 3, 7.5, 37.5, 281.25, 2812.5, 35156.25]

        pygame.font.init()
        self.my_font = pygame.font.SysFont('Futura', 50)

        """Background Images"""
        background1 = pygame.image.load('resources/images/mountains.png')
        #background2 = pygame.image.load('resources/images/ocean.jpg')
        self.backgrounds = []
        self.backgrounds.append(background1)
        #self.backgrounds.append(background2)
        for i in range(11):
            self.backgrounds.append(background1)

        """Sound Effects"""
        self.pickup_sound = mixer.Sound('resources/sounds/pickup.mp3')
        self.pickup_sound.set_volume(.05)

    def run_game(self):
        """Start the main loop for the game."""
        clock = pygame.time.Clock()

        while True:
            self.point_text = self.my_font.render("Points: " + str(self.total_points), False, (255, 255, 255))
            self.level_text = self.my_font.render("Level: " + str(self.weapon_level + 1), False, (255, 255, 255))
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

    def mouse_collision(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                for i, weapon in enumerate(self.weapons_to_render):
                    weapon_rect = weapon.image.get_rect()
                    x = weapon.position[0] + 16
                    y = weapon.position[1] + 16
                    weapon_rect.center = (x, y)
                    if weapon_rect.collidepoint(pygame.mouse.get_pos()):
                        self.pickup_sound.play()
                        self.total_points += ((weapon.level + 1) * self.point_modifiers[self.weapon_level]) * 10
                        claimed_weapon = self.weapons_to_render.pop(i)
                        print(self.claimed_weapons)
                        if claimed_weapon.name not in self.claimed_weapons.keys():
                            self.claimed_weapons[claimed_weapon.name] = 0
                        else:
                            self.claimed_weapons[claimed_weapon.name] += 1

    def bind_to_screen_x(self, weapon):
        return 0 < weapon.position[0] < self.settings.screen_width - 64

    def bind_to_screen_y(self, weapon):
        return 0 < weapon.position[1] < self.settings.screen_height - 64

    def _update_screen(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.backgrounds[self.weapon_level], (0, 0))
        if len(self.weapons_to_render) < (self.num_weapons * .8):
            self.weapons_to_render += \
                WeaponsLayer(self.weapon_level, self.num_weapons - len(self.weapons_to_render)).draw_weapons_layer()

        if self.total_points > self.next_level:
            if self.weapon_level < 11:
                self.weapon_level += 1
            self.next_level = self.next_level * 10

        for weapon in self.weapons_to_render:

            if self.bind_to_screen_x(weapon):
                vector_x_velocity = weapon.vector_x
                if vector_x_velocity > 0:
                    vector_x_velocity -= .1
                elif vector_x_velocity < 0:
                    vector_x_velocity += .1
                weapon.vector_x = vector_x_velocity
            else:
                weapon.vector_x = weapon.vector_x * -1.2

            if self.bind_to_screen_y(weapon):
                vector_y_velocity = weapon.vector_y
                if vector_y_velocity > 0:
                    vector_y_velocity -= .1
                elif vector_y_velocity < 0:
                    vector_y_velocity += .1
                weapon.vector_y = vector_y_velocity
            else:
                weapon.vector_y = weapon.vector_y * -1.2

            x = weapon.position[0] + weapon.vector_x
            y = weapon.position[1] + weapon.vector_y
            weapon.position = (x, y)

            self.screen.blit(weapon.image, weapon.position)
        self.mouse_collision()

        self.screen.blit(self.point_text, (0, 0))
        self.screen.blit(self.level_text, (720, 0))

        knight_to_render = KnightLayer(0).create_knight_animations()
        """knight_to_render.sprites[direction][animation frame]"""
        self.screen.blit(knight_to_render.sprites[0][0], (128, 260))
        self.screen.blit(knight_to_render.sprites[0][1], (196, 260))
        self.screen.blit(knight_to_render.sprites[0][2], (256, 260))

        knight_to_render = KnightLayer(3).create_knight_animations()
        self.screen.blit(knight_to_render.sprites[1][0], (128, 360))
        self.screen.blit(knight_to_render.sprites[1][1], (196, 360))
        self.screen.blit(knight_to_render.sprites[1][2], (256, 360))

        knight_to_render = KnightLayer(6).create_knight_animations()
        self.screen.blit(knight_to_render.sprites[2][0], (128, 460))
        self.screen.blit(knight_to_render.sprites[2][1], (196, 460))
        self.screen.blit(knight_to_render.sprites[2][2], (256, 460))

        knight_to_render = KnightLayer(9).create_knight_animations()
        self.screen.blit(knight_to_render.sprites[3][0], (128, 560))
        self.screen.blit(knight_to_render.sprites[3][1], (196, 560))
        self.screen.blit(knight_to_render.sprites[3][2], (256, 560))

        pygame.display.update()
