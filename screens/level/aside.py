from pygame import Surface, Rect
from consts import ASIDE_BAR_WIDTH, BORDER_WIDTH, HEIGHT, LEVEL_WIDTH, SCREEN_MARGIN, SPRITE_SIZE
from components import Text, Button
from packages.core import ScreenPart, Group
from packages.events import CustomEventsTypes, custom_event, emit_event
from .live import Live
from stores.lives import LivesStore
from packages.inject import Injector
from stores.scores import ScoresStore


@Injector.inject(ScoresStore, "__scores__")
@Injector.inject(LivesStore, "__lives__")
class Aside(ScreenPart):
    """
    Боковая панель во время игры
    """
    __scores__: ScoresStore
    """
    Хранилище очков
    """
    __lives__: LivesStore
    """
    Хранилище жизней
    """
    __margin__: float = SPRITE_SIZE / 2
    """
    Отступ между жизнями
    """
    __live_sprites__: Group[Live]
    """
    Отображаемые жизни
    """

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
        """
        Получение актуальных данных об очках
        """
        return super().update(score)

    def activate(self, *args, **kwargs) -> None:
        self.__create_text__()
        self.__create_lives__()
        self.__create_button__()
        return super().activate(*args, **kwargs)

    def inactivate(self, *args, **kwargs) -> None:
        self.__live_sprites__.empty()
        return super().inactivate(*args, **kwargs)

    def __validate_lives__(self) -> None:
        """
        Проверка правильности количественного отображения жизней

        Если нет, то создается правильное количество
        """
        live_sprites_count = len(self.__live_sprites__)
        lives_count = self.__lives__.get_lives()

        if lives_count != live_sprites_count:
            for live in self.__live_sprites__:
                """
                Проще уничтожить все и создать заново, чем вычислять, что нужно сделать
                """
                live.kill()
            self.__create_lives__()

    def __create_lives__(self) -> None:
        """
        Создание значков жизней
        """
        lives_count = self.__lives__.get_lives()

        def x(i): return self.rect.x + self.__margin__ + SPRITE_SIZE * i
        y = self.rect.bottom - SPRITE_SIZE * 2

        lives = []
        for i in range(lives_count):
            lives.append(Live(x(i), y))
        self.__all_sprites__.add(lives)
        self.__live_sprites__.add(lives)

    def __create_text__(self) -> None:
        """
        Создание текста
        """
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

    def __create_button__(self) -> None:
        """
        Создание кнопок
        """
        menu = Button("Меню", 0, 0, lambda: emit_event(
            custom_event(CustomEventsTypes.CHANGE_SCREEN, screen="menu")), "small")
        levels = Button("Уровни", 0, 0, lambda: emit_event(
            custom_event(CustomEventsTypes.CHANGE_SCREEN, screen="levels")), "small")

        menu.rect.y = levels.rect.y = self.rect.bottom - SPRITE_SIZE * 0.5
        left = self.rect.left
        right = self.rect.right
        center_y = self.rect.centerx

        menu.rect.centerx = (left + center_y) / 2
        levels.rect.centerx = (right + center_y) / 2

        self.__all_sprites__.add(menu, levels)
