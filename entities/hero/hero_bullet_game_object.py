from typing import List
from pygame import Surface, sprite
from consts import STEP
from ..bullet import Bullet, BulletType
from ..enemy import Enemy, EnemyBullet


class HeroBullet(Bullet):
    def __init__(self, image: Surface, x: float, y: float, groups: List[sprite.Group]) -> None:
        self.__velocity__ = STEP * 5 * BulletType.HERO.value
        super().__init__(image, x, y, self.__velocity__, groups)

    def __collide__(self) -> bool:
        for s in self.__collidable__.sprites():
            if s == self or not isinstance(s, (Enemy, EnemyBullet)):
                """
                Не дает застрелить себя или игрока
                """
                continue
            if sprite.collide_rect(self, s):
                s.kill()
                return True
        return False
