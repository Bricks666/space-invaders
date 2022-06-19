from pygame import Rect, Surface
from components.button import Button
from consts import SPRITE_SIZE
from components import Text
from consts.sizes import CONTENT_HEIGHT, CONTENT_WIDTH, SCREEN_MARGIN
from packages.core import ScreenPart
from packages.events import CustomEventsTypes, custom_event, emit_event
from packages.inject import Injector
from stores.scores import ScoresStore
from stores.level import LevelStore


@Injector.inject(ScoresStore, "__scores__")
class EndPhrases(ScreenPart):
    """
    Текст на конечном экране
    """
    __scores__: ScoresStore
    """
    Хранилище очков
    """

    def __init__(self, screen: Surface) -> None:
        rect = Rect(SCREEN_MARGIN, SCREEN_MARGIN,
                    CONTENT_WIDTH, CONTENT_HEIGHT)
        super().__init__(screen, rect)

    def activate(self, text: str, *args, **kwargs) -> None:
        self.__create_text__(text)
        return super().activate(*args, **kwargs)

    def update(self, *args) -> None:
        data = {
            "score": self.__scores__.get_scores(),
            "max_score": self.__scores__.get_max_scores(),
        }
        """
        Получение актуальных данных об очках завершенного уровня
        """
        return super().update(data, *args)

    def __create_text__(self, text: str) -> None:
        end = Text(text, 0, 0, "large")
        score = Text("Ваши очки: {score} POINTS", 0, 0)
        max_score = Text(
            "Максимальное количество очков на уровне: {max_score} POINTS", 0, 0)

        menu = Button("Выйти в меню", 0, 0, lambda: emit_event(
            custom_event(CustomEventsTypes.CHANGE_SCREEN, screen="menu")))

        score.rect.center = self.rect.center
        max_score.rect.center = self.rect.center
        end.rect.center = self.rect.center
        menu.rect.center = self.rect.center
        end.rect.y -= SPRITE_SIZE
        max_score.rect.y += SPRITE_SIZE
        menu.rect.y = self.rect.bottom - SPRITE_SIZE

        self.__all_sprites__.add(
            max_score, score, end, menu)
