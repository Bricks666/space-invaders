from typing import Dict, Optional
import pygame
from consts import UNICODE_NUMBER_OFFSET
from packages.core import StateMachine, ScreenPart
from packages.events import CustomEventsTypes, emit_event
from screens.level.level_place import LevelPlace
from packages.inject import Injector
from stores.level import LevelStore
from stores.lives import LivesStore
from stores.scores import ScoresStore


@Injector.inject(LevelStore, "__levels__")
@Injector.inject(LivesStore, "__lives__")
@Injector.inject(ScoresStore, "__scores__")
class LevelsMachine(StateMachine[int], ScreenPart):
    __injected__: Dict[str, object]
    __levels__: LevelStore
    __lives__: LivesStore
    __scores__: ScoresStore

    def __init__(self, screen: pygame.Surface) -> None:
        super().__init__(screen)
        ScreenPart.__init__(self, screen)

        self.__levels__ = self.__injected__.get("__levels__")
        self.__lives__ = self.__injected__.get("__lives__")
        self.__scores__ = self.__injected__.get("__scores__")

    def change_state(self, level_id: int) -> None:
        current_level = self.__levels__.change_level(level_id)
        super().change_state(level_id)
        self.__lives__.fetch_lives(current_level.level_id)
        self.__scores__.fetch_max_scores(current_level.level_id)

    def update(self) -> None:
        self.__control_events__()
        return super().update()

    def activate(self, start_level_id: Optional[int] = None) -> None:
        self.__levels__.fetch_levels()
        levels = self.__levels__.get_levels()

        for level in levels:
            level_place = LevelPlace(self.__screen__, level)
            self.__states__.update([[level.level_id, level_place]])

        return super().activate(start_level_id)

    def __control_events__(self):
        for event in pygame.event.get(pygame.KEYDOWN):
            key_code = event.key - UNICODE_NUMBER_OFFSET
            if key_code in list(range(1, self.__levels__.get_levels_count() + 1)):
                self.change_state(key_code)
                emit_event(pygame.event.Event(CustomEventsTypes.RESTART.value))
