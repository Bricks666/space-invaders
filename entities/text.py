from typing import Dict,  Union
import pygame
from consts import TEXT_COLOR


class Text(pygame.sprite.Sprite):
    font: pygame.font.Font
    message: str
    __last_message__: str

    def __init__(self, message: str, x: float, y: float) -> None:
        super().__init__()
        self.color = TEXT_COLOR
        self.message = message
        self.__last_message__ = ""
        self.image = self.font.render(
            message, True, self.color)
        self.rect = self.image.get_rect().move(x, y)

    def update(self, message_data: Dict[str, Union[str, int, float]] = {}) -> None:
        message = self.message.format(**message_data)
        if message != self.__last_message__:
            self.__last_message__ = message
            self.image = self.font.render(
                message, True, self.color)
            rect = self.image.get_rect()
            rect.centerx = self.rect.centerx
            rect.y = self.rect.y
            self.rect = rect
