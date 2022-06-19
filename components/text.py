from typing import Dict, Literal,  Union
import pygame
from consts import TEXT_COLOR


_FontSizes = Literal["small", "normal", "large"]
"""
Доступные размеры шрифта
"""
_ChangedType = Literal["color", "size", ""]
"""
Описывает варианты, которые изменились между отрисовками

Нужно для оптимизации рендера компонента
"""


class Text(pygame.sprite.Sprite):
    """
    Текст

    Описывает однострочный текст, выводимый на экран
    """
    fonts: Dict[_FontSizes, pygame.font.Font] = {}
    """
    Шрифты, доступные для отрисовки

    Есть малый, средний и большой. Средний используется по умолчанию
    """
    __message__: str
    """
    Шаблонное сообщение компонента
    """
    __last_color__: pygame.Color
    """
    Последний используемый цвет, нужно для избежания лишних рендеров
    """
    __last_message__: str
    """
    Текст, который был отрендерен последним, нужно для избежания лишних рендеров
    """
    __size__: _FontSizes
    """
    Текущий размер шрифта
    """

    def __init__(self, message: str, x: float, y: float,
                 size: _FontSizes = "normal", color: pygame.Color = TEXT_COLOR) -> None:
        super().__init__()

        self.__color__ = color
        self.__last_color__ = color
        self.__message__ = message
        self.__last_message__ = ""
        self.__size__ = size

        self.image = self.fonts.get(self.__size__).render(
            message, True, self.__color__)
        """
        Требуется для получения начального изображения и расстановки компонента
        """
        self.rect = self.image.get_rect().move(x, y)

    def update(self, message_data: Dict[str, Union[str, int, float]] = {}) -> None:
        """
        Метод для обновления состояния компонента

        Если передана шаблонная строка,
        то ожидает на вход словарь с данными для ее заполнения
        """
        message = self.__message__.format(**message_data)
        changed: _ChangedType = ""
        """
        Индикатор, что цвет или текст изменился
        """
        if self.__color__ != self.__last_color__:
            self.__last_color__ = self.__color__
            changed = "color"
        if message != self.__last_message__:
            self.__last_message__ = message
            changed = "size"
        if changed:
            self.image = self.fonts.get(self.__size__).render(
                message, True, self.__color__)
        if changed == "size":
            rect = self.image.get_rect()
            rect.centerx = self.rect.centerx
            rect.y = self.rect.y
            """
            Выравнивание текста, если было изменено сообщение
            """
            self.rect = rect

    def change_size(self, size: _FontSizes) -> None:
        """
        Метод для изменения шрифта
        """
        self.__size__ = size

    def change_color(self, color: pygame.Color) -> None:
        """
        Метод для изменения цвета
        """
        self.__color__ = color

    @staticmethod
    def get_font_height(text: 'Text') -> int:
        """
        Метод для получения размера шрифта по размеру
        """
        font = text.fonts.get(text.__size__)
        return font.get_height()
