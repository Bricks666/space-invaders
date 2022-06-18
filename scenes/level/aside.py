from typing import Dict
from pygame import Surface, Rect
from consts import ASIDE_BAR_WIDTH, BORDER_WIDTH, HEIGHT, LEVEL_WIDTH, SCREEN_MARGIN, SPRITE_SIZE
from entities.text import Text
from packages.core import ScreenPart, Group
from scenes.level.live import Live
from stores.lives import LivesStore
from packages.inject import Inject
from stores.scores import ScoresStore


@Inject(ScoresStore, "__scores__")
@Inject(LivesStore, "__lives__")
class Aside(ScreenPart):
    __injected__: Dict[str, object]
    __scores__: ScoresStore
    __lives__: LivesStore
    __margin__: float = SPRITE_SIZE / 2
    __live_sprites__: Group[Live]

    def __init__(self, screen: Surface) -> None:
        super().__init__(screen)
        self.rect = Rect(LEVEL_WIDTH + SCREEN_MARGIN + BORDER_WIDTH * 2, SCREEN_MARGIN - BORDER_WIDTH,
                         ASIDE_BAR_WIDTH, HEIGHT - SCREEN_MARGIN * 2 + BORDER_WIDTH * 2)

        self.__live_sprites__ = Group[Live]()

        self.__scores__ = self.__injected__.get("__scores__")
        self.__lives__ = self.__injected__.get("__lives__")

    def draw(self) -> None:

        return super().draw()

    def update(self) -> None:
        self.__validate_lives__()
        score = {
            "max_score": self.__scores__.get_max_scores(),
            "score": self.__scores__.get_scores()
        }
        return super().update(score)

    def select(self) -> None:
        self.__create_text__()
        self.__create_lives__()
        return super().select()

    def unselect(self) -> None:
        self.__live_sprites__.empty()
        return super().unselect()

    def __validate_lives__(self) -> None:
        live_sprites_count = len(self.__live_sprites__)
        lives_count = self.__lives__.get_lives()

        if lives_count != live_sprites_count:
            for live in self.__live_sprites__:
                live.kill()
            self.__create_lives__()

    def __create_lives__(self) -> None:
        lives_count = self.__lives__.get_lives()

        def x(i): return self.rect.x + self.__margin__ + SPRITE_SIZE * i
        y = self.rect.bottom - SPRITE_SIZE

        lives = []
        for i in range(lives_count):
            lives.append(Live(x(i), y))
        self.__all_sprites__.add(lives)
        self.__live_sprites__.add(lives)

    def __create_text__(self) -> None:

        max_scores_text = Text(
            "Max score:", self.rect.x + self.__margin__, SPRITE_SIZE * 1.5 + 24)
        max_scores = Text("{max_score} POINTS", self.rect.x +
                          self.__margin__, SPRITE_SIZE * 2 + 24)
        scores_text = Text(
            "Current score:", self.rect.x + self.__margin__, SPRITE_SIZE * 0.5 + 24)
        scores = Text(
            "{score} POINTS", self.rect.x + self.__margin__, SPRITE_SIZE * 1 + 24)

        max_scores_text.rect.centerx = max_scores.rect.centerx = \
            scores_text.rect.centerx = scores.rect.centerx = self.rect.centerx

        self.__all_sprites__.add(
            max_scores_text, max_scores, scores, scores_text)
