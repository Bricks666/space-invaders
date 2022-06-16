from typing import Dict, Optional
import pygame
from consts import UNICODE_NUMBER_OFFSET
from packages.core import Machine, Scene, reset_sprites
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
class LevelsMachine(Machine[int], Scene):
    START: pygame.mixer.Sound
    __injected__: Dict[str, object]
    __levels__: LevelStore
    __lives__: LivesStore
    __scores__: ScoresStore

    def __init__(self, screen: pygame.Surface) -> None:
        super().__init__(screen)

        self.__levels__ = self.__injected__.get("__levels__")
        self.__lives__ = self.__injected__.get("__lives__")
        self.__scores__ = self.__injected__.get("__scores__")

    def change_scene(self, level_id: int) -> None:
        self.__exit_level__()
        current_level = self.__levels__.change_level(level_id)
        generate_level(current_level.level_path)
        self.__lives__.fetch_lives(current_level.level_id)
        self.__scores__.fetch_max_scores(current_level.level_id)
        super().change_scene(level_id)

    def update(self) -> None:
        self.__control_events__()
        super().update()

    def draw(self) -> None:
        return super().draw()

    def restart(self) -> None:
        current_level = self.__levels__.get_current_level()
        if current_level:
            self.change_scene(current_level.level_id)

    def on(self) -> None:
        self.__levels__.fetch_levels()
        levels = self.__levels__.get_levels()

        for level_id in range(len(levels)):
            level = Level(self.__screen__, levels[level_id].level_name)
            self.__scenes__.update([[level_id, level]])

    def off(self) -> None:
        self.__exit_level__()
        return super().off()

    def select(self) -> None:
        self.on()
        return super().select()

    def unselect(self) -> None:
        self.off()
        return super().unselect()

    def __exit_level__(self) -> None:
        self.__lives__.reset()
        self.__scores__.save_score()
        self.__scores__.reset_score()

    def __control_events__(self):
        for event in pygame.event.get(pygame.KEYDOWN):
            key_code = event.key - UNICODE_NUMBER_OFFSET
            if key_code in list(range(1, self.__levels__.get_levels_count() + 1)):
                self.change_scene(key_code)
                emit_event(pygame.event.Event(CustomEventsTypes.RESTART.value))
