from abc import ABC, abstractmethod
from typing import Final, List
from pygame import sprite


collidable = sprite.Group()


class Collidable(sprite.Sprite, ABC):
    __collidable__: Final[sprite.Group]

    def __init__(self, *args: List[sprite.Group], **kwargs):
        super().__init__(*args, **kwargs)
        collidable.add(self)
        self.__collidable__ = collidable

    @abstractmethod
    def __collide__(self) -> bool:
        return False

    @staticmethod
    def reset_collidable() -> None:
        collidable.empty()


class Entity:
    """ Описать класс Entity, он должен быть базовым для героя, врага """
    __musics__: bool
    __images__: bool
    pass
