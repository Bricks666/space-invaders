from abc import ABCMeta, abstractmethod
import pygame


class Scene(metaclass=ABCMeta):
    __all_sprites__: pygame.sprite.Group

    def __init__(self, screen: pygame.Surface, all_sprites: pygame.sprite.Group):
        self._screen_ = screen
        self.__all_sprites__ = all_sprites

    @abstractmethod
    def draw(self):
        self.__all_sprites__.draw(self._screen_)

    @abstractmethod
    def update(self):
        self.__all_sprites__.update()
