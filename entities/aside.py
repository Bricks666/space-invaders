from typing import Dict
import pygame
from consts import ASIDE_BAR_WIDTH, BORDER_WIDTH, HEIGHT, LEVEL_WIDTH, SCREEN_MARGIN, SPRITE_SIZE
from entities.text import Text
from stores.lives import LivesStore
from packages.inject import Inject
from stores.scores import ScoresStore
from utils.loaders import sprite_loader


@Inject(ScoresStore, "__scores__")
@Inject(LivesStore, "__lives__")
class Aside(pygame.sprite.Sprite):
    __injected__: Dict[str, object]
    __scores__: ScoresStore
    __lives__: LivesStore
    __background__: pygame.Color
    __margin__: float

    def __init__(self, screen: pygame.Surface) -> None:
        self.__screen__ = screen
        self.rect = pygame.Rect(LEVEL_WIDTH + SCREEN_MARGIN + BORDER_WIDTH * 2, SCREEN_MARGIN - BORDER_WIDTH,
                                ASIDE_BAR_WIDTH, HEIGHT - SCREEN_MARGIN * 2 + BORDER_WIDTH * 2)

        self.__background__ = pygame.Color(0, 0, 0)
        self.__margin__ = SPRITE_SIZE / 2

        self.__scores__ = self.__injected__.get("__scores__")
        self.__lives__ = self.__injected__.get("__lives__")

    def draw(self) -> None:
        self.__screen__.fill(self.__background__, self.rect)
        self.__draw_current_score__()
        self.__draw_max_score__()
        self.__draw__lives__()

    def __draw_max_score__(self) -> None:
        label = Text.generate("Max score:")
        max_score = f"{self.__scores__.get_max_scores()} POINTS"
        max_scores_text = Text.generate(
            max_score)
        label_rect = label.get_rect()
        label_rect.centerx = self.rect.centerx
        label_rect.x = self.rect.x + self.__margin__
        label_rect.y = SPRITE_SIZE * 1.5 + 24
        score_rect = max_scores_text.get_rect()
        score_rect.x = self.rect.x + self.__margin__
        score_rect.y = SPRITE_SIZE * 2 + 24
        self.__screen__.blit(label, label_rect)
        self.__screen__.blit(max_scores_text, score_rect)

    def __draw_current_score__(self) -> None:
        label = Text.generate("Current score:")
        current_score = f"{self.__scores__.get_scores()} POINTS"
        current_scores_text = Text.generate(
            current_score)
        label_rect = label.get_rect()
        label_rect.x = self.rect.x + self.__margin__
        label_rect.y = SPRITE_SIZE * 0.5 + 24
        score_rect = current_scores_text.get_rect()
        score_rect.x = self.rect.x + self.__margin__
        score_rect.y = SPRITE_SIZE + 24
        self.__screen__.blit(label, label_rect)
        self.__screen__.blit(current_scores_text, score_rect)

    def __draw__lives__(self) -> None:
        for i in range(self.__lives__.get_lives()):
            live = self.__create_live__()
            rect = live.get_rect()
            rect.x = self.rect.x + self.__margin__ + SPRITE_SIZE * i
            rect.y = self.rect.y + self.rect.height - SPRITE_SIZE
            self.__screen__.blit(live, rect)

    def __create_live__(self) -> pygame.Surface:
        live = sprite_loader.load("hero.png")
        return pygame.transform.scale(live, (SPRITE_SIZE * 0.8, SPRITE_SIZE * 0.8))
