from typing import Callable, Dict, Union
from .text import Text, _FontSizes
from consts.colors import BORDER_COLOR, TEXT_COLOR
from pygame import SYSTEM_CURSOR_HAND, mouse, cursors, mixer, time

_THandler = Callable[['Button'], None]


class Button(Text):
    """
    Кнопка

    Класс описывает базовую текстовую кнопку,
    реагирующую на нажатие, наведение и уход курсора
    """
    __hovering__: bool = False
    """
    Состояние наведение курсора на кнопку
    """
    __sounds__: Dict[str, mixer.Sound] = {}
    """
    Звуки кнопки
    """
    on_click: _THandler
    """
    Пользовательский обработчик нажатия
    """

    def __init__(self, message: str, x: float, y: float, on_click: _THandler, size: _FontSizes = "normal") -> None:
        super().__init__(message, x, y, size)
        self.on_click = on_click

    def update(self, message_data: Dict[str, Union[str, int, float]] = {}) -> None:
        mouse_position = mouse.get_pos()
        if self.rect.collidepoint(mouse_position):
            if not self.__hovering__:
                self.__hovering__ = True
                self.__on_hover__()

            pressed = mouse.get_pressed()
            if pressed[0]:
                """
                Проверка, нажата ли ЛКМ
                """
                self.__on_click__()
                self.__on_leave__()

        elif self.__hovering__:
            self.__hovering__ = False
            self.__on_leave__()

        return super().update(message_data)

    def __on_hover__(self) -> None:
        self.change_color(BORDER_COLOR)
        mouse.set_cursor(SYSTEM_CURSOR_HAND)
        """
        Курсор изменяется на изображение руки,
        чтобы показать пользователю, что это кнопка
        """

    def __on_leave__(self) -> None:
        self.change_color(TEXT_COLOR)
        mouse.set_cursor(cursors.tri_left)
        """
        Курсор нужно менять, когда пользователь больше не наводит
        """

    def __on_click__(self) -> None:
        self.__sounds__.get("click").play(fade_ms=300, maxtime=300)
        time.wait(300)
        """
        Эмуляция прогрузки аркадного автомата и плавной смены сцен
        """
        self.on_click()

    @classmethod
    def set_sound(cls, name: str, sound: mixer.Sound) -> None:
        cls.__sounds__.update([[name, sound]])
