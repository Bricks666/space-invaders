from typing import Dict
from pygame import Rect, Surface
from consts import SPRITE_SIZE
from components import Text
from packages.core import ScreenPart
from consts import SCREEN_MARGIN, HEIGHT, WIDTH
from packages.inject import Injector
from stores.scores import ScoresStore
from stores.level import LevelStore


@Injector.inject(ScoresStore, "__scores__")
@Injector.inject(LevelStore, "__level__")
class EndPhrases(ScreenPart):
    __injected__: Dict[str, object]
    __scores__: ScoresStore
    __level__: LevelStore
    __text__: str = ""

    def __init__(self, screen: Surface) -> None:
        super().__init__(screen)
        self.rect = Rect(SCREEN_MARGIN, SCREEN_MARGIN,
                         WIDTH - SCREEN_MARGIN, HEIGHT - SCREEN_MARGIN)

        self.__scores__ = self.__injected__.get("__scores__")
        self.__level__ = self.__injected__.get("__level__")

    def activate(self, text: str) -> None:
        self.__text__ = text
        self.__create_text__()
        return super().activate()

    def update(self) -> None:
        args = {
            "text": self.__text__,
            "score": self.__scores__.get_scores(),
            "max_score": self.__scores__.get_max_scores(),
            "level_name": self.__level__.get_current_level().level_name
        }
        return super().update(args)

    def __create_text__(self) -> None:
        end_text = Text("{text}", 0, 0, "large")
        score_text = Text("Ваши очки: {score} POINTS", 0, 0)
        max_score_text = Text(
            "Максимальное количество очков на уровне: {max_score} POINTS", 0, 0)
        level_name_text = Text("Уровень {level_name}", 0, 0)
        restart_text = Text("Чтобы начать уровень заново, нажмите R", 0, 0)

        score_text.rect.center = self.rect.center
        max_score_text.rect.center = self.rect.center
        level_name_text.rect.center = self.rect.center
        end_text.rect.center = self.rect.center
        restart_text.rect.center = self.rect.center
        end_text.rect.y -= SPRITE_SIZE
        max_score_text.rect.y += SPRITE_SIZE
        restart_text.rect.y += SPRITE_SIZE * 1.5
        level_name_text.rect.y = self.rect.y

        self.__all_sprites__.add(
            max_score_text, score_text, level_name_text, end_text, restart_text)
