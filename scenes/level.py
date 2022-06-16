from random import randint
from time import time
from typing import Dict
import pygame
from consts import BORDER_WIDTH, FIRE_COOLDOWN, GAME_NAME, LEVEL_HEIGHT, LEVEL_WIDTH, SCREEN_MARGIN, SPRITE_SIZE
from entities.enemy import Enemy
from entities.text import Text
from packages.core import get_all_sprites_by_class
from scenes.scene import Scene
from stores.lives import LivesStore
from packages.inject import Inject


@Inject(LivesStore, "__lives__")
class Level(Scene):
    __injected__: Dict[str, object]
    __lives__: LivesStore

    def __init__(self, screen: pygame.Surface, level_name: int):
        super().__init__(screen)

        self.__enemies__ = get_all_sprites_by_class(Enemy)
        self.__last_enemy_fire_time__: float = time()

        self.__lives__ = self.__injected__.get("__lives__")
        pygame.display.set_caption(f"{GAME_NAME} - level: \"{level_name}\"")

    def update(self) -> None:
        if self.__check_lose__():
            self.__end__("Game over")
        elif self.__check_win__():
            self.__end__("You win")
        else:
            self.__fire_enemy__()
            super().update()

    def draw(self) -> None:
        self.__draw_border__()
        return super().draw()

    def __fire_enemy__(self) -> None:
        current_time = time()
        if self.__last_enemy_fire_time__ + FIRE_COOLDOWN <= current_time:
            enemies = self.__enemies__.sprites()
            shooter = randint(0, len(enemies) - 1)
            enemies[shooter].fire()
            self.__last_enemy_fire_time__ = current_time

    def __check_win__(self) -> bool:
        return not len(self.__enemies__)

    def __check_lose__(self) -> bool:
        return not self.__lives__.get_lives()

    def __end__(self, phrase: str) -> None:
        self.__all_sprites__.empty()
        self.__draw_end__(phrase)

    def __draw_end__(self, phase: str):
        phrase_text = Text.generate(phase)
        rect = phrase_text.get_rect()
        rect.center = self._screen_.get_rect().center
        rect.centerx = LEVEL_WIDTH / 2 + SCREEN_MARGIN
        rect.y -= SPRITE_SIZE
        self._screen_.blit(phrase_text, rect)

    def __draw_border__(self) -> None:
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
