from abc import abstractmethod
from enum import Enum
from typing import Final, final
from packages.core.collidable import Collidable
from .game_object import GameObject


@final
class Direction(Enum):
    LEFT: Final[int] = -1
    RIGHT: Final[int] = 1
    TOP: Final[int] = -1
    BOTTOM: Final[int] = 1


class Entity(GameObject):
    """
    Интерфейс для сущности
    """

    def fire(self) -> None:
        """
        Метод для стрельбы

        Должен быть реализован у потомка
        """
        pass

    def move(self) -> None:
        """
        Метод для передвижения сущности

        Должен быть реализован у потомка
        """
        pass
