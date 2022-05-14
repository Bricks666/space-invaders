from random import randint
from time import time
import pygame
from consts.main import FIRE_COOLDOWN
from scenes.scene import Scene
from utils.generate_level import generate_level


class Level1(Scene):
    def __init__(self, screen: pygame.Surface):
        all_sprites, enemies = generate_level(1)
        self._enemies = enemies
        self.__last_enemy_fire_time = 0
        super().__init__(screen, all_sprites)

    def update(self):
        current_time = time()
        if self.__last_enemy_fire_time + FIRE_COOLDOWN <= current_time:
            self.__fire_enemy()
            self.__last_enemy_fire_time = current_time
        super().update()

    def __fire_enemy(self):
        enemies = self._enemies.sprites()
        shoter = randint(0, len(enemies) - 1)
        enemies[shoter].shot()
