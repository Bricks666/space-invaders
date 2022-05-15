import pygame
from consts.main import BULLET_SIZE, LEVEL_HEIGHT, SCREEN_MARGIN, SPRITE_SIZE, STEP, BulletType
from entities.collidable import Collidable
from entities.sprite import Sprite


class Bullet(Collidable, Sprite):
    SHOOT: pygame.mixer.Sound

    def __init__(self, image: pygame.Surface, x: float, y: float, type: BulletType, *group):
        super().__init__(*group)
        Bullet.SHOOT.play()
        self.image = pygame.transform.scale(image, (BULLET_SIZE))
        self.rect = self.image.get_rect()
        self.__type__ = type
        self.rect.x = x
        self.rect.y = y

    def update(self):
        if self.__collide__():
            return

        if self.__is_out_of_screen__():
            self.kill()
            return
        self.rect.y += STEP * 4 * self.__type__.value

    def __is_out_of_screen__(self):
        return self.rect.y <= SCREEN_MARGIN - self.rect.height or self.rect.y >= LEVEL_HEIGHT + SCREEN_MARGIN
