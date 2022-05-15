
from enum import Enum


class Direction(Enum):
    LEFT = -1
    RIGHT = 1
    TOP = -1
    BOTTOM = 1


SPRITE_SIZE: int = 32


class BulletType(Enum):
    HERO = -1
    ENEMY = 1


FIRE_COOLDOWN: float = 0.5

WIDTH: int = 12 * SPRITE_SIZE
HEIGHT: int = 14 * SPRITE_SIZE
FPS: int = 12
RUNNING: bool = False


class Entities(Enum):
    HERO = "0"
    ENEMY = "1"


STEP: float = 3.5
