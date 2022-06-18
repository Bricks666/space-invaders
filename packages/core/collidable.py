from abc import ABC, abstractmethod
from typing import Final, List
from pygame import sprite

from packages.core.sprite import Sprite


collidable = sprite.Group()


class Collidable(Sprite, ABC):
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
