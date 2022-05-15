import pygame
from consts.main import SPRITE_SIZE, STEP, BulletType
from entities.collidable import Collidable


class Bullet(Collidable):
    def __init__(self, image: pygame.Surface, x: float, y: float, type: BulletType, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(image, (SPRITE_SIZE, SPRITE_SIZE))
        self.rect = self.image.get_rect()
        self.__type__ = type
        self.rect.x = x
        self.rect.y = y

    def update(self):
        is_collided = self.__collide__()
        print(is_collided, self)
        if is_collided:
            return
        self.rect.y += STEP * 4 * self.__type__.value
