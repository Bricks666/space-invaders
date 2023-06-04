from pygame import display
from time import time
from random import randint
from consts import GAME_NAME
from utils.generate_level import generate_level
from packages.core.script import Script
from packages.core.game_object import Group
from packages.events import CustomEventsTypes, custom_event, emit_event
from packages.inject import Injector
from stores.level import LevelStore
from stores.lives import LivesStore
from stores.scores import ScoresStore
from entities.enemy import Enemy
from consts import FIRE_COOLDOWN
from .level_place import *


@Injector.inject(ScoresStore, "_scores")
@Injector.inject(LivesStore, "_lives")
@Injector.inject(LevelStore, "_levels")
class LevelPlaceScript(Script['LevelPlace']):
    _enemies: Group[Enemy]
    _enemies: Group[Enemy]
    """
    Группа врагов на уровне
    """
    _scores: ScoresStore
    """
    Хранилище очков
    """
    _levels: LevelStore
    """
    Хранилище уровней
    """
    _lives: LivesStore
    """
    Хранилище жизней
    """
    _last_enemy_fire_time: float

    def activate(self, *args, **kwargs) -> None:
        level_id = self._game_object.level_id
        current_level = self._levels.change_level(level_id)
        self._lives.fetch_lives(level_id)
        self._scores.fetch_max_scores(level_id)
        sprites = generate_level(current_level.level_path)
        self._game_object.__objects__ = sprites[0]
        self._enemies = sprites[1]
        self._heros = sprites[2]
        self._last_enemy_fire_time: float = time()

        display.set_caption(
            f"{GAME_NAME} - level: {current_level.level_name}")

        return super().activate()

    def update(self) -> None:
        self.__fire_enemy()
        if self.__check_lose():
            self.__end("Game over")
            return
        elif self.__check_win():
            self.__end("You win")
            return
        super().update()

    def deactivate(self) -> None:
        self._enemies.empty()
        self._scores.save()

        return super().deactivate()

    def __fire_enemy(self) -> None:
        current_time = time()
        if self._last_enemy_fire_time + FIRE_COOLDOWN <= current_time:
            enemies = self._enemies.objects()
            shooter = randint(0, len(enemies) - 1)
            print(enemies[shooter])
            self._last_enemy_fire_time = current_time

    def __check_win(self) -> bool:
        """
        Уровень считается выигранным, если не осталось врагов
        """
        return not len(self._enemies)

    def __check_lose(self) -> bool:
        """
        Если игрок умер, то он проиграл
        """
        return not len(self.__heros)

    def __end(self, phrase: str) -> None:
        evt = custom_event(CustomEventsTypes.CHANGE_SCREEN,
                           phrase, screen="end")
        emit_event(evt)
