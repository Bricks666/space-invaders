from typing import Dict, List
from pygame import mixer, Surface, sprite, transform
from consts import BULLET_SIZE, LEVEL_HEIGHT, SCREEN_MARGIN, STEP, BulletType
from packages.core import Collidable


class Bullet(Collidable):
    __musics__: Dict[str, mixer.Sound] = {}
    __speed__: float

    def __init__(self, image: Surface, x: float, y: float, type: BulletType, groups: List[sprite.Group]) -> None:
        super().__init__(*groups)
        self.__musics__.get("shoot").set_volume(0.1)
        self.__musics__.get("shoot").play()
        self.__duration__ = type.value
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self) -> None:
        if self.__collide__():
            return

        if self.__is_out_of_screen__():
            self.kill()
            return
        self.rect.move_ip(0, self.__speed__ * self.__duration__)

    def __is_out_of_screen__(self) -> bool:
        return self.rect.y <= SCREEN_MARGIN or self.rect.y >= LEVEL_HEIGHT + SCREEN_MARGIN
