from typing import Dict, Literal,  Union
import pygame
from consts import TEXT_COLOR


_FontSizes = Literal["small", "normal", "large"]


class Text(pygame.sprite.Sprite):
    fonts: Dict[_FontSizes, pygame.font.Font] = {}
    message: str
    __last_message__: str
    __size__: _FontSizes

    def __init__(self, message: str, x: float, y: float, size: _FontSizes = "normal") -> None:
        super().__init__()

        self.color = TEXT_COLOR
        self.message = message
        self.__last_message__ = ""
        self.__size__ = size

        self.image = self.fonts.get(self.__size__).render(
            message, True, self.color)
        self.rect = self.image.get_rect().move(x, y)

    def update(self, message_data: Dict[str, Union[str, int, float]] = {}) -> None:
        message = self.message.format(**message_data)
        if message != self.__last_message__:
            self.__last_message__ = message

            self.image = self.fonts.get(self.__size__).render(
                message, True, self.color)

            rect = self.image.get_rect()
            rect.centerx = self.rect.centerx
            rect.y = self.rect.y
            self.rect = rect

    def change_size(self, size: _FontSizes) -> None:
        self.__size__ = size
