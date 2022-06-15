from abc import ABCMeta, abstractmethod
import pygame

sprites = pygame.sprite.Group()
collidable = pygame.sprite.Group()


class Sprite(pygame.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        sprites.add(self)
        print(self)


class Collidable(Sprite, metaclass=ABCMeta):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        collidable.add(self)
        self.__collidable__ = collidable

    @abstractmethod
    def __collide__(self) -> bool:
        return False


def get_all_sprites() -> pygame.sprite.Group:
    return sprites


def get_all_sprites_by_class(cls: object) -> pygame.sprite.Group:
    cls_sprites = pygame.sprite.Group()
    for sprite in sprites:
        if isinstance(sprite, cls):
            cls_sprites.add(sprite)

    return cls_sprites


def reset_sprites() -> None:
    sprites.empty()
    collidable.empty()
