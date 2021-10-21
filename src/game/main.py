import sys

from .data.KnightAsset import *
from .data.WeaponAsset import *
from .detect_collision import CollisionDetection
from .sound_engine import SoundEngine
from ..settings import Settings


class NumbersGoUp:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Numbers Go Up")

        # Initialize sound engine
        self.sound_engine = SoundEngine()

        self.num_weapons = 200
        self.weapon_level = 4

        self.num_knights = 5

        self.animation_dt = 0

        self.weapon_factory = WeaponAssetFactory()
        self.weapons_to_render = []
        for weapon_count in range(self.num_weapons):
            weapon_type = randint(0, 5)
            self.weapons_to_render.append(self.weapon_factory.create(self.weapon_level, weapon_type))

        self.knight_factory = KnightAssetFactory()
        self.knights_to_render = []
        for knight_count in range(self.num_knights):
            self.knights_to_render.append(self.knight_factory.create(self.weapon_level))

        # Score trackers
        self.total_points = 0
        self.claimed_weapons = {}

        # Game balance modifiers
        self.next_level = 1000
        self.point_modifiers = [1, 1.5, 3, 7.5, 37.5, 281.25, 2812.5, 35156.25, 527343.75, 9228515.625]

        # Initialize font and set global default font
        pygame.font.init()
        self.my_font = pygame.font.SysFont('Futura', 50)

        """Background Images"""
        background1 = pygame.image.load('resources/images/mountains.png')
        # background2 = pygame.image.load('resources/images/ocean.jpg')
        self.backgrounds = []
        self.backgrounds.append(background1)
        # self.backgrounds.append(background2)
        for i in range(11):
            self.backgrounds.append(background1)

    def run_game(self):
        """Start the main loop for the game."""
        clock = pygame.time.Clock()

        while True:
            self.point_text = self.my_font.render("Points: " + str(self.total_points), False, (255, 255, 255))
            self.level_text = self.my_font.render("Level: " + str(self.weapon_level + 1), False, (255, 255, 255))
            clock.tick(self.settings.FPS)
            self.animation_dt = clock.tick(self.settings.FPS) / 1000  # Amount of seconds between each loop.
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # elif event.type == pygame.VIDEORESIZE:
            #     # There's some code to add back window content here.
            #         self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

    def _update_screen(self):
        # Draw background layers each frame to 'reset' the screen
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.backgrounds[self.weapon_level], (0, 0))
        # Level up TODO: make this a function
        if self.total_points > self.next_level:
            if self.weapon_level < 11:
                self.weapon_level += 1
                self.knights_to_render.append(self.knight_factory.create(self.weapon_level))
            self.next_level = self.next_level * 10

        # Keep the weapons refilled on screen
        weapon_dif = self.num_weapons - len(self.weapons_to_render)
        for i in range(weapon_dif):
            self.weapons_to_render.append(self.weapon_factory.create(self.weapon_level, randint(0, 5)))

        # Updates animation frames and allows movement
        for weapon in self.weapons_to_render:
            self.screen.blit(weapon.sprite, weapon.position)

        for knight in self.knights_to_render:
            knight.animate()
            self.screen.blit(knight.sprite, knight.position)

        CollisionDetection(self.sound_engine, self.weapons_to_render, self.knights_to_render)

        # Draw score boards
        self.screen.blit(self.point_text, (0, 0))
        self.screen.blit(self.level_text, (720, 0))

        pygame.display.update()
