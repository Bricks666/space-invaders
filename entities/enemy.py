from time import time
from typing import Dict, List
from pygame import Surface, mixer, transform, sprite
from entities.bullet import Bullet
from packages.core import Collidable
from packages.inject import Inject
from stores.scores import ScoresStore
from utils.loaders import sprite_loader
from consts import LEVEL_WIDTH, SCREEN_MARGIN, SPRITE_SIZE, BulletType,  Direction


@Inject(ScoresStore, "__scores__")
class Enemy(Collidable):
    __injected__: Dict[str, object]
    __scores__: ScoresStore
    IMAGE: Surface = sprite_loader.load("enemy.png")
    BULLET: Surface = sprite_loader.load("enemy_bullet.png")
    DURATION: float = 0.5
    DESTROY: mixer.Sound

    def __init__(self, x: float, y: float, number: int, total_count: int, groups: List[sprite.Group], score: int = 50) -> None:
        super().__init__(*groups)
        self.image = transform.scale(
            Enemy.IMAGE, (SPRITE_SIZE * 0.7, SPRITE_SIZE * 0.7))
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
        current_time = time()
        can_move = self.__can_move__(current_time)
        if not can_move:
            return
        self.__last_move__ = current_time
        if self.__end__:
            self.__change_direction__()
            self.__down__()
        self.rect.x += SPRITE_SIZE / 4 * self.__direction__.value
        self.__end__ = self.__check_end__()

    def fire(self) -> None:
        groups = self.groups()
        groups.pop()
        EnemyBullet(Enemy.BULLET, self.rect.centerx,
                    self.rect.y + self.rect.height, groups)

    def kill(self) -> None:
        Enemy.DESTROY.play()
        self.__scores__.add(self.__score__)
        return super().kill()

    def __check_end__(self) -> bool:
        return self.rect.x <= SCREEN_MARGIN + self.__offset_left__ or self.rect.x >= LEVEL_WIDTH + SCREEN_MARGIN - self.__offset_right__

    def __change_direction__(self) -> None:
        self.__direction__ = Direction.RIGHT if self.__direction__ == Direction.LEFT else Direction.LEFT
        self.__end__ = False

    def __can_move__(self, current_time) -> bool:
        return self.__last_move__ + Enemy.DURATION <= current_time

    def __down__(self) -> None:
        self.rect.y += SPRITE_SIZE / 2

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
