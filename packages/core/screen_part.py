from abc import ABC
from pygame import Surface, sprite


class ScreenPart(ABC):
    __all_sprites__: sprite.Group
    __screen__: Surface

    def __init__(self, screen: Surface) -> None:
        self.__all_sprites__ = sprite.Group()
        self.__screen__ = screen

    def update(self, *args) -> None:
        self.__all_sprites__.update(*args)

    def draw(self, *args) -> None:
        self.__all_sprites__.draw(self.__screen__, *args)

    def select(self, *args) -> None:
        pass

    def unselect(self) -> None:
        self.__all_sprites__.empty()
