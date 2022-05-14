
from enum import Enum


class Direction(Enum):
    LEFT = -1
    RIGHT = 1
    TOP = -1
    BOTTOM = 1


SPRITE_SIZE = 48


class BulletType(Enum):
    HERO = 0
    ENEMY = 1


FIRE_COOLDOWN = 1

WIDTH: int = 12 * SPRITE_SIZE
HEIGHT: int = 5 * SPRITE_SIZE
FPS: int = 12
RUNNING: bool = False

STEP = 2

class Entities(Enum):
  HERO = "0"
  ENEMY = "1"
