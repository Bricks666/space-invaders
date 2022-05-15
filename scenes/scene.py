from abc import ABCMeta, abstractmethod
import pygame


class Scene(metaclass=ABCMeta):
    __all_sprites__: pygame.sprite.Group

    def __init__(self, screen: pygame.Surface):
        self._screen_ = screen

    @abstractmethod
    def draw(self):
        self.__all_sprites__.draw(self._screen_)

    @abstractmethod
    def update(self):
        self.__all_sprites__.update()
