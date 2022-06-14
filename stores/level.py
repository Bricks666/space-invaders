from enum import Enum

import pygame
from pygame.sprite import Group

from packages.inject import Injectable


class Levels(Enum):
    LEVEL1 = "level1"
    LEVEL2 = "level2"


@Injectable()
class LevelStore:
    __level__: Levels
    __enemies__: pygame.sprite.Group
    __all_sprites__: pygame.sprite.Group

    def __init__(self, level: Levels = Levels.LEVEL1, all_sprites: Group = Group(), enemies: Group = Group()) -> None:
        self.change_level(level, all_sprites, enemies)

    def get_level(self) -> Levels:
        return self.__level__

    def change_level(self, level: Levels, all_sprites: Group, enemies: Group) -> None:
        self.__level__ = level
        self.__all_sprites__ = all_sprites
        self.__enemies__ = enemies

    def get_enemies(self) -> pygame.sprite.Group:
        return self.__enemies__

    def get_all_sprites(self) -> pygame.sprite.Group:
        return self.__all_sprites__

    def set_level(self, level: Levels) -> None:
        self.__level__ = level
