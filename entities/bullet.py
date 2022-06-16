import pygame
from consts import BULLET_SIZE, LEVEL_HEIGHT, SCREEN_MARGIN, SPRITE_SIZE, STEP, BulletType
from packages.core import Collidable


class Bullet(Collidable):
    SHOOT: pygame.mixer.Sound

    def __init__(self, image: pygame.Surface, x: float, y: float, type: BulletType, *group) -> None:
        super().__init__(*group)
        Bullet.SHOOT.play()
        self.image = pygame.transform.scale(image, (BULLET_SIZE))
        self.rect = self.image.get_rect()
        self.__type__ = type
        self.rect.x = x
        self.rect.y = y

    def update(self) -> None:
        if self.__collide__():
            return

        if self.__is_out_of_screen__():
            self.kill()
            return
        self.rect.y += STEP * 4 * self.__type__.value

    def __is_out_of_screen__(self) -> bool:
        return self.rect.y <= SCREEN_MARGIN or self.rect.y >= LEVEL_HEIGHT + SCREEN_MARGIN
