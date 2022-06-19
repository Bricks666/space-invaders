from abc import ABC, abstractmethod
from typing import Final, List
from pygame import sprite

from .sprite import Sprite


collidable = sprite.Group()


class Collidable(Sprite, ABC):
    """
    Абстрактный класс сущности, которая может в коллизию

    Определяет метод для проверки коллизии и дает дает доступ ко всем объектам коллизии
    """
    __collidable__: Final[sprite.Group]
    """
    Хранит все объекты коллизии для текущего экрана
    """

    def __init__(self, *args: List[sprite.Group], **kwargs):
        super().__init__(*args, **kwargs)
        collidable.add(self)
        self.__collidable__ = collidable

    @abstractmethod
    def __collide__(self) -> bool:
        """
        Метод для проверки коллизии

        Должен быть реализован у потомков
        """
        return False

    @staticmethod
    def reset_collidable() -> None:
        """
        Дает способ очистить список всех объектов перед сменой сцены
        """
        collidable.empty()
