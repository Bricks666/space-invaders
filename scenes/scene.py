from abc import ABCMeta, abstractmethod
import pygame

from entities.sprite import inject_all_sprites


@inject_all_sprites
class Scene(metaclass=ABCMeta):
    __all_sprites__: pygame.sprite.Group

    def __init__(self, screen: pygame.Surface):
        self._screen = screen
        pass

    def draw(self):
        self.__all_sprites__.draw(self._screen)

    def update(self):
        self.__all_sprites__.update()

    @abstractmethod
    def select(self):
        pass

    @abstractmethod
    def unselect(self):
        self.__all_sprites__.empty()
