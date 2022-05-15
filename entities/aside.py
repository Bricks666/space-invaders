from typing import Dict
import pygame
from consts.main import ASIDE_BAR_WIDTH, BORDER_WIDTH, HEIGHT, LEVEL_WIDTH, SCREEN_MARGIN, SPRITE_SIZE
from entities.text import Text
from stores.lives import Lives, lives
from stores.main import inject
from stores.scores import Scores, scores
from utils.loaders import sprite_loader


@inject(scores, "__scores__")
@inject(lives, "__lives__")
class Aside(pygame.sprite.Sprite):
    __injected__: Dict
    __scores__: Scores
    __lives__: Lives

    def __init__(self, screen: pygame.Surface):
        self.__screen__ = screen
        self.rect = pygame.Rect(LEVEL_WIDTH + SCREEN_MARGIN + BORDER_WIDTH * 2, SCREEN_MARGIN - BORDER_WIDTH,
                                ASIDE_BAR_WIDTH, HEIGHT - SCREEN_MARGIN * 2 + BORDER_WIDTH * 2)
        self.__background__ = pygame.Color(0, 0, 0)
        self.__scores__ = self.__injected__.get("__scores__")
        self.__lives__ = self.__injected__.get("__lives__")
        self.__max_scores__ = Text()
        self.__current_scores__ = Text()
        self.__margin__ = SPRITE_SIZE / 2

    def draw(self):
        self.__screen__.fill(self.__background__, self.rect)
        self.__draw_current_score__()
        self.__draw_max_score__()
        self.__draw__lives__()

    def __draw_max_score__(self):
        max_score = str(self.__scores__.get_max_scores()) + " POINTS"
        max_scores_text = self.__max_scores__.generate(
            max_score)
        rect = max_scores_text.get_rect()
        rect.x = self.rect.x + self.__margin__
        rect.y = SPRITE_SIZE * 2 + 24
        rect.centerx = self.rect.centerx
        self.__screen__.blit(max_scores_text, rect)

    def __draw_current_score__(self):
        current_score = str(self.__scores__.get_scores()) + " POINTS"
        current_scores_text = self.__current_scores__.generate(
            current_score)
        rect = current_scores_text.get_rect()
        rect.x = self.rect.x + self.__margin__
        rect.y = SPRITE_SIZE + 24
        rect.centerx = self.rect.centerx
        self.__screen__.blit(current_scores_text, rect)

    def __draw__lives__(self):
        for i in range(self.__lives__.get_lives()):
            live = self.__create_live__()
            rect = live.get_rect()
            rect.x = self.rect.x + self.__margin__ + SPRITE_SIZE * i
            rect.y = self.rect.y + self.rect.height - SPRITE_SIZE
            self.__screen__.blit(live, rect)

    def __create_live__(self) -> pygame.Surface:
        live = sprite_loader.load("hero.png")
        return pygame.transform.scale(live, (SPRITE_SIZE * 0.8, SPRITE_SIZE * 0.8))
