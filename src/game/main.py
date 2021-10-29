import sys

from .data.KnightAsset import *
from .data.WeaponAsset import *
from .CollisionDetection import CollisionDetection
from .SoundEngine import SoundEngine
from .Scoarboard import Scores
from ..settings import Settings


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

        # Initialize sound engine
        self.sound_engine = SoundEngine()

        # Default parameters TODO: move this and make changable with upgrades
        self.num_weapons = 300
        self.num_knights = 5

        # Setup scores and scoreboard
        self.scores = Scores()

        # Initialize weapon class
        self.weapon_factory = WeaponAssetFactory()
        self.weapons_to_render = []
        # Render initial amount of weapons on init
        for weapon_count in range(self.num_weapons):
            weapon_type = randint(0, 5)
            self.weapons_to_render.append(self.weapon_factory.create(self.scores.level, weapon_type))

        # Initialize knight class
        self.knight_factory = KnightAssetFactory()
        self.knights_to_render = []
        # Render initial amount of knights on init
        for knight_count in range(self.num_knights):
            self.knights_to_render.append(self.knight_factory.create(self.scores.level))

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

    def _update_screen(self):
        # Draw background layers each frame to 'reset' the screen
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.backgrounds[self.scores.level], (0, 0))

        # Render the scoreboard
        self.scores.render_scoreboard(self.screen)

        # Keep the weapons refilled on screen
        weapon_dif = self.num_weapons - len(self.weapons_to_render)
        for i in range(weapon_dif):
            self.weapons_to_render.append(self.weapon_factory.create(self.scores.level, randint(0, 5)))

        for weapon in self.weapons_to_render:
            weapon.update_asset_position_in_bounds()
            self.screen.blit(weapon.sprite, weapon.position)

        for knight in self.knights_to_render:
            knight.animate()
            self.screen.blit(knight.sprite, knight.position)

        CollisionDetection(self.scores, self.sound_engine, self.weapons_to_render, self.knights_to_render)

        pygame.display.update()
