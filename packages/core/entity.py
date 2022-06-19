from abc import abstractmethod
from enum import Enum
from typing import Final, final
from packages.core.collidable import Collidable


@final
class Direction(Enum):
    LEFT: Final[int] = -1
    RIGHT: Final[int] = 1
    TOP: Final[int] = -1
    BOTTOM: Final[int] = 1


class Entity(Collidable):
    """
    Интерфейс для сущности
    """
    __velocity__: float = 0
    """
    Векторная скорость перемещения сущности
    """

    @abstractmethod
    def fire(self) -> None:
        """
        Метод для стрельбы

        Должен быть реализован у потомка
        """
        pass

    @abstractmethod
    def move(self) -> None:
        """
        Метод для передвижения сущности

        Должен быть реализован у потомка
        """
        pass
