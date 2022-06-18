from abc import abstractmethod
from enum import Enum
from pygame import Surface, mixer
from typing import Dict, Final, final
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
    __speed__: float = 0

    @abstractmethod
    def fire(self) -> None:
        """
        Должен быть реализован у потомка
        """
        pass

    @abstractmethod
    def move(self) -> None:
        """
        Должен быть реализован у потомка
        """
        pass