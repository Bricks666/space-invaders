from typing import Dict, Optional
import pygame
from consts.main import UNICODE_NUMBER_OFFSET
from packages.core import reset_sprites
from packages.events import CustomEventsTypes, emit_event
from scenes.level import Level
from packages.inject import Inject
from stores.level import LevelStore
from stores.lives import LivesStore
from stores.scores import ScoresStore
from utils.generate_level import generate_level


@Inject(LevelStore, "__levels__")
@Inject(LivesStore, "__lives__")
@Inject(ScoresStore, "__scores__")
class LevelsMachine:
    START: pygame.mixer.Sound
    __injected__: Dict
    __levels__: LevelStore
    __lives__: LivesStore
    __scores__: ScoresStore
    __active_level__: Optional[Level]

    def __init__(self, screen: pygame.Surface) -> None:
        self.__screen__ = screen
        self.__active_level__ = None

        self.__levels__ = self.__injected__.get("__levels__")
        self.__lives__ = self.__injected__.get("__lives__")
        self.__scores__ = self.__injected__.get("__scores__")

    def change_level(self, level_id: int) -> None:
        self.__exit_level__()

        current_level = self.__levels__.change_level(level_id)
        generate_level(current_level.level_path)

        self.__lives__.fetch_lives(current_level.level_id)
        self.__scores__.fetch_max_scores(current_level.level_id)

        self.__active_level__ = Level(self.__screen__, current_level.lives)

    def draw(self) -> None:
        if self.__active_level__:
            self.__active_level__.draw()

    def update(self) -> None:
        if self.__active_level__:
            self.__active_level__.update()
        self.__control_events__()

    def restart(self) -> None:
        current_level = self.__levels__.get_current_level()
        if current_level:
            self.change_level(current_level.level_id)

    def on(self) -> None:
        self.__levels__.fetch_levels()

    def off(self) -> None:
        self.__exit_level__()

    def __exit_level__(self) -> None:
        self.__lives__.reset()
        self.__scores__.save_score()
        self.__scores__.reset_score()
        reset_sprites()

    def __control_events__(self):
        for event in pygame.event.get(pygame.KEYDOWN):
            key_code = event.key - UNICODE_NUMBER_OFFSET
            if key_code in list(range(1, self.__levels__.get_levels_count() + 1)):
                self.change_level(key_code)
                emit_event(pygame.event.Event(CustomEventsTypes.RESTART.value))
