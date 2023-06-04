import math as m
from typing import Any, Union, NamedTuple, Self


class VectorLike(NamedTuple):
    x: float = 0
    y: float = x


class Vector:
    x: float
    y: float

    __isvector = True

    def __init__(self, x: float = 0, y: float = 0) -> None:
        super().__init__()
        self.x = x
        self.y = y

    def add(self, vector: Union['Vector', VectorLike]) -> Self:
        self.x += vector.x
        self.y += vector.y
        return self

    def sum(self, vector: Union['Vector', VectorLike]) -> 'Vector':
        return Vector(self.x + vector.x, self.y + vector.y)

    def set(self, vector: Union['Vector', VectorLike]) -> Self:
        self.x = vector.x
        self.y = vector.y

    def __len__(self):
        return m.sqrt(m.pow(self.x, 2) + m.pow(self.y, 2))

    def __eq__(self, __value: Union['Vector', VectorLike]) -> bool:
        if not isinstance(__value, Vector) and not isinstance(__value, VectorLike):
            return False

        return self.x == __value.x and self.y == __value.y

    def __ne__(self, __value: Union['Vector', VectorLike]) -> bool:
        return not self.__eq__(__value)

    def __instancecheck__(self, __instance: Union[Any, 'Vector']) -> bool:
        return hasattr(__instance, '__isvector') and __instance.__isvector

    def __str__(self) -> str:
        return f"<{self.__class__.__name__}({self.x},{self.y})>"

    @staticmethod
    def copy(vector: 'Vector') -> 'Vector':
        return Vector(vector.x, vector.y)


ZERO_VECTOR = Vector()
ONE_VECTOR = Vector(1, 1)
