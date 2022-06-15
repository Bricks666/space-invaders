
from enum import Enum
from typing import Tuple


class Direction(Enum):
    LEFT = -1
    RIGHT = 1
    TOP = -1
    BOTTOM = 1


SPRITE_SIZE: int = 64
BULLET_SIZE: Tuple[int, int] = (SPRITE_SIZE / 100 * 7, SPRITE_SIZE / 100 * 52)


class BulletType(Enum):
    HERO = -1
    ENEMY = 1


FIRE_COOLDOWN: float = 1

LEVEL_WIDTH: int = 12 * SPRITE_SIZE
LEVEL_HEIGHT: int = 14 * SPRITE_SIZE

SCREEN_MARGIN: int = 50
ASIDE_BAR_WIDTH: int = SPRITE_SIZE * 4 + 12

WIDTH: int = LEVEL_WIDTH + ASIDE_BAR_WIDTH + SCREEN_MARGIN * 2
HEIGHT: int = LEVEL_HEIGHT + SCREEN_MARGIN * 2
FPS: int = 60
BORDER_WIDTH: int = 5


class Entities(Enum):
    HERO = "0"
    ENEMY = "1"


STEP = 4

UNICODE_NUMBER_OFFSET = 48
