from pygame import Surface, Rect
from consts import ASIDE_BAR_WIDTH, BORDER_WIDTH, HEIGHT, LEVEL_WIDTH, SCREEN_MARGIN, SPRITE_SIZE
from components import Text
from packages.core import ScreenPart, Group
from screens.level.live import Live
from stores.lives import LivesStore
from packages.inject import Injector
from stores.scores import ScoresStore


@Injector.inject(ScoresStore, "__scores__")
@Injector.inject(LivesStore, "__lives__")
class Aside(ScreenPart):
    __scores__: ScoresStore
    __lives__: LivesStore
    __margin__: float = SPRITE_SIZE / 2
    __live_sprites__: Group[Live]

    def __init__(self, screen: Surface) -> None:
        rect = Rect(LEVEL_WIDTH + SCREEN_MARGIN + BORDER_WIDTH * 2, SCREEN_MARGIN - BORDER_WIDTH,
                    ASIDE_BAR_WIDTH, HEIGHT - SCREEN_MARGIN * 2 + BORDER_WIDTH * 2)
        super().__init__(screen, rect)

        self.__live_sprites__ = Group[Live]()

    def update(self) -> None:
        self.__validate_lives__()
        score = {
            "max_score": self.__scores__.get_max_scores(),
            "score": self.__scores__.get_scores()
        }
        return super().update(score)

    def activate(self, *args, **kwargs) -> None:
        self.__create_text__()
        self.__create_lives__()
        return super().activate(*args, **kwargs)

    def inactivate(self, *args, **kwargs) -> None:
        self.__live_sprites__.empty()
        return super().inactivate(*args, **kwargs)

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
            "Max score:", self.rect.x + self.__margin__, SPRITE_SIZE * 1.5 + 24, "small")
        max_scores = Text("{max_score} POINTS", self.rect.x +
                          self.__margin__, SPRITE_SIZE * 2 + 24, "small")
        scores_text = Text(
            "Current score:", self.rect.x + self.__margin__, SPRITE_SIZE * 0.5 + 24, "small")
        scores = Text(
            "{score} POINTS", self.rect.x + self.__margin__, SPRITE_SIZE * 1 + 24, "small")

        max_scores_text.rect.centerx = max_scores.rect.centerx = \
            scores_text.rect.centerx = scores.rect.centerx = self.rect.centerx

        self.__all_sprites__.add(
            max_scores_text, max_scores, scores, scores_text)
