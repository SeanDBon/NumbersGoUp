import pygame


class Asset:
    """Everything that displays on the screen from a sprite image."""
    def __init__(self, position, sprite, rotation, rect_center_offset, velocity):

        """Position on screen of the asset. (x, y)"""
        self.position = position

        """How far its supposed to move on X/Y axis."""
        self.x_velocity = velocity[0]
        self.y_velocity = velocity[1]

        """A sprite is a @pygame.surface, usually generated from a sprite sheet via @SpriteSheet."""
        self.sprite = pygame.transform.rotate(sprite, rotation)

        """The rotation of the asset on scree, -360 - 360. Positive is clockwise."""
        self.rotation = rotation

        """The center point of the asset on screen."""
        self.rect_center_offset = rect_center_offset

    def get_collision_rect(self):
        sprite_rect = self.sprite.get_rect()
        x_offset = self.position[0] + self.rect_center_offset[0]
        y_offset = self.position[1] + self.rect_center_offset[1]
        sprite_rect.center = (x_offset, y_offset)
        return sprite_rect

    def update_asset_position(self):
        x_vector = self.position[0] + self.x_velocity
        y_vector = self.position[1] + self.y_velocity
        self.position = (x_vector, y_vector)

