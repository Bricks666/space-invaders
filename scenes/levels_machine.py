from typing import Dict, Optional
import pygame
from scenes.level import Level
from packages.inject import Inject
from stores.level import LevelStore
from stores.lives import LivesStore
from utils.generate_level import generate_level


@Inject(LevelStore, "__levels__")
@Inject(LivesStore, "__lives__")
class LevelsMachine:
    START: pygame.mixer.Sound
    __injected__: Dict
    __levels__: LevelStore
    __lives__: LivesStore
    __active_level__: Optional[Level]

    def __init__(self, screen: pygame.Surface) -> None:
        self.__screen__ = screen
        self.__active_level__ = None
        self.__levels__ = self.__injected__.get("__levels__")
        self.__lives__ = self.__injected__.get("__lives__")

    def change_level(self, level_id: int) -> None:
        self.__levels__.change_level(level_id)
        current_level = self.__levels__.get_current_level()
        generate_level(current_level.level_path)
        self.__lives__.set_lives(current_level.lives)
        self.__active_level__ = Level(self.__screen__)

    def draw(self) -> None:
        if self.__active_level__:
            self.__active_level__.draw()

    def update(self) -> None:
        if self.__active_level__:
            self.__active_level__.update()
