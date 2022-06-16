from enum import Enum
from typing import Final, Tuple


class Direction(Enum):
    LEFT: Final[int] = -1
    RIGHT: Final[int] = 1
    TOP: Final[int] = -1
    BOTTOM: Final[int] = 1


SPRITE_SIZE: Final[int] = 64
BULLET_SIZE: Final[Tuple[int, int]] = (
    SPRITE_SIZE / 100 * 7, SPRITE_SIZE / 100 * 52)


class BulletType(Enum):
    HERO: Final[int] = -1
    ENEMY: Final[int] = 1


FIRE_COOLDOWN: Final[float] = 1

LEVEL_WIDTH: Final[int] = 12 * SPRITE_SIZE
LEVEL_HEIGHT: Final[int] = 14 * SPRITE_SIZE

SCREEN_MARGIN: Final[int] = 50
ASIDE_BAR_WIDTH: Final[int] = SPRITE_SIZE * 4 + 12

WIDTH: Final[int] = LEVEL_WIDTH + ASIDE_BAR_WIDTH + SCREEN_MARGIN * 2
HEIGHT: Final[int] = LEVEL_HEIGHT + SCREEN_MARGIN * 2
FPS: Final[int] = 60
BORDER_WIDTH: Final[int] = 5


class Entities(Enum):
    HERO: Final[str] = "0"
    ENEMY: Final[str] = "1"


STEP: Final[int] = 4

UNICODE_NUMBER_OFFSET: Final[int] = 48

GAME_NAME: Final[str] = "Space Invaders"
