from enum import Enum

import pygame
from pygame.sprite import Group


class Levels(Enum):
    LEVEL1 = "level1"
    LEVEL2 = "level2"


class LevelStore:
    __level__: Levels
    __enemies__: pygame.sprite.Group()
    __all_sprites__: pygame.sprite.Group()
    __players__: pygame.sprite.Group()

    def __init__(self, level: Levels = Levels.LEVEL1, all_sprites: Group = Group(), enemies: Group = Group(), players: Group = Group()):
        self.change_level(level, all_sprites, enemies, players)

    def get_level(self):
        return self.__level__

    def change_level(self, level: Levels, all_sprites: Group, enemies: Group, players: Group):
        self.__level__ = level
        self.__all_sprites__ = all_sprites
        self.__enemies__ = enemies
        self.__players__ = players

    def get_enemies(self) -> pygame.sprite.Group:
        return self.__enemies__

    def get_players(self) -> pygame.sprite.Group:
        return self.__players__

    def get_all_sprites(self) -> pygame.sprite.Group:
        return self.__all_sprites__


levels = LevelStore()
