from random import randint
from time import time
import pygame
from consts.main import FIRE_COOLDOWN
from scenes.scene import Scene
from utils.generate_level import generate_level


class Level(Scene):
    def __init__(self, screen: pygame.Surface, level: int):
        super().__init__(screen)
        self.__last_enemy_fire_time__: float = time()
        self.__level__ = level

    def update(self):
        is_end = self.__check_end__()
        if is_end:
            return
        self.__fire_enemy__()
        super().update()

    def select(self):
        _, enemies, players = generate_level(self.__level__)
        self._enemies_ = enemies
        self._players_ = players

    def unselect(self):
        return super().unselect()

    def __fire_enemy__(self):
        current_time = time()
        if self.__last_enemy_fire_time__ + FIRE_COOLDOWN <= current_time:
            enemies = self._enemies_.sprites()
            shoter = randint(0, len(enemies) - 1)
            enemies[shoter].fire()
            self.__last_enemy_fire_time__ = current_time

    def __check_end__(self) -> bool:
        return not len(self._enemies_) or not len(self._players_)
