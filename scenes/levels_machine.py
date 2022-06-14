from typing import Dict, Optional
import pygame
from scenes.level import Level
from stores.level import Levels
from packages.inject import Inject
from stores.level import LevelStore
from utils.generate_level import generate_level


@Inject(LevelStore, "__levels__")
class LevelsMachine:
    START: pygame.mixer.Sound
    __injected__: Dict
    __levels__: LevelStore

    def __init__(self, screen: pygame.Surface):
        self.__screen__ = screen
        self.__current_level__: Optional[Level] = None
        self.__levels__ = self.__injected__.get("__levels__")

    def change_level(self, level: Levels):
        sprites = self.__get_sprites__(level)
        self.__levels__.change_level(level, *sprites)
        self.__current_level__ = Level(self.__screen__, *sprites)

    def draw(self):
        if self.__current_level__:
            self.__current_level__.draw()

    def update(self):
        if self.__current_level__:
            self.__current_level__.update()

    def __get_sprites__(self, level: Levels):
        return generate_level(level.value)
