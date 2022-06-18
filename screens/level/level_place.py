from random import randint
from time import time
from typing import Dict, Tuple
from pygame import Surface, display, Rect, event, sprite
from consts import BORDER_WIDTH, FIRE_COOLDOWN, GAME_NAME, LEVEL_HEIGHT, LEVEL_WIDTH, SCREEN_MARGIN, BORDER_COLOR
from packages.core import ScreenPart, Group, Collidable
from packages.events import CustomEventsTypes, create_event_params, emit_event
from stores.lives import LivesStore
from packages.inject import Injector
from entities.enemy import Enemy
from models import LevelModel
from stores.scores import ScoresStore
from utils.generate_level import generate_level


_Sprites = Tuple[Group[sprite.Sprite], Group[Enemy]]


@Injector.inject(LivesStore, "__lives__")
@Injector.inject(ScoresStore, "__scores__")
class LevelPlace(ScreenPart):
    __injected__: Dict[str, object]
    __enemies__: Group[Enemy]
    __level__: LevelModel
    __lives__: LivesStore
    __scores__: ScoresStore
    """ __cache__: Cache """

    def __init__(self, screen: Surface, level: LevelModel) -> None:
        super().__init__(screen)
        self.__enemies__ = Group[Enemy]()
        self.__level__ = level

        self.__lives__ = self.__injected__.get("__lives__")
        self.__scores__ = self.__injected__.get("__scores__")

    def update(self) -> None:
        if self.__check_lose__():
            self.__end__("Game over")
        elif self.__check_win__():
            self.__end__("You win")
        else:
            self.__fire_enemy__()
            super().update()

    def draw(self) -> None:
        self.__draw_border__()
        return super().draw()

    def activate(self) -> None:

        sprites = generate_level(self.__level__.level_path)
        self.__all_sprites__ = sprites[0]
        self.__enemies__ = sprites[1]
        self.__last_enemy_fire_time__: float = time()

        display.set_caption(
            f"{GAME_NAME} - level: {self.__level__.level_name}")

        return super().activate()

    def inactivate(self) -> None:
        self.__enemies__.empty()
        Collidable.reset_collidable()

        self.__scores__.save()

        return super().inactivate()

    def __fire_enemy__(self) -> None:
        current_time = time()
        if self.__last_enemy_fire_time__ + FIRE_COOLDOWN <= current_time:
            enemies = self.__enemies__.sprites()
            shooter = randint(0, len(enemies) - 1)
            enemies[shooter].fire()
            self.__last_enemy_fire_time__ = current_time

    def __check_win__(self) -> bool:
        return not len(self.__enemies__)

    def __check_lose__(self) -> bool:
        return not self.__lives__.get_lives()

    def __end__(self, phrase: str) -> None:
        evt = event.Event(CustomEventsTypes.CHANGE_SCREEN.value,
                          create_event_params(args=(phrase,), screen="end"))
        emit_event(evt)

    def __draw_border__(self) -> None:
        top_left = (SCREEN_MARGIN - BORDER_WIDTH, SCREEN_MARGIN - BORDER_WIDTH)
        top_right = (SCREEN_MARGIN + LEVEL_WIDTH, SCREEN_MARGIN - BORDER_WIDTH)
        bottom_left = (SCREEN_MARGIN,
                       SCREEN_MARGIN + LEVEL_HEIGHT)
        self.__screen__.fill(BORDER_COLOR,
                             Rect(top_left, (LEVEL_WIDTH + BORDER_WIDTH, BORDER_WIDTH)))
        self.__screen__.fill(BORDER_COLOR,
                             Rect(top_right, (BORDER_WIDTH, LEVEL_HEIGHT + BORDER_WIDTH * 2)))
        self.__screen__.fill(BORDER_COLOR,
                             Rect(bottom_left, (LEVEL_WIDTH, BORDER_WIDTH)))
        self.__screen__.fill(BORDER_COLOR,
                             Rect(top_left, (BORDER_WIDTH, LEVEL_HEIGHT + BORDER_WIDTH)))
