from random import randint
from typing import Dict
from time import time
from pygame import K_LEFT, K_RIGHT, K_SPACE, K_a, K_d, Surface, display, Rect, key
from consts import BORDER_WIDTH, FIRE_COOLDOWN, GAME_NAME, LEVEL_HEIGHT, LEVEL_WIDTH, SCREEN_MARGIN, BORDER_COLOR
from entities.hero import Hero
from packages.core import ScreenPart, Group, Collidable
from packages.core.entity import Direction
from packages.events import CustomEventsTypes, custom_event,  emit_event
from packages.inject import Injector
from entities.enemy import Enemy
from stores.level import LevelStore
from stores.lives import LivesStore
from stores.scores import ScoresStore
from utils.generate_level import generate_level


@Injector.inject(ScoresStore, "__scores__")
@Injector.inject(LivesStore, "__lives__")
@Injector.inject(LevelStore, "__levels__")
class LevelPlace(ScreenPart):
    __injected__: Dict[str, object]
    __enemies__: Group[Enemy]
    __heros__: Group[Hero]
    __scores__: ScoresStore
    __levels__: LevelStore
    __lives__: LivesStore

    def __init__(self, screen: Surface) -> None:
        rect = Rect(SCREEN_MARGIN, SCREEN_MARGIN, LEVEL_WIDTH, LEVEL_HEIGHT)
        super().__init__(screen, rect)
        self.__enemies__ = Group[Enemy]()

        self.__scores__ = self.__injected__.get("__scores__")
        self.__levels__ = self.__injected__.get("__levels__")
        self.__lives__ = self.__injected__.get("__lives__")

    def update(self) -> None:
        if self.__check_lose__():
            self.__end__("Game over")
            return
        elif self.__check_win__():
            self.__end__("You win")
            return

        keys = key.get_pressed()
        hero = self.__get_hero__()
        if (keys[K_RIGHT] or keys[K_d]) and hero:
            hero.move(Direction.RIGHT)
        elif (keys[K_LEFT] or keys[K_a]) and hero:
            hero.move(Direction.LEFT)
        if keys[K_SPACE] and hero:
            hero.fire()

        self.__move_enemies__()
        self.__fire_enemy__()
        super().update()

    def draw(self) -> None:
        self.__draw_border__()
        return super().draw()

    def activate(self, level_id: int) -> None:
        current_level = self.__levels__.change_level(level_id)
        self.__lives__.fetch_lives(level_id)
        self.__scores__.fetch_max_scores(level_id)
        sprites = generate_level(current_level.level_path)
        self.__all_sprites__ = sprites[0]
        self.__enemies__ = sprites[1]
        self.__heros__ = sprites[2]
        self.__last_enemy_fire_time__: float = time()

        display.set_caption(
            f"{GAME_NAME} - level: {current_level.level_name}")

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

    def __move_enemies__(self) -> None:
        for enemy in self.__enemies__:
            enemy.move()

    def __get_hero__(self) -> Hero | None:
        return self.__heros__.sprites()[0]

    def __check_win__(self) -> bool:
        return not len(self.__enemies__)

    def __check_lose__(self) -> bool:
        return not len(self.__heros__)

    def __end__(self, phrase: str) -> None:
        evt = custom_event(CustomEventsTypes.CHANGE_SCREEN,
                           phrase, screen="end")
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
