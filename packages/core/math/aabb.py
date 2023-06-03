from abc import ABC
from typing import overload, Self, Union, NamedTuple
from enum import Enum
from .vector import Vector, ZERO_VECTOR, VectorLike
from ..base.event_emitter import EventEmitter


class Sizes(NamedTuple):
    width: float = 0
    height: float = 0


class AABBEvents(Enum):
    resize = 'resize'


class AABB(ABC, EventEmitter):
    _start: Vector
    _end: Vector

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
        super(ABC, self).__init__()
        super(EventEmitter, self).__init__()

        if len(args) == 0:
            self._start = Vector.copy(ZERO_VECTOR)
            self._end = Vector.copy(ZERO_VECTOR)
        elif len(args) == 1:
            self._start = Vector.copy(ZERO_VECTOR)
            self._end = args[0]
        else:
            self._start = args[0]
            self._end = args[1]

    @property
    def sizes(self) -> Sizes:
        return Sizes(self.width, self.height)

    @property
    def width(self) -> float:
        return abs(self._end.x - self._start.x)

    @width.setter
    def width(self, __value: float) -> float:
        self._end.x = self._start.x + __value
        return __value

    @property
    def height(self) -> float:
        return abs(self._end.y - self._start.y)

    @height.setter
    def height(self, __value: float) -> float:
        self._end.y = self._start.y + __value
        return __value

    @property
    def start_x(self) -> float:
        return self._start.x

    @start_x.setter
    def start_x(self, __value: float) -> float:
        self._start.x = __value
        return __value

    @property
    def center_x(self) -> float:
        return (self.start_x + self.end_x) / 2

    @center_x.setter
    def center_x(self, __value: float) -> float:
        width = self.width
        half_width = width / 2
        self._start.x = __value - half_width
        self._end.x = __value + half_width
        return __value

    @property
    def end_x(self) -> float:
        return self._end.x

    @end_x.setter
    def end_x(self, __value: float) -> float:
        self._end.x = __value
        return __value

    @property
    def start_y(self) -> float:
        return self._start.y

    @start_y.setter
    def start_y(self, __value: float) -> float:
        self._start.y = __value
        return __value

    @property
    def center_y(self) -> float:
        return (self.start_y + self.end_y) / 2

    @center_y.setter
    def center_y(self, __value: float) -> float:
        height = self.height
        half_height = height / 2
        self._start.y = __value - half_height
        self._end.y = __value + half_height
        return __value

    @property
    def end_y(self) -> float:
        return self._end.y

    @end_y.setter
    def end_y(self, __value: float) -> float:
        self._end.y = __value
        return __value

    def move_on(self, coords: Union[VectorLike, Vector]) -> Self:
        self._start.add(coords)
        self._end.add(coords)

        return self

    def move_to(self, coords: Union[VectorLike, Vector]) -> Self:
        width = self.width
        height = self.height

        self._start.set(coords)
        self._end.set(VectorLike(coords.x + width, coords.y + height))

        return self
