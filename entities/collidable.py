from abc import ABCMeta, abstractmethod
import pygame


collidable = pygame.sprite.Group()


class Collidable(pygame.sprite.Sprite, metaclass=ABCMeta):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        collidable.add(self)
        self.__collidable__ = collidable

    @abstractmethod
    def __collide__(self) -> bool:
        return False
