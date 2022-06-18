from time import time
from typing import Dict, List
from pygame import Surface, mixer, transform, sprite
from entities.bullet import Bullet
from packages.core import Direction, Entity
from packages.inject import Injector
from stores.scores import ScoresStore
from consts import LEVEL_WIDTH, SCREEN_MARGIN, SPRITE_SIZE, BulletType


@Injector.inject(ScoresStore, "__scores__")
class Enemy(Entity):
    __injected__: Dict[str, object]
    __scores__: ScoresStore
    DURATION: float = 0.5

    def __init__(self, x: float, y: float, number: int, total_count: int, groups: List[sprite.Group], score: int = 50) -> None:
        super().__init__(*groups)
        self.image = transform.scale(
            Enemy.__images__.get("enemy"), (SPRITE_SIZE * 0.7, SPRITE_SIZE * 0.7))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.__offset_right__ = SPRITE_SIZE * (total_count - number)
        self.__offset_left__ = SPRITE_SIZE * number

        self.__direction__ = Direction.LEFT

        self.__end__ = False

        self.__last_move__ = time()

        self.__score__ = score

        self.__scores__ = self.__injected__.get("__scores__")

    def update(self) -> None:
        if self.__collide__():
            return

        return super().move()

    def fire(self) -> None:
        groups = self.groups()
        groups.pop()
        EnemyBullet(self.__images__.get("enemy_bullet"), self.rect.centerx,
                    self.rect.y + self.rect.height, groups)

    def move(self) -> None:
        current_time = time()
        if not self.__can_move__(current_time):
            return

        self.__last_move__ = current_time

        if self.__end__:
            self.__change_direction__()
            self.rect.move_ip(0, SPRITE_SIZE / 2)
            return

        self.rect.move_ip(SPRITE_SIZE / 4 * self.__direction__.value, 0)
        self.__end__ = self.__check_end__()

    def kill(self) -> None:
        self.__musics__.get("destroy").play()
        self.__scores__.add(self.__score__)
        return super().kill()

    def __check_end__(self) -> bool:
        return self.rect.x <= SCREEN_MARGIN + self.__offset_left__ or self.rect.x >= LEVEL_WIDTH + SCREEN_MARGIN - self.__offset_right__

    def __change_direction__(self) -> None:
        self.__direction__ = Direction.RIGHT if self.__direction__ == Direction.LEFT else Direction.LEFT
        self.__end__ = False

    def __can_move__(self, current_time: float) -> bool:
        return self.__last_move__ + self.DURATION <= current_time



    def __collide__(self) -> bool:
        return super().__collide__()


class EnemyBullet(Bullet):
    def __init__(self, image: Surface, x: float, y: float, groups: List[sprite.Group]) -> None:
        super().__init__(image, x, y, BulletType.ENEMY, groups)

    def __collide__(self) -> bool:
        for s in self.__collidable__.sprites():
            if s == self or isinstance(s, (Enemy, EnemyBullet)):
                continue
            if sprite.collide_rect(self, s):
                self.kill()
                s.kill()
                return True
        return False
