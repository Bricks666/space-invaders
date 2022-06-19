from time import time
from typing import Dict, List, Tuple
from pygame import transform, Surface, mixer, sprite
from consts import FIRE_COOLDOWN,  LEVEL_WIDTH, SCREEN_MARGIN, SPRITE_SIZE, STEP, BulletType
from entities.bullet import Bullet
from packages.core import Entity, Direction
from stores.lives import LivesStore
from packages.inject import Injector


@Injector.inject(LivesStore, "__lives__")
class Hero(Entity):
    """
    Класс игрока
    """
    __lives__: LivesStore
    """
    Хранилище жизней
    """
    __start_position__: Tuple[float, float]
    """
    Стартовая позиция игрока, нужна для респауна после смерти
    """
    __last_fire__: float
    """
    Время последнего выстрела, нужно для ограничения скорострельности
    """

    def __init__(self, x: float, y: float, groups: List[sprite.Group]) -> None:
        super().__init__(*groups)
        self.image = self.__images__.get("hero")

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.__start_position__ = (x, y)
        self.__velocity__ = STEP

        self.__last_fire__ = time()

    def update(self) -> None:
        if self.__collide__():
            return
        return super().update()

    def kill(self) -> None:
        self.__lives__.decrement_lives()
        """
        Уменьшение количества жизней
        """
        self.__musics__.get("explosion").play().set_volume(0.2)

        if not self.__lives__.get_lives():
            """
            Окончательная смерть, если жизней больше нет
            """
            return super().kill()

        self.rect.move(self.__start_position__)

    def move(self, direction: Direction) -> None:
        if self.__can_move__(direction):
            self.rect.move_ip(self.__velocity__ * direction.value, 0)

    def fire(self) -> None:
        current_time = time()
        groups = self.groups()
        groups.pop()
        """
        Нужно так как враг состоит в группе всех спрайтов сцены,
        объектов для коллизии и отдельной группы врагов
        Она самая последняя и в нее не нужно добавлять пулю
        """
        if self.__last_fire__ + FIRE_COOLDOWN <= current_time:
            HeroBullet(self.__images__.get("hero_bullet"), self.rect.centerx, self.rect.y + 64 - 39,
                       groups)
            """
            64-39 так как граница спрайта находится выше границы модели.
            Такое вычитание позволяет запускать пулю с визуальной границы
            """
            self.__last_fire__ = current_time

    def __can_move__(self, direction: Direction) -> bool:
        match direction:
            case Direction.LEFT:
                return self.rect.x > SCREEN_MARGIN
            case Direction.RIGHT:
                return self.rect.x < LEVEL_WIDTH + SCREEN_MARGIN - SPRITE_SIZE

    def __collide__(self) -> bool:
        return super().__collide__()


class HeroBullet(Bullet):
    def __init__(self, image: Surface, x: float, y: float, groups: List[sprite.Group]) -> None:
        self.__velocity__ = STEP * 5 * BulletType.HERO.value
        super().__init__(image, x, y, self.__velocity__, groups)

    def __collide__(self) -> bool:
        for s in self.__collidable__.sprites():
            if s == self or isinstance(s, (Hero, HeroBullet)):
                """
                Не дает застрелить себя или игрока
                """
                continue
            if sprite.collide_rect(self, s):
                s.kill()
                return True
        return False
