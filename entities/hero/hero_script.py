from typing import Tuple
from time import time
from pygame import key, K_SPACE, K_LEFT, K_RIGHT, K_d, K_a
from packages.core.script import Script
from packages.core.entity import Direction
from packages.core.math import VectorLike
from packages.inject import Injector
from stores.lives import LivesStore
from consts import SCREEN_MARGIN, LEVEL_WIDTH, SPRITE_SIZE, STEP, FIRE_COOLDOWN
from .hero_bullet_game_object import HeroBullet
from .hero_game_object import *


@Injector.inject(LivesStore, "_lives")
class HeroScript(Script["Hero"]):
    """
    Класс игрока
    """
    _lives: LivesStore
    """
    Хранилище жизней
    """
    _start_position: Tuple[float, float]
    """
    Стартовая позиция игрока, нужна для респауна после смерти
    """
    _last_fire: float
    """
    Время последнего выстрела, нужно для ограничения скорострельности
    """
    _velocity: float

    def activate(self, *args, **kwargs):
        self._start_position = (
            self._game_object.start_x, self._game_object.start_y)
        self._velocity = STEP

        self._last_fire = time()

        return super().activate(*args, **kwargs)

    def update(self, *args, **kwargs):
        keys = key.get_pressed()
        if (keys[K_RIGHT] or keys[K_d]):
            self.move(Direction.RIGHT)
        elif (keys[K_LEFT] or keys[K_a]):
            self.move(Direction.LEFT)
        if keys[K_SPACE]:
            self.fire()

        return super().update(*args, **kwargs)

    def move(self, direction: Direction) -> None:
        if self.__can_move__(direction):
            self._game_object.move_on(
                VectorLike(self._velocity * direction.value, 0))

    def fire(self) -> None:
        current_time = time()
        groups = self._game_object.groups()

        """
        Нужно так как враг состоит в группе всех спрайтов сцены,
        объектов для коллизии и отдельной группы врагов
        Она самая последняя и в нее не нужно добавлять пулю
        """
        if self._last_fire + FIRE_COOLDOWN <= current_time:
            HeroBullet(self._game_object.__images__.get("hero_bullet"),
                       self._game_object.rect.centerx, self._game_object.rect.y + 64 - 39,
                       groups)
            """
            64-39 так как граница спрайта находится выше границы модели.
            Такое вычитание позволяет запускать пулю с визуальной границы
            """
            self._last_fire = current_time

    def kill(self) -> None:
        self._lives.decrement_lives()
        """
        Уменьшение количества жизней
        """
        self._game_object.__musics__.get("explosion").play()

        if not self._lives.get_lives():
            """
            Окончательная смерть, если жизней больше нет
            """
            return super().kill()

        self._game_object.start_x, self._game_object.start_y = self.__start_position__

    def __can_move__(self, direction: Direction) -> bool:
        match direction:
            case Direction.LEFT:
                return self._game_object.start_x > SCREEN_MARGIN
            case Direction.RIGHT:
                return self._game_object.start_x < LEVEL_WIDTH + SCREEN_MARGIN - SPRITE_SIZE
