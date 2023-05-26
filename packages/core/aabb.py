from abc import ABC
from typing import Tuple
from .math import Vector


Coordinates = Tuple[float, float]

class AABB(ABC):
    _start: Vector
    _end: Vector
