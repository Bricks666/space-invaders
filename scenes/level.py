from random import randint
from time import time
import pygame
from consts.main import BORDER_WIDTH, FIRE_COOLDOWN, HEIGHT, LEVEL_HEIGHT, LEVEL_WIDTH, SCREEN_MARGIN
from scenes.scene import Scene


class Level(Scene):
    def __init__(self, screen: pygame.Surface, all_sprites: pygame.sprite.Group, enemies: pygame.sprite.Group, players: pygame.sprite.Group):
        super().__init__(screen)
        self.__last_enemy_fire_time__: float = time()
        self.__all_sprites__ = all_sprites
        self.__enemies__ = enemies
        self.__players__ = players

    def update(self):
        is_end = self.__check_end__()
        if is_end:
            return
        self.__fire_enemy__()
        super().update()

    def draw(self):
        self.__draw_border__()
        return super().draw()

    def __fire_enemy__(self):
        current_time = time()
        if self.__last_enemy_fire_time__ + FIRE_COOLDOWN <= current_time:
            enemies = self.__enemies__.sprites()
            shoter = randint(0, len(enemies) - 1)
            enemies[shoter].fire()
            self.__last_enemy_fire_time__ = current_time

    def __check_end__(self) -> bool:
        return not len(self.__enemies__) or not len(self.__players__)

    def __draw_border__(self):
        color = pygame.Color(250, 250, 250)
        top_left = (SCREEN_MARGIN - BORDER_WIDTH, SCREEN_MARGIN - BORDER_WIDTH)
        top_right = (SCREEN_MARGIN + LEVEL_WIDTH, SCREEN_MARGIN - BORDER_WIDTH)
        bottom_left = (SCREEN_MARGIN,
                       SCREEN_MARGIN + LEVEL_HEIGHT)
        self._screen_.fill(color,
                           pygame.Rect(top_left, (LEVEL_WIDTH + BORDER_WIDTH, BORDER_WIDTH)))
        self._screen_.fill(color,
                           pygame.Rect(top_right, (BORDER_WIDTH, LEVEL_HEIGHT + BORDER_WIDTH * 2)))
        self._screen_.fill(color,
                           pygame.Rect(bottom_left, (LEVEL_WIDTH, BORDER_WIDTH)))
        self._screen_.fill(color,
                           pygame.Rect(top_left, (BORDER_WIDTH, LEVEL_HEIGHT + BORDER_WIDTH)))
