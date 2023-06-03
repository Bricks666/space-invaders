from random import randint
from time import time
from pygame import Surface, display, Rect
from components import Primitive
from consts import BORDER_WIDTH, FIRE_COOLDOWN, GAME_NAME, LEVEL_HEIGHT, LEVEL_WIDTH, SCREEN_MARGIN, BORDER_COLOR
from entities.hero import Hero
from packages.core import ScreenPart, Collidable
from packages.core.game_object import Group
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
    """
    Площадка уровня с игроком и врагами
    """
    __enemies__: Group[Enemy]
    """
    Группа врагов на уровне
    """
    __heros__: Group[Hero]
    """
    Группа игроков на уровне
    """
    __scores__: ScoresStore
    """
    Хранилище очков
    """
    __levels__: LevelStore
    """
    Хранилище уровней
    """
    __lives__: LivesStore
    """
    Хранилище жизней
    """

    def __init__(self, screen: Surface) -> None:
        rect = Rect(SCREEN_MARGIN, SCREEN_MARGIN, LEVEL_WIDTH, LEVEL_HEIGHT)
        super().__init__(screen, rect)
        self.__enemies__ = Group[Enemy]()

    def update(self) -> None:
        if self.__check_lose__():
            self.__end__("Game over")
            return
        elif self.__check_win__():
            self.__end__("You win")
            return
        super().update()

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

        self.__create_border__()

        return super().activate()

    def deactivate(self) -> None:
        self.__enemies__.empty()
        Collidable.reset_collidable()
        """
        Чтобы эти модели не мешались на других уровнях
        """
        self.__scores__.save()

        return super().deactivate()

    def __fire_enemy__(self) -> None:
        current_time = time()
        if self.__last_enemy_fire_time__ + FIRE_COOLDOWN <= current_time:
            enemies = self.__enemies__.objects()
            shooter = randint(0, len(enemies) - 1)
            enemies[shooter].fire()
            self.__last_enemy_fire_time__ = current_time

    def __check_win__(self) -> bool:
        """
        Уровень считается выигранным, если не осталось врагов
        """
        return not len(self.__enemies__)

    def __check_lose__(self) -> bool:
        """
        Если игрок умер, то он проиграл
        """
        return not len(self.__heros__)

    def __end__(self, phrase: str) -> None:
        evt = custom_event(CustomEventsTypes.CHANGE_SCREEN,
                           phrase, screen="end")
        emit_event(evt)

    def __create_border__(self) -> None:
        """
        Метод создающий рамку вокруг уровня
        """
        top_left = (SCREEN_MARGIN - BORDER_WIDTH, SCREEN_MARGIN - BORDER_WIDTH)
        top_right = (SCREEN_MARGIN + LEVEL_WIDTH, SCREEN_MARGIN - BORDER_WIDTH)
        bottom_left = (SCREEN_MARGIN,
                       SCREEN_MARGIN + LEVEL_HEIGHT)
        top = Rect(*top_left, LEVEL_WIDTH + BORDER_WIDTH, BORDER_WIDTH)
        right = Rect(top_right, (BORDER_WIDTH,
                     LEVEL_HEIGHT + BORDER_WIDTH * 2))
        bottom = Rect(bottom_left, (LEVEL_WIDTH, BORDER_WIDTH))
        left = Rect(top_left, (BORDER_WIDTH, LEVEL_HEIGHT + BORDER_WIDTH * 2))
        top = Primitive(top, BORDER_COLOR)
        right = Primitive(right, BORDER_COLOR)
        bottom = Primitive(bottom, BORDER_COLOR)
        left = Primitive(left, BORDER_COLOR)
        self.__all_sprites__.add(top, right, bottom, left)
