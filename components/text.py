from typing import Dict, Literal,  Union
import pygame
from consts import TEXT_COLOR


_FontSizes = Literal["small", "normal", "large"]
_ChangedType = Literal["color", "size", ""]


class Text(pygame.sprite.Sprite):
    fonts: Dict[_FontSizes, pygame.font.Font] = {}
    __message__: str
    __last_color__: pygame.Color
    __last_message__: str
    __size__: _FontSizes

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
        self.rect = self.image.get_rect().move(x, y)

    def update(self, message_data: Dict[str, Union[str, int, float]] = {}) -> None:
        message = self.__message__.format(**message_data)
        changed: _ChangedType = ""
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
            self.rect = rect

    def change_size(self, size: _FontSizes) -> None:
        self.__size__ = size

    def change_color(self, color: pygame.Color) -> None:
        self.__color__ = color
