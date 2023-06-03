from abc import ABC
from typing import overload, Self, Union
from .vector import Vector, ZERO_VECTOR, Coordinates


class AABB(ABC):
    __start: Vector
    __end: Vector

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, end: Vector) -> None:
        ...

    @overload
    def __init__(self, start: Vector, end: Vector) -> None:
        ...

    def __init__(self, *args) -> None:
        super().__init__()

        if len(args) == 0:
            self.__start = Vector.copy(ZERO_VECTOR)
            self.__end = Vector.copy(ZERO_VECTOR)
        elif len(args) == 1:
            self.__start = Vector.copy(ZERO_VECTOR)
            self.__end = args[0]
        else:
            self.__start = args[0]
            self.__end = args[1]

    @property
    def width(self) -> float:
        return abs(self.__end.x - self.__start.x)

    @width.setter
    def width(self, width: float) -> float:
        self.__end.x = self.__start.x + width
        return width

    @property
    def height(self) -> float:
        return abs(self.__end.y - self.__start.y)

    @height.setter
    def height(self, height: float) -> float:
        self.__end.y = self.__start.y + height
        return height

    @property
    def start_x(self) -> float:
        return self.__start.x

    @start_x.setter
    def start_x(self, x: float) -> float:
        self.__start.x = x
        return x

    @property
    def center_x(self) -> float:
        return (self.start_x + self.end_x) / 2

    @center_x.setter
    def center_x(self, x: float) -> float:
        width = self.width
        half_width = width / 2
        self.__start.x = x - half_width
        self.__end.x = x + half_width
        return x

    @property
    def end_x(self) -> float:
        return self.__end.x

    @end_x.setter
    def end_x(self, x: float) -> float:
        self.__end.x = x
        return x

    @property
    def start_y(self) -> float:
        return self.__start.y

    @start_y.setter
    def start_y(self, y: float) -> float:
        self.__start.y = y
        return y

    @property
    def center_y(self) -> float:
        return (self.start_y + self.end_y) / 2

    @center_y.setter
    def center_y(self, y: float) -> float:
        height = self.height
        half_height = height / 2
        self.__start.y = y - half_height
        self.__end.y = y + half_height
        return y

    @property
    def end_y(self) -> float:
        return self.__end.y

    @end_y.setter
    def end_y(self, y: float) -> float:
        self.__end.y = y
        return y

    def move_on(self, coords: Union[Coordinates, Vector]) -> Self:
        self.__start.add(coords)
        self.__end.add(coords)

        return self

    def move_to(self, coords: Union[Coordinates, Vector]) -> Self:
        width = self.width
        height = self.height

        self.__start.set(coords)
        self.__end.set(Coordinates(coords.x + width, coords.y + height))

        return self
