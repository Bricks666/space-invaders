from typing import TypeVar
import pygame



all_sprites = pygame.sprite.Group()


class Sprite(pygame.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        all_sprites.add(self)


T = TypeVar("T", bound=object)


def inject_all_sprites(cls: T) -> T:
    orig_init = cls.__init__

    def __init__(self, *args, **kwargs):
        orig_init(self, *args, **kwargs)
        self.__all_sprites__ = all_sprites

    cls.__init__ = __init__

    return cls
