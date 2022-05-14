import pygame
from consts.main import SPRITE_SIZE, STEP, BulletType

from utils.sprite_loader import SpriteLoader


class Bullet(pygame.sprite.Sprite):
    def __init__(self, image: pygame.Surface, x: float, y: float, type: BulletType, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(image, (SPRITE_SIZE, SPRITE_SIZE))
        self.rect = self.image.get_rect()
        self.__type = type
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.y += STEP * 8 * self.__type.value
        pass


class HeroBullet(Bullet):
    IMAGE = SpriteLoader.load("hero_bullet.png")

    def __init__(self, x: float, y: float, *group):
        super().__init__(HeroBullet.IMAGE, x, y, BulletType.HERO, *group)
        pass
