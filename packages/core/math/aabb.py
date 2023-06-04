from abc import ABC
from typing import overload, Self, Union, NamedTuple, ParamSpec, Callable, TypeVar
from .vector import Vector, ZERO_VECTOR, VectorLike


class Sizes(NamedTuple):
    width: float = 0
    height: float = 0


_P = ParamSpec('_P')
_R = TypeVar('_R')


def _observe_mutation():
    def decorator(func: Callable[_P, _R]) -> Callable[_P, _R]:
        def wrapper(self: 'AABB', *args: _P.args, **kwargs: _P.kwargs) -> _R:
            start = Vector.copy(self._start)
            end = Vector.copy(self._end)

            result = func(self, *args, **kwargs)

            if start != self._start or end != self._end:
                self._mutated = True

            return result

        return wrapper

    return decorator


class AABB(ABC):
    _start: Vector
    _end: Vector
    _mutated: bool = False

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, width: float, height: float) -> None:
        ...

    @overload
    def __init__(self, x: float, y: float, width: float, height: float) -> None:
        ...

    def __init__(self, *args, **kwargs) -> None:
        super().__init__()

        if len(args) == 0:
            self._start = Vector.copy(ZERO_VECTOR)
            self._end = Vector.copy(ZERO_VECTOR)
        elif len(args) == 2:
            width, height = args
            self._start = Vector.copy(ZERO_VECTOR)
            self._end = self._start.sum(VectorLike(width, height))
        else:
            x, y, width, height = args
            self._start = Vector(x, y)
            self._end = self._start.sum(VectorLike(width, height))

    @property
    def sizes(self) -> Sizes:
        return Sizes(self.width, self.height)

    @property
    def width(self) -> float:
        return abs(self._end.x - self._start.x)

    @width.setter
    @_observe_mutation()
    def width(self, __value: float) -> float:
        self._end.x = self._start.x + __value
        return __value

    @property
    def height(self) -> float:
        return abs(self._end.y - self._start.y)

    @height.setter
    @_observe_mutation()
    def height(self, __value: float) -> float:
        self._end.y = self._start.y + __value
        return __value

    @property
    def start_x(self) -> float:
        return self._start.x

    @start_x.setter
    @_observe_mutation()
    def start_x(self, __value: float) -> float:
        self._start.x = __value
        return __value

    @property
    def center_x(self) -> float:
        return (self.start_x + self.end_x) / 2

    @center_x.setter
    @_observe_mutation()
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
    @_observe_mutation()
    def end_x(self, __value: float) -> float:
        self._end.x = __value
        return __value

    @property
    def start_y(self) -> float:
        return self._start.y

    @start_y.setter
    @_observe_mutation()
    def start_y(self, __value: float) -> float:
        self._start.y = __value
        return __value

    @property
    def center_y(self) -> float:
        return (self.start_y + self.end_y) / 2

    @center_y.setter
    @_observe_mutation()
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
    @_observe_mutation()
    def end_y(self, __value: float) -> float:
        self._end.y = __value
        return __value

    @_observe_mutation()
    def move_on(self, coords: Union[VectorLike, Vector]) -> Self:
        self._start = self._start.add(coords)
        self._end = self._end.add(coords)

        return self

    @_observe_mutation()
    def move_to(self, coords: Union[VectorLike, Vector]) -> Self:
        width = self.width
        height = self.height

        self._start.set(coords)
        self._end.set(VectorLike(coords.x + width, coords.y + height))

        return self
