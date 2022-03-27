import sys

import pygame.display
import pygame.image

from .data.KnightAsset import *
from .data.WeaponAsset import *
from .data.LootSackAsset import *
from .CollisionDetection import CollisionDetection
from .SoundEngine import SoundEngine
from .Scoreboard import Scores
from ..menu.KnightMenu import *
from ..menu.WeaponMenu import *
from ..menu.PauseMenu import *


class NumbersGoUp:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create resources."""
        pygame.init()
        pygame.display.set_caption("Numbers Go Up")

        # Load default settings
        self.settings = Settings()

        # Set up screen (very important)
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        # Setup scores and scoreboard
        self.scores = Scores()

        # This bitch be running
        self.this_bitch_be_running = True

        # weapon icon button
        self.weapon_menu_button = Button('weapon_menu_icon.png', (5, 1025), 0, (24.99, 24.99), 600, 600, 0.0833,
                                         self.weapon_menu_button_callback)
        # knight icon button
        self.knight_menu_button = Button('knight_menu_icon.png', (65, 1025), 0, (24.99, 24.99), 600, 600, 0.0833,
                                         self.knight_menu_button_callback)
        self.is_weapon_menu_showing = False
        self.weapon_menu = WeaponMenu(self.screen, self.scores)

        self.is_knight_menu_showing = False
        self.knight_menu = KnightMenu(self.screen, self.scores)

        # Initialize sound engine
        self.sound_engine = SoundEngine()

        # Default parameters TODO: move this and make changeable with upgrades
        self.num_weapons = 300

        # Show game menu
        self.pause_menu = PauseMenu(self.screen, self.this_bitch_be_running)

        # Setup loot sack
        self.loot_sack = LootSackAsset(1)

        # Initialize weapon class
        self.weapon_factory = WeaponAssetFactory()
        self.weapons_to_render = []

        # Render initial amount of weapons on init
        for weapon_count in range(self.scores.num_weapons):
            weapon_type = randint(0, 5)
            self.weapons_to_render.append(self.weapon_factory.create(self.scores.level, weapon_type))

        # Initialize knight class
        self.knight_factory = KnightAssetFactory()
        self.knights_to_render = []
        # Render initial amount of knights on init
        for knight_count in range(self.scores.num_knights):
            self.knights_to_render.append(self.knight_factory.create(self.scores.knight_level))

        """Background Images"""
        background1 = pygame.image.load('resources/assets/mountains.png')
        # background2 = pygame.image.load('resources/assets/ocean.jpg')
        self.backgrounds = []
        self.backgrounds.append(background1)
        # self.backgrounds.append(background2)
        for i in range(11):
            self.backgrounds.append(background1)

    def weapon_menu_button_callback(self):
        self.is_knight_menu_showing = False
        self.is_weapon_menu_showing = not self.is_weapon_menu_showing

    def knight_menu_button_callback(self):
        self.is_weapon_menu_showing = False
        self.is_knight_menu_showing = not self.is_knight_menu_showing

    def run_game(self):
        """Start the main loop for the game."""
        clock = pygame.time.Clock()
        self.sound_engine.play_music("background_1");

        while self.this_bitch_be_running:
            clock.tick(self.settings.FPS)
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                elif event.key == pygame.K_ESCAPE:
                    self.pause_menu.is_game_menu_showing = not self.pause_menu.is_game_menu_showing

    def _update_screen(self):
        # Draw background layers each frame to 'reset' the screen
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.backgrounds[self.scores.level], (0, 0))

        # Render the scoreboard
        self.scores.render_scoreboard(self.screen)

        # Keep the weapons refilled on screen
        if len(self.weapons_to_render) <= (self.scores.num_weapons / 2):
            weapon_dif = self.scores.num_weapons - len(self.weapons_to_render)
            for i in range(weapon_dif):
                self.weapons_to_render.append(self.weapon_factory.create(self.scores.weapon_level, randint(0, 5)))

        # Update number of knights on screen
        knight_dif = self.scores.num_knights - len(self.knights_to_render)
        for i in range(knight_dif):
            self.knights_to_render.append(self.knight_factory.create(self.scores.knight_level))

        for weapon in self.weapons_to_render:
            if not self.pause_menu.is_game_menu_showing:
                weapon.update_asset_position_in_bounds()
            self.screen.blit(weapon.sprite, weapon.position)

        for knight in self.knights_to_render:
            if not self.pause_menu.is_game_menu_showing:
                knight.animate()
                if knight.level != self.scores.knight_level:
                    knight.update_level(self.scores.knight_level)
            self.screen.blit(knight.sprite, knight.position)

        if not self.pause_menu.is_game_menu_showing:
            CollisionDetection(self.scores, self.sound_engine, self.weapons_to_render, self.knights_to_render, self.loot_sack)
        self.screen.blit(self.loot_sack.sprite, self.loot_sack.position)
        if self.pause_menu.is_game_menu_showing:
            self.pause_menu.render_menu()

        self.screen.blit(self.weapon_menu_button.sprite, (5, 1025))
        self.screen.blit(self.knight_menu_button.sprite, (65, 1025))
        self.weapon_menu_button.check_for_click()
        if self.is_weapon_menu_showing:
            self.weapon_menu.render_menu()
        self.knight_menu_button.check_for_click()
        if self.is_knight_menu_showing:
            self.knight_menu.render_menu()

        pygame.display.update()
