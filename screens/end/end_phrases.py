from typing import Dict
from pygame import Rect, Surface
from components.button import Button
from consts import SPRITE_SIZE
from components import Text
from packages.core import ScreenPart
from consts import SCREEN_MARGIN, HEIGHT, WIDTH
from packages.events import CustomEventsTypes, custom_event, emit_event
from packages.inject import Injector
from stores.scores import ScoresStore
from stores.level import LevelStore


@Injector.inject(ScoresStore, "__scores__")
class EndPhrases(ScreenPart):
    __injected__: Dict[str, object]
    __scores__: ScoresStore

    def __init__(self, screen: Surface) -> None:
        super().__init__(screen)
        self.rect = Rect(SCREEN_MARGIN, SCREEN_MARGIN,
                         WIDTH - SCREEN_MARGIN * 2, HEIGHT - SCREEN_MARGIN * 2)

        self.__scores__ = self.__injected__.get("__scores__")

    def activate(self, text: str, *args, **kwargs) -> None:
        self.__create_text__(text)
        return super().activate(*args, **kwargs)

    def update(self, *args) -> None:
        data = {
            "score": self.__scores__.get_scores(),
            "max_score": self.__scores__.get_max_scores(),
        }
        return super().update(data, *args)

    def __create_text__(self, text: str) -> None:
        end_text = Text(text, 0, 0, "large")
        score_text = Text("Ваши очки: {score} POINTS", 0, 0)
        max_score_text = Text(
            "Максимальное количество очков на уровне: {max_score} POINTS", 0, 0)

        restart_text = Button("Выйти в меню", 0, 0, lambda: emit_event(
            custom_event(CustomEventsTypes.CHANGE_SCREEN, screen="menu")))

        score_text.rect.center = self.rect.center
        max_score_text.rect.center = self.rect.center
        end_text.rect.center = self.rect.center
        restart_text.rect.center = self.rect.center
        end_text.rect.y -= SPRITE_SIZE
        max_score_text.rect.y += SPRITE_SIZE
        restart_text.rect.y += SPRITE_SIZE * 1.5

        self.__all_sprites__.add(
            max_score_text, score_text, end_text, restart_text)
