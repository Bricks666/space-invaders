from abc import ABCMeta, abstractmethod
import pygame
from packages.core import get_all_sprites


class Scene(metaclass=ABCMeta):
    __all_sprites__: pygame.sprite.Group

    def __init__(self, screen: pygame.Surface) -> None:
        self._screen_ = screen
        self.__all_sprites__ = get_all_sprites()

    @abstractmethod
    def draw(self) -> None:
        self.__all_sprites__.draw(self._screen_)

    @abstractmethod
    def update(self) -> None:
        self.__all_sprites__.update()
